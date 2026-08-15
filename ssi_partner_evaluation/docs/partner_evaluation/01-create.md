# Create Partner Evaluation

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation`
>
> **Menu:** Contacts > Partner Evaluation > Evaluations
>
> **Actor:** user in group _Partner Evaluation - User_
>
> **State:** `—` → `draft`

## Pre-Condition

- **Config:** An active `policy.template` for `partner_evaluation` grants `open_ok` for
  state `draft` to the actor's group.
- **Data:** A `partner_evaluation_type` exists.
- **Access:** User has _Can Create_ access right.

## Flow

1. Open the **Contacts > Partner Evaluation > Evaluations** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Type**: the `partner_evaluation_type` this evaluation follows.
   - **Partner**: the partner being evaluated.
   - **Date**: date of the evaluation.
   - **Date Start** / **Date End**: the evaluation period.
4. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
