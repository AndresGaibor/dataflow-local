---
title: "Configuring on-demand reporting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/OnDemand/reports-on-demand-configure.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Working with on-demand reporting"]
---

# Configuring on-demand reporting

Report developers can make it possible for application consumers to generate reports on the fly when using an application. On-demand report generation is administered at the [report template](#glossary-1 "Glossary term") level. As a report developer, you can control the available report formats for the on-demand report generation, and several other parameters.

## How on-demand reporting works

On-demand reports are generated in analysis mode when a user views a sheet. On-demand reports do not run from a report task. Instead, a report template is activated for on-demand reporting. Each activated template becomes available to the user when they open Reports in the Assets panel. The user downloads the on-demand report directly to their computer when it is ready.

In an on-demand report, data reduction is based on the application access of the user generating the report, as well as their current selections. Data reduction applied through [report filters](#glossary-2 "Glossary term") is not applied to an on-demand report.

### Considerations

When you develop a template intended for use in on-demand reporting, it is important to consider the following:

- Each generation of an on-demand report counts towards the [tenant](#glossary-3 "Glossary term")'s consumption of its Qlik Reporting Service add-on subscription.
- The template needs to use content that is available to the users analyzing the application. In other words, if a template uses content from a private sheet, users will not be able to generate on-demand reports with this template.
- If the application uses [section access](#glossary-4 "Glossary term"), on-demand reports generated from this application will filter data based on the access level (as defined in the Section Access table) of the user generating the report.

## Configuring on-demand reports

The report developer activates [templates](#glossary-5 "Glossary term") for on-demand reporting.

Do the following:

1. Open the Templates tab in the Reporting section of an application.
2. Click ![Three-dot icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a template, then click ![Report](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_report_outline.svg) On-demand.

   The On-demand dialog opens.
3. Under File format, select the format options you want to make available for application consumers.
4. Enter a Title and Description.

   These are shown to users generating the report from the [sheet](#glossary-6 "Glossary term"). The Title will be the name of the downloaded file.
5. Click Save.

In the templates list, the template should now have a value of On in the On-demand column.

On-demand column in the Templates tab of an application, showing which templates have been activated for on-demand reporting

!['On-demand' column in the 'Templates' tab in the Reporting section of a Qlik Sense app, showing templates with different on-demand settings (on and off)](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CloudReportTemplate_on_demand.png "Click to view full size")

## Deactivating on-demand reports for a template

The report developer disables [templates](#glossary-7 "Glossary term") from being usable for on-demand reporting.

Do the following:

1. Open the Templates tab in the Reporting section of an application.
2. Click ![Three-dot icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a template, then click ![Report](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_report_outline.svg) On-demand.

   The On-demand dialog opens.
3. Under File format, deselect one or more format options. Deselect all available formats to deactivate the template completely from on-demand reporting.
4. Click Save.

## Permissions

To configure user generation of on-demand reports, you need:

- Permissions assigned to you by a tenant administrator. For more information, an administrator can refer to [*Setting permissions for metered reporting features*](../../Admin/mc-permissions-reporting.htm).
- Space permissions. See:

  - [*Requirements for applications in shared spaces*](#RequirementsShared)
  - [*Configuring on-demand reporting*](#RequirementsManaged)
  - [*Requirements for applications in your personal space*](#RequirementsPersonal)

  For more information about space permissions for reporting, see [*Qlik Reporting Service permissions*](../reporting-permissions.htm).

### Requirements for applications in shared spaces

For applications in [shared spaces](#glossary-8 "Glossary term"), you need Can edit permissions in the space to configure on-demand report generation for a template.

For more information, see [*Managing permissions in shared spaces*](../../Spaces/managing-shared-spaces.htm).

### Requirements for applications in managed spaces

To configure on-demand report generation for a template, you need one of the following roles in the managed space: Owner, Can manage, or Can operate.

Information noteFor user-based subscriptions, the Can operate role also requires a Professional user entitlement.

For more information, see [*Managing permissions in managed spaces*](../../Spaces/managing-managed-spaces.htm).

### Requirements for applications in your personal space

You must have the Private Analytics Content Creator user role in the tenant to configure on-demand report generation a template.

## User generation of on-demand reports

Users create on-demand reports as they analyze the [sheets](#glossary-9 "Glossary term") in an application.

For full details, see [*Creating on-demand reports*](reports-on-demand-create.htm).

## Limitations

On-demand reports have the following limitations:

- On-demand reports are not compatible with Star statements. If an application contains this statement in the script, the generated reports might show unexpected results.
