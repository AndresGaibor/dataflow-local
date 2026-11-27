---
title: "Anomaly detection and handling"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/anomaly-detection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Configuring experiments", "Working with model optimization", "Intelligent model optimization"]
---

# Anomaly detection and handling

Anomaly detection and handling are provided when using [intelligent model optimization](#glossary-0 "Glossary term"). With these capabilities, Qlik Predict can handle outlier values in your training data automatically with specific processing. During training, outlier data from your training data is not entirely removed, but is instead processed using an algorithm-powered weighting system.

It is common to observe outlier values, or anomalies, in almost every kind of data you can work with. Anomalies are data values that occur outside of the conventionally expected range you might expect. When training machine learning models, a certain proportion of anomalies can be tolerated and might even be desirable as a reflection of real-world deviation. However, in extreme cases, anomalies and outlier values introduce bias into a model, reducing its reliability and usefulness.

## Examples

Not all anomalies should be treated equally, and should not always be viewed as things to remove from your data. For example, if a data anomaly is a naturally possible but infrequent occurrence that can be observed when collecting data, it might make sense that you want this to be used in the models you train. A great example of this is instances of fraud in financial transactions. Over millions of transactions, only a handful might be related to fraud. Depending on the problem you want to analyze and address with your model, the probability of fraud in everyday transactions might be something you would like to account for when generating predictions.

An example of an anomaly that you would likely want to remove is an unintentional failure that occurs when you are collecting data. For example, let's say you are building a model that will be used to predict weather patterns. Your model is being trained on data from a sensor that monitors weather metrics, and an unrelated power outage results in faulty data being collected from the sensor. This faulty data might be considered anomaly data that you would want to remove before finishing the model training.

## How does Qlik Predict handle anomalies?

Anomaly detection and handling are performed when you train models with intelligent model optimization, which is turned on by default in new experiments.

Handling of anomalies can generally be considered to occur in two separate processes: detection and actual model training.

### Anomaly detection

When you run a version of the training, Qlik Predict completes several steps before model training begins. This includes data classification, null imputation, and a number of other processes. Anomaly detection is completed during this stage, and only when intelligent model optimization is turned on.

In technical terms, Qlik Predict uses a decision tree-based algorithm, the isolation forest algorithm, to detect anomalies and outlier values in your training data. During the data processing stage in intelligent model optimization, each data point in the dataset (generally known as a record) is assigned an anomaly score and is weighted based on the degree of certainty that it is an anomaly.

### Anomaly handling in model training

After your data is processed and transformed as needed, Qlik Predict begins training models. During this process, the weighted anomaly scores generated earlier are used to adjust the influence each row has on the model. For example, a row considered highly likely to contain an anomaly is assigned a lower influence on the model training.

This weighted scoring system allows Qlik Predict to avoid discarding data, and instead simply reduce the impact that outlier data has on the model.

## Considerations

Despite the anomaly detection capabilities that are available with Qlik Predict, this does not mean any data can be used to train a high-quality model. If your data contains uncharacteristically large proportions of faulty or corrupted information, anomaly detection cannot remedy all these issues.

In these scenarios, it is recommended that you return to the data collection process to make sure you have the most high-quality and realistic data available to you. This will help you optimize your machine learning model reliability and success.
