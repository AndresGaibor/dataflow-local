---
title: "Working with free text features in predictions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/free-text-features-predictions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML predictions"]
---

# Working with free text features in predictions

This help topic outlines the requirements for running predictions using an ML deployment that was trained with free text features.

## Requirements

When you deploy a model trained with a free text feature, the resulting ML deployment can generate predictions as long as the following requirements are met for the apply dataset:

- The column names of the feature match between the training dataset and the apply dataset
- The column in the apply dataset, which corresponds to the free text feature in the training data, contains string data

Warning noteAs long as the requirements above are met, the prediction will run successfully. In other words, the prediction will run successfully even if the corresponding column in the apply dataset does not actually contain free text. A prediction generated in this situation is not considered reliable. Always ensure that the equivalent column in your apply dataset, which corresponds to a free text feature in your training data, contains free text.

## Learn more

- [*Automatic feature engineering*](automatic-feature-engineering.htm)
- [*Handling of free text data*](free-text-handling.htm)
