# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class InsuranceProductRate(models.Model):
    _name = "insurance_product.rate"
    _description = "Insurance Product - Rate"
    _order = "insurance_product_id, effective_date"

    insurance_product_id = fields.Many2one(
        string="Insurance Product",
        comodel_name="insurance_product",
        required=True,
        ondelete="cascade",
        help="Insurance product this rate belongs to.",
    )
    effective_date = fields.Date(
        string="Effective Date",
        required=True,
        help="Date from which this rate becomes effective.",
    )
    employer_rate = fields.Float(
        string="Employer Rate (%)",
        required=True,
        help="Rate contribution percentage by the employer.",
    )
    employee_rate = fields.Float(
        string="Employee Rate (%)",
        required=True,
        help="Rate contribution percentage by the employee.",
    )
    total_rate = fields.Float(
        string="Total Rate (%)",
        compute="_compute_total_rate",
        store=True,
        help="Total rate computed from employer and employee rates.",
    )
    cap_amount = fields.Float(
        string="Cap Amount",
        help="Maximum amount cap for this rate.",
    )

    @api.depends("employer_rate", "employee_rate")
    def _compute_total_rate(self):
        for rec in self:
            rec.total_rate = rec.employer_rate + rec.employee_rate
