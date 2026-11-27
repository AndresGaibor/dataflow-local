---
title: "Detecting bias in machine learning models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/bias-detection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Reviewing models", "Analyzing models"]
---

# Detecting bias in machine learning models

You can identify bias in machine learning models you train in ML experiments. Also, you can optionally choose to get recommendations from a large language model (LLM) for features that might be susceptible to bias. Address detected bias by dropping skewed features, correcting improper data collection, or changing the structure of your training dataset.

Warning note

Qlik does not guarantee the accuracy, completeness, or reliability of any bias detection results and does not ensure compliance with any local, state, federal, or international laws, regulations, or industry standards. The user assumes all risk and responsibility for any actions taken based on the tool's output, which should not be used as a substitute for professional legal advice or independent human auditing.

Warning note

Bias detection has an optional component that uses generative artificial intelligence (“GenAI”) to recommend features that might be susceptible to bias. It is the user’s responsibility to review and verify any GenAI recommendations, and to evaluate whether its use is appropriate for any particular use case and whether it complies with applicable laws.

## Understanding bias

In machine learning, bias is an undesired phenomenon in which models favor, or could favor, certain groups over others. Bias negatively affects fairness and has ethical implications for [predictions](#glossary-0 "Glossary term") and the decisions they influence. Bias can be introduced in training data, in the outcomes predicted by trained models, or both.

Examples of bias—and its consequences for decision-making—include:

- Training models on data that disproportionately represents certain income levels or health statuses, resulting in unfair decisions for insurance claims.
- Training models on skewed data with respect to race and gender of candidates, affecting hiring decisions.
- Training models that associate ZIP codes with creditworthiness.

### Data bias

Data bias occurs when the data used to train a model is skewed in a way that favors certain groups over others. Data bias is caused by unequal representation between groups in the training data.

For example, a dataset for predicting hiring outcomes could contain data that represents one gender as being more successful than others.

Data bias can be introduced into training data in several ways, including:

- Improper data collection in which certain groups are underrepresented or overrepresented.
- Data that reflects historical patterns accurately, but exposes the underlying bias in these trends and practices.

The data in the visualization below indicates data bias.

An example of data bias, visualized by a bar chart. In the source data, certain marital statuses are overrepresented compared to others with respect to income levels.

![Biased data that would introduce data bias if used in a machine learning model.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_concepts-data-bias-example.png "Click to view full size")

### Model bias

Model bias, or algorithmic bias, occurs when the predictions made by a machine learning model favor some groups over others. With model bias, models make associations between certain groups and outcomes, negatively impacting other groups. Model bias can be caused by improperly collected or skewed data, as well as behaviors specific to the training algorithm that is in use.

For example, a model could predict disproportionately negative hiring rates for certain age groups because of unfair associations made by the model.

Visualization from the Analyze tab in an ML experiment, highlighting model bias. The visualization shows that a model makes higher income predictions for certain marital statuses than others.

!['Analyze' tab in ML experiment showing model bias.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-model-bias-example.png "Click to view full size")

## Data bias metrics

In Qlik Predict, data bias is measured by analyzing:

- Representation rate: Compares the distribution of data belonging to each group in the feature, in comparison to all data in the feature. The calculated metric is representation rate parity ratio.
- Conditional distribution parity ratio: Compares the balance between data for each group in the feature, with respect to the values of the target column. The calculated metric is conditional distribution parity ratio.

To learn more about the acceptable values for these metrics, see [*Acceptable values for bias metrics*](#Metrics).

## Model bias metrics

In Qlik Predict, model bias metrics are best understood in the context of the model type for the experiment. Broadly speaking, there are the following bias metric categories:

- Classification model metrics
- Regression and time series model metrics

To learn more about the acceptable values for these metrics, see [*Acceptable values for bias metrics*](#Metrics).

### Classification models

In binary and multiclass classification models, bias is measured by analyzing predicted target values (outcomes). In particular, differences in positive and negative outcome rates for groups are compared ("positive" and "negative" here refer to outcomes that are favorable versus unfavorable—for example, a value of yes or no for a Hired target column.). These models have the following bias metrics:

- Disparate impact
- Statistical parity difference
- Equal opportunity difference

#### Disparate impact

Disparate impact ratio (DI) assesses whether groups in a sensitive feature are being favored or harmed in the model's predicted outcomes. It is measured by calculating how often each group is selected as the predicted value, comparing it to the rate of selection for the most favored group in the feature.

#### Statistical parity difference

Similar to disparate impact, statistical parity difference (SPD) assesses model predictions to determine if they favor or harm any individual groups. The metric is calculated by comparing the positive outcome rates between the largest and smallest groups.

#### Equal opportunity difference

Equal opportunity difference (EOD) is similar to the other two classification model bias metrics. EOD compares the highest and lowest true positive rates across groups in a feature.

### Regression and time series models

In regression and time series models, bias is measured by comparing how often models make errors in their predictions, using parity ratios to determine fairness of predicted outcomes.

The following bias metrics are calculated, using error metrics that are commonly used for evaluating model accuracy:

- MAE parity ratio

  [*MAE*](scoring-regression.htm#MAE)
- MSE parity ratio

  [*MSE*](scoring-regression.htm#MSE)
- RMSE parity ratio

  [*RMSE*](scoring-regression.htm#RMSE)
- R2 gap

  [*R2*](scoring-regression.htm#R2)
- MASE parity ratio

  [*MASE*](scoring-time-series.htm#MASE)
- MAPE parity ratio

  [*MAPE*](scoring-time-series.htm#MAPE)
- SMAPE parity ratio

  [*SMAPE*](scoring-time-series.htm#SMAPE)

## Acceptable values for bias metrics

Bias metrics—acceptable ranges and values

| Bias metric | Bias category | Applicable model types | Acceptable values |
| --- | --- | --- | --- |
| Representation rate parity ratio | Data bias | All | Ideal value: between 0.8 and 1.  A lower ratio indicates disproportionate representation. |
| Conditional distribution parity ratio | Data bias | All | Ideal value: between 0.8 and 1.  A lower ratio indicates disproportionate representation. |
| Statistical parity difference (SPD) | Model bias | Binary classification, multiclass classification | Ideal value: 0.  A value above 0.2 is a strong signal of unfairness. |
| Disparate impact (DI) | Model bias | Binary classification, multiclass classification | Ideal value: 1.  A value below 0.8 signals unfairness. |
| Equal opportunity difference (EOD) | Model bias | Binary classification, multiclass classification | Ideal value: 0.  A value above 0.1 signals unfairness. |
| MAE parity ratio | Model bias | Regression | Ideal value: between 0.8 and 1.  A value above 1.25 signals unfairness. |
| MSE parity ratio | Model bias | Regression | Ideal value: between 0.8 and 1.  A value above 1.25 signals unfairness. |
| RMSE parity ratio | Model bias | Regression | Ideal value: between 0.8 and 1.  A value above 1.25 signals unfairness. |
| R2 gap | Model bias | Regression | Ideal value: 0.  A value above 0.2 signals unfairness. |
| MASE parity ratio | Model bias | Time series | A value above 1.25 signals unfairness. |
| MAPE parity ratio | Model bias | Time series | A value above 1.25 signals unfairness. |
| SMAPE parity ratio | Model bias | Time series | A value above 1.25 signals unfairness. |

## Configuring bias detection

Bias detection is configured per training feature in the experiment version.

Do the following:

1. In an ML experiment, expand Bias in the training configuration panel.
2. Before selecting features for bias detection, optionally click Get recommendations to use generative AI to suggest features that could contain biased data. See [*Using generative AI to recommend features for bias detection*](#UsingAI).
3. Select or deselect any features for which you want to run bias detection.

Alternatively, toggle on bias detection for the desired features in ![Rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view.

### Using generative AI to recommend features for bias detection

You can use built-in integration with a large language model (LLM) to recommend potentially sensitive features before running the experiment.

How it works

- When you click Get recommendations, feature names and data samples are scanned by the LLM to check which of your features are recommended to be selected for bias detection.
- Recommendations are generated in response to inference requests which may be processed outside your Qlik Cloud tenant region.

  Information noteWhether at rest or in transit, your data is always encrypted.
- After getting recommendations, you can review the reasoning for each recommendation. For example, you can see if a feature is recommended due to potential geographic bias.
- Recommendations from the LLM are in English.

Click Get recommendations to use AI for suggested features on which to run bias detection.

![Reviewing AI recommendations for features on which bias detection is suggested.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_bias-llm.png "Click to view full size")

Administrative requirements

- AI features—that is, cross-region inference—must be enabled by a tenant administrator in order for this functionality to be available. This is done in the Administration activity center.

  For more information, see [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm).
- In addition to permissions for configuring experiments, users must have the Manage ML experiments permission set to Allowed where GenAI usage is permitted. For more information, see [*Use of AI tools in ML experiments*](who-can-work-with-automl.htm#CreateUseExpAI).

## Quick analysis of bias results

After training completes, you can get a quick overview of the bias detection results in the Models tab.

Warning note

Qlik does not guarantee the accuracy, completeness, or reliability of any bias detection results and does not ensure compliance with any local, state, federal, or international laws, regulations, or industry standards. The user assumes all risk and responsibility for any actions taken based on the tool's output, which should not be used as a substitute for professional legal advice or independent human auditing.

Scroll down through the quick analysis items to find Bias detection. Expand sections using the ![Dropdown arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dropdown_arrow.svg) icons. You can analyze features with possible data and model biases.

Analyzing data bias using the Bias detection section in the Models tab.

![Analyzing data bias using the Bias detection section in the Models tab.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-quick-analysis-data-bias.png "Click to view full size")

### Notes

- Favored groups are the target values or ranges that are overrepresented in the data or projected outcomes of the target, based on the bias metrics. Harmed groups are the target values or ranges that are underrepresented in the data or projected outcomes of the target, based on the bias metrics.

  For information about how the bias metrics are used, see [*Acceptable values for bias metrics*](#Metrics).

  The numbers in parentheses describe the criteria used to calculate the metric. For example, if the metric is equal opportunity difference (EOD), female (10%) and male (80%) indicates true positive rates of 80% for male and 10% for female.
- Target outcome refers to the value of the target column that is predicted by the model.
- Not all bias metrics and values are shown in the Models tab due to limited space. For example:

  - Depending on the metric and model types, some metrics and groups may only include minimums and maximums.
  - If multiple metrics exceed the bias threshold for a feature, the metric indicating the highest degree of unfairness is shown.
  - For biased features in multiclass classification models, only the metric indicating the highest degree of unfairness is shown.
- More detailed information is available in the Analyze tab and model training report. See [*Detailed analysis of bias results*](#Detailed).
- For more information about terminology in this section, see [*Terminology on this page*](#Terminology).

## Detailed analysis of bias results

You can dive deeper into bias results in the Analyze tab.

Warning note

Qlik does not guarantee the accuracy, completeness, or reliability of any bias detection results and does not ensure compliance with any local, state, federal, or international laws, regulations, or industry standards. The user assumes all risk and responsibility for any actions taken based on the tool's output, which should not be used as a substitute for professional legal advice or independent human auditing.

Do the following:

1. In an ML experiment, select a model and go to the Analyze tab.
2. Open the Bias sheet.
3. Select between Data bias and Model bias depending on the desired analysis.
4. In the Features with potential bias table, select a single feature.

Charts and metrics that indicate possible bias are displayed with a red background. You can select features by clicking and drawing in visualizations.

Metrics in the table are static for bias metrics corresponding to standard features. For future features, bias metrics change dynamically depending on [time series group](#Terminology) selection.

Analyze tab showing an analysis of model bias for the select feature. Possible bias is indicated by red backgrounds for charts and metrics.

![Analyzing model bias in granular fashion using the Bias sheet in the Analyze tab.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-detail-analysis-model-bias.png "Click to view full size")

For more information about navigating detailed model analyses, see [*Performing detailed model analysis*](analyze-models-detailed.htm).

### Bias results in training reports

Bias metrics are also presented in ML training reports. They are included in a dedicated Bias section in the report.

For more information about training reports, see [*Downloading ML training reports*](training-report.htm).

## Addressing bias

After analyzing the bias detection results for your models, you might want to do any of the following:

- Run new experiment versions after dropping the biased features.

  [*Configuring a new version*](refining-models.htm#Configur)
- Avoid deploying models that display bias, instead deploying models that meet the recommended criteria for bias metrics.

  [*Deploying models*](deploying-models.htm)
- Update your dataset to correct any improper data collection or to address unequal representation rates.

  [*Getting your dataset ready for training*](dataset-preparation.htm)
- Redefine your machine learning problem using the structured framework. For example, if your original machine learning question is inherently biased, models will likely always be unreliable in creating fair predictions.

  [*Defining machine learning questions*](machine-learning-framework.htm)

  [*Working with multivariate time series forecasting*](machine-learning-framework-time-series.htm)

## Terminology on this page

On this page, and in Qlik Predict,"groups" is a term that has different meanings depending on context:

- "Groups" refers to the values or ranges in features that are being analyzed for bias. For example, a Marital Status feature might have four possible groups in the training data: Married, Divorced, Separated, or Widowed.
- In time series experiments, "groups" refers to functionality that allows target outcomes to be tracked for specific values of compatible features. On this page, these groups are referred to as "time series groups". For more information about these groups, see [*Groups*](machine-learning-framework-time-series.htm#Groups).

## Limitations

- Some limitations on training dataset sizes exist if bias detection is turned on. See [*Training dataset and profiling limitations*](ml-limitations-capacities.htm#DatasetSizeCapacities).
- You cannot activate bias detection for:

  - The target feature.
  - Free text features (even if the feature type is changed to categorical).
  - Date features that are used as the date index in time series experiments.
  - Auto-engineered date features. You can run bias detection on these features, but you do not activate them independently. Instead, activate the parent date feature for bias detection and ensure the auto-engineered date features are included for training.

## Learn more

- [*Configuring experiments*](configuring-experiments.htm)
- [*Performing quick model analysis*](analyze-models-quick.htm)
- [*Performing detailed model analysis*](analyze-models-detailed.htm)
