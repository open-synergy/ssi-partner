# Edit Partner ID Number

> **Module:** ssi_partner_identification\
> **Model:** `res.partner.id_number`\
> **Menu:** Contacts > Configuration > Identities > ID Numbers\
> **Actor:** user in group `Partner ID Numbers`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record already exists.
- **Access:** User is in group `Partner ID Numbers`.

## Flow

1. Open the **Contacts > Configuration > Identities > ID Numbers** menu.
2. Find and open the record to edit.
3. Click the **Edit** button.
4. Change the required fields (**Partner**, **Category**, **ID Number**) or any of the
   optional fields.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
- If the **Category** or **ID Number** changed and the category has a **Python
  validation code**, the new value is validated again; an invalid number is rejected
  with an error.
