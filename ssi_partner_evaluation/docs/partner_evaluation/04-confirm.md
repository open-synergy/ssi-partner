# Confirm Partner Evaluation

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation`
>
> **Menu:** Contacts > Partner Evaluation > Evaluations
>
> **Actor:** user in group _Partner Evaluation - User_
>
> **State:** `open` → `confirm`
>
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Config:** An active `policy.template` for `partner_evaluation` grants `confirm_ok`
  for state `open` to the actor's group.
- **Config:** An active `approval.template` for this model matches this record and has
  at least one approver level.
- **Access:** User has _Can Confirm_ access right.

## Flow

1. Open the **Contacts > Partner Evaluation > Evaluations** menu.
2. Open the record to confirm.
3. On the **Questions** tab, answer every question (fill in the manual
   qualitative/quantitative value where **Mode** is **Manual**).
4. Click the **Confirm** button.
5. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Waiting for Approval**.
- Approval records are created for each approver level defined by the approval template.
