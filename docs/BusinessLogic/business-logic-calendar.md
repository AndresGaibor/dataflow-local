---
title: "Defining analysis periods with calendar periods in Insight Advisor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business-logic-calendar.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Building logical models for Insight Advisor with Business logic"]
---

# Defining analysis periods with calendar periods in Insight Advisor

Define calendar periods for your calendar groups to control the time frames that [Insight Advisor](#glossary-0 "Glossary term") uses when creating [visualizations](#glossary-1 "Glossary term").

Calendar periods define time periods of interest for Insight Advisor to use in analysis in the [logical model](#glossary-2 "Glossary term"). For example, a KPI showing total sales for all time may be less useful than a KPI showing total sales for the current month. You could create a calendar period for the current month and set that as the default period to use with total sales. Calendar periods for logical model are created and managed in Calendar periods.

Calendar periods define single periods of times or comparisons of relative periods of time. For example, you can create calendar periods to:

- Show only the values from this month
- Compare this month to last month
- Compare the current quarter to the current quarter last year

Insight Advisor uses calendar periods when creating charts. Calendar periods enable additional analysis types. You can select and apply calendar periods when editing a chart in Insight Advisor. You can set a default calendar period to be used with a group when Insight Advisor creates charts for fields and master items in that group. Default calendar periods are set in Behaviors. For more information, see [*Default calendar period*](business-logic-behaviors.htm#Default).

Information note

Calendar periods is not available when a tenant is licensed for Qlik Answers. For more information, see [*Qlik Answers*](../QlikAnswers/Qlik-Answers.htm).

## Creating calendar periods

Create calendar periods from the calendar groups defined in Fields & groups. You can create calendar periods with or without fields that use the autoCalendar function in the data [load script](#glossary-3 "Glossary term").

Information note

You can use the Use Autocalendar option with a custom calendar if it uses the same declared fields as autoCalendar.

### Creating calendar periods using autocalendar

Select the grain for analysis when creating calendar periods using the autocalendar. The grain is for example, month of year or quarter of year. You can then the choose to use most recent value, or create a comparison.

Do the following:

1. Click Create calendar period.
2. Select a calendar group, and then select Use Autocalendar.
3. Enter a name for the calendar period.
4. Select the calendar period grain.
5. Do one of the following:
   - To use the most recent value in the period grain field, select Use last sorted value.
   - To make a comparative calendar period, do one of the following:
     - In Compare, select the period for comparison. Select Last complete period if Insight Advisor should use the last complete period instead of the current period.
     - In Custom, select the period for analysis in Offset, and then select the period for comparison in Compare offset.

       Offset and Compare offset use numeric values, with 0 being the current period.

       For example, if you used quarter of year as your period grain, 0 would be the current period and 3 would be three quarters ago.
6. Click Create.

### Creating calendar periods using a custom calendar

You can create calendar periods without using the autoCalendar in the load script. For example, you may have a custom calendar, or you may want to use custom calendar flags that do not exist in the autoCalendar.

To create a calendar period using a custom calendar, select a calendar group and choose a time [field](#glossary-4 "Glossary term") to aggregate. You then the choose to use most recent value or create a comparison. Two comparison methods are supported:

- Relative: A relative comparison that uses a field containing the relative number of periods ago. The relative period field must contain numeric values that define the relative period from the current date for each value in the aggregated field. You can then select the offset and comparison offset for analysis.

  For example, to do a comparison of this month to last month, select Date as your aggregate field. Next, select MonthsAgo as your relative period field. MonthsAgo uses an expression to evaluate how many months ago each value in Date is from the current month. If the current month is July, values from July would be 0, values from June would by 1, values from May would be 2, and so on. You can then select 0 for your offset and 1 for your compare offset.
- Flag: A flag comparison uses two fields that define two separate flagged periods of time.

  For example, first quarter and second quarter could be two periods used for a flag comparison. The comparison fields must contain binary values indicating which aggregated field values are in the flagged period.

  To compare Quarter 1 to Quarter 2, select Date as the aggregated field. As flag fields, you can then select InQuarter1 and InQuarter2. These fields use expressions to evaluate if values are or are not in Quarter 1 or Quarter 2.

For more examples of calendar periods made using a custom calendar, see [*Step-by-step – Creating calendar periods using a custom calendar*](Example/step-by-step-custom-calendar.htm).

Do the following:

1. Click Create calendar period.
2. Select a calendar group, and then clear the Use Autocalendar check box.
3. Enter a name for the calendar period.
4. Select the aggregated date field to use.
5. Do one of the following:
   - To use the most recent value in the period grain field, select Use last sorted value.
   - To make a comparative calendar period, do one of the following:
     - In Relative, for Relative periods ago, select the field defined in your load script containing the relative time period data for the field selected in Aggregated date. Set the time period for analysis in Offset, and then set time period for comparison in Compare offset.

       Offset and Compare offset use numeric values, with 0 being the current period.
     - In Flag, select the field containing the flag for the current period, and then select the field containing the flag for the comparison period.
6. Click Create.

## Limitations

Business logic calendar periods have the following limitations:

- Default calendar periods are not applied to time-based master [measures](#glossary-5 "Glossary term") that include specific time periods in their expression.
