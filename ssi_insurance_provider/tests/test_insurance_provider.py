# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestInsuranceProvider(YamlTransactionCase):
    """Cover ``insurance_product_coverage`` and ``insurance_product`` CRUD."""

    def test_insurance_provider(self):
        """Run the coverage/product creation scenarios."""
        self.run_yaml_scenario("test_data_insurance_provider.yaml")
