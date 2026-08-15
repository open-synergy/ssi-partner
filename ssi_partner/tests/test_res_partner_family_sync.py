# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestResPartnerFamilySync(YamlTransactionCase):
    """Cover ``children_ids``/``ward_ids`` sync and ``link_child`` on
    ``res.partner``."""

    def test_res_partner_family_sync(self):
        """Run the family sync and ``link_child`` scenario."""
        self.run_yaml_scenario("test_data_res_partner_family_sync.yaml")
