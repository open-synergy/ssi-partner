# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerAcademic(models.Model):
    """
    Records one academic history entry of a contact.

    Each record represents a study period of the ``res.partner``
    referenced in ``partner_id`` at the institution stored in
    ``partner_address_id`` (inherited from ``partner.experience.mixin``),
    together with the diploma, education level, field of study, GPA, and
    activities/associations of that period.
    """

    _name = "partner.academic"
    _inherit = "partner.experience.mixin"
    _description = "Contact's Academic Experience"

    diploma = fields.Char(
        string="Diploma Number",
    )
    education_level_id = fields.Many2one(
        string="Education Level",
        comodel_name="partner.formal_education_level",
    )
    field_of_study_id = fields.Many2one(
        string="Field of Study",
        comodel_name="partner.field_of_study",
    )
    gpa = fields.Float(
        string="Latest GPA",
    )
    activities = fields.Text(
        string="Activities and associations",
    )
