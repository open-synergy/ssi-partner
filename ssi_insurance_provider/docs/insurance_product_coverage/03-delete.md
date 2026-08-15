# Delete Insurance Product Coverage

> **Module:** ssi_insurance_provider\
> **Model:** `insurance_product_coverage`\
> **Menu:** Contacts > Configuration > Insurance Provider > Coverages\
> **Actor:** user in group `Insurance Product Coverage`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any insurance product.
- **Access:** User is in group `Insurance Product Coverage`.

## Flow

1. Open the **Contacts > Configuration > Insurance Provider > Coverages** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
