# Activate Company Entity Type

> **Module:** ssi_partner\
> **Model:** `company_entity_type`\
> **Menu:** Contacts > Configuration > Entity Types\
> **Actor:** user in group `Entity Type`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Entity Type`.

## Flow

1. Open the **Contacts > Configuration > Entity Types** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected again on company `res.partner` records.
