---
title: "Generating SHAP datasets during predictions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/prediction-shap.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML predictions"]
---

# Generating SHAP datasets during predictions

SHAP importance datasets can be generated when you run a prediction. You can use the SHAP calculations in these datasets to understand which features are the most important contributors to the predicted values.

SHAP datasets contain the row-level SHAP calculations for the features used to train the model. These values represent how much each feature contributes to the predicted value of the target, given all the other features of that row.

For example, SHAP importance can tell us if a feature makes a customer more or less likely to churn and how strongly it influences that outcome.

When you have run your prediction and generated the datasets, you can load the SHAP values into a Qlik Sense application and visualize them alongside the predicted values. For further details, see [*Visualizing SHAP values in Qlik Sense applications*](shap-values.htm) and [*Using SHAP values in real-world applications*](shap-applications.htm)

This help topic focuses on SHAP dataset generation during predictions by ML deployments. For information about SHAP importance charts shown during experiment training, see [*Understanding SHAP importance in experiment training*](shap-importance.htm).

Information noteSHAP datasets cannot be generated during predictions with time series models.

## Available options for generating SHAP datasets

When configuring a prediction, you can choose to generate SHAP datasets in two different formats. Both options provide the same information, but it is structured in different ways.

### SHAP

This is a dataset in which the SHAP values are separated into one column for each feature. This option is not available for multiclass classification models.

### Coordinate SHAP

This is a dataset in which all SHAP values are structured to be contained within only two columns: a 'feature' column and a 'value' column. This option is available for all model types.

Datasets from multiclass models work slightly differently compared to datasets from binary models. For each record to predict, a new row is created with the SHAP value for each possible class available to predict by the model. In the dataset, an additional column is also created to identify the class that the SHAP value represents.

When loading predictions and SHAP values into a Qlik Sense application and creating a data model, coordinate SHAP datasets can be easier to work with than SHAP datasets.

### Examples

