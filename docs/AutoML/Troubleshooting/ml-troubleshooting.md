---
title: "Troubleshooting - Qlik Predict"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/Troubleshooting/ml-troubleshooting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict"]
---

# Troubleshooting - Qlik Predict

This help topic contains guidance you can use when troubleshooting errors in Qlik Predict.

## Experiment training

### Training error: dataset limit exceeded

You might encounter an error when training an experiment version because the dataset exceeds Qlik Predict guardrails.

Possible cause 1

The training dataset exceeds the maximum cell count or file size for Qlik Predict. In some cases, this may not have been identified before training due to partial [profiling](#glossary-0 "Glossary term").

Maximum sizes for training datasets, by dataset type

| Dataset type | Maximum dataset size | Maximum dataset cell count | Maximum number of included columns |
| --- | --- | --- | --- |
| CSV | 2 GiB | 100 million | 500 |
| Parquet | 2 GiB | 500 million | 500 |
| QVD | 2 GiB | 500 million | 500 |
| Others | 1 GiB | 100 million | 500 |

For more information, see [*Training dataset and profiling limitations*](../ml-limitations-capacities.htm#DatasetSizeCapacities).

Proposed action 1

Consider:

- Dropping features from the experiment to reduce the size.
- Converting the dataset to a different file type.
- Return to dataset preparation and reduce the number of rows in the dataset.

Possible cause 2

The training dataset exceeds the maximum size for your Qlik Cloud subscription. In some cases, this may not have been identified before training, specifically when data profiling estimates row count.

For more information, see [*Training dataset and profiling limitations*](../ml-limitations-capacities.htm#DatasetSizeCapacities).

Proposed action 2

Consider:

- Dropping features from the experiment to reduce the size.
- Return to dataset preparation and reduce the number of rows of the dataset.

Possible cause 3

The training dataset has too many columns. You can have a maximum of 500 columns across the data you have selected to use in training.

This applies both to [training](#glossary-1 "Glossary term") and [apply datasets](#glossary-2 "Glossary term"). For training datasets, the limit is the number of columns used as features in an experiment version. More columns can be in the source dataset. For example, you might have a dataset with 501 columns. The dataset can still be used for training if you drop one feature during experiment configuration.

For more information, see [*General limitations*](../ml-limitations-capacities.htm#General).

Proposed action 3

Deselect any unneeded features until below the limit.

### Training: Certain functionality is not available when configuring experiment

For example, you might notice that the following are not available for your experiment:

- Free text feature engineering
- Bias detection

Possible cause 1

Your dataset is too large for the functionality to be available. The table below outlines the dataset limits for certain capabilities.

Training feature availability by dataset type and size

| Dataset type | Free text feature engineering supported | Time series experiments supported | Bias detection supported |
| --- | --- | --- | --- |
| CSV | Up to 100 million cells or 1 GiB (exceeding either of these limits is not supported) | Up to 1 GiB | Up to 1 GiB |
| Parquet | Up to 100 million cells or 1 GiB (exceeding either of these limits is not supported) | Up to 1 GiB | Up to 1 GiB |
| QVD | Up to 100 million cells or 1 GiB (exceeding either of these limits is not supported) | Up to 1 GiB | Up to 1 GiB |
| Others | Up to 100 million cells or 1 GiB (exceeding either of these limits is not supported) | Up to 1 GiB | Up to 1 GiB |

For more information, see [*Training dataset and profiling limitations*](../ml-limitations-capacities.htm#DatasetSizeCapacities).

Proposed action 1

Reduce the size of your training data. You can try any of the following:

- Dropping features from the experiment to reduce the size.
- Return to dataset preparation and reduce the number of rows of the dataset.

Possible cause 2

Your Qlik Cloud subscription does not include this functionality.

[*Qlik Predict subscription-governed capacities*](../introduction.htm#Subscription)

Proposed action 2

Contact your [tenant administrator](#glossary-3 "Glossary term") or [service account owner](#glossary-4 "Glossary term") to learn about the limits of the subscription.

## Model analysis in experiments

### Some features do not appear when analyzing model in Analyze tab

Possible cause

The column names contain one or more of the following characters:

- [
- ]

Proposed action

To analyze these features in the Analyze tab, you must remove these characters from the column names prior to training. For example, you could replace them with "(" and ")" characters. This can be done either at the data source (for example, Excel), or directly in Qlik Cloud using Qlik scripting and data preparation tools.

### Not all models can be analyzed in Analyze tab

Possible cause

Models that were trained with a sampling ratio of less than 100% cannot be opened in the Analyze tab.

Proposed action

Try analyzing other models. Models trained with less than 100% sampling are mostly intermediate byproducts of intelligent model optimization. Models trained on the full training set are more likely to be deployment-ready than those trained at less than 100% sampling.

For more information about sampling, see [*Intelligent model optimization*](../intelligent-model-optimization.htm).

## Learn more

- [*Qlik Predict limitations and capacities*](../ml-limitations-capacities.htm)
