# Deactivate Insurance Product

> **Module:** ssi_insurance_provider\
> **Model:** `insurance_product`\
> **Menu:** Contacts > Configuration > Insurance Provider > Products\
> **Actor:** user in group `Insurance Product`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Insurance Product`.

## Flow

1. Open the **Contacts > Configuration > Insurance Provider > Products** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated insurance products cannot be selected in new transactions.
- Transactions that already use this record can still be viewed.
