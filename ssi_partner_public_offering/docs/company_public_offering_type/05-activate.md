# Activate Company Public Offering Type

> **Module:** ssi_partner_public_offering\
> **Model:** `company_public_offering_type`\
> **Menu:** Contacts > Configuration > Public Offering Types\
> **Actor:** user in group `Public Offering Types`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Public Offering Types`.

## Flow

1. Open the **Contacts > Configuration > Public Offering Types** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected again on `res.partner` records.
