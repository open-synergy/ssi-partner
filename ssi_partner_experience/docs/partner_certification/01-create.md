# Create Certification

> **Module:** ssi_partner_experience\
> **Model:** `partner.certification`\
> **Menu:** Contacts > Configuration > Experiences > Certifications\
> **Actor:** user in group `Contact's Certification Experience`

## Pre-Condition

- **Data:** The contact (`res.partner`) this certification belongs to already exists.
- **Access:** User is in group `Contact's Certification Experience`.

## Flow

1. Open the **Contacts > Configuration > Experiences > Certifications** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Partner** _(required)_: Select the contact this certification belongs to.
   - **Date Start** _(required)_: Enter the date this certification was obtained.
   - **Date End** _(required if **Expire** is checked)_: Enter the date this
     certification expires. **Expire** is checked by default; uncheck it if the
     certification does not expire so **Date End** is no longer required.
4. Optionally fill in the remaining fields:
   - **Certification**: A name identifying this certification.
   - **Certification Number**: The certificate number issued.
   - **Issued By**: The authority that issued this certification.
   - **Location**: Where this certification was issued.
5. Optionally fill in the **Note** tab with free-text notes about this certification.
6. Click **Save**.

## Post-Condition

- A new **Certification** record is created and appears in the Certifications list.
- The record also appears on the **Experiences** page of the related contact's form,
  under **Certifications**.
