---
title: "Configuring experiments"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/configuring-experiments.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments"]
---

# Configuring experiments

The configuration of experiments consists of selecting the target and the features that the model will use to predict the target. You can also configure a number of optional settings.

To support you in the selection of a target, the historical dataset is analyzed and summary statistics are displayed about each column in the dataset. Several automatic preprocessing steps are applied to the dataset to make sure that only suitable data is included. For more details on the data preprocessing, see [*Automatic data preparation and transformation*](preprocessing-steps.htm).

After running v1, you can create new experiment versions if needed to further refine the model training. For more information, see [*Refining models*](refining-models.htm).

## Requirements and permissions

To learn more about the user requirements for working with ML experiments, see [*Working with experiments*](working-with-experiments.htm).

## The interface

The following sections outline how to navigate the experiment interface to configure your experiment. For more information about the interface, see [*Navigating the experiment interface*](navigate-experiment-interface.htm).

### Tabbed navigation

When you create an experiment, the Configuration tab opens. This is where you can configure the target and features for the experiment.

After running at least one experiment version, the Configuration tab becomes Training data. Other tabs also become available. These other tabs allow you to analyze the models you have just trained in the version. If you need to configure subsequent versions with different feature selections, you can return to the Training data tab.

### Schema view and Data view

In the Configuration/Training data tab, you can alternate between ![Rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view and ![Profile](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_profile.svg) Data view.

#### Schema view

![Rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view is the default view. In this view, each column in your dataset is represented by a row in the schema with information and statistics.

You can:

- Select features to include in your experiment.
- View details about each column, such as data type and feature type.
- View insights about columns, such as why they cannot be selected, or how they will be processed during training.

Tip noteClick ![Column move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_column_move.svg) to customize the information in the table. For example, you can hide certain columns to reduce the information that is displayed.

Schema view in an ML experiment

![Schema view in an ML experiment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen-automl-experiment-schema-view.png "Click to view full size")

#### Data view

![Profile](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_profile.svg) Data view is an alternative view you can use to access more information and sample data for each column.

Data view in an ML experiment

![Data view in an ML experiment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen-automl-experiment-data-view.png "Click to view full size")

### Experiment configuration panel

In the experiment configuration panel, you can further customize the experiment training. This panel is open by default in new experiments.

After running a version, click ![Controls](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) View configuration to open the panel to configure the next version.

With the experiment configuration panel, you can:

- Select a [target](#glossary-0 "Glossary term") and experiment type
- Set a version name
- Add or remove features
- Configure a new version of the experiment
- View the type of model you are training
- Select to change or refresh the training dataset
- Add or remove algorithms
- Change model optimization settings
- For time series models, set the forecast settings
- Configure bias detection

Experiment configuration panel

![Experiment configuration panel with selected target, experiment type, and default feature selection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-tutorial-exp-configuration.png "Click to view full size")

## Selecting the target and experiment type

You can change the target column and experiment type until you start the first training. After that, they are locked for editing.

The target column contains the values that you want the machine learning model to predict.

The experiment type is determined by the target and the type of data it contains. The experiment type defines what type of model you want to train. The following options may be available:

- Binary classification: Trains models to predict a target that has two possible values (for example, yes or no). Data can be of any feature type.
- Multiclass classification: Trains models to predict a target with 3-10 possible values (for example, a list of categories). Data can be of any feature type but a column with more than 10 distinct, non-numeric classes (values) is not selectable as the target.
- Regression: Trains models to predict a target with more than 10 possible values — specifically, a target with numeric feature type.
- Time series: Trains models to forecast target values for specific future time periods, leveraging historical data. The target must have more than 10 distinct values and have numeric data. For more information, see [*Working with time series experiments*](time-series-experiment.htm).

Do the following:

- In ![Rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view or ![Profile](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_profile.svg) Data view, click the radio button for a column.

  The target column is now indicated by ![Target](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_target.svg) and the other available columns are automatically selected as features.

  Selecting the target in Schema view

  ![Dataset column with target symbol.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/selecting_target_pane.png "Click to view full size")

  In the experiment configuration panel, under Experiment settings, you can change the target before training if needed.

Information note

Experiment settings may contain an Experiment type selector. For example:

- If there is a date feature in the dataset and target feature type is numeric, you can switch between Multiclass classification and Binary classification.
- If time series forecasting is possible for your dataset and target, you can change the experiment type from Regression to Time series.

When the target and experiment type are selected, you can start running the first version of the experiment. Read more in [*Training experiments*](training-experiments.htm). You can do additional configuration at this point—described below—or adjust the configuration after you have reviewed the training results.

Explanations of how your data is being interpreted and processed are shown as the experiment training continues. For more information, see [*Interpreting dataset insights*](dataset-insights.htm#Explanations).

## Selecting feature columns

With the target set, you can choose which of the other available columns to include in the training of the model. Exclude any features that you don't want to be part of the model. Note that the column will stay in the dataset but will not be used by the training algorithm.

At the top of the experiment configuration panel, you can see the number of cells in your dataset. If the number exceeds your dataset limit, you can exclude features to get below the limit.

You can select the feature columns in various ways:

### In Schema view and Data view

In the main views, you can:

- Deselect Include all available features and then select only the ones you want to include.
- Manually clear the checkboxes for the features you don't want to include.
- Make a search and exclude or include all features in your filtered search result.

Tip note

In these views, each column has an icon next to it to provide more information:

- ![Check](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_check.svg): The feature is included, or can be included, in the experiment.
- ![Excluded feature](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_close.svg): The feature is excluded from the experiment. It can sometimes be included, but is generally not recommended.
- ![Feature cannot be selected](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_restricted.svg): The feature cannot be included in the experiment.

### In the experiment configuration panel

In the experiment configuration panel, you can:

- Manually clear the checkboxes for the features you don't want to include.
- After you have run the first version of the experiment, you can define the Number of top features to include.

Features section in the experiment configuration panel

![Features section in the Qlik Predict experiment configuration panel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml_features-configuration-panel.png "Click to view full size")

When you select features, they are automatically assigned a feature type. The possible feature types are:

- Categorical
- Numeric
- Date
- Free text

The feature type is assigned based on the data contained in the feature column. If a feature meets certain criteria, it might be selected to become the basis for auto-engineered features. If desired, you can change whether the feature is used for automatic feature engineering. For full details about automatic feature engineering, see [*Automatic feature engineering*](automatic-feature-engineering.htm).

Certain columns in your dataset may not be selectable as features for your experiment, or may have specific processing applied to them. Explanations of how your data is being interpreted and processed are shown as you navigate experiment training. For more information, see [*Interpreting dataset insights*](dataset-insights.htm#Explanations).

## Configuring bias detection

You can activate bias detection for features containing sensitive data. Bias detection is performed when you run the experiment. You can also click Get recommendations to use generative AI to scan your training data for possibly sensitive features before running bias detection.

Bias detection determines whether the feature increases the model's likelihood of promoting unfair outcomes in its predictions, or if the source data is inherently biased.

Do the following:

1. In an ML experiment, expand Bias in the training configuration panel.
2. Before selecting features for bias detection, optionally click Get recommendations to use generative AI to suggest features that could contain biased data. See [*Using generative AI to recommend features for bias detection*](bias-detection.htm#UsingAI).
3. Select or deselect any features for which you want to run bias detection.

Alternatively, toggle on bias detection for the desired features in ![Rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view.

For more information about bias detection, see [*Detecting bias in machine learning models*](bias-detection.htm).

## Selecting algorithms

All available algorithms are included by default and you can exclude any algorithms that you don't want to use. Normally, you would do this as part of the model refinement when you have seen the first training results. Read more in [*Refining models*](refining-models.htm).

Algorithms section in the experiment configuration panel

![Algorithms section in the Qlik Predict experiment configuration panel.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_select-algorithms-rev.png "Click to view full size")

## Changing feature types

When a dataset is loaded, the columns are treated as categorical, numeric, date, or free text based on the data type and other characteristics. In some cases, you might want to change this setting.

For example, if the days of the week are represented by the numbers 1-7, each number represents a categorical value. By default, it is treated as a continuous ranked numeric value, so you would need to manually change the configuration to treat it as categorical.

When a column is identified as containing date and time information, it is used as the basis for new generated auto-engineered features. When this happens, the original column (the parent feature) is treated as having the date feature type.

You can change the parent feature from a date feature to a categorical or numeric feature. For example, this is useful when a feature is identified as a date, but you need it to be treated as a string or number. When you do this, you can no longer use its auto-engineered features in experiment training.

Do the following:

1. In ![Rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view, locate the feature.
2. In the Feature type column for this feature, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg).
3. Select a value in the list.

You can alternatively change feature types from ![Profile](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_profile.svg) Data view. Locate the feature, then click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to the current feature type. Select a value in the list.

### Time series forecasting

If you are training a time series experiment, certain feature type transformations are automatically applied depending on your configuration. For example, if you select any groups to use for multivariate forecasting, the feature types of these groups are automatically switched to categorical.

### Impact on predictions

When you manually change the feature type of a feature, and then deploy a resulting model, the feature type overrides will be applied to the feature in the apply dataset that is used in predictions made with that model.

## Changing dataset

You can change the training dataset before you run the first experiment version, as well as after running any version.

If you change the dataset before running the first version, you will lose any configuration that you have done prior to changing the dataset.

Do the following:

1. In the experiment configuration panel under Training data > Review dataset, click Change dataset.
2. Select a new dataset.

For more information about changing and refreshing the dataset during model refinement (after running an experiment version), see [*Changing and refreshing the dataset*](refining-models.htm#Changing).

## Configuring model optimization

If your [experiment type](#glossary-2 "Glossary term") is binary classification, multiclass classification, or regression, you can adjust the following settings to optimize your models:

- Turning intelligent model optimization on or off
- Turning hyperparameter optimization on or off
- Turning time-aware training on or off

These options can be turned on or off for each version of the experiment that you run.

Model optimization section in the experiment configuration panel

![Model optimization section in the Qlik Predict training configuration panel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen-automl-optimization.png "Click to view full size")

### Configuring intelligent optimization

By default, the experiment uses intelligent model optimization. With intelligent model optimization, Qlik Predict handles the model refinement process for you by iterating feature selection and applying advanced transformations to your data.

For more information about intelligent optimization, see [*Intelligent model optimization*](intelligent-model-optimization.htm).

You can turn this setting off to manually refine the models you train. For example, you might want to start your model training with intelligent model optimization, then switch to manual refinement for v2 to further adjust the configuration.

Do the following:

1. Click ![Controls](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) View configuration.
2. If you have already run at least one version of the experiment, click New version.
3. In the panel, expand Model optimization.
4. Switch from Intelligent to Manual.
5. Using the slider, set the maximum run duration for the training.

### Configuring hyperparameter optimization

You can optimize the models using hyperparameter optimization. Note that this is an advanced option that could increase the training time significantly. Hyperparameter optimization is available if you turn off intelligent optimization.

For more information, see [*Hyperparameter optimization*](hyperparameter-optimization.htm).

Do the following:

1. Click ![Controls](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) View configuration.
2. If you have already run at least one version of the experiment, click New version.
3. In the panel, expand Model optimization.
4. Switch from Intelligent to Manual.
5. Select the Hyperparameter optimization checkbox.
6. Optionally, set a time limit for your optimization. The default time limit is one hour.

### Configuring time-aware training

If you want your models trained with consideration to a time series dimension, activate time-aware training for the experiment version. To use this option, you need to have a column in your dataset that contains the relevant time series information.

When time-aware training is turned on, Qlik Predict uses specialized cross-validation and null imputation processes to train the models.

For more information, see [*Creating time-aware models*](time-aware-models.htm) and [*Time-based cross-validation*](holdout-crossvalidation.htm#TimeAware).

Do the following:

1. Click ![Controls](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) View configuration.
2. If you have already run at least one version of the experiment, click New version.
3. In the panel, expand Model optimization.
4. Under Time-based test-train split, select the Date index to use for sorting the data.

## Viewing insights about the training data

In the Configuration/Training data tab of the experiment, you can view insights into the handling of the training data. This information is available in both ![Table rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view and ![Profile](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_profile.svg) Data view. The information shown depends on whether or not you have run a version with the current training data. The changes in the Insights can help you identify why features might be unavailable for use, or why they have been automatically dropped.

For more information about what each insight means, see [*Interpreting dataset insights*](dataset-insights.htm#Explanations).

Related learning:

- [Introduction to Qlik Predict](/lnk/Introduction_Qlik_AutoML)
