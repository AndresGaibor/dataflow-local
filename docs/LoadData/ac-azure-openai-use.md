---
title: "Using Azure OpenAI connections in visualization expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-azure-openai-use.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Azure OpenAI analytics source"]
---

# Using Azure OpenAI connections in visualization expressions

In addition to adding Azure OpenAI questions and answers to your application's data model using the load script, you can also perform these operations directly in a chart in your application. Data for a single field is sent back and forth between you and the Azure OpenAI service.

In many cases, the code used for a load script connection can be re-purposed for use in a chart, with some differences.

If the use case is based on user input, you can use an analytic connection and corresponding server side extension syntax in your chart expression to create interactive [charts](#glossary-0 "Glossary term") that visualize data received from the model endpoints.

## Considerations for data request volumes

It is recommended to only use Azure OpenAI connections in chart expressions for one or a handful of rows of data. Using chart expressions to send large amounts of data to the service is not recommended.

It is important to be aware of how many rows you are sending with each request. Errors in configuring the Azure OpenAI connection in a chart expression can lead to unintentionally large requests (for example, identical rows with the same question due to improper use of the data model in a chart). The larger the request you send to the Azure OpenAI service, the higher the financial cost you could incur from Microsoft Azure. Despite there being a request limit of 25 rows per request for this connector, it is still important to recognize this.

Follow these guidelines to moderate and limit the size of your Azure OpenAI requests:

- When working with chart expressions, only use the connection in a Text object (from the Dashboard bundle). Using the Azure OpenAI connection in a Table object is strongly discouraged, especially if you are adding the expression to a table with one or more dimensions already added.
- If the chart expression is linked to your application's data model, use an if statement in the expression to only calculate the chart when a single selection is made in the application. This drastically reduces the row count in the requests that your chart sends to the Azure OpenAI service.
- If you are using an Azure OpenAI connection to send large requests, use the connection in your load script instead of in a chart expression, so that the data is pre-loaded into your data model.

## Quick examples

Here you can find sample expressions that can be used when getting started with the Azure OpenAI connector. Consider the following details:

- Only use the expressions with a Text object (from the Dashboard bundle). See [*Text*](../Visualizations/DashboardBundle/text-object.htm).
- Consider adding an if statement to your expressions to control when the chart is re-calculated, and to update depending on user selections in the application.
- For the expressions to work, you must substitute the connectionname value and any field names to match your own connections and applications.

For additional examples, see [*Tutorial – Using the OpenAI analytics connector in Qlik Cloud*](ac-openai-tutorial.htm).

Chart expression examples for the Azure OpenAI analytics connector

| Connector configuration | Expression | Summary |
| --- | --- | --- |
| OpenAI Chat Completions API | endpoints.ScriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":"My\_OpenAIConnection","column":"choices.message.content"}}', 'Translate this text from english to spanish: The sun was rising over the new tomorrow with a tinge of excitement.') | This statement will return the response to a single question, which has been entered into the expression.  Warning note This expression does not use an if statement, and therefore is not suitable to be used if tied to a field in your data model. It is only suitable for use in a standalone expression with a single input cell containing a hard-coded value. |
| OpenAI Chat Completions API | if(vQuestion <> '', endpoints.scriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":"My\_OpenAI\_Connection\_Rows\_3","column":"choices.message.content"}}',vQuestion)) | This is a statement which can be used in a Text object (from the Dashboard bundle) linked to a Variable input control. The chart is only calculated when input is entered. When the user types input into the object and presses Enter, the chart displays the model's response to their input. |
| OpenAI Chat Completions API | if(GetSelectedCount(BusinessTopic)=1, endpoints.ScriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":"My\_OpenAI\_Connection\_Rows\_3", "column":"choices.message.content"}}', 'What are people saying about ' & 'BusinessTopic'), 'Please select a single value for BusinessTopic.') | This is a complex if statement in which the chart is only calculated if the user has selected one value for the field BusinessTopic. The chart only updates if the user has made this selection in the application, and if they have not, the chart will display the following alternate message: Please select a single value for BusinessTopic. |
| OpenAI Chat Completions API | if( count(distinct [IssueCategory]) = 1, endpoints.ScriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":"My\_OpenAI\_Connection\_Chat\_3\_5","column":"choices.message.content"}}', 'write me a sample response from a technical support department for a customer complaint about ' & [IssueCategory])) | In this example, the chart is only calculated if one distinct value has been selected from the field IssueCategory in the application's data model. A request is sent to ask for a sample response from a technical support department about a general type of issue, a list of which is contained in the IssueCategory field. The chart is updated depending on the value selected by the user. |

## Detailed examples

Examples showing how to use the Azure OpenAI connection in chart expressions can be found in the tutorial for the OpenAI connector. Note that the Azure OpenAI connector communicates with the models through the Microsoft Azure platform instead of the OpenAI platform.

[*Tutorial – Using the OpenAI analytics connector in Qlik Cloud*](ac-openai-tutorial.htm)

[*Examples – Creating load scripts and chart expressions for the OpenAI analytics connector*](ac-openai-tutorial-example-3.htm)

[*OpenAI analytics connector – Interactive example*](ac-openai-tutorial-example-interactive.htm)

## Learn more

- [*Server side extensions syntax*](sse-syntax.htm)
- [*GetSelectedCount - chart function*](../ChartFunctions/FieldFunctions/getselectedcount.htm)
- [*Using variables in expressions*](../Variables/work-with-variables.htm)
