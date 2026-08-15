# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPartnerEvaluationValueSet(HttpSavepointCase):
    """Tour test for ``partner_evaluation_value_set`` creation."""

    @classmethod
    def setUpClass(cls):
        """Prepare the value item line picked by the tour."""
        super().setUpClass()
        cls.env["partner_evaluation_value_item"].create(
            {"name": "TOUR Value Set Item", "code": "/"}
        )

    def test_create(self):
        """Run the create tour for ``partner_evaluation_value_set``.

        IK: docs/partner_evaluation_value_set/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_evaluation_partner_evaluation_value_set_create",
            login="admin",
        )
