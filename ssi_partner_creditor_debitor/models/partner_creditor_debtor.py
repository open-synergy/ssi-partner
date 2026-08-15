# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerCreditorDebtor(models.Model):
    """
    Represents a single creditor/debtor relationship between two
    ``res.partner`` records. Each record links one partner acting as
    creditor to another partner acting as debtor, and is edited inline
    from the Creditor & Debtor tab of either partner's form.
    """

    _name = "partner_creditor_debtor"
    _description = "Partner Creditors Debtors"
    _order = "sequence, id"

    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=10,
    )
    creditor_id = fields.Many2one(
        string="Creditor",
        comodel_name="res.partner",
        required=True,
    )

    debtor_id = fields.Many2one(
        string="Debtor",
        comodel_name="res.partner",
        required=True,
    )
