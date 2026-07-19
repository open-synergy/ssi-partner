# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class ResPartnerReligion(models.Model):
    """Represents the religion of an individual partner. Used for
    demographic reporting and document templates that require religion
    information."""

    _name = "res_partner_religion"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Partner Religion"
