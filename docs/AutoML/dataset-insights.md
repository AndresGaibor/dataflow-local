---
title: "Viewing  insights about your training data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/dataset-insights.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Configuring experiments"]
---

# Viewing insights about your training data

As you add your training data and run versions of the training, you can access insights about how your data is being handled. The Insights provide information about the target and features in your experiment, such as features that have been dropped, are unavailable, or will be encoded with special processing.

The Insights can be found in the Configuration/Training data tab, in both ![Schema](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view and ![Profile](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_profile.svg) Data view:

- In Schema view: Found in the Insights column.
- In Data view: Found as Insights in the information provided about each dataset column.

Insights are created individually for each model trained within the experiment.

Insights column in Schema view

![Insights shown about each feature column in the training dataset](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_dataset-insights.png "Click to view full size")

Insights are generated:

- After you have added or changed training data, but have not run any experiment versions yet.
- After each experiment version has run. A separate set of insights is created for each model trained.

The insights might be different before and after running a version. This is because as the training begins, Qlik Predict is able to preprocess your data and further diagnose issues with the data. For more information, see [*Automatic data preparation and transformation*](preprocessing-steps.htm).

## Viewing insights before training

Before you run a version of the experiment, you can analyze the Insights to see how the current training data is being interpreted. These insights could change after you run the version.

Do the following:

1. In an experiment, make sure you have added the training data that you want to use for the experiment version.
2. Open the Training data tab.
3. Analyze the Insights. Tooltips provide additional context behind the insights. For further explanations of what each insight means, see [*Interpreting dataset insights*](#Explanations).

## Viewing the insights for a model

After the models have finished training for an experiment version, select a model and inspect how the data was handled.

Do the following:

1. Run an experiment version and then open the Configuration/Training data tab.
2. Select a model from the drop down list in the toolbar.
3. Analyze the Insights. Tooltips provide additional context behind the insights. For further explanations of what each insight means, see [*Interpreting dataset insights*](#Explanations).

## Interpreting dataset insights

The following tables provide more detail about the possible insights that may be displayed in the schema.

### General insights

Dataset insights — General

| Insight | Meaning | Impact on configuration | When the insight is determined | Additional references |
| --- | --- | --- | --- | --- |
| Constant | The column has the same value for all rows. | The column cannot be used as a target or included feature. | Before and after running the version | [*Cardinality*](cardinality.htm) |
| One-hot encoded | The feature type is categorical and the column has less than 14 unique values. | No effect on configuration. | Before and after running the version | [*Categorical encoding*](categorical-encoding.htm) |
| Impact encoded | The feature type is categorical and the column has 14 or more unique values. | No effect on configuration. | Before and after running the version | [*Categorical encoding*](categorical-encoding.htm) |
| High cardinality | The column has too many unique values, and can negatively affect model performance if used as a feature. | The column cannot be used as a target. It will be excluded automatically as a feature, but can still be included if needed. | Before and after running the version | [*Cardinality*](cardinality.htm) |
| Sparse data | The column has too many null values. | The column cannot be used as a target or included feature. | Before and after running the version | [*Imputation of nulls*](null-imputation.htm) |
| Underrepresented class | The column has a class with less than 10 rows. | The column cannot be used as a target, but can be included as a feature. | Before and after running the version | - |
| Feature transform failed | The feature type of a feature was manually changed from its default type. With this configuration, an error occurred. | The experiment version cannot run successfully with this feature transform. Revert the feature type of the feature to its former value, or exclude the feature from the training. | After running the version | [*Changing feature types*](configuring-experiments.htm#Changing) |

### Automatic feature engineering insights

Dataset insights — Automatic feature engineering

| Insight | Meaning | Impact on configuration | When the insight is determined | Additional references |
| --- | --- | --- | --- | --- |
| <number of> auto-engineered features | The column is the parent feature that can be used to generate auto-engineered features. | If this parent feature is interpreted as a date feature, it is automatically removed from the configuration. It is recommended that you instead use the auto-engineered date features that can be generated from it. It is possible to override this setting and include the feature rather than the auto-engineered features. | Before and after running the version | [*Automatic feature engineering*](automatic-feature-engineering.htm) |
| Auto-engineered feature | The column is an auto-engineered feature which can, or has been, generated from a parent date feature. It did not appear in the original dataset. | You can remove one or multiple of these auto-engineered features during experiment training. If you switch the feature type of the parent feature to categorical, all auto-engineered features are removed. | Before and after running the version | [*Automatic feature engineering*](automatic-feature-engineering.htm) |
| Could not process as date | The column possibly includes date and time information, but could not be used to create auto-engineered date features. | The feature is dropped from the configuration. If auto-engineered features were previously generated from this parent feature, they are removed from future experiment versions. You can still use the feature in the experiment, but you must switch its feature type to categorical. | After running the version | [*Automatic feature engineering*](automatic-feature-engineering.htm#Date) |
| Possible free text | The column could possibly be available for use as a free text feature. | The free text feature type is assigned to the column. You must run an experiment version to confirm whether the feature can be processed as free text. | Before running the version | [*Automatic feature engineering*](automatic-feature-engineering.htm#FreeText) |
| Free text | The column has been confirmed as containing free text. It can be processed as free text. | No additional configurations are required for the feature. | After running the version | [*Automatic feature engineering*](automatic-feature-engineering.htm#FreeText) |
| Could not process as free text | Upon further analysis, the column cannot be processed as free text. | You need to deselect the feature from the configuration for the next experiment version. If the feature does not have high cardinality, you can alternatively change the feature type to categorical. | After running the version | [*Automatic feature engineering*](automatic-feature-engineering.htm#FreeText) |

### Intelligent model optimization insights

Dataset insights — Intelligent model optimization

| Insight | Meaning | Impact on configuration | When the insight is determined | Additional references |
| --- | --- | --- | --- | --- |
| Target leakage | The feature is suspected of being affected by target leakage. If so, it includes information about the target column that you are trying to predict. Features with target leakage can give you a false sense of assurance about model performance. In real-world predictions, they cause the model to perform very poorly. | The feature has not been used to train the model. | After running the version | [*Data leakage*](data-leakage.htm) |
| Low permutation importance | The feature does not have much, if any, influence on the model predictions. Removing these features improves model performance by reducing statistical noise. | The feature has not been used to train the model. | After running the version | [*Understanding permutation importance*](permutation-importance.htm) |
| Highly correlated | The feature is highly correlated with one or more other features in the experiment. Having features that are highly correlated with one another decreases model performance. | The feature has not been used to train the model. The feature with which it is highly correlated has not been dropped due to high correlation, but could have been dropped for another reason, such as low permutation importance. | After running the version | [*Correlation*](correlation.htm) |

### Time series forecasting insights

Dataset insights — Time series forecasting

| Insight | Meaning | Impact on configuration | When the insight is determined | Additional references |
| --- | --- | --- | --- | --- |
| Possible date index | The feature can possibly be used as a date index for the time series experiment. | If used as a time series date index, the data in the column can affect aspects of the time series configuration, such as how long into the future you can forecast.  Values in the date index need to increase with each row or unique group value at a fixed time interval. | Before running the version | [*Working with time series experiments*](time-series-experiment.htm)  [*Date index*](machine-learning-framework-time-series.htm#DateIndex) |

### Bias detection insights

Dataset insights — Bias detection

| Insight | Meaning | Impact on configuration | When the insight is determined | Additional references |
| --- | --- | --- | --- | --- |
| Data bias detected | With the respect to the values in the target column, some groups (values)  are underrepresented compared to others. | Analyze bias detection results to determine next steps—these can include dropping the feature, changing the dataset, or creating a new experiment with a revised framework. | After running the version | [*Detecting bias in machine learning models*](bias-detection.htm) |
| Representation bias detected | Bias has been detected in how the trained model is using the data from the feature to create predictions. | Analyze bias detection results to determine next steps—these can include dropping the feature, changing the dataset, or creating a new experiment with a revised framework. | After running the version | [*Detecting bias in machine learning models*](bias-detection.htm) |
