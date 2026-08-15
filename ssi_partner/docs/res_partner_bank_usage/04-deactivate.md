# Deactivate Bank Account Usage

> **Module:** ssi_partner\
> **Model:** `res_partner_bank_usage`\
> **Menu:** Contacts > Configuration > Bank Account Usage\
> **Actor:** user in group `Bank Account Usage`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Bank Account Usage`.

## Flow

1. Open the **Contacts > Configuration > Bank Account Usage** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated usages cannot be selected on new `res.partner.bank` records.
- Bank accounts that already reference this usage can still be viewed.
