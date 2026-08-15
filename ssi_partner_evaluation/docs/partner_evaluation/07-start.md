# Start Partner Evaluation

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation`
>
> **Menu:** Contacts > Partner Evaluation > Evaluations
>
> **Actor:** user in group _Partner Evaluation - User_
>
> **State:** `draft` → `open`
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for `partner_evaluation` grants `open_ok` for
  state `draft` to the actor's group.
- **Config:** An active `sequence.template` exists for this model.
- **Access:** User has _Can Start_ access right.

## Flow

1. Open the **Contacts > Partner Evaluation > Evaluations** menu.
2. Open the record to start.
3. Click the **Start** button.

## Post-Condition

- Status changes to **On Progress** (`open`).
- A document number is assigned according to the sequence template.
- Question lines are created on the **Questions** tab, one per question configured on
  the evaluation type.
