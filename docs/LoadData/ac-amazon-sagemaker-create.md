---
title: "Creating an Amazon SageMaker connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-amazon-sagemaker-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Amazon SageMaker analytics source"]
---

# Creating an Amazon SageMaker connection

Amazon SageMaker [connections](#glossary-0 "Glossary term") are created in [Data load editor](#glossary-1 "Glossary term") or Script.

Once you have created a [connection](#glossary-2 "Glossary term"), you can select data from the available tables to send to Amazon SageMaker for calculations, and then load that data into your application. This connection can not only be used in your data [load script](#glossary-4 "Glossary term") but also in chart expressions to call model endpoints and perform real time chart expression calculations.

You must know the settings and access credentials to the Amazon SageMaker service that you want to connect to.

## Configurable settings

The following settings can be configured in the connection dialog:

Configurable settings in the connection dialog

| Field | Description |
| --- | --- |
| Endpoint Name | Name of the endpoint.  The endpoint name is the identifier given for the endpoint on AWS. This is typically created by the user who sets up the endpoint or deploys a model. |
| Model Name | Name of the deployed model.  This parameter is only required when a multi-model endpoint is deployed. For a simple endpoint, this parameter should not be provided as it will trigger an error from AWS. |
| Model Variant Name | Name of variant of the deployed model.  This parameter is only required when a multi-model endpoint is deployed. For a simple endpoint, this parameter should not be provided as it will trigger an error from AWS. |
| Settings | The following settings are available:   - AWS Region: Select the region you intend to use for the comprehend service. - Use FIPS Endpoint: Specify if you need to use a FIPS compliant endpoint.  This will only work if you choose a region that supports FIPS and for most users should be left as the default “No”. |
| Authentication | Provide the AWS authentication Access key and Secret key for the Amazon Comprehend endpoints. These need to be created with access to the right policy permissions.  The authentication properties can be found in the AWS console and need to be input every time the connection needs to be re-authenticated. |
| Response Format | Value of response format of the deployed machine learning model:   - JSON - Text Array   Most models will return their data in JSON format, however some only return a text-based output. The option needs to be selected based on the type of model being deployed, otherwise this will result in a connection setting error. |
| Response Table | - Name of Returned Table: Name of the returned table from the deployed machine learning model. - Table Path (JMESPath): The Table can be specified by using the JMES table path to the predictions row in the JSON response array. |
| Response Fields | - Load all available fields: Enable loading of all available fields returned by the machine learning endpoint. Disabling this, will allow you to specify the table fields and values to load into the application.  It is recommended to first load all fields returned from the model endpoint, and then potentially remove the fields that are not needed for the analysis in the application. - Table Fields (JMESPath): The Table fields can be specified by adding:    - Name: the name of the table that will be loaded in the application.   - Value: the name of the response row in the JSON response array. JMESPath query language can be used to parse the JSON response array. |
| Association | - Association Field: A field from the input data table containing a unique identifier.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the predictions to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. - Send Association Field: When selected, the field specified as the association field will be both returned to Qlik Sense and included in the fields sent to the endpoint  If the field belongs to the source data and is expected by the model, it needs to be sent to the model by enabling Send Association Field. |
| Name | The name of the connection. The default name will be used if you do not enter a name. |

## Creating a new connection

Do the following:

1. Access the connector through [Data load editor](#glossary-5 "Glossary term") or Script.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Select Amazon SageMaker from the list of data connectors.
5. Fill out the connection dialog fields.
6. Click Create.

Your connection is now listed under Data connections in Data load editor or Script.
