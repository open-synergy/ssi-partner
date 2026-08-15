# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PartnerEvaluationValueItem(models.Model):
    """
    Master data for one selectable qualitative value (e.g. a rating
    label) that can belong to a ``partner_evaluation_value_set``.
    """

    _name = "partner_evaluation_value_item"
    _inherit = ["mixin.master_data"]
    _description = "Partner Evaluation Value Item"
