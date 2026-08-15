# Create Religion

> **Module:** ssi_partner\
> **Model:** `res_partner_religion`\
> **Menu:** Contacts > Configuration > Religion\
> **Actor:** user in group `Religion`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** An active `sequence.template` for model `res_partner_religion` is
  configured. Only needed if the **Generate Code** button will be used to auto-assign
  the **Code** field.
- **Access:** User is in group `Religion`.

## Flow

1. Open the **Contacts > Configuration > Religion** menu.
2. Click the **Create** button.
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name of the religion.
   - **Code** _(required)_: Enter a unique code, or enter **/** to leave it blank for
     now and assign it later with the **Generate Code** button.
4. Click **Generate Code** in the header to assign a value to the **Code** field from
   the configured sequence template. Only applies when **Code** is still **/** — records
   with a manually entered code are left unchanged. Skip this step if a code was already
   entered manually in step 3.
5. Optionally fill in the **Note** tab with free-text notes.
6. Click **Save**.

## Post-Condition

- A new **Religion** record is created and appears in the Religion list.
- If **Generate Code** was used, the **Code** field now holds a value from the
  configured sequence template.
- The record becomes selectable in the **Religion** field on individual `res.partner`
  records.
