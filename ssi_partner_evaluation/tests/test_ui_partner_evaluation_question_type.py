# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPartnerEvaluationQuestionType(HttpSavepointCase):
    """Tour test for ``partner_evaluation_question_type`` creation."""

    def test_create(self):
        """Run the create tour for ``partner_evaluation_question_type``.

        IK: docs/partner_evaluation_question_type/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_evaluation_partner_evaluation_question_type_create",
            login="admin",
        )
