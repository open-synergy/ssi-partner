# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PortalIdentificationNumber(models.Model):
    """
    Portal-facing view of ``res.partner.id_number`` used by the
    identification self-service pages under ``/my/identifications``.
    Shares the same database table as ``res.partner.id_number`` so
    portal users manage the same records exposed in the backend,
    scoped to their own partner through the security rules of this
    module.
    """

    _name = "portal_identification_number"
    _inherit = ["res.partner.id_number"]
    _description = "Portal Identification Number"
    _table = "res_partner_id_number"
    _order = "category_id"
