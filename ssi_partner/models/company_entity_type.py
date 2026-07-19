# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class CompanyEntityType(models.Model):
    """Represents the legal entity form of a company partner (e.g.
    Limited Liability Company, Partnership, Cooperative). Used to
    classify company partners for reporting and document templates."""

    _name = "company_entity_type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Company Entity Type"
