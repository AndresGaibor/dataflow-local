---
title: "Troubleshooting - Report tasks and generated reports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Troubleshooting/troubleshooting-tasks-generated-reports.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Troubleshooting - In-application reporting"]
---

# Troubleshooting - Report tasks and generated reports

This topic provides help with resolving common issues encountered when managing report tasks and generating reports with them.

## Application reload fails when uploading distribution list file

Possible cause

This could be due to a number of issues with how the end of your load script is formatted before adding the distribution list.

Common examples:

- There is an Exit script statement at the end of your current load script.
- There is a missing semicolon at the end of the last LOAD or SELECT statement in the load script.

Proposed action

Given the examples above, the following solutions could work:

- Move the newly added Distribution List script section to a new location above the Exit script statement. Alternatively, remove the Exit script statement if this makes sense given your use case and scripting context.
- Add the missing semicolon.

## Report task: "Failed to send to some users."

The report task might send to some users, but fails to send to others.

Possible cause 1

The email address of these recipients was changed in the [distribution list](#glossary-0 "Glossary term"). When generating reports for each recipient added to the report task, Qlik Cloud searches for the email address in the distribution list. If no match is found, a report cannot be generated for the user.

Proposed action 1

A best practice is to use groups to add users to the report task. Groups are collections of recipients. When you change the email address of a recipient who has been added to the task as part of a group, reports are generated and delivered to the updated email address.

If you do need to add single recipients to the report task, delete the original user from the report task and re-add them with their updated email address.

For more information, see [*Creating a distribution list for your report*](../Generate/cloud-in-app-reports-distribution.htm).

Possible cause 2

One or more [report filters](#glossary-1 "Glossary term") referenced in the distribution list were not found in the application. For example:

- The name of a filter was changed in the application, but not updated in the distribution list.
- A filter was deleted in the application, but it continues to be referenced in the distribution list.
- A filter referenced in the distribution list has not yet been added to the application.

Proposed action 2

Update filter names to align between the application and the distribution list. Add filters as needed. If a filter is deleted and no longer applicable, remove its reference from the distribution list.

## Report task that includes an Excel template: "Failed to send: Could not generate"

Possible cause 1

The template uses Excel features that are not supported for tabular reporting.

Examples:

- Visual Basic for Applications, macros, and scripting
- Third-party extensions

Proposed action 1

Create a template that does not use unsupported Excel features.

For a list of limitations for the Qlik add-in for Microsoft Excel, see [*Qlik Reporting Service specifications and limitations*](../Reporting-service-specifications-limitations.htm).

Possible cause 2

One or more fields in the application are configured with Always one selected value, and there are not any report filters applied to the report task to select exactly one value for each of these fields.

Proposed action 2

If an application contains one or more fields configured with the Always one selected value property, you need to configure your report filters so that the filters select exactly one value for each of these fields. These report filters need to be applied to the report task.

If a filter doesn't contain a value for these fields, or no filters are associated at all to the task, the report task will fail.

Possible cause 3

The following has happened:

- You added data from a Table chart from the application to the template, using one or more column tags.
- In the application, one or more of the Table columns has the Show column if setting applied to it in the application.
- At the time of report generation, the Show column if conditions for these columns are not met.

When you add column tags that are associated with a Show column if condition set on a Table chart, the condition must be met when a report task using that template is run. Otherwise, the report task fails.

Proposed action 3

Remove the column tags and add the Table chart data back to the template as a table tag. Report tasks using this template will then run successfully even if the condition is not met.

## Report task fails to execute - maximum number of unique reports reached

A report task execution fails with the following message:

The report was not sent because the maximum number of unique reports for this task has been reached. Check the recipient list for more details.

Possible cause

A [report task](#glossary-2 "Glossary term") can generate a maximum of 500 unique reports. This limit is evaluated across all templates added to the task, rather than per template in the task. This limit also applies to all report tasks regardless of whether or not one or mores cycles are applied.

Proposed action

Edit the report task, changing the definition so that less than 500 unique reports are generated with each execution. If you still need to produce more than 500 unique reports at once, you can create separate tasks with similar delivery settings.

## My report does not contain the data I thought it would

Possible cause 1

The load script contains a Star statement, and the report is set to use filters.

Proposed action 1

Rework the load script so that it works as intended without using any Star statements.

Possible cause 2

The report is migrated from a Qlik NPrinting template that uses object filters, and one or more object references in the template do not match available objects in the current application.

Proposed action 2

Open the template with the editor and validate object references. Re-upload the corrected template and run a test task to verify object-level filter behavior.

For more information, see [Exporting report templates from Qlik NPrinting to Qlik Cloud](/en-US/migration/Content/Migration/NPrinting/exporting-nprinting-excel-to-qlik-cloud.htm).

Possible cause 3

Report data relies on aggregation of a key field.

Proposed action 3

Aggregations based on key fields can introduce issues with the data shown in reports.

Instead of aggregating the key field, create a copy of the key field that is not explicitly used to link multiple tables.

For more information about best practices for aggregating key fields in Qlik data models, see [*Aggregation of key fields*](../../Scripting/AggregationFunctions/aggregation-functions.htm#Aggregat).

## Report task has been disabled

Possible cause 1

A [section access](#glossary-3 "Glossary term") table was added or removed in the application.

Proposed action 1

Evaluate whether the data security restrictions defined in the section access tables are acceptable for the report task use case. If they are acceptable, re-enable the report task.

Possible cause 2

The application has section access and a [tenant admin](#glossary-4 "Glossary term") has changed the owner of the [report task](#glossary-5 "Glossary term"). This automatically disables the report task. In this situation, only the new owner of the report task will be able to re-enable the task.

Proposed action 2

Changes in report task ownership can affect the data reduction applied to individual recipients of the task. Keep in mind that if the report task is configured to send reports to individuals who are not users in the Qlik Cloud tenant, the data they will receive will be the same data that the new report task owner would receive.

When the new report task owner has evaluated the configuration and made any necessary changes, they can re-enable the report task.

For more information, see [*In-application reporting and section access*](../Generate/cloud-in-app-reports-section-access.htm).

## Timestamp for report generation in file name (or file name preview) is incorrect

Possible cause

The report task owner has not set a preferred time zone in their personal settings. When a preferred time zone has not been explicitly set, report file names use timestamps in UTC.

Proposed action

The user who owns the report task needs to set a time zone in their personal settings.

Do the following:

1. In Qlik Cloud, click your user profile menu in the top right corner.
2. Click Settings.
3. Under Time zone, select your preferred time zone.

## Incorrect font used in report generated from Excel template

Possible cause

A custom font is used in the template.

The use of custom fonts in the Excel template file is not supported. If your template contains fonts that are unavailable for report generation, elements using these fonts will instead use a default Excel font in generated reports.

Proposed action

When authoring your Excel template, use an Excel font that is best matched to the custom font you originally used. This is the best way to avoid unexpected results in report output.

## Learn more

- [*Troubleshooting - Working with report templates*](troubleshooting-report-templates.htm)
- [*Troubleshooting - Administration and installation of reporting*](troubleshooting-report-administration.htm)
