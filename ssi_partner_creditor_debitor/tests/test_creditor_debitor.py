# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestCreditorDebitor(YamlTransactionCase):
    """Cover the creditor/debitor relationship on ``res.partner``."""

    def test_creditor_debitor(self):
        """Run the create-relationship scenario for creditor/debtor."""
        self.run_yaml_scenario("test_data_creditor_debitor.yaml")
