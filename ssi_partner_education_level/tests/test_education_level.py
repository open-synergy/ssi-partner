# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestEducationLevel(YamlTransactionCase):
    """Cover master data creation for education level models.

    Exercises ``partner.formal_education_level`` and
    ``partner.field_of_study`` record creation.
    """

    def test_education_level(self):
        """Run the education level master data creation scenario."""
        self.run_yaml_scenario("test_data_education_level.yaml")
