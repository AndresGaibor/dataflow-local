---
title: "Adding content to report templates with Qlik add-ins for Microsoft Office"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/OfficeCommon/add-in-content.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office"]
---

# Adding content to report templates with Qlik add-ins for Microsoft Office

You can add various forms of content to your Excel, PowerPoint, or Word [report template](#glossary-0 "Glossary term"). Add content as chart image placeholders and tags, and enhance it with native Microsoft Office formatting. Content added using add-ins takes the form of objects. These objects can be added, managed, and re-used in the add-in window.

For information about getting started with Qlik add-ins for Microsoft Office, see [*Getting started with using Qlik add-ins for Microsoft Office*](add-in-get-started.htm).

## Applies to

This content applies to the following types of Qlik Cloud report templates:

- Excel

  [*Qlik add-in for Microsoft Excel*](reporting-add-ins.htm#Excel)
- PowerPoint

  [*Qlik add-in for Microsoft PowerPoint*](reporting-add-ins.htm#PowerPoint)
- Word

  [*Qlik add-in for Microsoft Word*](reporting-add-ins.htm#Word)

## What can you add to tabular, PowerPoint, and Word report templates?

Objects are the primary form of content added to tabular, PowerPoint, and Word report templates. Objects can be created, edited, and deleted within the add-in you are using. You can add more than one of the same object to a template. You can create the following objects:

- Chart images
- Chart tables
- Variables
- Expressions
- Levels
- Pages

### Chart images

You can add images of charts in your analytics application. Image objects are added as placeholder images that, when generated in a report, will reflect current application data.

[*Adding charts as images to report templates with Qlik add-ins for Microsoft Office*](add-in-chart-images.htm)

### Tabular data

You can add the source table from a chart in your analytics application as tabular data in your report. Tabular data can be added as full tables or sets of individual columns.

See:

- [*Adding tabular data to report templates with Qlik add-ins for Microsoft Office*](add-in-tabular-data.htm)
- [*Formatting properties for tabular data in Excel report templates*](../Excel/add-in-excel-tabular-properties.htm)
- [*Formatting properties for tabular data in PowerPoint report templates*](../PowerPoint/powerpoint-tabular-properties.htm)
- [*Formatting properties for tabular data in Word report templates*](../Word/word-tabular-properties.htm)

### Variables and expressions

Add variables and expressions based on content and data in your application, using Qlik-native analytics functions.

[*Using variables and expressions in report templates with Qlik add-ins for Microsoft Office*](add-in-variables-expressions.htm)

### Levels and pages

Use levels and pages to automate the creation of separate sections and pages in your report, looping and repeating the generation of tabular and image data for a distinct number of [dimension](#glossary-1 "Glossary term") values.

See:

- [*Working with levels and pages in tabular report templates*](../Excel/add-in-excel-levels-pages.htm)
- [*Designing PowerPoint report templates*](../PowerPoint/powerpoint-report-template.htm)
- [*Designing Word report templates*](../Word/word-report-template.htm)

Information note

Levels are not applicable to PowerPoint report templates.

Information note

Pages are not applicable to Word report templates.

## The different types of tags

The following table lists the available types of tags you can insert into the template, and what each tag does. Use the Qlik add-in window in your Microsoft Office application to add the tags.

Available tags you can use in Qlik add-ins for Microsoft Office

| Tag type | Description | Example and format |
| --- | --- | --- |
| Table | A single tag representing an entire chart that has been added as a table. In the output, each column is generated in the same way as an individual column. | <Table Name> |
| Column | A single tag representing a single column in a chart that has been added as a table. Whether one or more columns are added from a table, the underlying template object is still a table. | <Column Name> |
| Level | A set of tags representing an instance of a level object. Between the opening and closing tags, other tags can be added, signaling that a new section (level) is to be created in the report, including these items, for each distinct entity upon which the level object is based.  Information noteNot applicable to PowerPoint report templates. | <Entity Name\_Level>  ...  </Entity Name\_Level> |
| Field | A tag used inside a level tag, or in a cell on a worksheet defined by a page tag, to display the field values which are being used for each filtered section or page. | <Field Name> |
| Page | A tag that represents a page object. With a page tag, a new page is created in the report for every distinct entity upon which the page object is based.  Page tags have some differences based on template type:   - In tabular (Excel) templates, page tags appear in the name of the worksheet tab. A page object generates a new worksheet for each distinct entity. - In PowerPoint templates, page tags are added as hidden metadata and are not visible. A page object generates one or multiple new slides for each distinct entity.   Information noteNot applicable to Word report templates. | <Entity Name\_Page> |
| Variable | A single tag representing an instance of a variable that is found in the source Qlik Sense application. | <Variable Name> |
| Expression | A single tag representing an instance of an expression added to the template as an object. | <Expression Name> |
| Deleterow | A tag indicating a row in a table which is to be removed in the generated report output. See [*Removing rows with the Deleterow tag*](../Excel/add-in-excel-deleterow.htm).  Information noteOnly applicable for Excel report templates. | <deleterow> |

## Application selections

[Selections](#glossary-2 "Glossary term") you make in the Qlik Sense source application are reflected in the [report template](#glossary-3 "Glossary term") while authoring it. The selections are applied to the preview of the report you can generate from the add-in. However, the selections are not reflected in output from [report tasks](#glossary-4 "Glossary term") in Qlik Cloud. Instead, data reduction in the report output is controlled by [filters](#glossary-5 "Glossary term") you create in the Reporting section of a Qlik Sense application. See [*Working with report filters*](../../Generate/cloud-in-app-reports-filters.htm) for more information.

If you do want to change the selections reflected in the template for the purposes of previews and image placeholders, you can change the selections in the original Qlik Sense application, and then refresh the report template. To see the new selections in Excel, PowerPoint, or Word, click the ![Reload](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg) icon in the top right corner of the properties pane for the object. This refreshes the selections only in the selected object.
