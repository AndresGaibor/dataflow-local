---
title: "Creating a Qlik Predict connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-qlik-automl-connector-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik Predict analytics source"]
---

# Creating a Qlik Predict connection

Qlik Predict [connections](#glossary-0 "Glossary term") are created in Data load editor, Script, or the Analytics [activity center](#glossary-1 "Glossary term").

Once you have created a connection, you can select data from the available tables to send to Qlik Predict for calculations, and then load that data into your application. This [connection](#glossary-3 "Glossary term") can not only be used in your data [load script](#glossary-4 "Glossary term"), but also in chart expressions to call model endpoints and perform real time [chart](#glossary-5 "Glossary term") expression calculations.

Information noteIn order for a deployment to appear in the ML deployment dropdown, you must select Enable real-time API access in the Create ML deployment dialog window when creating the deployment.

## Configurable settings

The following settings can be configured in the connection dialog:

Configurable settings in the connection dialog

| Field | Description |
| --- | --- |
| Connection | - ML deployment: The ML deployment that will be employed to produce predictions.  Information noteThis dropdown list can display a maximum of 100 deployments. |
| Alias | - Specify the [model alias](#glossary-6 "Glossary term") referencing the model to use for predictions. Case-sensitive. The default value is the Default alias contained in the ML deployment. |
| Response Table | - Name of Returned Table: Name of the returned table from the deployed machine learning model. - Include SHAP: If checked, the SHAP values will be included in the response. - Include Apply dataset: If checked, the source data will be included in the response. - Include Errors: If checked, the response will include a column with the reason why the prediction was not produced. |
| Association | - Association Field: The name of the field in the source data table containing a unique identifier to use as an index in the response data. The column will be included with its original name and values. This is intended to allow the user to join results with source data. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name will be used if you do not enter a name. |

## Creating a new connection

Do the following:

1. To create a Qlik Predict connection, machine learning endpoints must be turned on for the Qlik Cloud tenant. For more information, see [*Enabling ML endpoints in Qlik Cloud*](ac-qlik-automl-connector-overview.htm#EnableMLEndpoints).
2. Access the connector through [Data load editor](#glossary-7 "Glossary term") or Script.
3. Click Create new connection.
4. Under Space, select the space where the connection will be located.
5. Select Qlik Predict from the list of data connectors.
6. Fill out the connection dialog fields.
7. Click Create.

Your connection is now listed under Data connections in Data load editor or Script.
