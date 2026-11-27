---
title: "Working with ML deployments"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/working-with-deployments.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict"]
---

# Working with ML deployments

After training and refining a model, you can deploy the model to make predictions.

ML deployments can be created in personal, shared, and managed spaces.

## Workflow

The following steps are an example of how to work with ML deployments and predictions.

1. Deploy your model

   Deploy the model you want to use to make predictions.

   [*Deploying models*](deploying-models.htm)
2. Get your model approved

   Before you can make predictions with the ML deployment, the source model needs to be activated for making predictions. Model approval can be performed by users and administrators with specific permissions.

   [*Approving deployed models*](approve-models.htm)
3. Make predictions

   Make manual or scheduled predictions on datasets or use the real-time prediction endpoint in the Machine Learning API.

   [*Creating predictions on datasets*](creating-predictions.htm)

   [Machine Learning API](https://qlik.dev/apis/rest/ml/)
4. Visualize the predictive insights

   Load the generated prediction data into an application and create visualizations.

   [*Visualizing SHAP values in Qlik Sense applications*](shap-values.htm)
5. Explore the data with what-if scenarios

   Integrate the prediction API into an application to get real-time predictions. This allows you to try out what-if scenarios by changing feature values and getting predicted outcomes for the new values. The record is passed to the ML deployment via API and a response is received in real time. For example, what would happen to the risk of customer churn if we changed the plan type or increased the base fee?
6. Take action

   Analyze the predictive insights and scenarios to find out which actions to take. Qlik Automate helps you automate the actions and provides specific templates for machine learning use cases. For more information about automations, see [Qlik Automate.](/en-US/cloud-services/Subsystems/Sense_QlikAutomation/Content/Sense_QlikAutomation/introduction/home-automation.htm)
7. Replace models when needed

   Over time, your input data might change in distribution and features. If your original machine learning problem remains the same, you can swap new models into your existing ML deployment to allow seamless improvement to predictions with minimal disruption. If you need to redefine your original machine learning problem, you can create a new experiment.

   [*Using multiple models in your ML deployment*](ml-deployment-available-models.htm)

## Requirements and permissions

For information about the required space roles for working with deployments and predictions in shared and managed spaces, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](../Spaces/permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](../Spaces/permissions-managed-space-admin.htm)

If you are an administrator, see [*Who can work with Qlik Predict*](who-can-work-with-automl.htm) for a comprehensive overview of the required user permissions for working with deployments and predictions.
