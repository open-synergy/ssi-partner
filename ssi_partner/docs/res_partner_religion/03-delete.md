# Delete Religion

> **Module:** ssi_partner\
> **Model:** `res_partner_religion`\
> **Menu:** Contacts > Configuration > Religion\
> **Actor:** user in group `Religion`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any `res.partner` record.
- **Access:** User is in group `Religion`.

## Flow

1. Open the **Contacts > Configuration > Religion** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
