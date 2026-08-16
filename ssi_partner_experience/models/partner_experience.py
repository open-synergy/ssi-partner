# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerExperience(models.Model):
    """
    Records one professional job experience of a contact.

    Each record represents a past or current employment held by the
    ``res.partner`` referenced in ``partner_id``, with the employer stored
    in ``partner_address_id`` (inherited from ``partner.experience.mixin``)
    and the role described by ``job_position``/``job_level``.
    """

    _name = "partner.experience"
    _inherit = "partner.experience.mixin"
    _description = "Contact's Professional Experience"

    job_position = fields.Char(
        string="Job Position",
    )
    job_level = fields.Char(
        string="Job Level",
    )
