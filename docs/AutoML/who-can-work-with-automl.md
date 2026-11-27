---
title: "Who can work with Qlik Predict"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/who-can-work-with-automl.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Administering Qlik Predict"]
---

# Who can work with Qlik Predict

Expand/Collapse all

# Who can work with Qlik Predict

Tenant administrators assign permissions and entitlements to allow users to perform actions in Qlik Predict. Users and administrators can assign space roles to further control access to ML resources in shared and managed spaces.

## Access control overview

The ability to perform actions in Qlik Predict is controlled by:

- User entitlement (applies only to user-based subscriptions)
- Assignment of built-in security roles
- Assignment of permissions through the default permissions and custom roles
- Space roles

### User entitlement

If you have a user-based subscription, users need Professional user entitlement for full Qlik Predict access. Users with Analyzer entitlement have limited permissions for running predictions.

For more information, see [*Managing user entitlements*](../Admin/SaaS-user-allocations.htm).

### Built-in security roles

The Automl Experiment Contributor and Automl Deployment Contributor roles are built-in security roles that provide user access to Qlik Predict functionality—specifically, working with experiments and deployments. These roles are assigned by tenant administrators on a per-user basis.

Built-in security roles provide similar permissions as the permissions available through the default permissions and custom security roles. Conflicting permissions are handled as follows:

- If a user does not have the required built-in security role, but has the equivalent permission through the default permissions or a custom security role, they are granted access to the functionality.
- If a user has the required built-in security role, but does not have the equivalent permission through the default permissions or a custom security role, they are granted access to the functionality.

