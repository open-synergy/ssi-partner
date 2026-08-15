# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase - NOT HttpCase. Plain HttpCase in 14.0 does not set up
# ``cls.env`` in ``setUpClass``, and the fixtures below need it.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPartnerEvaluationResult(HttpSavepointCase):
    """Tour test for the ``partner_evaluation_result`` work instruction."""

    @classmethod
    def setUpClass(cls):
        """Prepare the ``res.partner.category`` picked by the tour."""
        super().setUpClass()
        cls.env["res.partner.category"].create({"name": "TOUR Result Tag"})

    def test_create(self):
        """Run the create tour for ``partner_evaluation_result``.

        IK: docs/partner_evaluation_result/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_evaluation_partner_evaluation_result_create",
            login="admin",
        )
