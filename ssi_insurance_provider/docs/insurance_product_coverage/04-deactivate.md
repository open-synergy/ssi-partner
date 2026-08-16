# Deactivate Insurance Product Coverage

> **Module:** ssi_insurance_provider\
> **Model:** `insurance_product_coverage`\
> **Menu:** Contacts > Configuration > Insurance Provider > Coverages\
> **Actor:** user in group `Insurance Product Coverage`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Insurance Product Coverage`.

## Flow

1. Open the **Contacts > Configuration > Insurance Provider > Coverages** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated coverage types cannot be selected on new insurance products.
- Insurance products that already use this coverage type can still be viewed.
