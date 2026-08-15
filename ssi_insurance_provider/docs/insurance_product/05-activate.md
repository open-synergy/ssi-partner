# Activate Insurance Product

> **Module:** ssi_insurance_provider\
> **Model:** `insurance_product`\
> **Menu:** Contacts > Configuration > Insurance Provider > Products\
> **Actor:** user in group `Insurance Product`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Insurance Product`.

## Flow

1. Open the **Contacts > Configuration > Insurance Provider > Products** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected in new transactions again.
