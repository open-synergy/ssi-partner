/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_insurance_provider.insurance_product_coverage_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/insurance_product_coverage/01-create.md
    tour.register(
        "ssi_insurance_provider_insurance_product_coverage_create",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Contacts > Configuration > Insurance
            // Provider > Coverages menu. "Insurance Provider" is a
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
                content: "Open the Coverages menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_insurance_provider.insurance_product_coverage_menu"]',
            },
            {
                // Gerbang: tunggu action TUJUAN benar-benar terpasang.
                content: "Insurance Product Coverages list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Insurance Product Coverages)",
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
                run: "text Tour Test Coverage",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text /",
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
