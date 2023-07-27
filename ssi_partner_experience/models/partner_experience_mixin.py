# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PartnerExperienceMixin(models.AbstractModel):
    _name = "partner.experience.mixin"
    _inherit = [
        "mixin.master_data",
        "mixin.employee_document",
        "mixin.date_duration",
    ]
    _description = "Abstract Class for Partner Experience"
    _date_end_required = False

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        domain="[('is_company', '=', False)]",
    )
    partner_address_id = fields.Many2one(
        comodel_name="res.partner",
        string="Address",
        help="Employer, School, University, " "Certification Authority",
    )
    location = fields.Char(
        string="Location",
        help="Location",
    )
    expire = fields.Boolean(
        string="Expire",
        help="Expire",
        default=True,
    )
