# Activate Company Ownership Type

> **Module:** ssi_partner\
> **Model:** `company_ownership_type`\
> **Menu:** Contacts > Configuration > Ownership Types\
> **Actor:** user in group `Ownership Type`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Ownership Type`.

## Flow

1. Open the **Contacts > Configuration > Ownership Types** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected again on company `res.partner` records.
