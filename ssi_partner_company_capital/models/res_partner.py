# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResPartner(models.Model):
    """
    Adds company capital/shareholder tracking to contacts.
    Lets a company contact list the shareholders holding its shares
    and how many shares each shareholder holds, edited from the
    Capital page of the contact form.
    """

    _name = "res.partner"
    _inherit = "res.partner"

    shareholder_ids = fields.One2many(
        string="Shareholders",
        comodel_name="company.shareholder",
        inverse_name="partner_id",
    )
