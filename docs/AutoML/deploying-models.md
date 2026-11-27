---
title: "Deploying models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/deploying-models.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML deployments"]
---

# Deploying models

You can deploy models from experiments in personal or shared spaces. Deploying a model adds it to a new or existing ML deployment. ML deployments can be created in personal, shared, and managed spaces. An ML deployment can contain multiple models, which can be used across different prediction workflows. The number of ML deployments is limited by the subscription.

The tier included in a Qlik Cloud subscription defines a maximum number of deployed models that can be created across all tenants created within the license. This consumption limit is defined per model, meaning that multiple ML deployments created from a single model count as a single deployed model. If you have reached the maximum number of deployed models, delete one or more existing deployed models or upgrade the subscription to a higher tier.

When you have deployed a model, the model is marked with a ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton.svg) icon in the ML experiment. This icon can be clicked to go directly to the ML deployment. You can also access the ML deployment from the catalog.

You can deploy a model from the Models, Data, or Analyze tab. You can choose to deploy a model to a new deployment or an existing deployment.

## Requirements and permissions

To learn more about the user requirements for working with ML deployments and predictions, see [*Who can work with Qlik Predict*](who-can-work-with-automl.htm).

## Deploying a model to a new ML deployment

As you deploy a model, you can create a new deployment, and add the model to that deployment.

### From the Models tab

Do the following:

1. In the Model metrics table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a model.
2. Click ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton.svg) Deploy.

   Information noteAlternatively, click ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton.svg) Deploy model above Model insights.
3. Select the option to deploy the model to A new deployment.
4. Enter a Name and select a Space. Optionally, you can add a description and tags.
5. Optionally, select Enable real-time API access. This option is controlled by your subscription and enables predictions where the apply data is in the API request and the results are in the response.
6. Click Create.

You should now be able to find your ML deployment in the catalog.

### From the Data or Analyze tabs

Do the following:

1. In the toolbar, use the drop down menu to select a model.
2. Click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) .
3. Click ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton.svg) Deploy.
4. Select the option to deploy the model to A new deployment.
5. Enter a Name and select a Space. Optionally, you can edit the description and add tags.
6. Optionally, select Enable real-time API access. This option is controlled by your subscription and enables predictions where the apply data is in the API request and the results are in the response.
7. Click Create.

You should now be able to find your ML deployment in the catalog.

## Deploying a model to an existing deployment

You can also deploy a model to a deployment that already exists. You can deploy models to ML deployments for which you have the required access.

### From the Models tab

Do the following:

1. In the Model metrics table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a model.
2. Click ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton.svg) Deploy.
3. Select the option to deploy the model to An existing deployment.
4. Under Choose deployment, select a deployment using the drop-down menu.
5. Optionally, you can edit the description.
6. Optionally, select Enable real-time API access. This option is controlled by your subscription and enables predictions where the apply data is in the API request and the results are in the response.
7. Click Deploy.

### From the Data or Analyze tabs

Do the following:

1. In the toolbar, use the drop down menu to select a model.
2. Click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) .
3. Click ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton.svg) Deploy.
4. Select the option to deploy the model to An existing deployment.
5. Under Choose deployment, select a deployment using the drop-down menu.
6. Optionally, you can edit the description.
7. Optionally, select Enable real-time API access. This option is controlled by your subscription and enables predictions where the apply data is in the API request and the results are in the response.
8. Click Deploy.

## Removing models from an ML deployment

Over time, you might need to remove models from the deployment.

Do the following:

1. In the ML deployment, open the Deployable models pane.
2. Under All models in the deployment, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the model and select Remove from deployment. In order to be able to remove a model from the deployment, the model needs to be unassigned from all aliases in the deployment.
3. Click Save changes in the top right corner of the interface.

## Viewing deployed model details

In the Deployable models pane, you can view details about a model that has been added to an ML deployment.

Do the following:

1. In the ML deployment, open the Deployable models pane.
2. Under All models in the deployment, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the model and select Show model details.

The model details panel opens on the right, displaying information such as model features, description, and the experiment and training data.

## Editing name and other details of ML deployments

You can change the titles and descriptions of your ML deployments. You can also change the tags used with the ML deployment. Tags are used to group ML deployments with related content. When adding new tags to an ML deployment, users can view all tags that exist in the tenant.

Do the following:

1. Open an ML deployment from the catalog.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) by the deployment name.
3. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit details.
4. Edit the name or other details.

## Sharing ML deployments

You can share an ML deployment by inviting a user, group, or everyone in your tenant to the space where it is stored.

Do the following:

1. In the catalog, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the item to be shared and select Share > Invite.
2. Search for users or groups by name or email address.
3. Select space permissions for the users or groups.
4. Or, select permissions for Anyone at <your tenant name> from the dropdown list.
5. Click Done.

The users receive access to the shared item and all other content in the space.

## Deleting ML deployments

You can delete an ML deployment from the catalog.

## Managing ML deployment jobs

Tenant admins can stop or cancel deployment jobs from the Administration activity center.
For more information, see [*Administering Qlik Predict*](../Admin/mc-managing-experiments-deployments.htm).

## Configuring notifications

You can receive notifications when a model is deployed from an experiment. For more information, see [*Configuring notifications for Qlik Predict*](automl-customize-experience.htm#Configur).
