---
title: "Adding content to your HTML report template"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/html-report-add-content.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing HTML report templates"]
---

# Adding content to your HTML report template

You can add various forms of content to your HTML [report template](#glossary-0 "Glossary term"). Add application content as chart images, tabular data, variables, and expressions. In your HTML template, application content takes the form of objects. These objects—not to be confused with native HTML objects—can be added, managed, and re-used in the objects panel in the HTML designer. Content that does not directly visualize application data—for example, introductory messaging for emails, and custom formatting—can be added if it is included in [the list of supported code syntax](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/html-report-allowed-code.htm).

## Application content that can be added to HTML reports

HTML report templates work with the following types of application content:

- Chart images.

  [*Adding charts as images in your HTML template*](html-report-chart-images.htm)
- HTML tables based on chart data. The following options are available:

  - An entire chart added with a single table tag.

    [*Adding an entire chart*](html-report-tabular-data.htm#FullChartTable)
  - A table consisting of one or more individual columns from a chart.

    [*Adding a chart by column*](html-report-tabular-data.htm#ChartTableColumn)
  - Variables from the analytics application.

    [*Adding variables and expressions to HTML report templates*](html-report-variables-expressions.htm)
  - Expressions written using Qlik analytics syntax.

    [*Adding variables and expressions to HTML report templates*](html-report-variables-expressions.htm)

  For more information about the available tags you can add, see [*Available application content tags*](#The).

The HTML report authoring experience offers flexibility when working with application content. For example, you can add images, variables, and expression as tabular data using HTML code.

Use levels to automate the creation of separate sections in your report, looping and repeating the generation of application data for a distinct number of dimension values. For information, see [*Looping and cycling HTML report elements with levels*](html-report-levels.htm).

### Object types

You add application content to your template as objects. Objects can be reused and edited over the course of the template development. work with the following objects:

- Chart images
- Chart tables
- Variables
- Expressions
- Levels

## Available application content tags

The following table lists the available types of tags you can insert into the template, and what each tag does. Use the HTML designer to add the tags.

Available tags you can use in HTML report templates in Qlik Cloud Analytics

| Tag type | Description | Example and format |
| --- | --- | --- |
| Table | A single tag representing an entire chart that has been added as a table. In the output, each column is generated in the same way as an individual column. | %%Table Name%% |
| Column | A single tag representing a single column in a chart that has been added as a table. Whether one or more columns are added from a table, the underlying template object is still a table. | %%Column Name%% |
| Level | A set of tags representing an instance of a level object. Between the opening and closing tags, other tags can be added, signaling that a new section (level) is to be created in the report, including these items, for each distinct entity upon which the level object is based. | %%Entity Name\_Level%%  ...  %%/Entity Name\_Level%% |
| Field | A tag used inside a level tag to display the field values which are being used for each filtered iteration of the level. | %%Field Name%% |
| Variable | A single tag representing an instance of a variable that is found in the source application. | %%Variable Name%% |
| Expression | A single tag representing an instance of an expression added to the template as an object. | %%Expression Name%% |

## Custom code

Because the HTML designer is effectively a code editor, you can add your own custom code to the template. This code is likely not going to consist entirely of application content. For example, your template might require inline CSS, corporate web content, and other features that do not directly incorporate application content.

You can add code to the report template if it is listed as a supported component. Otherwise, your template must be sanitized to remove all non-compliant code. For a list of supported HTML code components, see [*Allowlist for code in HTML templates*](html-report-allowed-code.htm).

## Application selections

[Selections](#glossary-1 "Glossary term") you make in the source application are reflected in the [report template](#glossary-2 "Glossary term") while authoring it. The selections are applied to the preview of the report you can generate from the HTML designer. However, the selections are not reflected in output from [report tasks](#glossary-3 "Glossary term") in Qlik Cloud. Instead, data reduction in the report output is controlled by report filters, cycles, and section access.

If you do want to change the selections reflected in previews, you can change the selections in sheet view. You can then click ![Refresh entities](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg) in the top right corner of the objects panel in the HTML designer. This refreshes the selections only in the selected object.
