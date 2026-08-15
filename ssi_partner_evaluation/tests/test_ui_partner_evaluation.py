# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPartnerEvaluation(HttpSavepointCase):
    """Tour test for the ``partner_evaluation`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the type and partner picked by the tour's dropdowns."""
        super().setUpClass()
        cls.env["partner_evaluation_type"].create(
            {
                "name": "TOUR Evaluation Type",
                "code": "/",
                "result_computation_code": "result = False",
            }
        )
        cls.env["res.partner"].create({"name": "TOUR Evaluation Partner"})

    def test_create(self):
        """Run the create tour for ``partner_evaluation``.

        IK: docs/partner_evaluation/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_evaluation_partner_evaluation_create",
            login="admin",
        )
