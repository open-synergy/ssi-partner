# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestPartnerEvaluation(YamlTransactionCase):
    """Cover master data creation for the partner evaluation models."""

    def test_partner_evaluation(self):
        """Run the evaluation result/type creation scenario."""
        self.run_yaml_scenario("test_data_partner_evaluation.yaml")
