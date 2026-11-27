---
title: "Handling Qlik application data in PixelPerfect reports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-handle-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report"]
---

# Handling Qlik application data in PixelPerfect reports

This help topic provides guidelines for formatting certain types of Qlik analytics data in your PixelPerfect report.

## Handling dates and dual values

Dates and dual values are supported in PixelPerfect reports—for example, those used in autocalendars.

For example, the My\_Date\_Field field in this script excerpt:

```
[autoCalendar]:
  DECLARE FIELD DEFINITION Tagged ('$date')
FIELDS
  Dual(Year($1), YearStart($1)) AS [Year] Tagged ('$axis', '$year'),
...
DERIVE FIELDS FROM FIELD [My_Date_Field] USING [autoCalendar] ;
```

In PixelPerfect reports, dual and date values are shown by default as serial numbers. To display them as dates, for example, you need to format them as dates in the template using the PixelPerfect designer.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Under Levels, expand or create the item that you want to format as a date.
3. Hover your cursor over the item and click the Add calculated field icon.

   Creating a calculated field

   ![Adding a calculated field for a level in the PixelPerfect designer.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_report-pixelperfect-gen-calc-field.png "Click to view full size")
4. On the new calculated field, click the Edit icon.
5. Optionally, add a Name to change it from the default.
6. Next to Expression, click ![More](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
7. In the Expression Editor, paste the following expression, replacing my\_date\_field with the name of your date field:

   ```
   AddDays( #1899-12-30#, [my_date_field] )
   ```
8. Click OK.
9. Add the item to the report design surface.

   [*Working with levels*](pixelperfect-work-with-levels.htm)
10. Set the date format you want to use in the Format String Editor. Do the following:

    1. On the design surface, select the item.
    2. Click the three-dot icon next to the item, and then click the gear icon.
    3. Click ![More](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) under Text Format String.
    4. Select the date format you want to use, and click OK.

## Learn more

- [*Designing PixelPerfect report templates*](design-pixelperfect-templates.htm)
- [*Creating highly formatted tables*](pixelperfect-highly-formatted-table.htm)
- [*Dual Script and chart function*](../../../Scripting/FormattingFunctions/Dual.htm)
