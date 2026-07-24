# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=C8101
{
    "name": "Partner Data Privacy Consent",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "ssi_partner",
    ],
    "data": [
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "menu.xml",
        "views/partner_consent_purpose_views.xml",
        "views/partner_consent_notice_views.xml",
    ],
    "demo": [],
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
}
