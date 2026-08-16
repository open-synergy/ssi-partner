# Create Partner ID Category

> **Module:** ssi_partner_identification\
> **Model:** `res.partner.id_category`\
> **Menu:** Contacts > Configuration > Identities > ID Categories\
> **Actor:** user in group `Partner ID Categories`

## Pre-Condition

- **Access:** User is in group `Partner ID Categories`.

## Flow

1. Open the **Contacts > Configuration > Identities > ID Categories** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **ID name** _(required)_: the label of this identification type, for example
     "Driver License".
   - **Code** _(required)_: a short abbreviation for this identification type, up to 16
     characters, for example "driver_license".
4. Optionally fill in **Python validation code** with a snippet that validates the
   format of ID numbers assigned to this category. Leave empty to skip validation.
5. Click **Save**.

## Post-Condition

- A new record is created and **Active**.
- The category becomes selectable as **Category** when creating a Partner ID Number.
