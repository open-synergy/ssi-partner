# Create Partner Evaluation Value Set

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation_value_set`
>
> **Menu:** Contacts > Configuration > Partner Evaluation > Value Sets
>
> **Actor:** user in group _Partner Evaluation Value Set_

## Pre-Condition

- **Data:** At least one `partner_evaluation_value_item` exists to add as a line.
- **Access:** User has _Partner Evaluation Value Set_ access right.

## Flow

1. Open the **Contacts > Configuration > Partner Evaluation > Value Sets** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the **Name** of the value set.
4. On the **Items** tab, add one line per allowed value item.
5. Click **Save**.

## Post-Condition

- A new value set record is created with its ordered value items.
- The value set becomes selectable as a qualitative question's **Value Set**.
