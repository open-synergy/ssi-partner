# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class CompanyOwnershipType(models.Model):
    """Master data classifying the ownership structure of a company.

    Selected on company ``res.partner`` records (e.g. Private, State-Owned,
    Publicly Listed) to distinguish who ultimately owns the business
    partner.
    """

    _name = "company_ownership_type"
    _inherit = ["mixin.master_data"]
    _description = "Company Ownership Type"
