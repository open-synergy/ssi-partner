# Activate Privacy Notice

> **Module:** ssi_partner_data_privacy_consent\
> **Model:** `partner_consent_notice`\
> **Menu:** Contacts > Configuration > Data Privacy > Privacy Notice\
> **Actor:** user in group `Partner Consent Privacy Notice`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Partner Consent Privacy Notice`.

## Flow

1. Open the **Contacts > Configuration > Data Privacy > Privacy Notice** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected again on new `res.partner.consent` records.
