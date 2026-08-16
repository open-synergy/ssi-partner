# Deactivate Partner ID Number

> **Module:** ssi_partner_identification\
> **Model:** `res.partner.id_number`\
> **Menu:** Contacts > Configuration > Identities > ID Numbers\
> **Actor:** user in group `Partner ID Numbers`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Partner ID Numbers`.

## Flow

1. Open the **Contacts > Configuration > Identities > ID Numbers** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated ID numbers no longer appear in the related partner's **Identification
  Numbers** tab by default.
- The record can still be viewed by enabling the **Archived** filter.
