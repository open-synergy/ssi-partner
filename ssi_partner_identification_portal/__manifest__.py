# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Partner Identification Portal",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "auto_install": True,
    "depends": [
        "ssi_partner_identification",
        "ssi_partner_portal",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/portal_templates.xml",
    ],
    "demo": [],
}
