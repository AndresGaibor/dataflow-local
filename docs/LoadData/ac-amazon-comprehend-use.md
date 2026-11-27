---
title: "Using Amazon Comprehend connections in visualization expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-amazon-comprehend-use.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Amazon Comprehend analytics source"]
---

# Using Amazon Comprehend connections in visualization expressions

You can use the analytic connections in [visualization](#glossary-0 "Glossary term") expressions. The syntax when using the analytic connections in expressions must follow the server side extensions syntax.

Data should be processed in a visualization expression only when it will dynamically change based on the input from a user. If the text for text analysis is from the data model and will always be the same, the text analysis should instead be calculated in the [load script](#glossary-1 "Glossary term") and cached in the data model.

If the use case is based on user input, you can use an analytic connection and corresponding server side extension syntax in your [chart](#glossary-2 "Glossary term") expression to create interactive charts that visualize data received from the model endpoints.

Do the following:

1. When editing a visualization, click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to enter the expression editor.
2. In the expression editor, enter an expression in the expression field. The expression must be constructed using the server side extension syntax.

Information noteDepending on the data size and the called machine learning endpoints, the responsiveness of charts containing analytic connections could be impacted due to that data is sent to and returned from Amazon services for text analysis.

[Working with the expression editor](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Expressions/work-with-expression-editor.htm)

[Server side extensions syntax](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/sse-syntax.htm)

## Example

You can have a variable containing some user input text that can be scored for sentiment.

endpoints.ScriptAggrStr('{"RequestType":"endpoint", "endpoint":{"connectionname":":Amazon\_Comprehend\_Sentiment","parameters":{"languagecode":"$(vLanguage)"}}}',vText)

The above example uses the function “ScriptAggrStr” – “Aggr” to send a single row contained in the variable vText. String values are being sent and returned.

The example uses a pre-set language in the connection settings. You can change these settings dynamically in the request script, by providing a parameter in the script to change the language code. In this case the variable vLanguage is set for the parameter languagecode to dynamically change the language based on the users input without needing to create a new connection.
