# Activate Partner ID Number

> **Module:** ssi_partner_identification\
> **Model:** `res.partner.id_number`\
> **Menu:** Contacts > Configuration > Identities > ID Numbers\
> **Actor:** user in group `Partner ID Numbers`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Partner ID Numbers`.

## Flow

1. Open the **Contacts > Configuration > Identities > ID Numbers** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The record appears again in the related partner's **Identification Numbers** tab.
