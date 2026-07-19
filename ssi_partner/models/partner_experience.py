# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class PartnerExperience(models.Model):
    """Represents a work experience entry of a partner (e.g. a past or
    current job), used for recruitment, partner assessment, and expert
    profiling purposes."""

    _name = "partner_experience"
    _inherit = [
        "mixin.partner_experience",
    ]
    _description = "Partner Work Experience"

    job_position = fields.Char(
        help="Job position/title held during this work experience entry.",
    )
    job_level = fields.Char(
        help="Job level/rank held during this work experience entry, "
        "e.g. Junior, Senior, Manager.",
    )
