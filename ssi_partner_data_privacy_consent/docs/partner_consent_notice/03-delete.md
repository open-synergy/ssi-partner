# Delete Privacy Notice

> **Module:** ssi_partner_data_privacy_consent\
> **Model:** `partner_consent_notice`\
> **Menu:** Contacts > Configuration > Data Privacy > Privacy Notice\
> **Actor:** user in group `Partner Consent Privacy Notice`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any `res.partner.consent` record (the
  relation is `ondelete="restrict"`).
- **Access:** User is in group `Partner Consent Privacy Notice`.

## Flow

1. Open the **Contacts > Configuration > Data Privacy > Privacy Notice** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
