# Delete Consent Purpose

> **Module:** ssi_partner_data_privacy_consent\
> **Model:** `partner_consent_purpose`\
> **Menu:** Contacts > Configuration > Data Privacy > Consent Purpose\
> **Actor:** user in group `Partner Consent Purpose`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any `partner_consent_notice` or
  `res.partner.consent` record.
- **Access:** User is in group `Partner Consent Purpose`.

## Flow

1. Open the **Contacts > Configuration > Data Privacy > Consent Purpose** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
