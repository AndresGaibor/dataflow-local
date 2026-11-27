---
title: "Handling Qlik application data in tabular reports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/Excel/add-in-excel-handle-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Designing tabular report templates"]
---

# Handling Qlik application data in tabular reports

This help topic describes how you can use native Excel features to format certain types of Qlik analytics data.

## Handling dual values

Dual values are supported in tabular reports—for example, those used in autocalendars.

For example, the My\_Date\_Field field in this script excerpt:

```
[autoCalendar]:
  DECLARE FIELD DEFINITION Tagged ('$date')
FIELDS
  Dual(Year($1), YearStart($1)) AS [Year] Tagged ('$axis', '$year'),
...
DERIVE FIELDS FROM FIELD [My_Date_Field] USING [autoCalendar] ;
```

In tabular reports, dual values are shown by default as serial numbers. To display them as dates, for example, you need to format them as dates in the template using the Qlik add-in for Microsoft Excel.

Do the following:

1. In the add-in window, deselect the Keep source formats option from the table, column, variable, or expression.
2. Use the native Excel features to format the data. For example: format the data as dates in MM-DD-YYYY format.

## Learn more

- [*Designing tabular report templates*](design-tabular-report-templates.htm)
- [*Dual Script and chart function*](../../../Scripting/FormattingFunctions/Dual.htm)
