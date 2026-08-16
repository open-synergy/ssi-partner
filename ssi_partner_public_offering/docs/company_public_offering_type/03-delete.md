# Delete Company Public Offering Type

> **Module:** ssi_partner_public_offering\
> **Model:** `company_public_offering_type`\
> **Menu:** Contacts > Configuration > Public Offering Types\
> **Actor:** user in group `Public Offering Types`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any `res.partner` record.
- **Access:** User is in group `Public Offering Types`.

## Flow

1. Open the **Contacts > Configuration > Public Offering Types** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