The following tables contain samples from SHAP and coordinate SHAP datasets, which were generated from a regression model trained on five features. The samples contain SHAP values for two records from the [apply dataset](#glossary-1 "Glossary term") (corresponding to two account IDs).

These examples highlight the difference between how the data is structured.

SHAP dataset sample

| AccountID | AdditionalFeatureSpend\_SHAP | Churned\_SHAP | CurrentPeriodUsage\_SHAP | HasRenewed\_SHAP | NumberOfPenalties\_SHAP |
| --- | --- | --- | --- | --- | --- |
| aa16889 | 1.76830971241 | -0.58154511451721 | -1.106874704361 | -0.36080026626587 | 3.6597540378571 |
| aa33396 | 0.80359643697739 | -0.64805734157562 | 0.076582334935665 | 0.38967734575272 | -0.31007811427116 |

Coordinate SHAP dataset sample

| AccountID | automl\_feature | SHAP\_value |
| --- | --- | --- |
| aa16889 | AdditionalFeatureSpend | 1.76830971241 |
| aa16889 | Churned | -0.58154511451721 |
| aa16889 | CurrentPeriodUsage | -1.106874704361 |
| aa16889 | HasRenewed | -0.36080026626587 |
| aa16889 | NumberOfPenalties | 3.6597540378571 |
| aa33396 | AdditionalFeatureSpend | 0.80359643697739 |
| aa33396 | Churned | -0.64805734157562 |
| aa33396 | CurrentPeriodUsage | 0.076582334935665 |
| aa33396 | HasRenewed | 0.38967734575272 |
| aa33396 | NumberOfPenalties | -0.31007811427116 |

## Interpreting SHAP prediction values

Unlike the values in the SHAP importance chart that is shown during experiment training, SHAP datasets contain row-level SHAP calculations that have directionality. In other words, they are not absolute values, but can instead be positive or negative. When visualizing the values in an application, you can choose to aggregate them as absolute values, depending on your use case.

The SHAP value for a record should be analyzed with respect to the corresponding predicted value for that record. Depending on the model type (binary classification, multiclass classification, or regression), the directionality of the SHAP values should be interpreted slightly differently.

### Classification models

With binary classification models, large positive SHAP values indicate larger influence towards one of the two possible outcomes, and highly negative values indicate larger influence towards the other outcome. When using the data in an application, the directionality of the SHAP values might not allow the analysis you need. To solve this, you can reverse the direction of the SHAP values (for example, multiply the entire column by -1). For more information about the SHAP direction check, see [*Preparations*](shap-values.htm#Preparat).

A SHAP dataset from a multiclass model is structured differently. For each record to predict, it includes a separate row for each possible class, along with a corresponding SHAP value for that class. The class is specified in a 'Predicted\_class' column.

In your coordinate SHAP dataset, interpret the SHAP values from multiclass model predictions as follows:

- A high positive SHAP value indicates that the feature is having larger influence towards the outcome being the specified 'Predicted\_class'.
- A high negative SHAP value indicates that the feature is having larger influence towards the outcome not being the specified 'Predicted\_class'.

#### Example

The following example demonstrates the difference in the dataset structure between binary and multiclass classification model output.

Let's say we start with an [apply dataset](#glossary-2 "Glossary term") that contains one row per account ID. Each feature on which the model is trained is represented as a separate column.

A single account ID record would look like this:

Single record from a dataset on which predictions will be generated

| AccountID | AdditionalFeatureSpend | BaseFee | CurrentPeriodUsage | HasRenewed | NumberOfPenalties |
| --- | --- | --- | --- | --- | --- |
| aa16889 | 18 | 33.52 | 210.1 | yes | 4 |

If we train a binary classification model to predict the outcome of a Churned field, there will be two possible outcomes: 'yes' or 'no'. Based on the single account ID record above, the coordinate SHAP dataset for this record would look like this:

Sample from coordinate SHAP dataset for binary classification model prediction

| AccountID | automl\_feature | SHAP\_value |
| --- | --- | --- |
| aa16889 | AdditionalFeatureSpend | -0.049129267835076 |
| aa16889 | BaseFee | -1.5363064624041 |
| aa16889 | CurrentPeriodUsage | 0.10787960191299 |
| aa16889 | HasRenewed | 1.2441783315923 |
| aa16889 | NumberOfPenalties | 2.3803616183224 |

In the above table, the SHAP values for a single account ID are displayed, and they are broken down by feature. A new row is created for each feature, and each feature is assigned a SHAP value. The direction and magnitude of these SHAP values must be assessed in relation to the two possible outcomes. Ideally, the higher the SHAP value, the larger the influence the feature has the outcome with a positive interpretation (in this case, 'yes'). If this representation is instead reversed, you can reverse the direction of the SHAP values (multiply them by -1) to make the analysis more easily interpretable.

For comparison, let's say we train a multiclass classification model to predict a categorical PlanType field (with four possible outcomes - 'Blue Plan', 'Green Plan', 'Purple Plan', and 'Red Plan'). Based on the single account ID record in the first table, the coordinate SHAP dataset for this record would look like this:

Sample from coordinate SHAP dataset for multiclass classification model prediction

| AccountID | automl\_feature | Predicted\_class | SHAP\_value |
| --- | --- | --- | --- |
| aa16889 | AdditionalFeatureSpend | Blue Plan | 0.004155414339679 |
| aa16889 | AdditionalFeatureSpend | Green Plan | 0.0066376343942741 |
| aa16889 | AdditionalFeatureSpend | Purple Plan | -0.014411468558894 |
| aa16889 | AdditionalFeatureSpend | Red Plan | 0.003618419824941 |
| aa16889 | BaseFee | Blue Plan | 0.089301017079318 |
| aa16889 | BaseFee | Green Plan | 0.28876498452748 |
| aa16889 | BaseFee | Purple Plan | 0.055689421438434 |
| aa16889 | BaseFee | Red Plan | -0.43375542304524 |
| aa16889 | CurrentPeriodUsage | Blue Plan | -0.0040098954629816 |
| aa16889 | CurrentPeriodUsage | Green Plan | -0.27902537442842 |
| aa16889 | CurrentPeriodUsage | Purple Plan | -0.21871561841248 |
| aa16889 | CurrentPeriodUsage | Red Plan | 0.50175088830388 |
| aa16889 | HasRenewed | Blue Plan | -0.011878031228962 |
| aa16889 | HasRenewed | Green Plan | 0.036835618725654 |
| aa16889 | HasRenewed | Purple Plan | 0.13798314881109 |
| aa16889 | HasRenewed | Red Plan | -0.16294073630778 |
| aa16889 | NumberOfPenalties | Blue Plan | 0.20519095034486 |
| aa16889 | NumberOfPenalties | Green Plan | 0.0015682625647107 |
| aa16889 | NumberOfPenalties | Purple Plan | -0.084355421853302 |
| aa16889 | NumberOfPenalties | Red Plan | -0.12240379105627 |

In the table above, a single account ID is represented with 20 separate rows: one row for each feature, with a row for the SHAP value corresponding to each possible outcome in the target. The Predicted\_class column represents the possible outcome (class) to predict, not necessarily the actual predicted outcome displayed in the prediction dataset. Ultimately, the class with the highest SHAP value becomes the predicted value for the record.

The SHAP values in this table are measurements of the influence that the specified feature (automl\_feature) is having on the outcome possibly being the specified class (Predicted\_class). A large positive value indicates the feature is strongly influencing the predicted outcome to be the specifed class, while a large negative value indicates the feature is strongly influencing the predicted outcome to not be the specified class.

### Regression models

In a SHAP dataset generated from a regression model, the direction of the SHAP values is more straightforward to interpret.

- A positive SHAP value corresponds to an increase in the predicted value for the row.
- A negative SHAP value corresponds to a decrease in the predicted value for the row.

## Calculation of SHAP values

SHAP values are calculated for a variety of algorithms.
SHAP importance is calculated using two distinct methods:

- Tree SHAP: A fast and exact method to estimate SHAP values for tree models
- Linear SHAP: A method to compute SHAP values for linear models

Available algorithms by model types and SHAP calculation method

| Algorithm | Supported model types | SHAP calculation method |
| --- | --- | --- |
| Random Forest Classification | Binary classification, multiclass classification | Tree SHAP |
| XGBoost Classification | Binary classification, multiclass classification | Tree SHAP |
| LightGBM Classification | Binary classification, multiclass classification | Tree SHAP |
| CatBoost Classification | Binary classification, multiclass classification | Tree SHAP |
| Logistic Regression | Binary classification, multiclass classification | Linear SHAP |
| Lasso Regression | Binary classification, multiclass classification | Linear SHAP |
| Elastic Net Regression | Binary classification, multiclass classification | Linear SHAP |
| Gaussian Naive Bayes | Binary classification, multiclass classification | SHAP not calculated |
| CatBoost Regression | Regression | Tree SHAP |
| LightGBM Regression | Regression | Tree SHAP |
| Linear Regression | Regression | Linear SHAP |
| Random Forest Regression | Regression | Tree SHAP |
| SGD Regression | Regression | Linear SHAP |
| XGBoost Regression | Regression | Tree SHAP |
