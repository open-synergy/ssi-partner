# Edit Contact Group

> **Module:** ssi_partner\
> **Model:** `partner_contact_group`\
> **Menu:** Contacts > Configuration > Contact Groups\
> **Actor:** user in group `Partner Contact Groups`\
> **Requires:** `01-create`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Record:** The record to edit already exists.
- **Access:** User is in group `Partner Contact Groups`.

## Flow

1. Open the **Contacts > Configuration > Contact Groups** menu.
2. Find and open the record to edit.
3. Change the **Name**, **Code**, or **Note** fields as needed.
4. To change **Commercial Contact**, select a different parent/commercial contact.
   Changing it clears the current **Contacts** selection, since the list of selectable
   contacts changes with it.
5. Add or remove entries in **Contacts**, choosing only from the child contacts of the
   current **Commercial Contact**.
6. Click **Generate Code** in the header to assign a value to the **Code** field from
   the configured sequence template — for example after resetting **Code** back to
   **/**. Only applies when **Code** is still **/**; records with a manually entered
   code are left unchanged.
7. Click **Save**.

## Post-Condition

- The record is updated with the new values.
- If **Generate Code** was used, the **Code** field now holds a value from the
  configured sequence template.
