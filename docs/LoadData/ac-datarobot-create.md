---
title: "Creating a DataRobot connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-datarobot-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "DataRobot analytics source"]
---

# Creating a DataRobot connection

DataRobot [connections](#glossary-0 "Glossary term") are created in Data load editor or Script.

Once you have created a connection, you can select data from the available tables to send to DataRobot for calculations, and then load that data into your application. This connection can not only be used in your data [load script](#glossary-2 "Glossary term") but also in chart expressions to call model endpoints and perform real time chart expression calculations.

You must know the settings and access credentials to the DataRobot service that you want to connect to.

## Configurable settings

The following settings can be configured in the connection dialog:

Configurable settings in the connection dialog

| Field | Description |
| --- | --- |
| Select configuration | Drop-down menu item to select the configuration which determines which DataRobot models to use for machine learning model predictions.  Supported configurations:   - DataRobot Predictions - DataRobot Timeseries Predictions |
| Deployment | - Deployment ID: deployment identifier of the created deployment on DataRobot cloud. - Host URL: Host URL to the DataRobot platform where the DataRobot model is deployed. |
| Authentication | Provide the API Key and DataRobot Key for the DataRobot endpoints.  All DataRobot API endpoints use API keys as a mode of authentication. |
| Prediction Type | Available prediction types:   - Predictions - Predictions with explanations   DataRobot’s Prediction Explanations allows you to calculate the impact of a configurable number of features for each outcome your model generates. |
| Request | - Field Formats: can be optionally added and specified including Name and Value. - Timestamp Format: must be changed if the default format does not fit the format used by the model. |
| Response Table | - Name of Returned Table: Name of the returned table from the deployed machine learning model. |
| Response Fields | - Load all available fields: Enable loading of all available fields returned by the machine learning endpoint. Disabling this, lets you to specify the table fields and values to load into the application.  When developing applications, it is recommended to first load all fields returned from the model endpoint, and then potentially remove the fields that are not needed for the analysis in the application. - Transpose Arrays as Columns in Response: transpose the arrays as columns and select how many array items to transpose as columns  JMESPath query language can be used to specify the Value, for example [\*] to specify that the array is at the root object.  DataRobot uses nested arrays in the returned results.   <https://docs.datarobot.com/en/docs/predictions/api/dr-predapi.html#prediction-objects>. |
| Association | - Association Field: A field from the input data table containing a unique identifier.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the predictions to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. - Send Association Field: When selected, the field specified as the association field will be both returned to Qlik Sense and included in the fields sent to the endpoint  If the field belongs to the source data and is expected by the model, it needs to be sent to the model by enabling Send Association Field. |
| Name | The name of the connection. The default name will be used if you do not enter a name. |

## Creating a new connection

Do the following:

1. Access the connector through [Data load editor](#glossary-3 "Glossary term") or Script.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Select DataRobot from the list of data connectors.
5. Fill out the connection dialog fields.
6. Click Create.

Your connection is now listed under Data connections in Data load editor or Script.
