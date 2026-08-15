// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_partner.partner_contact_group_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block -- Flow 1 of the partner_contact_group IK:
    // "Open the Contacts > Configuration > Contact Groups menu."
    function openContactGroupList() {
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
                content: "Open the Contact Groups menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner.partner_contact_group_menu"]',
            },
            {
                content: "Contact Groups list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Contact Groups)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // IK: docs/partner_contact_group/01-create.md
    tour.register(
        "ssi_partner_partner_contact_group_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Contact Groups menu.
            openContactGroupList(),
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

                // ── Flow 3 — Fill in the required fields (Name, Code,
                // Commercial Contact, Contacts). Code is left as "/" so the
                // Generate Code button of Flow 4 actually assigns a value.
                {
                    content: "Fill in Name",
                    trigger: ".o_field_widget[name='name']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text TOUR CONTACT GROUP Create",
                },
                {
                    content: "Fill in Code",
                    trigger: ".o_field_widget[name='code']",
                    run: "text /",
                },
                {
                    content: "Select the Commercial Contact",
                    trigger: ".o_field_widget[name='commercial_contact_id'] input",
                    run: "text TOUR CONTACT GROUP Commercial",
                },
                {
                    content: "Pick the commercial contact from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item " +
                        "a:contains(TOUR CONTACT GROUP Commercial)",
                    in_modal: false,
                },
                {
                    // The Contacts field selector list only shows children of
                    // the just-selected Commercial Contact -- fill it last so
                    // the domain recompute (triggered by the commercial
                    // contact onchange) does not race with this dropdown
                    // (odoo-development-ui-test patterns.md §C, Jebakan 1).
                    content: "Select a Contact",
                    trigger: ".o_field_widget[name='contact_ids'] input",
                    run: "text TOUR CONTACT GROUP Child",
                },
                {
                    content: "Pick the contact from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item " +
                        "a:contains(TOUR CONTACT GROUP Child)",
                    in_modal: false,
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

                // ── Post-Condition — A new Contact Group record is created
                // and appears in the Contact Groups list, and the Code now
                // holds a value from the sequence template. The selected
                // Contact tag itself is a value fact, verified by the unit
                // tests.
                {
                    content: "Record is saved and displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(TOUR CONTACT GROUP Create)",
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
