---
title: "In-application reporting and section access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Generate/cloud-in-app-reports-section-access.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Configuring report generation"]
---

# In-application reporting and section access

You can use in-application reporting with applications that use [section access](#glossary-0 "Glossary term"). This help topic describes the differences you can expect when configuring reports from an application that uses section access.

Warning note

Always define explicit, filtered recipients in the distribution list for any report task running against a section access–enabled application. Do not rely on section access alone to reduce data for report distribution.

Why: Section access protects the app; it does not protect the report task. The distribution list is where recipients are mapped to filters. If, for any reason, a recipient does not match as expected in the Qlik tenant, that recipient receives the report task owner's own data access instead — adding a filter on the recipient is what ensures the data is reduced for that person specifically, rather than defaulting to the owner's view.

Action: Replicate the section access rules as explicit report filters per recipient, even where this duplicates logic is already enforced in the script. Treat this as mandatory, not optional, wherever the app carries sensitive data.

The data reduction applied to report output depends on:

- Whether the application uses section access
- The [report filters](#glossary-1 "Glossary term") that are used
- If the recipient is internal or external to the Qlik Cloud [tenant](#glossary-2 "Glossary term")
- The cycles applied

Refer to the sections below to learn how reports are generated for each type of recipient. For additional details, see [*Who can receive reports?*](../InAppGeneral/cloud-in-app-reports-intro.htm#RecipientTypes).

## Differences between internal and external recipients

### Recipient identification

To identify recipients as internal or external, recipient email addresses are checked for matches with users in the Qlik Cloud tenant. Email address matching is case-insensitive. The check produces the following outcomes:

- If the email address matches the email address of a user in the Qlik Cloud tenant, the recipient is internal.
- If no match is found, the recipient is external.

### Internal recipients

Any internal report recipient must have access to the application and be included in the section access table for the report to be generated and sent to them. If these criteria are not met, an error will be added to the task execution history for that recipient. When the criteria are met, the data in the report output will also be filtered based on the data access restrictions defined for that user in the section access script.

### External recipients

External report recipients receive report output as defined by the access of the report task owner.

## Capacities for a report task

A [report task](#glossary-3 "Glossary term") can generate a maximum of 500 unique reports. This limit is evaluated across all templates added to the task, rather than per template in the task. This limit also applies to all report tasks regardless of whether or not one or mores cycles are applied.

In applications without section access, a unique report is generated for each distinct recipient-level filter applied across all users added to the report task. However, this behavior is different in applications with section access.

If the application has section access:

- A unique report is generated for each internal recipient added to the report task, regardless of the filter applied to the recipient.
- For external recipients, a unique report is generated only if the filter defined for the recipient is different than the filter defined for the report task owner. For external recipients with the same filter applied to them, one unique report is generated per unique filter.

## Automatic deactivation of report tasks

In some scenarios, report tasks are automatically disabled in an application that uses section access. The following behaviors can be expected:

- If a section access table is added to or removed from the application, the report task is automatically disabled. It can be re-enabled manually. This allows the report developer to evaluate whether they want to proceed with report deliveries, based on the definitions of the recipients in the distribution list.
- If the application has section access and a tenant admin changes the ownership of the report task in the Administration activity center, the report task is automatically disabled.
  After this, only the new report task owner can re-enable the report task.

## Limitations

Report delivery via Microsoft SharePoint distribution folder is not available if the application uses section access.

## Learn more

- [*Managing data security with Section Access*](../../Scripting/Security/manage-security-with-section-access.htm)
- [*Troubleshooting - In-application reporting*](../../Troubleshooting/troubleshooting-reporting.htm)
