# Create Partner Batch Evaluation

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_batch_evaluation`
>
> **Menu:** Contacts > Partner Evaluation > Batch Evaluations
>
> **Actor:** user in group _Partner Batch Evaluation - User_
>
> **State:** `—` → `draft`
>
> **Inline Actions:** `action_load_partner` (Load)

## Pre-Condition

- **Config:** An active `policy.template` for `partner_batch_evaluation` grants
  `confirm_ok` for state `draft` to the actor's group.
- **Data:** A `partner_evaluation_type` exists.
- **Access:** User has _Can Create_ access right.

## Flow

1. Open the **Contacts > Partner Evaluation > Batch Evaluations** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Type**: the `partner_evaluation_type` this batch follows.
   - **Date**: defaults to today. Change if needed.
   - **Date Start** / **Date End**: the batch period.
4. On the **Partners** tab, click **Load** to populate the partner list with the
   partners matching the type's configurator (manual list, domain, or Python code). You
   may also add or remove partners manually. At least one partner must remain — later
   confirming the batch creates one evaluation per partner listed here.
5. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
