---
title: "Creating an Azure ML connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-azure-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Azure ML analytics source"]
---

# Creating an Azure ML connection

Azure ML [connections](#glossary-0 "Glossary term") are created in the data load editor.

Once you have created a connection, you can select data from the available tables to send to Azure ML for calculations, and then load that data into your application. This connection can not only be used in your data [load script](#glossary-2 "Glossary term") but also in [chart](#glossary-3 "Glossary term") expressions to call model endpoints and perform real time chart expression calculations.

You must know the settings and access credentials to the Azure ML service that you want to connect to.

## Configurable settings

The following settings can be configured in the connection dialog:

Configurable settings in the connection dialog

| Field | Description |
| --- | --- |
| Select configuration | Drop-down menu item to select the configuration which determines which Azure ML models to use for machine learning model predictions.  Supported configurations:   - Azure ML - Legacy Format: This configuration should be used for the models deployed before mid-January 2022 that were created using Automated ML which expects JSON in the following format:  {      "data": [        {          <field\_list>        }      ]   } - Azure ML: This configuration should be used for the models that are created using Automated ML or Designer  which expects JSON in the following format:  {      "Inputs": {        "<JSON\_object\_name>(default is ‘data’)": [          {            < field\_list >          }        ]      }   }   Information noteIf you are in doubt which configuration to use, you can re-deploy your model and it will use the new format. |
| Endpoint Name | Name of the endpoint.  The endpoint name is the identifier given for the endpoint on Azure. This is typically created by the user who sets up the endpoint or deploys a model. |
| Authentication | Provides the Azure ML Endpoint Key.  All models on Azure are authenticated with Azure key-based authentication enabled. This requires an access key (primary or secondary key) generated that has access to the model resource. |
| Request | Web Service Input Name: Name of the JSON object that is expected by the deployed machine learning model. Must be changed if the default name does not fit the format used by the model. |
| Response Table | - Name of Returned Table: Name of the returned table from the deployed machine learning model. - Table Path (JMESPath): The Table can be specified by using the JMES table path to the predictions row in the JSON response array. |
| Response Fields | - Load all available fields: Enable loading of all available fields returned by the machine learning endpoint. Disabling this, will allow you to specify the table fields and values to load into the application.  When developing applications, it is recommended to first load all fields returned from the model endpoint, and then potentially remove the fields that are not needed for the analysis in the application. - Table Fields (JMESPath): The Table fields can be specified by adding:    - Name: the name of the table that will be loaded in the application.   - Value: the name of the response row in the JSON response array. JMESPath query language can be used to parse the JSON response array. |
| Association | - Association Field: A field from the input data table containing a unique identifier.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the predictions to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. - Send Association Field: When selected, the field specified as the association field will be both returned to Qlik Sense and included in the fields sent to the endpoint  If the field belongs to the source data and is expected by the model, it needs to be sent to the model by enabling Send Association Field. |
| Name | The name of the connection. The default name will be used if you do not enter a name. |

## Creating a new connection

Do the following:

1. Access the connector through [Data load editor](#glossary-4 "Glossary term") or Script.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Select Azure ML from the list of data connectors.
5. Fill out the connection dialog fields.
6. Click Create.

Your connection is now listed under Data connections in Data load editor or Script.
