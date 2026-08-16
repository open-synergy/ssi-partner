# Create Partner ID Number

> **Module:** ssi_partner_identification\
> **Model:** `res.partner.id_number`\
> **Menu:** Contacts > Configuration > Identities > ID Numbers\
> **Actor:** user in group `Partner ID Numbers`

## Pre-Condition

- **Data:** An active Partner ID Category record exists (e.g. "Driver License").
- **Data:** The partner (a `res.partner` record) this ID belongs to already exists.
- **Access:** User is in group `Partner ID Numbers`.

## Flow

1. Open the **Contacts > Configuration > Identities > ID Numbers** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Partner** _(required)_: the partner this identification belongs to.
   - **Category** _(required)_: the identification type, for example "Driver License".
   - **ID Number** _(required)_: the identification number itself.
4. Optionally fill in the remaining fields:
   - **Issued by**: another partner who issued this ID.
   - **Place of Issuance**: the place where the ID was issued.
   - **Issued on**: the date the ID was issued.
   - **Valid from** / **Valid until**: the validity period of the ID.
   - **Status**: the current renewal status of the ID.
   - **Notes**: free-text remarks.
5. Click **Save**.

## Post-Condition

- A new record is created and **Active**.
- If the selected **Category** has a **Python validation code**, the **ID Number** is
  validated against it; an invalid number is rejected with an error and the record is
  not saved.
