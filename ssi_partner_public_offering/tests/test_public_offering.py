# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestPublicOffering(YamlTransactionCase):
    """Cover the ``company_public_offering_type`` master data model."""

    def test_public_offering(self):
        """Run the public offering type creation scenario."""
        self.run_yaml_scenario("test_data_public_offering.yaml")
