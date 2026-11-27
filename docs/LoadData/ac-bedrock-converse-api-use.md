---
title: "Using Amazon Bedrock - Converse API connections in visualization expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-bedrock-converse-api-use.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Amazon Bedrock analytics sources", "Amazon Bedrock - Converse API analytics source"]
---

# Using Amazon Bedrock - Converse API connections in visualization expressions

In addition to adding Amazon Bedrock questions and answers to your application's data model using the load script, you can also perform these operations directly in a chart in your application in analysis mode. Data for a single field is sent back and forth between you and Amazon Bedrock.

In many cases, the code used for a load script connection can be re-purposed for use in a chart, with some differences.

If the use case is based on user input, you can use an analytic connection and corresponding server side extension syntax in your chart expression to create interactive [charts](#glossary-0 "Glossary term") that visualize data received from the model endpoints.

## Considerations for data request volumes

It is recommended to only use Amazon Bedrock - Converse API connections in chart expressions for one or a handful of rows of data. Using chart expressions to send large amounts of data to Amazon Bedrock is not recommended.

It is important to be aware of how many rows you are sending with each request. Errors in configuring the connection in a chart expression can lead to unintentionally large requests (for example, identical rows with the same question due to improper use of the data model in a chart). Before you interact with a third-party platform, make sure you're aware of how the fields used in the chart expression calculation, and their place in the data model, affect your financial agreement and billing arrangements with the third party. Higher usage of the external platform could result in higher costs incurred.

Follow these guidelines to moderate and limit the size of your requests:

- When working with chart expressions, only use the connection in a Text object (from the Dashboard bundle). Using the Amazon Bedrock - Converse API connection in a Table object is strongly discouraged, especially if you are adding the expression to a table with one or more dimensions already added.
- If the chart expression is linked to your application's data model, use an if statement in the expression to only calculate the chart when a single selection is made in the application. This drastically reduces the row count in the requests that your chart will send to Amazon Bedrock.
- If you are using the Amazon Bedrock - Converse API connection to send large requests, use the connection in your load script instead of in a chart expression, so that the data is pre-loaded into your data model.

## Prompt engineering

When writing the requests you are sending to a generative AI model (often known as prompts), follow the guidelines specific to the platform you are interacting with. For information about prompt engineering and some guidelines on how to structure your prompts for Amazon Bedrock connectors, see [Prompt engineering concepts](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html).

You can interact with the Amazon Bedrock - Converse API connector using standard sentence or text formatting. You do not need to prefix or suffix the prompt with any special keywords or strings. See [*Quick examples*](#Quick).

## Creating the chart expression

Do the following:

1. When editing a visualization, click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to enter the expression editor.
2. In the expression editor, enter an expression in the expression field. The expression must be constructed using the server side extension syntax.

## Quick examples

Here you can find sample expressions that can be used when getting started with the Amazon Bedrock - Converse API connector. Consider the following details:

- Only use the expressions with a Text object (from the Dashboard bundle). See [*Text*](../Visualizations/DashboardBundle/text-object.htm).
- Consider adding an if statement to your expressions to control when the chart is re-calculated, and to update depending on user selections in the application.
- For the expressions to work, you must substitute the connectionname value and any field names to match your own connections and scripts.

### Example 1

This statement will return the response to a single question, which has been entered into the expression.

Warning note

This expression does not use an if statement, and is not advised to be used if tied to a field in your data model. It is only suitable for use in a standalone expression with a single input cell containing a hard-coded value.

```
endpoints.ScriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":"My_Bedrock_Connection","column":"text"}}', 'Translate this text from english to spanish: The sun was rising over the new tomorrow with a tinge of excitement.')
```

### Example 2

This is a statement which can be used in a Text object (from the Dashboard bundle) linked to a Variable input control. The chart is only calculated when input is entered. When the user types input into the object and presses Enter, the chart displays the model's response to their input.

For a similar walkthrough with a different connector, see [*Exercise: Creating a text input box using a variable*](ac-openai-tutorial-example-3.htm#Exercise).

```
if(vQuestion <> '', endpoints.scriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":"My_Bedrock_Connection","column":"text"}}',vQuestion))
```

### Example 3

In this example, the chart is only calculated if one distinct value has been selected from the field IssueCategory in the application's data model. A request is sent to the model requesting a sample response from a technical support department about a general type of issue, a list of which is contained in the IssueCategory field. The chart is updated depending on the value selected by the user.

```
if(count(distinct [IssueCategory]) = 1, endpoints.ScriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":"My_Bedrock_Connection","column":"text"}}', 'Write me a sample response from a technical support department for a customer complaint about ' & [IssueCategory]'))
```
