# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiResPartner(HttpSavepointCase):
    """Tour test for the ``res.partner`` Creditor & Debtor field delta."""

    def test_field_creditor_debtor(self):
        """Run the delta tour for the Contacts create form.

        IK: docs/res_partner/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_creditor_debitor_res_partner_field_creditor_debtor",
            login="admin",
        )
