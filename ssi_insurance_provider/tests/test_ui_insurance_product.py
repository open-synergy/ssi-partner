# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase — BUKAN HttpCase. 14.0's HttpCase does not expose
# cls.env in setUpClass.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiInsuranceProduct(HttpSavepointCase):
    """Tour tests for the ``insurance_product`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the provider, coverage type, and currency the tour
        picks from the many2one dropdowns (IK Pre-Condition data).
        """
        super().setUpClass()
        cls.provider = cls.env["res.partner"].create(
            {"name": "Tour Test Insurance Provider", "is_company": True}
        )
        cls.coverage = cls.env["insurance_product_coverage"].create(
            {"name": "Tour Test Product Coverage", "code": "/"}
        )
        # The currency dropdown only lists active currencies; ensure USD
        # is active so the tour can select it.
        cls.currency = cls.env.ref("base.USD")
        if not cls.currency.active:
            cls.currency.sudo().write({"active": True})

    def test_create(self):
        """Run the create tour for ``insurance_product``.

        IK: docs/insurance_product/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_insurance_provider_insurance_product_create",
            login="admin",
        )
