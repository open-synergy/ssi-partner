# Activate Partner ID Category

> **Module:** ssi_partner_identification\
> **Model:** `res.partner.id_category`\
> **Menu:** Contacts > Configuration > Identities > ID Categories\
> **Actor:** user in group `Partner ID Categories`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Partner ID Categories`.

## Flow

1. Open the **Contacts > Configuration > Identities > ID Categories** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected as the **Category** of a new Partner ID Number again.
