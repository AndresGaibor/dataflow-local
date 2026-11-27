---
title: "Automatic feature engineering"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/automatic-feature-engineering.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Configuring experiments", "Automatic data preparation and transformation"]
---

# Automatic feature engineering

With automatic feature engineering, Qlik Predict can use existing features in your training data to create new features. These new auto-engineered features allow you to discover new patterns in your data, and can greatly improve the performance of your machine learning models. Qlik Predict supports date feature engineering and free text feature engineering.

## Background

Feature engineering is the process of creating new feature columns from current ones. Qlik Predict can perform feature engineering automatically for improved handling of certain types of data. For general information about feature engineering, see [*Creating new feature columns*](feature-engineering.htm).

## Identifying when automatic feature engineering is possible

After you select a dataset for use in your experiment, the dataset is analyzed and the columns within it are identified as containing certain data types. These data types allow Qlik Predict to assign a feature type to each column in the dataset. Each column is given one of the following feature types:

- Categorical
- Numeric
- Date
- Free text

When possible, Qlik Predict displays a list of auto-engineered features that can be created from eligible parent features. This list of auto-engineered features is further refined and reduced as preprocessing begins. Including auto-engineered features in your experiment is recommended but optional. You can remove individual auto-engineered features before you start training, and when configuring each new experiment version.

For more information about the processes completed before experiment training begins, see [*Automatic data preparation and transformation*](preprocessing-steps.htm).

## Date feature engineering

When date and datetime columns are detected in your training data, new date features can automatically be created from these columns. For more information, see [*Date feature engineering*](date-feature-engineering.htm).

## Free text handling

Special handling of free text data is supported when training models. For more information, see [*Handling of free text data*](free-text-handling.htm).

## Learn more

- [*Automatic data preparation and transformation*](preprocessing-steps.htm)
- [*Configuring experiments*](configuring-experiments.htm)
