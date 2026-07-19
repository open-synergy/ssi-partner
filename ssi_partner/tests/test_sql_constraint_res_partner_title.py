# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase
from psycopg2 import IntegrityError

from odoo.tests import tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestSqlConstraintResPartnerTitle(YamlTransactionCase):
    def test_duplicate_name_is_rejected_by_unique_constraint(self):
        """Python murni — pemicu P5 (L-22: `expect_error.type` di
        `odoo-yaml-test` terbatas 12 nama hard-coded dan tidak termasuk
        `psycopg2.IntegrityError`; constraint unik DB-level seperti
        `models.Constraint` tak bisa diuji dari YAML).

        Membuktikan `_partner_title_name_uniq = models.Constraint(...)`
        benar-benar aktif di level database: dua record `res.partner.title`
        dengan `name` yang sama harus ditolak.
        """
        model = self.env["res.partner.title"]
        model.create({"name": "Duplicate Title"})

        with self.assertRaises(IntegrityError), mute_logger("odoo.sql_db"):
            model.create({"name": "Duplicate Title"})
            self.env.cr.flush()
