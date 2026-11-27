---
title: "Fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/fields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Using data assets in visualizations"]
---

# Fields

Fields hold the data that is used in Qlik Sense. Fields can be thought of as the data loaded from the [load script](#glossary-0 "Glossary term").

Fields contain one or more values, called field values, and at the basic level, correspond to columns in a database table, but can also exist in more than one table. Field values consists of numeric or alphanumeric data. When loaded from the load script, fields can be represented as a table [visualization](#glossary-1 "Glossary term").

Example of data in a load script:

Temp:
LOAD \* inline [
Customer Product UnitSales UnitPrice
Imagine Film 4 16
Imagine Film 10 15
Imagine Shutter 9 9
PhotoInc Shutter 5 10
PhotoInc Lens 2 20
PhotoInc Magnifier 4 25
Gallery Film 8 15
Gallery Lens 7 19
] (delimiter is ' ');

The fields represented in a data model table after having loaded the data:

![Data model table.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_DataInTable.png)

The same fields as columns in a table visualization on a sheet:

![Table visualization.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_FieldsAsColumnsTable.png)

Fields are used to create visualizations in application sheets. They are added to visualizations in the sheet in edit mode. In a sheet in edit mode, fields are available from Assets. For more information, see [*Working with sheets*](../Sheets/working-with-sheets.htm).

- [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm)
- [*Expression editor*](../Expressions/expression-editor.htm)
- [*Data grouping with dimensions*](../Dimensions/dimensions.htm)
- [*Measures*](../Measures/measures.htm)
- [*System fields*](../Scripting/system-fields.htm)
