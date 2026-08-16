# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestDataPrivacyConsent(YamlTransactionCase):
    """Cover ``res.partner.consent`` and its related master data models.

    Exercises purpose/notice master data CRUD, ACL for the
    configurator group, immutability of consent records, required
    fields, and the derivation of ``active_consent_purpose_ids`` on
    ``res.partner`` from the consent log.
    """

    def test_data_privacy_consent(self):
        """Run the data privacy consent YAML scenario."""
        self.run_yaml_scenario("test_data_privacy_consent.yaml")
