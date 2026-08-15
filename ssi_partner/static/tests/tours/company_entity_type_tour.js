// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_partner.company_entity_type_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block -- Flow 1 of the company_entity_type IK: "Open
    // the Contacts > Configuration > Entity Types menu."
    function openCompanyEntityTypeList() {
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
                content: "Open the Entity Types menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner.company_entity_type_menu"]',
            },
            {
                // Gate on the TARGET action's breadcrumb, not merely "a list
                // is on screen" (odoo-development-ui-test patterns.md §A).
                content: "Entity Type list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Entity Type)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // IK: docs/company_entity_type/01-create.md
    tour.register(
        "ssi_partner_company_entity_type_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Entity Types menu.
            openCompanyEntityTypeList(),
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
                    run: "text TOUR ENTITY TYPE Create",
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
                    // The record has no id until this button auto-saves it,
                    // so the breadcrumb literal "New" going away is the
                    // data-independent proof the save+reload completed
                    // (odoo-development-ui-test patterns.md §P). The
                    // generated Code value itself is a value fact, verified
                    // by the unit tests.
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

                // ── Post-Condition — A new Company Entity Type record is
                // created and appears in the Entity Types list, and the Code
                // now holds a value from the sequence template. Only what is
                // visible is asserted here.
                {
                    content: "Record is saved and displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(TOUR ENTITY TYPE Create)",
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
