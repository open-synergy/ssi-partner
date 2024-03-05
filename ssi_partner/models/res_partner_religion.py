from odoo import api, fields, models


class ResPartnerReligion(models.Model):
    _name = "res_partner_religion"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Religion"
