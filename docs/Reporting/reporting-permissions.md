---
title: "Qlik Reporting Service permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/reporting-permissions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics"]
---

# Qlik Reporting Service permissions

This topic outlines the required permissions that users need for working with the value-add (metered) capabilities of the Qlik Reporting Service.

## Scope of this page

This page outlines permissions for working with value-add capabilities of the Qlik Reporting Service. This includes:

- In-application reporting, including on-demand reporting
- Reporting with Qlik Automate
- Usage of the Qlik Reporting Service API for metered operations. This excludes using the API for other functionality, such as [subscriptions](#glossary-0 "Glossary term") and downloads of application content.

## Administrator controls

Tenant administrators set permissions to control which users can access metered reporting capabilities. Users can be granted full access, partial access, or no access. These permissions are prerequisites to be able to work with reporting in spaces. If you do not have the required administration-assigned permissions, you are not granted access in any space.

For full details, see [*Setting permissions for metered reporting features*](../Admin/mc-permissions-reporting.htm).

## Space permissions for in-application reporting

This section outlines the space roles required for performing different actions within the in-application reporting capability.

### Template development

#### Tabular (Excel), PowerPoint, and Word reports

To connect to an application in Qlik add-ins for Microsoft Office, you need:

- For applications in shared spaces, one of the following roles:

  - Owner (of the space)
  - Can manage
  - Can edit data in applications
  - Can edit
- For applications in managed spaces, one of the following roles:

  - Owner (of the space)
  - Can manage
  - Can contribute
  - Can operate (Professional and capacity-based subscription users only)

After connecting to the application, you have full access to the report development features.

#### PixelPerfect and HTML reports

To work with the PixelPerfect and HTML designers, you need:

- For applications in shared spaces, one of the following roles:

  - Owner (of the space)
  - Can manage
  - Can edit data in applications
  - Can edit
- For applications in managed spaces, one of the following roles:

  - Owner (of space)
  - Can manage
  - Can operate (Professional and capacity-based subscription users only)

### Report tasks, template management, filters, and output folders

To work with report tasks, template management, filters, and output folders, you generally need the following. An exception is noted below.

- For applications in shared spaces, one of the following roles:

  - Owner (of the space)
  - Can manage
  - Can edit data in applications
  - Can edit
- For applications in managed spaces, one of the following roles:

  - Owner (of space)
  - Can manage
  - Can operate (Professional and capacity-based subscription users only)

#### Exception

Anyone with Can edit access to the space can run a report task, but if the report task owner does not have Can edit access to the space, the report task cannot run successfully. Therefore, if the user who owns a report task loses Can edit access, or is removed from the space or the tenant, either the ownership of the report task needs to change or the report task should be recreated by someone with sufficient permissions.

### Distribution lists

To view the distribution list in the Reporting section of the application, you need:

- For applications in shared spaces, one of the following roles:

  - Owner (of the space)
  - Can manage
  - Can edit data in applications
  - Can edit
- For applications in managed spaces, one of the following roles:

  - Owner (of space)
  - Can manage
  - Can operate (Professional and capacity-based subscription users only)

To edit, re-upload, and delete the distribution list for an application in a shared space, you need to have the Can edit in apps role in the space, or otherwise you need to be the application owner and have space access.

### On-demand report generation

To generate on-demand reports, you need:

- For applications in shared spaces, one of the following roles:

  - Owner (of the space)
  - Can manage
  - Can edit data in applications
  - Can edit
  - Can view (in space or to application only)
- For applications in managed spaces, one of the following roles:

  - Owner (of space)
  - Can manage
  - Can publish
  - Can contribute (in space or to application only)
  - Can view (in space or to application only)
  - Has restricted view (in space or to application only)
  - Can operate (Professional and capacity-based subscription users only)

## Space permissions for reporting with Qlik Automate

Permissions for Qlik Reporting automations are governed by the space in which the automation is located, as well as access to the applications upon which the report might be generated.

Automations and automation connections can be created in shared spaces. For the associated permissions, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](../Spaces/permissions-shared-space-admin.htm)

## Space permissions — reference tables

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](../Spaces/permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](../Spaces/permissions-managed-space-admin.htm)
