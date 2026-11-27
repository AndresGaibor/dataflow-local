---
title: "Creating an OpenAI connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-openai-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "OpenAI analytics source"]
---

# Creating an OpenAI connection

To communicate with the OpenAI platform, create a connection to the OpenAI analytics source.

To communicate with OpenAI, create a connection to the OpenAI analytics source. Create the [connection](#glossary-0 "Glossary term") in the Create page of the Analytics activity center, Data load editor, or Script.

Data received from these connections can be used in the load script and in chart expressions to enhance your Qlik Sense analytics applications.

## Configurations and configurable settings

Set up your OpenAI analytics connection with one of the following configurations. The configurable settings can vary depending on which configuration is used.

### OpenAI Chat Completions API

This configuration sends each row of data as a question to the OpenAI Chat Completions API. Each response is stored as text in a table with the same number of rows as the input.

Information noteSending multiple rows as a chat context is not supported. You need to include all the questions in a single request row.

This configuration can be used in both the load script and chart expressions.

For OpenAI's documentation about the API used by this configuration, see [Chat](https://platform.openai.com/docs/api-reference/chat).

Configurable settings for OpenAI Chat Completions API configuration

| Field | Description |
| --- | --- |
| Select Configuration | Under Configuration, select OpenAI Chat Completion API. |
| Authorization | Enter the OpenAI API Key. For more information, see [*Generating an OpenAI API key*](ac-openai-overview.htm#Generati). |
| OpenAI Request | - OpenAI Model: The model used. - Temperature: The sampling temperature to use. - Max Tokens: This parameter adjusts the maximum number of tokens to be generated. In other words, it controls the size of the response that will be generated. You will almost always need to alter the default value in order for the connection to function properly for your needs. - Top P: Adjusts the nucleus sampling. This can be altered as an alternative to Temperature sampling. - Frequency Penalty: The degree to which the model penalizes new tokens that are repeated verbatim from existing tokens. - Presence Penalty: The degree to which the model penalizes new tokens which are already contained in the text up until the point at which they are introduced. - User: The end-user ID, which can help in monitoring policy violations. |
| Association | Specify an Association Field, a field from the input data table containing a unique identifier.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

### OpenAI Embeddings

This configuration sends rows of input text to the OpenAI Embeddings API. OpenAI returns a separate vector representation of each input. This vector representation is in a form which can be consumed by machine learning models.

For OpenAI's documentation about the API used by this configuration, see [Embeddings](https://platform.openai.com/docs/api-reference/embeddings).

Configurable settings for OpenAI Embeddings configuration

| Field | Description |
| --- | --- |
| Select Configuration | Under Configuration, select OpenAI Embeddings. |
| Authorization | Enter the OpenAI API Key. For more information, see [*Generating an OpenAI API key*](ac-openai-overview.htm#Generati). |
| OpenAI Request | - OpenAI Model: The model used. - User: The end-user ID, which can help in monitoring policy violations. |
| Association | Specify an Association Field, a field from the input data table containing a unique identifier.  It is required to include this field in the source data when making an endpoint request for the results table returned to be associated with the source field table using a key. The designated field will be returned as a field in the response and enable the response to be associated with the source data in the data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name is used if you do not enter a name. |

## Creating the connection

You can create a connection to the analytic connector from the Analytics activity center, from Data load editor in an existing application, or from Script in an existing script.
Follow the steps below to create a connection.

Do the following:

1. Create a new Qlik Sense application or script. Open Data load editor or Script.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Under Analytics sources, click OpenAI.
5. Choose the Configuration needed. For more information about each available option, see [*Configurations and configurable settings*](#Configur2).
6. Enter your OpenAI API Key. For more information, see [*Generating an OpenAI API key*](ac-openai-overview.htm#Generati).
7. Under OpenAI Model, select the OpenAI model you want to use.
8. Adjust any of the other default parameter values as required. These parameters are described in OpenAI's API documentation. For more information, see [Chat](https://platform.openai.com/docs/api-reference/chat), [Completions](https://platform.openai.com/docs/api-reference/completions), and [Embeddings](https://platform.openai.com/docs/api-reference/embeddings).

   For additional descriptions of the parameters, see [*Configurations and configurable settings*](#Configur2).

   Information noteYou will almost always need to alter the Max Tokens parameter value in order for the connection to function properly for your needs. This parameter controls the size of the response that will be generated.
9. Click Create.

The data connection is saved to the space where the application is created, so it can be reused in other Qlik Sense applications and scripts. It is also listed under Data connections in Data load editor or Script.

Once you have created the connection, you can use it to load data with the requests and the platform's responses to them. Additionally, you can use it in chart expressions. For more information, see [*Select and load data from an OpenAI connection*](ac-openai-load.htm) and [*Using OpenAI connections in visualization expressions*](ac-openai-use.htm).

## Detailed examples

For full examples of how to work with the OpenAI analytics connector, see [*Tutorial – Using the OpenAI analytics connector in Qlik Cloud*](ac-openai-tutorial.htm).

## Learn more

- [Chat](https://platform.openai.com/docs/api-reference/chat)
- [Completions](https://platform.openai.com/docs/api-reference/completions)
- [Embeddings](https://platform.openai.com/docs/api-reference/embeddings)
- [OpenAI Guides - Embeddings](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)
