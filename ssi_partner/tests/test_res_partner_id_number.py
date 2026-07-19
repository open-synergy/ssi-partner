# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo_yaml_test import YamlTransactionCase
from psycopg2 import IntegrityError

from odoo.tests import tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestResPartnerIdNumber(YamlTransactionCase):
    def test_res_partner_id_number(self):
        self.run_yaml_scenario("test_data_res_partner_id_number.yaml")

    @mute_logger("odoo.sql_db")
    def test_category_id_is_required(self):
        """Python murni — pemicu P5 (L-22: `expect_error.type` di
        `odoo-yaml-test` terbatas 12 nama hard-coded dan tidak termasuk
        `psycopg2.IntegrityError`).

        ``category_id`` adalah field ``required=True`` biasa (NOT NULL
        di database), bukan ``@api.constrains``, sehingga
        pelanggarannya lolos sampai ke database dan muncul sebagai
        ``psycopg2.errors.NotNullViolation`` saat di-flush, bukan
        salah satu dari 12 tipe yang didukung ``expect_error`` YAML.
        """
        partner = self.env["res.partner"].create({"name": "Contact A"})

        with self.assertRaises(IntegrityError):
            self.env["res_partner_id_number"].create(
                {
                    "name": "123456",
                    "partner_id": partner.id,
                }
            )
            self.env.cr.flush()
