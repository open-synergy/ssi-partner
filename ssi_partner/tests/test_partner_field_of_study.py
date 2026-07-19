# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestPartnerFieldOfStudy(YamlTransactionCase):
    def test_partner_field_of_study(self):
        self.run_yaml_scenario("test_data_partner_field_of_study.yaml")
