# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPartnerConsentNotice(HttpSavepointCase):
    """UI/UX tour test for the ``partner_consent_notice`` work instruction.

    ``test_create`` runs the tour paired with the IK file named in its
    docstring (``docs/partner_consent_notice/01-create.md``).
    Pre-Condition data of that IK file is prepared here in Python --
    never through UI steps -- so the tour only walks the click-flow the
    IK documents.
    """

    @classmethod
    def setUpClass(cls):
        """Prepare the IK Pre-Condition for the create tour.

        Covers ``Access``: admin is put in the *Partner Consent Privacy
        Notice* group so the menu and Create button are visible.
        """
        super().setUpClass()

        cls.user_admin = cls.env.ref("base.user_admin")
        cls.group_notice = cls.env.ref(
            "ssi_partner_data_privacy_consent.partner_consent_notice_group"
        )
        cls.group_notice.sudo().write(
            {
                "users": [(4, cls.user_admin.id)],
            }
        )

    def test_create(self):
        """Run the create tour for ``partner_consent_notice``.

        IK: docs/partner_consent_notice/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_data_privacy_consent_partner_consent_notice_create",
            login="admin",
        )
