# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PortalPartnerAcademic(models.Model):
    """Expose ``partner.academic`` records to the customer portal.

    Same PostgreSQL table as ``partner.academic`` (``_table =
    "partner_academic"``), so no data is duplicated. This model only
    exists so portal-specific access rights (``ir.model.access.csv``,
    ``ir.rule``) can be attached without loosening the backend model.
    """

    _name = "portal_partner_academic"
    _inherit = ["partner.academic"]
    _description = "Portal Partner Academic"
    _table = "partner_academic"
    _order = "date_start"
