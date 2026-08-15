# Cancel Partner Batch Evaluation

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_batch_evaluation`
>
> **Menu:** Contacts > Partner Evaluation > Batch Evaluations
>
> **Actor:** user in group _Partner Batch Evaluation - User_
>
> **State:** `draft` | `confirm` | `done` → `cancel`
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status allows cancellation (**Draft**, **Waiting for Approval**, or
  **Done**).
- **Config:** An active `policy.template` grants `cancel_ok` for that state to the
  actor's group.
- **Access:** User has _Can Cancel_ access right.

## Flow

1. Open the **Contacts > Partner Evaluation > Batch Evaluations** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. In the wizard that appears, select the **Cancellation Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancelled**.
- Evaluations created by this batch are deleted.
