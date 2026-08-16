# Deactivate Company Public Offering Type

> **Module:** ssi_partner_public_offering\
> **Model:** `company_public_offering_type`\
> **Menu:** Contacts > Configuration > Public Offering Types\
> **Actor:** user in group `Public Offering Types`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Public Offering Types`.

## Flow

1. Open the **Contacts > Configuration > Public Offering Types** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated public offering types cannot be selected on new `res.partner` records.
- Partners that already reference this public offering type can still be viewed.
