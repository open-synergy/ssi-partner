# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPartnerAcademic(HttpSavepointCase):
    """UI/UX tour test for the ``partner.academic`` work instruction."""

    @classmethod
    def setUpClass(cls):
        """Grant the configurator group the create tour menu requires.

        Pre-Condition: the Academic Experiences menu is gated by the
        ``Contact's Academic Experience`` group. Without it the tour dies
        on its first step -- the menu is never rendered for admin.
        """
        super().setUpClass()
        cls.env.ref(
            "ssi_partner_experience.partner_academic_configurator_group"
        ).sudo().write(
            {
                "users": [(4, cls.env.ref("base.user_admin").id)],
            }
        )

    def test_create(self):
        """Run the create tour for ``partner.academic``.

        IK: docs/partner_academic/01-create.md
        """
        self.start_tour(
            "/web", "ssi_partner_experience_partner_academic_create", login="admin"
        )
