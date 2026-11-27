---
title: "Delivering reports to a distribution folder"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Generate/cloud-in-app-reports-output-folder.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Configuring report generation"]
---

# Delivering reports to a distribution folder

You can configure a [report task](#glossary-0 "Glossary term") to generate and deliver output to a remote distribution folder on Microsoft SharePoint. This can be used alongside, or as an alternative to, report delivery by the default email delivery option. The default delivery method for generated reports is email, but this option allows you to also store reports directly into a cloud-based Microsoft SharePoint folder.

Connect to folders available within your connection to the Office 365 Sharepoint connector.

## Report generation with distribution folders

Report distribution via distribution folder sends the report output via the established connection to the Office 365 Sharepoint connector.

When you configure a [report task](#glossary-1 "Glossary term") with the intention of delivery via distribution folder, you must still include recipients and groups as receivers of the output. This is done in the Users & groups section of the report task dialog (under Distribute). Delivering report task output to a distribution folder does not send the output directly to each recipient. Instead, when the report task runs, a separate report file is generated and stored in the folder for each filter defined on the recipients you have included in the task. Any task-level filter is applied to each file and interacts with the recipient-level filters as it does for email delivery.

For more context on how filters interact with file generation from report tasks, see [*How report generation works*](cloud-in-app-reports-tasks.htm#How).

### Example

Let's say you add four recipients to your report task:

- User1, with filter A
- User1, with filter B
- User2, with filter A
- User2, with filter C

In this case, three separate reports, one for each unique recipient-level filter, are generated and stored in the folder.

## Setting up output to a distribution folder

Before you begin, make sure there is a connection to theOffice 365 Sharepoint connector already created in the space. To learn how to create a connection to the Office 365 Sharepoint connector, see [Office 365 Sharepoint](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/Office365-Sharepoint-storage-provider-connector.htm).

Do the following:

1. Begin the regular workflow for creating or editing a report task. See [*Creating a report task*](cloud-in-app-reports-tasks.htm#Creating).
2. Add Users & groups from the [distribution list](#glossary-2 "Glossary term"). Note that a separate recipient must be added for each recipient-level filter you want to generate reports for. See [*Report generation with distribution folders*](#DistFold).
3. When you arrive at the Distribute section of the configuration dialog, toggle on the Folder option.
4. Under Connection, select the Office 365 Sharepoint connection from the drop down list.
5. Under Folder path, enter the path of the folder you want the reports to be stored in.

   Tip note

   This might take some trial and error. The sub-site (provided in the connection configuration) is not included in the path. The folder path starts with the top-level folder within the sub-site. Separate the folder structure with forward slashes.

   For example, if your sub-site is named ParacelCompany, the distribution folder is EnterpriseReports2023, and it is located inside a folder named SalesAndRevenue, your folder path is: EnterpriseReports2023/SalesAndRevenue

   You can deliver report task output to a Microsoft SharePoint connection

   ![Clicking the button in the Recipients tab to download the example source file](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CloudExcelReportSharePoint.png "Click to view full size")
6. Click Next to proceed to the next step in configuring the report task.

## Permissions

To configure a report task to deliver reports by distribution folder, you need:

- Permissions assigned to you by a tenant administrator. For more information, an administrator can refer to [*Setting permissions for metered reporting features*](../../Admin/mc-permissions-reporting.htm).
- Space permissions. See:

  - [*Shared spaces*](#Shared)
  - [*Managed spaces*](#Managed)

### Shared spaces

For an application in a [shared space](#glossary-3 "Glossary term"), you need Can edit permissions in the space to configure the report task, including selecting a distribution folder from an existing [connection](#glossary-4 "Glossary term").

If your application is in a shared space and you are creating the Office 365 Sharepoint connection from scratch, you must have Can edit permissions in the space to create a connection.

For more information about permissions in shared spaces, see [*Managing permissions in shared spaces*](../../Spaces/managing-shared-spaces.htm).

### Managed spaces

For an application in a [managed space](#glossary-5 "Glossary term"), you need one of the following roles in the space to configure the report task, including selecting a distribution folder from an existing [connection](#glossary-6 "Glossary term").

- Owner
- Can manage
- Can operate

Information noteFor user-based subscriptions, the Can operate role also requires a Professional user entitlement.

If your application is in a managed space and you are creating the Office 365 Sharepoint connection from scratch, you must have Professional user entitlement (this requirement does not apply to capacity-based subscriptions), as well as Owner, Can manage, or Can operate permissions in the space, to create a connection.

## Section access considerations

Report delivery via Microsoft SharePoint distribution folder is not available if the application uses section access.

For additional information about how section access affects in-application reporting with Qlik Cloud Analytics, see [*In-application reporting and section access*](cloud-in-app-reports-section-access.htm).

## Learn more

- [Office 365 Sharepoint](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/Office365-Sharepoint-storage-provider-connector.htm)
- [*Working with report tasks*](cloud-in-app-reports-tasks.htm)
- [*Working with report filters*](cloud-in-app-reports-filters.htm)
