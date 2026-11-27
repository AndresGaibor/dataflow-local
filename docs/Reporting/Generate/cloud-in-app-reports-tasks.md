---
title: "Working with report tasks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Generate/cloud-in-app-reports-tasks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Configuring report generation"]
---

# Working with report tasks

As a report developer, you can create configurations for centralized report generation with [report tasks](#glossary-0 "Glossary term"). Create and manage report tasks in the Report tasks tab within the Reporting section of an application.

A report task converts the [report template](#glossary-2 "Glossary term") into the report output. The task can be run manually or on a schedule.

A report task is where reporting building blocks – templates, [filters](#glossary-3 "Glossary term"), and [distribution list](#glossary-4 "Glossary term") – come together to generate the output. When you create a report task, you also set the report file names, the users and groups who receive the output, the email or output folder details, and the schedule for when its reports are generated.

The Report tasks tab in the Reporting section of an application

![The 'Report tasks' tab in the app's Reporting section](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CloudInAppReportTasks.png "Click to view full size")

With the help of report filters, you can use a single report task to administer and employ a report bursting use case. Report bursting allows you to generate reports with varied information with different subsets of data for different recipient parties. For more information, see [*Burst reporting using report filters*](cloud-in-app-reports-bursting.htm).

## How report generation works

You must define a [distribution list](#glossary-5 "Glossary term") for the application before you can create report tasks.

In a report task, you select the recipients and groups from your distribution list that you want to generate reports for. When adding recipients as receivers of the task output, you add the recipient as a user-filter pairing which corresponds to a single recipient-level [filter](#glossary-6 "Glossary term") that has been applied to them in the distribution list. You cannot combine multiple recipient-level filters in the same user report, but you can add each user-filter pairing individually in the task configuration so that a separate report is generated and sent to the same user for each filter.

When a report task runs, a unique report is generated for each distinct recipient-level filter applied across all users added to the report task.

A [report task](#glossary-7 "Glossary term") can generate a maximum of 500 unique reports. This limit is evaluated across all templates added to the task, rather than per template in the task. This limit also applies to all report tasks regardless of whether or not one or mores cycles are applied.

Information noteReport generation might work differently if the application uses section access. For more information, see [*In-application reporting and section access*](cloud-in-app-reports-section-access.htm).

You can choose to send the generated reports by email, store them to a Microsoft SharePoint folder, or both. When you deliver reports via a Microsoft SharePoint distribution folder, reports are not sent directly to recipients and a separate report is stored for each filter defined on the recipients you have included in the task. For further details, see [*Report generation with distribution folders*](cloud-in-app-reports-output-folder.htm#DistFold).

### Requirements for email delivery

To send report task output by email, toggle on the Email switch under Distribute in the dialog when you are creating the report task.

If you are sending the reports by email, an email provider must be configured for the Qlik Cloud tenant. For instructions on setting this up, see [*Configuring email for reports and notifications*](../../Admin/mc-configure-email-support.htm).

### Requirements for storing reports in Microsoft SharePoint folders

If you need to automatically save generated reports to a folder in your Microsoft SharePoint network, toggle on the Folder switch under Distribute in the dialog when you are creating the report task.

To store the report output to a Microsoft SharePoint folder, a connection to the Office 365 Sharepoint connector must be created in the space. For more information, see [*Delivering reports to a distribution folder*](cloud-in-app-reports-output-folder.htm).

## Creating a report task

To create a task-based report configuration, follow the sections below in order.

### Before you start

Before you can create report tasks, you need to define a distribution list. See [*Creating a distribution list for your report*](cloud-in-app-reports-distribution.htm).

### Part 1: Create the task

Do the following:

1. Open the Report tasks tab in the Reporting section of the Qlik Sense application.

   [*Navigating in the application interface*](../../UserInterface/navigate-user-interface.htm)
2. Click Create report task. The report task dialog opens.
3. Enter a Title for your report task.
4. Optionally, add a Description.

### Part 2: Select one or more templates

Next, you need to define the [templates](#glossary-8 "Glossary term").

Do the following:

1. In the Template dialog tab, click Add existing template. Select a template you have already created.

   Alternatively, click Upload new if you have not already added the template you want to use.
2. Optionally, add additional templates to the task using the procedure in the first step.

   You can add up to five report template instances to a report task, including copies of the same template. For example, if you add an Excel template twice to a task, with one .xlsx and one PDF output, this counts as two templates added to the task.
3. Click Next. The dialog moves to the Output tab.

### Part 3: Configure the output

Next, configure the output. Output is configured separately for each template instance you add to the task. The output consists of:

- Defining the properties of the generated reports.
- Defining localization of report elements (only for PDF output). Users opening a report in Excel, PowerPoint, or Word format will see region-dependent formatting (dates, numbers, and other information) as per their settings in the respective Microsoft Office application.
- Applying a task-level filter.
- Applying cycles.

Do the following:

1. In the Output dialog tab, expand a template instance you have added.
2. To configure report file names, do one of the following:

   - Standard naming:

     Use the default File name and Timestamp format settings. Enter the file name to use as the base for each report.

     Information noteSpecial characters are not allowed in the File name. Leading and trailing spaces are removed.

     Information noteStandard naming will be replaced with advanced report naming in October 2027. Turn on Advanced report naming to configure file names before the change.
   - Advanced naming:

     For more in-depth file name customization, turn on Advanced report naming. This replaces the standard File name and Timestamp format settings.

     Add up to 10 segments in the order you want them to appear in the file name. Use the Add menu to add segments. The following types are available:

     - Text: Add literal text.
     - Cycle: Add the cycle name, if configured.
     - Recipient email: Add the recipient's email address.
     - Recipient filter name: Add the names of the filters applied to the recipient (both at the recipient and task levels).
     - Recipient name: Add the recipient's name.
     - Timestamp format: Add a timestamp for when the report was created. You can choose from several different timestamp formats.

     Considerations for advanced naming:

     - If some values are not set for the specific run (for example, you use a filters tag, but no filter is configured), the tag will be completely removed. This may result in an empty file name being generated. In some cases, delivery systems (for example, Exchange servers) may generate a random file name that will be displayed in place of the empty name.
     - If your file name configuration produces duplicate names across different runs, files on SharePoint may be overwritten over time.
3. If you selected PDF output, define the Regional format settings for the PDF. This setting controls the locale in which dates, numbers, and other information are formatted in the reports.

   If you need to perform other configurations to prepare for PDF or printed output, return to template creation.
4. Optionally, select a Filter to apply to the reports.

   This filter applies to all reports generated from the template instance, unlike filters you add to individual recipients. For more information about how task-level and recipient-level filters interact with each other, see [*Working with report filters*](cloud-in-app-reports-filters.htm#Using).
5. Under Cycle, select up to three dimensions to use as cycles. Adding cycles will generate a unique version of the reports for each unique value in the dimension. For more information, see [*Cycling reports*](reports-cycles.htm).
6. Repeat the above procedure for any other template instances you have added to the task.
7. Click Next to proceed to the Distribute dialog tab.

### Part 4: Configure distribution

You should now be in the Distribute tab in the dialog.

Do the following:

1. Add the recipients and groups from your distribution list who will receive the report output. Note that a separate recipient must be added for each recipient-level filter you want to generate reports for. See [*How report generation works*](#How).
2. Specify how to distribute and deliver your reports. Toggle on at least one of the following options:

   - To deliver your reports by email, leave the Email switch on. This is the default delivery method. Delivery is as follows:

     - For HTML templates in the task, you can choose to attach reports as files, embed a report in the email message itself, or both. For more information, see [*Embedding report content in an email message*](html-report-as-email.htm).
     - For templates of all other types within the task, reports will be included as email attachments.
   - To deliver your reports to a Microsoft SharePoint folder, toggle on the Folder switch.

     For specifics about configuring email and distribution folder options, see [*Requirements for email delivery*](#Requirem) and [*Requirements for storing reports in Microsoft SharePoint folders*](#Requirem3).
3. Fill in the required fields for Email and/or Folder output as needed.
4. Click Next to proceed to the Schedule dialog tab.

### Part 5: Schedule report delivery

Do the following:

1. In the Schedule dialog tab, configure the report distribution schedule. Reports can be sent whenever data is refreshed, or on a daily, weekly, monthly, or yearly schedule.
2. Click Save.

Your report will be sent to your recipients at the scheduled time. You can also send the report task output at any time. See [*Manually sending reports*](#Manually).

## Manually sending reports

You can run a report task manually when you need recipients to receive the reports immediately.

This is also helpful when you're testing your report configuration.

Do the following:

1. Open the Report tasks tab in the Reporting section of an application.
2. Click ![More actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the report task you want to run.
3. Click ![Send](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_send_outline.svg)Send now.

## Requirements for a report task to run successfully

The report template creator creates a template based on their access to the application content. However, a report task runs based on the application access of the report task owner. Therefore, if a user creates a [template](#glossary-9 "Glossary term") based on an application sheet that is private to them, the report task cannot run successfully.

There are also requirements related to report task ownership. For more information, see [*Ownership of report tasks*](#Ownershi).

## Editing report tasks

You can change the configuration of the report task after it has been created.

Do the following:

1. Open the Report tasks tab in the Reporting section of an application.
2. Click ![More actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the report task.
3. Click ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit.

## Deleting a report task

Do the following:

1. Open the Report tasks tab in the Reporting section of an application.
2. Click ![More actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the report task you want to delete.
3. Click ![Trash bin](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) Delete.

Tenant admins can delete and manage report tasks in the Subscriptions section of the Administration activity center.
See [*Administering reporting and subscriptions*](../../Admin/mc-administer-subscriptions.htm).

## Enabling or disabling a report task

A report task can be enabled or disabled. When it is enabled, the report task generates output as per the configured schedule, and can be manually run as needed. When it is disabled, the report task cannot generate output on the schedule, but can still be manually run as needed.

You might want to enable or disable the report task manually. There are also situations in which a report task will be automatically disabled.

Do the following:

1. Open the Report tasks tab in the Reporting section of an application.
2. Click ![More actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the report task you want to turn on or off.
3. Click ![Checkmark box](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_success_outline.svg) Enable or ![Disable](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_restricted.svg) Disable.

If you are a [tenant admin](#glossary-10 "Glossary term"), you can enable and disable the report task in the Subscriptions section of the Administration activity center.
For more information, see [*Administering reporting and subscriptions*](../../Admin/mc-administer-subscriptions.htm).

Information noteIt is important to be aware of how enabling and disabling report tasks works for applications with section access. See [*Section access considerations*](#Section).

## Canceling a currently running report task

There might be a time when a report task is currently running but you need to cancel it. This might be when there is a server error, or when the task is taking too long.

Do the following:

1. Open the Report tasks tab in the Reporting section of an application.
2. Click ![More actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the report task you want to cancel.
3. Click ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove_outline.svg) Cancel.

## Viewing the execution history for a report task

You can view the history of when the report task was run. Use the History view to view more information about errors that might have happened during task execution.

Do the following:

1. In an application, open the Reports section.
2. In the Report tasks tab, click ![Three-dot menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a report task.
3. Select ![Clock](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_history.svg) History.

Tip noteYou can also simply click a report task to open its history.

For more information, see [*Viewing execution history for report tasks*](report-tasks-history.htm).

## Setting up multiple outputs for the same template

You can add up to five report template instances to a report task, including copies of the same template. For example, if you add an Excel template twice to a task, with one .xlsx and one PDF output, this counts as two templates added to the task.

The following are common use cases for adding the same template more than once to a single report task:

- Generating reports into two different file formats—for example, a .xlsx and PDF copy of a single report.
- Embedding the report into an email body message, but also including an HTML copy of the same report as an email attachment.
- Generating reports with two different localization settings.

To achieve this output from the same template, add it twice (or more than twice) to the report task.

Do the following:

1. In the Template dialog tab when configuring a report task, select the template to use, or click Upload new to upload it.
2. After adding the first template instance, click Add existing template.
3. Select the same template again.
4. Click Next.
5. In the Output settings, configure a different report name for each template instance. If Advanced report naming is on, use distinct segments for each instance. Otherwise, enter a different File name.
6. Complete the configuration for the report task.

## Section access considerations

If the application uses section access, report generation works differently. For more information, see [*In-application reporting and section access*](cloud-in-app-reports-section-access.htm).

## Ownership of report tasks

When you create a report task, you become its owner. Administrators can change the owner of a report task. For more information, see [*Administering reporting and subscriptions*](../../Admin/mc-administer-subscriptions.htm). In a shared space, to transfer ownership of a report task to another user, that user needs to have Can edit permissions in the space.

Anyone with Can edit access to the space can run a report task, but if the report task owner does not have Can edit access to the space, the report task cannot run successfully. Therefore, if the user who owns a report task loses Can edit access, or is removed from the space or the tenant, either the ownership of the report task needs to change or the report task should be recreated by someone with sufficient permissions.

Keep in mind that if you change the owner of a report task for an application which uses section access, certain behaviors can be expected. For more information, see [*In-application reporting and section access*](cloud-in-app-reports-section-access.htm).

### Report filters and report task ownership

Report filters also have corresponding owners. The creator of a report filter is its first owner. Changing the owner of a report task does not change the owner of any report filters used by the report task.

## Permissions for report tasks

Managing the report tasks of an application requires specific roles. The permissions requirements vary depending on the type of space in which your application is located.

To work with report tasks for an application, you need:

- Permissions assigned to you by a tenant administrator. For more information, an administrator can refer to [*Setting permissions for metered reporting features*](../../Admin/mc-permissions-reporting.htm).
- [*Space permissions*](#Space)

  For more information about space permissions for reporting, see [*Qlik Reporting Service permissions*](../reporting-permissions.htm).

### Space permissions

Managing the report tasks for an application requires specific space roles. The requirements depend on the type of space in which your application is located.

#### Requirements for applications in shared spaces

You need Can edit access to the space to perform the following actions on a report task from within the application:

- View
- Create
- Run
- Delete
- Enable
- Disable

For more information, see [*Managing permissions in shared spaces*](../../Spaces/managing-shared-spaces.htm).

#### Requirements for applications in managed spaces

Users with the Owner, Can manage, or Can operate roles in a managed space can perform the following actions on a report task from within the application:

Information noteFor user-based subscriptions, the Can operate role also requires a Professional user entitlement.

- View
- Create
- Run
- Delete
- Enable
- Disable

For more information, see [*Managing permissions in managed spaces*](../../Spaces/managing-managed-spaces.htm).

#### Requirements for an application in your personal space

You must have the Private Analytics Content Creator user role in the tenant to view, create, edit, and delete report tasks.

## Administering report tasks in the Administration activity center

As an administrator, you manage report tasks in the Subscriptions section of the Administration activity center.
See [*Administering reporting and subscriptions*](../../Admin/mc-administer-subscriptions.htm).

## Learn more

- [*Enabling and disabling reporting, subscriptions, and sharing features*](../../Admin/mc-enable-reporting-features.htm)
- [*Troubleshooting - In-application reporting*](../../Troubleshooting/troubleshooting-reporting.htm)
