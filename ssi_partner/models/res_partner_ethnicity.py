from odoo import api, fields, models


class ResPartnerEthnicity(models.Model):
    _name = "res_partner_ethnicity"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Ethnicity"
