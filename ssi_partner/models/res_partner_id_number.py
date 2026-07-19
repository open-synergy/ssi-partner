# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import datetime

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval


class ResPartnerIdNumber(models.Model):
    """Represents an identification number (e.g. National ID, Tax ID,
    Driving License, Passport, Business Registration Number) assigned
    to a partner. Each number belongs to a category
    (``res_partner_id_category``) that determines how its format is
    validated, and may carry its own validity period."""

    _name = "res_partner_id_number"
    _description = "Partner ID Number"
    _order = "partner_id, category_id, name"

    name = fields.Char(
        string="Number",
        required=True,
        help="The identification number itself, as printed on the "
        "document (e.g. the National ID number).",
    )
    category_id = fields.Many2one(
        string="Category",
        comodel_name="res_partner_id_category",
        required=True,
        ondelete="restrict",
        help="Category of this identification number, e.g. National "
        "ID, Tax ID, Driving License. Determines the validation rule "
        "applied to the number.",
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        help="Partner this identification number belongs to.",
    )
    partner_issued_id = fields.Many2one(
        string="Issued By",
        comodel_name="res.partner",
        help="Partner (institution/authority) that issued this "
        "identification number, e.g. the government agency.",
    )
    date_issued = fields.Date(
        string="Date Issued",
        help="Date this identification number was issued.",
    )
    valid_from = fields.Date(
        string="Valid From",
        help="Date from which this identification number is "
        "considered valid. Leave empty if there is no start date.",
    )
    valid_until = fields.Date(
        string="Valid Until",
        help="Date until which this identification number is "
        "considered valid. Leave empty if it does not expire.",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        help="Uncheck to archive this identification number without deleting it.",
    )
    status = fields.Selection(
        string="Status",
        selection=[
            ("draft", "Draft"),
            ("open", "Valid"),
            ("expired", "Expired"),
        ],
        compute="_compute_status",
        store=True,
        compute_sudo=True,
        help="Validity status computed from the Valid From/Valid "
        "Until dates compared to today: Draft when no validity period "
        "is set at all, Expired once Valid Until has passed, Valid "
        "otherwise.",
    )

    @api.depends("valid_from", "valid_until")
    def _compute_status(self):
        today = datetime.date.today()
        for record in self:
            if not record.valid_from and not record.valid_until:
                record.status = "draft"
            elif record.valid_until and record.valid_until < today:
                record.status = "expired"
            else:
                record.status = "open"

    @api.depends("name", "category_id.code")
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"[{record.category_id.code}] {record.name}"

    def _get_id_number_validation_localdict(self):
        self.ensure_one()
        return {
            "id_number": self.name,
        }

    def _check_id_number_format_condition(self):
        self.ensure_one()
        validation_code = self.category_id.validation_code
        if not validation_code:
            return True
        localdict = self._get_id_number_validation_localdict()
        safe_eval(validation_code, localdict, mode="exec")
        return bool(localdict.get("result", True))

    @api.constrains("name", "category_id")
    def _check_id_number_format(self):
        for record in self.sudo():
            if not record._check_id_number_format_condition():
                category_name = record.category_id.name
                error_message = f"""
Context: Create or update partner identification number
Database ID: {record.id}
Problem: Number "{record.name}" is not valid for category "{category_name}"
Solution: Enter a number matching the format required by "{category_name}"
"""
                raise ValidationError(error_message)
