# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class IrActionsActWindow(models.Model):
    _name = "ir.actions.act_window"
    _inherit = [
        "ir.actions.act_window",
    ]

    def read(self, fields=None, load="_classic_read"):
        actions = super().read(fields=fields, load=load)
        for action in actions:
            if action.get("res_model") == "res.partner":
                # By default, a contact list only shows standalone contacts.
                action_context = action.get("context") or "{}"
                if "search_show_all_positions" not in action_context:
                    action["context"] = action_context.replace(
                        "{",
                        (
                            "{'search_show_all_positions': "
                            "{'is_set': True, 'set_value': False},"
                        ),
                        1,
                    )
        return actions
