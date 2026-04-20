# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=C8101
{
    "name": "Insurance Provider",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "ssi_product",
        "ssi_master_data_mixin",
    ],
    "data": [
        "security/res_groups/insurance_product_coverage.xml",
        "security/res_groups/insurance_product.xml",
        "security/ir_model_access/insurance_product_coverage.xml",
        "security/ir_model_access/insurance_product.xml",
        "menu.xml",
        "views/insurance_product_coverage_views.xml",
        "views/insurance_product_views.xml",
    ],
    "demo": [],
}
