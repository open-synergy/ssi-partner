# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerEvaluationTypeQuestion(models.Model):
    """
    Detail line configuring one question of a
    ``partner_evaluation_type``.

    Each line links a ``partner_evaluation_question_type`` to the
    parent evaluation type in a given ``sequence``, and is used as
    the template to create a ``partner_evaluation.question`` when an
    evaluation of that type is opened.
    """

    _name = "partner_evaluation_type.question"
    _description = "Partner Evaluation Type - Question"
    _order = "type_id, sequence"

    type_id = fields.Many2one(
        string="Partner Evaluation Type",
        comodel_name="partner_evaluation_type",
        required=True,
        ondelete="cascade",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
        readonly=True,
    )
    question_type_id = fields.Many2one(
        string="Question Type",
        comodel_name="partner_evaluation_question_type",
        required=True,
    )

    def _create_evaluation_question(self, evaluation):
        """Create a ``partner_evaluation.question`` from this line.

        :param evaluation: the ``partner_evaluation`` record the new
            question line is attached to
        """
        self.ensure_one()
        self.env["partner_evaluation.question"].create(
            {
                "evaluation_id": evaluation.id,
                "sequence": self.sequence,
                "question_type_id": self.question_type_id.id,
            }
        )
