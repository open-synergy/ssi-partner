# Create Field of Study

> **Module:** ssi_partner_education_level\
> **Model:** `partner.field_of_study`\
> **Menu:** Contacts > Configuration > Education Levels > Field of Study\
> **Actor:** user in group `Field Of Study`

## Pre-Condition

- None.

## Flow

1. Open the **Contacts > Configuration > Education Levels > Field of Study** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: Enter the field of study name.
   - **Code**: Enter a unique code for this field of study, or fill with **/** to
     generate it later using the **Generate Code** button.
   - **Parent**: Optionally select a parent field of study to build a hierarchy.
4. Click **Save**.

## Post-Condition

- A new Field of Study record is created and available for selection as **Latest Field
  of Study** on a partner.
