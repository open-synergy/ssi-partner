# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestCompanyCapital(YamlTransactionCase):
    """Cover the shareholder relationship on ``res.partner``."""

    def test_company_capital(self):
        """Run the create-shareholder scenario for company capital."""
        self.run_yaml_scenario("test_data_company_capital.yaml")
