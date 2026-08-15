/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_partner_evaluation.partner_evaluation_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block: Contacts > Partner Evaluation > Evaluations.
    function openEvaluationList() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Contacts app",
                trigger: '.o_app[data-menu-xmlid="contacts.menu_contacts"]',
            },
            {
                content: "Open the Partner Evaluation menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner_evaluation.menu_partner_evaluation_header"]',
            },
            {
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner_evaluation.partner_evaluation_menu"]',
            },
            {
                content: "Partner Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Partner Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    tour.register(
        "ssi_partner_evaluation_partner_evaluation_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(openEvaluationList(), [
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
                content: "Select the Type",
                trigger: ".o_field_many2one[name='type_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Evaluation Type",
            },
            {
                content: "Pick the Type from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(TOUR Evaluation Type)",
                in_modal: false,
            },
            {
                content: "Select the Partner",
                trigger: ".o_field_many2one[name='partner_id'] input",
                run: "text TOUR Evaluation Partner",
            },
            {
                content: "Pick the Partner from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(TOUR Evaluation Partner)",
                in_modal: false,
            },
            {
                content: "Fill in the Date",
                trigger: ".o_field_widget[name='date'] input",
                run: "text 01/15/2026",
            },
            {
                content: "Fill in the Date Start",
                trigger: ".o_field_widget[name='date_start'] input",
                run: "text 01/15/2026",
            },
            {
                content: "Fill in the Date End",
                trigger: ".o_field_widget[name='date_end'] input",
                run: "text 01/31/2026",
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
        ])
    );
});
