---
title: "Select and load data from a Meta (Amazon Bedrock) connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-bedrock-meta-load.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Amazon Bedrock analytics sources", "Meta (Amazon Bedrock) analytics source"]
---

# Select and load data from a Meta (Amazon Bedrock) connection

Once you have created a [connection](#glossary-0 "Glossary term"), you can select data and load it into a Qlik Senseapplication or script.
You load data in [Data load editor](#glossary-3 "Glossary term") or Script.

Information note

The Amazon Bedrock - Converse API connector allows you to connect to Amazon Bedrock's universal API for text generation models, including one or more models available through this connector. Consider replacing Anthropic (Amazon Bedrock) connections with Amazon Bedrock - Converse API connections for more advanced functionality. For more information, see [*Amazon Bedrock - Converse API analytics source*](ac-bedrock-converse-api-overview.htm).

In Data load editor or Script, basic communications with an analytic connection are formulated as a script with the following components, at a minimum:

- Table (Resident Table) containing the request field (Data Field) you want to send to AI21 Labs.
- AI21 Labs load statement, which communicates to AI21 Labs through your connection.

In an advanced setup, the request field and association field could technically be defined in a table containing other fields. However, the request field and association field must be contained in the same input table. It is important to be aware that when you link these fields to fields in your data model, responses are generated for each field value.

## Prompt engineering

When writing the requests you are sending to a generative AI model (often known as prompts), follow the guidelines specific to the platform you are interacting with. For information about prompt engineering and some guidelines on how to structure your prompts for Amazon Bedrock connectors, see [Prompt engineering concepts](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html).

You can interact with the Meta (Amazon Bedrock) connector using standard sentence or text formatting. You do not need to prefix or suffix the prompt with any special keywords or strings. See [*Example*](#Example).

## Creating the table of data to be sent to Meta (Amazon Bedrock)

First, a table must be loaded which contains the data you are sending to the model as a request. This table must consist of a single column of data within which each cell represents text to be completed by the model. There can be a second additional field for the Association Field, but this needs to match the field name specified in the configuration. This is a special field that won’t be sent to Meta, but is attached to the responses for the purpose of integrating the interaction data into the data model.

### Considerations for data request volumes

When you load data, every row in the request field will be sent to Meta. Before you interact with a third-party platform, make sure you're aware of how the number of requests, volume of data included in your requests, and your connector configuration affect your financial agreement and billing arrangements with the third party. Higher usage of the external platform could result in higher costs incurred.

## Creating the Meta load statement

You also need to create a load statement, using the extension syntax, to communicate with Meta. This part of the script references your Meta (Amazon Bedrock) connection and specifies the names of the table and fields you are using to send the request data (see above section). It loads a separate table which will contain the model's responses to each row in the request, among other data.

To generate this part of the script, you can use the Select data wizard for the connection you are using. This generates a template script including the names of the properties you provide.

Locate the connection you are using in the Data sources panel of Data load editor or Script, and click ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok.svg). This opens the Select data wizard.

When using the Select data wizard, you need to provide two properties:

- The name of the Resident Table. This is the table with the request being sent to Meta.
- The name of the Data Field. This is the field containing the request data being sent to Meta.

Alternatively, you can add this manually into the script editor without using the wizard.

When you click Insert script, the new table is added to the load script. You can now load the data, inspect the resulting data model, and use the data to create analytics content in your application.

## Example

The following load script requests three completions from Meta.

Here is how it is set up:

- The Resident Table is QuestionsTable.
- The Data Field with the prompts is Question.
- The Association Field is Question\_ID.
- The Meta load statement is contained in the table named Meta.

QuestionsTable:
Load \* Inline [
Question\_ID,Question
1,"show me general ways to help boost a company's sales"
2,"what are the core concepts in accounting?"
3,"how large is the sun?"
];
[Meta]:
LOAD
[generation],
[prompt\_token\_count],
[generation\_token\_count],
[stop\_reason],
[RowId]
EXTENSION endpoints.ScriptEval('{"RequestType":"endpoint", "endpoint":{"connectionname":"Meta\_(Amazon\_Bedrock)"}}', QuestionsTable{Question\_Id,Question});
