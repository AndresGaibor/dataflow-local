---
title: "Creating and configuring the experiment"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/tutorial-creating-configuring.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Tutorial – Generating and visualizing prediction data"]
---

# Creating and configuring the experiment

The first step is to create and configure the experiment. You will use the training dataset you uploaded earlier to train the model until it is ready to be deployed for making predictions.

## Creating a new experiment

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-0 "Glossary term") and select ML experiment.
2. Enter a name for your experiment, for example, Customer churn tutorial.
3. Optionally, add a description and tags.
4. Choose a space for your experiment. It can be your personal space or a shared space.
5. Click Create.
6. Select the training dataset file. This will be either of the following, depending on whether you are working with CSV or QVD:

   - ML - Churn data - training.csv
   - ML - Churn data - training.qvd

## Reviewing the data

Now you are ready to start configuring your experiment, but before you start, let's have a look at the dataset.

We start out in the Configuration tab. The default view is the ![Table rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view. Here we can see a table where each row represents a column in your dataset. Statistics and insights have been generated in automatic data preparation. You might have to scroll to the right-hand side of the schema to see the Insights.

We can see that AccountID has been excluded due to high cardinality. This means that the column contains too many unique values. The feature Country has been excluded for the opposite reason: the value is the same for all rows. These two features would not provide any value to the machine learning models.

We can also see that the categorical feature Territory has been impact encoded. Hover over the warning ![Warning triangle](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning_triangle_2.svg) and information ![Info](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) icons for more information.

Schema view for training dataset in Qlik Predict

![Schema view in ML experiment with insights about features.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-ml-exp-view-schema.png "Click to view full size")

Click ![Profile](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_profile.svg) Data view. In this view, we can see more information about each column, including sample data.

Data view

![Data view in experiment configuration.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-ml-exp-view-data.png "Click to view full size")

## Selecting a target

We want our machine learning model to predict customer churn, so we select Churned, the final column in the dataset, as our target.

Do the following:

1. Switch back to ![Table rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_rows.svg) Schema view.
2. Click the radio button for Churned.

A row in schema view is selected as target

![Table row for selected target.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-tutorial_target.png "Click to view full size")

In the experiment configuration panel, expand Experiment settings. You can see that Churned has been selected as the target. Based on your target and the available feature data, the Experiment type is Binary classification.

You can also see which features are automatically selected and excluded. Churned is the target so it will not be used as a feature.

Information shown in the configuration panel

![Experiment configuration panel with selected target, experiment type, and default feature selection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-tutorial-exp-configuration.png "Click to view full size")

## Feature selection and model optimization

By default, the experiment is set to use intelligent model optimization. To confirm, expand Model optimization in the experiment configuration panel. The Intelligent option should be selected.

Confirming intelligent model optimization in the configuration panel

![Experiment configuration panel with intelligent model optimization turned on](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ml-tutorial_optimization.png "Click to view full size")

Feature selection can be manually configured in the Features section of the configuration panel. With intelligent model optimization, feature selection is handled automatically by removal of unhelpful features. With this setting turned on, we can include all available features in the training.

## Training the experiment

The configuration is done and we are ready to start the training.

Do the following:

- Click Run experiment.

When the experiment has finished running, we can move on to the next step, which is to review the resulting model metrics.
