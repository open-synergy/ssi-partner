# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class InsuranceProduct(models.Model):
    """
    Represents an insurance product offered by a provider.
    Contains details about coverage type and associated rates.
    """

    _name = "insurance_product"
    _inherit = ["mixin.master_data"]
    _description = "Insurance Product"

    provider_id = fields.Many2one(
        string="Provider",
        comodel_name="res.partner",
        required=True,
        help="Insurance provider offering this product.",
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        help="Related product in the product catalog.",
    )
    coverage_type_id = fields.Many2one(
        string="Coverage Type",
        comodel_name="insurance_product_coverage",
        required=True,
        help="Type of coverage provided by this insurance product.",
    )
    currency_id = fields.Many2one(
        string="Currency",
        comodel_name="res.currency",
        required=True,
        help="Currency used for the rates and cap amounts of this insurance product.",
    )
    rate_ids = fields.One2many(
        string="Rates",
        comodel_name="insurance_product.rate",
        inverse_name="insurance_product_id",
        help="Rate schedule for this insurance product.",
    )
