---
title: "Predicting with the time series deployment"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/time-series-tutorial-predict.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Tutorial – Predicting sales with multivariate time series forecasting"]
---

# Predicting with the time series deployment

After you have deployed and approved your time series model, you can create time-specific forecasts. In this tutorial, we create a prediction configuration within the ML deployment and use it to run a [batch prediction](#glossary-0 "Glossary term").

So far, we have used daily sales data to create a machine learning model. The goal with this process has been to recognize patterns through machine learning, with the goal of applying them to new data.

## Understanding predictions with time series models

It is important to distinguish between how predictions work for time series models, since it is different from predictions for other model types. The steps you complete to prepare your apply dataset are different from the steps for other model types.

With time series models, new predictions are added as new rows rather than being added as a separate column.

## Creating an apply dataset

This section outlines how you can create your apply dataset for this time series problem. The actual process of compiling the dataset rows is not shown, but the workflow is.

Linear diagram outlining the needed components, and timeline, of an apply dataset that is used to generate predictions with a time series forecasting model.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/concept_ml-time-series-forecast-apply-data.png "Click to view full size")

### Column structure

Your apply dataset needs to contain the same schema as the time series model you deployed. The schema can be found when you open the ML deployment.

In any case, the apply dataset should include the same columns as the model schema — in other words, a column for each of the following:

- Date index
- Target
- Groups
- Features (covariates)

### Row structure

Your dataset needs to contain records (rows) as follows:

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

### Other modifications

You might need to make other modifications to the dataset so that it matches the model schema. In particular, grouped features, when selected as groups during training, are automatically transformed to the categorical feature type so that they can be used as groups. In your apply data, if you have features containing numeric data that you are using as groups, you will need to transform their data type so that it is identified as categorical data. An example of this is shown in [*Preparing the dataset*](#Preparing).

### Preparing the dataset

This tutorial provides an apply dataset that has already been configured with the required columns and records. However, the provided apply dataset contains a numeric column, store\_nbr, that was configured as a group in the model. So, you need to create a script to transform this column to string data.

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-1 "Glossary term") and select Script.
2. Enter a name for your script, for example, Transformed apply data.
3. Choose a space for your script. It needs to be the same space where you stored the original apply dataset.
4. Click Create.
5. In Script, switch to Editor.
6. Under Sections, click ![Create new section](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) to add a new section.
7. Paste the load script below into the editor.
8. Click Export data.

Load script

```
ApplyDataset_Transformed:

LOAD
    id,
    "date",
    text(store_nbr) as store_nbr,
    family,
    sales,
    onpromotion
FROM [lib://:DataFiles/ML - Multivariate forecasting - apply.csv]
(txt, codepage is 28591, embedded labels, delimiter is ',', msq);

Store [ApplyDataset_Transformed] into [lib://:DataFiles/Final transformed apply dataset.qvd](QVD);
```

Running the script to export a new version of the apply dataset to Qlik Cloud Analytics.

![Script editor with load script pasted into editor and 'Export data' button highlighted](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ml_time-series-run-script.png "Click to view full size")

After the script runs, a new apply dataset,  Final transformed apply dataset.qvd, should be located in the same space as the original apply dataset.

## Creating predictions

Now that you have a compatible apply dataset, use it to create predictions from your ML deployment.

Do the following:

1. In the catalog, open the Sales forecasting deployment deployment you created in [*Deploying a time series model*](time-series-tutorial-deploy.htm).
2. In the bottom right corner, click Create prediction.
3. In the Prediction configuration pane on the right side, under Apply data, click Select apply dataset.
4. Select the [apply dataset](#glossary-2 "Glossary term") file:  Final transformed apply dataset.qvd.
5. Compare the schemas of the [training](#glossary-3 "Glossary term") and apply datasets. There should not be any schema mismatch errors.
6. In the Prediction configuration pane, click Name prediction dataset. Type the following name: ML - Sales predictions. Use the default Parquet format.
7. Select a space and click Confirm.

Prediction configuration showing schema comparisons and configuration panel.

![ML deployment with time series model, showing the prediction configuration with schemas](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ml-time-series-tutorial-deployment-predictions.png "Click to view full size")

Click the ![Down arrow](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dropdown_arrow.svg) icon next to Save and close. Select Save and predict now.

The process can be monitored in Dataset predictions. You can review the output in the catalog by clicking Open in the popup that appears.

When the prediction has finished running, create an application to view your predictions. Move to the next topic.
