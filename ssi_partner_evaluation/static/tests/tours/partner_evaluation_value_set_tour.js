/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_partner_evaluation.partner_evaluation_value_set_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    tour.register(
        "ssi_partner_evaluation_partner_evaluation_value_set_create",
        {
            test: true,
            url: "/web",
        },
        [
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
                content: "Open the Value Sets menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner_evaluation.partner_evaluation_value_set_menu"]',
            },
            {
                content: "Partner Evaluation Value Sets list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Partner Evaluation Value Sets)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Fill in the Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Value Set",
            },
            {
                content: "Ensure Code is /",
                trigger: ".o_field_widget[name='code']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text_blur /",
            },
            {
                content: "Open the Items tab",
                trigger: ".o_notebook .nav-link:contains(Items)",
            },
            {
                content: "Add a value item line",
                trigger: ".o_field_x2many .o_field_x2many_list_row_add a",
            },
            {
                content: "Select the value item",
                trigger: ".o_selected_row .o_field_widget[name='item_id'] input",
                run: "text TOUR Value Set Item",
            },
            {
                content: "Pick from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(TOUR Value Set Item)",
                in_modal: false,
            },
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
