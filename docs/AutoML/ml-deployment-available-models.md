---
title: "Using multiple models in your ML deployment"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/ml-deployment-available-models.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML deployments"]
---

# Using multiple models in your ML deployment

You can deploy multiple models to your ML deployment, including models from different experiments. After [deploying models from experiments](deploying-models.htm), use the Deployable models pane in the ML deployment to configure dynamic prediction workflows. When generating predictions, the model you are using is referenced as an [alias](#glossary-0 "Glossary term"). This system of aliases allows you to replace models over time without needing to create a new ML deployment, and also eases comparative testing of model performance on production data.

Model aliases are used in both batch prediction and real-time prediction workflows. For information, see:

- [*Configuring model aliases for batch predictions*](alias-predictions-batch.htm)
- [*Working with model aliases in real-time predictions*](creating-real-time-predictions.htm#AliasPredictions)

Deployable models pane in an ML deployment

!['Deployable models' pane in Qlik Predict ML deployment interface](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-automl_available-models.png "Click to view full size")

## What are model aliases?

Each model you add to your ML deployment is referenced as a model alias. An alias is a dynamic container within your ML deployment that directs Qlik Predict to run predictions with a model in the deployment. Within the alias, models can be changed to allow easy replacement of out-of-date models. One model can be added per model alias. Aliases allow you to easily change models within a prediction generation workflow without the need for editing prediction configurations, creating a new ML deployment, or updating API calls.

Every ML deployment has a default alias. The default alias cannot be deleted or renamed, but you can easily change the model to use for generating predictions with it. If you do not specify an alias to use in predictions from your ML deployment, the default alias is used.

You can add up to 10 aliases within an ML deployment, including the default alias.

### Use cases for model aliases

- Replacing out-of-date models with retrained models over time without requiring updates to prediction configurations or API calls.
- Testing and comparing performance of different models on the same production data without having to create multiple ML deployments.
- Using a single deployment to generate predictions from different models depending on specific conditions.

## Considerations for deploying models to ML deployments

When adding models to an ML deployment, models can be from different ML experiments, which may be in different spaces in Qlik Cloud Analytics. Consider the following:

- To add a model to an ML deployment, the model needs to have the same experiment type (binary classification, multiclass classification, regression, or time series) as the model in the default alias.
- If the model schema and apply data are not compatible, predictions (batch, real-time, direct API, or connector-based) cannot run successfully.
- There are permissions requirements for the users adding models to deployments, as well as working with model aliases (for example, adding, renaming, and deleting aliases). For more information, see [*Permissions*](#Permissions).

## Working with aliases

You work with aliases in the Deployable models pane within the ML deployment. The Deployable models pane features an intuitive drag-and-drop interface for model assignment.

When you are finished making changes in the Deployable models, click Save changes in the top right corner of the interface.

Adding new aliases is optional. If you do not need to work with multiple aliases, you can work with the default alias only, and swap between models using only this alias.

### Getting started

Before you can assign models to aliases, you need to deploy all required models to the ML deployment. This process is performed in the ML experiment where each model was trained. For information, see [*Deploying models*](deploying-models.htm).

### Adding an alias

First, create a blank alias.

Do the following:

1. In the ML deployment, open the Deployable models pane.
2. Under Available models, click Add alias.
3. Click Save changes in the top right corner of the interface.

Alternatively, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a model under All models in the deployment, and select Add to new alias.

### Assigning a model to an alias (including the default alias)

After you have added the alias, you need to assign a model to it. You can also assign a different model to the default alias using this workflow.

Do the following:

1. Under All models in the deployment, find the model you want to assign to the alias.
2. Next to the Model name, drag the model onto the alias.

   Alternatively, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the model and select Add to <alias name>, or Swap to default alias to replace the model assigned to the default alias.
3. Click Save changes in the top right corner of the interface.

### Renaming and deleting aliases

You can rename and delete any alias except the default alias.

Do the following:

1. In the ML deployment, open the Deployable models pane.
2. Click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the model alias, and select Rename or Delete.
3. Click Save changes in the top right corner of the interface.

## Removing models from an ML deployment

Over time, you might need to remove models from the deployment.

Do the following:

1. In the ML deployment, open the Deployable models pane.
2. Under All models in the deployment, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the model and select Remove from deployment. In order to be able to remove a model from the deployment, the model needs to be unassigned from all aliases in the deployment.
3. Click Save changes in the top right corner of the interface.

## Permissions

Working with deployed models in ML deployments requires that you are assigned specific permissions. For information about required space roles, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](../Spaces/permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](../Spaces/permissions-managed-space-admin.htm)

If you are an administrator, you need to assign certain entitlements, security roles, and permissions to allow users to work with deployed models in ML deployments. See:

- [*Model deployment and creation of ML deployments*](who-can-work-with-automl.htm#ModelDeployment)
- [*Management of ML deployments*](who-can-work-with-automl.htm#ManagementMLDeploy)
