# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase
from psycopg2 import IntegrityError

from odoo.tests import tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestPartnerHistory(YamlTransactionCase):
    def test_partner_history(self):
        self.run_yaml_scenario("test_data_partner_history.yaml")

    def test_experience_requires_date_start(self):
        """Python murni — pemicu P5 (L-22: `expect_error.type` di
        `odoo-yaml-test` terbatas 12 nama hard-coded dan tidak termasuk
        `psycopg2.IntegrityError`; `date_start` yang hilang melanggar
        `NOT NULL` di level database, bukan salah satu dari 12 tipe itu).

        Membuktikan `date_start` (`required=True` pada
        `mixin.partner_experience`) benar-benar wajib diisi di level
        database: `partner_experience` tanpa `date_start` harus ditolak.
        """
        partner = self.env["res.partner"].create({"name": "Jane Doe"})
        model = self.env["partner_experience"]

        with self.assertRaises(IntegrityError), mute_logger("odoo.sql_db"):
            model.create(
                {
                    "name": "Software Engineer at Acme",
                    "partner_id": partner.id,
                }
            )
            self.env.cr.flush()
