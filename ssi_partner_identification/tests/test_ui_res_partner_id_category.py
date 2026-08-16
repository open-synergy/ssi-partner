# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase — BUKAN HttpCase. 14.0's HttpCase does not expose
# cls.env in setUpClass.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiResPartnerIdCategory(HttpSavepointCase):
    """Tour tests for the ``res.partner.id_category`` work instructions."""

    def test_create(self):
        """Run the create tour for ``res.partner.id_category``.

        IK: docs/res_partner_id_category/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_identification_res_partner_id_category_create",
            login="admin",
        )
