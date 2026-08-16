# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase — BUKAN HttpCase. 14.0's HttpCase does not expose
# cls.env in setUpClass.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiInsuranceProductCoverage(HttpSavepointCase):
    """Tour tests for the ``insurance_product_coverage`` work instructions."""

    def test_create(self):
        """Run the create tour for ``insurance_product_coverage``.

        IK: docs/insurance_product_coverage/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_insurance_provider_insurance_product_coverage_create",
            login="admin",
        )
