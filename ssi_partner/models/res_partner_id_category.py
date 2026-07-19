# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResPartnerIdCategory(models.Model):
    """Represents a category of partner identification numbers (e.g.
    National ID, Tax ID, Driving License, Passport, Business
    Registration Number). Each category may carry its own Python
    validation code, used to check the format of the identification
    numbers assigned to it."""

    _name = "res_partner_id_category"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Partner ID Category"

    validation_code = fields.Text(
        string="Validation Code",
        help="Python code evaluated to validate the format of an "
        "identification number belonging to this category. The number "
        "being validated is available as the `id_number` variable; "
        "the code must set a boolean `result` variable (True = valid, "
        "False = invalid). Leave empty to accept any number for this "
        "category.",
    )
    color = fields.Integer(
        string="Color",
        help="Color index used to visually distinguish this category, "
        "e.g. in kanban or tag-like widgets.",
    )
