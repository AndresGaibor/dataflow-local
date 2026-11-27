---
title: "Creating time-aware models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/time-aware-models.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Configuring experiments", "Working with model optimization"]
---

# Creating time-aware models

With time-aware training, you can build models that are equipped to predict data along a time-based column that exists in your training data. Activate time-aware training if you need to make predictions on a target that is known to be impacted by this time-based column.

Time-aware training helps reduce data leakage by applying specialized data processing to the training data. This processing allows machine learning algorithms to better interpret the data, and the predictive context, as dependent on a specific date or time dimension.

To train time-aware models, you need a column in your training dataset that contains date or timestamp data. This column is the date index that is used to sort the dataset prior to training. For more information about the date index, see [*Date index requirements*](#Index).

## When to use time-aware training

Time-aware model training is ideal for models that are forecasting changes over a time metric that is already present in the training. For example:

- You want to predict your sales for next month, and you have a Transaction Date column in your dataset.
- You want to predict metrics on late shipping deliveries, and you have a Delivered Date column in your dataset.

## How does time-aware training work

A common problem in machine learning is finding a way to make sure models are trained only on information that would be available at the time of training. If your training data contains prominent date and time information, this information can be used to help prevent data leakage.

### Date index requirements

To activate time-aware training, you need to have a column in your dataset that contains the date and time information on which the model training depends. You select the column when configuring model optimization for the training.

To use a column as the date index in your training, the column must have all of the following:

- Full dates. For example, columns consisting of month or day values cannot be used.
- The date or timestamp data type.
- The date feature type.

### Holdout and cross-validation

When choosing how the data is separated for the holdout and cross-validation process, methods of random selection can introduce future data into the model training. When you activate time-aware training, Qlik Predict instead uses the following process:

- The training dataset is sorted along your selected index column before it is separated into training and holdout data.
- Each iteration of the training uses a fixed test size and a gradually increasing training size. With each iteration, the data becomes more and more recent.

For full details, see [*Time-based cross-validation*](holdout-crossvalidation.htm#TimeAware).

### Other processing

Time-aware model training also uses other processes that are different from the default training processes. For example, time-aware training uses a modified process for null imputation. For more information, see [*Imputation of nulls*](null-imputation.htm).

## Turning on time-aware training

Time-aware model training can be turned on or off, or reconfigured, for each version you run in an experiment.

Do the following:

1. In an experiment, click ![Schema](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) View configuration.
2. If you have already run at least one version of the experiment, click New version.
3. In the panel, expand Model optimization.
4. Under Time-based test-train split, select the Date index to use for sorting the data.

You can change the time-aware training during model refinement. For example, you can turn the setting off, or select a new column as the date index. For more information, see [*Refining models*](refining-models.htm).

## Limitations and considerations

Depending on your use case, time-aware model training could help you build better models. In other cases, you might see better results with time series models or the default training process for classification and regression models. Time-aware training is useful when you do not want to train a time series model but you still need to include some time-based focus into the resulting model. For example, time-aware training can be a suitable alternative to time series model training when your input data does not allow [grouping](machine-learning-framework-time-series.htm#Groups).

Time-aware training does not perform automated feature engineering to generate lagging features for time series problems.

Time-aware training is not available for time series experiments.
