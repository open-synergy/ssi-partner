# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiResPartner(HttpSavepointCase):
    """Tour test for the ``res.partner`` Capital field delta."""

    def test_field_capital(self):
        """Run the delta tour for the Contacts create form.

        IK: docs/res_partner/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_company_capital_res_partner_field_capital",
            login="admin",
        )
