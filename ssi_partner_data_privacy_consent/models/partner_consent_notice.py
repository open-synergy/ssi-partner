# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import datetime

from odoo import fields, models


class PartnerConsentNotice(models.Model):
    """
    Master data of privacy notice documents. One record represents exactly
    one version of a privacy notice whose exact text is presented to and
    agreed by the data subject. Referenced by partner consent records.
    """

    _name = "partner_consent_notice"
    _inherit = ["mixin.master_data"]
    _description = "Partner Consent Privacy Notice"

    version = fields.Char(
        string="Version",
        required=True,
        help="Version identifier of this privacy notice document.",
    )
    body = fields.Text(
        string="Body",
        required=True,
        help="Exact text of the privacy notice agreed by the data subject.",
    )
    date_effective = fields.Date(
        string="Effective Date",
        required=True,
        default=lambda self: datetime.date.today(),
        help="Date from which this privacy notice version takes effect.",
    )
    purpose_ids = fields.Many2many(
        string="Purposes",
        comodel_name="partner_consent_purpose",
        relation="rel_partner_consent_notice_2_purpose",
        column1="notice_id",
        column2="purpose_id",
        help="Data-processing purposes covered by this privacy notice.",
    )
