# Deactivate Religion

> **Module:** ssi_partner\
> **Model:** `res_partner_religion`\
> **Menu:** Contacts > Configuration > Religion\
> **Actor:** user in group `Religion`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Religion`.

## Flow

1. Open the **Contacts > Configuration > Religion** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated religions cannot be selected on new individual `res.partner` records.
- Contacts that already reference this religion can still be viewed.
