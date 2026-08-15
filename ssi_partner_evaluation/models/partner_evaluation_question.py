# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class PartnerEvaluationQuestion(models.Model):
    """
    Represents one answered question line of a ``partner_evaluation``.

    Holds both manual and automatically computed qualitative/
    quantitative values; the effective value used downstream depends
    on the question type's ``mode`` (manual or auto).
    """

    _name = "partner_evaluation.question"
    _description = "Partner Evaluation - Question"
    _inherit = [
        "mixin.localdict",
    ]
    _order = "evaluation_id, sequence"

    evaluation_id = fields.Many2one(
        string="# Evaluation",
        comodel_name="partner_evaluation",
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
        string="Question",
        comodel_name="partner_evaluation_question_type",
        required=True,
    )
    type = fields.Selection(
        related="question_type_id.type",
        store=False,
        compute_sudo=True,
    )
    mode = fields.Selection(
        related="question_type_id.mode",
        store=False,
        compute_sudo=True,
    )
    manual_qualitative_value_id = fields.Many2one(
        string="Manual Qualitative Value",
        comodel_name="partner_evaluation_value_item",
    )
    automatic_qualitative_value_id = fields.Many2one(
        string="Automatic Qualitative Value",
        comodel_name="partner_evaluation_value_item",
        compute="_compute_automatic_value",
        store=True,
        compute_sudo=True,
    )
    qualitative_value_id = fields.Many2one(
        string="Qualitative Value",
        comodel_name="partner_evaluation_value_item",
        compute="_compute_qualitative_value_id",
        store=True,
        compute_sudo=True,
    )
    manual_quantitative_value = fields.Float(
        string="Manual Quantitative Value",
    )
    automatic_quantitative_value = fields.Float(
        string="Automatic Quantitative Value",
        compute="_compute_automatic_value",
        store=True,
        compute_sudo=True,
    )
    quantitative_value = fields.Float(
        string="Quantitative Value",
        compute="_compute_quantitative_value",
        store=True,
        compute_sudo=True,
    )
    value = fields.Char(
        string="Value",
        compute="_compute_value",
        store=False,
        compute_sudo=True,
    )

    @api.depends(
        "manual_qualitative_value_id",
        "automatic_qualitative_value_id",
        "mode",
    )
    def _compute_qualitative_value_id(self):
        """Pick the qualitative value matching the question's mode.

        Uses ``manual_qualitative_value_id`` when ``mode`` is
        ``"manual"``, otherwise falls back to
        ``automatic_qualitative_value_id``.
        """
        for record in self:
            result = False
            if record.mode == "manual":
                result = record.manual_qualitative_value_id
            else:
                result = record.automatic_qualitative_value_id
            record.qualitative_value_id = result

    @api.depends(
        "manual_quantitative_value",
        "automatic_quantitative_value",
        "mode",
    )
    def _compute_quantitative_value(self):
        """Pick the quantitative value matching the question's mode.

        Uses ``manual_quantitative_value`` when ``mode`` is
        ``"manual"``, otherwise falls back to
        ``automatic_quantitative_value``.
        """
        for record in self:
            result = 0.0
            if record.mode == "manual":
                result = record.manual_quantitative_value
            else:
                result = record.automatic_quantitative_value
            record.quantitative_value = result

    @api.depends(
        "question_type_id",
        "type",
        "mode",
    )
    def _compute_automatic_value(self):
        """Evaluate ``question_type_id.computation_code`` for the row.

        Executes the question type's computation code in a sandboxed
        ``localdict``; the code is expected to set a ``result``
        variable. The resolved value is stored on
        ``automatic_qualitative_value_id`` or
        ``automatic_quantitative_value`` depending on ``type``. Any
        exception during evaluation is swallowed and treated as no
        result.
        """
        for record in self:
            result = False

            if record.mode != "auto":
                record.automatic_qualitative_value_id = result
                record.automatic_quantitative_value = result

            localdict = record._get_default_localdict()
            try:
                safe_eval(
                    record.question_type_id.computation_code,
                    localdict,
                    mode="exec",
                    nocopy=True,
                )
                result = localdict["result"]
            except Exception:
                result = False

            if record.type == "qualitative":
                record.automatic_qualitative_value_id = result
            else:
                record.automatic_quantitative_value = result

    @api.depends(
        "type",
        "qualitative_value_id",
        "quantitative_value",
    )
    def _compute_value(self):
        """Build the display value shown in the question's list view.

        Returns ``quantitative_value`` as-is for quantitative
        questions, or ``qualitative_value_id``'s display name for
        qualitative ones.
        """
        for record in self:
            result = ""
            if record.type == "quantitative":
                result = record.quantitative_value
            else:
                result = (
                    record.qualitative_value_id
                    and record.qualitative_value_id.display_name
                    or ""
                )
            record.value = result

    def _compute_result(self):
        """Recompute this question's automatic and derived values."""
        self.ensure_one()
        self._compute_automatic_value()
        self._compute_qualitative_value_id()
        self._compute_quantitative_value()
        self._compute_value()
