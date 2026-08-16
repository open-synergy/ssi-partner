# Create Privacy Notice

> **Module:** ssi_partner_data_privacy_consent\
> **Model:** `partner_consent_notice`\
> **Menu:** Contacts > Configuration > Data Privacy > Privacy Notice\
> **Actor:** user in group `Partner Consent Privacy Notice`

## Pre-Condition

- **Access:** User is in group `Partner Consent Privacy Notice`.
- **Data:** (optional) At least one `partner_consent_purpose` record exists, if this
  notice needs to reference purposes.

## Flow

1. Open the **Contacts > Configuration > Data Privacy > Privacy Notice** menu.
2. Click the **Create** button.
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name of the privacy notice.
   - **Code** _(required)_: Enter a unique code, or enter **/** to leave it unassigned
     for now.
4. Open the **Privacy Notice** tab and fill in:
   - **Version** _(required)_: Enter the version identifier of this notice document.
   - **Effective Date** _(required)_: Defaults to today's date; change if the notice
     takes effect on a different date.
   - **Purposes**: Optionally select one or more `partner_consent_purpose` records
     covered by this notice.
   - **Body** _(required)_: Enter the exact text of the privacy notice.
5. Optionally fill in the **Note** tab with free-text notes.
6. Click **Save**.

## Post-Condition

- A new **Privacy Notice** record is created and appears in the Privacy Notice list.
- The record becomes selectable as a **Privacy Notice** on `res.partner.consent`
  records.
