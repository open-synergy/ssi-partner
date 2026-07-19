# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MixinPartnerExperience(models.AbstractModel):
    """Abstract base for a dated entry in a partner's history (academic
    background, certification, or work experience). Provides a native
    date range (``date_start``/``date_end``, without depending on
    ``ssi_duration_mixin``, unavailable in this series) together with the
    common fields shared by every concrete history entry.

    Concrete models inheriting this mixin are expected to add their own
    entry-specific fields (e.g. ``diploma``, ``certification``,
    ``job_position``) on top of the fields defined here.
    """

    _name = "mixin.partner_experience"
    _inherit = [
        "mail.thread",
        "mail.activity.mixin",
    ]
    _description = "Mixin for Partner Experience"
    _order = "partner_id, date_start desc"

    name = fields.Char(
        required=True,
        help="Short label identifying this history entry.",
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
        help="Partner this history entry belongs to.",
    )
    partner_address_id = fields.Many2one(
        string="Institution/Company",
        comodel_name="res.partner",
        domain=[("is_company", "=", True)],
        help="Institution or company associated with this history entry "
        "(e.g. the school or employer).",
    )
    date_start = fields.Date(
        required=True,
        help="Date this history entry started.",
    )
    date_end = fields.Date(
        help="Date this history entry ended. Leave empty if it is still ongoing.",
    )
    location = fields.Char(
        help="Place where this history entry took place, e.g. city or campus.",
    )
    expire = fields.Boolean(
        default=True,
        help="Whether this history entry is expected to have an end date at all.",
    )
    active = fields.Boolean(
        default=True,
        help="Uncheck to archive this history entry without deleting it.",
    )
    note = fields.Text(
        help="Free-text note about this history entry.",
    )

    def _check_experience_date_range_condition(self):
        self.ensure_one()
        if not self.date_end:
            return True
        return self.date_end >= self.date_start

    @api.constrains("date_start", "date_end")
    def _check_experience_date_range(self):
        for record in self.sudo():
            if not record._check_experience_date_range_condition():
                error_message = f"""
Document Type: {record._description}
Context: Create or update partner history entry
Database ID: {record.id}
Problem: End date is earlier than start date
Solution: Set an end date on or after the start date, or leave it empty
"""
                raise ValidationError(error_message)
