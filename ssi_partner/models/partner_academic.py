# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class PartnerAcademic(models.Model):
    """Represents an academic history entry of a partner (e.g. a
    completed or ongoing degree), used for recruitment, partner
    assessment, and expert profiling purposes."""

    _name = "partner_academic"
    _inherit = [
        "mixin.partner_experience",
    ]
    _description = "Partner Academic History"

    diploma = fields.Char(
        help="Name of the diploma/degree obtained, e.g. Bachelor of Science.",
    )
    education_level_id = fields.Many2one(
        comodel_name="partner_formal_education_level",
        help="Formal education level of this academic history entry.",
    )
    field_of_study_id = fields.Many2one(
        comodel_name="partner_field_of_study",
        help="Field of study of this academic history entry.",
    )
    gpa = fields.Float(
        string="GPA",
        help="Grade point average obtained, if applicable.",
    )
    activities = fields.Text(
        string="Extracurricular Activities",
        help="Extracurricular activities and organizations the partner "
        "was involved in during this academic history entry.",
    )
