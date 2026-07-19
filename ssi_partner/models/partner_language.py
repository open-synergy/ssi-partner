# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
from odoo.exceptions import UserError

ILR_RATING_SELECTION = [
    ("0", "0 - No Proficiency"),
    ("0+", "0+ - Memorized Proficiency"),
    ("1", "1 - Elementary Proficiency"),
    ("1+", "1+ - Elementary Proficiency, Plus"),
    ("2", "2 - Limited Working Proficiency"),
    ("2+", "2+ - Limited Working Proficiency, Plus"),
    ("3", "3 - General Professional Proficiency"),
    ("3+", "3+ - General Professional Proficiency, Plus"),
    ("4", "4 - Advanced Professional Proficiency"),
    ("4+", "4+ - Advanced Professional Proficiency, Plus"),
    ("5", "5 - Functionally Native Proficiency"),
]


class PartnerLanguage(models.Model):
    """Records a language spoken by an individual partner, together
    with its reading, writing, speaking, and listening proficiency on
    the 11-level ILR (Interagency Language Roundtable) scale. Used for
    recruitment, assignment, and partner assessment purposes. A given
    language can only be recorded once per partner."""

    _name = "partner_language"
    _description = "Partner Language"
    _order = "partner_id, name"

    name = fields.Selection(
        selection="_get_lang_selection",
        string="Language",
        required=True,
        help="Language spoken by the partner, sourced from the "
        "languages installed on this database.",
    )
    description = fields.Char(
        help="Free-text note about this language proficiency, e.g. "
        "the context in which it was learned.",
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
        help="Partner this language proficiency record belongs to.",
    )
    read_rating = fields.Selection(
        selection=ILR_RATING_SELECTION,
        string="Reading",
        required=True,
        default="0",
        help="Reading proficiency rated on the 11-level ILR scale.",
    )
    write_rating = fields.Selection(
        selection=ILR_RATING_SELECTION,
        string="Writing",
        required=True,
        default="0",
        help="Writing proficiency rated on the 11-level ILR scale.",
    )
    speak_rating = fields.Selection(
        selection=ILR_RATING_SELECTION,
        string="Speaking",
        required=True,
        default="0",
        help="Speaking proficiency rated on the 11-level ILR scale.",
    )
    listen_rating = fields.Selection(
        selection=ILR_RATING_SELECTION,
        string="Listening",
        required=True,
        default="0",
        help="Listening proficiency rated on the 11-level ILR scale.",
    )

    @api.model
    def _get_lang_selection(self):
        return self.env["res.lang"].get_installed()

    @api.constrains("partner_id", "name")
    def _check_no_duplicate_language(self):
        for record in self:
            criteria = [
                ("id", "!=", record.id),
                ("partner_id", "=", record.partner_id.id),
                ("name", "=", record.name),
            ]
            if self.search_count(criteria) > 0:
                language_name = dict(record._get_lang_selection()).get(
                    record.name, record.name
                )
                partner_name = record.partner_id.name
                error_message = f"""
Context: Create or update partner language
Database ID: {record.id}
Problem: Language "{language_name}" is already recorded for partner "{partner_name}"
Solution: Choose a different language, or edit the existing record instead
"""
                raise UserError(error_message)
