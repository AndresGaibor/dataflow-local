---
title: "Reporting from Qlik Cloud Analytics with Qlik Automate"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Automations/Reports-with-application-automations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics"]
---

# Reporting from Qlik Cloud Analytics with Qlik Automate

You can create automated multi-page reports based on a Qlik Sense application using Qlik Automate and the Qlik Reporting Service. Recipients can receive complex, scheduled reports, even if they do not have access to Qlik Cloud Analytics. Get started with a report template, or create a fully custom automation. Reports can be in PDF or PowerPoint format.

You can also integrate the Qlik Reporting Service API into your own enterprise systems. For more information about the API, see [Developer Portal for Qlik Cloud](https://qlik.dev/apis/rest/reports).

Information note

This functionality is not available in Qlik Sense Business or Qlik Cloud Analytics Standard.

## When to use reporting with Qlik Automate

Use the Qlik Reporting Service and Qlik Automate when you need to:

- Deliver bursted, multi-page reports.
- Deliver reports to external recipients, or internal recipients who cannot access Qlik Cloud Analytics.
- Create looping reports: a page within a report, looping over [dimension](#glossary-1 "Glossary term") values.
- Create a report based on multiple Qlik Cloud applications.

Report automations can be simple, such as a PDF where each page is a [sheet](#glossary-2 "Glossary term") from the Qlik Sense application. They can also be very complex. For example:

- A daily PowerPoint report where each page shows a different supply item that is running low, and should be re-ordered.
- A cycled report that goes out to all regional managers. Each manager only sees information relevant to their region. The recipient list is imported from Microsoft Office 365.
- A report that uses levels to create a month > category hierarchy to generate a report with sales for each product category for each month.

### Other ways to share data insights

In addition to generating reports with Qlik Automate, you can configure and generate reports from your application using in-application reporting. Output can be in Microsoft Excel, Microsoft PowerPoint, Microsoft Word, PDF, or HTML format. With in-application reporting, you create a report template using Qlik add-ins for Microsoft Office, the PixelPerfect designer, or the HTML designer. Create report tasks to control the distribution of the report output, employing filters to generate individualized output for report recipients. You can also activate on-demand reporting for specific templates, so that application users can generate reports instantly as they analyze sheets. For more information, see [*In-application reporting with Qlik Cloud Analytics*](../InAppGeneral/cloud-in-app-reports-intro.htm).

If you want to receive notifications when certain conditions are met in your data, see [*Monitoring data with alerts*](../../Alerting/monitoring-changes-with-alerts.htm). Alerts are evaluated based on data reloads and are sent based on data exceptions. Alerts can also trigger on a schedule, but you still need to create a condition or target to save an alert. You can add Qlik Sense users to an alert.

If you want to receive regular updates about a single chart or sheet based solely on a schedule, you can create a subscription. For more information, see [*Scheduling reports with subscriptions*](../Subscriptions/Subscription-reports.htm). You can add Qlik Cloud users to a subscription.

## Security

Once a report is created using an automation, you can share the document with anyone. This means you could potentially share data from an application that recipients in your Qlik Cloud system do not have permission to view. Or you might be sharing data with people outside your Qlik Cloud system.

Warning noteBefore creating and sending reports, make sure you understand the security implications of the application and data used to create the report.

## Report overview

### Features

You can create automated reports using the [Qlik Reporting connector](/en-US/cloud-services/Subsystems/Sense_QlikAutomation/Content/Sense_QlikAutomation/connector-blocks/connectors-intro.htm#anchor-4) included with Qlik Automate. A report automation can be connected to multiple Qlik Sense applications. Your automation can access everything in the application, including charts, data, selections, fields, and variables. You can customize the report by applying different selections to specific sheets, or by configuring sheets to show alternate states.

Qlik Cloud Analytics provides report templates that can be customized and re-used. If your reports are distributed as PowerPoint files, they can be edited by your recipients.

Your reports can have a dynamic name based on fields or [variables](#glossary-3 "Glossary term"). For example, a daily report can have the date it was generated as part of the name.

### Access

You can only make a report automation with Qlik Sense applications you have permission to access. Report automations are saved in your [personal space](#glossary-4 "Glossary term").

### Recipients

Your recipients do not need to have a Qlik Cloud user account. You can add recipients in several ways:

- manually
- table or data source in the Qlik Sense application
- Microsoft Office 365 file
- Amazon S3 file
- spreadsheet
- database

### Distribution

The report is generated as a PDF or PowerPoint document. Reports can be generated on a schedule or based on a trigger.

Reports can be delivered to email or Qlik Automate cloud storage connectors. External email clients often enforce size limits for email attachments. Check with your email provider to find out what your limit is. Reports delivered using cloud connectors have no file size limit.

The following connectors are available:

- Amazon S3
- Dropbox
- FTP
- Google Cloud Storage
- SFTP

For more information, see [Connector blocks](/en-US/cloud-services/Subsystems/Sense_QlikAutomation/Content/Sense_QlikAutomation/connector-blocks/connectors-intro.htm).

## Permissions

To work with report automations, you need specific permissions:

- Permissions assigned to you by tenant administrators. See [*Setting permissions for metered reporting features*](../../Admin/mc-permissions-reporting.htm).
- The required space roles. These are required for applications in shared and managed spaces, as well as shared automations. See:

  - [*Shared space permissions for Professional and capacity-based subscription users*](../../Spaces/permissions-shared-space-prof-full.htm)
  - [*Shared space permissions for users with Analyzer entitlement*](../../Spaces/permissions-shared-space-analyzer.htm)
  - [*Shared space permissions for administrators*](../../Spaces/permissions-shared-space-admin.htm)
  - [*Managed space permissions for Professional and capacity-based subscription users*](../../Spaces/permissions-managed-space-prof-full.htm)
  - [*Managed space permissions for users with Analyzer entitlement*](../../Spaces/permissions-managed-space-analyzer.htm)
  - [*Managed space permissions for administrators*](../../Spaces/permissions-managed-space-admin.htm)

## Learn more

- [*Qlik Reporting Service specifications and limitations*](../Reporting-service-specifications-limitations.htm)
