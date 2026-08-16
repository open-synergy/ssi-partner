# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    """
    Adds background history to the contact form.

    Exposes the ``partner.academic``, ``partner.certification``, and
    ``partner.experience`` records owned by this contact as one2many
    lines, so the Experiences page on the contact form can display and
    manage them.
    """

    _inherit = "res.partner"

    academic_ids = fields.One2many(
        comodel_name="partner.academic",
        inverse_name="partner_id",
        string="Academic experiences",
        help="Academic experiences",
    )
    certification_ids = fields.One2many(
        comodel_name="partner.certification",
        inverse_name="partner_id",
        string="Certifications",
        help="Certifications",
    )
    experience_ids = fields.One2many(
        comodel_name="partner.experience",
        inverse_name="partner_id",
        string="Professional Experiences",
        help="Professional Experiences",
    )
