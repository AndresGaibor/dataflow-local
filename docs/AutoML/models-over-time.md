---
title: "Evaluating model performance over time"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/models-over-time.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning"]
---

# Evaluating model performance over time

After you have trained a number of machine learning models and deployed the best one, you will start creating predictions on production data. It is important to continually evaluate your model's performance to ensure it is still generating reliable predictions, and that the data on which it was trained is still relevant.

## Factors that are important to monitor

### Operational needs

Your predictive use case is likely to change over time. Changes can be minor or significant. You will need to assess whether your model still provides value with its current configuration. If your machine learning question has changed substantially since you first trained your models, it is recommended you re-start the process of defining your question and dataset.

### Input data and prediction accuracy

It is common for distributions and trends in input data to change over time. What was once a defining quality of your training data might no longer be relevant, or might be even more pronounced in impact. You might discover that there are new variables affecting predicted outcomes that need to be introduced into your model as new features. Along the same lines, certain features might no longer be contributing substantially enough to outcomes to be included in the model.

It is important to monitor your data for the amount of drift between your initial training data and the latest available data. If the drift for certain features starts to reach a threshold that is no longer acceptable, it is time to collect new data and re-train your model, or start with a new definition of your machine learning problem. For additional details about data drift, see [*Data drift*](data-drift.htm).

Also, if you notice that the model is no longer predicting with the accuracy at which it did initially, you need to re-assess what you need to change to return it to acceptable performance. For example, you might find that model accuracy is being impacted by errors that are happening during data collection process.

## Re-training models

As more historical data becomes available, and regardless of whether your performance has declined, it is inevitable that you will need to re-train your models to reflect the most up-to-date information.

## Monitoring data drift

Qlik Predict has built-in functionality available to help you detect feature drift for your deployed models. For more information, see [*Monitoring data drift in deployed models*](monitor-drift.htm).

## Next steps

Depending on how substantially your use case and the input data has changed, you might want to consider one or more of the following:

- Re-train models within the same experiment, with new data. If your machine learning problem has not changed substantially, this option offers several benefits. In particular, you can compare models from all experiment versions in detail within the same experiment. For more information, see [*Changing and refreshing the dataset*](refining-models.htm#Changing).
- If the original machine learning problem you initially defined is no longer relevant, it might make sense to create a new experiment altogether. This depends largely on your use case.
