# Delete Partner Evaluation Result

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation_result`
>
> **Menu:** Contacts > Configuration > Partner Evaluation > Results
>
> **Actor:** user in group _Partner Evaluation Result_
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by any `partner_evaluation_type`,
  `partner_evaluation`, or `res.partner.evaluation_result`.
- **Access:** User has _Partner Evaluation Result_ access right.

## Flow

1. Open the **Contacts > Configuration > Partner Evaluation > Results** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
