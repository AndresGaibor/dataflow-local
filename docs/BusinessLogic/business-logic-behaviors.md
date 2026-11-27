---
title: "Applying behaviors to logical models for Insight Advisor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business-logic-behaviors.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Building logical models for Insight Advisor with Business logic"]
---

# Applying behaviors to logical models for Insight Advisor

Behaviors enable you to set prefer or deny relationships between measure groups and other groups. You can also use behaviors to enforce value selection in [Insight Advisor](#glossary-0 "Glossary term").

You may have groups that either should be always used together in analysis or never used together in analysis. You also maybe have [field](#glossary-1 "Glossary term") values that you would prefer always been included as selected when fields from a group are being used by Insight Advisor. Behaviors enable you to set these preferences on a group by group basis. Logical model behaviors are created and managed in Behaviors.

The following behaviors are available in logical models:

- Required selections
- Prefer relationship
- Deny relationship
- Default calendar period

You can edit or delete behaviors by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and selecting Edit or Delete.

Information note

Behaviors is not available when a tenant is licensed for Qlik Answers. For more information, see [*Qlik Answers*](../QlikAnswers/Qlik-Answers.htm).

## Required selections

Required selection behavior enables you to specify field values that must be included when using fields from a group. A behavior can include multiple required [selections](#glossary-2 "Glossary term").

For example, you may have fields for Country, Population, and Year. When generating recommendations in Insight Advisor, you might get [charts](#glossary-3 "Glossary term") that use Country and Population, but include the sum of data for all years in the charts. You can use required selection behavior to limit Insight Advisor results to use the current year instead of all time when generating analysis for Population or Country.

## Prefer relationships

Prefer relationship behavior guides Insight Advisor into selecting groups that should be used more often together when generating analysis
. When you specify a prefer relationship, Insight Advisor uses the preferred group when generating results. Prefer relationships are useful when there might be ambiguity .

Prefer relationships does not prevent a group from being used with other groups. It only selects the preferred group when all group choices are equal in the analysis. In analysis where other groups are more appropriate, the non-preferred groups may be used instead.

For example, there are four groups:

- Sales
- Customer
- Product
- Sales Person

Sales has a preferred relationship with Customer. For a breakdown analysis with Sales, Customer is selected over the other groups as it is preferred. For a trend analysis for Sales, Product might be used in the analysis instead.

## Deny relationships

Deny relationship behavior prevents Insight Advisor from using the selected groups together when generating insights. This is useful when some groups in the same package may not be useful to use together in analysis. Deny relationships can also be used to block groups from being used together that could impact application performance. With star schema data models, there may be groups that have one-to-many and many-to-one relationships that complicate analysis. Deny relationships can prevent association between these groups.

Deny relationships are overruled when a user specifically requests insights from the groups that have a deny relationship. For example, Sales and Supplier have a deny relationship. If someone searches 'show me sales', no analysis will be generated that contains Sales and Supplier. If someone searches 'show me sales by supplier', results including Sales and Supplier are generated.

## Default calendar period

Default calendar period behaviors assign calendar periods to be used as the default time period in [visualizations](#glossary-5 "Glossary term") for the selected group. The default calendar period is applied whenever Insight Advisor creates visualizations for fields from that group. Groups can have single default calendar period. Default calendar periods behaviors overrule any default period grains set for a date field.

Calendar periods are generally applied to analyses in the following way:

- Fact and rank analyses use the current or first selected period from the calendar period. The previous or second selected period from the calendar period is added to the analyses for comparison.
- Trend analyses and similar analyses only use the aggregated grain from the calendar period.
- Other analyses use the current or first selected period from the calendar period.

For example, you have the group Client Satisfaction that contains client satisfaction data. By default, many of your application's users are only interested in seeing data for the current month. By creating a calendar period for the current month and making it the default calendar period, Insight Advisor visualizations for Client Satisfaction will only show data from the current month.

### Ignoring default calendar periods for select analysis types

You can configure analysis types to ignore parts or all of a default calendar period. This is useful for controlling how default calendar periods are applied more specifically. For example, you may not want a comparison in your fact analyses and only want to view the current period.

You can pick analysis types to ignore period 1 (the previous or second selected period), period 2 (the current or first selected period), or the grain of your calendar period. Ignoring period 1 stops using earlier period in analyses that would compare two periods so that only period 2 is displayed. Ignoring period 2 or the grain stops the calendar period from being used by default with that analysis type. For more information about the different analyses, see [*Insight Advisor analysis types*](../Insights/insight-analysis-types.htm).

## Creating behaviors

Do the following:

1. Click Create behavior.
2. Under Applies to, select a group.
3. Select a behavior type
4. Do one of the following:
   - If configuring a Prefer relationship or a Deny relationship, select the groups to which to apply that relationship.
   - If configuring a Required selection, select if this is a single value. From Require for, select the fields and their required values.

     You can add additional required selections by clicking Add another.
   - If configuring a Default calendar period, select a calendar group and a calendar period from that group. Optionally, specify which analysis types should have exceptions from the default calendar period under Ignore Period 1, Ignore Period 2, and Ignore grain.
5. Click Create.
