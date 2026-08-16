// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_partner_data_privacy_consent.partner_consent_purpose_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block -- Flow 1 of the partner_consent_purpose IK:
    // "Open the Contacts > Configuration > Data Privacy > Consent Purpose
    // menu."
    function openConsentPurposeList() {
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
            // "Data Privacy" (menu_config_data_privacy) is a <menuitem>
            // without an action that has children -- Odoo 14 renders it as
            // a dropdown-header grouping label, not a clickable
            // data-menu-xmlid item. Skip straight to the leaf menu below it.
            {
                content: "Open the Consent Purpose menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner_data_privacy_consent.partner_consent_purpose_menu"]',
            },
            {
                content: "Consent Purpose list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Consent Purpose)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // IK: docs/partner_consent_purpose/01-create.md
    tour.register(
        "ssi_partner_data_privacy_consent_partner_consent_purpose_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Consent Purpose menu.
            openConsentPurposeList(),
            [
                // ── Flow 2 — Click the Create button.
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

                // ── Flow 3 — Fill in the required fields (Name, Code).
                {
                    content: "Fill in Name",
                    trigger: ".o_field_widget[name='name']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text TOUR CONSENT PURPOSE Create",
                },
                {
                    content: "Fill in Code",
                    trigger: ".o_field_widget[name='code']",
                    run: "text TOURCONSENTPURPOSE01",
                },

                // ── Flow 5 — Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },

                // ── Post-Condition — A new Consent Purpose record is
                // created and appears in the Consent Purpose list.
                {
                    content: "Record is saved and displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(TOUR CONSENT PURPOSE Create)",
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
