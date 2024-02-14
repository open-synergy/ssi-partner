# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    creditor_ids = fields.One2many(
        string="Creditors",
        comodel_name="partner_creditor_debtor",
        inverse_name="debtor_id",
    )
    debtor_ids = fields.One2many(
        string="Debitors",
        comodel_name="partner_creditor_debtor",
        inverse_name="creditor_id",
    )
