# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResPartnerBank(models.Model):
    _name = "res.partner.bank"
    _inherit = [
        "res.partner.bank",
    ]

    usage_id = fields.Many2one(
        string="Usage",
        comodel_name="res_partner_bank_usage",
        help="Classifies the intended usage of this bank account, e.g. "
        "Operational, Payroll, Tax, or Escrow. Optional.",
    )
