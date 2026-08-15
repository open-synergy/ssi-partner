# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date
from math import ceil

from odoo import _, api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class PartnerBatchEvaluation(models.Model):
    """
    Represents a batch that groups several partner evaluations.

    Loads a set of partners eligible for a given evaluation type,
    creates one ``partner_evaluation`` per partner on confirmation,
    and offers bulk actions (start/confirm/approve/reject/cancel/
    restart) that dispatch to the underlying evaluations through
    queue jobs.
    """

    _name = "partner_batch_evaluation"
    _description = "Partner Batch Evaluation"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_confirm",
        "mixin.transaction_date_duration",
        "mixin.many2one_configurator",
        "mixin.localdict",
    ]
    _order = "date desc, id"

    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "done"
    _approval_state = "confirm"
    _after_approved_method = "action_done"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True
    _automatically_insert_multiple_approval_page = True
    _automatically_insert_done_policy_fields = False
    _automatically_insert_done_button = False

    _method_to_run_from_wizard = "action_cancel"

    _statusbar_visible_label = "draft,confirm,done"
    _policy_field_order = [
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "cancel_ok",
        "restart_ok",
        "done_ok",
        "manual_number_ok",
    ]

    _header_button_order = [
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_confirm",
        "dom_reject",
        "dom_done",
        "dom_cancel",
    ]

    # Sequence attribute
    _create_sequence_state = "done"

    type_id = fields.Many2one(
        comodel_name="partner_evaluation_type",
        string="Type",
        required=True,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    date = fields.Date(
        string="Date",
        required=True,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=lambda r: r._default_date(),
    )
    allowed_partner_ids = fields.Many2many(
        comodel_name="res.partner",
        string="Allowed Partners",
        compute="_compute_allowed_partner_ids",
        store=False,
        compute_sudo=True,
    )
    partner_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="rel_partner_batch_evaluation_2_partner",
        column1="batch_id",
        column2="partner_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    evaluation_ids = fields.One2many(
        string="Evaluations",
        comodel_name="partner_evaluation",
        inverse_name="batch_id",
        readonly=True,
    )

    # queue
    queue_job_batch_id = fields.Many2one(
        string="Queue Job Batch",
        comodel_name="queue.job.batch",
        readonly=True,
        copy=False,
    )

    queue_job_ids = fields.One2many(
        string="Queue Jobs",
        comodel_name="queue.job",
        related="queue_job_batch_id.job_ids",
        store=False,
        compute_sudo=True,
    )
    queue_job_batch_state = fields.Selection(
        string="Queue Job Batch State",
        related="queue_job_batch_id.state",
        store=True,
        compute_sudo=True,
    )

    @api.model
    def _default_date(self):
        """Return today as the default batch date.

        :return: a ``date`` instance
        """
        return date.today()

    def action_load_partner(self):
        """Populate ``partner_ids`` with the current allowed partners."""
        for record in self.sudo():
            record._load_partner()

    def action_confirm_evaluation(self):
        """Queue ``action_confirm`` for all open evaluations in batch."""
        for record in self.sudo():
            record._confirm_evaluation()

    def action_start_evaluation(self):
        """Queue ``action_open`` for all draft evaluations in batch."""
        for record in self.sudo():
            record._start_evaluation()

    def action_approve_evaluation(self):
        """Queue approval for all confirmed evaluations in batch."""
        for record in self.sudo():
            record._approve_evaluation()

    def action_reject_evaluation(self):
        """Queue rejection for all confirmed evaluations in batch."""
        for record in self.sudo():
            record._reject_evaluation()

    def action_cancel_evaluation(self):
        """Queue ``action_cancel`` for every non-cancelled evaluation."""
        for record in self.sudo():
            record._cancel_evaluation()

    def action_restart_evaluation(self):
        """Queue ``action_restart`` for all cancelled evaluations."""
        for record in self.sudo():
            record._restart_evaluation()

    def _create_job_batch(self, batch_name):
        """Create and link a new ``queue.job.batch`` for this record.

        :param batch_name: label used for the queue job batch
        """
        self.ensure_one()
        batch = self.env["queue.job.batch"].get_new_batch(batch_name)
        self.write(
            {
                "queue_job_batch_id": batch.id,
            }
        )

    def _process_evaluation_batch(
        self,
        action_method,
        state_filter,
        batch_action_name,
        split_action_name,
        state_condition=None,
    ):
        """Dispatch an evaluation action in split queue jobs.

        Creates a ``queue.job.batch``, filters ``evaluation_ids`` either
        by ``state_filter`` or by ``state_condition``, splits the
        resulting recordset into chunks of 100 records, and enqueues
        ``action_method`` for each chunk with a delayed job.

        :param action_method: name of the method to run on evaluations
        :param state_filter: evaluation state to select, or ``None``
            when ``state_condition`` is used instead
        :param batch_action_name: label used for the job batch name
        :param split_action_name: label used for each split job
            description
        :param state_condition: optional callable used to filter
            ``evaluation_ids`` instead of ``state_filter``
        """
        self.ensure_one()
        batch_name = f"{batch_action_name} batch evaluation ID {self.id}"
        self._create_job_batch(batch_name)
        data_per_split = 100
        if state_condition:
            effected_evaluations = self.evaluation_ids.filtered(state_condition)
        else:
            effected_evaluations = self.evaluation_ids.filtered(
                lambda r: r.state == state_filter
            )
        num_split = ceil(len(effected_evaluations) / data_per_split)
        for split_number in range(1, num_split + 1):
            evaluations = effected_evaluations[
                (data_per_split * split_number)
                - data_per_split : split_number * data_per_split
            ]
            description = f"{split_action_name} batch {self.id}"
            description += f" split {split_number}"
            getattr(
                evaluations.with_context(job_batch=self.queue_job_batch_id).with_delay(
                    description=_(description)
                ),
                action_method,
            )()
            self.queue_job_batch_id.enqueue()

    def _confirm_evaluation(self):
        """Enqueue ``action_confirm`` for open evaluations in batch."""
        self._process_evaluation_batch(
            action_method="action_confirm",
            state_filter="open",
            batch_action_name="Confirm",
            split_action_name="Confirm",
        )

    def _start_evaluation(self):
        """Enqueue ``action_open`` for draft evaluations in batch."""
        self._process_evaluation_batch(
            action_method="action_open",
            state_filter="draft",
            batch_action_name="Start",
            split_action_name="Start",
        )

    def _approve_evaluation(self):
        """Enqueue approval for confirmed evaluations in batch."""
        self._process_evaluation_batch(
            action_method="action_approve_approval",
            state_filter="confirm",
            batch_action_name="Approve",
            split_action_name="Approve",
        )

    def _reject_evaluation(self):
        """Enqueue rejection for confirmed evaluations in batch."""
        self._process_evaluation_batch(
            action_method="action_reject_approval",
            state_filter="confirm",
            batch_action_name="Reject",
            split_action_name="Reject",
        )

    def _cancel_evaluation(self):
        """Enqueue ``action_cancel`` for non-cancelled evaluations."""
        self._process_evaluation_batch(
            action_method="action_cancel",
            state_filter=None,
            batch_action_name="Cancel",
            split_action_name="Cancel",
            state_condition=lambda r: r.state != "cancel",
        )

    def _restart_evaluation(self):
        """Enqueue ``action_restart`` for cancelled evaluations."""
        self._process_evaluation_batch(
            action_method="action_restart",
            state_filter="cancel",
            batch_action_name="Restart",
            split_action_name="Restart",
        )

    @api.depends("type_id")
    def _compute_allowed_partner_ids(self):
        """Resolve partners matching the evaluation type configurator.

        Uses ``type_id``'s many2one configurator fields (selection
        method, manual recordset, domain, python code) to build the
        set of partners that may be loaded into this batch.
        """
        for record in self:
            result = False
            if record.type_id:
                result = record._m2o_configurator_get_filter(
                    object_name="res.partner",
                    method_selection=record.type_id.partner_selection_method,
                    manual_recordset=record.type_id.partner_ids,
                    domain=record.type_id.partner_domain,
                    python_code=record.type_id.partner_python_code,
                )
            record.allowed_partner_ids = result

    def action_open_evaluation(self):
        """Open the list view of evaluations belonging to this batch.

        :return: an ``ir.actions.act_window`` dict
        """
        for record in self.sudo():
            result = record._open_evaluation()
        return result

    def _open_evaluation(self):
        """Build the window action listing this batch's evaluations.

        :return: an ``ir.actions.act_window`` dict filtered by
            ``batch_id`` and pre-filled with this batch's defaults
        """
        self.ensure_one()
        action = self.env.ref(
            "ssi_partner_evaluation.partner_evaluation_action"
        ).read()[0]
        action["domain"] = [("batch_id", "=", self.id)]
        action["context"] = {
            "default_type_id": self.type_id.id,
            "default_date": self.date,
            "default_date_start": self.date_start,
            "default_date_end": self.date_end,
            "default_batch_id": self.id,
        }
        return action

    def _load_partner(self):
        """Replace ``partner_ids`` with the current allowed partners."""
        self.ensure_one()
        self.write({"partner_ids": [(6, 0, self.allowed_partner_ids.ids)]})

    @ssi_decorator.post_done_action()
    def _create_evaluations(self):
        """Create one ``partner_evaluation`` per partner on done.

        Runs after the batch reaches ``done``; each evaluation is
        created with this batch's type, dates, and target partner.
        """
        self.ensure_one()
        Evaluation = self.env["partner_evaluation"]
        for partner in self.partner_ids:
            data = {
                "type_id": self.type_id.id,
                "partner_id": partner.id,
                "date": self.date,
                "date_start": self.date_start,
                "date_end": self.date_end,
                "batch_id": self.id,
            }
            Evaluation.create(data)

    @ssi_decorator.post_cancel_action()
    def _delete_evaluation(self):
        """Delete every evaluation linked to this batch on cancel."""
        self.ensure_one()
        self.evaluation_ids.unlink()

    @api.model
    def _get_policy_field(self):
        res = super()._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "cancel_ok",
            "done_ok",
            "reject_ok",
            "restart_ok",
            "restart_approval_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch
