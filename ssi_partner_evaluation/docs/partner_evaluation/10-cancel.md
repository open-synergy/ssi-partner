# Cancel Partner Evaluation

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation`
>
> **Menu:** Contacts > Partner Evaluation > Evaluations
>
> **Actor:** user in group _Partner Evaluation - User_
>
> **State:** `draft` | `open` | `confirm` | `done` → `cancel`
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status allows cancellation (**Draft**, **On Progress**, **Waiting for
  Approval**, or **Done**).
- **Config:** An active `policy.template` grants `cancel_ok` for that state to the
  actor's group.
- **Access:** User has _Can Cancel_ access right.

## Flow

1. Open the **Contacts > Partner Evaluation > Evaluations** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. In the wizard that appears, select the **Cancellation Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancelled**.
- Question lines linked to this evaluation are deleted.
