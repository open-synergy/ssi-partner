# Create Insurance Product

> **Module:** ssi_insurance_provider\
> **Model:** `insurance_product`\
> **Menu:** Contacts > Configuration > Insurance Provider > Products\
> **Actor:** user in group `Insurance Product`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** An active `sequence.template` for this model is set, if the **Generate
  Code** button will be used instead of a manual code.
- **Data:** An active `insurance_product_coverage` record exists.
- **Data:** The provider (a `res.partner` record) already exists.
- **Access:** User is in group `Insurance Product`.

## Flow

1. Open the **Contacts > Configuration > Insurance Provider > Products** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: the insurance product label.
   - **Code**: a unique identifier, or leave as **/** to assign it later.
   - **Provider**: the partner offering this product.
   - **Coverage Type**: the coverage classification for this product.
   - **Currency**: the currency used for the rates and cap amounts.
4. In the header, click **Generate Code** to assign a code from the configured sequence
   template. Only applies when **Code** is still **/**. Skip this step to keep a
   manually typed code.
5. On the **Rates** tab, add rate lines with **Effective Date**, **Employer Rate (%)**,
   **Employee Rate (%)**, and **Cap Amount** as needed. This step is optional; the
   product can be saved without rates.
6. Click **Save**.

## Post-Condition

- A new record is created and **Active**.
