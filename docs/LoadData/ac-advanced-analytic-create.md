---
title: "Creating an Advanced Analytics connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-advanced-analytic-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Advanced Analytics analytics source"]
---

# Creating an Advanced Analytics connection

Advanced Analytics [connections](#glossary-0 "Glossary term") are created in [Data load editor](#glossary-1 "Glossary term") and Script.

Once you have created a connection you can select data from the available tables to send to the model for machine learning problems and tasks, and then load the results into your application. The connection can not only be used in your data [load script](#glossary-3 "Glossary term"), but also in chart expressions to call deployed model endpoints and enable interactive [charts](#glossary-4 "Glossary term") using machine learning insights.

You must know the settings and access credentials to the service that you want to connect to.

## Configurable settings

The following settings can be configured in the connection dialog:

Configurable settings in the connection dialog

| Field | Description |
| --- | --- |
| URL | Host URL to the platform where the model is deployed. |
| Method | HTTP method to use in the API endpoint requests to the model.   - GET - POST |
| Content Type | HTTP request header Content-Type.  For example “application/json”. |
| HTTP Headers | HTTP headers fields, such as Name and Value, to send in every API endpoint requests to the model. |
| Query Parameters | Query parameters, such as Name and Value, that will be attached to the end of the URL. |
| Authorization Method | The authorization method to be set in the HTTP Authorization request header in order to authenticate the user.  Supported authorization methods:   - None - Bearer Token - AWS Auth v4 Signature |
| Request | - Field Formats: Field formats can be optionally added and specified including Name and Value. - Timestamp Format: Timestamp format needs to be changed if the default format does not fit the format used by the model. |
| Response Fields | - Load all available fields: Enable loading of all available fields returned by the machine learning endpoint. Disabling this, lets you to specify the table fields and values to load into the application.  When developing applications, it is recommended to first load all fields returned from the model endpoint, and then potentially remove the fields that are not needed for the analysis in the application. |
| Response Table | - Table Fields (JMESPath): The Table fields can be specified by adding:    - Name: the name of the table that will be loaded in the application.   - Value: the name of the response row in the JSON response array. JMESPath query language can be used to parse the JSON response array. |
| Association | - Association field: A field from the input data table containing a unique identifier.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the predictions to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. - Send Association Field: When selected, the field specified as the association field will be both returned to Qlik Sense and included in the fields sent to the endpoint  If the field belongs to the source data and is expected by the model, it needs to be sent to the model by enabling Send Association Field. |
| Name | The name of the connection. The default name will be used if you do not enter a name. |

## Creating a new connection

Do the following:

1. Access the connector through Data load editor or Script.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Select Advanced Analytics from the list of data connectors.
5. Fill out the connection dialog fields.
6. Click Create.

Your connection is now listed under Data connections in the Data load editor.
