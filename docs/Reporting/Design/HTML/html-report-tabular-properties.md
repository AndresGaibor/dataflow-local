---
title: "Formatting properties for tabular HTML data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/html-report-tabular-properties.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing HTML report templates", "Adding content to your HTML report template", "Adding tabular data to your HTML template"]
---

# Formatting properties for tabular HTML data

This help topic provides an overview of the available formatting properties for tabular data in an HTML report template.

## Formatting properties for entire tables

The following formatting properties can be adjusted for tabular data in an HTML template, both for a table added as a single item and a table added as a series of individual columns:

- Keep source formats
- Display headers

If you change either of these settings at the table level, you are prompted to automatically change any individual columns that have different values for these settings.

Each setting is explained in more detail below.

### Keep source formats setting at the table level

Every table added as a single item has the Keep source formats setting activated by default. With this setting turned on, the HTML designer tries to keep the formatting of the original application object. By turning this setting off, you can apply customized formats to the table. For example, you can style the object with a background color or border using HTML code.

By default, your generated reports are set to use the same formatting as the source Qlik Sense objects. If you manually apply custom formats to the template, they will be ignored. To add custom styling, you must turn off Keep source formats.

Warning note

When you use the default Keep source formats setting for a table or column in your template, you may encounter formatting differences between Qlik Sense objects and generated report objects. If you find that your report does not match the Qlik Sense application, you can turn off Keep source formats for a table or column and customize the report template manually.

### Header settings at the table level

Use the Display headers setting to configure column headers for the entire table. You have two options:

- Show (default): Table headers will appear at the location where you insert the table in the template code, and table data will start on a row directly below them.
- Hide: Headers are removed entirely. Table data will start at the location where you insert the table in the template code. This can be helpful if you want to design your own headers and style them using HTML code.

## Formatting properties for individual columns

When viewing a table object in the objects panel, click Expand columns to access the properties for each individual column. The following formatting properties can be adjusted:

- Keep source formats
- Display header

Each setting is explained in more detail below.

### Keep source formats at the column level

Keep source formats can be set at the column level to customize the formats of every single column. Expand a column in the object panel, and uncheck the related Keep source formats checkbox. Alternatively, open the table in the Tables objects from the object panels, and expand the column. Then, uncheck the checkbox.

Changing the Keep source formats value at the table level will change the value of this setting for all individual columns in the table. For information about setting this at the table level, see [*Keep source formats setting at the table level*](#Keep).

Warning note

When you use the default Keep source formats setting for a table or column in your template, you may encounter formatting differences between Qlik Sense objects and generated report objects. If you find that your report does not match the Qlik Sense application, you can turn off Keep source formats for a table or column and customize the report template manually.

### Column header settings

You can set the header style at the column level. Use the Display header setting to configure headers for each column. You have two options:

- Show (default): Table headers will appear at the location where you insert the table in the template code, and table data will start on a row directly below them.
- Hide: Headers are removed entirely. Table data will start at the location where you insert the table in the template code. This can be helpful if you require differences in the appearance of each header. Depending on whether you have added your table as a single item or as a set of individual columns, this process will be performed differently in your HTML code.

## Learn more

- [*Adding tabular data to your HTML template*](html-report-tabular-data.htm)
