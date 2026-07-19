# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class ResPartnerEthnicity(models.Model):
    """Represents the ethnicity of an individual partner. Used for
    demographic reporting purposes."""

    _name = "res_partner_ethnicity"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Partner Ethnicity"
