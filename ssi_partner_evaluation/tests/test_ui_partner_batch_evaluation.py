# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPartnerBatchEvaluation(HttpSavepointCase):
    """Tour test for the ``partner_batch_evaluation`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create a type whose configurator picks one manual partner.

        The type's many2one configurator is set to ``manual`` with a
        single partner, so the tour's **Load** button deterministically
        populates ``partner_ids`` with that partner.
        """
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create(
            {"name": "TOUR Batch Evaluation Partner"}
        )
        cls.env["partner_evaluation_type"].create(
            {
                "name": "TOUR Batch Evaluation Type",
                "code": "/",
                "result_computation_code": "result = False",
                "partner_selection_method": "manual",
                "partner_ids": [(6, 0, [cls.partner.id])],
            }
        )

    def test_create(self):
        """Run the create tour for ``partner_batch_evaluation``.

        IK: docs/partner_batch_evaluation/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_evaluation_partner_batch_evaluation_create",
            login="admin",
        )
