// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define(
    "ssi_partner_education_level.partner_formal_education_level_tour",
    function (require) {
        "use strict";

        var tour = require("web_tour.tour");

        // IK: docs/partner_formal_education_level/01-create.md
        tour.register(
            "ssi_partner_education_level_partner_formal_education_level_create",
            {
                test: true,
                url: "/web",
            },
            [
                // ── Flow 1 — Open the Contacts > Configuration >
                // Education Levels > Education Level menu.
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
                // "Education Levels" is a grouping menuitem WITHOUT an
                // action (it only has children) -- Odoo 14.0 renders it
                // as a non-clickable <div class="dropdown-header">,
                // without data-menu-xmlid. Skip it and go straight to
                // the leaf menu.
                {
                    content: "Open the Education Level menu",
                    trigger:
                        '.o_menu_sections [data-menu-xmlid="ssi_partner_education_level.partner_formal_education_level_menu"]',
                },
                {
                    // Gerbang: tunggu action TUJUAN benar-benar
                    // terpasang, bukan sekadar "ada list di layar"
                    // (patterns.md skill odoo-development-ui-test §A).
                    content: "Education Level list is displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(Education Level)",
                    extra_trigger: ".o_list_view",
                    run: function () {
                        // Assertion only.
                    },
                },

                // ── Flow 2 — Click the New button.
                {
                    content: "Click New",
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

                // ── Flow 3 — Fill in the required fields: Name, Code.
                // Sequence already carries its default value (5).
                {
                    content: "Fill in the Name",
                    trigger: ".o_field_widget[name='name']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text TOUR Formal Education Level",
                },
                {
                    content: "Fill in the Code",
                    trigger: ".o_field_widget[name='code']",
                    run: "text /",
                },

                // ── Flow 4 — Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },

                // ── Post-Condition — a new Formal Education Level
                // record is created.
                {
                    content: "Record is saved",
                    trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        );
    }
);
