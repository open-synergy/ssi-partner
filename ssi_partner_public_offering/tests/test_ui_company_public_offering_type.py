# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiCompanyPublicOfferingType(HttpSavepointCase):
    """UI/UX tour test for the ``company_public_offering_type`` work
    instruction.

    ``test_create`` runs the tour paired with the IK file named in its
    docstring (``docs/company_public_offering_type/01-create.md``).
    Pre-Condition data of that IK file is prepared here in Python -- never
    through UI steps -- so the tour only walks the click-flow the IK
    documents.
    """

    @classmethod
    def setUpClass(cls):
        """Prepare the IK Pre-Conditions for the create tour.

        Covers ``Access`` (admin is put in the Public Offering Types
        group) and ``Config`` (a ``sequence.template`` for
        ``company_public_offering_type``, without which the Generate Code
        button raises a ``UserError`` instead of assigning a code).
        """
        super().setUpClass()

        cls.user_admin = cls.env.ref("base.user_admin")
        cls.group_public_offering_type = cls.env.ref(
            "ssi_partner_public_offering."
            "contact_public_offering_type_configurator_group"
        )
        cls.group_public_offering_type.sudo().write(
            {
                "users": [(4, cls.user_admin.id)],
            }
        )

        cls.code_sequence = cls.env["ir.sequence"].create(
            {
                "name": "TOUR Company Public Offering Type Code Sequence",
                "code": "ssi_partner_public_offering.tour."
                "company_public_offering_type",
                "prefix": "TOURSEQCPOT",
                "padding": 4,
            }
        )
        cls.env["sequence.template"].create(
            {
                "name": "TOUR Company Public Offering Type Sequence " "Template",
                "model_id": cls.env["ir.model"]._get_id("company_public_offering_type"),
                "sequence_field_id": cls.env["ir.model.fields"]
                ._get("company_public_offering_type", "code")
                .id,
                "date_field_id": cls.env["ir.model.fields"]
                ._get("company_public_offering_type", "create_date")
                .id,
                "sequence_selection_method": "use_sequence",
                "sequence_id": cls.code_sequence.id,
            }
        )

    def test_create(self):
        """Run the create tour for ``company_public_offering_type``.

        IK: docs/company_public_offering_type/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_partner_public_offering_company_public_offering_type_create",
            login="admin",
        )
