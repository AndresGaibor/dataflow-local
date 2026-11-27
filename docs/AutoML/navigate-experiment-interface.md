---
title: "Navigating the experiment interface"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/navigate-experiment-interface.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments"]
---

# Navigating the experiment interface

The tabbed interface helps you move through each stage of model training. Use the tabs and experiment configuration panel to train and optimize your model.

## Toolbar

Use the toolbar to switch between tabs in the interface.

In the toolbar, you can also do the following:

- Depending on which tab you are on, you can switch between your trained models.
- Click ![View configuration](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) View configuration to further configure training, review the current version, or start a new version.

Toolbar in an ML experiment

![Toolbar in an ML experiment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_automl-experiment-toolbar.png "Click to view full size")

## Configuration and Training data

This tab lets you manage experiment data. When you create an experiment, Configuration is the only tab shown. As training progresses, the tab is renamed to Training data, and you can switch to other tabs for model analysis.

In this tab, you can:

- Select a [target](#glossary-0 "Glossary term") before training the first version.
- Add or remove [features](#glossary-1 "Glossary term").
- View feature dataset insights and statistics and review data quality warnings.
- Select a new training dataset.
- Configure bias detection.

Switch between ![Schema view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view and ![Data view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_profile.svg) Data view for different representations of the training dataset.

Configuration tab in an ML experiment. After training, this tab is renamed to Training data.

!['Data' tab in an ML experiment before the user has run a version of the training](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen-automl-experiment-data-tab.png "Click to view full size")

## Models

In the Models tab, perform quick analysis of training results and explore recommended models. This tab helps you compare core metrics for each model and evaluate different predictive use cases.

To perform more detailed model analysis, you can switch to the Compare and Analyze tabs.

Select a model in the Model metrics table or from the recommendations above the table. You can view:

- Performance scores.
- Model training summary (available with intelligent model optimization).
- Feature importance visualizations.
- Other visualizations specific to the experiment type.
- Bias detection results.

For more information, see [*Performing quick model analysis*](analyze-models-quick.htm).

Models tab in an ML experiment trained with intelligent model optimization

!['Models' tab in an ML experiment, showing summary, core model metrics, and auto-generated visualizations](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-ml-exp-models.png "Click to view full size")

## Compare

Compare your models in detail using embedded analytics. Make [selections](#glossary-2 "Glossary term") and customize dashboard data to uncover insights into model performance.

In the Compare tab, you can:

- Access all available model metrics and hyperparameters.
- Compare training and holdout metrics across models.

For more information, see [*Comparing models*](analyze-models-compare.htm).

Compare tab in an ML experiment

![Comparative model analysis in ML experiment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen-experiment-model-comparison.png "Click to view full size")

## Analyze

Dive deeper with embedded analytics for each model you train.

In the Analyze tab, you can:

- Further analyze prediction accuracy.
- Evaluate feature importance at a granular level.
- View the distribution of feature data.
- View detailed information about bias detection results.

For more information about detailed model analysis, see [*Performing detailed model analysis*](analyze-models-detailed.htm).

Analyze tab in an ML experiment

!['Analyze' tab in an ML experiment, showing prediction accuracy and feature importance](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_experiment_model-details-overview.png "Click to view full size")

## Experiment configuration panel

Use this panel to configure experiment settings.

The experiment configuration panel opens by default in new experiments. After you run a version, click ![View configuration](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) View configuration to open the panel.

With the experiment configuration panel, you can:

- Select a [target](#glossary-3 "Glossary term") and experiment type
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
