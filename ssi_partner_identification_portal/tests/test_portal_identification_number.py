# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase
from psycopg2 import IntegrityError

from odoo.tests import tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestPortalIdentificationNumber(YamlTransactionCase):
    """Scenario tests for ``portal_identification_number``."""

    def test_portal_identification_number(self):
        """Run the CRUD scenario for the model."""
        self.run_yaml_scenario("test_data_portal_identification_number.yaml")

    @mute_logger("odoo.sql_db")
    def test_name_required(self):
        """Reject a record created without the required ``name``.

        Pure Python -- trigger P5 (L-22: ``psycopg2.IntegrityError`` is
        outside the 12 error types ``expect_error`` understands, since
        ``name`` is only enforced by the NOT NULL column constraint
        inherited from ``res.partner.id_number``, not by a
        Python-level ``@api.constrains``).
        ``mute_logger("odoo.sql_db")`` silences the PostgreSQL ERROR
        line this deliberately triggers, so ``oca_checklog_odoo``
        does not fail the CI even though the test itself passes.
        """
        partner = self.env["res.partner"].create(
            {
                "name": "Test Missing Identification Name Owner",
                "is_company": True,
            }
        )
        category = self.env["res.partner.id_category"].create(
            {
                "code": "test_missing_name",
                "name": "Test Missing Name Category",
            }
        )
        with self.assertRaises(IntegrityError):
            self.env["portal_identification_number"].create(
                {
                    "partner_id": partner.id,
                    "category_id": category.id,
                }
            )
