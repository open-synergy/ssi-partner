# Create Formal Education Level

> **Module:** ssi_partner_education_level\
> **Model:** `partner.formal_education_level`\
> **Menu:** Contacts > Configuration > Education Levels > Education Level\
> **Actor:** user in group `Formal Education Level`

## Pre-Condition

- None.

## Flow

1. Open the **Contacts > Configuration > Education Levels > Education Level** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: Enter the formal education level name.
   - **Code**: Enter a unique code for this education level, or fill with **/** to
     generate it later using the **Generate Code** button.
   - **Sequence**: Defaults to **5**. Optionally change it to control the display order
     among other education levels.
4. Click **Save**.

## Post-Condition

- A new Formal Education Level record is created and available for selection as **Latest
  Formal Level Education** on a partner.
