---
title: "Select and load data from an Anthropic (Amazon Bedrock) connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-bedrock-anthropic-load.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Amazon Bedrock analytics sources", "Anthropic (Amazon Bedrock) analytics source"]
---

# Select and load data from an Anthropic (Amazon Bedrock) connection

Once you have created a [connection](#glossary-0 "Glossary term"), you can select data and load it into a Qlik Sense application or script.
You load data in [Data load editor](#glossary-3 "Glossary term") or Script.

Information note

The Amazon Bedrock - Converse API connector allows you to connect to Amazon Bedrock's universal API for text generation models, including one or more models available through this connector. Consider replacing Anthropic (Amazon Bedrock) connections with Amazon Bedrock - Converse API connections for more advanced functionality. For more information, see [*Amazon Bedrock - Converse API analytics source*](ac-bedrock-converse-api-overview.htm).

In Data load editor or Script, basic communications with an analytic connection are formulated as a script with the following components, at a minimum:

- Table (Resident Table) containing the request field (Data Field) you want to send to Anthropic.
- Anthropic load statement, which communicates to Anthropic through your connection.

In an advanced setup, the request field and association field could technically be defined in a table containing other fields. However, the request field and association field must be contained in the same input table. It is important to be aware that when you link these fields to fields in your data model, responses are generated for each field value.

## Prompt engineering

When writing the requests you are sending to a generative AI model (often known as prompts), follow the guidelines specific to the platform you are interacting with. For information about prompt engineering and some guidelines on how to structure your prompts for Amazon Bedrock connectors, see [Prompt engineering concepts](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html).

### Constructing prompts for the Anthropic - Claude (Messages API) configuration

The Anthropic - Claude (Messages API) configuration connects to the Messages API.

When using this configuration, prompts do not require any specific syntax. For a full example, see [*Examples*](#Example).

### Constructing prompts for the Anthropic - Claude configuration

You can use the Anthropic - Claude configuration to connect to several legacy Claude models.

Prompts written for this configuration require specific syntax in order to return completions successfully. Here are the requirements:

- Each prompt must be prefixed with the text Human:
- Each prompt must be suffixed with the text Assistant:
- The Human: prefix must have two preceding carriage returns. This is accomplished by adding chr(10) & chr(10) to the expression, before the prefix.
- The Assistant: suffix must have two preceding carriage returns. This is accomplished by adding chr(10) & chr(10) to the expression, before the suffix.

For information about how to structure and format a Claude prompt, see [Constructing a prompt](https://docs.anthropic.com/claude/docs/constructing-a-prompt).

Note that there are multiple ways in which this can be done in a script. For a full example, see [*Examples*](#Example).

## Creating the table of data to be sent to Anthropic

First, a table must be loaded which contains the data you are sending to the model as a request. This table must consist of a single column of data within which each cell represents text to be completed by the model. There can be a second additional field for the Association Field, but this needs to match the field name specified in the configuration. This is a special field that won’t be sent to Amazon Titan, but is attached to the responses for the purpose of integrating the interaction data into the data model.

### Considerations for data request volumes

When you load data, every row in the request field will be sent to Anthropic. Before you interact with a third-party platform, make sure you're aware of how the number of requests, volume of data included in your requests, and your connector configuration affect your financial agreement and billing arrangements with the third party. Higher usage of the external platform could result in higher costs incurred.

## Creating the Anthropic load statement

You also need to create a load statement, using the extension syntax, to communicate with Anthropic. This part of the script references your Anthropic (Amazon Bedrock) connection and specifies the names of the table and fields you are using to send the request data (see above section). It loads a separate table which will contain the model's responses to each row in the request, among other data.

To generate this part of the script, you can use the Select data wizard for the connection you are using. This generates a template script including the names of the properties you provide.

Locate the connection you are using in the Data sources panel of Data load editor or Script, and click ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok.svg). This opens the Select data wizard.

When using the Select data wizard, you need to provide two properties:

- The name of the Resident Table. This is the table with the request being sent to Anthropic.
- The name of the Data Field. This is the field containing the request data being sent to Anthropic.

Alternatively, you can add this manually into the script editor without using the wizard.

When you click Insert script, the new table is added to the load script. You can now load the data, inspect the resulting data model, and use the data to create analytics content in your application.

## Examples

### Anthropic - Claude (Messages API)

The following load script requests three completions from Anthropic, via the Anthropic - Claude (Messages API) configuration.

For further information about writing prompts, see [*Prompt engineering*](#Prompt).

Here is how it is set up:

- The Resident Table is QuestionsClaude.
- The Data Field with the prompts is Question.
- The Association Field is Question\_ID.
- The Anthropic load statement is contained in the table named Anthropic.

```
QuestionsClaude:

Load * Inline [

Question_ID,Question

1,"show me general ways to help boost a company's sales"
2,"what are the core concepts in accounting?"
3,"how large is the sun?"
];

[Anthropic]:
LOAD
[text],
[stop_reason],
[input_tokens],
[output_tokens],
[model],
[id],
[Question_ID]
EXTENSION endpoints.ScriptEval('{"RequestType":"endpoint", "endpoint":{"connectionname":"Anthropic_(Amazon_Bedrock)"}}', QuestionsClaude);
```

### Anthropic - Claude

The following load script requests a completion from Anthropic, via the Anthropic - Claude configuration. For details about the required syntax, see [*Constructing prompts for the Anthropic - Claude configuration*](#LegacyClaudePrompt1).

For further information about writing prompts, see [*Prompt engineering*](#Prompt).

Here is how it is set up:

- The Resident Table is QuestionsClaude.
- The Data Field with the prompts is Intputtextclaude.
- The Association Field is RowId.
- The Anthropic load statement is contained in the table named Anthropic.

```
QuestionsClaude:

load RowNo() as RowId,
chr(10) & chr(10) & 'Human:' & Inputtext & chr(10) & chr(10) & 'Assistant:' as Inputtextclaude
Inline [
Inputtext
What is the time in Germany if it's 6 pm in New York?
](delimiter is \n);

[Anthropic]:
LOAD
[completion],
[stop_reason],
[RowId]
EXTENSION endpoints.ScriptEval('{"RequestType":"endpoint", "endpoint":{"connectionname":"Anthropic_(Amazon_Bedrock)"}}', QuestionsClaude{RowId,Inputtextclaude});
```
