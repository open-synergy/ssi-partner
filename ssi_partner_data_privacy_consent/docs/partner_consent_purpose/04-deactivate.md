# Deactivate Consent Purpose

> **Module:** ssi_partner_data_privacy_consent\
> **Model:** `partner_consent_purpose`\
> **Menu:** Contacts > Configuration > Data Privacy > Consent Purpose\
> **Actor:** user in group `Partner Consent Purpose`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Partner Consent Purpose`.

## Flow

1. Open the **Contacts > Configuration > Data Privacy > Consent Purpose** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated purposes cannot be selected on new `partner_consent_notice` or
  `res.partner.consent` records.
- Notices and consents that already reference this purpose can still be viewed.
