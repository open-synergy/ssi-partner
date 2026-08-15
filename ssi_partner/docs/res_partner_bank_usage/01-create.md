# Create Bank Account Usage

> **Module:** ssi_partner\
> **Model:** `res_partner_bank_usage`\
> **Menu:** Contacts > Configuration > Bank Account Usage\
> **Actor:** user in group `Bank Account Usage`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** An active `sequence.template` for model `res_partner_bank_usage` is
  configured. Only needed if the **Generate Code** button will be used to auto-assign
  the **Code** field.
- **Access:** User is in group `Bank Account Usage`.

## Flow

1. Open the **Contacts > Configuration > Bank Account Usage** menu.
2. Click the **Create** button.
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name of the usage (e.g. "Operational", "Payroll",
     "Tax", "Escrow").
   - **Code** _(required)_: Enter a unique code, or enter **/** to leave it blank for
     now and assign it later with the **Generate Code** button.
4. Click **Generate Code** in the header to assign a value to the **Code** field from
   the configured sequence template. Only applies when **Code** is still **/** — records
   with a manually entered code are left unchanged. Skip this step if a code was already
   entered manually in step 3.
5. Optionally fill in the **Note** tab with free-text notes.
6. Click **Save**.

## Post-Condition

- A new **Bank Account Usage** record is created and appears in the Bank Account Usage
  list.
- If **Generate Code** was used, the **Code** field now holds a value from the
  configured sequence template.
- The record becomes selectable in the **Usage** field on `res.partner.bank` records.
