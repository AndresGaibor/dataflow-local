---
title: "Creating an Azure OpenAI connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-azure-openai-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Azure OpenAI analytics source"]
---

# Creating an Azure OpenAI connection

To communicate with Azure OpenAI, create a connection to the Azure OpenAI analytics source.

Data received from these connections can be used in the load script and in chart expressions, to enhance your Qlik Sense analytics applications or scripts.

## Before you start

Within your Microsoft Azure account, the Azure OpenAI service is located within Azure's Cognitive Services, and is not enabled by default. Contact Microsoft if you need assistance with getting the Azure OpenAI service enabled.

## Available connector configurations

Set up your Azure OpenAI analytics connection with one of the following configurations.

### OpenAI Completions API

This configuration sends each row of data as a question to the completions API (in small batches to improve performance). Each response will be stored as text in a table with the same number of rows as the input.

This configuration can be used in both the load script and chart expressions.

### OpenAI Chat Completions API

This configuration sends each row of data as a request to the OpenAI Chat Completions API. In this case, the requests are made with the “user” message role, and each row of data from Qlik is sent as a separate request.

Information noteSending multiple rows as a chat context is not supported. You need to include all the questions in a single request row.

This configuration can be used in both the load script and chart expressions.

## Creating the connection

You can create a connection to the Azure OpenAI analytics connector from the Create page of the Analytics [activity center](#glossary-0 "Glossary term"), or from the Data load editor in an application you have already created.
Follow the steps below to create a connection.

For information about how to set the parameter values, see [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference).

Do the following:

1. Create a new Qlik Sense application or script and open Data load editor or Script.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Under Analytics sources, click Azure OpenAI.
5. Choose the Configuration needed. For more information about each available option, see [*Available connector configurations*](#Availabl).
6. Enter your Azure OpenAI API Key.
7. Enter the Azure API Version. This field is already populated with the current default.
8. Adjust any of the other default parameter values as required.

   For additional descriptions of the parameters, see [*Configurable settings*](#Configur).

   Information noteYou will almost always need to alter the Max Tokens parameter value in order for the connection to function properly for your needs. This parameter controls the size of the response that will be generated.
9. Click Create.

The data connection is saved to the space where the application is created, so it can be reused in other Qlik Sense applications or scripts.

Once you have created the connection, you can use it to load data to send to Azure OpenAI. Additionally, you can use it in chart expressions. For more information, see [*Select and load data from an Azure OpenAI connection*](ac-azure-openai-load.htm) and [*Using Azure OpenAI connections in visualization expressions*](ac-azure-openai-use.htm).

## Configurable settings

The settings in the following table can be configured in the connection dialog.

Configurable settings in the connection dialog

| Field | Description |
| --- | --- |
| Select Configuration | Under Configuration, select the configuration for the connector. For more information, see [*Available connector configurations*](#Availabl). |
| Authorization | Enter the Azure OpenAI API Key. For more information, see [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference). |
| Azure OpenAI Request | - Azure Resource Name: The resource project you have set up in Microsoft Azure.  Azure Deployment Name: The specific deployment you have set up for the OpenAI model you have chosen. - Azure API Version: The API version in Azure. This is pre-populated with the current default value. |
| OpenAI Request | - Temperature: The sampling temperature to use. - Max Tokens: This parameter adjusts the maximum number of tokens to be generated. In other words, it controls the size of the response that will be generated. You will almost always need to alter the default value in order for the connection to function properly for your needs. - Top P: Adjusts the nucleus sampling. This can be altered as an alternative to Temperature sampling. - Frequency Penalty: The degree to which the model penalizes new tokens that are repeated verbatim from existing tokens. - Presence Penalty: The degree to which the model penalizes new tokens which are already contained in the text up until the point at which they are introduced. - User: The end-user ID, which can help in monitoring policy violations. |
| Association | Specify an Association Field, a field from the input data table containing a unique identifier.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

## Learn more

- [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
