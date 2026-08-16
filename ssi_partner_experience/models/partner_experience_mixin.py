# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerExperienceMixin(models.AbstractModel):
    """
    Abstract base shared by the different kinds of contact background
    records (professional experience, academic history, certification).

    Provides the fields common to all of them: the owning ``partner_id``,
    the institution/employer (``partner_address_id``), location, the
    ``date_start``/``date_end`` pair inherited from ``mixin.date_duration``,
    an ``expire`` flag, and the ``active`` flag used to archive a record
    instead of deleting it. Concrete models add only the fields specific
    to their kind of record (e.g. ``job_position`` for
    ``partner.experience``, ``diploma`` for ``partner.academic``).
    """

    _name = "partner.experience.mixin"
    _inherit = [
        "mail.activity.mixin",
        "mail.thread",
        "mixin.date_duration",
    ]
    _description = "Abstract Class for Partner Experience"
    _date_end_required = False

    name = fields.Char(
        string="Name",
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
    )
    partner_address_id = fields.Many2one(
        comodel_name="res.partner",
        string="Address",
        help="Employer, School, University, " "Certification Authority",
        domain="[('is_company', '!=', False)]",
    )
    location = fields.Char(
        string="Location",
        help="Location",
    )
    expire = fields.Boolean(
        string="Expire",
        help="Expire",
        default=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
