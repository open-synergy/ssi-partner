# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = [
        "res.partner",
    ]

    type = fields.Selection(
        selection_add=[
            ("branch", "Branch Address"),
        ],
        ondelete={"branch": "cascade"},
    )

    def action_open_contact_address(self):
        for record in self.sudo():
            result = record._open_contact_address()
        return result

    def _open_contact_address(self):
        self.ensure_one()
        waction = self.env.ref("contacts.action_contacts").read()[0]
        waction.update(
            {
                "view_mode": "list,form",
                "domain": [("id", "child_of", self.id), ("id", "!=", self.id)],
                "context": {},
            }
        )
        return waction
