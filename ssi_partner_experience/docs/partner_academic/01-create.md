# Create Academic Experience

> **Module:** ssi_partner_experience\
> **Model:** `partner.academic`\
> **Menu:** Contacts > Configuration > Experiences > Academic Experiences\
> **Actor:** user in group `Contact's Academic Experience`

## Pre-Condition

- **Data:** The contact (`res.partner`) this academic record belongs to already exists.
- **Access:** User is in group `Contact's Academic Experience`.

## Flow

1. Open the **Contacts > Configuration > Experiences > Academic Experiences** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Partner** _(required)_: Select the contact this academic record belongs to.
   - **Date Start** _(required)_: Enter the date this study period started.
   - **Date End** _(required if **Expire** is checked)_: Enter the date this study
     period ended. **Expire** is checked by default; uncheck it if the study period is
     still ongoing so **Date End** is no longer required.
4. Optionally fill in the remaining fields:
   - **Institution**: The school or university this academic record belongs to.
   - **Location**: Where this institution is located.
   - **Diploma Number**: The diploma or certificate number issued.
   - **Education Level**: The level of education completed.
   - **Field of Study**: The major or field studied.
   - **Latest GPA**: The final grade point average obtained.
   - **Activities and associations**: Extracurricular activities or associations during
     this period.
5. Optionally fill in the **Note** tab with free-text notes about this academic record.
6. Click **Save**.

## Post-Condition

- A new **Academic Experience** record is created and appears in the Academic
  Experiences list.
- The record also appears on the **Experiences** page of the related contact's form,
  under **Academics**.
