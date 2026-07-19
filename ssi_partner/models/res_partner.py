# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from datetime import date

from odoo import api, fields, models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = [
        "res.partner",
    ]

    type = fields.Selection(
        selection_add=[
            ("branch", "Branch Address"),
        ],
        ondelete={"branch": "cascade"},
    )

    # Individual attributes
    gender = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        help="Gender of the individual contact.",
    )
    birthdate_date = fields.Date(
        string="Date of Birth",
        help="Date of birth of the individual contact.",
    )
    age = fields.Integer(
        compute="_compute_age",
        compute_sudo=True,
        help="Age computed from the date of birth as of today. Not "
        "stored because its value changes over time.",
    )
    birth_city = fields.Char(
        string="City of Birth",
        help="City where the individual contact was born.",
    )
    birth_state_id = fields.Many2one(
        string="State of Birth",
        comodel_name="res.country.state",
        help="State/province where the individual contact was born.",
    )
    birth_country_id = fields.Many2one(
        string="Country of Birth",
        comodel_name="res.country",
        help="Country where the individual contact was born.",
    )
    nationality_id = fields.Many2one(
        string="Nationality",
        comodel_name="res.country",
        help="Country of nationality/citizenship of the individual contact.",
    )
    blood_type = fields.Selection(
        selection=[
            ("a", "A"),
            ("b", "B"),
            ("o", "O"),
            ("ab", "AB"),
        ],
        help="Blood type of the individual contact.",
    )
    blood_type_rhesus = fields.Selection(
        selection=[
            ("positive", "+"),
            ("negative", "-"),
        ],
        string="Rhesus",
        help="Rhesus factor of the individual contact's blood type.",
    )
    religion_id = fields.Many2one(
        string="Religion",
        comodel_name="res_partner_religion",
        help="Religion of the individual contact, used for demographic reporting.",
    )
    ethnicity_id = fields.Many2one(
        string="Ethnicity",
        comodel_name="res_partner_ethnicity",
        help="Ethnicity of the individual contact, used for demographic reporting.",
    )
    marital = fields.Selection(
        selection=[
            ("single", "Single"),
            ("married", "Married"),
            ("cohabitant", "Legal Cohabitant"),
            ("widower", "Widower"),
            ("divorced", "Divorced"),
        ],
        string="Marital Status",
        default="single",
        help="Marital status of the individual contact.",
    )
    spouse_complete_name = fields.Char(
        string="Spouse's Name",
        help="Full name of the spouse. Only relevant when the contact is "
        "married or a legal cohabitant.",
    )
    spouse_birthdate = fields.Date(
        string="Spouse's Birthdate",
        help="Date of birth of the spouse. Only relevant when the "
        "contact is married or a legal cohabitant.",
    )
    title_id = fields.Many2one(
        string="Title",
        comodel_name="res.partner.title",
        ondelete="restrict",
        compute="_compute_title_id",
        store=True,
        compute_sudo=True,
        precompute=True,
        readonly=False,
        help="Honorific title of the individual contact (e.g. Doctor, "
        "Madam). Automatically cleared when the contact is a company.",
    )

    # Company attributes
    ownership_type_id = fields.Many2one(
        string="Ownership Type",
        comodel_name="company_ownership_type",
        help="How the ownership of the company contact is structured "
        "(e.g. Private, State-Owned, Publicly Listed).",
    )
    entity_type_id = fields.Many2one(
        string="Entity Type",
        comodel_name="company_entity_type",
        help="Legal entity form of the company contact (e.g. Limited "
        "Liability Company, Partnership, Cooperative).",
    )
    secondary_industry_ids = fields.Many2many(
        string="Secondary Industries",
        comodel_name="res.partner.industry",
        relation="rel_res_partner_2_secondary_industry",
        help="Additional industries the company contact operates in, "
        "besides its main industry.",
    )

    @api.depends("birthdate_date")
    def _compute_age(self):
        today = date.today()
        for partner in self:
            if not partner.birthdate_date:
                partner.age = 0
                continue
            birthdate = partner.birthdate_date
            years = today.year - birthdate.year
            if (today.month, today.day) < (birthdate.month, birthdate.day):
                years -= 1
            partner.age = years

    @api.depends("is_company")
    def _compute_title_id(self):
        for partner in self:
            if partner.is_company:
                partner.title_id = False

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        # `title_id` is a precomputed, user-editable field: when
        # `is_company` and `title_id` are both given explicitly in the
        # same `create()` call, the ORM stores the given `title_id`
        # as-is and never re-runs `_compute_title_id` for it. Enforce
        # the "no title on a company" invariant explicitly here so it
        # also holds right after creation, not only after a later
        # `write()` of `is_company`.
        records.filtered("is_company").title_id = False
        return records

    def action_open_contact_address(self):
        for record in self.sudo():
            result = record._open_contact_address()
        return result

    def _open_contact_address(self):
        self.ensure_one()
        waction = self.env.ref("contacts.action_contacts").read()[0]
        waction.update(
            {
                "view_mode": "list,form",
                "domain": [("id", "child_of", self.id), ("id", "!=", self.id)],
                "context": {},
            }
        )
        return waction
