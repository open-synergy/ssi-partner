# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models


class ResPartner(models.Model):
    """
    Adds creditor/debtor tracking to contacts.
    Lets a contact list which other contacts are its creditors and
    which are its debtors, and exposes the primary (first-sequence)
    creditor as a dedicated field for quick reference.
    """

    _name = "res.partner"
    _inherit = "res.partner"

    primary_creditor_id = fields.Many2one(
        string="Primary Creditor",
        comodel_name="res.partner",
        compute="_compute_primary_creditor_id",
        store=True,
        compute_sudo=True,
    )
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

    @api.depends(
        "creditor_ids",
        "creditor_ids.sequence",
        "creditor_ids.creditor_id",
    )
    def _compute_primary_creditor_id(self):
        """Set ``primary_creditor_id`` to the first creditor in line.

        The first row of ``creditor_ids``, ordered by ``sequence``, is
        taken as the partner's primary creditor. Falls back to
        ``False`` when no creditor row exists.
        """
        for record in self:
            result = False
            if record.creditor_ids:
                result = record.creditor_ids[0].creditor_id
            record.primary_creditor_id = result
