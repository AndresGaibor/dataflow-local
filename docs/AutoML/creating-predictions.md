---
title: "Creating predictions on datasets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/creating-predictions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML predictions"]
---

# Creating predictions on datasets

Use your ML deployment to predict future outcomes on new data. With [batch predictions](#glossary-0 "Glossary term"), you create prediction configurations within your ML deployment and then use them to generate predictions as datasets. In the generated datasets, each row contains a predicted value for that specific row. With batch predictions, you generate a prediction for each row in your apply dataset.

To start creating prediction configurations, open an ML deployment and go to the Batch predictions pane. See [*Navigating the ML deployment interface*](ml-model-management.htm).

With batch predictions, you can make predictions on datasets in the catalog, for example, daily predictions on new transactions. Alternatively, predictions can also be made in real time using the real-time prediction endpoint in the Machine Learning API. For information about real-time predictions, see [*Creating real-time predictions*](creating-real-time-predictions.htm).

Information note

The real-time predictions API is deprecated and replaced by the real-time prediction endpoint in the [Machine Learning API](https://qlik.dev/apis/rest/ml/). The functionality itself is not being deprecated. For future real-time predictions, use the real-time prediction endpoint in the Machine Learning API. For help with migrating from the real-time predictions API to the Machine Learning API, refer to [the migration guide on the Qlik Cloud developer portal](https://qlik.dev/apis/rest/automl-deployments/#migrate-from-the-automl-real-time-predictions-api-to-the-machine-learning-api).

Batch predictions are generated in a dataset with predictions and—for classification models—a column with the probability of each class. Optionally, you can also generate datasets with SHAP values or errors, and a copy of the [apply dataset](#glossary-1 "Glossary term"). The datasets can be in Parquet, CSV, or QVD format.

When predictions are generated, you can load the predictive insights into a Qlik Sense application. This lets you visualize and interact with the data and create what-if scenarios.

## Requirements and permissions

For information about the required space roles for working with deployments and predictions in shared and managed spaces, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](../Spaces/permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](../Spaces/permissions-managed-space-admin.htm)

If you are an administrator, see [*Who can work with Qlik Predict*](who-can-work-with-automl.htm) for a comprehensive overview of the required user permissions for working with deployments and predictions.

## Creating new batch predictions

You can create new prediction configurations from the Deployment overview, Deployable models, or Batch predictions pane.

Do the following:

1. Open an ML deployment from the catalog.
2. In the bottom right, click Create prediction.
3. In the Apply dataset schema section, click Select apply dataset.
4. Select a dataset to generate predictions for, or click Add apply dataset to upload a new dataset. For more information about adding data files in Qlik Cloud Analytics, see [*Adding datasets*](../DataSource/add-datasets.htm).

   Information noteAt this stage, you are notified if the apply dataset schema does not match the model schema. For predictions to run successfully, the schemas must have the same features and data types.
5. You can optionally name your prediction configuration, and add a description. In the Prediction configuration pane on the right, under Prediction name, edit the Name and Description.
6. By default, your prediction configuration is set to generate predictions using the default model in the deployment. You can alternatively choose to run the predictions from a different model, using an [alias](#glossary-2 "Glossary term"). In the Prediction configuration pane, expand Choose model alias and select the alias to use.

   For more information about using aliases in batch predictions, see [*Configuring model aliases for batch predictions*](alias-predictions-batch.htm).
7. In the Prediction configuration pane, under Prediction dataset (output), click Name prediction dataset.
8. As needed, edit the path within the space where you want to store the datasets, including folders and a file name. Separate folders with / characters.

   Qlik Predict also supports dynamic naming for prediction output. For more information, see [*Dynamic naming and storage for batch predictions*](automl-dynamic-naming-predictions.htm).
9. Select a format for the generated datasets. The default is Parquet. Datasets can also be generated in CSV or QVD format.
10. Select a space.
11. Click Confirm.
12. Under Prediction options, select any additional datasets that you want to generate.

    - Apply dataset: Generate a copy of the apply dataset being used for the predictions. For time series models, this copy of the apply dataset will only contain the records in the apply window—that is, the records used to generate the predictions.
    - Errors dataset: Generate a dataset with errors for records in the apply dataset. This lets you know if a record was dropped and for what reason. Not available for time series models.
    - SHAP: Generate a dataset with SHAP values for each record. The dataset has the columns index and <feature>\_SHAP for each feature in the model. Not available for time series models.

      Information noteThis option is not available for predictions from multiclass classification models. For these models, you can use the Coordinate SHAP option instead.
    - Coordinate SHAP: Generate a dataset with SHAP values for each record. This gives you the same values as the SHAP dataset but organized in a different way. The dataset has the columns index, automl\_feature, and SHAP\_value. An additional column, Predicted\_class, is included with predictions from a multiclass classification model. Not available for time series models.
13. As needed, edit the path within the space where you want to store each of the above datasets. The path includes folders and a file name. Separate folders with / characters.

    Qlik Predict also supports dynamic naming for prediction output. For more information, see [*Dynamic naming and storage for batch predictions*](automl-dynamic-naming-predictions.htm).
14. Under Index column, choose whether to autogenerate an index column or use an existing column in the apply dataset. Not available for time series models.
15. You might also like to run your predictions on a schedule. Under Prediction schedule, click Create schedule and adjust the settings in the dialog that appears. For more information, see [*Scheduling predictions*](#Schedule).
16. Click the Save and close button to save your prediction configuration and return to the Batch predictions pane without running the prediction. You might prefer this option if you only want the predictions to run on a schedule.

    Alternatively, click the ![Down arrow](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dropdown_arrow.svg) icon next to Save and close. Select Save and predict now. This saves the prediction configuration and manually runs the prediction.

    When Last run shows ![Checkbox](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_success_outline.svg), the predictions finished successfully.
17. Go to the catalog to see the generated datasets.

## Editing prediction configurations

You can edit existing prediction configurations from the Batch predictions pane.

Do the following:

1. In the Batch predictions pane, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the prediction configuration to edit.
2. Select Edit prediction configuration from the Actions menu.

   The prediction configuration opens, with the model and apply dataset schemas shown in the center of the screen.
3. In the Prediction configuration pane, you can edit the following sections:

   - Prediction name: Change the name and description of the prediction configuration.
   - Owner: Make yourself the owner of the prediction configuration. For information about when this might be needed, see [*Prediction configuration ownership*](#Ownership).
   - Choose model alias: Change the model alias used for predictions.
   - Apply data (input): You can change the apply dataset.  For time series models, this copy of the apply dataset will only contain the records in the apply window—that is, the records used to generate the predictions.
   - Prediction dataset (output): You can change the name and space of the prediction dataset.
   - Prediction options: You can change your selections for the additional datasets that are generated, or change their names and folder locations.
   - Prediction schedule: If you wish, you can set the schedule on which your prediction will be run. For more information, see [*Scheduling predictions*](#Schedule).
4. Click the Save and close button to save your prediction configuration and return to the Batch predictions pane without running the prediction.

   Alternatively, click the ![Down arrow](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dropdown_arrow.svg) icon next to Save and close. Select Save and predict now. This saves the prediction configuration and manually runs the prediction.

   When Last status shows "Success", the predictions are finished.

## Running batch predictions

You can run predictions for existing prediction configurations from the Batch predictions pane. Alternatively, you might want to run your predictions according to a customizable schedule. You can combine manual and scheduled runs of your predictions to best suit your needs.

### Running predictions manually

You can start running a prediction configuration directly by selecting the option within a context menu in the Batch predictions pane.

For a user to run a prediction manually, that user must meet the access requirements for the action. See [*Prediction configuration ownership*](#Ownership).

Do the following:

1. In the Batch predictions pane, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg)on the prediction configuration to use for predictions.
2. Select Run predictions now from the Actions menu to start generating predictions.

   When Last status shows "Success", the predictions are finished.

### Scheduling predictions

Predictions can be set to run automatically on a schedule. You can create one schedule for each prediction configuration that you create. Access the Prediction schedule menu when creating or editing a prediction configuration.

For a scheduled prediction to run successfully, the owner of the prediction configuration ownership must meet several permission requirements. Otherwise, the prediction cannot run. For more information, see [*Prediction configuration ownership*](#Ownership).

The Prediction schedule dialog allows you to specify the following parameters for your schedule:

- Run predictions: Adjust the general schedule on which the prediction will run (daily, weekly, or monthly). Set the interval, day of the week, or day of the month depending on your selection.
- Time: Configure the time of day at which your prediction will start running.

  If you are scheduling by the hour (for daily or weekly predictions), you will also be able to specify a start and end time between which the predictions will run.
- Start date: Set the date on which the prediction schedule takes effect.
- End date: Set the date on which the predictions will stop being run on the schedule. By default, the schedule will be set to continue running indefinitely, but you can specify an end date for the schedule.
- Only run if apply dataset has changed: If any of the following events occurs, the scheduled prediction will run. Otherwise, the scheduled prediction will not run.

  - A change is detected in the apply dataset.
  - The model used in the batch prediction has changed, either by a change in the model assigned to the current alias or a change to a different alias that uses a different model.

## Deleting prediction configurations

You can delete existing prediction configurations from the Batch predictions pane.

Do the following:

1. In the Batch predictions pane, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the prediction configuration to delete.
2. Select Delete prediction configuration from the Actions menu.
3. Click Delete to confirm.

## Key concepts

### Apply dataset

During experiment training, you deploy a model that is used to generate predictions on a new dataset. This dataset is known as the apply dataset. The predictions are generated in a dataset with predictions and—for classification models—a column with the probability of each class. Optionally, you can also generate datasets with SHAP values or errors.

Information note

Any flat file that can be uploaded and profiled in Qlik Cloud is supported for use in Qlik Predict.

For multi-table files such as Microsoft Excel files with multiple sheets, only the first table will be imported. If data profiling fails for a table (for example, if it is empty), the file is not supported.

Requirements for the apply dataset are different depending on your model type:

- For classification and regression models, the apply dataset must have the same features and data types as the dataset used to train the ML deployment. The target column specified in the ML experiment does not need to be included in the apply dataset.
  Note that additional columns that were not part of the model training can still be present in the apply dataset. Qlik Predict will simply ignore the additional columns when generating predictions.
- For time series models, predictions are created as rows rather than columns. The predictions are still being generated for a target column, but they are records corresponding to specific future time values. The structure of the columns does not change between the training and apply datasets. The apply dataset for a time series model needs to contain historical data and placeholder values for the future records that you need to predict. For more information, see [*Preparing an apply dataset*](machine-learning-framework-time-series.htm#ApplyPrepare) and [*Working with predictions for time series models*](time-series-prediction.htm).

### Prediction configuration

Prediction datasets are generated from a prediction configuration. Each ML deployment can have multiple prediction configurations. The prediction configuration can be set to run with or without a schedule.

#### Prediction configuration ownership

When a user creates a prediction configuration, they are automatically assigned as the owner.

It could happen that the owner of a prediction configuration loses access to the tenant, or no longer meets the other requirements for working with ML deployments. In this case, a user with the required permissions can click Make me the owner to take ownership of the scheduled prediction so that it can run. This is done in the prediction configuration pane, or as an action in the Dataset predictions window.

To make yourself the owner of a prediction configuration, you need:

For information about the required permissions to make yourself the owner of a prediction configuration, see [*Requirements and permissions*](#Requirem).

### Model activation

Before you can start generating predictions with your ML deployment, the source model needs to be activated. For more information, see [*Approving deployed models*](approve-models.htm).

### Automatic feature engineering

For information about generating predictions with models that were trained using automatic feature engineering, see [*Automatic feature engineering*](automatic-feature-engineering.htm).

## Considerations for apply datasets

### Impact of manually changing feature type

When you manually change the feature type of a feature, and then deploy a resulting model, the feature type overrides will be applied to the feature in the apply dataset that is used in predictions made with that model.

[*Changing feature types*](configuring-experiments.htm#Changing)

Information noteAn exception exists for time series models. See [*Changing feature types*](time-series-prediction.htm#Changing).

## Managing prediction jobs

Tenant admins can stop or cancel prediction jobs from the Administration activity center. For more information, see [*Administering Qlik Predict*](../Admin/mc-managing-experiments-deployments.htm).

## Configuring notifications

You can receive notifications when predictions are created from an ML deployment. For more information, see [*Configuring notifications for Qlik Predict*](automl-customize-experience.htm#Configur).

## Viewing data drift and prediction event details

After you run a prediction, switch to the Data drift monitoring and Operations monitoring panes to view details about:

- The level of data drift for each feature in the apply dataset. The comparison is performed between your apply dataset and the training dataset.
- Details about the prediction event, such as whether it succeeded or failed, and how many predictions it generated.

For more information, see [*Monitoring performance and usage of deployed models*](monitor-models.htm).

## Viewing lineage and impact analysis

Using the Lineage and Impact analysis tools in Qlik Cloud, you can analyze:

- The origins of prediction datasets and apply datasets. This can include the related training data, experiments, models, and ML deployments.

  [*Analyzing lineage for machine learning content*](../Catalog/lineage.htm#MLLineage)
- How prediction datasets and apply datasets are being used in downstream content across Qlik Cloud.

  [*Impact analysis for machine learning content*](../Catalog/impact-analysis2.htm#MLImpact)

## Learn more

- [*Navigating the ML deployment interface*](ml-model-management.htm)
