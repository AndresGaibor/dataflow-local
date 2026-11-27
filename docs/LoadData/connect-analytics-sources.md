---
title: "Analytics sources in Qlik Cloud Analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/connect-analytics-sources.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data"]
---

# Analytics sources in Qlik Cloud Analytics

With analytic connections you create a [connection](#glossary-0 "Glossary term") between the Qlik associative engine and machine learning models, exposing REST based API endpoints that are designed to receive and return data. You can connect to third-party models, as well as models deployed from Qlik Predict.

The connections are created in Data load editor or Script. Once you have created a connection, you can use this connection in your data [load script](#glossary-1 "Glossary term") or chart expressions to call external machine learning model endpoints that are deployed on third party services.

The technology is based on Qlik Sense Server-Side Extensions (SSE), and it follows the same usage patterns as for Qlik Sense Enterprise Client-Managed.

Typical use cases for the integration are:

- Sending and returning a table of data in the load script to form a part of the data model at application reload
- Performing a real time chart expression which will be unique to the user’s session state

## A

![Logo icon for Amazon Bedrock AI21 Labs connector](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/amazon-bedrock-AI21Labs-square.png)

### [AI21 Labs (Amazon Bedrock)](ac-bedrock-ai21-overview.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/advanced-analytic-square.png)

### [Advanced Analytics](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-advanced-analytic-overview.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/comprehend-square.png)

### [Amazon Comprehend](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-amazon-comprehend-overview.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/bedrock-square.png)

### [Amazon Bedrock - Converse API](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-bedrock-converse-api-overview.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/sagemaker-square.png)

### [Amazon SageMaker](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-amazon-sagemaker-overview.htm)

![Logo icon for Amazon Bedrock Amazon Titan connector](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/amazon-bedrock-AmazonTitan-square.png)

### [Amazon Titan (Amazon Bedrock)](ac-bedrock-amazon-titan-overview.htm)

![Logo icon for Amazon Bedrock Anthropic connector](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/amazon-bedrock-Anthropic-square.png)

### [Anthropic (Amazon Bedrock)](ac-bedrock-anthropic-overview.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/azure-ml-square.png)

### [Azure ML](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-azure-overview.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/azure-openai-square.png)

### [Azure OpenAI](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-azure-openai-overview.htm)

## C

![Logo icon for Amazon Bedrock Cohere connector](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/amazon-bedrock-Cohere-square.png)

### [Cohere (Amazon Bedrock)](ac-bedrock-cohere-overview.htm)

## D

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/databricks-square.png)

### [Databricks MLflow](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-databricks-mlflow-overview.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/datarobot-square.png)

### [DataRobot](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-datarobot-overview.htm)

## G

![Logo icon for Google AI - Gemini connector](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/gemini-square.png)

### [Google AI - Gemini](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-google-ai-overview.htm)

## H

![Logo icon for Hugging Face connector](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/hugging-face-square.png)

### [Hugging Face](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-hugging-face-overview.htm)

## M

![Logo icon for Meta (Amazon Bedrock) connector](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/amazon-bedrock-meta-square.png)

### [Meta (Amazon Bedrock)](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-bedrock-meta-overview.htm)

## O

![Logo icon for OpenAI analytics connector](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/openai-square.png)

### [OpenAI](ac-openai-overview.htm)

## Q

![Logo icon for Qlik Predict analytics connector](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/qlik-predict-square.png)

### [Qlik Predict](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-qlik-automl-connector-overview.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GeoOperations.png)

### [*Qlik GeoOperations analytics sources*](../../Global_Common/GeoOperationsFunctions/GeoOperations.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GeoOperations.png)

### [*Qlik GeoOperations GeoJSON connection*](../../Global_Common/GeoOperationsFunctions/GeoOperationsGeoJSON.htm)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/GeoOperations.png)

### [*Qlik GeoOperations Shapefile analytics connection*](../../Global_Common/GeoOperationsFunctions/GeoOperationsShapefile.htm)
