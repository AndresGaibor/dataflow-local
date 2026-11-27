---
title: "Administering Qlik Predict"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-managing-experiments-deployments.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud"]
---

# Administering Qlik Predict

Qlik Predict resources and user permissions can be administered in the Administration activity center.

Administering Qlik Predict involves the following:

- Viewing and administering ML resources and jobs, including activating and deactivating models for making predictions. This is configured in the Qlik Predict section of the Administration activity center.
- Controlling user access and permissions for working with Qlik Predict resources. This is configured in the Manage users section of the Administration activity center.
- Monitoring the consumption of the allotted ML resources for the subscription. Monitor consumption metrics in the Home and Qlik Predict sections of the Administration activity center.
- Generating training reports for models trained with Qlik Predict.

For information on how to create experiments and deployments, see [*Machine learning with Qlik Predict*](../AutoML/home-automl.htm).

## Types of administrators for Qlik Predict

Several permissions allow a user to perform administrator actions related to Qlik Predict. More than one of these permissions can be applied to a single user. The following list outlines each user scenario for administering Qlik Predict:

- Tenant administrators: User with the Tenant Admin role.
- Analytics administrators: Users with the Analytics Admin role.
- Model approver administrators: Users who can activate and deactivate models, and perform other Qlik Predict actions in the Administration activity center. These are users who have the Approve and reject ML models permission set to Allowed.
- Qlik Predict administrators:  Users who can view all experiments, deployed models, and ML deployments. These users can also activate and deactivate models. These are users who have the Manage ML experiments and deployments permission set to Allowed.

The following table outlines what is possible for each user scenario.

Permissions for administrators in Qlik Predict

| Action | Tenant admin supported | Analytics admin supported | Model approver administrator supported | Qlik Predict administrator supported |
| --- | --- | --- | --- | --- |
| Configure user roles and permissions | Yes | No | No | No |
| View all experiments, deployed models, and ML deployments | Yes | Yes | Yes | Yes |
| Move any ML deployment in any personal space to any shared or managed space (or your own personal space) | Yes | No | No | Yes |
| Delete any experiment or deployment | Yes | Yes | No | Yes |
| Activate and deactivate any deployed model | Yes | No | Yes | Yes |
| Monitor consumption of Qlik Predict capacities for the subscription | Yes | Yes | Yes | Yes |
| View, stop, and cancel Qlik Predict jobs | Yes | Yes | No | No |
| Configure additional model approval notices | Yes | Yes | Yes | Yes |
| Generate training reports for machine learning models | Yes | Yes | No | Yes |

## Navigating the Qlik Predict section in the Administration activity center

