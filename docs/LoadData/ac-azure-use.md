---
title: "Using Azure ML connections in visualization expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-azure-use.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Azure ML analytics source"]
---

# Using Azure ML connections in visualization expressions

You can use the analytic [connections](#glossary-0 "Glossary term") in [visualization](#glossary-1 "Glossary term") expressions. The syntax when using the analytic connections in expressions must follow the server side extensions syntax.

Data should be processed in a visualization expression only when it will dynamically change based on the input from a user. If the text for text analysis is from the data model and will always be the same, the text analysis should instead be calculated in the [load script](#glossary-2 "Glossary term") and cached in the data model.

If the use case is based on user input, you can use an analytic [connection](#glossary-3 "Glossary term") and corresponding server side extension syntax in your chart expression to create interactive [charts](#glossary-4 "Glossary term") that visualize data received from the model endpoints.

Information noteWhen using Azure ML in a chart expression it is important to provide the datatypes of the fields as Azure needs to process these in the correct string/numeric format. A limitation of server side extensions in chart expressions is that the data types are not automatically worked out as they are in the load script.

Do the following:

1. When editing a visualization, click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to enter the expression editor.
2. In the expression editor, enter an expression in the expression field. The expression must be constructed using the server side extension syntax.

Information noteDepending on the data size and the called machine learning endpoints, the responsiveness of charts containing analytic connections could be impacted due to that data is sent to and returned from Azure services for calculations.

[Working with the expression editor](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Expressions/work-with-expression-editor.htm)

[Server side extensions syntax](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/sse-syntax.htm)

## Example

Here is an example of a call made to an external model that does banking customer churn prediction:

sum(aggr(endpoints.ScriptEvalEx('SNNNNNNNNNNSSNNSNNNNNSSSSSNSNNSS','{"RequestType":"endpoint", "endpoint":{"connectionname":"$(vConnectionName)"}}',
id\_loan,
CurrentBalance,
loan\_age,
delq\_sts,
Margin,
countLatePayment,
RefinanceRateRelativity,
RealGDP,
ChangeUnemploymentRate,
CurrentLCV,
fico,
flag\_fthb,
cd\_msa,
mi\_pct,
cnt\_units,
occpy\_sts,
cltv,
dti,
orig\_upb,
ltv,
int\_rt + vInterestRateShift as int\_rt,
channel,
ppmt\_pnlty,
prod\_type,
st,
prop\_type,
zipcode,
loan\_purpose,
orig\_loan\_term,
cnt\_borr,
flag\_sc,
customerFeedback
),id\_loan))
