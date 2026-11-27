---
title: "Date & time fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Assets/date-time-fields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Using data assets in visualizations", "Fields"]
---

# Date & time fields

Expand/Collapse all

# Date & time fields

If you are working with fields containing date or timestamp information in your application, you can define a number of related attributes of a date, for example, year or week, and use them in your [visualization](#glossary-1 "Glossary term").

## Creating date fields in Data manager

Date fields are created automatically for all data fields recognized as a date or a timestamp when you use Add data with data profiling enabled to build your data model in [Data manager](#glossary-2 "Glossary term"), or when you click Load data in Data manager.

Information note

Date fields created in Data manager are automatically added to autoCalendar.

For more information, see [*Loading and managing data with Data Manager*](../LoadData/managing-data.htm).

If the date or timestamp [field](#glossary-3 "Glossary term") is not recognized automatically, you can adjust the input format in the Data manager table editor. You can also set the display format to use in visualizations.

For more information, see [*Changing field types*](../LoadData/changing-date-time-format.htm).

### Which date & time fields are automatically recognized?

Date & timestamp fields will be recognized automatically based on your system locale settings. Additionally, the following formats are recognized:

- M/D/YYYY h:mm
- D/M/YYYY h:mm TT
- M/D/YYYY
- D/MM/YYYY
- YYYYMMDD
- YYYYMMDDhhmmss
- YYYYMMDDhhmmss.fff
- YYYYMMDDhhmmssK
- YYYY-MM-DD
- YYYY-MM-DDThh:mm:ss
- YYYY-MM-DD-Thh:mm:ss.fff
- YYYY-MM-DD-Thh:mm:ssK

Date & time formats

| Format specifier | Description |
| --- | --- |
| YYYY | Year |
| M, MM | Month |
| D, DD | Day |
| hh | Hour |
| mm | Minute |
| ss | Second |
| fff | Millisecond |
| TT | AM or PM |
| K | Timezone |
| T | Divider between date and time. T can not be replaced with another character. |

## Creating date & time fields in the data load script

If you use [Data load editor](#glossary-4 "Glossary term") to build your data model, you need to create a calendar template where you define which fields to derive in the data [load script](#glossary-5 "Glossary term"). The derived date & time fields will be generated when the script is run and data is reloaded.

For more information, see [*Derived fields*](../Scripting/derived-fields.htm).

## Using date & time fields in your application

### Date & time fields in visualizations

All date or timestamp fields in the assets panel Fields tab are marked with ![Date and time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_calendar.svg), and you can expand them to use the generated date & time fields. You can use them in visualizations, just like any other data field.

### Date & time fields in dimensions

You can also use date & time fields when you create a [dimension](#glossary-6 "Glossary term"). The date & time fields are listed under the field that they have been generated from.

### Date & time fields in expressions

You can use date & time fields in all expressions, for example when you create a [measure](#glossary-7 "Glossary term"). The date & time fields are named according to:

[field name].autoCalendar.[date & time field].

- [field name] is the name of the data field that was used to generate date & time fields.
- [date & time field] is the date & time field you want to use, for example, Year.

Example:

Date.autoCalendar.Year

### Date & time fields in calendar measures

Calendar measures use date & time fields created in autoCalendar. Each of these date & time fields is calculated by a [set analysis](#glossary-8 "Glossary term") expression that determines whether or not data falls within the time-to-date period, or if dates are within a defined relative position to the current date. These date & time fields are relative and return results based on the current date. You can use these fields independently of calendar measures.

Calendar field date & time fields are formatted as follows:

[field name].autoCalendar.[date & time field]={[value]}

- [field name] is the name of the date field used to generate date & time fields.
- [data & time field] is the name of the date & time field used, for example, InYTD.
- [value] is the value for the date & time field’s set analysis expression and determines which dates are included.

Example:

Date.autoCalendar.YearsAgo={1}

The following are the available date & time fields with sample values:

InYTD

This date & time field determines whether or not dates are within the year-to-date range or outside the year-to-date range.

InYTD

| Example | Result |
| --- | --- |
| Date.autoCalendar.InYTD={0} | Returns all dates that fall in the year-to-date time range.  For example, if the current date was the 54th day of the year, the dates within the first 54 days of every year in the date field would be included. |
| Date.autoCalendar.InYTD={1} | Returns all dates outside the year-to-date time range.  For example, if the current date was the 54th day of the year, all the dates after the first 54 days of every year in the date field would be included. |

YearsAgo

This date & time field determines whether or not dates are from a specific year relative to the current date.

YearsAgo

| Example | Result |
| --- | --- |
| Date.autoCalendar.YearsAgo={0} | Returns all dates from this year. |
| Date.autoCalendar.YearsAgo={1} | Returns all dates from last year. |
| Date.autoCalendar.YearsAgo={8} | Returns all dates from eight years ago. |

InQTD

This date & time field determines whether or not dates are within the quarter-to-date range or outside the quarter-to-date range, relative to the current date.

InQTD

| Example | Result |
| --- | --- |
| Date.autoCalendar.InQTD={0} | Returns all dates from all quarters that are within the quarter-to-date range.  For example, if the current date was the 14th day of Quarter 1, the first 14 days of every quarter in the date field would be included. |
| Date.autoCalendar.InQTD={1} | Returns all dates from all quarters that are outside the current quarter-to-date range.  For example, if the current date was the 14th day of Quarter 1, all dates after the first 14 days of every quarter in the date field would be included. |

QuartersAgo

This date & time field determines whether or not dates are from a specific quarter relative to the current date.

QuartersAgo

| Example | Result |
| --- | --- |
| Date.autoCalendar.QuartersAgo={0} | Returns all dates from the current quarter. |
| Date.autoCalendar.QuartersAgo={1} | Returns all dates from the last quarter. |
| Date.autoCalendar.QuartersAgo={8} | Returns all dates from eight quarters ago. |

QuarterRelNo

This date & time field determines whether or not dates are from a specific quarter relative to the current date.

QuarterRelNo

| Example | Result |
| --- | --- |
| Date.autoCalendar.QuarterRelNo={0} | Returns all dates from each instance of the current quarter.  For example, if the current date was in Quarter 4, all dates from each Quarter 4 in the date field would be included. |
| Date.autoCalendar.QuarterRelNo={3} | Returns all dates from each instance of the quarter two quarters prior to the current quarter.  For example, if the current date was in Quarter 4, all dates from each Quarter 1 in the date field would be included |

InMTD

This date & time field determines whether or not dates are within the month-to-date range or outside the month-to-date range, relative to the current date.

InMTD

| Example | Result |
| --- | --- |
| Date.autoCalendar.InMTD={0} | Returns all dates from all months that are within the current month-to-date range.  For example, if the date was November 15, 2016, dates from the first 15 days of every month in the date field would be included. |
| Date.autoCalendar.InMTD={1} | Returns all dates from all months that are outside the current month-to-date range.  For example, if the date was November 15, 2016, dates after the first 15 days to the end of the month of every month in the date field would be included. |

MonthsAgo

This date & time field determines whether or not dates are from a specific month relative to the current date.

MonthsAgo

| Example | Result |
| --- | --- |
| Date.autoCalendar.MonthAgo={0} | Returns all dates from the current month. |
| Date.autoCalendar.MonthAgo={1} | Returns all dates from the last month. |
| Date.autoCalendar.MonthAgo={8} | Returns all dates from eight months ago. |

MonthRelNo

This date & time field determines whether or not dates are from a specific month relative to the current date.

MonthRelNo

| Example | Result |
| --- | --- |
| Date.autoCalendar.MonthRelNo={0} | Returns all dates from each instance of the current month.  For example, if the current month was June, all dates in every instance of June in the date field would be included. |
| Date.autoCalendar.MonthRelNo={1} | Returns all dates from the each instance of the previous month.  For example, if the current month was June, all dates in every instance of May in the date field would be included. |

InWTD

This date & time field determines whether or not dates are within the week-to-date range or outside the week-to-date range, relative to the current date.

InWTD

| Example | Result |
| --- | --- |
| Date.autoCalendar.InWTD={0} | Returns all dates from all weeks that are within the current week-to-date range.  For example, if the current date was the third day of a week, dates from the first three days of every week in the date field would be included. |
| Date.autoCalendar.InWTD={1} | Returns all dates from all months that are outside the current month-to-date range.  For example, if the current date was the third day of a week, dates from the last four days of the every week in the date field would be included. |

WeeksAgo

This date & time field determines whether or not dates are from a specific week relative to the current week.

WeeksAgo

| Example | Result |
| --- | --- |
| Date.autoCalendar.WeeksAgo={0} | Returns all dates from the current week. |
| Date.autoCalendar.WeeksAgo={8} | Returns all dates from eight weeks ago. |

WeekRelNo

This date & time field determines whether or not dates are from a specific week relative to the current date.

WeekRelNo

| Example | Result |
| --- | --- |
| Date.autoCalendar.WeekRelNo={0} | Returns all dates from each instance of the current week.  For example, if the current week was the second week of the year, dates from the second week of every year in the date field would be included. |
| Date.autoCalendar.WeekRelNo={1} | Returns all dates from each instance of the previous week.  For example, if the current week was the second week of the year, dates from the first week of every year in the date field would be included. |

## Learn more

- [*Create calendar measures*](../Measures/create-calendar-measure.htm)
