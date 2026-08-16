# Deactivate Partner ID Category

> **Module:** ssi_partner_identification\
> **Model:** `res.partner.id_category`\
> **Menu:** Contacts > Configuration > Identities > ID Categories\
> **Actor:** user in group `Partner ID Categories`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Partner ID Categories`.

## Flow

1. Open the **Contacts > Configuration > Identities > ID Categories** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated ID categories cannot be selected as the **Category** of a new Partner ID
  Number.
- Partner ID Numbers that already use this category can still be viewed.
