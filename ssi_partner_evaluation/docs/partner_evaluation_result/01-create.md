# Create Partner Evaluation Result

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation_result`
>
> **Menu:** Contacts > Configuration > Partner Evaluation > Results
>
> **Actor:** user in group _Partner Evaluation Result_

## Pre-Condition

- **Data:** A `res.partner.category` tag exists if the result should apply a tag to the
  partner.
- **Access:** User has _Partner Evaluation Result_ access right.

## Flow

1. Open the **Contacts > Configuration > Partner Evaluation > Results** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: label of the result (e.g. "Pass", "Fail").
   - **Tag**: the `res.partner.category` applied to a partner when this result becomes
     their latest evaluation outcome.
4. Click **Save**.

## Post-Condition

- A new evaluation result record is created.
- The result becomes selectable in a `partner_evaluation_type`'s **Allowed Results** and
  in `result_computation_code`.
