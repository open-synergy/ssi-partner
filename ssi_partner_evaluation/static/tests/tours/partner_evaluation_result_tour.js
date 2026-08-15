/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_partner_evaluation.partner_evaluation_result_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    tour.register(
        "ssi_partner_evaluation_partner_evaluation_result_create",
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
                content: "Open the Results menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner_evaluation.partner_evaluation_result_menu"]',
            },
            {
                content: "Partner Evaluation Results list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Partner Evaluation Results)",
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
                run: "text TOUR Result",
            },
            {
                content: "Ensure Code is /",
                trigger: ".o_field_widget[name='code']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text_blur /",
            },
            {
                content: "Select the Tag",
                trigger: ".o_field_many2one[name='tag_id'] input",
                run: "text TOUR Result Tag",
            },
            {
                content: "Pick from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR Result Tag)",
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
