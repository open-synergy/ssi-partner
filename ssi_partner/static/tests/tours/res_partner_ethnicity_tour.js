// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_partner.res_partner_ethnicity_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block -- Flow 1 of the res_partner_ethnicity IK:
    // "Open the Contacts > Configuration > Ethnicity menu."
    function openEthnicityList() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Contacts app",
                trigger: '.o_app[data-menu-xmlid="ssi_partner.menu_contacts"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner.res_partner_menu_config"]',
            },
            {
                content: "Open the Ethnicity menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner.res_partner_ethnicity_menu"]',
            },
            {
                content: "Ethnicity list is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Ethnicity)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // IK: docs/res_partner_ethnicity/01-create.md
    tour.register(
        "ssi_partner_res_partner_ethnicity_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Ethnicity menu.
            openEthnicityList(),
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

                // ── Flow 3 — Fill in the required fields (Name, Code). Code
                // is left as "/" so the Generate Code button of Flow 4
                // actually assigns a value.
                {
                    content: "Fill in Name",
                    trigger: ".o_field_widget[name='name']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text TOUR ETHNICITY Create",
                },
                {
                    content: "Fill in Code",
                    trigger: ".o_field_widget[name='code']",
                    run: "text /",
                },

                // ── Flow 4 — Click Generate Code in the header. This is an
                // inline action of this IK (metadata "Inline Actions:
                // action_generate_code").
                {
                    content: "Click Generate Code",
                    trigger: ".o_statusbar_buttons button[name='action_generate_code']",
                    extra_trigger: ".o_form_view.o_form_editable",
                },
                {
                    content: "Record is saved by Generate Code",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:not(:contains(New))",
                    run: function () {
                        // Assertion only; do not trigger the default click
                        // action.
                    },
                },

                // ── Flow 6 — Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },

                // ── Post-Condition — A new Ethnicity record is created and
                // appears in the Ethnicity list, and the Code now holds a
                // value from the sequence template.
                {
                    content: "Record is saved and displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(TOUR ETHNICITY Create)",
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
