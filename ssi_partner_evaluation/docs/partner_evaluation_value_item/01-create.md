# Create Partner Evaluation Value Item

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation_value_item`
>
> **Menu:** Contacts > Configuration > Partner Evaluation > Value Items
>
> **Actor:** user in group _Partner Evaluation Value Item_

## Pre-Condition

- **Access:** User has _Partner Evaluation Value Item_ access right.

## Flow

1. Open the **Contacts > Configuration > Partner Evaluation > Value Items** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the **Name** of the value (e.g. "Excellent", "Good").
4. Click **Save**.

## Post-Condition

- A new value item record is created.
- The value item becomes selectable as a line inside a `partner_evaluation_value_set`.
