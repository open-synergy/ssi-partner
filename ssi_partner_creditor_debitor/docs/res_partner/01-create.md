# Create Contact

> **Module:** ssi_partner_creditor_debitor\
> **Extends:** res.partner (Odoo core Contacts) — no base Instruksi Kerja exists for this
> model

## Additional Fields

When this module is installed, the Contacts form gains a **Creditor & Debtor** page:

- **Primary Creditor**: Read-only. Automatically shows the **Creditor** of the first row
  (by **Sequence**) in the **Creditors** list below. Empty when that list has no rows.
- **Creditors**: One or more contacts this contact owes money to. Optional — zero or
  more rows may be added. Each row has:
  - **Sequence**: Drag handle used to reorder the rows; the top row determines **Primary
    Creditor**. Defaults to `10`.
  - **Creditor**: The creditor contact, selected only from contacts in the **Creditor**
    category. Required per row.
- **Debtors**: One or more contacts that owe money to this contact. Optional — zero or
  more rows may be added. Each row has:
  - **Debtor**: The debtor contact. Not restricted to any category. Required per row.
