# Create Professional Experience

> **Module:** ssi_partner_experience\
> **Model:** `partner.experience`\
> **Menu:** Contacts > Configuration > Experiences > Professional Experiences\
> **Actor:** user in group `Contact's Professional Experience`

## Pre-Condition

- **Data:** The contact (`res.partner`) this experience belongs to already exists.
- **Access:** User is in group `Contact's Professional Experience`.

## Flow

1. Open the **Contacts > Configuration > Experiences > Professional Experiences** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Partner** _(required)_: Select the contact this professional experience belongs
     to.
   - **Date Start** _(required)_: Enter the date this job started.
   - **Date End** _(required if **Expire** is checked)_: Enter the date this job ended.
     **Expire** is checked by default; uncheck it if the job is still ongoing so **Date
     End** is no longer required.
4. Optionally fill in the remaining fields:
   - **Job Position**: The role held during this experience.
   - **Job Level**: The seniority level of the role.
   - **Employer**: The company or institution this experience was held at.
   - **Location**: Where this job took place.
5. Optionally fill in the **Note** tab with free-text notes about this experience.
6. Click **Save**.

## Post-Condition

- A new **Professional Experience** record is created and appears in the Professional
  Experiences list.
- The record also appears on the **Experiences** page of the related contact's form,
  under **Professional Experiences**.
