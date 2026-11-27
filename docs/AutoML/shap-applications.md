---
title: "Using SHAP values in real-world applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/shap-applications.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML predictions", "Generating SHAP datasets during predictions"]
---

# Using SHAP values in real-world applications

The following examples show how SHAP importance can be used in real-world applications.

## Call center guidance

Customer service agents in a call center can use SHAP importance to understand what the most important features are for the customer who is currently calling. Based on this information, they can focus the conversation on the most effective actions. With the real-time prediction endpoint in the Machine Learning API, they can get real-time predictions on the effects of different actions for the specific customer.

Information note

The real-time predictions API is deprecated and replaced by the real-time prediction endpoint in the [Machine Learning API](https://qlik.dev/apis/rest/ml/). The functionality itself is not being deprecated. For future real-time predictions, use the real-time prediction endpoint in the Machine Learning API. For help with migrating from the real-time predictions API to the Machine Learning API, refer to [the migration guide on the Qlik Cloud developer portal](https://qlik.dev/apis/rest/automl-deployments/#migrate-from-the-automl-real-time-predictions-api-to-the-machine-learning-api).

Customer experience dashboard in Qlik Sense, displaying SHAP importance of risk factors for churn

![Example of app that may be useful to call center agents in analyzing customer data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_shap-customer-management-dashboard.png "Click to view full size")

## Academic success management

SHAP importance can be used to create individualized recommendations for student success. By identifying risk factors contributing to a student's likelihood of dropping out, it is possible to take specific early action to help students succeed academically.

Qlik Sense application identifying features that influence the risk of dropout for a specific student

![Example of application showing information about a student.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/automl_example-app_dashboard-student.png "Click to view full size")

## Customer retention marketing

Cohort-specific marketing campaigns can be created by looking at SHAP importance and focusing on the most influential features for each group. One group might get the offer to "Renew your contract and guarantee access to your Gold Plan!" and another group would get "Renew your contract and lock in your discount for the next 12 months!".

The chart below breaks down the most significant features contributing to churn predictions for each plan type offered by a company.

Chart in Qlik Sense displaying most significant churn influencers by plan type

![Trellis object in Qlik Sense showing set analysis values for four different feature field values (plan types).](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl_shap-trellis-chart-cohorts.png "Click to view full size")
