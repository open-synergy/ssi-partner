# Edit Bank Account Usage

> **Module:** ssi_partner\
> **Model:** `res_partner_bank_usage`\
> **Menu:** Contacts > Configuration > Bank Account Usage\
> **Actor:** user in group `Bank Account Usage`\
> **Requires:** `01-create`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Record:** The record to edit already exists.
- **Access:** User is in group `Bank Account Usage`.

## Flow

1. Open the **Contacts > Configuration > Bank Account Usage** menu.
2. Find and open the record to edit.
3. Change the **Name**, **Code**, or **Note** fields as needed.
4. Click **Generate Code** in the header to assign a value to the **Code** field from
   the configured sequence template — for example after resetting **Code** back to
   **/**. Only applies when **Code** is still **/**; records with a manually entered
   code are left unchanged.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
- If **Generate Code** was used, the **Code** field now holds a value from the
  configured sequence template.
