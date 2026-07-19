# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class PartnerCertification(models.Model):
    """Represents a professional certification held by a partner (e.g. a
    license or qualification issued by an institution), used for
    recruitment, partner assessment, and expert profiling purposes."""

    _name = "partner_certification"
    _inherit = [
        "mixin.partner_experience",
    ]
    _description = "Partner Certification"

    certification = fields.Char(
        help="Name of the certification obtained, e.g. Certified Public Accountant.",
    )
