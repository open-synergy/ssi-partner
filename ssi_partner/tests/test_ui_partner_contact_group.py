# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPartnerContactGroup(HttpSavepointCase):
    """UI/UX tour test for the ``partner_contact_group`` work instruction.

    ``test_create`` runs the tour paired with the IK file named in its
    docstring (``docs/partner_contact_group/01-create.md``). Pre-Condition
    data of that IK file is prepared here in Python -- never through UI
    steps -- so the tour only walks the click-flow the IK documents.
    """

    @classmethod
    def setUpClass(cls):
        """Prepare the IK Pre-Conditions for the create tour.

        Covers ``Access`` (admin is put in the Partner Contact Groups
        group), ``Config`` (a ``sequence.template`` for
        ``partner_contact_group``, without which the Generate Code button
        raises a ``UserError`` instead of assigning a code), and ``Data``
        (a commercial contact with one child contact, to be picked in the
        Commercial Contact / Contacts fields).
        """
        super().setUpClass()

        cls.user_admin = cls.env.ref("base.user_admin")
        cls.group_contact_group = cls.env.ref(
            "ssi_partner.partner_contact_group_configurator_group"
        )
        cls.group_contact_group.sudo().write(
            {
                "users": [(4, cls.user_admin.id)],
            }
        )

        cls.commercial_contact = cls.env["res.partner"].create(
            {
                "name": "TOUR CONTACT GROUP Commercial",
                "is_company": True,
            }
        )
        cls.env["res.partner"].create(
            {
                "name": "TOUR CONTACT GROUP Child",
                "is_company": False,
                "parent_id": cls.commercial_contact.id,
            }
        )

        cls.code_sequence = cls.env["ir.sequence"].create(
            {
                "name": "TOUR Contact Group Code Sequence",
                "code": "ssi_partner.tour.partner_contact_group",
                "prefix": "TOURSEQPCG",
                "padding": 4,
            }
        )
        cls.env["sequence.template"].create(
            {
                "name": "TOUR Contact Group Sequence Template",
                "model_id": cls.env["ir.model"]._get_id("partner_contact_group"),
                "sequence_field_id": cls.env["ir.model.fields"]
                ._get("partner_contact_group", "code")
                .id,
                "date_field_id": cls.env["ir.model.fields"]
                ._get("partner_contact_group", "create_date")
                .id,
                "sequence_selection_method": "use_sequence",
                "sequence_id": cls.code_sequence.id,
            }
        )

    def test_create(self):
        """Run the create tour for ``partner_contact_group``.

        IK: docs/partner_contact_group/01-create.md
        """
        self.start_tour(
            "/web", "ssi_partner_partner_contact_group_create", login="admin"
        )
