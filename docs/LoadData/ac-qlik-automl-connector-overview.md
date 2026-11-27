---
title: "Qlik Predict analytics source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-qlik-automl-connector-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Qlik Predict analytics source

Use the Qlik Predict connector to load data via an analytics connection from the integrated Qlik Predict platform into Qlik Cloud.

This connector can apply your machine learning models (ML deployments) to data using an analytics connection. The connector sends data to specific predictive endpoints, returning predictions that can be loaded into Qlik Cloud.

For information on creating ML experiments and ML deployments, see [*Working with experiments*](../AutoML/working-with-experiments.htm).

Information note

Real-time predictions APIs, and therefore, the connector, are available with the add-on tiers of Qlik Predict. They are not available for customers using the capacity that is included with a Qlik Cloud subscription.

Qlik Cloud Government noteThe Qlik Predict connector is not supported in Qlik Cloud Government.

## Enabling ML endpoints in Qlik Cloud

To work with this connector, machine learning endpoints must be enabled in the Administration activity center. The switch is located under Feature control in the Settings section.

For more information, see [*Enabling analytic connections for machine learning endpoints*](load-data-from-advanced-analytic-connections.htm#Enabling).

## Required permissions

To use this connector, you need to have sufficient permissions for using data sources and running predictions from Qlik Predict. For full details, see:

- [*Working with ML predictions*](../AutoML/working-with-predictions.htm)
- [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm)
- [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm)

## Limitations

- The Qlik Predict connector is limited to 200k rows per request. These are sent to the endpoint service in batches of 2k rows. In scenarios where more rows are required to be processed, use a Loop within the Data [load script](#glossary-0 "Glossary term") to process more rows in batches.
- When using in a chart expression, it is important to provide the data types of the fields as the model needs to process these in the correct string/numeric format. A limitation of server-side extensions in chart expressions is that the data types are not automatically detected as they are in the load script.
- If you are using a relative connection name, and if you decide to move the application from a [shared space](#glossary-2 "Glossary term") to another shared space, or if you move your application from a shared space to your private space, then it may take some time for the analytic connection to be updated to reflect the new space location.
- The Qlik Predict analytics connector does not support time series models.
- You cannot create and manage connections to this connector in Data manager within an analytics application.
