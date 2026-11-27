---
title: "Working with levels"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-work-with-levels.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Defining report structure and data"]
---

# Working with levels

Levels provide an easy way to automate the creation of report elements for different subsets of data. In PixelPerfect reports, you add levels by creating specific data bindings and connecting them to DetailReport bands in your [template](#glossary-0 "Glossary term").

Adding levels to bands allows flexibility to your template creation experience. You can add a level to certain bands to enhance reports with detail, and to automate the repetition of a particular structure. You can nest levels within other levels to create complex, detailed reports.

## How levels work

A level is a field (specifically a [dimension](#glossary-1 "Glossary term")), or a chart, over which some or all of the report contents are repeated, filtering for a single unique value at a time.

For example, let's say you have a chart in your application showing sales totals by Product. You could add this chart to your report, and apply a level for a Continent field. When the report is generated, a separate chart is automatically created for each continent, showing the sales data for one continent in each chart.

Levels are applied by binding a level data binding to a band in the template.

Using levels allow you to present details and granularity in repeated format, without manually creating specific charts for individual field values.

## Adding levels to your template

To learn how to add levels to your report template, see [*Using a level to loop over application data*](pixelperfect-create-level.htm).

## Levels and highly formatted tables

To create highly formatted PixelPerfect tables using the recommended workflow, it is mandatory that you apply a level. For more information, see [*Creating highly formatted tables*](pixelperfect-highly-formatted-table.htm).

## Limitations

- You can nest up to five levels deep in your report.
- You cannot add a level to the default Detail1 band in the report. Instead, create a new DetailReport band if you need to add levels.

  Levels are also unavailable for other special types of bands, such as headers and footers.

## Learn more

- [*Banded report authoring*](pixelperfect-banded-authoring.htm)
