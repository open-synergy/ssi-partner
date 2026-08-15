# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase
from psycopg2 import IntegrityError

from odoo.tests import tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestPortalPartnerExperience(YamlTransactionCase):
    """Scenario tests for ``portal_partner_experience``."""

    def test_portal_partner_experience(self):
        """Run the CRUD and constraint scenario for the model."""
        self.run_yaml_scenario("test_data_portal_partner_experience.yaml")

    @mute_logger("odoo.sql_db")
    def test_partner_id_required(self):
        """Reject a record created without the required ``partner_id``.

        Pure Python — trigger P5 (L-22: ``psycopg2.IntegrityError`` is
        outside the 12 error types ``expect_error`` understands, since
        ``partner_id`` is only enforced by the NOT NULL column
        constraint the ORM creates for ``required=True``, not by a
        Python-level ``@api.constrains``).
        ``mute_logger("odoo.sql_db")`` silences the PostgreSQL ERROR
        line this deliberately triggers, so ``oca_checklog_odoo`` does
        not fail the CI even though the test itself passes.
        """
        with self.assertRaises(IntegrityError):
            self.env["portal_partner_experience"].create(
                {
                    "date_start": "2020-01-01",
                }
            )
