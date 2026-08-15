# Deactivate Company Ownership Type

> **Module:** ssi_partner\
> **Model:** `company_ownership_type`\
> **Menu:** Contacts > Configuration > Ownership Types\
> **Actor:** user in group `Ownership Type`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Ownership Type`.

## Flow

1. Open the **Contacts > Configuration > Ownership Types** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated ownership types cannot be selected on new company `res.partner` records.
- Companies that already reference this ownership type can still be viewed.
