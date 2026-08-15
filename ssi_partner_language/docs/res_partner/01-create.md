# Create Contact

> **Module:** ssi_partner_language\
> **Extends:** ssi_partner — model `res.partner`, aksi `01-create`

## Additional Fields

When this module is installed, the Contacts form gains a **Languages** page (individual
contacts only, i.e. **Individual** is selected instead of **Company**):

- **Languages**: a list of languages the contact can use, with a proficiency rating for
  each. Optional — zero or more rows may be added. Each row has:
  - **Language**: the language, selected from the standard list of installed languages.
    Required per row.
  - **Reading**, **Writing**, **Speaking**, **Listening**: proficiency rating for that
    skill, one of `0` (No Proficiency) through `5` (Functionally Native Proficiency),
    with `+` half-steps in between. Each defaults to `0`. Required per row.
  - **Description**: free-text optional note for the row. Only shown when a row is
    opened in its own pop-up form, not in the inline table.

## Modified Validation

- Saving fails with an error if the same **Language** is added twice for the same
  contact.