In addition, the Tenant Admin and Analytics Admin roles provide administrator access to certain Qlik Predict actions. For a comparison of administrator privileges by role and permission, see [*Types of administrators for Qlik Predict*](../Admin/mc-managing-experiments-deployments.htm#Types).

For more information about built-in security roles, see:

- [*Permissions granted by security roles*](../Admin/SaaS-user-permissions-capacity-model.htm) (capacity-based subscriptions)
- [*Permissions granted by security roles*](../Admin/SaaS-user-permissions.htm) (user-based subscriptions)

### Default permissions and custom security roles

User access to Qlik Predict can be controlled by permissions assigned through the default permissions and custom security roles. Tenant administrators assign permissions by setting baseline permissions for all users, and then grant additional permissions for selected users as needed.

For a list of available Qlik Predict permissions, see [*Available default permissions and custom roles*](#Permissions).

These permissions provide similar access as built-in security roles. Conflicting permissions are handled as follows:

- If a user does not have the required permission, but has the equivalent built-in security role, they are granted the access to the functionality.
- If a user has the required permission, but does not have the equivalent built-in security role, they are granted the access to the functionality.

### Space roles

In addition to tenant-level permissions and built-in security roles, user access to working with ML resources in shared and managed spaces is further controlled by their space roles in these spaces. The administrator-assigned permissions are prerequisites for working with ML resources in spaces.

For more information, see:

- [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm)
- [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm)

## Available default permissions and custom roles

These permissions are assigned by tenant administrators to control user and administrator access to Qlik Predict across the tenant.

For more information, see:

- [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm) (capacity-based subscriptions)
- [*Default permissions and custom roles*](../Admin/permissions-scopes.htm) (user-based subscriptions)

### User permissions

Approve or reject your ML models

The Approve or reject your ML models permission has the following options:

- Allowed: From any ML deployment they can access, users can activate and deactivate predictions for the source model.
- Not allowed: From any ML deployment they can access, users cannot activate or deactivate predictions for the source model.

Manage ML deployments

The Manage ML deployments permission has the following options:

- Allowed: Users can view, manage, and delete, and run predictions with ML deployments. With sufficient permissions for the ML experiment, they can also deploy models to ML deployments. Additionally, users can view ML experiments.

  Users with Allowed can also:

  - Manage ML deployments by adding and removing models.
  - Activate and deactivate models for predictions.
  - Run all types of predictions—that is, batch predictions and predictions using the real-time predictions endpoint in the Machine Learning API or the Qlik Predict analytics connector.
- Run predictions only: Users can run predictions from ML deployments using the real-time predictions endpoint in the Machine Learning API or the Qlik Predict analytics connector. Other access to ML deployments, such as [batch predictions](#glossary-0 "Glossary term") and ML model management, is blocked.
- Not allowed: Users cannot view, manage, delete, or run predictions with ML deployments. They also cannot deploy models to ML deployments.

  Users with Not allowed cannot manage ML deployments by adding and removing deployed models to them, nor can they activate and deactivate these models for predictions.

Manage ML experiments

The Manage ML experiments permission has the following options:

- Allowed: Users can view, create, manage, and delete ML experiments, including in-product access to GenAI for bias detection feature recommendations. They can also deploy models from experiments into ML deployments.
- Manage ML experiments without GenAI: Users can view, create, manage, and delete ML experiments. They can also deploy models from experiments into ML deployments. They are blocked from using GenAI functionality in experiments—that is, using GenAI to recommend features for bias detection.
- Not allowed: Users cannot view, create, manage, or delete ML experiments.

### Admin permissions

Approve or reject ML models

The Approve or reject ML models admin permission has the following options:

- Allowed: In the Administration activity center, users can activate and deactivate predictions for any deployed model in the tenant. From any ML deployment they can access, users can also activate and deactivate predictions for the source model.
- Not allowed: In the Administration activity center, users cannot activate or deactivate predictions for any deployed model in the tenant. However, users can activate and deactivate predictions for the source model from any ML deployment they have access to.

Manage ML experiments and deployments

The Manage ML experiments and deployments admin permission has the following options:

- Allowed: Users can view, manage, and delete, and run predictions with ML deployments. With sufficient permissions for the ML experiment, they can also deploy models to ML deployments. Additionally, users can view ML experiments.
- Not allowed: Users cannot list or delete experiments or deployments, or activate and deactivate deployed models. They cannot access the Qlik Predict section of the Administration activity center.

## User access to ML experiments

Working with ML experiments generally involves the following action types:

- [*Listing and opening ML experiments*](#ListOpenExp)
- [*Creation, use, and management of ML experiments*](#CreateUseExp)
- [*Use of AI tools in ML experiments*](#CreateUseExpAI)

Listing and opening ML experiments

To list and open ML experiments, a user needs the following. Users meeting these requirements can also generate training reports and open lineage and impact analysis for the experiment.

- Professional user entitlement (applies only to user-based subscriptions)
- One of the following:

  - Automl Experiment Contributor built-in security role
  - Automl Deployment Contributor built-in security role
  - Manage ML experiments permission set to Allowed or Manage ML experiments without GenAI via default permissions or custom security role
  - Manage ML deployments permission set to Allowed via default permissions or custom security role
  - Manage ML experiments and deployments admin permission set to Allowed via custom security role
- For experiments in shared spaces, one of the following space roles in the space where the ML experiment is located:

  - Owner (of the space)
  - Can manage
  - Can edit

Creation, use, and management of ML experiments

Experiment creation, use, and management involves the following actions:

- Creating ML experiments
- Deleting ML experiments
- Editing ML experiments
- Moving ML experiments between spaces

To perform these actions, a user needs the following:

- Professional user entitlement (applies only to user-based subscriptions)
- One of the following:

  - Automl Experiment Contributor built-in security role
  - Manage ML experiments permission set to Allowed or Manage ML experiments without GenAI via default permissions or custom security role
- For experiments in shared spaces, one of the following space roles in the space where the ML experiment is located:

  - Owner (of the space)
  - Can manage
  - Can edit

In the case of moving between spaces, the user needs one of the above roles in both the current space and the destination space.

Use of AI tools in ML experiments

Generative AI is integrated into bias detection in ML experiments. To work with this functionality, a user needs:

- Professional user entitlement (applies only to user-based subscriptions)
- One of the following:

  - Automl Experiment Contributor built-in security role
  - Manage ML experiments permission set to Allowed via default permissions or custom security role
- For experiments in shared spaces, one of the following space roles in the space where the ML experiment is located:

  - Owner (of the space)
  - Can manage
  - Can edit

## User access to ML deployments and predictions

Working with ML deployments and predictions involves the following action types:

- [*Listing and opening ML deployments*](#ListMLDeploy)
- [*Model deployment and creation of ML deployments*](#ModelDeployment)
- [*Management of ML deployments*](#ManagementMLDeploy)
- [*Deleting ML deployments*](#DeleteMLDeploy)
- [*Running batch predictions*](#RunningBatch)
- [*Running real-time predictions*](#RunningRealTime)
- [*Running predictions with the Qlik Predict analytics connector*](#RunningConnector)
- [*Model approval*](#ModelApproval)

Listing and opening ML deployments

To list and open ML deployments, a user needs the following. Users meeting these requirements can also generate training reports and open lineage and impact analysis from the ML deployment. For generating training reports, the user needs view access to the experiment in which the model was trained.

- Professional user entitlement (applies only to user-based subscriptions)
- One of the following:

  - Automl Experiment Contributor built-in security role
  - Automl Deployment Contributor built-in security role
  - Manage ML experiments permission set to Allowed or Manage ML experiments without GenAI via default permissions or custom security role
  - Manage ML deployments permission set to Allowed via default permissions or custom security role
  - Manage ML experiments and deployments admin permission set to Allowed via custom security role
- For ML deployments in [shared spaces](#glossary-1 "Glossary term"), one of the following space roles in the space where the ML experiment is located:

  - Owner (of the space)
  - Can manage
  - Can edit
- For ML deployments in [managed spaces](#glossary-2 "Glossary term"), one of the following space roles in the space where the ML experiment is located:

  - Owner (of the space)
  - Can manage

Model deployment and creation of ML deployments

Model deployment and creation of ML deployments involves the following actions:

- Deploying models into new ML deployments
- Deploying models into existing ML deployments
- Removing models from ML deployments

To deploy models to an ML deployment (new or existing), a user needs the following:

- Professional user entitlement (applies only to user-based subscriptions)
- One of the following:

  - Automl Experiment Contributor built-in security role
  - Automl Deployment Contributor built-in security role
  - Manage ML experiments permission set to Allowed or Manage ML experiments without GenAI via default permissions or custom security role
  - Manage ML deployments permission set to Allowed via default permissions or custom security role
- Required space role in the space of the ML deployment

  - For deployments in shared spaces, one of the following:

    - Owner (of the space)
    - Can manage
    - Can edit
  - For deployments in managed spaces, one of the following:

    - Owner (of the space)
    - Can manage
- Required space role in the space of the ML experiment:

  - For experiments in shared spaces, one of the following:

    - Owner (of the space)
    - Can manage
    - Can edit

To remove models from an ML deployment, a user needs the following:

- Professional user entitlement (applies only to user-based subscriptions)
- Automl Deployment Contributor security role
- One of the following:

  - Automl Deployment Contributor built-in security role
  - Manage ML deployments permission set to Allowed via default permissions or custom security role
- Required space role in the space of the ML deployment

  - For deployments in shared spaces, one of the following:

    - Owner (of the space)
    - Can manage
    - Can edit
  - For deployments in managed spaces, one of the following:

    - Owner (of the space)
    - Can manage

Management of ML deployments

Managing ML deployments involves the following actions:

- Editing ML deployment details
- Creating, editing, deleting, and changing owner of batch prediction configurations
- Creating, editing, and deleting prediction schedules
- Creating, renaming, and deleting [model aliases](#glossary-3 "Glossary term") in an ML deployment
- Moving ML deployments between spaces

To perform these actions, a user needs the following:

- Professional user entitlement (applies only to user-based subscriptions)
- One of the following:

  - Automl Deployment Contributor built-in security role
  - Manage ML deployments permission set to Allowed via default permissions or custom security role
- Required space role in the space of the ML deployment (or, in the case of moving between spaces, in the current and destination space)

  - For deployments in shared spaces, one of the following:

    - Owner (of the space)
    - Can manage
    - Can edit
  - For deployments in managed spaces, one of the following:

    - Owner (of the space)
    - Can manage

Deleting ML deployments

To delete ML deployments, a user needs the following:

- Professional user entitlement (applies only to user-based subscriptions)
- One of the following:

  - Automl Deployment Contributor built-in security role
  - Manage ML deployments permission set to Allowed via default permissions or custom security role
  - Manage ML experiments and deployments admin permission set to Allowed via custom security role
- Required space role in the space of the ML deployment (or, in the case of moving between spaces, in the current and destination space)

  - For deployments in shared spaces, one of the following:

    - Owner (of the space)
    - Can manage
    - Can edit
  - For deployments in managed spaces, one of the following:

    - Owner (of the space)
    - Can manage

Running batch predictions

To run batch predictions, a user needs the following:

- Professional user entitlement (applies only to user-based subscriptions)
- One of the following:

  - Automl Deployment Contributor built-in security role
  - Manage ML deployments permission set to Allowed via default permissions or custom security role
- Required space role in the space of the ML deployment

  - For deployments in shared spaces, one of the following:

    - Owner (of the space)
    - Can manage
    - Can edit
  - For deployments in managed spaces, one of the following:

    - Owner (of the space)
    - Can manage
- Permissions to store datasets in the desired space. To store datasets in your personal space, you need the Private Analytics Content Creator built-in security role.

Running real-time predictions

To run real-time predictions via the real-time API endpoint, a user needs the following:

- One of the following:

  - Automl Deployment Contributor built-in security role
  - Manage ML deployments permission set to Allowed or Create predictions only via default permissions or custom security role
- Required space role in the space of the ML deployment

  - For deployments in shared spaces, one of the following:

    - Owner (of the space) (including Analyzer user)
    - Can manage
    - Can edit
    - Can consume data (including Analyzer user)
  - For deployments in managed spaces, one of the following:

    - Owner (of the space) (including Analyzer user)
    - Can manage
    - Can consume data (including Analyzer user)

Running predictions with the Qlik Predict analytics connector

To run predictions with the Qlik Predict analytics connector, a user with existing access to working with [data connections](#glossary-4 "Glossary term") needs the following:

- One of the following:

  - Automl Deployment Contributor built-in security role
  - Manage ML deployments permission set to Allowed or Create predictions only via default permissions or custom security role
- For using the connector in an application or script in your personal space, you need the Private Analytics Content Creator built-in security role.
- Required space role in the space of both the ML deployment and the Qlik Predict connection

  - In shared spaces, one of the following:

    - Owner (of the space) (including Analyzer user)
    - Can manage
    - Can edit
    - Can consume data (including Analyzer user)
  - In managed spaces, one of the following:

    - Owner (of the space) (including Analyzer user)
    - Can manage
    - Can consume data (including Analyzer user)

Model approval

To activate and deactivate a model within an ML deployment, a user needs the following:

- Professional user entitlement (applies only to user-based subscriptions).
- One of the following sets of permissions:

  - Option 1 — all of the following:

    - Automl Deployment Contributor built-in security role
    - Approve or reject your ML models user permission set to Allowed via default permissions or custom security role
  - Option 2 — one of the following:

    - Manage ML deployments user permission set to Allowed via default permissions or custom security role
    - Manage ML experiment and deployments admin permission set to Allowed via custom security role
    - Approve or reject ML models admin permission set to Allowed via custom security role
- Required space role in the space of the ML deployment

  - For deployments in shared spaces, one of the following:

    - Owner (of the space)
    - Can manage
    - Can edit
  - For deployments in managed spaces, one of the following:

    - Owner (of the space)
    - Can manage

For more information about model approval, see [*Approving deployed models*](approve-models.htm).

## Administering experiments and ML deployments

### Administering from Analytics or Insights activity centers

In the Analytics and Insights [activity centers](#glossary-5 "Glossary term"), administrators can perform various actions related to ML experiments and deployments. Possible actions for administrators can be:

- Actions that do not require any additional permissions other than the administrator access. See [*Types of administrators for Qlik Predict*](../Admin/mc-managing-experiments-deployments.htm#Types).
- Actions that may require space roles, as well as other permissions assigned through default permissions and custom roles.

### Administering from the Administration activity center

From the Administration activity center, tenant and analytics administrators, and users with specific permissions, can administer Qlik Predict.

For more information about model approval, see [*Approving deployed models*](approve-models.htm).
