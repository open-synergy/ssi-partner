# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo_yaml_test import YamlTransactionCase
from psycopg2 import IntegrityError

from odoo.tests import tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestPartnerContactGroup(YamlTransactionCase):
    def test_partner_contact_group(self):
        self.run_yaml_scenario("test_data_partner_contact_group.yaml")

    def test_commercial_contact_id_is_required(self):
        """Python murni — pemicu P5 (L-22: `expect_error.type` di
        `odoo-yaml-test` terbatas 12 nama hard-coded dan tidak termasuk
        `psycopg2.IntegrityError`).

        ``commercial_contact_id`` adalah field ``required=True`` biasa
        (NOT NULL di database), bukan ``@api.constrains``, sehingga
        pelanggarannya lolos sampai ke database dan muncul sebagai
        ``psycopg2.errors.NotNullViolation`` saat di-flush, bukan salah
        satu dari 12 tipe yang didukung ``expect_error`` YAML.
        """
        contact = self.env["res.partner"].create({"name": "Contact A"})

        with self.assertRaises(IntegrityError), mute_logger("odoo.sql_db"):
            self.env["partner_contact_group"].create(
                {
                    "name": "Deal Team",
                    "code": "/",
                    "contact_ids": [(6, 0, [contact.id])],
                }
            )
            self.env.cr.flush()
