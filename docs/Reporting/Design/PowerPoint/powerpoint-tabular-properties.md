---
title: "Formatting properties for tabular data in PowerPoint report templates"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PowerPoint/powerpoint-tabular-properties.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Designing PowerPoint report templates"]
---

# Formatting properties for tabular data in PowerPoint report templates

This help topic provides an overview of the available formatting properties for tabular data in a PowerPoint report template.

## Applies to

This content applies to designing PowerPoint report templates using the Qlik add-in for Microsoft PowerPoint. See [*Qlik add-in for Microsoft PowerPoint*](../OfficeCommon/reporting-add-ins.htm#PowerPoint).

Similar functionality exists for Word and Excel templates, with some notable differences. For more information, see:

- [*Formatting properties for tabular data in Word report templates*](../Word/word-tabular-properties.htm)
- [*Formatting properties for tabular data in Excel report templates*](../Excel/add-in-excel-tabular-properties.htm)

## Formatting properties for entire tables

In PowerPoint, tables added as single tags have the following Table settings:

- Keep source formats: The add-in tries to keep the original object formats. By turning this setting off, you can apply customized PowerPoint formats to the table.
- Display headers: Configure table column headers to be displayed or hidden.

If you change the Display headers or Keep source formats settings at the table level, you are prompted to automatically change any individual columns that have different values for these settings.

Each of these settings is explained in more detail below.

Adjustable settings for a Qlik Sense chart added with a single table tag

![Table formatting settings when added as single tag](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_PowerPointReport_TableFormat.png "Click to view full size")

### Keep source formats setting at the table level

In your PowerPoint template, the Keep source formats setting is turned off by default. This allows you to add custom styling to the table tag using the native PowerPoint features. With Keep source formats turned on, the table is rendered with minimal formatting.

Warning note

When Keep source formats is turned on for a table or column in your template, you may encounter formatting differences between Qlik Sense objects and generated report objects. If you find that your report does not match the Qlik Sense application, you can turn off Keep source formats for a table or column and customize the report template manually.

The image below is an example of the output generated from a single table tag highlighted in yellow, with Keep source formats turned off.

Report output from template with single table tag highlighted in yellow

![Result of applying yellow highlighting to a single table tag - the entire table is highlighted in yellow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_PowerPointReport_CustomStyleTable.png "Click to view full size")

### Header settings at the table level

Use the Display headers setting to configure column headers for the entire table. You have two options:

- Show (default): Table headers are added to the top of the table automatically.
- Hide: Table headers are removed from the table. This option is suitable if you do not need headers, or if you want to manually add headers for the table at a later time.

## Formatting properties for individual columns

Keep source formats and Display header can be defined separately for each column.

If you change the Display headers or Keep source formats settings at the table level, you are prompted to automatically change any individual columns that have different values for these settings.

Each of these settings is explained in more detail below.

### Keep source formats at the column level

Keep source formats can be set at the column level to customize the formats of every single column. Click on a column tag and uncheck the related Keep source formats checkbox. Alternatively, open the table in the Tables objects within the add-in, and expand the column. Then, uncheck the checkbox.

With Keep source formats turned on, the column is rendered with minimal formatting.

Changing the Keep source formats value at the table level will change the value of this setting for all individual columns in the table. For information about setting this at the table level, see [*Keep source formats setting at the table level*](#Keep).

Changing formatting properties for individual columns in a PowerPoint report template

![Report template showing individual column tags and headers with different formatting settings for each column](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_PowerPointReport_CustomStyleColumns.png "Click to view full size")

Warning note

When Keep source formats is turned on for a table or column in your template, you may encounter formatting differences between Qlik Sense objects and generated report objects. If you find that your report does not match the Qlik Sense application, you can turn off Keep source formats for a table or column and customize the report template manually.

### Column header settings

You can set the header style at the column level. Use the Display header setting to configure headers for each column.

Information noteIt is recommended that you use the same header settings for all columns which are placed side by side.
