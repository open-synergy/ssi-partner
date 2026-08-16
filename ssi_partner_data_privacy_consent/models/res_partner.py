# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    """
    Adds data privacy consent tracking to partner records.
    Exposes the append-only consent log and the set of purposes
    currently granted, derived from that log.
    """

    _name = "res.partner"
    _inherit = "res.partner"

    consent_ids = fields.One2many(
        string="Data Privacy Consents",
        comodel_name="res.partner.consent",
        inverse_name="partner_id",
        readonly=True,
        help="Append-only log of privacy consent events for this partner.",
    )
    active_consent_purpose_ids = fields.Many2many(
        string="Active Consent Purposes",
        comodel_name="partner_consent_purpose",
        compute="_compute_active_consent_purpose_ids",
        store=False,
        compute_sudo=True,
        help="Purposes whose most recent consent event is a grant. Derived "
        "from the consent log, not stored.",
    )

    @api.depends(
        "consent_ids",
        "consent_ids.consent_type",
        "consent_ids.purpose_id",
        "consent_ids.consent_date",
    )
    def _compute_active_consent_purpose_ids(self):
        """Derive the purposes currently granted from the consent log.

        For each purpose, only the most recent consent event (by
        ``consent_date`` desc) determines whether it is active: a
        purpose is active when that event's ``consent_type`` is
        ``grant``, and inactive when it is ``withdraw`` or has no
        event at all.
        """
        for record in self:
            active = self.env["partner_consent_purpose"]
            seen = set()
            # consent_ids is ordered by "consent_date desc, id", so the first
            # event encountered per purpose is its most recent event.
            for consent in record.consent_ids:
                purpose = consent.purpose_id
                if purpose.id in seen:
                    continue
                seen.add(purpose.id)
                if consent.consent_type == "grant":
                    active |= purpose
            record.active_consent_purpose_ids = active
