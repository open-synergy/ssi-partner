# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    """
    Adds partner evaluation traceability to ``res.partner``.

    Exposes the evaluations and per-type result trackers linked to
    the partner, plus a computed set of evaluation tags derived from
    the latest result of each tracker.
    """

    _name = "res.partner"
    _inherit = "res.partner"

    partner_evaluation_result_ids = fields.One2many(
        string="Partner Evaluation Results",
        comodel_name="res.partner.evaluation_result",
        inverse_name="partner_id",
        readonly=True,
    )

    partner_evaluation_ids = fields.One2many(
        string="Partner Evaluations",
        comodel_name="partner_evaluation",
        inverse_name="partner_id",
        readonly=True,
    )
    evaluation_tag_ids = fields.Many2many(
        string="Evaluation Tags",
        comodel_name="res.partner.category",
        compute="_compute_evaluation_tag_ids",
        store=True,
        compute_sudo=True,
        relation="rel_partner_2_evaluation_tag",
        column1="res_partner_id",
        column2="tag_id",
    )

    @api.depends(
        "partner_evaluation_result_ids",
        "partner_evaluation_result_ids.latest_evaluation_id",
    )
    def _compute_evaluation_tag_ids(self):
        """Collect the tags of the partner's latest evaluation results.

        For each ``res.partner.evaluation_result`` tracker of the
        partner, takes ``latest_evaluation_id.final_result_id.tag_id``
        and merges the tags across all trackers.
        """
        Evaluation = self.env["res.partner.evaluation_result"]
        for record in self:
            result = []
            criteria = [
                ("partner_id", "=", record.id),
            ]
            evaluations = Evaluation.search(criteria)
            if len(evaluations) > 0:
                result = evaluations.mapped(
                    "latest_evaluation_id.final_result_id.tag_id"
                )
            record.evaluation_tag_ids = result

    def _get_partner_evaluation_result(self, evaluation_type):
        """Return this partner's result tracker for an evaluation type.

        :param evaluation_type: a ``partner_evaluation_type`` record
        :return: the matching ``res.partner.evaluation_result``
            record, or ``False`` when none exists yet
        """
        self.ensure_one()
        result = False
        evaluations = self.partner_evaluation_result_ids.filtered(
            lambda r: r.type_id.id == evaluation_type.id
        )
        if evaluations:
            result = evaluations[0]

        return result
