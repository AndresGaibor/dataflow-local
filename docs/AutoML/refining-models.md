---
title: "Refining models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/refining-models.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments"]
---

# Refining models

Once you have created some initial models, it is important to refine them to increase their effectiveness and potential accuracy. The model scores indicate different measures of this performance. While the goal of refining the models is to increase these scores, a higher score doesn't always indicate a better model.

You can refine your models by excluding or including features, changing the training data, and modifying other configuration parameters. In doing so, you can compare different versions to see what effect your changes have.

By interpreting the scores, you will learn how to refine the model. The values for the different metrics can give you insights about which actions to take to improve the outcome.

## Requirements and permissions

To learn more about the user requirements for working with ML experiments, see [*Working with experiments*](working-with-experiments.htm).

## Configuring a new version

After you have run an experiment version, you can refine your models if needed by creating a new version.

Do the following:

1. From the Training data, Models, or Analyze tab, select the model to use as the basis for the next version.
2. Click View configuration.

   The experiment configuration panel opens.
3. Click Create new version.

Tip noteAlternatively, in the Models tab, under Model metrics, switch to the ![By version](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tree_view.svg) ("by version") view. Next to the version, click ![Vertical context menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical_outline.svg) > New version.

After you create a new version, you can make changes to its configuration, such as:

- Excluding existing features
- Including previously excluded features
- Changing or refreshing the dataset
- Selecting or deselecting algorithms

More information about these options is provided in the sections below.

When drafting a new version, click the filter ![Filter](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filter2.svg) icon under Features in the experiment configuration panel. When filtering, you can more easily visualize which features have been introduced since you changed the training dataset. You can also see which features are auto-engineered and non-engineered.

## Improving the dataset

If your model doesn't score well, you might want to review the dataset to address any issues. Read more about how to improve the dataset in [*Getting your dataset ready for training*](dataset-preparation.htm).

### Excluding features

More features do not necessarily make a better model. To refine the model, you want to exclude unreliable and irrelevant features such as:

- Features with too high correlation. From two correlated features, exclude the one with less feature importance.
- Features with too low feature importance. Those features don't provide any influence on what you’re trying to learn about.
- Features with too high feature importance. It might be due to data leakage.

Test to remove the feature from the training data, then run the training again and check if this improves the model. Does it make a big difference or none to the model score?

Do the following:

1. Open an experiment from the catalog.
2. From the Training data, Models, or Analyze tab, select the model to use as the basis for the next version.
3. Click View configuration.

   The experiment configuration panel opens.
4. Click Create new version to configure a new experiment version.
5. Under Features, clear the checkboxes for any feature that you don’t want to use in the training.

