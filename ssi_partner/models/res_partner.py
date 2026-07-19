# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from datetime import date

from odoo import api, fields, models
from odoo.fields import Domain


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
        comodel_name="res_partner_religion",
        help="Religion of the individual contact, used for demographic reporting.",
    )
    ethnicity_id = fields.Many2one(
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
        comodel_name="company_ownership_type",
        help="How the ownership of the company contact is structured "
        "(e.g. Private, State-Owned, Publicly Listed).",
    )
    entity_type_id = fields.Many2one(
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

    # Contact in several companies
    contact_type = fields.Selection(
        selection=[
            ("standalone", "Standalone Contact"),
            ("attached", "Attached to existing Contact"),
        ],
        compute="_compute_contact_type",
        store=True,
        index=True,
        default="standalone",
        help="A standalone contact represents a person on its own. An "
        "attached contact represents one of the several positions held "
        "by the same person, and keeps its name and title synchronized "
        "with its main contact.",
    )
    contact_id = fields.Many2one(
        string="Main Contact",
        comodel_name="res.partner",
        domain=[("is_company", "=", False), ("contact_type", "=", "standalone")],
        help="Standalone contact this position belongs to. Name and "
        "title are kept synchronized with it.",
    )
    other_contact_ids = fields.One2many(
        string="Others Positions",
        comodel_name="res.partner",
        inverse_name="contact_id",
        help="Other positions, in other companies, held by the same "
        "person as this standalone contact.",
    )

    # Identification numbers
    id_numbers = fields.One2many(
        string="ID Numbers",
        comodel_name="res_partner_id_number",
        inverse_name="partner_id",
        help="Identification numbers held by this contact, e.g. "
        "National ID, Tax ID, Driving License, Passport, or Business "
        "Registration Number.",
    )

    # Languages
    language_ids = fields.One2many(
        string="Languages",
        comodel_name="partner_language",
        inverse_name="partner_id",
        help="Languages spoken by this contact, each rated on the "
        "11-level ILR scale for reading, writing, speaking, and "
        "listening proficiency.",
    )

    # Academic history, certifications & work experience
    academic_ids = fields.One2many(
        string="Academic History",
        comodel_name="partner_academic",
        inverse_name="partner_id",
        help="Academic background of this contact, e.g. degrees "
        "obtained and fields of study.",
    )
    certification_ids = fields.One2many(
        string="Certifications",
        comodel_name="partner_certification",
        inverse_name="partner_id",
        help="Professional certifications held by this contact.",
    )
    experience_ids = fields.One2many(
        string="Work Experience",
        comodel_name="partner_experience",
        inverse_name="partner_id",
        help="Work experience history of this contact.",
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

    @api.depends("contact_id")
    def _compute_contact_type(self):
        for partner in self:
            partner.contact_type = "attached" if partner.contact_id else "standalone"

    @api.depends("contact_type", "contact_id")
    def _compute_commercial_partner(self):
        result = super()._compute_commercial_partner()
        for partner in self:
            if partner.contact_type == "attached" and not partner.parent_id:
                partner.commercial_partner_id = partner.contact_id
        return result

    @api.model
    def _contact_fields(self):
        """Fields kept synchronized between a standalone contact and the
        positions attached to it via ``contact_id``."""
        return ["name", "title_id"]

    def _contact_sync_from_parent(self):
        """Pull the synchronized fields from the main contact onto self,
        as if they were related fields."""
        self.ensure_one()
        if self.contact_id:
            contact_fields = self._contact_fields()
            sync_vals = self.contact_id._convert_fields_to_values(contact_fields)
            self.write(sync_vals)

    def update_contact(self, vals):
        """Push a downstream update of the synchronized fields onto self,
        guarded against recursive sync loops."""
        if self.env.context.get("__update_contact_lock"):
            return
        contact_fields = self._contact_fields()
        contact_vals = {
            field_name: vals[field_name]
            for field_name in contact_fields
            if field_name in vals
        }
        if contact_vals:
            self.with_context(__update_contact_lock=True).write(contact_vals)

    def _fields_sync(self, values):
        result = super()._fields_sync(values)
        contact_fields = self._contact_fields()
        if values.get("contact_id"):
            # From UPSTREAM: sync from the newly set main contact.
            self._contact_sync_from_parent()
        elif any(field_name in contact_fields for field_name in values):
            # To DOWNSTREAM: propagate to the main contact and siblings.
            update_ids = self.other_contact_ids.filtered(lambda p: not p.is_company)
            if self.contact_id:
                update_ids |= self.contact_id
            update_ids.update_contact(values)
        return result

    def _search(self, domain, offset=0, limit=None, order=None, **kw):
        show_all_positions = self.env.context.get("search_show_all_positions") or {}
        if not show_all_positions.get("is_set") or show_all_positions.get("set_value"):
            return super()._search(
                domain, offset=offset, limit=limit, order=order, **kw
            )

        # Display only standalone contacts matching `domain`, or standalone
        # contacts having an attached contact matching `domain`.
        no_filter_self = self.with_context(search_show_all_positions={"is_set": False})
        base_domain = Domain(domain)
        attached_query = no_filter_self._search(
            base_domain & Domain("contact_type", "=", "attached")
        )
        filtered_domain = (
            Domain("contact_type", "=", "standalone") & base_domain
        ) | Domain("other_contact_ids", "in", attached_query)
        return no_filter_self._search(
            filtered_domain, offset=offset, limit=limit, order=order, **kw
        )

    @api.onchange("contact_id")
    def onchange_name(self):
        if self.contact_id:
            self.name = self.contact_id.name

    @api.onchange("contact_type")
    def onchange_contact_id(self):
        if self.contact_type == "standalone":
            self.contact_id = False

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Core enforces `CHECK(type != 'contact' OR name IS NOT NULL)`
            # at the database level, which runs on the initial INSERT
            # itself. `_fields_sync()` only fills `name` from `contact_id`
            # *after* the row already exists, which is too late to satisfy
            # that constraint, so an attached contact created without an
            # explicit `name` must have it pre-filled here.
            if vals.get("contact_id") and not vals.get("name"):
                vals["name"] = self.browse(vals["contact_id"]).name
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
