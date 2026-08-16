# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase — BUKAN HttpCase. 14.0's HttpCase does not expose
# cls.env in setUpClass.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiResPartnerIdNumber(HttpSavepointCase):
    """Tour tests for the ``res.partner.id_number`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the partner and ID category the tour selects via the
        many2one dropdowns (IK Pre-Condition data).
        """
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create(
            {"name": "Tour Test ID Number Partner", "is_company": True}
        )
        cls.category = cls.env["res.partner.id_category"].create(
            {"name": "Tour Test ID Number Category", "code": "tour_test_idn"}
        )

    def test_create(self):
        """Run the create tour for ``res.partner.id_number``.

        IK: docs/res_partner_id_number/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_identification_res_partner_id_number_create",
            login="admin",
        )
