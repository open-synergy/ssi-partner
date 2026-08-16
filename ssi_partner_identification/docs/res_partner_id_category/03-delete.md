# Delete Partner ID Category

> **Module:** ssi_partner_identification\
> **Model:** `res.partner.id_category`\
> **Menu:** Contacts > Configuration > Identities > ID Categories\
> **Actor:** user in group `Partner ID Categories`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any Partner ID Number.
- **Access:** User is in group `Partner ID Categories`.

## Flow

1. Open the **Contacts > Configuration > Identities > ID Categories** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
