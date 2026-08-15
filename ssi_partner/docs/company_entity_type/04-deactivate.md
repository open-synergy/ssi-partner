# Deactivate Company Entity Type

> **Module:** ssi_partner\
> **Model:** `company_entity_type`\
> **Menu:** Contacts > Configuration > Entity Types\
> **Actor:** user in group `Entity Type`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Entity Type`.

## Flow

1. Open the **Contacts > Configuration > Entity Types** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated entity types cannot be selected on new company `res.partner` records.
- Companies that already reference this entity type can still be viewed.
