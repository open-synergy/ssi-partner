# Activate Contact Group

> **Module:** ssi_partner\
> **Model:** `partner_contact_group`\
> **Menu:** Contacts > Configuration > Contact Groups\
> **Actor:** user in group `Partner Contact Groups`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Partner Contact Groups`.

## Flow

1. Open the **Contacts > Configuration > Contact Groups** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
