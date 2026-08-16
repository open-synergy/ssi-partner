# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestPartnerExperience(YamlTransactionCase):
    """Cover ``partner.experience`` and ``partner.academic`` creation."""

    def test_partner_experience(self):
        """Run the create scenarios for experience and academic records."""
        self.run_yaml_scenario("test_data_partner_experience.yaml")
