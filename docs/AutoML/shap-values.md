---
title: "Visualizing SHAP values in Qlik Sense applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/shap-values.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML predictions", "Generating SHAP datasets during predictions"]
---

# Visualizing SHAP values in Qlik Sense applications

SHAP values help us understand what is driving a model as well as driving individual outcomes. Build visualizations of SHAP values in Qlik Sense applications to further explore your data. The following examples will give you an idea of the insights you can gain.

## Preparations

Before you get started, do the following preparations:

- Generate a Coordinate SHAP dataset. This dataset has the SHAP value columns pivoted into a "feature" and "value", which lets you use multiple features in a single chart.
- For binary classification predictions, plot the predicted probability against the sum of SHAP values per row and look at the direction of the SHAP values. If the slope is negative, reverse direction of the SHAP values to make it easier to interpret the visualizations.

Direction check for SHAP values showing a positive slope

![Graph of SHAP values to show positive slope.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_shap-direction-plot.png "Click to view full size")

## Feature importance ranking

You can create a feature importance rank using the average absolute values of the SHAP values for each feature. The figure shows the importance of different features on the probability that a customer will churn.

SHAP importance ranking in Qlik Sense

![Feature importance ranking with a bar chart.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_shap-importance-rank.png "Click to view full size")

## Direction and distribution

The SHAP values can also be used to understand the direction and distribution of each feature’s influence. In the figure, you can see if the different features make the customers more or less likely to churn.

SHAP distribution plot in Qlik Sense

![Feature importance distribution graph.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_shap-distribution-chart.png "Click to view full size")

## Feature importance for cohorts

The feature importance can be created for distinct cohorts. For example, you can compare the most important features for customers with different plan types. The figure shows the feature influencers by plan type.

This chart uses a Trellis container to represent the data for specific field values in the data. You can also create similar charts individually using set expressions.

Chart in Qlik Sense displaying most significant churn influencers by plan type

![Trellis object in Qlik Sense showing set analysis values for four different feature field values (plan types).](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_shap-trellis-chart-cohorts.png "Click to view full size")

## Feature importance at the row level

SHAP importance can be used to understand feature importance at the row level. You can investigate and compare which features influence the probability of churn for different customers, as seen in the figure.

SHAP importance charts for specific customer IDs

![Bar charts showing SHAP importance rankings for two different customers. The customer on the left is expected to churn, and the customer on the right is expected to not churn.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_shap-analysis-customer-specific.png "Click to view full size")

## Feature variation

You can plot the influence of each variation of a feature. For example, you can create visualizations to show the average influence of customer plan type for each of the plan types you offer.

Bar chart in Qlik Sense displaying SHAP importance of specific field values for a single feature

![SHAP Importance bar chart for each plan type.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_shap-chart-plan-type-bar.png "Click to view full size")

Distribution plot in Qlik Sense displaying SHAP importance of specific field values for a single feature

![Bar charts showing SHAP importance rankings for two different customers. The customer on the left is expected to churn, and the customer on the right is expected to not churn.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_shap-chart-plan-type-distribution.png "Click to view full size")

## Continuous variables

SHAP values can be used in scatter plots to analyze trends as continuous variables fluctuate in value. In this plot of SHAP values, we can see that a customer's probability of churn generally increases alongside increases in their base fee.

Optionally, we can also use regression lines and other tools to uncover new insights in the data.

SHAP scatter plot showing trends in churn outcome as base fee increases

![Example of visualization of prediction data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_shap-scatter-plot-base-fee.png "Click to view full size")
