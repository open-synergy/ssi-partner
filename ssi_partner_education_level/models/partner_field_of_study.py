# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerFieldOfStudy(models.Model):
    """
    Represents a field of study (academic major) master data record.
    Used to classify the education background of a partner, and can be
    organized hierarchically through ``parent_id``/``child_ids``.
    """

    _name = "partner.field_of_study"
    _inherit = ["mixin.master_data"]
    _description = "Field of Study"

    parent_id = fields.Many2one(
        string="Parent",
        comodel_name="partner.field_of_study",
        ondelete="cascade",
        index=True,
    )
    child_ids = fields.One2many(
        string="Child",
        comodel_name="partner.field_of_study",
        inverse_name="parent_id",
    )
