---
title: "Deploying and approving your model"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/tutorial-deploying-model.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Tutorial – Generating and visualizing prediction data"]
---

# Deploying and approving your model

The next step is to deploy your model, and then approve it so that it can generate predictions.

## Deploying a model

Deploying a model allows you to use it to generate predictions on new data.

The model refinement process is different for each project you work on. Once you have a model that meets the criteria for your use case, you can deploy it. This will create an ML deployment, which is available in the catalog.

For more information about deploying your models in Qlik Predict, see [*Working with ML deployments*](working-with-deployments.htm).

Information noteQlik Predict is continually improving its model training processes. Your model metrics, as well as the algorithm for the model which you will deploy, might not be identical to those shown in the images on this page.

Do the following:

1. Switch back to the Models tab in the experiment.
2. Click the ![Trophy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_trophy.svg) Best model card above the model metrics table to select the best overall model.
3. Click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the model that has a ![Trophy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_trophy.svg) icon next to it.
4. Click ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton.svg) Deploy.

   Information noteAlternatively, click ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton.svg) Deploy model above Model insights.
5. Select the option to deploy the model to A new deployment.
6. Type a name for your deployment, such as Customer churn deployment.
7. If needed, adjust the space, description, and tags.
8. Click Deploy.

Deploying a model in Qlik Predict

![Selecting the 'Deploy' option for the chosen model.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-tutorial-model-deploy.png "Click to view full size")

Your new ML deployment will now be available in the catalog.

Click Open, or navigate back to the catalog and open the ML deployment.

## Approving your model

At the top of the ML deployment interface, a banner indicates that a model approver needs to activate the default model for making predictions.

Do the following:

1. In the banner at the top of the ML deployment, click Activate model.
2. In the dialog that opens, click Activate model to confirm.

Approving a deployed model in an ML deployment

![Activating the ML model that you deployed to the ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-tutorial_approve-model.png "Click to view full size")

For more information about approving models, see [*Approving deployed models*](approve-models.htm).

You can now proceed to creating predictions with your ML deployment. Move to the next topic in this tutorial.
