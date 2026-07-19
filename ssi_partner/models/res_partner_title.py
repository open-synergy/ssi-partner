# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResPartnerTitle(models.Model):
    """Represents an honorific title used to qualify a contact's name
    (e.g. Doctor, Madam, Professor).

    Odoo 19 removed the core ``res.partner.title`` model, while many
    reports and addons still reference it by its legacy dotted name. This
    model re-introduces it as a plain model (intentionally **not**
    ``mixin.master_data``, and intentionally keeping the dotted name as an
    exception to the usual underscore naming convention) so that those
    references keep working.
    """

    _name = "res.partner.title"
    _description = "Contact Title"
    _order = "sequence, name"

    _partner_title_name_uniq = models.Constraint(
        "UNIQUE(name)",
        "Another title with that name already exists.",
    )

    name = fields.Char(
        string="Title",
        required=True,
        translate=True,
        help="Name of the title, displayed after the contact's name (e.g. Doctor).",
    )
    shortcut = fields.Char(
        string="Abbreviation",
        translate=True,
        help="Short form of the title, used when space is limited (e.g. Dr.).",
    )
    active = fields.Boolean(
        default=True,
        help="Uncheck to archive this title without deleting it.",
    )
    sequence = fields.Integer(
        default=0,
        help="Determines the display order of titles in selection lists.",
    )
