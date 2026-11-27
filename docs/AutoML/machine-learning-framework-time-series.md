---
title: "Working with multivariate time series forecasting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning", "Defining machine learning questions"]
---

# Working with multivariate time series forecasting

Expand/Collapse all

# Working with multivariate time series forecasting

With Qlik Predict, you can train machine learning models to forecast time-specific metrics. Using neural network-based methods, models learn and predict complex patterns involving time-specific associations, grouped target data, historical features, and known future variables. To create a time series forecast, prepare a training dataset, use it in a time series experiment, deploy a model, and then create apply datasets that you can use to generate predictions.

## Components of a time series problem

With time series forecasting, the goal is to predict target values for specific dates into the future. For example, you might want to predict sales for the next week, month, or quarter.

When developing your time series problem, define the following components:

- Target and groups
- Date index
- Forecast horizon
- Covariates

Information noteThis framework describes how to define a machine learning question for time series forecasting problems. To define machine learning questions for classification and regression problems, see [*Defining machine learning questions*](machine-learning-framework.htm).

Simplified illustration outlining the components of a time series forecasting problem in Qlik Predict.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/concept_ml-time-series-forecast-simple.png "Click to view full size")

### Target

As with other experiment types, the target is the column for which you want the model to predict future values. For time series experiments, the target needs to contain numeric data—for example, sales or inventory.

