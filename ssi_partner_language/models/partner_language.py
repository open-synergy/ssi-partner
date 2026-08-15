# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models, tools
from odoo.exceptions import UserError

LANGUAGE_RATING = [
    ("0", "0 - No Proficiency"),
    ("0+", "0+ - Memorized Proficiency"),
    ("1", "1 - Elementary Proficiency"),
    ("1+", "1+ - Elementary Proficiency, Plus"),
    ("2", "2 - Limited Working Proficiency"),
    ("2+", "2+ - Limited Working Proficiency, Plus"),
    ("3", "3 - General Professional Proficiency"),
    ("3+", "3+ - General Professional Proficiency, Plus"),
    ("4", "4 - Advance Professional Proficiency"),
    ("4+", "4+ - Advance Professional Proficiency, Plus"),
    ("5", "5 - Funcionally Native Proficiency"),
]


class PartnerLanguage(models.Model):
    """
    Records a single language proficiency entry for a contact.
    Each record links one ``res.partner`` to one language, with
    separate proficiency ratings for reading, writing, speaking, and
    listening. Rows are managed inline from the Contacts form and have
    no standalone menu of their own.
    """

    _name = "partner.language"
    _description = "Partner Language"

    name = fields.Selection(
        string="Language",
        selection=tools.scan_languages(),
        required=True,
    )
    description = fields.Char(
        string="Description",
        size=64,
        required=False,
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
    )
    read_rating = fields.Selection(
        string="Reading",
        selection=LANGUAGE_RATING,
        required=True,
        default="0",
    )
    write_rating = fields.Selection(
        string="Writing",
        selection=LANGUAGE_RATING,
        required=True,
        default="0",
    )
    speak_rating = fields.Selection(
        string="Speaking",
        selection=LANGUAGE_RATING,
        required=True,
        default="0",
    )
    listen_rating = fields.Selection(
        string="Listening",
        selection=LANGUAGE_RATING,
        required=True,
        default="0",
    )

    @api.constrains(
        "partner_id",
        "name",
    )
    def _check_no_duplicate_language(self):
        """Forbid a partner from having the same language twice.

        Raised as a ``UserError`` when another ``partner.language``
        record already exists for the same ``partner_id`` and
        ``name`` combination.

        :raises UserError: when a duplicate language entry is found
        """
        obj_language = self.env["partner.language"]
        for language in self:
            criteria = [
                ("id", "!=", language.id),
                ("partner_id", "=", language.partner_id.id),
                ("name", "=", language.name),
            ]
            result = obj_language.search_count(criteria)
            if result > 0:
                msg = _("No duplicate language")
                raise UserError(msg)
