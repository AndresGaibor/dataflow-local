---
title: "Formatting properties for tabular data in Excel report templates"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/Excel/add-in-excel-tabular-properties.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Designing tabular report templates"]
---

# Formatting properties for tabular data in Excel report templates

This help topic provides an overview of the available formatting properties for tabular data in an Excel report template.

## Applies to

This content applies to designing [tabular report](#glossary-0 "Glossary term") templates using the Qlik add-in for Microsoft Excel. See [*Qlik add-in for Microsoft Excel*](../OfficeCommon/reporting-add-ins.htm#Excel).

Similar functionality exists for PowerPoint and Word templates, with some notable differences. For more information, see:

- [*Formatting properties for tabular data in PowerPoint report templates*](../PowerPoint/powerpoint-tabular-properties.htm)
- [*Formatting properties for tabular data in Word report templates*](../Word/word-tabular-properties.htm)

## Formatting properties for entire tables

In Excel, every table added as a single tag has three table settings enabled by default:

- Keep source formats: The add-in tries to keep the original object formats. By turning this setting off, you can apply customized Excel formats to the table. For example, you can set a background color in the cell with the table tag and it will be propagated on all cells in the generated report.
- Expand range: The add-in will add an adequate number of rows under the table to avoid overlap with table tags placed underneath. If the Expand range option is cleared, the add-in will not add rows under the table. You will have to manually manage the position of other table tags to stop related cells from being overwritten. Cell references will be kept.
- Wrap text: All text in table cells will be wrapped.

You can configure table column headers with the Display headers setting.

If you change the Display headers or Keep source formats settings at the table level, you are prompted to automatically change any individual columns that have different values for these settings.

Each of these settings is explained in more detail below.

Adjustable settings for a Qlik Sense chart added with a single table tag

![Table formatting settings when added as single tag](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddInTableFormat.png "Click to view full size")

### Keep source formats setting at the table level

By default, your generated reports are set to use the same formatting as the source Qlik Sense objects. If you manually apply custom formats to the template, they will be ignored. To add custom styling, you must turn off Keep source formats.

Warning note

When you use the default Keep source formats setting for a table or column in your template, you may encounter formatting differences between Qlik Sense objects and generated report objects. If you find that your report does not match the Qlik Sense application, you can turn off Keep source formats for a table or column and customize the report template manually.

The image below is an example of the output generated from a single table tag highlighted in yellow, with Keep source formats turned off.

Report output from template with single table tag highlighted in yellow

![Result of applying yellow highlighting to a single table tag - the entire table is highlighted in yellow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_CustomStyleTable.png "Click to view full size")

### Expand range

If the number of rows and columns in a table is fixed and known during the development of the template, you can add Excel formulas to the table. However, if you keep the Expand range box checked, the generated report will be wrong. It will contain incorrect cell references and the formulas will not apply to the correct cells.

In the example below, we have added some calculated cells outside the cells to be populated with the Qlik Sense table columns. Additionally, calculated cells are placed at the bottom of three columns in the table. We leave the Expand range setting turned on.

Report template with calculated cells highlighted in yellow

![Report template with calculated cells which are outside the table columns. The calculated cells refer to the locations of cells within the table columns. The 'Expand range' setting is turned on in template, which will produce incorrect results](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_ExpandRange1.png "Click to view full size")

However, in the report generated from this template, the cell references are not respected, and the calculated cells are instead added below the table. See the image below.

Incorrect output from report template with Expand range setting turned on

![Output from report template with 'Expand range' setting turned on. Specifically, the calculated cells outside the table will be moved below the table, making them not return results relevant to the table values](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_ExpandRange2.png "Click to view full size")

If we turn the Expand range setting off and generate the report, we can see that the cell references are now kept and function as intended. This is shown in the image below.

Correct output from report template with Expand range setting turned off

![Correct report output after 'Expand range' setting is turned off. The calculated cells outside the table columns now refer to the table values, which is what was intended](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_ExpandRange3.png "Click to view full size")

### Wrap text

When Wrap text is turned on at the table level, every column in the table will have text wrapping automatically applied to it. Turn off this setting if this is not desired.

### Header settings at the table level

Use the Display headers setting to configure column headers for the entire table. You have three options:

- Show in tag cell (default): Table headers will appear in the same row as the table tag, and table data will start on the row directly below it.
- Hide: Headers are removed entirely. Table data will start on the same row as the table tag. If you use this option and keep header manually entered above the tags, you can customize both the header text and the formatting of the header cells.
- Show above tag cell: Headers are moved to the row above the table tag. Table data starts on the same row as the table tag. You can apply custom Excel formatting to the cell above the table tag, so that the header cells are styled to your preference. The text in the header cells themselves, however, is generated with the dimension and measure titles from the Qlik Sense application.

## Formatting properties for individual columns

If you add a table as columns, or if you do not add all the columns of the source table, the table properties function the same as if you added an entire table tag. The only exception is that the Display header column setting also inserts a customizable fixed string.

The Expand range and Wrap text settings affect the whole table. Keep source formats and Display header can be defined separately for each column.

If you change the Display headers or Keep source formats settings at the table level, you are prompted to automatically change any individual columns that have different values for these settings.

Changing native Excel formatting properties for individual columns

![Report template showing individual column tags and headers with different formatting settings for each column](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_CustomStyleColumns.png "Click to view full size")

### Keep source formats at the column level

Keep source formats can be set at the column level to customize the formats of every single column. Click on a column tag and uncheck the related Keep source formats checkbox. Alternatively, open the table in the Tables objects within the add-in, and expand the column. Then, uncheck the checkbox.

Changing the Keep source formats value at the table level will change the value of this setting for all individual columns in the table. For information about setting this at the table level, see [*Keep source formats setting at the table level*](#Keep).

Warning note

When you use the default Keep source formats setting for a table or column in your template, you may encounter formatting differences between Qlik Sense objects and generated report objects. If you find that your report does not match the Qlik Sense application, you can turn off Keep source formats for a table or column and customize the report template manually.

### Column header settings

You can set the header style at the column level. Use the Display header setting to configure headers for each column.

Information noteIt is recommended that you use the same header settings for all columns which are placed side by side in your Excel sheet.

## Learn more

- [*Handling Qlik application data in tabular reports*](add-in-excel-handle-data.htm)
