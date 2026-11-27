---
title: "Select and load data from an OpenAI connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-openai-load.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "OpenAI analytics source"]
---

# Select and load data from an OpenAI connection

Once you have created a [connection](#glossary-0 "Glossary term"), you can select data and load it into a Qlik Sense application or script. You load data in Data load editor or Script.

In Data load editor or Script, basic communications with an analytic connection are formulated as a script with the following components, at a minimum:

- Table (Resident Table) containing the request field (Data Field) you want to send to OpenAI.
- OpenAI load statement, which communicates to OpenAI through your connection.

In an advanced setup, the request field and association field could technically be defined in a table containing other fields. However, the request field and association field must be contained in the same input table. It is important to be aware that when you link these fields to fields in your data model, responses are generated for each field value.

## Creating the table of data to be sent to OpenAI

First, a table must be loaded which contains the data you are sending to the model as a request. This table must consist of a single column of data within which each cell represents text to be completed by the model. There can be a second additional field for the Association Field, but this needs to match the field name specified in the configuration. This is a special field that won’t be sent to OpenAI, but is attached to the responses for the purpose of integrating the interaction data into the data model.

### Considerations for data request volumes

When you load data, every row in the request field will be sent to OpenAI. Before you interact with a third-party platform, make sure you're aware of how the number of requests, volume of data included in your requests, and your connector configuration affect your financial agreement and billing arrangements with the third party. Higher usage of the external platform could result in higher costs incurred.

## Creating the OpenAI load statement

You also need to create a load statement, using the extension syntax, to communicate with OpenAI. This part of the script references your OpenAI connection and specifies the names of the table and fields you are using to send the request data (see above section). It loads a separate table which will contain the model's responses to each row in the request, among other data.

To generate this part of the script, you can use the Select data wizard for the connection you are using. This generates a template script including the names of the properties you provide.

Locate the connection you are using in the Data sources panel of Data load editor or Script, and click ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok.svg). This opens the Select data wizard.

When using the Select data wizard, you need to provide two properties:

- The name of the Resident Table. This is the table with the request being sent to OpenAI.
- The name of the Data Field. This is the field containing the request data being sent to OpenAI.

Alternatively, you can add this manually into the script editor without using the wizard.

When you click Insert script, the new table is added to the load script. You can now load the data, inspect the resulting data model, and use the data to create analytics content in your application.

## Detailed examples

For full examples of how to add OpenAI requests to your data model, see [*Tutorial – Using the OpenAI analytics connector in Qlik Cloud*](ac-openai-tutorial.htm).
