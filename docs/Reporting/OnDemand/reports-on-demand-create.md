---
title: "Creating on-demand reports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/OnDemand/reports-on-demand-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Working with on-demand reporting"]
---

# Creating on-demand reports

Create on-demand reports when analyzing [sheet](#glossary-0 "Glossary term") content in an application. On-demand report generation is available for [templates](#glossary-1 "Glossary term") that have been activated for on-demand reporting by a report developer. The [selections](#glossary-2 "Glossary term") you have made in the application are reflected in the on-demand report.

Generating an on-demand report in a Qlik Sense application where selections have been made

![Clicking 'Reports' in the assets panel to open the on-demand report generation window](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_app-consume-on-demand-create.png "Click to view full size")

On-demand reporting is controlled at the level of the report template. In the Reporting section of the application, a report developer chooses which templates can be used as the basis of report generation by users who are consuming application content. For more information about configuring on-demand reports, see [*Configuring on-demand reporting*](reports-on-demand-configure.htm).

## How on-demand reporting works

You can generate on-demand reports as you analyze a sheet. On-demand reports do not run from a report task. Instead, a [report template](#glossary-4 "Glossary term") is activated for on-demand reporting by a report developer. Each activated template is available to you when you open Reports in the Assets panel. When you generate an on-demand report, the files are downloaded directly to your computer.

In an on-demand report, data reduction is based on the application access of the user generating the report, as well as their current selections. Data reduction applied through [report filters](#glossary-5 "Glossary term") is not applied to an on-demand report.

Each generation of an on-demand report counts towards the [tenant](#glossary-6 "Glossary term")'s consumption of its Qlik Reporting Service add-on subscription.

## Generating an on-demand report

Do the following:

1. In an application, open a sheet in analysis mode.
2. Make any required [selections](#glossary-7 "Glossary term").
3. Click Assets to expand the assets panel if it is not already open.
4. Click ![Report](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_report_outline.svg) Reports.

   If no [template](#glossary-8 "Glossary term") has been activated in the application for on-demand use, this section is not visible.

   Click Reports in the Assets panel when analyzing a sheet to generate on-demand reports

   ![Clicking 'Reports' in the assets panel to open the on-demand report generation window](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_app-consume-reports-assets.png "Click to view full size")
5. Identify the template you want to generate.
6. Next to the template, click ![Download](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg).
7. If more than one report format is available, select the format you want.

The report is generated and downloaded from your web browser window.

## Region-dependent formatting

In your report, certain information is formatted according to regional settings. This includes dates, numbers, and other information. The formatting used in your on-demand report depends on the selected report format and—if applicable—the add-in used to create the template.

For reports in Excel, PowerPoint, or Word format, region-dependent formatting is based on:

- Tabular (Excel) reports: The regional Excel settings configured for the user who opens the report.
- PowerPoint reports: The language settings configured in Microsoft Office for the user who opens the report.
- Word reports: The language settings configured in Microsoft Office for the user who opens the report.

For reports in PDF format, region-dependent formatting is applied as per the Qlik Cloud settings for the user generating the on-demand report. The setting that controls this formatting is Preferred language in your personal Settings. Regional settings for creating apps and script in your Settings is unrelated and has no effect on PDF formatting. For more information about your personal settings, see [*Managing your personal settings*](../../Introduction/profile-settings.htm).

## Permissions

To generate on-demand reports, you need:

- Permissions assigned to you by a tenant administrator. For more information, an administrator can refer to [*Setting permissions for metered reporting features*](../../Admin/mc-permissions-reporting.htm).
- Space permissions. See:

  - [*Space roles for applications in shared spaces*](#RequirementsShared)
  - [*Space roles for applications in managed spaces*](#RequirementsManaged)
  - [*Requirements for applications in your personal space*](#RequirementsPersonal)

  For more information about space permissions for reporting, see [*Qlik Reporting Service permissions*](../reporting-permissions.htm).

### Space roles for applications in shared spaces

In [shared spaces](#glossary-9 "Glossary term"), you need Can view or higher permissions in the space (or to the application) to generate on-demand reports.

For more information, see [*Managing permissions in shared spaces*](../../Spaces/managing-shared-spaces.htm).

### Space roles for applications in managed spaces

In [managed spaces](#glossary-10 "Glossary term"), you need Has restricted view or higher permissions in the space to generate on-demand reports. Non-space members with Can view, Can contribute, or Has restricted view access to the application can also generate on-demand reports.

For more information, see [*Managing permissions in managed spaces*](../../Spaces/managing-managed-spaces.htm).

### Requirements for applications in your personal space

You must have the Private Analytics Content Creator user role in the tenant to generate on-demand reports from an application in your personal space.
