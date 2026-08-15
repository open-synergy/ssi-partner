# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ResPartnerBankUsage(models.Model):
    """Master data listing the usage/purpose of a partner bank account.

    Selected on ``res.partner.bank`` records (e.g. Operational, Payroll,
    Tax, Escrow) to classify how a bank account is intended to be used.
    """

    _name = "res_partner_bank_usage"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Bank Account Usage"
