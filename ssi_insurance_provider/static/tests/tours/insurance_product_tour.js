/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_insurance_provider.insurance_product_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/insurance_product/01-create.md
    tour.register(
        "ssi_insurance_provider_insurance_product_create",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Contacts > Configuration > Insurance
            // Provider > Products menu. "Insurance Provider" is a
            // grouping header (has children, level 3+) so it renders
            // without a data-menu-xmlid and is skipped here.
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
                content: "Open the Products menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_insurance_provider.insurance_product_menu"]',
            },
            {
                // Gerbang: tunggu action TUJUAN benar-benar terpasang.
                content: "Insurance Products list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Insurance Products)",
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
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour Test Insurance Product",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text /",
            },
            {
                content: "Select the Provider",
                trigger: ".o_field_many2one[name='provider_id'] input",
                run: "text Tour Test Insurance Provider",
            },
            {
                content: "Pick the Provider from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(Tour Test Insurance Provider)",
                in_modal: false,
            },
            {
                content: "Select the Coverage Type",
                trigger: ".o_field_many2one[name='coverage_type_id'] input",
                run: "text Tour Test Product Coverage",
            },
            {
                content: "Pick the Coverage Type from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(Tour Test Product Coverage)",
                in_modal: false,
            },
            {
                content: "Select the Currency",
                trigger: ".o_field_many2one[name='currency_id'] input",
                run: "text USD",
            },
            {
                content: "Pick the Currency from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(USD)",
                in_modal: false,
            },

            // Flow 6 — Click Save.
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
