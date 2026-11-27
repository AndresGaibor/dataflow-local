---
title: "Using Qlik Predict connections in visualization expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-qlik-automl-connector-use.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik Predict analytics source"]
---

# Using Qlik Predict connections in visualization expressions

You can use the analytic connections in [visualization](#glossary-0 "Glossary term") expressions. The syntax when using the analytic connections in expressions must follow the server-side extensions syntax.

Data should be processed in a visualization expression only when it will dynamically change based on the input from a user. If the transaction from the data model will always be the same, the prediction should instead be calculated in the [load script](#glossary-1 "Glossary term") and cached in the data model.

If the use case is based on user input, you can use an analytic connection and corresponding server-side extension syntax in your chart expression to create interactive [charts](#glossary-2 "Glossary term") that visualize data received from the model endpoints.

Do the following:

1. When editing a visualization, click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to enter the expression editor.
2. In the expression editor, enter an expression in the expression field. The expression must be constructed using the server side extension syntax.

Information noteDepending on the data size and the called machine learning endpoints, the responsiveness of charts containing analytic connections could be impacted, since data is sent to and returned from Qlik Predict for calculations.

[Working with the expression editor](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Expressions/work-with-expression-editor.htm)

[Server side extensions syntax](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/sse-syntax.htm)

## Requirements for auto-engineered date features

When you use a Qlik Predict analytics connection in a visualization expression, you are running predictions with a Qlik Predict deployed model.

There are specific requirements for date formatting when running predictions from a model trained on date feature columns. For these columns, the data you provide to the Qlik Predict analytics connection must meet the following requirements:

- Date and datetime values must be strings formatted in accordance with ISO 8601 standards. Examples:

  - 2020-01-14
  - 2020-01-14T00:00:00.000Z
- The parent date—the feature from which the date parts were derived—must be included in its entirety. For example, your model might only use a Year feature but you still need to provide the date in ISO 8601-compliant format.
- Data within each column needs to be of the same time zone.

The above requirements:

- Only apply for features trained with date feature engineering. If the feature type is manually changed to the categorical feature type, these requirements do not apply. If the feature type has been changed to categorical, provide the column, in the date format in which it was originally used for training, in the apply data.
- Do not apply to time series models.

For more information about working with date features in predictions, see [*Working with date features in predictions*](../AutoML/date-features-predictions.htm).

## Examples

Here is an example of a call made to a Qlik Predict deployment that provides banking customer churn prediction.

```
sum(aggr(endpoints.ScriptEvalEx('SNNNNNNNNNNSSNNSNNNNNSSSSSNSNNSS','{"RequestType":"endpoint", "endpoint":{"connectionname":"Qlik_Predict_Churn", "column":"Churned_yes"}}',
id_loan,
CurrentBalance,
loan_age,
delq_sts,
Margin,
countLatePayment,
RefinanceRateRelativity,
RealGDP,
ChangeUnemploymentRate,
CurrentLCV,
fico,
flag_fthb,
cd_msa,
mi_pct,
cnt_units,
occpy_sts,
cltv,
dti,
orig_upb,
ltv,
int_rt + vInterestRateShift as int_rt,
channel,
ppmt_pnlty,
prod_type,
st,
prop_type,
zipcode,
loan_purpose,
orig_loan_term,
cnt_borr,
flag_sc,
customerFeedback
),id_loan))
```

## Learn more

- [*Example - What-if analysis with the Qlik Predict analytics connector*](../AutoML/example-what-if-analysis.htm)
- [*Server side extensions syntax*](sse-syntax.htm)
