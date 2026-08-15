# Delete Partner Evaluation Value Item

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation_value_item`
>
> **Menu:** Contacts > Configuration > Partner Evaluation > Value Items
>
> **Actor:** user in group _Partner Evaluation Value Item_
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any `partner_evaluation_value_set` line or
  evaluation question.
- **Access:** User has _Partner Evaluation Value Item_ access right.

## Flow

1. Open the **Contacts > Configuration > Partner Evaluation > Value Items** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
