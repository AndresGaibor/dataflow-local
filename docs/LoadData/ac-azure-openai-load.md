---
title: "Select and load data from an Azure OpenAI connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-azure-openai-load.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Azure OpenAI analytics source"]
---

# Select and load data from an Azure OpenAI connection

Once you have created a [connection](#glossary-0 "Glossary term"), you can select data and load it into a Qlik Sense application or script.
You load data in [Data load editor](#glossary-3 "Glossary term") or Script.

In Data load editor and Script, communications with an Azure OpenAI analytics connection are formulated as a script with the following components:

- A table containing the request you want to send to the Azure OpenAI service
- A load statement, which communicates to the Azure OpenAI service through your connection

## Creating the table of data to be sent to Microsoft Azure

First, a table must be loaded which contains the data you are sending to the Azure OpenAI service as a request. This table must consist of a single column of data within which each cell represents text to be completed by the generative AI model. There can be a second additional field for the Association Field, but this needs to match the field name specified in the configuration. This is a special field that won’t be sent to Microsoft Azure, but is attached to the responses for the purpose of generating a Qlik data model.

### Considerations for data request volumes

Every row in the table for a request will be sent to the Azure OpenAI service. Each request costs money, and increased row counts in your request also come with increased costs billed by Microsoft Azure.

## Creating the load statement

You also need to create a load statement, using the extension syntax, to communicate with the Azure OpenAI service. This part of the script references your analytics connection and specifies the names of the table and fields you are using the send the request data (see above section). It loads a separate table which will contain the model's responses to each row in the request, among other data.

To generate this part of the script, you can use the Select data wizard for the connection you are using. This generates a template script including the names of the properties you provide.

Locate the connection you are using in the Data sources panel of Data load editor or Script, and click ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok.svg). This opens the Select data wizard.

When using the Select data wizard, you need to provide two properties:

- The name of the Resident Table. This is the table with the request being sent to the Azure OpenAI service.
- The name of the Data Field. This is the field containing the request data being sent to Azure OpenAI service.

Alternatively, you can add this manually into the script editor without using the wizard.

When you click Insert script, the new table is added to the load script. You can now load the data, inspect the resulting data model, and use the data to create analytics content in your application.

## Examples

Examples showing how to use the Azure OpenAI connection in the load script can be found in the tutorial for the OpenAI connector. Note that the Azure OpenAI connector communicates with the models through the Microsoft Azure platform instead of the OpenAI platform.

- [*Tutorial – Using the OpenAI analytics connector in Qlik Cloud*](ac-openai-tutorial.htm)
- [*Examples – Creating load scripts and chart expressions for the OpenAI analytics connector*](ac-openai-tutorial-example-3.htm)
- [*OpenAI analytics connector – Interactive example*](ac-openai-tutorial-example-interactive.htm)
