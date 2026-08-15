# Delete Partner Evaluation Question Type

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation_question_type`
>
> **Menu:** Contacts > Configuration > Partner Evaluation > Question Types
>
> **Actor:** user in group _Partner Evaluation Question Type_
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any `partner_evaluation_type.question` or
  `partner_evaluation.question`.
- **Access:** User has _Partner Evaluation Question Type_ access right.

## Flow

1. Open the **Contacts > Configuration > Partner Evaluation > Question Types** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
