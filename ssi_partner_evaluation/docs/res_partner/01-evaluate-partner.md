# Evaluate Partner

> **Module:** ssi_partner_evaluation
>
> **Extends:** base — model `res.partner`
>
> **Model:** `evaluate_partner`
>
> **Menu:** Contacts > Contacts (list or form view, **Action** menu)
>
> **Actor:** user in group _Partner Evaluation - User_

## Pre-Condition

- **Data:** At least one `partner_evaluation_type` exists.
- **Access:** User has _Partner Evaluation - User_ access right.

## Flow

1. Open the **Contacts > Contacts** menu.
2. Select one or more partners (check the checkbox on the list view), or open a single
   partner's form.
3. Click **Action** > **Evaluate Partner**.
4. In the wizard that appears:
   - **Partner**: defaults to the partner(s) selected in step 2. Add or remove partners
     as needed.
   - **Evaluation Types**: select one or more evaluation types.
5. Click **Confirm**.

## Post-Condition

- One `partner_evaluation` record is created in **Draft** status for every combination
  of selected partner and evaluation type.
- A list view opens showing the evaluations just created.
