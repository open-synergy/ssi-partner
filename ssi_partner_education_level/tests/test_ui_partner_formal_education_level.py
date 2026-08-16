# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. HttpCase in 14.0 inherits
# TransactionCase, which does not set up ``cls.env`` in ``setUpClass``.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPartnerFormalEducationLevel(HttpSavepointCase):
    """UI/UX tour tests for ``partner.formal_education_level``.

    The ``test_create`` method below runs the tour pairing with the IK
    file named in its docstring (``docs/partner_formal_education_level/
    01-create.md``).
    """

    def test_create(self):
        """Run the create tour for ``partner.formal_education_level``.

        IK: docs/partner_formal_education_level/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_education_level_partner_formal_education_level_create",
            login="admin",
        )
