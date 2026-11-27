---
title: "Monitoring performance and usage of deployed models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/monitor-models.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML deployments"]
---

# Monitoring performance and usage of deployed models

As you use your ML deployment to generate predictions, you can monitor the performance of the source model by analyzing data drift over time. You can also view details about usage of the deployment for predictions, such as how predictions have been triggered and the rate of prediction failure.

Monitoring of deployed models and ML deployments is performed with embedded analytics.

## Data drift monitoring

With data drift monitoring, you can analyze how the input data for model predictions has changed over time, and how it differs from the original training dataset. With these tools, you can determine the point at which your model needs to be re-trained or replaced due to significant feature drift.

For more information about data drift monitoring in Qlik Predict, see [*Monitoring data drift in deployed models*](monitor-drift.htm).

For general information about data drift, see [*Data drift*](data-drift.htm).

## Operations monitoring

As your ML deployment is used to create predictions, it is helpful to monitor details about its operations. With operations monitoring in Qlik Predict, you can:

- View the number of requests, predictions, prediction failures for the deployment.
- Analyze prediction events by trigger (for example, how many were initially manually versus on a schedule).
- View a detailed log showing each prediction event along with key details.

For more information, see [*Monitoring deployed model operations*](monitor-model-operations.htm).
