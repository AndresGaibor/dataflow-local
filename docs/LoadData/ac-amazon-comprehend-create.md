---
title: "Creating an Amazon Comprehend connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-amazon-comprehend-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Amazon Comprehend analytics source"]
---

# Creating an Amazon Comprehend connection

Amazon Comprehend [connections](#glossary-0 "Glossary term") are created in [Data load editor](#glossary-1 "Glossary term") or Script.

Once you have created a connection, you can select data from the available tables to send to Amazon Comprehend for calculations, and then load that data into your application. This connection can not only be used in your data [load script](#glossary-3 "Glossary term") but also in chart expressions to call model endpoints and perform real time chart expression calculations.

You must know the settings and access credentials to the Amazon Comprehend service that you want to connect to.

## Configurable settings

The following settings can be configured in the connection dialog:

Configurable settings in the connection dialog

| Field | Description |
| --- | --- |
| Select configuration | Drop-down menu item to select the configuration which determines which Amazon Comprehend service to use for text analysis.  Supported configurations:   - Sentiment Analysis - Key phrase Extraction - Language Detection - Entity Recognition - Syntax Analysis - Personally Identifiable Information (PII) Detection |
| Settings | The following settings are available:   - AWS Region: Select the region you intend to use for the comprehend service. - Use FIPS Endpoint: Specify if you need to use a FIPS compliant endpoint.  This will only work if you choose a region that supports FIPS and for most users should be left as the default “No”. - Language Code: Specify the Language Code.  This is the language of the text that you intend to do text analysis on.  Information noteLanguage Code is not available for Personally Identifiable Information (PII) Detection as this configuration is English only. |
| Authentication | Provide the AWS authentication Access key and Secret key for the Amazon Comprehend endpoints. These need to be created with access to the right policy permissions.  The authentication properties can be found in the AWS console and need to be input every time the connection needs to be re-authenticated. |
| Association Field | A field from the input data table containing a unique identifier.  It is recommended to use an association field when creating an analytic connection to ensure a relationship between the generated content from machine learning the model and the source data maintained in the Qlik Sense data model. This can be any field with a unique ID, either from the source data or as part of the table load process. |
| Name | The name of the connection. The default name will be used if you do not enter a name. |

## Creating a new connection

Do the following:

1. Access the connector through Data load editor or Script.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Select Amazon Comprehend from the list of data connectors.
5. Fill out the connection dialog fields.
6. Click Create.

Your connection is now listed under Data connections.
