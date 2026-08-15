# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestResPartnerFamily(YamlTransactionCase):
    """Cover ``res.partner`` family fields: father, mother, guardian,
    spouse, children, and wards."""

    def test_res_partner_family(self):
        """Run the family fields scenario for ``res.partner``."""
        self.run_yaml_scenario("test_data_res_partner_family.yaml")
