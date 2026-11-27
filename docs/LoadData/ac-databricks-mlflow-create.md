---
title: "Creating a Databricks MLflow connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-databricks-mlflow-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Databricks MLflow analytics source"]
---

# Creating a Databricks MLflow connection

Databricks MLflow [connections](#glossary-0 "Glossary term") are created in [Data load editor](#glossary-1 "Glossary term") or Script.

Once you have created a connection, you can select data from the available tables to send to Databricks MLflow for calculations, and then load that data into your application. This connection can be used in your data [load script](#glossary-3 "Glossary term") and in chart expressions to call model endpoints and perform real-time chart expression calculations.

You must know the settings and access credentials to the Databricks MLflow service that you want to connect to.

## Configurable settings

The following settings can be configured in the Connection dialog:

Configurable settings in the connection dialog

| Field | Description |
| --- | --- |
| Select Configuration | Configuration: Select the version of Databricks MLflow that your model uses. The following options are available:   - MLflow 1.0: The model is created using Databricks MLflow 1.x. - MLflow 2.0: The model is created using Databricks MLflow 2.x.  Information note   For models created with Databricks MLflow 2.0 (versions 2.x), data is sent to Databricks in the dataframe\_split JSON format, which is the preferred format for structured data in Databricks MLflow. |
| Model | Model URL: URL to the Databricks MLflow platform where the Databricks MLflow model is deployed. |
| Authentication | Provides the Databricks API Token.  All models on Databricks MLflow are authenticated with Databricks token-based authentication enabled. This requires an API token to be generated that has access to the model resource. |
| Response Table | Name of Returned Table: Name of the returned table from the deployed machine learning model. |
| Response Fields | - Load all available fields: Enable loading of all available fields returned by the machine learning endpoint. Disabling this, will allow you to specify the table fields and values to load into the application.  When developing applications, it is recommended to first load all fields returned from the model endpoint, and then potentially remove the fields that are not needed for the analysis in the application. - Table Fields (JMESPath): The Table fields can be specified by adding:    - Name: the name of the table that will be loaded in the application.   - Value: the name of the response row in the JSON response array. JMESPath query language can be used to parse the JSON response array. |
| Association | - Association Field: A field from the input data table containing a unique identifier.  Including this field in the source data is required when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the predictions to be associated with the source data in the data model. This can be any field with a unique ID, from the source data, or as part of the table load process. - Send Association Field: When selected, the field specified as the association field will be both returned to Qlik Sense and included in the fields sent to the endpoint  If the field belongs to the source data and is expected by the model, it must be sent to the model by enabling Send Association Field. |
| Name | The name of the connection. The default name is used if you don't enter a name. |

## Creating a new connection

Do the following:

1. Access the connector through [Data load editor](#glossary-4 "Glossary term") or Script.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Select Databricks MLflow from the list of data connectors.
5. Fill out the connection dialog fields.
6. Click Create.

Your connection is now listed under Data connections in Data load editor or Script.
