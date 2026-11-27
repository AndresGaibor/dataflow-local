---
title: "Navigating the ML deployment interface"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/ml-model-management.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML deployments"]
---

# Navigating the ML deployment interface

When you open your ML deployment, you can perform management and monitoring activities, and use it to create predictions on datasets.

Open an ML deployment from the catalog. There are navigation options for the following:

- [*Deployment overview*](#Overview)
- [*Deployable models*](#Deployable)
- [*Batch predictions*](#Batch)
- [*Real-time predictions*](#RealTime)
- [*Operations monitoring*](#Operations)
- [*Data drift monitoring*](#Drift)

## Deployment overview

The Deployment overview shows the features used in the model training and details for the deployment.

Overview of the ML deployment

![Model overview pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-automl-manage-model_depl-overview.png "Click to view full size")

If the default model in the deployment is inactive, you are notified in a banner at the top of the screen. If you have the correct permissions, you can activate the model by clicking Activate model. For more information, see:

- [*Approving deployed models*](approve-models.htm)
- [*Working with model approval as an administrator*](../Admin/mc-approve-models-admin.htm)

## Deployable models

The Deployable models pane is where you can manage [model aliases](#glossary-0 "Glossary term") and configure which models are used for predictions.

For more information, see [*Using multiple models in your ML deployment*](ml-deployment-available-models.htm).

Deployable models pane in Qlik Predict

!['Deployable models' pane in [[[Undefined variable CommonComponents.AutoML]]] ML deployment interface](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-automl_available-models.png "Click to view full size")

## Batch predictions

In Batch predictions, you can manage and run [batch predictions](#glossary-1 "Glossary term") using the ML deployment. Click Create prediction to create a prediction configuration, from which you run batch predictions. You can have several prediction configurations for an ML deployment.

You can use the Actions menu ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the table to:

- View and edit details for prediction configurations
- Run predictions from existing configurations
- Edit and delete configurations
- Create, edit, and delete prediction schedules for an existing configuration

Batch predictions with an overview and Actions menu expanded

![Dataset predictions pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-automl-manage-model_batch-predictions.png "Click to view full size")

If you select Edit prediction configuration, the Prediction configuration pane is opened. You can compare the model and apply dataset schema side-by-side as you edit the prediction.

If your deployment contains a time series model, you can also view important details about your defined time series problem, such as the forecast window, time step, and apply window.

Batch predictions with side pane for prediction configuration

![Prediction configuration menu and dataset schemas when creating predictions.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-tutorial_batch-prediction.png "Click to view full size")

## Real-time predictions

The Real-time predictions pane gives you access to the real-time prediction endpoint in the Machine Learning API. If the default model in the ML deployment is activated for making predictions, this pane is visible.

For information about creating real-time predictions, see [*Creating real-time predictions*](creating-real-time-predictions.htm).

Information note

The real-time predictions API is deprecated and replaced by the real-time prediction endpoint in the [Machine Learning API](https://qlik.dev/apis/rest/ml/). The functionality itself is not being deprecated. For future real-time predictions, use the real-time prediction endpoint in the Machine Learning API. For help with migrating from the real-time predictions API to the Machine Learning API, refer to [the migration guide on the Qlik Cloud developer portal](https://qlik.dev/apis/rest/automl-deployments/#migrate-from-the-automl-real-time-predictions-api-to-the-machine-learning-api).

Real-time predictions pane

![Real time predictions pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml_realtime-predictions.png "Click to view full size")

## Operations monitoring

In Operations monitoring, you can monitor usage information for the ML deployment. You can view details about how the ML deployment is being used, such as how many prediction events succeed or fail, and how prediction events are typically triggered.

For more information, see [*Monitoring deployed model operations*](monitor-model-operations.htm).

Operations monitoring pane in ML deployment

![Embedded analysis showing operations analysis for an ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-ops-monitoring.png "Click to view full size")

## Data drift monitoring

In Data drift monitoring, you can monitor data drift for the ML deployment.

With data drift monitoring, you can assess changes in the distribution of features in the source model. When significant drift is observed, it is recommended that you retrain or re-configure your model to account for the latest data, which may indicate new patterns in data trends.

For more information, see [*Monitoring data drift in deployed models*](monitor-drift.htm).

Data drift monitoring pane in ML deployment

![Embedded analysis data drift analysis for an ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-data-drift-monitor.png "Click to view full size")
