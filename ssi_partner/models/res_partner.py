# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    """Extend ``res.partner`` with SSI personal, company, and family data.

    Adds identity fields (nickname, blood type, religion, ethnicity,
    marital status), family relations (father, mother, guardian,
    spouse, children, wards), and company classification fields
    (ownership type, entity type) used across SSI modules.
    """

    _inherit = "res.partner"

    nickname = fields.Char(
        string="Nickname",
        required=False,
        help="Familiar or informal name the individual contact is "
        "commonly called by, as opposed to their official name.",
    )
    type = fields.Selection(
        selection_add=[
            ("branch", "Branch Address"),
        ],
    )

    ownership_type_id = fields.Many2one(
        string="Ownership Type",
        comodel_name="company_ownership_type",
    )
    entity_type_id = fields.Many2one(
        string="Entity Type",
        comodel_name="company_entity_type",
    )
    blood_type = fields.Selection(
        string="Blood Type (ABO)",
        selection=[
            ("A", "A"),
            ("B", "B"),
            ("0", "O"),
            ("AB", "AB"),
        ],
        required=False,
    )
    blood_type_rhesus = fields.Selection(
        string="Blood Type (Rh)",
        selection=[
            ("positive", "+"),
            ("negative", "-"),
        ],
        required=False,
    )
    religion_id = fields.Many2one(
        string="Religion",
        comodel_name="res_partner_religion",
    )
    ethnicity_id = fields.Many2one(
        string="Ethnicity",
        comodel_name="res_partner_ethnicity",
    )
    marital = fields.Selection(
        string="Marital Status",
        selection=[
            ("single", "Single"),
            ("married", "Married"),
            ("cohabitant", "Legal Cohabitant"),
            ("widower", "Widower"),
            ("divorced", "Divorced"),
        ],
        default="single",
        required=False,
    )
    spouse_complete_name = fields.Char(
        string="Spouse Complete Name",
        required=False,
    )
    spouse_birthdate = fields.Date(
        string="Spouse Birthdate",
        required=False,
    )
    father_id = fields.Many2one(
        string="Father",
        comodel_name="res.partner",
        domain=[("is_company", "=", False)],
        required=False,
        help="Father of this contact. Only individual contacts can be selected.",
    )
    mother_id = fields.Many2one(
        string="Mother",
        comodel_name="res.partner",
        domain=[("is_company", "=", False)],
        required=False,
        help="Mother of this contact. Only individual contacts can be selected.",
    )
    guardian_id = fields.Many2one(
        string="Guardian",
        comodel_name="res.partner",
        domain=[("is_company", "=", False)],
        required=False,
        help="Legal guardian of this contact. Only individual contacts can be "
        "selected.",
    )
    spouse_id = fields.Many2one(
        string="Spouse",
        comodel_name="res.partner",
        domain=[("is_company", "=", False)],
        required=False,
        help="Spouse of this contact, linked as a partner record. Only "
        "individual contacts can be selected. This does not replace or "
        "synchronize with Spouse Complete Name/Spouse Birthdate.",
    )
    children_ids = fields.Many2many(
        string="Children",
        comodel_name="res.partner",
        relation="rel_partner_2_children",
        column1="parent_id",
        column2="children_id",
        domain=[("is_company", "=", False)],
        required=False,
        help="Children of this contact. Only individual contacts can be "
        "selected. Many2many is used because a single contact record cannot "
        "hold a dedicated parent field for both father and mother.",
    )
    ward_ids = fields.One2many(
        string="Wards",
        comodel_name="res.partner",
        inverse_name="guardian_id",
        help="Contacts that have this contact set as their legal guardian. "
        "This is the automatic inverse of the Guardian field and is "
        "maintained entirely by the ORM.",
    )

    @api.constrains(
        "father_id", "mother_id", "guardian_id", "spouse_id", "children_ids"
    )
    def _check_family_self_reference(self):
        for record in self:
            for field_name, field_label in (
                ("father_id", "Father"),
                ("mother_id", "Mother"),
                ("guardian_id", "Guardian"),
                ("spouse_id", "Spouse"),
            ):
                related = record[field_name]
                if related and related.id == record.id:
                    error_message = """
Context: Set %s
Database ID: %s
Problem: A contact cannot be set as its own %s
Solution: Choose a different contact
""" % (
                        field_label,
                        record.id,
                        field_label.lower(),
                    )
                    raise ValidationError(_(error_message))

            if record.id in record.children_ids.ids:
                error_message = """
Context: Set Children
Database ID: %s
Problem: A contact cannot be added to its own children
Solution: Remove this contact from its own children list
""" % (
                    record.id,
                )
                raise ValidationError(_(error_message))

    def _sync_parent_to_children(self, old_father, old_mother):
        """Keep father_id/mother_id in sync with the parent's children_ids.

        `self` is a single child record. `old_father`/`old_mother` are the
        father_id/mother_id recordsets held by the record *before* the
        current create()/write() was applied (empty recordsets on create).
        Only father_id/mother_id feed children_ids - guardian_id is inverted
        separately by the ward_ids One2many and must not be touched here.
        """
        self.ensure_one()
        new_parents = self.father_id | self.mother_id
        old_parents = (old_father | old_mother) - new_parents

        for new_parent in new_parents:
            if self.id not in new_parent.sudo().children_ids.ids:
                new_parent.sudo().write({"children_ids": [(4, self.id)]})

        for old_parent in old_parents:
            old_parent.sudo().write({"children_ids": [(3, self.id)]})

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        empty = self.env["res.partner"]
        for record, vals in zip(records, vals_list):
            if "father_id" in vals or "mother_id" in vals:
                record._sync_parent_to_children(empty, empty)
        return records

    def write(self, vals):
        if "father_id" in vals or "mother_id" in vals:
            previous_parents = {
                record.id: (record.father_id, record.mother_id) for record in self
            }
            result = super().write(vals)
            for record in self:
                old_father, old_mother = previous_parents[record.id]
                record._sync_parent_to_children(old_father, old_mother)
            return result
        return super().write(vals)

    def link_child(self, child, relationship=False):
        """Link `child` to `self` as father, mother, guardian, or plain child.

        `self` is the parent/guardian (ensure_one) and `child` is a single
        res.partner record (ensure_one). Fields that are already set on
        `child` are never overwritten. Returns True.
        """
        self.ensure_one()
        child.ensure_one()

        if child == self:
            error_message = """
Context: Link Child
Database ID: %s
Problem: A contact cannot be linked as its own child
Solution: Choose a different contact as child
""" % (
                self.id,
            )
            raise ValidationError(_(error_message))

        if relationship == "father":
            if not child.father_id:
                child.write({"father_id": self.id})
        elif relationship == "mother":
            if not child.mother_id:
                child.write({"mother_id": self.id})
        elif relationship == "guardian":
            if not child.guardian_id:
                child.write({"guardian_id": self.id})

        if relationship != "guardian":
            if child.id not in self.children_ids.ids:
                self.sudo().write({"children_ids": [(4, child.id)]})

        return True

    def action_open_contact_address(self):
        for record in self.sudo():
            result = record._open_contact_address()
        return result

    def _open_contact_address(self):
        waction = self.env.ref("contacts.action_contacts").read()[0]
        waction.update(
            {
                "view_mode": "tree,form",
                "domain": [("id", "child_of", self.id), ("id", "!=", self.id)],
                "context": {},
            }
        )
        return waction
