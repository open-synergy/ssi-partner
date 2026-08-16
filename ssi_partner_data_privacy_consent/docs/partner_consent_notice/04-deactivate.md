# Deactivate Privacy Notice

> **Module:** ssi_partner_data_privacy_consent\
> **Model:** `partner_consent_notice`\
> **Menu:** Contacts > Configuration > Data Privacy > Privacy Notice\
> **Actor:** user in group `Partner Consent Privacy Notice`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Partner Consent Privacy Notice`.

## Flow

1. Open the **Contacts > Configuration > Data Privacy > Privacy Notice** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated notices cannot be selected on new `res.partner.consent` records.
- Consents that already reference this notice can still be viewed.
