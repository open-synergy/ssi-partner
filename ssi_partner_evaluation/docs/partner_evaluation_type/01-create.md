# Create Partner Evaluation Type

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation_type`
>
> **Menu:** Contacts > Configuration > Partner Evaluation > Types
>
> **Actor:** user in group _Partner Evaluation Type_

## Pre-Condition

- **Access:** User has _Partner Evaluation Type_ access right.

## Flow

1. Open the **Contacts > Configuration > Partner Evaluation > Types** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: label of the evaluation type.
   - **Result Computation Code**: Python snippet that sets a `result` variable to one of
     the allowed `partner_evaluation_result` records.
4. On the **Question** tab, add one line per question by selecting a **Question**
   (`partner_evaluation_question_type`).
5. On the **Result** tab, select the **Allowed Results** and confirm the **Result
   Computation Code**.
6. On the **Partners** tab, configure how eligible partners are selected (manual list,
   domain, or Python code).
7. Click **Save**.

## Post-Condition

- A new evaluation type record is created.
- The type becomes selectable when creating a `partner_batch_evaluation` or
  `partner_evaluation`, and from the **Evaluate Partner** wizard.
