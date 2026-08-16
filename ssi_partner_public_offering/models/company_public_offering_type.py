# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class CompanyPublicOfferingType(models.Model):
    """
    Represents a type of public offering a company partner can be
    associated with (e.g. stock, bond). Used as master data for the
    ``public_offering_ids`` field on ``res.partner``.
    """

    _name = "company_public_offering_type"
    _inherit = ["mixin.master_data"]
    _description = "Company Public Offering Type"
