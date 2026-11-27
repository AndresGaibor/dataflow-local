---
title: "Data drift"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/data-drift.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning", "Evaluating model performance over time"]
---

# Data drift

Over time, your model's accuracy can decline because the data in one or more features changes in distribution, magnitude, and other properties. Because the original model was trained with features that contain specific patterns and distributions, future changes to these distributions will affect the precision and quality of predictions.

Data drift can be quantified and can be calculated in a number of ways. In Qlik Predict, data drift is calculated with the population stability index formula. See [*Monitoring data drift in deployed models*](monitor-drift.htm).

A best practice is to monitor your model for data drift by comparing the original [training dataset](#glossary-0 "Glossary term") against the most up-to-date [apply dataset](#glossary-1 "Glossary term") on which you are generating predictions. When data drift reaches a specific threshold, re-train the model, or configure a new model if your original machine learning problem has changed substantially.

For more information about assessing model performance over time, see [*Evaluating model performance over time*](models-over-time.htm).

## Example

Suppose a company has a set of products that has been established to be popular mainly with consumers aged 45 and older. The value distribution for a feature Age might look like the following.

Bar chart showing company sales appealing more to consumers above the age of 45.

![Bar chart showing distribution of product purchases by age before the company has introduced a new product. In this case, the distribution of the age frequencies shows sales appealing mainly to adults 45 and older.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/data-drift-example_before-product-launch.png "Click to view full size")

Recently, the company has introduced a new product that is marketed to appeal to younger consumers as well. When the product sells as expected, we see a significant feature drift for the feature Age.

Bar chart showing company sales that are more evenly distributed, with the company sales appealing more equally to consumers of all ages.

![Bar chart showing distribution of product purchases by age after the company has introduced a new product. In this case, the distribution of the age frequencies has shifted from sales appealing mainly to adults 45 and older towards a more equallty distributed popularity among all age groups.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/data-drift-example_after-product-launch.png "Click to view full size")

## Data drift monitoring in Qlik Predict

Qlik Predict has built-in tools to help you detect data drift on a per-feature basis within your deployed models. For more information, see [*Monitoring data drift in deployed models*](monitor-drift.htm).
