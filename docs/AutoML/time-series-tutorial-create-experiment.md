---
title: "Creating and configuring the time series experiment"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/time-series-tutorial-create-experiment.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Tutorial – Predicting sales with multivariate time series forecasting"]
---

# Creating and configuring the time series experiment

The first step is to create and configure a time series experiment. You will use the training dataset you uploaded earlier to train the model until it is ready to be deployed for making predictions.

## Creating a new experiment

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-0 "Glossary term") and select ML experiment.
2. Enter a name for your experiment, for example, Sales forecasts.
3. Optionally, add a description and tags.
4. Choose a space for your experiment. It can be your personal space or a shared space.
5. Click Create.
6. Select the training dataset file  ML - Multivariate forecasting - training.csv.

ML experiment with time series training dataset selected.

![Schema view in new ML experiment with time series training dataset selected](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ml_time-series-tutorial-experiment.png "Click to view full size")

## Configuring time series forecasting settings

### Step 1: Select target

Start by defining a target column. We want to forecast future sales, so select that column as the target.

Do the following:

- In ![Table rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view, click the radio button next to sales. A target ![Target](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_target.svg) icon replaces the button.

Selecting the target column for the time series experiment.

![Selecting the target column for the time series experiment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ml_time-series-tutorial-exp-target.png "Click to view full size")

### Step 2: Configure the experiment to be a time series experiment

Do the following:

1. In the experiment configuration panel, expand Experiment settings.
2. Under Experiment type, select Time series. This option only appears after selecting a high-cardinality numeric column.

### Step 3: Select a date index

Next, you need to select the time series index column to use.

Do the following:

1. A new section, Time series settings, appears in the configuration panel. Under Date index, click the drop down menu to expand it.
2. Select date.

Experiment configuration panel with Time series selected as experiment type and date selected as the date index column.

![Selecting the experiment type and date index for the experiment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ml_time-series-tutorial-exp-type.png "Click to view full size")

### Step 4: Set the forecast window and gap

After you select your date index, some new information appears in the panel.

Go to the Based on your data section. This section outlines the time range of your historical data and allows you to configure the range of future dates for which you want predictions.

The Estimated maximum forecast is 180 days. This estimate is based on the available historical data, where the forecast window is a fraction of the total historical data available. It represents the maximum number of future time steps (in this case, days) for which you are estimated to be able to predict the target. After running a version of the training, more information will be known and this estimate will be replaced by a definitive maximum forecast.

The Desired forecast window size sets how many time steps into the future you want to predict. For example, in this tutorial, setting the forecast window to 7 would indicate that the model is to predict a week of future target dates.

The Forecast gap size sets the number of time steps immediately after the end of your training data for which you do not want predictions. For example, you might only want to predict sales for dates three or more days into the future.

Do the following:

1. In the Based on your data section, set the Desired forecast window size to 7 time steps.
2. Set the Desired forecast gap size to 3 time steps.

Information noteThe forecast horizon is the forecast window plus the forecast gap size, measured in time steps. In this case, the forecast horizon is 10, which indicates that at prediction time, you are forecasting 10 time steps ahead, even though no actual values may have been recorded for that prediction gap.

### Step 4: Select groups

The training dataset for this tutorial is designed for multivariate forecasting. With multivariate forecasting, the goal is to predict target values alongside other dimensions that vary directly alongside the target. For instance, in this tutorial, the data contains sales metrics tracked individually for each store and product family. Multivariate forecasting allows you to combine each of these dimensions — which might otherwise need to be trained as separate models — into a single experiment, allowing models to learn more about patterns and interactions between different cohorts of data.

You configure multivariate experiments by selecting up to two columns from the training data to use as groups.

The goal of this tutorial is to train models to learn and predict sales alongside store number and product family, so select these two columns as groups.

Do the following:

- Select store\_nbr and family as Groups.

Information note If no group is explicitly selected, the model will automatically search for a suitable grouping using only categorical features. Once a valid group is identified, the process proceeds to training. Therefore, if we want the system to automatically detect store\_nbr as a valid group column, it must be marked as a categorical feature.

### Step 5: Configure covariates (features)

The terms "covariate" and "feature" are often used synonymously in machine learning, but in time series forecasting in Qlik Predict, the term "covariate" is commonly used and more descriptive. In a multivariate time series model, there are three types of covariates: static, past, and future.

Static and past covariates are among the Features that you include in the experiment training, other than the groups, date index, and future features. Static and past covariates are identified automatically by the system. You do not need to configure these beyond including them as features (and avoiding configuring them as future features).

Future covariates, or future features, also refer to Features you include in training. Future covariates are features that have future data that you will know in advance—in particular, you have access to future values for this feature spanning your selected [forecast horizon](machine-learning-framework-time-series.htm#ForecastHorizon). For future features, you also need to know the data values for the historical time range on which the model is trained.

In addition to including a future feature in the list of training Features, you also need to configure it as a future feature in the training configuration panel. At prediction time, the model will expect future feature data spanning the forecast horizon in order to generate accurate forecasts.

In the training data, the onpromotion feature tracks how many products are discounted at promotional rates for the specified date. This is information that is known ahead of time, and there is future data available for it, so it can be used as a future feature.

Do the following:

- Below the Groups drop down, expand Future features and select onpromotion.

To summarize:

- onpromotion has been selected as a future feature.
- Other than the date index, no other covariates were selected for the training.

Experiment configuration panel showing configured groups, future feature, and a summary of all selected features.

![Experiment configuration panel showing configured groups, future feature, and a summary of all selected features.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ml_time-series-tutorial-forecast-groups-future.png "Click to view full size")

The following diagram illustrates time series forecasting concepts and how they relate to the experiment configuration. For more information about time series forecasting concepts, see [*Working with multivariate time series forecasting*](machine-learning-framework-time-series.htm).

Simplified illustration outlining the components of a time series forecasting problem in Qlik Predict.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/concept_ml-time-series-forecast-simple.png "Click to view full size")

## Confirming other settings

Now that you have completed the time series configurations, review the remaining training settings in the configuration panel.

- Under Features, you can see that four features are selected.
- Under Algorithms, you can see that all available algorithms are selected.

## Training the experiment

The configuration is done and we are ready to start the training.

Do the following:

- Click Run experiment.

When the experiment has finished running, we can move on to the next step, which is to review the resulting model metrics.
