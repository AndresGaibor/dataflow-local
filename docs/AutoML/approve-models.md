---
title: "Approving deployed models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/approve-models.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML deployments"]
---

# Approving deployed models

Before a model within an ML deployment can generate predictions, it needs to be activated by someone with sufficient permissions. When a model is activated, all ML deployments that use this model are activated for predictions.

Models can be activated and deactivated as needed to help your organization optimize the usage of the Qlik Cloud subscription. The process of activating and deactivating models is known as model approval.

## Guide for administrators

This help topic describes the process of model approval for users who do not have any administrator privileges. For information about model approval for administrators, including assignment of model approver permissions, see [*Working with model approval as an administrator*](../Admin/mc-approve-models-admin.htm).

## About model approval

Model approval allows both users and administrators to control the number of deployed models within the Qlik Cloud subscription that are activated for making predictions. The Qlik Cloud subscription limits the number of deployed models that can be used for predictions at a given time. With model approval, users and administrators can activate or deactivate models, and assign permissions for model approval accordingly. This allows a more efficient usage of the subscription.

## Model approval status

The approval status of a deployed model indicates whether it can be used to make predictions. A deployed model can be in one of the following statuses at a given time:

- Active: The model is activated and able to generate predictions.
- Inactive: The model is deactivated and cannot generate predictions.
- Requested: Approval for the model has been requested but not yet provided.
  When a model is in Requested status, it does not count towards the total number of deployed models allowed for the subscription.

If you open an ML deployment and see a banner at the top of the screen allowing you to activate the default model, the default model is in the Inactive or Requested state. This banner is removed when the default model moves to an Active state.

## Activating and deactivating models as a user

### Activating the default model in the deployment

Do the following:

1. Open an ML deployment.
2. In the banner at the top of the ML deployment, click Activate model.
3. In the dialog that opens, click Activate model to confirm.

For the equivalent procedure for administrators, see [*Activating and deactivating models as an administrator*](../Admin/mc-approve-models-admin.htm#ApprovalProcedureAdmin).

### Activating and deactivating other models in the deployment

Do the following:

1. Open an ML deployment.
2. Switch to the Deployable models pane.
3. Under All models in the deployment, find the model to activate or deactivate.
4. Click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the model and select Set model to inactive.

For the equivalent procedure for administrators, see [*Activating and deactivating models as an administrator*](../Admin/mc-approve-models-admin.htm#ApprovalProcedureAdmin).

## Use cases

The primary benefit of model approval is to allow more efficient usage of the Qlik Cloud subscription. If desired, your organization can additionally use model approval to ensure optimum quality in deployed models. For example, you can assign a select number of users with permissions for model approval and restrict model approval for others. These model approvers can enforce quality assurance to help your organization generate more accurate and reliable predictions.

Deactivating a deployed model is an alternative to deleting the ML deployments that use it. When you deactivate a model, it is not counted as a usable deployed model in your Qlik Cloud subscription. This allows you to more efficiently use your tenant's allotted capacity for deployed models. For example, you can deactivate outdated models until new training data becomes available, allowing other users to run predictions from other models while there is capacity to do so.

## Methods and required permissions

The model within an ML deployment needs to be approved before it can generate [predictions](#glossary-2 "Glossary term"). Model approval can be performed by users and administrators.

Model approval methods and required permissions

| Approval method | Where approval is performed | Required permissions |
| --- | --- | --- |
| User | ML deployment | - Professional user entitlement (applies only to user-based subscriptions). - One of the following sets of permissions:    - Option 1 — all of the following:      - Automl Deployment Contributor built-in security role     - Approve or reject your ML models user permission set to Allowed via default permissions or custom security role   - Option 2 — one of the following:      - Manage ML deployments user permission set to Allowed via default permissions or custom security role     - Manage ML experiment and deployments admin permission set to Allowed via custom security role     - Approve or reject ML models admin permission set to Allowed via custom security role - Required space role in the space of the ML deployment    - For deployments in shared spaces, one of the following:      - Owner (of the space)     - Can manage     - Can edit   - For deployments in managed spaces, one of the following:      - Owner (of the space)     - Can manage |
| Administrator | Administration activity center | One of the following:   - Tenant Admin security role - Manage ML experiment and deployments admin permission set to Allowed via default permissions or custom security role - Approve or reject ML models admin permission set to Allowed via default permissions or custom security role |

### User method for model approval

A user (non-administrator) opens the ML deployment, and then activates or deactivates models from the Deployable models pane.

### Administrator method for model approval

An administrator activates or deactivates models from the Qlik Predict section in the Administration activity center.

## Assigning model approval permissions

For more information about how to assign permissions, see:

- [*Roles and permissions for users and administrators*](../Admin/permissions-admins-users.htm) (user-based subscriptions)
- [*Roles and permissions for users and administrators*](../Admin/permissions-admins-users-capacity-model.htm) (capacity-based subscriptions)

For more information about the available permissions in Qlik Cloud, see:

- [*Default permissions and custom roles*](../Admin/permissions-scopes.htm) (user-based subscriptions)
- [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm) (capacity-based subscriptions)

## Workflow

This section outlines a sample workflow that can be used to make the most out of model approval.

### Step 1: A user deploys the model

When a model is first deployed into an ML deployment, it enters Requested approval status. This means that the model can be approved by users and administrators.

### Step 2: The model is approved or rejected

A user or administrator needs to activate the model for making predictions. If a decision is made to not allow the model to generate predictions, an administrator approver can set it to Inactive, or it can be left in Requested status until approval is needed.

When a model in an ML deployment is approved and able to generate predictions, it has the Active status. When a model in an ML deployment has been deactivated from being able to make predictions, it has the Inactive status.

### Step 3: The model status is changed over time

Over time, a model might be replaced by other models, or the tenant might need to deactivate some models to allow other models to make predictions. This can be a temporary solution to more efficiently use the deployed models included in the subscription, or it might be permanent if you want to keep the model for reference purposes only.

## Learn more

- [*Default permissions and custom roles*](../Admin/permissions-scopes.htm)
