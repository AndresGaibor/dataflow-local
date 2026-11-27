---
title: "Creating real-time predictions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/creating-real-time-predictions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML predictions"]
---

# Creating real-time predictions

Use your ML deployment to predict future outcomes on new data. You create [real-time predictions](#glossary-0 "Glossary term") using the real-time prediction endpoint in the [Machine Learning API](https://qlik.dev/apis/rest/ml/).

Predictions can be made in real time, such as real-time decisions about customer discounts at checkout. When predictions are generated, you can load the predictive insights into a Qlik Sense application. This lets you visualize and interact with the data and create what-if scenarios.

Information note

The real-time predictions API is deprecated and replaced by the real-time prediction endpoint in the [Machine Learning API](https://qlik.dev/apis/rest/ml/). The functionality itself is not being deprecated. For future real-time predictions, use the real-time prediction endpoint in the Machine Learning API. For help with migrating from the real-time predictions API to the Machine Learning API, refer to [the migration guide on the Qlik Cloud developer portal](https://qlik.dev/apis/rest/automl-deployments/#migrate-from-the-automl-real-time-predictions-api-to-the-machine-learning-api).

## Creating real-time predictions with the API

The Real-time predictions pane in the ML deployment interface gives you access to the real-time prediction endpoint in the Machine Learning API. This pane is visible if the default model in the deployment is activated and you have the required permissions for real-time predictions.

The real-time prediction endpoint s a two-way communication between Qlik Predict and other capabilities in Qlik Cloud, including Qlik Sense and Automations, as well as external applications. You can use the endpoint to programmatically make predictions by passing data to a model and retrieve the prediction results in real time.

Real-time predictions pane

![Real time predictions pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml_realtime-predictions.png "Click to view full size")

Do the following:

1. Open the Real-time predictions pane in an ML deployment.
2. Use the copy buttons to copy the applicable URL or JSON to your clipboard (for information about selecting which alias to use, see [*Working with model aliases in real-time predictions*](#AliasPredictions)).
3. Incorporate calls to the Machine Learning API into your own applications, or manually call the API using your desired tool.

   For real-time endpoint specifications for the Machine Learning API, see [Generate predictions in a synchronous request/response](https://qlik.dev/apis/rest/ml/#post-v1-ml-deployments-deploymentId-realtime-predictions-actions-run).

For more general information about the Machine Learning API, see [Machine Learning API](https://qlik.dev/apis/rest/ml/).

## Requirements for real-time predictions

- An API key is required to use the real-time prediction endpoint. Users must have the Manage API keys permission in the tenant to generate an API key. See [*Generating and managing API keys*](../Admin/mc-generate-api-keys.htm#Generating).
- The source model for the ML deployment you are using must be activated for making predictions. For more information, see:

  - [*Approving deployed models*](approve-models.htm)
  - [*Working with model approval as an administrator*](../Admin/mc-approve-models-admin.htm)
- You need the correct permissions for working with ML deployments and predictions. For more information, see [*Requirements and permissions*](working-with-predictions.htm#Requirements).

## Working with model aliases in real-time predictions

You can add multiple models to an ML deployment. A system of [aliases](#glossary-1 "Glossary term") is used in ML deployments to allow for dynamic swapping of models for use in predictions. For more information, see [*Using multiple models in your ML deployment*](ml-deployment-available-models.htm).

When you copy your URL or JSON, the following options are available:

- Default prediction: Use this option to generate predictions from the default alias in the ML deployment.
- Alias prediction: Use this option when you want to generate predictions from any additional aliases you have added to the ML deployment. Select an alias using the drop down menu, and then copy the URL or JSON.

## Viewing data drift and prediction event details

After you run a real-time prediction, open the ML deployment and explore the Operations monitoring and Data drift monitoring panes. In these views, you can evaluate:

- The level of data drift for each feature involved in the prediction. The comparison is performed between the data you send to the Qlik Predict real-time prediction API and the training dataset.
- Details about the prediction event, such as whether it succeeded or failed, and how many predictions it generated.

For more information, see:

- [*Monitoring deployed model operations*](monitor-model-operations.htm)
- [*Monitoring data drift in deployed models*](monitor-drift.htm)
