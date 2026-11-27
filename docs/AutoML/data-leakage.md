---
title: "Data leakage"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/data-leakage.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning", "Getting your dataset ready for training"]
---

# Data leakage

Data leakage means that the data used to train a machine learning algorithm includes the information you are trying to predict. This could lead to the model performing better in training than it would in the real world, creating a false assurance of how well the model performs. Learn how to identify and prevent data leakage to get reliable predictions.

Generally speaking, data leakage is caused by at least one of the following:

- When one or more features in the training set can be used to derive the target variable you are trying to predict. For example, your target is a Sales field and one of your features is a Sales Tax field that is calculated from Sales.
- When one or more features in the training set includes information that would not be known at the time of prediction.

In the following table, the column Stage is a duplicate column of the column Stage (Binary) that we want to predict. By including Stage in the training dataset, we would be providing the answer to the anticipated result, leading to a high score for our model.

Table with the "leaky column" Stage that contains information about the target column Stage (Binary)

| Total Employees | Annual Revenue (M$) | Lead Source | Forecast Deal ($) | Stage | Stage (Binary) |
| --- | --- | --- | --- | --- | --- |
| 12078 | 2705 | Partner | 369,000 | 6 - Closed/Lost | LOST |
| 10076 | 1783 | Inside sales | 71,000 | 6 - Closed/Won | WON |
| 8518 | 2114 | Inside sales | 294,000 | 6 - Closed/Lost | LOST |
| 3978 | 1159 | Sales rep | 214,000 | 6 - Closed/Won | WON |
| 3517 | 2285 | Marketing promo | 154,000 | 6 - Closed/Lost | LOST |
| 3370 | 97 | Customer referral | 41,000 | 6 - Closed/Won | WON |

## Target leakage

Target leakage is a form of data leakage. Target leakage occurs when feature data references target data that could be used for predictions. The references, or "leakages", can be direct or indirect.

With intelligent model optimization, Qlik Predict identifies target leakage and prevents it from being introduced into your models. Features indicating target leakage are automatically detected and removed from model training. For more information about intelligent model optimization, see [*Intelligent model optimization*](intelligent-model-optimization.htm).

## Identifying data leakage

To identify data leakage, consider questions like "Will you have the same information for records at the time you want to make a prediction?" or "Will the record be the same in 30 days?". Remember that all data in your training dataset must be relevant to the time constraint in your business question.

When you have trained a model, you can look for the following clues in the model metrics.

- High scores: Is the score really high? For example, is the F1 score above 85?
- Feature importance: Is one feature a lot more important than everything else?
- Holdout score: Is the holdout score much lower than the cross-validation score?

The table shows examples of common features that might cause data leakage.

| Business use case | Target | Potentially leaky features |
| --- | --- | --- |
| Will a sales opportunity close? | Close (Yes or No) | Stage, close date, invoice details, commissions paid |
| Predict a future transaction amount | Amount of the next transaction | Taxes, order details |
| Will a lead convert to an opportunity? | Convert (Yes or No) | Opportunity details, conversion date |
| Will a customer churn? | Churn (Yes or No) | Churn reason, churn date, static customer tenure, customer temperature |
| Will an employee voluntarily term? | Terminate (Yes or No) | Exit interview details, term date, resignation letter information |

## Preventing data leakage

The best way to prevent data leakage is to use the structured framework to get a good business question and dataset. For more information, see [*Defining machine learning questions*](machine-learning-framework.htm).

Tip noteIf you have identified a leaky column that should not be used in the model training, you can still keep it in the dataset. Just exclude this feature from the training data in your machine learning experiment.
