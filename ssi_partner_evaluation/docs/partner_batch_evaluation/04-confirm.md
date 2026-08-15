# Confirm Partner Batch Evaluation

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_batch_evaluation`
>
> **Menu:** Contacts > Partner Evaluation > Batch Evaluations
>
> **Actor:** user in group _Partner Batch Evaluation - User_
>
> **State:** `draft` → `confirm`
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Record:** The **Partners** tab has at least one partner.
- **Config:** An active `policy.template` for `partner_batch_evaluation` grants
  `confirm_ok` for state `draft` to the actor's group.
- **Config:** An active `approval.template` for this model matches this record and has
  at least one approver level.
- **Access:** User has _Can Confirm_ access right.

## Flow

1. Open the **Contacts > Partner Evaluation > Batch Evaluations** menu.
2. Open the record to confirm.
3. Click the **Confirm** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Waiting for Approval**.
- Approval records are created for each approver level defined by the approval template.
