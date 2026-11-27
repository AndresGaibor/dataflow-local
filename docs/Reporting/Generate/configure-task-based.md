---
title: "Configuring report generation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Generate/configure-task-based.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics"]
---

# Configuring report generation

You can configure task-based report generation within Qlik Sense. With task-based reporting, centrally administer the generation of reports with multi-recipient output. Task-based report configurations are designed for burst reporting use cases with automated report delivery. Generation can be triggered manually or on a schedule. Report generation is controlled by a number of building blocks, which are listed below.

## Report tasks

[Report tasks](#glossary-0 "Glossary term") control scheduled report generation by email or to a remote folder. You can also manually run a report task to generate reports immediately. A report task links together templates you have built, as well as your desired report filters. Users from your distribution list are added to the report task individually or as members of groups.

For more information, see [*Working with report tasks*](cloud-in-app-reports-tasks.htm).

## Filters

[Report filters](#glossary-1 "Glossary term") control the data reduction applied to reports generated from a report task. A report filter is a dynamic entity that can include variables and expressions. Use report filters to employ a bursted reporting use case.

For more information, see [*Working with report filters*](cloud-in-app-reports-filters.htm).

## Distribution list

The [distribution list](#glossary-2 "Glossary term") is a collection of all the recipients, and groups of recipients, that you can add to a report task. Before creating any report tasks, you need to define the application's distribution list. This can be specified from an uploaded file or manually in the load script.

For more information, see [*Creating a distribution list for your report*](cloud-in-app-reports-distribution.htm).

## Templates

A [report template](#glossary-3 "Glossary term") defines the structure of a report. You can create templates in a number of different formats:

- [Tabular report](#glossary-4 "Glossary term") templates, in Excel format, created in the Qlik add-in for Microsoft Excel.
- PixelPerfect templates, created in the embedded PixelPerfect designer.
- HTML templates, created in the embedded HTML designer.
- PowerPoint templates, created in the Qlik add-in for Microsoft PowerPoint.
- Word templates, created in the Qlik add-in for Microsoft Word.

You can add more than one report template, and even multiple copies of the same template, to a single report task. With these capabilities, you can achieve flexible, sophisticated, and automated report generation workflows.

For more information about report templates, see:

- [*Designing report templates*](../Design/design-report-templates.htm)
- [*Managing report templates*](cloud-in-app-reports-templates.htm)
