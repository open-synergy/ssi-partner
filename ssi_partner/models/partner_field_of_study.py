# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class PartnerFieldOfStudy(models.Model):
    """Represents a field of study (e.g. Computer Science, Civil
    Engineering, Accounting) that can be assigned to a partner's academic
    history. Organized hierarchically so a broad field can be broken down
    into narrower specializations."""

    _name = "partner_field_of_study"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Partner Field of Study"
    _parent_store = True

    parent_id = fields.Many2one(
        comodel_name="partner_field_of_study",
        ondelete="cascade",
        index=True,
        help="Broader field of study this one specializes from. Leave "
        "empty for a top-level field of study.",
    )
    child_ids = fields.One2many(
        string="Specializations",
        comodel_name="partner_field_of_study",
        inverse_name="parent_id",
        help="Narrower specializations under this field of study.",
    )
    parent_path = fields.Char(
        index=True,
        help="Materialized path used internally to query the field of "
        "study hierarchy efficiently.",
    )
