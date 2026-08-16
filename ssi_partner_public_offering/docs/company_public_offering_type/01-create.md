# Create Company Public Offering Type

> **Module:** ssi_partner_public_offering\
> **Model:** `company_public_offering_type`\
> **Menu:** Contacts > Configuration > Public Offering Types\
> **Actor:** user in group `Public Offering Types`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** An active `sequence.template` for model `company_public_offering_type` is
  configured. Only needed if the **Generate Code** button will be used to auto-assign
  the **Code** field.
- **Access:** User is in group `Public Offering Types`.

## Flow

1. Open the **Contacts > Configuration > Public Offering Types** menu.
2. Click the **Create** button.
3. Fill in the required fields:
   - **Name** _(required)_: Enter a name that identifies this public offering type (e.g.
     "Initial Public Offering").
   - **Code** _(required)_: Enter a unique code, or enter **/** to leave it blank for
     now and assign it later with the **Generate Code** button.
4. Click **Generate Code** in the header to assign a value to the **Code** field from
   the configured sequence template. Only applies when **Code** is still **/** — records
   with a manually entered code are left unchanged. Skip this step if a code was already
   entered manually in step 3.
5. Optionally fill in the **Note** tab with free-text notes about this public offering
   type.
6. Click **Save**.

## Post-Condition

- A new **Company Public Offering Type** record is created and appears in the Public
  Offering Types list.
- If **Generate Code** was used, the **Code** field now holds a value from the
  configured sequence template.
- The record becomes selectable in the **Public Offering** field on `res.partner`
  records.