Administer Qlik Predict in the Qlik Predict section in the Administration [activity center](#glossary-0 "Glossary term"). All types of Qlik Predict administrators can view the information in this section. Depending on which type of administrator you are, you might be restricted from performing certain actions.

### Deployed models

The Deployed models tab shows all the models that have been deployed into ML deployments. Administrators can manage the following:

- Activate and deactivate models for making predictions from associated ML deployments.

  [*Working with model approval as an administrator*](mc-approve-models-admin.htm)
- View the source ML experiment where a model was trained.
- View the approval status and last approver of a model.
- Monitor all instances of where a model is deployed.
- Generate training reports for deployed models.

Click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to a model to access additional details, including model history, details about the source experiment, and the name of the training dataset.

### ML deployments

The ML deployments tab shows all ML deployment in the tenant. Details available include:

- Date when the source model was deployed into the ML deployment.
- Name, status, and last approver of the source model.

Click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to a model to access details about the source model for an ML deployment, including model history and information about the source [experiment](#glossary-1 "Glossary term").

### Active jobs

In the Active jobs tab, cancel or stop ongoing Qlik Predict jobs. For more information, see [*Stopping or canceling jobs*](#Stopping).

### Jobs history

In the Jobs history tab, view past Qlik Predict jobs. For more information, see [*Viewing job history*](#ViewPastJobs).

### Settings

The Settings tab allows you to configure additional options for model approval notifications across the tenant. For more information, see [*Configuring an additional approval notice*](#ApprovalNotice).

## Managing Qlik Predict permissions for users

For users to view and work with Qlik Predict resources, they typically need a combination of user entitlement, permissions assigned through the default permissions and custom roles, and built-in security roles. In shared and managed spaces, access controls are further defined by space roles.

For more information, see:

- [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm)
- User-based subscriptions: [*Assigning security roles and custom roles*](SaaS-roles.htm)
- Capacity-based subscriptions: [*Assigning security roles and custom roles*](SaaS-roles-capacity-model.htm)

## Model approval for administrators

Before generating [predictions](#glossary-2 "Glossary term"), a user or an administrator must approve the model within an ML deployment.

For more information about model approval for administrators, see [*Working with model approval as an administrator*](mc-approve-models-admin.htm).

Model approval methods and required permissions

| Approval method | Where approval is performed | Required permissions |
| --- | --- | --- |
| User | ML deployment | - Professional user entitlement (applies only to user-based subscriptions). - One of the following sets of permissions:    - Option 1 — all of the following:      - Automl Deployment Contributor built-in security role     - Approve or reject your ML models user permission set to Allowed via default permissions or custom security role   - Option 2 — one of the following:      - Manage ML deployments user permission set to Allowed via default permissions or custom security role     - Manage ML experiment and deployments admin permission set to Allowed via custom security role     - Approve or reject ML models admin permission set to Allowed via custom security role - Required space role in the space of the ML deployment    - For deployments in shared spaces, one of the following:      - Owner (of the space)     - Can manage     - Can edit   - For deployments in managed spaces, one of the following:      - Owner (of the space)     - Can manage |
| Administrator | Administration activity center | One of the following:   - Tenant Admin security role - Manage ML experiment and deployments admin permission set to Allowed via default permissions or custom security role - Approve or reject ML models admin permission set to Allowed via default permissions or custom security role |

### Configuring an additional approval notice

Whenever a user opens an ML deployment that uses a model that is pending approval, a message appears to notify them that model approval has been requested. This message is also shown when a user creates the first ML deployment from a given model.

As an administrator, you can add an additional notice to appear with this message. To modify the content of this notice, you need one of the following:

- Tenant Admin security role
- The administrator permission for Approve or reject ML models set to Allowed
- The administrator permission for Manage ML experiments and deployments set to Allowed

Do the following:

1. In the Administration activity center, go to Qlik Predict.
2. Open the Settings tab.
3. In the Additional notice field, type the additional notice you want to show to users.

## Monitoring jobs

In the Administration activity center, tenant and analytics administrators can view all content about Qlik Predict jobs. They can see currently running, queued, and historical jobs for model training, deployment, and [prediction](#glossary-4 "Glossary term") generation. Filter the list on the job type, user, and status.

### Viewing job history

Tenant and analytics administrators can view past Qlik Predict jobs in the Jobs history tab.

1. In Administration, go to Qlik Predict.
2. Open the Jobs history tab.

### Stopping or canceling jobs

Tenant and analytics administrators can stop or cancel jobs as needed in the Active jobs tab.

Do the following:

1. In Administration, go to Qlik Predict.
2. Open the Active jobs tab.
3. Click ![Three dots to show more options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a job.

   Information noteAlternatively, select multiple jobs by clicking the rows for each job.
4. Click Cancel job.
5. Confirm in the Job cancellation dialog.

The jobs are canceled.

## Monitoring Qlik Predict consumption for the subscription

You can monitor how many deployed models are currently activated for creating predictions. In the Administration activity center, open the Home or Qlik Predict section. The following charts show how much of the deployed model capacity (counting only active models) is remaining for the subscription:

- Qlik Predict deployed models
- Qlik Predict deployed models with predictions active

This information can also be viewed in the ML deployment interface by any user who opens the resource. The information is shown in the model status section at the top of the page.

A Qlik Cloud Analytics subscription defines a maximum number of deployed models that can be active at the same time (across all tenants within the subscription, for multi-tenant subscriptions). This consumption limit is defined per model, meaning that multiple ML deployments created from a single model count as a single deployed model. If you have reached the maximum number of active deployed models, you can do one of the following:

- Deactivate one or more currently active models to make room for new ones.
- Delete one or more existing deployed models to make room for new ones.
- If you need to have all current and future models activated at the same time, upgrade the subscription to a higher tier. For information about upgrade options, see the [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) product description.

## Generating training reports

Administrators can download training reports for models trained with Qlik Predict. Training reports are in PDF format and are downloaded directly to the user's local machine.

Without any administrator privileges, Qlik Predict users can generate training reports for models from experiments and deployments they have access to. Tenant and analytics administrators, as well as users with the Manage ML experiments and deployments permission set to Allowed, can generate reports in the following ways:

- From the Administration activity center.
- From an ML experiment.
- From an ML deployment.

For more information, see [*Downloading ML training reports as an administrator*](mc-training-report.htm).
