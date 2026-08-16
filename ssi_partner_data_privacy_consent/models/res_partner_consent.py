# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, fields, models
from odoo.exceptions import UserError


class ResPartnerConsent(models.Model):
    """
    Append-only log of privacy consent events for a data subject
    (res.partner). Each record captures a single grant or withdrawal of one
    processing purpose against one privacy notice version, together with the
    technical evidence of the event. Records are immutable once created:
    withdrawing a consent is done by creating a new record with
    consent_type "withdraw", never by modifying an existing record. The set
    of currently active purposes is derived (not stored) from this log.
    """

    _name = "res.partner.consent"
    _description = "res.partner - Data Privacy Consent"
    _order = "consent_date desc, id"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        ondelete="cascade",
        required=True,
        help="Data subject whose consent this record captures.",
    )
    notice_id = fields.Many2one(
        string="Privacy Notice",
        comodel_name="partner_consent_notice",
        ondelete="restrict",
        required=True,
        help="Privacy notice version presented to and agreed by the data "
        "subject at the time of this consent event.",
    )
    purpose_id = fields.Many2one(
        string="Purpose",
        comodel_name="partner_consent_purpose",
        ondelete="restrict",
        required=True,
        help="Data-processing purpose granted or withdrawn by this consent "
        "event. One purpose per record allows per-purpose granularity and "
        "withdrawal.",
    )
    consent_type = fields.Selection(
        string="Consent Type",
        selection=[
            ("grant", "Granted"),
            ("withdraw", "Withdrawn"),
        ],
        required=True,
        default="grant",
        help="Whether this event grants or withdraws consent for the purpose.",
    )
    consent_date = fields.Datetime(
        string="Consent Date",
        required=True,
        default=fields.Datetime.now,
        help="Date and time at which the consent event occurred.",
    )
    channel = fields.Selection(
        string="Channel",
        selection=[
            ("portal", "Portal"),
            ("manual", "Back Office"),
            ("import", "Import"),
        ],
        required=True,
        default="portal",
        help="Channel through which this consent event was captured.",
    )
    evidence_ip = fields.Char(
        string="Evidence IP",
        help="IP address recorded as technical evidence of the consent event.",
    )
    evidence_user_agent = fields.Char(
        string="Evidence User Agent",
        help="Browser user agent recorded as technical evidence of the "
        "consent event.",
    )
    note = fields.Text(
        string="Note",
        help="Free-text note about this consent event.",
    )

    def write(self, vals):
        """Block modification of consent records by non-superuser calls.

        Consent events must stay immutable to keep the log an
        auditable trail. Withdrawing consent means creating a new
        record with ``consent_type`` "withdraw", never editing an
        existing one.

        :raises UserError: when called without ``self.env.su``
        """
        if not self.env.su:
            raise UserError(
                _(
                    "Data privacy consent records are immutable and cannot be "
                    "modified. To withdraw a consent, create a new record with "
                    "consent type Withdrawn."
                )
            )
        return super(ResPartnerConsent, self).write(vals)

    def unlink(self):
        """Block deletion of consent records by non-superuser calls.

        Consent events must stay in the log permanently to preserve
        the audit trail required for privacy compliance.

        :raises UserError: when called without ``self.env.su``
        """
        if not self.env.su:
            raise UserError(
                _(
                    "Data privacy consent records are immutable and cannot be "
                    "deleted."
                )
            )
        return super(ResPartnerConsent, self).unlink()
