# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class PartnerFormalEducationLevel(models.Model):
    """Represents a formal education level (e.g. Elementary School, High
    School, Bachelor's Degree, Master's Degree, Doctorate) that can be
    assigned to a partner's academic history."""

    _name = "partner_formal_education_level"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Partner Formal Education Level"
    _order = "sequence, id"

    sequence = fields.Integer(
        required=True,
        default=5,
        help="Determines the display order of education levels in "
        "selection lists, from the lowest to the highest level.",
    )
