# Delete Company Ownership Type

> **Module:** ssi_partner\
> **Model:** `company_ownership_type`\
> **Menu:** Contacts > Configuration > Ownership Types\
> **Actor:** user in group `Ownership Type`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any `res.partner` record.
- **Access:** User is in group `Ownership Type`.

## Flow

1. Open the **Contacts > Configuration > Ownership Types** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
