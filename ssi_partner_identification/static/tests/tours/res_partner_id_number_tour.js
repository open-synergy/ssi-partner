/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_partner_identification.res_partner_id_number_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/res_partner_id_number/01-create.md
    tour.register(
        "ssi_partner_identification_res_partner_id_number_create",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Contacts > Configuration > Identities >
            // ID Numbers menu. "Identities" is a grouping header (has
            // children, no action) so it renders without a
            // data-menu-xmlid and is skipped here.
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
                content: "Open the ID Numbers menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="partner_identification.menu_partner_id_numbers"]',
            },
            {
                // Gerbang: tunggu action TUJUAN benar-benar terpasang.
                content: "Partner ID Numbers list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Partner ID Numbers)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Click the New button.
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 3 — Fill in the required fields.
            {
                content: "Select the Partner",
                trigger: ".o_field_many2one[name='partner_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour Test ID Number Partner",
            },
            {
                content: "Pick the Partner from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(Tour Test ID Number Partner)",
                in_modal: false,
            },
            {
                content: "Select the Category",
                trigger: ".o_field_many2one[name='category_id'] input",
                run: "text Tour Test ID Number Category",
            },
            {
                content: "Pick the Category from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(Tour Test ID Number Category)",
                in_modal: false,
            },
            {
                content: "Fill in the ID Number",
                trigger: ".o_field_widget[name='name']",
                run: "text TOUR-ID-0001",
            },

            // Flow 5 — Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                // Post-Condition — a new record is created and Active.
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
