# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartnerBank(models.Model):
    """Add a usage/purpose classification to partner bank accounts.

    Links each bank account to a ``res_partner_bank_usage`` master data
    record so its intended use (e.g. Operational, Payroll) is traceable.
    """

    _inherit = "res.partner.bank"

    usage_id = fields.Many2one(
        string="Usage",
        comodel_name="res_partner_bank_usage",
        help="Usage/purpose of this bank account, e.g. Operational, Payroll, "
        "Tax, Escrow. Optional, used to classify how the account is intended "
        "to be used.",
    )
