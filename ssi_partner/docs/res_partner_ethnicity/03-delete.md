# Delete Ethnicity

> **Module:** ssi_partner\
> **Model:** `res_partner_ethnicity`\
> **Menu:** Contacts > Configuration > Ethnicity\
> **Actor:** user in group `Ethnicity`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any `res.partner` record.
- **Access:** User is in group `Ethnicity`.

## Flow

1. Open the **Contacts > Configuration > Ethnicity** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
