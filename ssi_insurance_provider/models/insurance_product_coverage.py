# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class InsuranceProductCoverage(models.Model):
    """
    Represents a type of coverage offered by insurance products.
    Used to classify insurance products by their coverage scope.
    """

    _name = "insurance_product_coverage"
    _inherit = ["mixin.master_data"]
    _description = "Insurance Product Coverage"
