# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PortalPartnerExperience(models.Model):
    """Expose ``partner.experience`` records to the customer portal.

    Same PostgreSQL table as ``partner.experience`` (``_table =
    "partner_experience"``), so no data is duplicated. This model only
    exists so portal-specific access rights (``ir.model.access.csv``,
    ``ir.rule``) can be attached without loosening the backend model.
    """

    _name = "portal_partner_experience"
    _inherit = ["partner.experience"]
    _description = "Portal Partner Experience"
    _table = "partner_experience"
    _order = "date_start"
