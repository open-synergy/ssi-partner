# Activate Ethnicity

> **Module:** ssi_partner\
> **Model:** `res_partner_ethnicity`\
> **Menu:** Contacts > Configuration > Ethnicity\
> **Actor:** user in group `Ethnicity`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Ethnicity`.

## Flow

1. Open the **Contacts > Configuration > Ethnicity** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected again on individual `res.partner` records.