Tip noteAlternatively, you can deselect features from the schema or data views. Switch to the Training data tab in the experiment, then click ![Schema view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view or ![Data view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_profile.svg) Data view.

### Adding features

If your model still isn’t scoring well, it could be because the features that have a relationship with the target are not yet captured in the dataset. You can re-process and re-purpose your dataset to optimize the data quality, and to add new features and information. When ready, the new dataset can be added to future experiment versions. See [*Changing and refreshing the dataset*](#Changing).

Read more about how to capture or engineer new features in [*Creating new feature columns*](feature-engineering.htm).

## Changing bias detection settings

You can change the features on which bias detection is set to run. For example, if you have added new features to the dataset, you can turn on bias detection for these features.

Do the following:

1. Open an experiment from the catalog.
2. From the Training data, Models, or Analyze tab, select the model to use as the basis for the next version.
3. Click View configuration.

   The experiment configuration panel opens.
4. Click Create new version to configure a new experiment version.
5. Expand Bias in the training configuration panel.
6. Optionally click Get recommendations to use generative AI to suggest features that could contain biased data. See [*Using generative AI to recommend features for bias detection*](bias-detection.htm#UsingAI).
7. Select or deselect any features for which you want to run bias detection.

Alternatively, set bias detection settings in ![Rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view.

For more information about bias detection, see [*Detecting bias in machine learning models*](bias-detection.htm).

## Selecting algorithms

Based on the data type of your target column, suitable algorithms are automatically selected for training. You might want to exclude the algorithms that don't perform as well or are slower. This way you don't have to waste time on them for training.

For more information about how algorithms are chosen, see [*Understanding model algorithms*](algorithms.htm).

Do the following:

1. Open an experiment from Catalog.
2. From the Training data, Models, or Analyze tab, select the model to use as the basis for the next version.
3. Click View configuration.

   The experiment configuration panel opens.
4. Click Create new version to configure a new experiment version.
5. Under Algorithms, clear the checkboxes for any algorithms that you don’t want to use in the training.

## Changing and refreshing the dataset

If your training data has changed since the last experiment version, you can change or refresh the dataset for future versions of the experiment.

This might be helpful if you would like to compare model metrics and performance for different datasets within the same experiment. For example, this is helpful if:

- A new set of data records is available, or updates to the original set of data records were made. For example, the latest month's transactions might have become available and appropriate for use in training, or a data collection issue might have been identified and addressed.
- The original training dataset has been re-processed or re-purposed, perhaps with the intention of improving model training. For example, you might have improved the logic to define feature column values, or even added new feature columns.

Changing or refreshing the dataset does not alter existing models that have already been trained from previous experiment versions. Within an experiment version, the models are trained only on the training data defined within that specific version.

### Requirements

When you change or refresh the dataset for a new experiment version, the new dataset must meet the following requirements:

- The name and feature type of the target column needs to be the same as the target in the original training dataset.
- The number of distinct values in the target column must be within the same range as required for the given experiment type. For example, for a multiclass classification experiment, the target column in the new dataset must still have between three and ten unique values. For the specific ranges, see [*Configuring experiments*](configuring-experiments.htm#Determin).

The other feature columns can be entirely new, have different names, and contain different data.

### Changing the dataset

Do the following:

1. From the Training data, Models, or Analyze tab, select the model to use as the basis for the next version.
2. Click View configuration.

   The experiment configuration panel opens.
3. Click Create new version to configure a new experiment version.
4. Under Training data > Review dataset, click Change dataset.
5. Select or upload the new dataset. You can choose from:

   - Datasets: Select a dataset in any space you can access. See [*Tips and guidelines for uploading and selecting datasets*](#Tips).
   - Data products: Select a dataset from an active data product you can access. For more information about data products, see [*Creating data products*](../DataIntegration/DataProducts/Creating-data-products.htm).

### Refreshing the dataset

Do the following:

1. From the Training data, Models, or Analyze tab, select the model to use as the basis for the next version.
2. Click View configuration.

   The experiment configuration panel opens.
3. Click Create new version to configure a new experiment version.
4. Under Training data, click Refresh dataset.

   You are notified if a dataset refresh is available. A dataset typically refreshes when the existing data file is overwritten by the creation of a new file with the same name.

### Tips and guidelines for uploading and selecting datasets

- Datasets can be uploaded via the Create page in the Analytics activity center, and are visible in the catalog.
  You can also upload a new dataset directly into the catalog from the experiment's dataset selection page. To do so, click Upload file and choose the file to upload.
- Any flat file that can be uploaded and profiled in Qlik Cloud is supported for use in Qlik Predict.

  For multi-table files such as Microsoft Excel files with multiple sheets, only the first table will be imported. If data profiling fails for a table (for example, if it is empty), the file is not supported.

## Running the refined version

When you have finished configuring the version, you can run it.

Do the following:

- Click Run v2 in the bottom right corner of the screen.

  (The text on the button depends on the number of versions you have run.)

## Comparing experiment versions

After the new version has finished training, compare the new version with the old one to see the effect of your changes. You have a number of options for comparing models across experiment versions.

### Quick analysis

Use the Models and Training data tabs in the experiment to compare the version with older versions. In the Models tab, you can:

- View the results in the Model metrics table.
- View recommended models based on common predictive analytics requirements, including accuracy and prediction speed.
- Switch between models to view the differences in the Model training summary and other auto-generated charts.

For more information about quick model analysis, see [*Performing quick model analysis*](analyze-models-quick.htm).

### In-depth analysis

You can dive deeper into your model analysis by switching to the Compare and Analyze tabs in the experiment. These tabs offer an embedded analytics experience where you can interactively evaluate the models at a more granular level.

The Compare tab offers comparison of model scores and hyperparameters across all models. The Analyze tab allows you to focus on a specific model to assess prediction accuracy, feature importance, and other details.

For more information, see [*Comparing models*](analyze-models-compare.htm) and [*Performing detailed model analysis*](analyze-models-detailed.htm).

## Changing model optimization settings

You can turn off intelligent optimization after running a version in which it was activated. This allows you to use the insights provided from the intelligent optimization, while also giving you the needed control to do minor, minimal tweaks. Alternatively, you can turn intelligent model optimization on after running one or more versions with the setting turned off.

Hyperparameter optimization is a setting that can be helpful to turn on during the model refinement process. Generally, it is not recommended to have this setting turned on for the first version of the experiment.

You can also change whether or not to use time-aware training, or change the column used as the date index.

Do the following:

1. Click View configuration.
2. If needed, click Create new version to configure a new experiment version.
3. In the panel, expand Model optimization.
4. Switch between the Intelligent and Manual settings to turn intelligent model optimization on or off.
5. If you would like to activate hyperparameter optimization, click the Hyperparameter optimization checkbox and set a maximum training time.
6. Under Time-based test-train split, you can change the settings for time-aware training:

   1. To turn time-aware training on, change the default value of None by selecting a specific Date index column in the dataset.
   2. To turn time-aware training off, set the Date index to the value of None.
   3. Change the selected Date index column to a different column.

## Deleting experiment versions

You can delete experiment versions that you don't want to keep. Note that all models in the experiment versions will also be deleted and can't be recovered.

Do the following:

1. Switch to the Models tab.
2. In the Model metrics table, select a model from the experiment version you want to delete.

   Tip noteYou can also select a model when you are on the Training data or Analyze tabs, using the drop down menu in the toolbar.
3. In the top right, click Delete <version number>.
4. In the confirmation dialog, click Delete.

Alternatively, in Model metrics, switch to the ![By version](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tree_view.svg) ("by version") view. Next to the version, click ![Vertical context menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical_outline.svg) > Delete.
