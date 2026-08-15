# Create Contact

> **Module:** ssi_partner\
> **Extends:** res.partner (Odoo core Contacts) — no base Instruksi Kerja exists for this
> model

## Additional Fields

When this module is installed, the Contacts form gains the following fields.

On the **Personal Information** page (individual contacts only, i.e. **Individual** is
selected instead of **Company**):

- **Nickname**: Familiar or informal name the contact is commonly called by. Optional.
- **Religion**: The contact's religion, selected from the **Religion** master data.
  Optional.
- **Ethnicity**: The contact's ethnicity, selected from the **Ethnicity** master data.
  Optional.
- **Blood Type (ABO)**: One of `A`, `B`, `O`, `AB`. Optional.
- **Blood Type (Rh)**: One of `+`, `-`. Optional.
- **Marital Status**: One of Single, Married, Legal Cohabitant, Widower, Divorced.
  Defaults to Single.
- **Spouse Complete Name**, **Spouse Birthdate**: Only visible when **Marital Status**
  is Married or Legal Cohabitant. Optional, free text. These do not link to an actual
  contact record — use **Spouse** below for that.

In the **Family** group, also on the **Personal Information** page:

- **Father**, **Mother**, **Guardian**, **Spouse**: Each a link to another individual
  contact. Optional. A contact cannot be set as its own father, mother, guardian, or
  spouse.
- **Children**: One or more individual contacts linked as children of this contact.
  Optional. A contact cannot be added to its own children.
- **Wards**: Read-only. Automatically shows contacts that have this contact set as their
  **Guardian**.

On the **Company Information** page (company contacts only, i.e. **Company** is selected
instead of **Individual**):

- **Ownership Type**: The company's ownership structure, selected from the **Ownership
  Type** master data. Optional.
- **Entity Type**: The company's legal entity type, selected from the **Entity Type**
  master data. Optional.

## Modified Validation

- Saving fails with a validation error if **Father**, **Mother**, **Guardian**, or
  **Spouse** is set to the contact itself, or if the contact is added to its own
  **Children**.
- Setting **Father** or **Mother** automatically adds this contact to that parent's
  **Children** list; changing or clearing **Father**/**Mother** automatically removes it
  from the previous parent's **Children** list. Setting **Guardian** does not affect
  **Children** — it is only reflected on the guardian's **Wards** list.

## Related Views

- The **Open** button (before the **Contacts & Addresses** section) opens the Contacts
  list filtered to this contact's own children (addresses and sub-contacts), without
  writing any field. It is pure navigation and is not covered by a tour.
