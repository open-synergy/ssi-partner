# Deactivate Contact Group

> **Module:** ssi_partner\
> **Model:** `partner_contact_group`\
> **Menu:** Contacts > Configuration > Contact Groups\
> **Actor:** user in group `Partner Contact Groups`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Partner Contact Groups`.

## Flow

1. Open the **Contacts > Configuration > Contact Groups** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- The **Commercial Contact** and **Contacts** partner records themselves are not
  affected.
