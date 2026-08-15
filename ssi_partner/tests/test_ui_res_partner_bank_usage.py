# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiResPartnerBankUsage(HttpSavepointCase):
    """UI/UX tour test for the ``res_partner_bank_usage`` work instruction.

    ``test_create`` runs the tour paired with the IK file named in its
    docstring (``docs/res_partner_bank_usage/01-create.md``).
    Pre-Condition data of that IK file is prepared here in Python -- never
    through UI steps -- so the tour only walks the click-flow the IK
    documents.
    """

    @classmethod
    def setUpClass(cls):
        """Prepare the IK Pre-Conditions for the create tour.

        Covers ``Access`` (admin is put in the Bank Account Usage group)
        and ``Config`` (a ``sequence.template`` for
        ``res_partner_bank_usage``, without which the Generate Code
        button raises a ``UserError`` instead of assigning a code).
        """
        super().setUpClass()

        cls.user_admin = cls.env.ref("base.user_admin")
        cls.group_bank_usage = cls.env.ref(
            "ssi_partner.res_partner_bank_usage_configurator_group"
        )
        cls.group_bank_usage.sudo().write(
            {
                "users": [(4, cls.user_admin.id)],
            }
        )

        cls.code_sequence = cls.env["ir.sequence"].create(
            {
                "name": "TOUR Bank Account Usage Code Sequence",
                "code": "ssi_partner.tour.res_partner_bank_usage",
                "prefix": "TOURSEQBKU",
                "padding": 4,
            }
        )
        cls.env["sequence.template"].create(
            {
                "name": "TOUR Bank Account Usage Sequence Template",
                "model_id": cls.env["ir.model"]._get_id("res_partner_bank_usage"),
                "sequence_field_id": cls.env["ir.model.fields"]
                ._get("res_partner_bank_usage", "code")
                .id,
                "date_field_id": cls.env["ir.model.fields"]
                ._get("res_partner_bank_usage", "create_date")
                .id,
                "sequence_selection_method": "use_sequence",
                "sequence_id": cls.code_sequence.id,
            }
        )

    def test_create(self):
        """Run the create tour for ``res_partner_bank_usage``.

        IK: docs/res_partner_bank_usage/01-create.md
        """
        self.start_tour(
            "/web", "ssi_partner_res_partner_bank_usage_create", login="admin"
        )
