---
title: "Qlik Predict limitations and capacities"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/ml-limitations-capacities.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict"]
---

# Qlik Predict limitations and capacities

This page lists general limitations and capacities for Qlik Predict functionality. For capacities that are specific to individual Qlik Cloud subscriptions, refer to [Qlik Pricing](https://www.qlik.com/us/pricing) and [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) or contact your Qlik account representative.

## General limitations

- Qlik Predict has an API rate limit of 300 requests per minute.
- Maximum number of columns in the dataset: 500

  This applies both to [training](#glossary-0 "Glossary term") and [apply datasets](#glossary-1 "Glossary term"). For training datasets, the limit is the number of columns used as features in an experiment version. More columns can be in the source dataset. For example, you might have a dataset with 501 columns. The dataset can still be used for training if you drop one feature during experiment configuration.
- Any flat file that can be uploaded and profiled in Qlik Cloud is supported for use in Qlik Predict.

  For multi-table files such as Microsoft Excel files with multiple sheets, only the first table will be imported. If data profiling fails for a table (for example, if it is empty), the file is not supported.

## Training dataset and profiling limitations

This section lists guardrails enforced on training dataset sizes in Qlik Predict.

Note the following:

- The limitations apply only to the data included in the experiment version: all included features, including the target column.
- The limitations apply either to general [data profiling](#glossary-2 "Glossary term") across the Qlik Cloud platform, or are specific to Qlik Predict.
- The limitations are maximum capacities. The limits of your Qlik Cloud subscription may be lower.

### Dataset size limits for training

These limits are technical capacities for the size, cell count, and number of included columns in training datasets.

Maximum sizes for training datasets, by dataset type

| Dataset type | Maximum dataset size | Maximum dataset cell count | Maximum number of included columns |
| --- | --- | --- | --- |
| CSV | 2 GiB | 100 million | 500 |
| Parquet | 2 GiB | 500 million | 500 |
| QVD | 2 GiB | 500 million | 500 |
| Others | 1 GiB | 100 million | 500 |

In addition, certain training functionality is only available for datasets under specific sizes and cell counts.

Training feature availability by dataset type and size

| Dataset type | Free text feature engineering supported | Time series experiments supported | Bias detection supported |
| --- | --- | --- | --- |
| CSV | Up to 100 million cells or 1 GiB (exceeding either of these limits is not supported) | Up to 1 GiB | Up to 1 GiB |
| Parquet | Up to 100 million cells or 1 GiB (exceeding either of these limits is not supported) | Up to 1 GiB | Up to 1 GiB |
| QVD | Up to 100 million cells or 1 GiB (exceeding either of these limits is not supported) | Up to 1 GiB | Up to 1 GiB |
| Others | Up to 100 million cells or 1 GiB (exceeding either of these limits is not supported) | Up to 1 GiB | Up to 1 GiB |

### Profiling limitations

When you add a training dataset to an experiment, it is analyzed by Qlik Cloud data profiling to estimate various statistics (such as cell count and distinct value count). After running an experiment version, Qlik Predict preprocessing is performed, which sometimes results in changes to certain statistics.

For large datasets—those exceeding 1 GiB—the data is partially profiled. This can cause some estimated statistics—for example, row, cell, distinct value, and null counts—to change after running the training.

As a result, with some large datasets, you could experience the following training errors:

- Training fails due to a dataset exceeding the cell count permitted by the subscription, even though no errors were present upon profiling.
- Training fails because the null count exceeds the maximum permitted threshold, even though no errors were present upon profiling.
- The estimated experiment type is found to be incompatible with the training dataset, even though no errors were present upon profiling.

For troubleshooting steps you can follow to reduce your dataset size, see [*Troubleshooting - Qlik Predict*](Troubleshooting/ml-troubleshooting.htm).

## Learn more

- [*Troubleshooting - Qlik Predict*](Troubleshooting/ml-troubleshooting.htm)
