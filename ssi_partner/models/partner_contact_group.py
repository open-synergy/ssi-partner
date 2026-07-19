# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class PartnerContactGroup(models.Model):
    """Groups a subset of contacts belonging to the same commercial
    entity (e.g. the people relevant to a particular deal or
    department), so that a set of ``res.partner`` contacts can be
    handled together instead of one by one."""

    _name = "partner_contact_group"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Partner Contact Group"

    commercial_contact_id = fields.Many2one(
        comodel_name="res.partner",
        domain=[("parent_id", "=", False)],
        required=True,
        help="Top-level commercial entity (company or standalone "
        "individual) that owns the contacts allowed in this group.",
    )
    allowed_contact_ids = fields.Many2many(
        string="Allowed Contacts",
        comodel_name="res.partner",
        compute="_compute_allowed_contact_ids",
        compute_sudo=True,
        store=False,
        help="Children of the commercial contact that can be selected "
        "in Contacts. Used to restrict the selection widget, not "
        "meant to be edited directly.",
    )
    contact_ids = fields.Many2many(
        string="Contacts",
        comodel_name="res.partner",
        relation="rel_partner_contact_group_2_partner",
        required=True,
        help="Contacts belonging to the commercial contact that are "
        "part of this group.",
    )

    @api.depends("commercial_contact_id")
    def _compute_allowed_contact_ids(self):
        for record in self:
            record.allowed_contact_ids = record.commercial_contact_id.child_ids

    @api.onchange("commercial_contact_id")
    def onchange_contact_ids(self):
        self.contact_ids = False
