// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_partner_experience.partner_certification_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block -- Flow 1 of the partner_certification IK:
    // "Open the Contacts > Configuration > Experiences > Certifications
    // menu."
    //
    // "Experiences" (ssi_partner_experience.menu_config_partner_experience)
    // is a <menuitem> WITHOUT an action that has children, so Odoo 14
    // renders it as an unclickable "dropdown-header" grouping label (no
    // data-menu-xmlid) and flattens its children straight into the
    // Configuration dropdown. There is therefore NO step for it -- the
    // tour goes straight from Configuration to the leaf menu below it.
    function openPartnerCertificationList() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Contacts app",
                trigger: '.o_app[data-menu-xmlid="contacts.menu_contacts"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner.res_partner_menu_config"]',
            },
            {
                content: "Open the Certifications menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner_experience.partner_certification_menu"]',
            },
            {
                content: "Certifications list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Certifications)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // IK: docs/partner_certification/01-create.md
    tour.register(
        "ssi_partner_experience_partner_certification_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Certifications menu.
            openPartnerCertificationList(),
            [
                // ── Flow 2 — Click the New button.
                {
                    content: "Click Create",
                    trigger: ".o_list_button_add",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Form is open in edit mode",
                    trigger: ".o_form_view.o_form_editable",
                    run: function () {
                        // Assertion only; do not trigger the default click
                        // action.
                    },
                },

                // ── Flow 3 — Fill in the required fields (Partner, Date
                // Start, Date End -- Expire stays checked by default).
                {
                    content: "Select the Partner",
                    trigger: ".o_field_many2one[name='partner_id'] input",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text TOUR Partner Certification Create",
                },
                {
                    content: "Pick the Partner from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(TOUR Partner Certification Create)",
                    in_modal: false,
                },
                {
                    content: "Fill in Date Start",
                    trigger: ".o_field_widget[name='date_start'] input",
                    run: "text 01/15/2023",
                },
                {
                    content: "Fill in Date End",
                    trigger: ".o_field_widget[name='date_end'] input",
                    run: "text 01/15/2026",
                },

                // ── Flow 4 — Optionally fill in Certification (used here
                // to identify the record afterwards).
                {
                    content: "Fill in Certification",
                    trigger: ".o_field_widget[name='name']",
                    run: "text TOUR CERTIFICATION Create",
                },

                // ── Flow 6 — Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },

                // ── Post-Condition — the new Certification record is
                // created and appears in the Certifications list.
                {
                    content: "Record is saved and displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(TOUR CERTIFICATION Create)",
                    extra_trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        // Assertion only; do not trigger the default click
                        // action.
                    },
                },
            ]
        )
    );
});
