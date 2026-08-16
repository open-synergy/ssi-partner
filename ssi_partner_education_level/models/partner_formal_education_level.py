# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerFormalEducationLevel(models.Model):
    """
    Represents a formal education level master data record (e.g. High
    School, Bachelor, Master). Used to classify the highest formal
    education attained by a partner, ordered by ``sequence``.
    """

    _name = "partner.formal_education_level"
    _inherit = ["mixin.master_data"]
    _description = "Formal Education Level"
    _order = "sequence, id"

    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )
