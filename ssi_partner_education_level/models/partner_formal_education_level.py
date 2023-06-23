# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import fields, models


class PartnerFormalEducationLevel(models.Model):
    _name = "partner.formal_education_level"
    _inherit = ["mixin.master_data"]
    _description = "Formal Education Level"
    _order = "sequence, id"

    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )