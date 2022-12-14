# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Partner App",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "contacts",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "menu.xml",
        "views/res_partner_views.xml",
        "views/res_partner_category_views.xml",
        "views/res_partner_title_views.xml",
        "views/res_partner_industry_views.xml",
        "views/res_country_views.xml",
        "views/res_country_state_views.xml",
        "views/res_country_group_views.xml",
        "views/res_bank_views.xml",
        "views/res_partner_bank_views.xml",
    ],
    "demo": [],
}
