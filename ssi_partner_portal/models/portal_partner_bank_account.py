# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PortalPartnerBankAccount(models.Model):
    """
    Portal-facing view of ``res.partner.bank`` used by the bank
    account self-service pages under ``/my/bank_accounts``.
    Shares the same database table as ``res.partner.bank`` so portal
    users manage the same records exposed in the backend, scoped to
    their own partner through the security rules of this module.
    """

    _name = "portal_partner_bank_account"
    _inherit = ["res.partner.bank"]
    _description = "Portal Partner Bank Account"
    _table = "res_partner_bank"
    _order = "acc_number"
