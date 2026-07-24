# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PartnerConsentPurpose(models.Model):
    """
    Master data of data-processing purposes referenced by partner consent
    records. Each purpose represents a specific reason for which personal
    data may be processed under a privacy consent.
    """

    _name = "partner_consent_purpose"
    _inherit = ["mixin.master_data"]
    _description = "Partner Consent Purpose"
