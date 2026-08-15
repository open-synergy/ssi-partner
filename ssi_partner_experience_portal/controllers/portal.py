# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo.http import request, route

from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import CustomerPortal

_logger = logging.getLogger(__name__)


class CustomerPortalExtended(CustomerPortal):
    """Portal routes for a partner's academic and professional history.

    Extends the core ``CustomerPortal`` controller with list/edit/
    remove routes for ``portal_partner_academic`` and
    ``portal_partner_experience``, mirroring the ``/my/*`` pattern
    already used by other portal document types.
    """

    @route(["/my/academics"], type="http", auth="user", website=True, methods=["GET"])
    def academics(self):
        """Render the list of the current user's academic experiences.

        :return: rendered ``portal_my_academics`` page listing every
            ``portal_partner_academic`` record owned by the logged-in
            user's partner
        """
        values = self._prepare_portal_layout_values()
        values["get_error"] = portal.get_error
        values["academic_ids"] = request.env["portal_partner_academic"].search(
            [("partner_id", "=", request.env.user.partner_id.id)]
        )

        return request.render(
            "ssi_partner_experience_portal.portal_my_academics",
            values,
            headers={"X-Frame-Options": "DENY"},
        )

    @route(
        ["/my/academic", "/my/academic/<int:id>"],
        type="http",
        auth="user",
        website=True,
        methods=["GET", "POST"],
    )
    def academic(self, **post):
        """Show or save one academic experience record for the portal.

        On ``GET`` renders the create/edit form (empty when ``id`` is
        absent, pre-filled when present). On ``POST`` validates the
        submitted values, creates or writes the
        ``portal_partner_academic`` record for the current user's
        partner, then redirects to ``/my/academics``; on validation
        failure the form is re-rendered with ``error_message`` set.

        :param post: form payload (``id``, ``location``,
            ``date_start``, ``expire``, ``date_end``, ``diploma``,
            ``gpa``, ``activities``, ``note``,
            ``partner_address``, ``education_level``,
            ``field_of_study``)
        :return: rendered form page, or a redirect on success
        """
        id = post.get("id")
        partner_obj = request.env["res.partner"].sudo()
        academic_obj = request.env["portal_partner_academic"]
        education_level_obj = request.env["partner.formal_education_level"]
        field_of_study_obj = request.env["partner.field_of_study"]
        values = self._prepare_portal_layout_values()
        error_messages = []
        values.update(
            {
                "error_message": "",
                "partner_address_ids": partner_obj.search([("is_company", "=", True)]),
                "education_level_ids": education_level_obj.search([]),
                "field_of_study_ids": field_of_study_obj.search([]),
                "current_academic_id": academic_obj,
            }
        )
        current_academic_id = academic_obj
        if id:
            id = int(id)
            current_academic_id = academic_obj.search([("id", "=", id)])
            values.update(
                {
                    "current_academic_id": current_academic_id,
                }
            )

        if request.httprequest.method == "POST":
            academic_vals = {
                "partner_id": request.env.user.partner_id.id,
                "location": post.get("location"),
                "date_start": post.get("date_start") or False,
                "expire": post.get("expire"),
                "date_end": post.get("date_end") or False,
                "diploma": post.get("diploma"),
                "gpa": post.get("gpa"),
                "activities": post.get("activities"),
                "note": post.get("note"),
            }
            if post.get("partner_address"):
                partner_address_id = partner_obj.sudo().search(
                    [("id", "=", int(post.get("partner_address", "0")))]
                )
                if not partner_address_id:
                    error_messages.append("Institution not found.")
                academic_vals.update(
                    {
                        "partner_address_id": partner_address_id.id,
                    }
                )
            if post.get("education_level"):
                education_level_id = education_level_obj.sudo().search(
                    [("id", "=", int(post.get("education_level", "0")))]
                )
                if not education_level_id:
                    error_messages.append("Education level not found.")
                academic_vals.update(
                    {
                        "education_level_id": education_level_id.id,
                    }
                )
            if post.get("field_of_study"):
                field_of_study_id = field_of_study_obj.sudo().search(
                    [("id", "=", int(post.get("field_of_study", "0")))]
                )
                if not field_of_study_id:
                    error_messages.append("Field of Study not found.")
                academic_vals.update(
                    {
                        "field_of_study_id": field_of_study_id.id,
                    }
                )
            if error_messages:
                values["error_message"] = "\n".join(error_messages)
                return request.render(
                    "ssi_partner_experience_portal.portal_my_academic",
                    values,
                    headers={"X-Frame-Options": "DENY"},
                )
            if not current_academic_id:
                academic_obj.create(academic_vals)
            else:
                current_academic_id.write(academic_vals)
            return request.redirect("/my/academics")

        return request.render(
            "ssi_partner_experience_portal.portal_my_academic",
            values,
            headers={"X-Frame-Options": "DENY"},
        )

    @route(
        ["/my/academic/remove/<int:id>"],
        type="http",
        auth="user",
        website=True,
        methods=["GET", "POST"],
    )
    def remove_academic(self, **post):
        """Delete one academic experience record, then go back to list.

        :param post: route payload; ``id`` is the ``portal_
            partner_academic`` record to delete (also available as
            the ``id`` path segment)
        :return: redirect to ``/my/academics``
        """
        id = post.get("id")
        academic_id = request.env["portal_partner_academic"].search(
            [("id", "=", int(id))]
        )
        academic_id.unlink()
        return request.redirect("/my/academics")

    @route(["/my/experiences"], type="http", auth="user", website=True, methods=["GET"])
    def experiences(self):
        """Render the list of the current user's professional history.

        :return: rendered ``portal_my_experiences`` page listing every
            ``portal_partner_experience`` record owned by the
            logged-in user's partner
        """
        values = self._prepare_portal_layout_values()
        values["get_error"] = portal.get_error
        values["experience_ids"] = request.env["portal_partner_experience"].search(
            [("partner_id", "=", request.env.user.partner_id.id)]
        )

        return request.render(
            "ssi_partner_experience_portal.portal_my_experiences",
            values,
            headers={"X-Frame-Options": "DENY"},
        )

    @route(
        ["/my/experience", "/my/experience/<int:id>"],
        type="http",
        auth="user",
        website=True,
        methods=["GET", "POST"],
    )
    def experience(self, **post):
        """Show or save one professional experience record.

        On ``GET`` renders the create/edit form (empty when ``id`` is
        absent, pre-filled when present). On ``POST`` validates the
        submitted values, creates or writes the
        ``portal_partner_experience`` record for the current user's
        partner, then redirects to ``/my/experiences``; on validation
        failure the form is re-rendered with ``error_message`` set.

        :param post: form payload (``id``, ``job_position``,
            ``job_level``, ``location``, ``date_start``, ``expire``,
            ``date_end``, ``note``, ``partner_address``)
        :return: rendered form page, or a redirect on success
        """
        id = post.get("id")
        partner_obj = request.env["res.partner"].sudo()
        experience_obj = request.env["portal_partner_experience"]
        values = self._prepare_portal_layout_values()
        error_messages = []
        values.update(
            {
                "error_message": "",
                "partner_address_ids": partner_obj.search([("is_company", "=", True)]),
                "current_experience_id": experience_obj,
            }
        )
        current_experience_id = experience_obj
        if id:
            id = int(id)
            current_experience_id = experience_obj.search([("id", "=", id)])
            values.update(
                {
                    "current_experience_id": current_experience_id,
                }
            )

        if request.httprequest.method == "POST":
            experience_vals = {
                "partner_id": request.env.user.partner_id.id,
                "job_position": post.get("job_position"),
                "job_level": post.get("job_level"),
                "location": post.get("location"),
                "date_start": post.get("date_start") or False,
                "expire": post.get("expire"),
                "date_end": post.get("date_end") or False,
                "note": post.get("note"),
            }
            if post.get("partner_address"):
                partner_address_id = partner_obj.sudo().search(
                    [("id", "=", int(post.get("partner_address", "0")))]
                )
                if not partner_address_id:
                    error_messages.append("Institution not found.")
                experience_vals.update(
                    {
                        "partner_address_id": partner_address_id.id,
                    }
                )
            if error_messages:
                values["error_message"] = "\n".join(error_messages)
                return request.render(
                    "ssi_partner_experience_portal.portal_my_experience",
                    values,
                    headers={"X-Frame-Options": "DENY"},
                )
            if not current_experience_id:
                experience_obj.create(experience_vals)
            else:
                current_experience_id.write(experience_vals)
            return request.redirect("/my/experiences")

        return request.render(
            "ssi_partner_experience_portal.portal_my_experience",
            values,
            headers={"X-Frame-Options": "DENY"},
        )

    @route(
        ["/my/experience/remove/<int:id>"],
        type="http",
        auth="user",
        website=True,
        methods=["GET", "POST"],
    )
    def remove_experience(self, **post):
        """Delete one professional experience record, then go to list.

        :param post: route payload; ``id`` is the ``portal_
            partner_experience`` record to delete (also available as
            the ``id`` path segment)
        :return: redirect to ``/my/experiences``
        """
        id = post.get("id")
        experience_id = request.env["portal_partner_experience"].search(
            [("id", "=", int(id))]
        )
        experience_id.unlink()
        return request.redirect("/my/experiences")
