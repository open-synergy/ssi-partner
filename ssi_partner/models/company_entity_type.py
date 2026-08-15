# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class CompanyEntityType(models.Model):
    """Master data classifying the legal entity type of a company.

    Selected on company ``res.partner`` records (e.g. Limited Liability
    Company, Cooperative, Sole Proprietorship) to distinguish the legal
    form under which a business partner operates.
    """

    _name = "company_entity_type"
    _inherit = ["mixin.master_data"]
    _description = "Company Entity Type"
