# Create Contact

> **Module:** ssi_partner_company_capital\
> **Extends:** res.partner (Odoo core Contacts) — no base Instruksi Kerja exists for this
> model

## Additional Fields

When this module is installed, the Contacts form gains a **Capital** page. This page is
only visible when the contact is a **Company** (i.e. **Company** is selected instead of
**Individual**).

- **Shareholders**: One or more shareholders holding shares of this company. Optional —
  zero or more rows may be added. Each row has:
  - **Sequence**: Drag handle used to reorder the rows. Defaults to `10`.
  - **Shareholder**: The shareholder contact, selected only from top-level contacts (not
    an address/child contact) other than the company itself. Required per row.
  - **Num. Of Share**: The number of shares this shareholder holds. Required per row,
    defaults to `1`.
