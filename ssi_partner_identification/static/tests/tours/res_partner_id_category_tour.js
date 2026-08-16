/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_partner_identification.res_partner_id_category_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/res_partner_id_category/01-create.md
    tour.register(
        "ssi_partner_identification_res_partner_id_category_create",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Contacts > Configuration > Identities >
            // ID Categories menu. "Identities" is a grouping header (has
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
                content: "Open the ID Categories menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="partner_identification.menu_partner_id_category"]',
            },
            {
                // Gerbang: tunggu action TUJUAN benar-benar terpasang.
                content: "Partner ID Categories list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Partner ID Categories)",
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
                content: "Fill in ID name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour Test ID Category",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                run: "text tour_test_cat",
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
