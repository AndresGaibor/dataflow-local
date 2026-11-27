---
title: "Using Hugging Face connections in visualization expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-hugging-face-use.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Hugging Face analytics source"]
---

# Using Hugging Face connections in visualization expressions

In addition to adding Hugging Face input and responses to your data model using the load script, you can also perform these operations directly in a chart in your application in analysis mode. Data for a single field is sent back and forth between you and Hugging Face.

In many cases, the code used for a load script connection can be re-purposed for use in a chart, with some differences.

If the use case is based on user input, you can use an analytic connection and corresponding server side extension syntax in your chart expression to create interactive [charts](#glossary-0 "Glossary term") that visualize data received from the model endpoints.

## Considerations for data request volumes

It is recommended to only use Hugging Face connections in chart expressions for one or a handful of rows of data. Using chart expressions to send large amounts of data to Hugging Face is not recommended.

It is important to be aware of how many rows you are sending with each request. Errors in configuring the connection in a chart expression can lead to unintentionally large requests (for example, identical rows with the same question due to improper use of the data model in a chart). Before you interact with a third-party platform, make sure you're aware of how the fields used in the chart expression calculation, and their place in the data model, affect your financial agreement and billing arrangements with the third party. Higher usage of the external platform could result in higher costs incurred.

Follow these guidelines to moderate and limit the size of your requests:

- Many of these connector configurations return multiple interrelated response fields. If you are using the connection in a scenario where you need only one of the response fields in your chart, use the expressions with a Text object (from the Dashboard bundle). If you do need to represent multiple response fields in tabular form, use the connector in the load script instead. Connecting these expressions to fields in your data model can easily result in unintentionally large requests if configured incorrectly. It is instead recommended to use the load script in these scenarios.
- Consider adding an if statement to your expressions to control when the chart is re-calculated, and to update depending on user selections in the application.

## Creating the chart expression

Do the following:

1. When editing a visualization, click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to enter the expression editor.
2. In the expression editor, enter an expression in the expression field. The expression must be constructed using the server side extension syntax.

## Learn more

- [*Server side extensions syntax*](sse-syntax.htm)
- [*if Script and chart function*](../Scripting/ConditionalFunctions/if.htm)
- [*GetSelectedCount - chart function*](../ChartFunctions/FieldFunctions/getselectedcount.htm)
- [*Using variables in expressions*](../Variables/work-with-variables.htm)