If you are using [groups](#Groups) in the time series forecast, models will predict one target value per group per time step in the [forecast window](#ForecastHorizon). If you are not using groups, your trained models will predict one target value for each time step in the forecast window.

### Date index

The date index tracks the time series metrics over a continuous time interval (time step). You need to decide on your time step at an early stage: how often do you need to predict future values?

Specifically, the date index is a column that appears in your training and apply datasets for time series problems. The date index determines the structure of both of these apply datasets—each row represents a step in time (or, with groups, a step in time for each unique grouping).

When you add your training dataset in a time series experiment, possible date index columns are automatically identified and presented to you as Insights at the column level. You can identify them from the Possible date index insight in schema view.

### Groups

Groups are features containing categorical information for which you want to generate predictions separately. Classic examples of groups include store number and product, which could have been used to organize data for a target such as sales. By selecting store number and product type as groups, your time series models will provide predictions for each individual value across these columns. For example, with a target of sales, if you have three store numbers — 1, 2, and 3 — and two product types — grocery and produce — your model will generate sales predictions for each unique combination of these values.

You should incorporate groups into your time series problem if you have the data and need individual predictions by category. Another advantage of groups is that models can learn globally, better understanding the patterns that exist between the different groupings you define.

You can configure the groups to use for each experiment version. If you do not specify groups but groups are identified in your training dataset, the training will use groups.

Groups are identified by duplicate values in the date index column—for example, for a date of 1/14/2025, you have two records: one for store A, and the other for store B.

Each group in a time series experiment — including the target alone — are considered to be separate time series within your dataset. See [*What is a time series?*](#TimeSeries).

#### Primary and secondary groups

For time series problems with two group columns, one group is the primary group and the other is the secondary group. For examples, see [*Preparing a training dataset*](#TrainPrepare), [*Training dataset example — two groups*](#2Groups), and [*Apply dataset example — two groups*](#TwoGroups).

The primary grouping defines independent time series. For example, each store becomes its own separate time series, allowing the model to learn different behaviors and patterns across stores.

The secondary grouping is treated differently. Instead of creating fully separate series, the system pivots those values into additional features (covariates), allowing related sub-series to provide contextual information to each other.

You generally do not need to know which group is the primary and which is the secondary, although you can optionally choose a primary group in your experiment. Certain considerations apply for predicting with deployed time series models—see [*Preparing an apply dataset*](#ApplyPrepare).

Information note

All primary groups should share the same secondary groups. For example, if stores are primary groups and products are secondary groups, each store should contain the same set of products. Missing secondary groups would lead to inconsistent feature dimensions across time series.

If you expect secondary group values to not align with primary group values at prediction time, one possible approach is to combine the original primary and secondary group values into a new grouping column and use it as the primary group when retraining the model. In this setup, the model no longer depends on secondary groups, but correlated information between groups might be reduced.

### Forecast horizon

The forecast horizon specifies how far into the future you want to forecast. The forecast horizon is composed of the forecast window (the number of time steps for which you need predictions) and forecast gap (an optional number of time steps after your historical data for which you do not want predictions).

You set the forecast window and gap size when configuring an experiment version. These values are used both during model training and when generating predictions from models deployed as ML deployments.

The forecast window is the number of [time steps](#TimeSteps) for which you want to predict into the future. For example, if your time step is one day and you want to forecast sales for the next two weeks, you would set your forecast window to 14.

The forecast gap is the amount of time in the future for which you do not require predictions. Setting a forecast gap is optional, because you may or may not need one. The forecast gap starts at the end of the recorded historical training data you have provided. The forecast window begins where the forecast gap ends.

For example, you might be looking to predict future sales, but you are only interested in future sales for dates later than one week after the end of your input data. In this case, with a time step of days, you could set your forecast gap size to seven time steps.

Your selected forecast window, in addition to how much training data you have, limits how far into the future you can forecast. For more information, see [*Maximum forecast window*](#MaximumForecast).

### Covariates

In time series problems, [features](#glossary-0 "Glossary term") are often called covariates. Similar to other machine learning problems, covariates are the other variables that you suspect have an influence on the outcome of the target. Each covariate is represented as a single column in your training dataset.

In time series forecasting, there are several types of covariates and they have some important distinctions:

- Static covariates: Columns that do not vary over the course of a time series. Static covariates are applicable in time series experiments where groups are being used. For example, suppose you have groups for Product and Store Number, and there is a feature Default Discount. If Product A in Store 1 has a default discount of 10% and Product B in Store 2 has a default discount of 20%, Default Discount would be a static covariate. That is, it does not vary within the data for the group within which it appears.

  Static covariates are detected automatically from historical features you include in the experiment. You do not need to indicate which features are static covariates.
- Past covariates: Time-dependent variables that are available only in the historical data, and which vary across this data. Past covariates are detected automatically from historical features you include in the experiment. You do not need to explicitly indicate which features are past covariates.
- Future covariates: Future covariates, also known as [future features](#FutureFeatures), are time-dependent variables for which you will know the future values within the forecast horizon. When using future covariates in training, you need to indicate them as future features in the training configuration.

#### Future features

With future features, you can provide additional data to your models about future information you already know or can reasonably expect. In particular, you have access to future values for this feature spanning your selected [forecast horizon](#ForecastHorizon). When defining future features, you need to provide historical as well as future data.

For example, for a model predicting metrics that could be influenced by future discounts offered by a store, you could include the historically observed discounts, as well as the discounts for future time periods within the forecast window. Other examples of future features could be weather or calendar information.

## Other important concepts

This section outlines concepts that are relevant to your time series problem, but that you do not configure directly in an experiment or ML deployment. These are properties that are defined by your data or by other [properties you configure for the model](#Components).

### Time steps

The time step is defined by your training dataset and is important for both training and predictions.

In your training dataset, the time step is the interval at which the data in your date index is recorded. For example, the time step can be daily, every hour, every minute, or every second. The smallest time step detected is milliseconds.

It is important to be aware of the time step used in your training data. Other experiment parameters you define, such as [forecast window and forecast gap size](#ForecastHorizon), will follow this time step interval.

After deploying your model, the apply data for which you want to create predictions will need to follow the same time step as defined in the training dataset.

#### Quality

When you select a training dataset, the system infers the time step used. If there are some missing values or gaps in the date index, columns such as target, groups, and covariates can often be interpolated automatically by the system. Recurring gap patterns caused by missing values are handled automatically and do not by themselves introduce a new time step. However, if your data contains truly mixed recording intervals to the point where different native time steps are detected, the data must be fixed first. For example, if you have several months of data recorded once daily, but there is a section in which data is consistently recorded on a weekly basis, the dataset cannot be used because multiple time steps will be detected.

### Apply window

The apply window, or look-back period, is the portion of the training data that the algorithm can use to provide the predictions for your specified [forecast window](#ForecastHorizon).

The apply window is calculated and set by the system. It is measured in [time steps](#TimeSteps). The apply window is defined by what you set as the forecast window and gap (forecast horizon). Your apply window size is shown in the experiment configuration panel and the Model training summary, after running at least one experiment version. It is also shown in an ML deployment Model schema when creating or editing a batch prediction configuration.

The apply window is identified automatically from your training configuration. To generate predictions for a given forecast window, you need to provide the historical data covering at least your apply window. This is provided in your apply dataset. See [*Preparing an apply dataset*](#ApplyPrepare).

### Maximum forecast window

The maximum forecast window is estimated as you configure your time series experiment. After you have run a version of the training, the maximum forecast window is confirmed with certainty. The maximum forecast window is displayed to you as the Estimated maximum forecast or Maximum forecast under Based on your data, when you open Target and experiment type in the experiment configuration panel. The maximum forecast window is the maximum number of time steps for which you can generate forecasts, given your chosen forecast window, how much historical data you have provided, and the minimum sample size expected by the system. The more historical data you provide, the further in time you will be able to predict. However, to generate reliable predictions, it is important to select a reasonable forecast window.

The maximum forecast window can be as large as 180 time steps.

### Forecast cut-off time

The forecast cut-off time is especially important when defining your apply dataset during predictions. The forecast cut-off time is the last date in your sample for which you have a target value. Essentially, dates after this cut-off time are the dates for which you want to generate predictions.

### What is a time series?

In Qlik Predict time series forecasting, each group — including the target alone — are considered to be separate time series within the training dataset. For example, suppose your training dataset contains sales metrics. These sales metrics are defined for each store and product type. With Store and Product Type columns defined as groups, there are three time series in the training dataset.

## Preparing a training dataset

For multivariate time series forecasts, your training dataset needs to contain the following columns:

- Date index
- Target column
- Group columns (optional)
- Feature columns (optional—without features, you are training a univariate forecasting model)

Illustrations showing the required columns and data for time series training datasets. Scenarios with no groups, one group, and two groups are described.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/concept_ml-time-series-forecast-train-data-tabular.png "Click to view full size")

Linear diagram outlining the needed components, and timeline, of a training dataset for a time series forecasting model.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/concept_ml-time-series-forecast-train-data.png "Click to view full size")

### Date index column

You need a [date index](#DateIndex) containing full dates or time stamps. This column is the chronological index along which the target and covariate metrics are tracked. The date index column organizes the time-based measurements sequentially along a consistent time interval (the [time step](#TimeSteps)).

The date index column is organized as follows, depending on whether or not you are using groups:

- No groups: A single record for each time step. For example, with a daily forecast, each row represents a single day.
- With groups: One or more duplicate entries for each time step depending on the groups used.

With a multivariate training dataset, there will be one or more duplicate entries for each time step depending on the groups used. There is flexibility in the time step you use — you could, for example, record dates one or more times on a daily, weekly, or monthly basis, and so on.

Missing or inconsistently recorded values in this column are sometimes acceptable, if they can be interpolated, and recurring missing-value gap patterns are handled automatically. However, your date index values cannot contain multiple different native time steps. For example, if the interval is determined to be once daily, but at some point, an interval of twice daily is identified, an error will occur during training.

### Target column and group columns

Your dataset needs to have a target column containing a numeric metric that you want to forecast. A common example is sales.

If you are using groups, you provide historical target values for each possible value in [groups](#Groups) that you add. For example, if your target is Sales and you add a group Store Number that contains data for Store A and Store B, your dataset needs to include two separate records for each time step: one with the sales value for Store A, and the other with the sales value for Store B.

Information noteIf you have two groups, ensure that all primary groups share the same secondary groups. See [*Primary and secondary groups*](#Primary).

### Feature columns

You can train a time series model without any [covariates](#Covariates). However, if you include covariates, provide a column in the dataset for each feature. Feature data should generally be historically recorded data unless you are adding future features. Future feature columns can contain both historical and future data. You should only include future feature data in the training dataset if you are confident that the future values of these column will be known when you create predictions.

Keep track of which features you will use as future features, as you will need to select them as such in the training configuration.

### Data volume

Your dataset needs to contain enough records—data volume is determined by the time range shared across all groups. Only the data from this overlapping period is used to train the experiment.

The volume of your historical data plays a part in determining how far into the future you can predict. Your desired forecast window also affects how much historical data you need.

Generally, more historical data is better than less. However, the data needs to be of good quality and capture the desired trends. If the data provides irrelevant information or contains inaccuracies, it is not helpful to have it in the model. Consider a balance between optimizing volume and maintaining quality and relevance.

### Examples

Training dataset example — no groups

The table below is a truncated example of a training dataset that does not use any groups.

In this example:

- We want to predict two weeks of daily sales, with no gap. Note that this desired forecast horizon and gap size is not denoted directly in the training data, but we provide enough records so that this forecast horizon can be used in the configuration.
- Date is the date index, with a time step of 1 day.
- Sales is the target, tracking total daily sales.
- Transactions Per Hour tracks the rounded average number of transactions that took place per hour. This is a past covariate, containing only historical data. This information will not be known into the future.
- On Promotion tracks how many products are discounted at promotional rates for the specified date. It can be used as a future feature, because in this case, discounts are known and planned ahead of time. In this case, we provide historical (past) data only.

Truncated example of training dataset that contains no group columns

| ID | Date | On Promotion | Transactions per Hour | Sales |
| --- | --- | --- | --- | --- |
| 1 | 1/1/2024 | 0 | 301 | 90010.01 |
| 2 | 1/2/2024 | 100 | 291 | 19491.65 |
| 3 | 1/3/2024 | 0 | 163 | 70001.87 |
| 4 | 1/4/2024 | 14 | 499 | 50240.33 |
| 5 | 1/5/2024 | 55 | 211 | 106943.00 |
| 6 | 1/6/2024 | 2 | 309 | 131492.59 |
| 7 | 1/7/2024 | 1341 | 300 | 46349.49 |
| 8 | 1/8/2024 | 0 | 432 | 88203.08 |
| 9 | 1/9/2024 | 0 | 104 | 40254.95 |
| 10 | 1/10/2024 | 150 | 495 | 45964.44 |
| 11 | 1/11/2024 | 65 | 204 | 90185.50 |
| 12 | 1/12/2024 | 12 | 252 | 76340.25 |
| 13 | 1/13/2024 | 70 | 99 | 71311.11 |
| 14 | 1/14/2024 | 5 | 305 | 50396.70 |
| ... | ... | ... | ... | ... |
| 610 | 9/1/2025 | 158 | 168 | 104205.33 |

Training dataset example — two groups

The table below is a truncated example of a training dataset that uses two group columns.

In this example:

- We want to predict two weeks of daily sales, with no gap. Note that this desired forecast horizon size is not denoted directly in the training data, but we provide enough records so that this forecast horizon can be used in the configuration.
- Date is the date index, with a time step of 1 day.
- Sales is the target, tracking total daily sales.
- Store and Product are groups. For each unique time step in the training data, separate rows are included for each store and product.

  In this context, Store is the primary group and Product is the secondary group.
- Transactions Per Hour tracks the average number of transactions that take place per hour, for each store and product. It is a past covariate, containing only historical data. This information will not be known into the future.
- On Promotion tracks how many products are discounted at promotional rates for the specified date, for each store and product. It can be used as a future feature, because in this case, discounts are known and planned ahead of time. In this case, we provide historical (past) data only.

Truncated example of training dataset that contains two groups

| Date | Store | Product | On Promotion | Transactions per Hour | Sales |
| --- | --- | --- | --- | --- | --- |
| 1/1/2024 | Store 1 | A | 0 | 343 | 90010.01 |
| 1/1/2024 | Store 2 | A | 100 | 545 | 19491.65 |
| 1/1/2024 | Store 3 | A | 0 | 1004 | 70001.87 |
| 1/1/2024 | Store 1 | B | 14 | 305 | 39522.11 |
| 1/1/2024 | Store 2 | B | 55 | 700 | 91859.30 |
| 1/1/2024 | Store 3 | B | 2 | 94 | 19583.55 |
| 1/1/2024 | Store 1 | C | 1341 | 267 | 194863.00 |
| 1/1/2024 | Store 2 | C | 0 | 630 | 140244.13 |
| 1/1/2024 | Store 3 | C | 0 | 1143 | 76666.66 |
| 1/2/2024 | Store 1 | A | 56 | 576 | 30593.55 |
| 1/2/2024 | Store 2 | A | 3 | 403 | 10549.33 |
| 1/2/2024 | Store 3 | A | 14 | 1303 | 100003.33 |
| 1/2/2024 | Store 1 | B | 29 | 593 | 105893.99 |
| 1/2/2024 | Store 2 | B | 100 | 305 | 80195.22 |
| 1/2/2024 | Store 3 | B | 0 | 305 | 61051.13 |
| 1/2/2024 | Store 1 | C | 5 | 105 | 55938.38 |
| 1/2/2024 | Store 2 | C | 33 | 72 | 104823.33 |
| 1/2/2024 | Store 3 | C | 15 | 1052 | 99105.99 |
| 1/3/2024 | Store 1 | A | 5 | 521 | 130533.31 |
| 1/3/2024 | Store 2 | A | 1 | 205 | 67676.73 |
| 1/3/2024 | Store 3 | A | 36 | 302 | 52745.45 |
| 1/3/2024 | Store 1 | B | 111 | 502 | 99642.10 |
| 1/3/2024 | Store 2 | B | 350 | 693 | 34660.34 |
| 1/3/2024 | Store 3 | B | 34 | 200 | 60345.44 |
| 1/3/2024 | Store 1 | C | 93 | 205 | 44603.33 |
| 1/3/2024 | Store 2 | C | 60 | 295 | 105844.44 |
| 1/3/2024 | Store 3 | C | 10 | 76 | 150385.44 |
| ... | ... | ... | ... | ... | ... |
| 9/10/2025 | Store 1 | A | 15 | 1058 | 159383.33 |
| 9/10/2025 | Store 2 | A | 20 | 402 | 80119.11 |
| 9/10/2025 | Store 3 | A | 20 | 191 | 106020.00 |
| 9/10/2025 | Store 1 | B | 39 | 100 | 39581.34 |
| 9/10/2025 | Store 2 | B | 109 | 190 | 76939.23 |
| 9/10/2025 | Store 3 | B | 37 | 99 | 49548.42 |
| 9/10/2025 | Store 1 | C | 75 | 1555 | 93150.77 |
| 9/10/2025 | Store 2 | C | 190 | 1603 | 15923.49 |
| 9/10/2025 | Store 3 | C | 0 | 403 | 159342.05 |

## Preparing an apply dataset

After you deploy a time series model, you need to develop an [apply dataset](#glossary-1 "Glossary term") for which predictions will be made.

### Apply dataset — Requirements and validation

For time series models, the apply dataset needs:

- Columns and column headers for all columns included in [the training dataset](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm#TrainPrepare).
- The same [time step](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm) as the training dataset.
- All [groups](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm#Groups) and group values that were present in the training dataset.

  Information noteIf new group values are present in the apply dataset (which were not present in the training data), predictions are not generated for these rows. If predictions are required for these new group values, it is recommended that you retrain the model with training data that includes them.

  Information note

  At prediction time or in the apply dataset, missing group values are handled as follows:

  - The absence of [primary group](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm#Primary) values—on which the model is trained—is allowed.
  - Missing secondary group values are not allowed. Prediction fails with an error.

  It is best to collect and provide all secondary group data during prediction whenever possible. However, if secondary groups are expected to be missing mainly at prediction time, one possible solution is to avoid using secondary groups altogether.

  Instead, you can combine the original primary and secondary group values into a single new grouping column, use it as the new primary group, and retrain the model based on that structure. In this setup, the new model depends only on the newly introduced primary groups.

  The tradeoff is that you may lose some of the correlated information between groups, since they will now be treated as fully separate time series rather than related sub-series providing contextual information to each other.
- As many or more historical data records (per target and group) prior to the [forecast cut-off time](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm#ForecastCutOff) as the number of records in the [apply window](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm#ApplyWindow) for the model. These need to be full records containing the historically observed date or time stamp, [target](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm#Target), and [covariate](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm#Covariates) values. The apply window is determined by the [forecast window and gap](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm#ForecastHorizon) configured during training — the longer into the future you need to predict, the more historical data you need in your apply dataset to run predictions.
- Records for all future time steps in your forecast horizon. For these future records, only include the values for the date index column, as well as any [future features](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework-time-series.htm#FutureFeatures). Leave the values for the other columns blank.

Tip noteMost of the historical data requirements for your apply dataset are to specify minimum acceptable data volumes. You can always provide more than needed. When the model generates predictions, only the records needed to cover the apply window are used.

Illustrations showing the required columns and data for apply datasets used to generate predictions from time series forecasting models. Scenarios with no groups, one group, and two groups are described.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/concept_ml-time-series-forecast-apply-data-tabular.png "Click to view full size")

Linear diagram outlining the needed components, and timeline, of an apply dataset that is used to generate predictions with a time series forecasting model.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/concept_ml-time-series-forecast-apply-data.png "Click to view full size")

### Examples

Apply dataset example — no groups

Suppose you have a time series model configured as follows:

- Target: Sales
- No groups
- Date index: Date
- Time step: 1 day
- Forecast window of 7 days and forecast gap of 14 days. Therefore, the forecast horizon is 21 days.
- Forecast cut-off time of September 1, 2025. This is the last date for which historical data was provided.
- A past covariate Transactions Per Hour that tracks the average number of transactions that took place per hour.
- A future covariate On Promotion that tracks how many products are discounted at promotional rates for the specified date.

In this example, it is assumed that the system-defined apply window is 63 days. In addition to 63 days of historical data (July 1, 2025 to September 1, 2025), the dataset provides future covariate data for the 21-day forecast horizon (September 2 to 22, 2025).

Full example of apply dataset for model trained with no groups

| ID | Date | On Promotion | Transactions per Hour | Sales |
| --- | --- | --- | --- | --- |
| 548 | 7/1/2025 | 0 | 343 | 90010.01 |
| 549 | 7/2/2025 | 100 | 545 | 19491.65 |
| 550 | 7/3/2025 | 0 | 1004 | 70001.87 |
| 551 | 7/4/2025 | 14 | 305 | 39522.11 |
| 552 | 7/5/2025 | 55 | 700 | 91859.30 |
| 553 | 7/6/2025 | 2 | 94 | 19583.55 |
| 554 | 7/7/2025 | 1341 | 267 | 194863.00 |
| 555 | 7/8/2025 | 0 | 630 | 140244.13 |
| 556 | 7/9/2025 | 0 | 1143 | 76666.66 |
| 557 | 7/10/2025 | 56 | 576 | 30593.55 |
| 558 | 7/11/2025 | 3 | 403 | 10549.33 |
| 559 | 7/12/2025 | 14 | 1303 | 100003.33 |
| 560 | 7/13/2025 | 29 | 593 | 105893.99 |
| 561 | 7/14/2025 | 100 | 305 | 80195.22 |
| 562 | 7/15/2025 | 0 | 305 | 61051.13 |
| 563 | 7/16/2025 | 5 | 105 | 55938.38 |
| 564 | 7/17/2025 | 33 | 72 | 104823.33 |
| 565 | 7/18/2025 | 15 | 1052 | 99105.99 |
| 566 | 7/19/2025 | 5 | 521 | 130533.31 |
| 567 | 7/20/2025 | 1 | 205 | 67676.73 |
| 568 | 7/21/2025 | 36 | 302 | 52745.45 |
| 569 | 7/22/2025 | 111 | 502 | 99642.10 |
| 570 | 7/23/2025 | 350 | 693 | 34660.34 |
| 571 | 7/24/2025 | 34 | 200 | 60345.44 |
| 572 | 7/25/2025 | 93 | 205 | 44603.33 |
| 573 | 7/26/2025 | 60 | 295 | 105844.44 |
| 574 | 7/27/2025 | 10 | 76 | 150385.44 |
| 575 | 7/28/2025 | 402 | 473 | 40963.10 |
| 576 | 7/29/2025 | 15 | 1058 | 159383.33 |
| 577 | 7/30/2025 | 20 | 402 | 80119.11 |
| 578 | 7/31/2025 | 20 | 191 | 106020.00 |
| 579 | 8/1/2025 | 39 | 100 | 39581.34 |
| 580 | 8/2/2025 | 109 | 190 | 76939.23 |
| 581 | 8/3/2025 | 37 | 99 | 49548.42 |
| 582 | 8/4/2025 | 75 | 1555 | 93150.77 |
| 583 | 8/5/2025 | 190 | 1603 | 15923.49 |
| 584 | 8/6/2025 | 0 | 403 | 159342.05 |
| 585 | 8/7/2025 | 32 | 430 | 20451.33 |
| 586 | 8/8/2025 | 436 | 1000 | 150314.44 |
| 587 | 8/9/2025 | 1 | 1532 | 15923.91 |
| 588 | 8/10/2025 | 40 | 99 | 15944.10 |
| 589 | 8/11/2025 | 42 | 1058 | 60000.01 |
| 590 | 8/12/2025 | 25 | 734 | 39583.55 |
| 591 | 8/13/2025 | 1 | 569 | 150333.65 |
| 592 | 8/14/2025 | 305 | 692 | 124594.13 |
| 593 | 8/15/2025 | 11 | 164 | 59303.13 |
| 594 | 8/16/2025 | 60 | 205 | 150333.31 |
| 595 | 8/17/2025 | 70 | 186 | 103483.53 |
| 596 | 8/18/2025 | 25 | 1483 | 105038.13 |
| 597 | 8/19/2025 | 30 | 999 | 201857.11 |
| 598 | 8/20/2025 | 30 | 1533 | 35439.33 |
| 599 | 8/21/2025 | 30 | 1583 | 51956.24 |
| 600 | 8/22/2025 | 0 | 350 | 55334.30 |
| 601 | 8/23/2025 | 33 | 1509 | 11111.12 |
| 602 | 8/24/2025 | 145 | 74 | 15493.33 |
| 603 | 8/25/2025 | 33 | 140 | 159334.14 |
| 604 | 8/26/2025 | 59 | 884 | 45603.39 |
| 605 | 8/27/2025 | 65 | 239 | 46593.34 |
| 606 | 8/28/2025 | 16 | 502 | 74747.74 |
| 607 | 8/29/2025 | 17 | 158 | 45491.34 |
| 608 | 8/30/2025 | 15 | 1693 | 34503.11 |
| 609 | 8/31/2025 | 36 | 1544 | 159334.13 |
| 610 | 9/1/2025 | 62 | 1999 | 193803.15 |
| 611 | 9/2/2025 | 45 | - | - |
| 612 | 9/3/2025 | 32 | - | - |
| 613 | 9/4/2025 | 52 | - | - |
| 614 | 9/5/2025 | 10 | - | - |
| 615 | 9/6/2025 | 0 | - | - |
| 616 | 9/7/2025 | 13 | - | - |
| 617 | 9/8/2025 | 99 | - | - |
| 618 | 9/9/2025 | 14 | - | - |
| 619 | 9/10/2025 | 56 | - | - |
| 620 | 9/11/2025 | 32 | - | - |
| 621 | 9/12/2025 | 13 | - | - |
| 622 | 9/13/2025 | 15 | - | - |
| 623 | 9/14/2025 | 70 | - | - |
| 624 | 9/15/2025 | 71 | - | - |
| 625 | 9/16/2025 | 17 | - | - |
| 626 | 9/17/2025 | 3 | - | - |
| 627 | 9/18/2025 | 0 | - | - |
| 628 | 9/19/2025 | 32 | - | - |
| 629 | 9/20/2025 | 4 | - | - |
| 630 | 9/21/2025 | 15 | - | - |
| 631 | 9/22/2025 | 0 | - | - |

Apply dataset example — two groups

Suppose you have a time series model configured as follows:

- Target: Sales
- Date index: Date
- Time step: 1 day
- Store and Product are groups. In this context, Store is the primary group and Product is the secondary group.
- Forecast window of 3 days and forecast gap of 1 day. Therefore, the forecast horizon is 4 days.
- Forecast cutoff time of September 1, 2025. This is the last date for which historical data was provided.
- A past covariate Transactions Per Hour that tracks the average number of transactions that take place per hour, for each store and product.
- A future covariate On Promotion that tracks how many products are discounted at promotional rates for the specified date, for each store and product.

In this example, it is assumed that the system-defined apply window is 12 days. In addition to 12 days of historical data (August 21 to September 1, 2025), the dataset provides future covariate data for the 4-day forecast horizon (September 2 to 5, 2025).

Full example of apply dataset for model trained with two groups

| Date | Store | Product | On Promotion | Transactions per Hour | Sales |
| --- | --- | --- | --- | --- | --- |
| 8/21/2025 | Store 1 | A | 0 | 343 | 90010.01 |
| 8/21/2025 | Store 2 | A | 100 | 545 | 19491.65 |
| 8/21/2025 | Store 3 | A | 0 | 1004 | 70001.87 |
| 8/21/2025 | Store 1 | B | 14 | 305 | 39522.11 |
| 8/21/2025 | Store 2 | B | 55 | 700 | 91859.30 |
| 8/21/2025 | Store 3 | B | 2 | 94 | 19583.55 |
| 8/21/2025 | Store 1 | C | 1341 | 267 | 194863.00 |
| 8/21/2025 | Store 2 | C | 0 | 630 | 140244.13 |
| 8/21/2025 | Store 3 | C | 0 | 1143 | 76666.66 |
| 8/22/2025 | Store 1 | A | 56 | 576 | 30593.55 |
| 8/22/2025 | Store 2 | A | 3 | 403 | 10549.33 |
| 8/22/2025 | Store 3 | A | 14 | 1303 | 100003.33 |
| 8/22/2025 | Store 1 | B | 29 | 593 | 105893.99 |
| 8/22/2025 | Store 2 | B | 100 | 305 | 80195.22 |
| 8/22/2025 | Store 3 | B | 0 | 305 | 61051.13 |
| 8/22/2025 | Store 1 | C | 5 | 105 | 55938.38 |
| 8/22/2025 | Store 2 | C | 33 | 72 | 104823.33 |
| 8/22/2025 | Store 3 | C | 15 | 1052 | 99105.99 |
| 8/23/2025 | Store 1 | A | 5 | 521 | 130533.31 |
| 8/23/2025 | Store 2 | A | 1 | 205 | 67676.73 |
| 8/23/2025 | Store 3 | A | 36 | 302 | 52745.45 |
| 8/23/2025 | Store 1 | B | 111 | 502 | 99642.10 |
| 8/23/2025 | Store 2 | B | 350 | 693 | 34660.34 |
| 8/23/2025 | Store 3 | B | 34 | 200 | 60345.44 |
| 8/23/2025 | Store 1 | C | 93 | 205 | 44603.33 |
| 8/23/2025 | Store 2 | C | 60 | 295 | 105844.44 |
| 8/23/2025 | Store 3 | C | 10 | 76 | 150385.44 |
| 8/24/2025 | Store 1 | A | 402 | 473 | 80195.22 |
| 8/24/2025 | Store 2 | A | 15 | 1058 | 61051.13 |
| 8/24/2025 | Store 3 | A | 20 | 402 | 55938.38 |
| 8/24/2025 | Store 1 | B | 20 | 191 | 104823.33 |
| 8/24/2025 | Store 2 | B | 39 | 100 | 11111.12 |
| 8/24/2025 | Store 3 | B | 109 | 190 | 15493.33 |
| 8/24/2025 | Store 1 | C | 37 | 99 | 159334.14 |
| 8/24/2025 | Store 2 | C | 75 | 1555 | 45603.39 |
| 8/24/2025 | Store 3 | C | 190 | 1603 | 19491.65 |
| 8/25/2025 | Store 1 | A | 0 | 403 | 70001.87 |
| 8/25/2025 | Store 2 | A | 32 | 430 | 45642.25 |
| 8/25/2025 | Store 3 | A | 436 | 1000 | 25633.19 |
| 8/25/2025 | Store 1 | B | 1 | 1532 | 19191.31 |
| 8/25/2025 | Store 2 | B | 40 | 99 | 90010.01 |
| 8/25/2025 | Store 3 | B | 42 | 1058 | 19491.65 |
| 8/25/2025 | Store 1 | C | 25 | 734 | 70001.87 |
| 8/25/2025 | Store 2 | C | 1 | 569 | 39522.11 |
| 8/25/2025 | Store 3 | C | 305 | 692 | 91859.30 |
| 8/26/2025 | Store 1 | A | 11 | 164 | 19583.55 |
| 8/26/2025 | Store 2 | A | 60 | 205 | 194863.00 |
| 8/26/2025 | Store 3 | A | 70 | 186 | 140244.13 |
| 8/26/2025 | Store 1 | B | 25 | 1483 | 76666.66 |
| 8/26/2025 | Store 2 | B | 30 | 999 | 30593.55 |
| 8/26/2025 | Store 3 | B | 30 | 1533 | 10549.33 |
| 8/26/2025 | Store 1 | C | 30 | 1583 | 100003.33 |
| 8/26/2025 | Store 2 | C | 0 | 350 | 105893.99 |
| 8/26/2025 | Store 3 | C | 33 | 1509 | 80195.22 |
| 8/27/2025 | Store 1 | A | 145 | 74 | 61051.13 |
| 8/27/2025 | Store 2 | A | 33 | 140 | 55938.38 |
| 8/27/2025 | Store 3 | A | 59 | 884 | 104823.33 |
| 8/27/2025 | Store 1 | B | 65 | 239 | 99105.99 |
| 8/27/2025 | Store 2 | B | 16 | 502 | 130533.31 |
| 8/27/2025 | Store 3 | B | 17 | 158 | 67676.73 |
| 8/27/2025 | Store 1 | C | 15 | 1693 | 52745.45 |
| 8/27/2025 | Store 2 | C | 36 | 1544 | 99642.10 |
| 8/27/2025 | Store 3 | C | 62 | 1999 | 34660.34 |
| 8/28/2025 | Store 1 | A | 45 | 343 | 60345.44 |
| 8/28/2025 | Store 2 | A | 32 | 545 | 44603.33 |
| 8/28/2025 | Store 3 | A | 52 | 1004 | 105844.44 |
| 8/28/2025 | Store 1 | B | 10 | 305 | 150385.44 |
| 8/28/2025 | Store 2 | B | 0 | 700 | 40963.10 |
| 8/28/2025 | Store 3 | B | 13 | 94 | 159383.33 |
| 8/28/2025 | Store 1 | C | 99 | 267 | 80119.11 |
| 8/28/2025 | Store 2 | C | 14 | 630 | 106020.00 |
| 8/28/2025 | Store 3 | C | 56 | 1143 | 39581.34 |
| 8/29/2025 | Store 1 | A | 32 | 576 | 76939.23 |
| 8/29/2025 | Store 2 | A | 13 | 403 | 49548.42 |
| 8/29/2025 | Store 3 | A | 15 | 1303 | 93150.77 |
| 8/29/2025 | Store 1 | B | 70 | 593 | 15923.49 |
| 8/29/2025 | Store 2 | B | 71 | 305 | 159342.05 |
| 8/29/2025 | Store 3 | B | 17 | 305 | 20451.33 |
| 8/29/2025 | Store 1 | C | 3 | 105 | 150314.44 |
| 8/29/2025 | Store 2 | C | 0 | 72 | 15923.91 |
| 8/29/2025 | Store 3 | C | 32 | 1052 | 15944.10 |
| 8/30/2025 | Store 1 | A | 4 | 521 | 60000.01 |
| 8/30/2025 | Store 2 | A | 15 | 205 | 39583.55 |
| 8/30/2025 | Store 3 | A | 0 | 302 | 150333.65 |
| 8/30/2025 | Store 1 | B | 15 | 502 | 124594.13 |
| 8/30/2025 | Store 2 | B | 20 | 693 | 59303.13 |
| 8/30/2025 | Store 3 | B | 20 | 200 | 150333.31 |
| 8/30/2025 | Store 1 | C | 39 | 205 | 103483.53 |
| 8/30/2025 | Store 2 | C | 109 | 295 | 105038.13 |
| 8/30/2025 | Store 3 | C | 37 | 76 | 201857.11 |
| 8/31/2025 | Store 1 | A | 75 | 1058 | 35439.33 |
| 8/31/2025 | Store 2 | A | 190 | 402 | 51956.24 |
| 8/31/2025 | Store 3 | A | 0 | 191 | 55334.30 |
| 8/31/2025 | Store 1 | B | 0 | 100 | 11111.12 |
| 8/31/2025 | Store 2 | B | 100 | 190 | 15493.33 |
| 8/31/2025 | Store 3 | B | 0 | 99 | 159334.14 |
| 8/31/2025 | Store 1 | C | 14 | 1555 | 45603.39 |
| 8/31/2025 | Store 2 | C | 55 | 1603 | 46593.34 |
| 8/31/2025 | Store 3 | C | 2 | 403 | 74747.74 |
| 9/1/2025 | Store 1 | A | 1341 | 158 | 45491.34 |
| 9/1/2025 | Store 2 | A | 0 | 1693 | 34503.11 |
| 9/1/2025 | Store 3 | A | 0 | 1544 | 159334.13 |
| 9/1/2025 | Store 1 | B | 56 | 1999 | 193803.15 |
| 9/1/2025 | Store 2 | B | 3 | 343 | 76666.66 |
| 9/1/2025 | Store 3 | B | 14 | 545 | 30593.55 |
| 9/1/2025 | Store 1 | C | 29 | 303 | 10549.33 |
| 9/1/2025 | Store 2 | C | 100 | 154 | 100003.33 |
| 9/1/2025 | Store 3 | C | 0 | 531 | 34351.42 |
| 9/2/2025 | Store 1 | A | 5 | - | - |
| 9/2/2025 | Store 2 | A | 33 | - | - |
| 9/2/2025 | Store 3 | A | 15 | - | - |
| 9/2/2025 | Store 1 | B | 5 | - | - |
| 9/2/2025 | Store 2 | B | 1 | - | - |
| 9/2/2025 | Store 3 | B | 36 | - | - |
| 9/2/2025 | Store 1 | C | 111 | - | - |
| 9/2/2025 | Store 2 | C | 350 | - | - |
| 9/2/2025 | Store 3 | C | 34 | - | - |
| 9/3/2025 | Store 1 | A | 93 | - | - |
| 9/3/2025 | Store 2 | A | 60 | - | - |
| 9/3/2025 | Store 3 | A | 10 | - | - |
| 9/3/2025 | Store 1 | B | 465 | - | - |
| 9/3/2025 | Store 2 | B | 22 | - | - |
| 9/3/2025 | Store 3 | B | 249 | - | - |
| 9/3/2025 | Store 1 | C | 50 | - | - |
| 9/3/2025 | Store 2 | C | 15 | - | - |
| 9/3/2025 | Store 3 | C | 25 | - | - |
| 9/4/2025 | Store 1 | A | 1 | - | - |
| 9/4/2025 | Store 2 | A | 0 | - | - |
| 9/4/2025 | Store 3 | A | 112 | - | - |
| 9/4/2025 | Store 1 | B | 50 | - | - |
| 9/4/2025 | Store 2 | B | 75 | - | - |
| 9/4/2025 | Store 3 | B | 130 | - | - |
| 9/4/2025 | Store 1 | C | 139 | - | - |
| 9/4/2025 | Store 2 | C | 136 | - | - |
| 9/4/2025 | Store 3 | C | 168 | - | - |
| 9/5/2025 | Store 1 | A | 155 | - | - |
| 9/5/2025 | Store 2 | A | 73 | - | - |
| 9/5/2025 | Store 3 | A | 19 | - | - |
| 9/5/2025 | Store 1 | B | 103 | - | - |
| 9/5/2025 | Store 2 | B | 54 | - | - |
| 9/5/2025 | Store 3 | B | 23 | - | - |
| 9/5/2025 | Store 1 | C | 24 | - | - |
| 9/5/2025 | Store 2 | C | 134 | - | - |
| 9/5/2025 | Store 3 | C | 193 | - | - |
