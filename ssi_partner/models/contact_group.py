# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ContactGroup(models.Model):
    _name = "contact_group"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Contact Group"

    commercial_contact_id = fields.Many2one(
        string="Commercial Contact",
        comodel_name="res.partner",
        domain=[
            ("parent_id", "=", False),
        ],
        required=True,
    )
    contact_ids = fields.Many2many(
        string="Contacts",
        comodel_name="res.partner",
        relation="rel_contact_group_partner",
        column1="group_id",
        column2="partner_id",
        required=True,
    )

    @api.onchange(
        "commercial_contact_id",
    )
    def onchange_contact_ids(self):
        self.contact_ids = False
