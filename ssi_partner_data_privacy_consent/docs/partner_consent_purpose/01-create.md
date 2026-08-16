# Create Consent Purpose

> **Module:** ssi_partner_data_privacy_consent\
> **Model:** `partner_consent_purpose`\
> **Menu:** Contacts > Configuration > Data Privacy > Consent Purpose\
> **Actor:** user in group `Partner Consent Purpose`

## Pre-Condition

- **Access:** User is in group `Partner Consent Purpose`.

## Flow

1. Open the **Contacts > Configuration > Data Privacy > Consent Purpose** menu.
2. Click the **Create** button.
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name of the data-processing purpose.
   - **Code** _(required)_: Enter a unique code, or enter **/** to leave it unassigned
     for now.
4. Optionally fill in the **Note** tab with free-text notes.
5. Click **Save**.

## Post-Condition

- A new **Consent Purpose** record is created and appears in the Consent Purpose list.
- The record becomes selectable as a **Purpose** on `partner_consent_notice` and
  `res.partner.consent` records.
