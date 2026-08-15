// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_partner_creditor_debitor.res_partner_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/res_partner/01-create.md (E1 delta -- Additional Fields)
    //
    // res.partner is Odoo core Contacts, so there is no base Instruksi
    // Kerja with navigation steps to reuse. This tour writes the standard
    // Contacts navigation itself: open the Contacts app, click Create,
    // then assert the Creditor & Debtor tab this module adds.
    tour.register(
        "ssi_partner_creditor_debitor_res_partner_field_creditor_debtor",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Open the Contacts app. The Contacts app tile has no
            // action of its own; it redirects straight to the Contacts
            // action (its only actionable child menu), so there is no
            // intermediate landing view to race against.
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Contacts app",
                trigger: '.o_app[data-menu-xmlid="contacts.menu_contacts"]',
            },
            {
                // Gate: wait for the Contacts action to actually be
                // mounted. The Contacts action's view_mode starts with
                // "kanban", so the landing view is Kanban, not List.
                content: "Contacts kanban view is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Contacts)",
                extra_trigger: ".o_kanban_view",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },

            // ── Click Create. The Contacts kanban view's Create button
            // uses the kanban-specific class, not the list one.
            {
                content: "Click Create",
                trigger: ".o-kanban-button-new",
                extra_trigger: ".o_kanban_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },

            // ── Additional Fields (docs/res_partner/01-create.md, delta of
            // ssi_partner_creditor_debitor) -- the Creditor & Debtor page
            // is always visible (no attrs gate it). Delta-only tour: it
            // stops here, it does not fill any field and does not
            // continue to Save (E1 delta-only; see
            // odoo-development-ui-test scope-and-boundaries.md).
            {
                content: "Creditor & Debtor tab is displayed",
                trigger:
                    ".o_notebook_headers li.nav-item:not(.o_invisible_modifier)" +
                    " > a.nav-link:contains(Creditor & Debtor)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ]
    );
});
