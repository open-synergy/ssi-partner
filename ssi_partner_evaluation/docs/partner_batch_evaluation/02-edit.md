# Edit Partner Batch Evaluation

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_batch_evaluation`
>
> **Menu:** Contacts > Partner Evaluation > Batch Evaluations
>
> **Actor:** user in group _Partner Batch Evaluation - User_
>
> **Requires:** `01-create`
>
> **Inline Actions:** `action_load_partner` (Load)

## Pre-Condition

- **Record:** Status is **Draft**.
- **Access:** User has _Can Create_ access right.

## Flow

1. Open the **Contacts > Partner Evaluation > Batch Evaluations** menu.
2. Find and open the record to edit.
3. Change the **Type**, **Date**, **Date Start**, or **Date End**.
4. On the **Partners** tab, click **Load** to refresh the partner list — for example
   after changing **Type** — replacing the current list with the partners matching the
   new configurator. You may also add or remove partners manually.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
