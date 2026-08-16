# Edit Insurance Product Coverage

> **Module:** ssi_insurance_provider\
> **Model:** `insurance_product_coverage`\
> **Menu:** Contacts > Configuration > Insurance Provider > Coverages\
> **Actor:** user in group `Insurance Product Coverage`\
> **Requires:** `01-create`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Record:** The record already exists.
- **Access:** User is in group `Insurance Product Coverage`.

## Flow

1. Open the **Contacts > Configuration > Insurance Provider > Coverages** menu.
2. Find and open the record to edit.
3. Click the **Edit** button.
4. Change the required fields (**Name**, **Code**, or **Note**).
5. Click **Generate Code** to re-assign a code from the sequence template — for example
   after clearing **Code** back to **/**. Skip this step if keeping the current code.
6. Click **Save**.

## Post-Condition

- The record is updated with the new values.
