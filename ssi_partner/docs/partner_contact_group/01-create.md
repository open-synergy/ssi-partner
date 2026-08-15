# Create Contact Group

> **Module:** ssi_partner\
> **Model:** `partner_contact_group`\
> **Menu:** Contacts > Configuration > Contact Groups\
> **Actor:** user in group `Partner Contact Groups`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** An active `sequence.template` for model `partner_contact_group` is
  configured. Only needed if the **Generate Code** button will be used to auto-assign
  the **Code** field.
- **Data:** At least one `res.partner` record with no **Related Company** (i.e.
  `parent_id` not set) exists, to be selected as the **Commercial Contact**. That
  commercial contact has at least one child contact, to be selected in **Contacts**.
- **Access:** User is in group `Partner Contact Groups`.

## Flow

1. Open the **Contacts > Configuration > Contact Groups** menu.
2. Click the **Create** button.
3. Fill in the required fields:
   - **Name** _(required)_: Enter a name that identifies this contact group.
   - **Code** _(required)_: Enter a unique code, or enter **/** to leave it blank for
     now and assign it later with the **Generate Code** button.
   - **Commercial Contact** _(required)_: Select the parent/commercial contact whose
     children will be grouped.
   - **Contacts** _(required)_: Select one or more contacts from the child contacts of
     the selected **Commercial Contact**. Only contacts whose **Related Company** is the
     selected **Commercial Contact** can be chosen.
4. Click **Generate Code** in the header to assign a value to the **Code** field from
   the configured sequence template. Only applies when **Code** is still **/** — records
   with a manually entered code are left unchanged. Skip this step if a code was already
   entered manually in step 3.
5. Optionally fill in the **Note** tab with free-text notes.
6. Click **Save**.

## Post-Condition

- A new **Contact Group** record is created and appears in the Contact Groups list.
- If **Generate Code** was used, the **Code** field now holds a value from the
  configured sequence template.
- Changing **Commercial Contact** after **Contacts** has been filled clears the
  **Contacts** selection, since the list of selectable contacts changes with it.
