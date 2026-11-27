---
title: "Create calendar measures"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Measures/create-calendar-measure.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Create calendar measures

To analyze data over relative time ranges, use calendar measures. For example, you might want to compare current year-to-date sales figures with figures from the same period the previous year.

Calendar measures aggregate data from a [field](#glossary-0 "Glossary term") over a time range, and are saved in the Measures category in the master items. Calendar measures comprise a field to be aggregated, an [aggregation](#glossary-1 "Glossary term"), a date field, and a time range for that date field that sets which data is included in the aggregation. You create calendar measures under Fields in the Assets panel, using the Create calendar measures dialog.

You can aggregate fields from tables loaded in [Data manager](#glossary-2 "Glossary term") or from a script in [Data load editor](#glossary-3 "Glossary term"), as long as the field is in the same table as the date field, or is in an associated table.

However, the date field must be from a table that has been loaded using Data manager, because calendar measures use expressions tagged as date & time fields that are declared in autoCalendar, and date fields are only mapped to autoCalendar when loaded in Data manager. Calendar measures support the following aggregations with the aggregated field: Sum, Count, Avg, Min, and Max.

Information note

Calendar measures do not support calendars created using the Data load editor. If you use calendars created using Data load editor and want to create calendar measures, you must load a table containing a date field using Data manager for use with your tables loaded using Data load editor.

Information note

If your date field is subject to more than one calendar and both calendars are qualified for use with calendar measures, then the first calendar loaded in the data [load script](#glossary-4 "Glossary term") is used in the calendar measures.

A calendar measure can use one of the following time ranges are available for use with calendar measures: weekly, monthly, quarterly, and yearly. Within each time range, different measures exist for periods such as current month, year-to-date, and current week last year. The following time ranges and measures are available for creating calendar measures:

Calendar measures for time range Yearly

| Measure | Description |
| --- | --- |
| YTD | The year to date for all years. |
| YTD Current Year | The year to date for the current year. |
| YTD Last Year | The year to date for last year. |

Calendar measures for time range Monthly

| Measure | Description |
| --- | --- |
| MTD | The month to date for all months and years. |
| MTD Current Month | The month to date for the current month. |
| MTD Last Month | The month to date for last month. |
| Current Month | All dates this month. |
| Current Month Last Year | All dates this month last year. |
| Last Month | All dates last month. |

Calendar measures for time range Quarterly

| Measure | Description |
| --- | --- |
| QTD | The quarter to date for all years. |
| QTD Current Quarter | The quarter to date for the current quarter. |
| QTD Last Quarter | The quarter to date for the last quarter. |
| Current Quarter | All dates in the current quarter. |
| Current Quarter Last Year | All dates in the current quarter last year. |
| Last Quarter | All days for the last quarter. |

Calendar measures for time range Weekly

| Measure | Description |
| --- | --- |
| WTD | The week to date for all weeks across all years. |
| WTD Current Week | This week to date for the current week. |
| WTD Last Week | The week to date for the last week. |
| Current Week | All dates this week. |
| Current Week Last Year | All dates this week last year. |
| Last Week | All dates last week. |

Once created, calendar measures are treated identically to master measures. That is, calendar measures are reusable and editable while an application is unpublished. Users of a published application will have access to the calendar measures, but will not be able to modify them.

## Creating a calendar measure from a field

Do the following:

1. In the assets panel, right-click a field and select Create calendar measures.

   By default, the field you right-clicked will be included as the Aggregated field.
2. Select a date field from the Date field drop-down list.
3. Select a field from the Aggregated field drop-down list.
4. Select an aggregation from the Aggregation drop-down list.
5. Select a time range from the Time range drop-down list.

   A list of the available measures displays under Preview of measures.

   You can toggle the display of the measures' expressions by selecting the Preview of measures switch.
6. Select the calendar measures to add to your master items.

   By default, all measures are selected.
7. Click Save to master items.
8. Click Close.

## Learn more

- [*Reusing assets with master items*](../Assets/work-with-master-items.htm)
- [*Date & time fields*](../Assets/date-time-fields.htm)
- [*Assets panel in edit mode*](../Sheets/sheet-view.htm#Assets)
