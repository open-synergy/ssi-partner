# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestPartnerLanguage(YamlTransactionCase):
    """Cover ``partner.language`` create and duplicate-check behavior."""

    def test_partner_language(self):
        """Run the create scenario for ``partner.language``."""
        self.run_yaml_scenario("test_data_partner_language.yaml")
