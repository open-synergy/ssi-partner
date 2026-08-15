# Activate Religion

> **Module:** ssi_partner\
> **Model:** `res_partner_religion`\
> **Menu:** Contacts > Configuration > Religion\
> **Actor:** user in group `Religion`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Religion`.

## Flow

1. Open the **Contacts > Configuration > Religion** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected again on individual `res.partner` records.
