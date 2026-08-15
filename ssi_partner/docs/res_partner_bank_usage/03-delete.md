# Delete Bank Account Usage

> **Module:** ssi_partner\
> **Model:** `res_partner_bank_usage`\
> **Menu:** Contacts > Configuration > Bank Account Usage\
> **Actor:** user in group `Bank Account Usage`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any `res.partner.bank` record.
- **Access:** User is in group `Bank Account Usage`.

## Flow

1. Open the **Contacts > Configuration > Bank Account Usage** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
