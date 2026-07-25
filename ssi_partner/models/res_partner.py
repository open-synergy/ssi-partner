# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

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
