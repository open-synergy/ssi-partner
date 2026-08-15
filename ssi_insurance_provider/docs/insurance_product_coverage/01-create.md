# Create Insurance Product Coverage

> **Module:** ssi_insurance_provider\
> **Model:** `insurance_product_coverage`\
> **Menu:** Contacts > Configuration > Insurance Provider > Coverages\
> **Actor:** user in group `Insurance Product Coverage`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** An active `sequence.template` for this model is set, if the **Generate
  Code** button will be used instead of a manual code.
- **Access:** User is in group `Insurance Product Coverage`.

## Flow

1. Open the **Contacts > Configuration > Insurance Provider > Coverages** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: the coverage type label.
   - **Code**: a unique identifier, or leave as **/** to assign it later.
4. In the header, click **Generate Code** to assign a code from the configured sequence
   template. Only applies when **Code** is still **/**. Skip this step to keep a
   manually typed code.
5. Click **Save**.

## Post-Condition

- A new record is created and **Active**.
