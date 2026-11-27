---
title: "Step-by-step – Creating calendar periods using a custom calendar"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/Example/step-by-step-custom-calendar.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Building logical models for Insight Advisor with Business logic", "Defining analysis periods with calendar periods in Insight Advisor"]
---

# Step-by-step – Creating calendar periods using a custom calendar

This step-by-step walkthrough shows you how to create calendar periods using custom calendar fields and flags.

Calendar periods can be made either by using the autocalendar or by using individual date/time fields from your data. You can also use fields containing binary data to flag periods of time for comparative analysis.

There are three kinds of calendar periods you can make with custom calendar data:

- Last sorted value: Last sorted value calendar periods show the most recent period in the selected aggregated [field](#glossary-0 "Glossary term"). In [Insight Advisor](#glossary-1 "Glossary term") analyses supporting comparisons, such as rank analysis, the last sorted value shows the previous period as well.
- Relative comparison: Relative calendar periods use a field containing the relative periods of data from the current date. It provides a comparison between the current or previous period and an older period.
- Flag comparison: Flags use boolean classified fields containing binary data to flag two periods of time for comparative analysis.

Information note

To demonstrate relative time period comparisons, the data source for this app contains data for future dates. The [load script](#glossary-3 "Glossary term") loads data from the data source up to the current date. The results in the images may differ from your results as the time periods shown in the images will have changed.

## Getting started

Download the example package and unzip it:

[Calendar periods example app](/en-US/cloud-services/tutorials/ExampleCalendarPeriodSaaS.zip)

The QVF file contains the following data file:

- TutorialCustomCalendarData.xlsx

  To demonstrate relative comparisons possible through calendar periods, TutorialCustomCalendarData.xlsx contains data for future dates. The app load script updates the in app data for the current date when loaded.

Upload the QVF file and XLSX file to Qlik Sense. Once you have uploaded the app and data file, load the app data in [Data load editor](#glossary-4 "Glossary term").

## Example data

The data is used in this example is loaded with the following load script:

Sales:
LOAD
City,
Country,
Customer,
OrderDate,
Sales,
"Q4-2020",
"Q1-2021",
"Q2-2021",
"Q3-2021",
"Q4-2021",
"Q1-2022",
"Q2-2022",
"Q3-2022",
"Q4-2022",
"Q1-2023",
"Q2-2023",
"Q3-2023",
Month([OrderDate]) AS [Month],
Year([OrderDate]) AS [Year],
Day([OrderDate]) AS [Day],
Dual(Year(OrderDate)&'-'&Month(OrderDate), monthstart(OrderDate)) AS [YearMonth],
12\*Year(Today())+Month(Today())-12\*Year(OrderDate)-Month(OrderDate) AS [MonthsAgo]

FROM [lib://:DataFiles/TutorialCustomCalendarData.xlsx]

(ooxml, embedded labels, table is Sales) Where OrderDate <= Today(1);

The load script creates separate fields for Year, Month, and Day. These three fields are used to create the following calculated fields:

- YearMonth, which has year and month information. This is the primary field for [aggregation](#glossary-5 "Glossary term") in the example.
- MonthsAgo, which calculates if months are from a specific month relative to the current date.

The data also contains several fields for the different quarters covered in the data. These fields contain binary data that indicates to which fiscal quarter each value in the Sales table belongs.

## Tasks

This walkthrough takes you through creating three different kinds of calendar periods:

- Create a custom calendar period without autocalendar
- Create a relative calendar period
- Creating a flag comparison calendar period

### Creating a calendar period using the last sorted value

For the first calendar period, you will create a calendar period for YearMonth using the last sorted value.

Do the following:

1. In the example app, open the app navigation menu.
2. Under Business logic, select Logical model.
3. Click Create calendar period.
4. Select OrderDate.
5. For Calendar period name, enter Last sorted month.
6. For Aggregated date, select YearMonth.
7. Select Use last sorted value.
8. Click Create.

#### Result

Navigate to Sheet and search for show me sales by customer.

Select the [chart](#glossary-6 "Glossary term") sum(Sales) by customer and apply the analysis period Last sorted month. The chart updates to display a comparison between the current month and the previous month.

Last sorted month applied to Customer by sum(Sales) between 2022-Dec and 2023-Jan

![Bar chart showing comparison between sales figures for December 2022 and January 2023 for each customer.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example_custom_calendars_last_sorted_month.png "Click to view full size")

### Creating a relative comparison calendar period

Next, you will make a relative calendar period. A relative calendar period requires:

- An aggregation field containing a period of time (year, month, quarter, etc).
- A field containing the relative positions of dates from that field to today's date.

From these fields, you then define the offset. The offset is the relative difference, in the selected period of time, from the current date for the two periods of comparison. You can compare the current or previous period (set as 0 or 1 in Offset) to an older period up to 12 periods ago (set as a number from 1 to 12 in Compare offset).

For this calendar period, we will use YearMonth as the aggregation field and MonthsAgo as the relative periods field. We want to compare the current month to the same month last year.

Do the following:

1. Click Create calendar period.
2. Select OrderDate.
3. For Calendar period name, enter This month to this month last year.
4. For Aggregated date, select YearMonth.
5. Under Relative periods ago, select MonthsAgo.
6. Under Offset, select 0.
7. Under Compare offset, select 12.
8. Click Create.

#### Result

Navigate to Sheet and search for show me sales by customer.

Select the chart sum(Sales) by customer and apply the analysis period This month to this month last year. The chart updates to display a comparison between the current month and the current month last year.

Customer by sum(Sales) between 2022-Jan and 2023-Jan

![Bar chart showing comparison between sales figures for January 2022 and January 2023 for each customer.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example_custom_calendars_this_month_to_this_month_last_year.png "Click to view full size")

### Creating a flag comparison calendar period

Flag comparison calendar periods use two fields to flag two separate periods for analysis from an aggregated date field.

In the example app data, there are separate fields for the different fiscal quarters. Each field has binary data indicating if the corresponding dates are or are not in the quarter. You will use these with YearMonth to make a flag comparison calendar period.

Do the following:

1. Click Create calendar period.
2. Select OrderDate.
3. For Calendar period name, enter Q4 to Q3
4. For Aggregated date, select YearMonth.
5. Click Flags.
6. Under Current period flag, select Q4-2020.
7. Under Compare period flag, select Q3-2020.
8. Click Create.

#### Result

Navigate to Sheet and search for show me sales by customer.

Select the chart sum(Sales) by customer and apply the analysis period Q4 to Q3. The chart updates to display a comparison between the fourth fiscal quarter of 2020 and the third fiscal quarter of 2020.

Customer by sum(Sales) between Q4 and Q3

![Bar chart comparing sales values between Q3 and Q4 for each customer.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example_custom_calendars_Q3_Q4.png "Click to view full size")
