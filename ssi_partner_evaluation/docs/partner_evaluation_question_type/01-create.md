# Create Partner Evaluation Question Type

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation_question_type`
>
> **Menu:** Contacts > Configuration > Partner Evaluation > Question Types
>
> **Actor:** user in group _Partner Evaluation Question Type_

## Pre-Condition

- **Data:** A `partner_evaluation_value_set` exists when the question will be
  **Qualitative**.
- **Access:** User has _Partner Evaluation Question Type_ access right.

## Flow

1. Open the **Contacts > Configuration > Partner Evaluation > Question Types** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: label of the question.
4. On the **Detail** tab, fill in:
   - **Type**: **Qualitative** or **Quantitative**.
   - **Value Set**: required when **Type** is **Qualitative**.
   - **Mode**: **Manual** or **Automatic**.
   - **Computation Code**: required when **Mode** is **Automatic** — Python snippet that
     sets a `result` variable.
5. Click **Save**.

## Post-Condition

- A new question type record is created.
- The question type becomes selectable as a line on a `partner_evaluation_type`'s
  **Question** tab.
