# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase
from psycopg2 import IntegrityError

from odoo.tests import tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestPortalPartnerBankAccount(YamlTransactionCase):
    """Scenario tests for ``portal_partner_bank_account``."""

    def test_portal_partner_bank_account(self):
        """Run the CRUD and compute scenario for the model."""
        self.run_yaml_scenario("test_data_portal_partner_bank_account.yaml")

    @mute_logger("odoo.sql_db")
    def test_acc_number_required(self):
        """Reject a record created without the required ``acc_number``.

        Pure Python — trigger P5 (L-22: ``psycopg2.IntegrityError`` is
        outside the 12 error types ``expect_error`` understands, since
        ``acc_number`` is only enforced by the NOT NULL column
        constraint inherited from ``res.partner.bank``, not by a
        Python-level ``@api.constrains``).
        ``mute_logger("odoo.sql_db")`` silences the PostgreSQL ERROR
        line this deliberately triggers, so ``oca_checklog_odoo``
        does not fail the CI even though the test itself passes.
        """
        partner = self.env["res.partner"].create(
            {
                "name": "Test Missing Account Number Owner",
                "is_company": True,
            }
        )
        with self.assertRaises(IntegrityError):
            self.env["portal_partner_bank_account"].create(
                {
                    "partner_id": partner.id,
                }
            )
