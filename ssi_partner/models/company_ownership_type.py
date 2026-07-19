# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class CompanyOwnershipType(models.Model):
    """Represents how ownership of a company partner is structured (e.g.
    Private, State-Owned, Publicly Listed). Used to classify company
    partners for reporting and eligibility rules."""

    _name = "company_ownership_type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Company Ownership Type"
