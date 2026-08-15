# Approve Partner Evaluation

> **Module:** ssi_partner_evaluation
>
> **Model:** `partner_evaluation`
>
> **Menu:** Contacts > Partner Evaluation > Evaluations
>
> **Actor:** approver on the level that is currently pending
>
> **State:** `confirm` → `done`
>
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` grants `approve_ok` to the actor's group.
- **Access:** User is registered as an approver on the approval level that is currently
  **pending**.
- **Access:** User has _Can Approve_ access right.

## Flow

1. Open the **Contacts > Partner Evaluation > Evaluations** menu.
2. Open the record to approve.
3. Click the **Approve** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- If all approval levels are fulfilled, status changes automatically to **Done**. The
  automatic and final results are computed, and a `res.partner.evaluation_result`
  tracker is created for the partner and type if one does not already exist.
- If there are still pending approval levels, status remains **Waiting for Approval**
  and the next level becomes pending.
