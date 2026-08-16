// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_partner_data_privacy_consent.partner_consent_notice_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block -- Flow 1 of the partner_consent_notice IK:
    // "Open the Contacts > Configuration > Data Privacy > Privacy Notice
    // menu."
    function openConsentNoticeList() {
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
            // "Data Privacy" (menu_config_data_privacy) is a <menuitem>
            // without an action that has children -- Odoo 14 renders it as
            // a dropdown-header grouping label, not a clickable
            // data-menu-xmlid item. Skip straight to the leaf menu below it.
            {
                content: "Open the Privacy Notice menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_partner_data_privacy_consent.partner_consent_notice_menu"]',
            },
            {
                content: "Privacy Notice list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Privacy Notice)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // IK: docs/partner_consent_notice/01-create.md
    tour.register(
        "ssi_partner_data_privacy_consent_partner_consent_notice_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // ── Flow 1 — Open the Privacy Notice menu.
            openConsentNoticeList(),
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

                // ── Flow 3 — Fill in the required fields (Name, Code).
                {
                    content: "Fill in Name",
                    trigger: ".o_field_widget[name='name']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text TOUR CONSENT NOTICE Create",
                },
                {
                    content: "Fill in Code",
                    trigger: ".o_field_widget[name='code']",
                    run: "text TOURCONSENTNOTICE01",
                },

                // ── Flow 4 — Open the Privacy Notice tab and fill in
                // Version and Body (Effective Date keeps its default).
                // "Privacy Notice" is the first page inserted into the
                // master_data form notebook (xpath position="before" the
                // "note" page), so it is already the active tab when the
                // form opens -- no click needed. Odoo 14 also renders the
                // tab's href as an auto-generated id (e.g. "#notebook_page_
                // 774") rather than the page name, so a selector like
                // `a[href="#notice"]` would never match even if a click
                // were required.
                {
                    content: "Fill in Version",
                    trigger: ".o_field_widget[name='version']",
                    run: "text 1.0",
                },
                {
                    content: "Fill in Body",
                    trigger: ".o_field_widget[name='body'] textarea",
                    run: "text This is the tour privacy notice body.",
                },

                // ── Flow 6 — Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },

                // ── Post-Condition — A new Privacy Notice record is
                // created and appears in the Privacy Notice list.
                {
                    content: "Record is saved and displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(TOUR CONSENT NOTICE Create)",
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
