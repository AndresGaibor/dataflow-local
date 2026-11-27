---
title: "Databricks MLflow analytics source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-databricks-mlflow-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Databricks MLflow analytics source

Databricks MLflow is a machine-learning platform for automating, assuring, and accelerating predictive analytics, helping data scientists and analysts to build and deploy accurate predictive models.

To connect to Databricks MLflow, you must have created, or have access to, a model and deployed it to an endpoint on the Databricks MLflow platform. Additionally, this endpoint must be publicly accessible by Qlik Cloud.

[Managed MLflow](https://databricks.com/product/managed-mlflow).

## Enabling ML endpoints in Qlik Cloud

To work with this connector, machine learning endpoints must be enabled in the Administration activity center. The switch is located under Feature control in the Settings section.

For more information, see [*Enabling analytic connections for machine learning endpoints*](load-data-from-advanced-analytic-connections.htm#Enabling).

## Limitations

- Databricks MLflow has an endpoint quota. For more information, see [Introduction to Databricks Machine Learning](https://docs.databricks.com/applications/machine-learning/index.html).
- The resources available on the Databricks MLflow services where the model has been deployed impact and limit performance in the Qlik Sense reload and [chart](#glossary-0 "Glossary term") responsiveness.
- The Databricks MLflow connector is limited to 200,000 rows per request. These are sent to the endpoint service in batches of 2,000 rows. In scenarios where more rows must be processed, use a Loop within the Data [load script](#glossary-1 "Glossary term") to process more rows in batches.
- When an application is regularly reloaded, it's best practice to cache the predictions using a [QVD](#glossary-2 "Glossary term") file and only send the new rows to the prediction endpoint. This will improve the performance of the Qlik Sense application reload and reduce the load on the Databricks MLflow endpoint.
- When using Databricks MLflow in a chart expression, it's important to provide the data types of the fields as the model needs to process these in the correct string/numeric format. A limitation of server-side extensions in chart expressions is that the data types are not automatically detected as in the load script.
- If you are using a relative [connection](#glossary-3 "Glossary term") name, and if you decide to move your application from a [shared space](#glossary-5 "Glossary term") to another shared space, or if you move your application from a shared space to your private space, then it will take some time for the analytic connection to be updated to reflect the new space location.
- You cannot create and manage connections to this connector in Data manager within an analytics application.
