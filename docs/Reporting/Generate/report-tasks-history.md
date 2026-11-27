---
title: "Viewing execution history for report tasks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Generate/report-tasks-history.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Configuring report generation", "Working with report tasks"]
---

# Viewing execution history for report tasks

Use History in a [report task](#glossary-0 "Glossary term") to view the history of the executions of a report task. Use this view to more easily diagnose errors with the dependencies in the report task.

You can view detailed information about each execution of the report task that was run within the past three months.

History view for a report task

![Image showing Report task 'History' view when it is first opened (no executions expanded for further details)](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_report-task-history4.png "Click to view full size")

## What is an execution of a report task?

A report task is an asset within an application that generates reports and sends them to the selected recipients. Report tasks are designed to be run many times, often on a schedule. Each time a report task runs, reports are generated and sent. Each occurrence of the report task running is an execution of that report task.

A report task can be executed in several different ways:

- It is manually triggered by a user clicking Send now on the task. This is a one-time execution.
- It is set up to be executed whenever the application data is refreshed.
- It is a scheduled execution. For example, you might have set your report task to run twice per week on a recurring basis.

Errors can occur when executing a report task. The History view in a report task can help you identify the issues that were encountered during the execution.

### Statuses for report task executions

A report task execution results in one of the following three statuses:

- Successful: The report task ran successfully without encountering any warnings or errors. All reports were generated and sent. This status is shown in green (either with the ![Checkbox](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_success_outline.svg) icon or as a green circle).
- Errors: The report task could not run successfully because of one or more errors. No reports were generated or sent. This status is shown in red (either with the ![Errors box](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning.svg) icon or as a red circle).
- Warnings:  One or more errors were encountered but some reports were still sent. Some reports may have been generated and sent, but others could have failed. This status is shown in orange (either with the ![Warnings box](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning_triangle_2.svg) icon or as an orange circle).
- Canceled: The execution was started but then canceled before it finished running. This status is shown in black, with the ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove_outline.svg) icon.

## Opening the history for a task

Do the following:

1. In an application, open the Reports section.
2. In the Report tasks tab, click ![Three-dot menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a report task.
3. Select ![Clock](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_history.svg) History.

Tip noteYou can also simply click a report task to open its history.

## Viewing details about the report task from History

When you open History for a report task, you can view the following details at the top of the window:

- When the report task was created.
- When the task is set to run, or if it has been disabled.
- The owner of the report task.

The History view also provides access to actions such as editing, running (Send now), deleting, and disabling the report task.

For more information about working with report tasks, see [*Working with report tasks*](cloud-in-app-reports-tasks.htm).

## Filtering executions

It is possible that when you open History, there are a lot of executions shown. You can filter the executions to only show what you need to analyze.

First, open the History pane for a report task. See [*Opening the history for a task*](#Open).

### Filtering by date

Do the following:

1. In the History window, click the Date filter box.

   A calendar opens.
2. Select the first date from which you want to start including executions.
3. Select the last date from which you want to stop including executions.

   Tip noteYou can set the filter to include only one day by clicking the same day again.

### Filtering by status

Do the following:

1. In the History window, click the Status filter box.
2. In the drop down menu, select one or more statuses. There are the following statuses:

   - Successful
   - Errors
   - Warnings
   - Canceled

   For more information about what each status means, see [*Statuses for report task executions*](#Statuses).

## Analyzing task execution details

Under History, execution histories are organized by month and year. For a given month of the year, you can see how many report task executions ended with Successful ![Checkbox](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_success_outline.svg), Errors ![Errors box](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning.svg), and Warnings ![Warning box](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning_triangle_2.svg), and Canceled ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove_outline.svg) statuses.

Click a month to expand and show each execution. Then, click a specific execution to view more details. Each execution status is shown as a circle with a specific color:

- Successful: Green
- Errors: Red
- Warnings: Yellow
- Canceled: Black with ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove_outline.svg) icon

The timestamp for each execution is shown in the time zone of the current user. Therefore, timestamps and total executions per month can be different for each user, depending on when the executions were run and the user's time zone. The user's current time zone is configured in their personal settings. For more information, see [*Managing your personal settings*](../../Introduction/profile-settings.htm).

Tip note

You can also identify the execution status by the subtitle displayed underneath the execution time header, when expanded. The statuses might look something like the following:

- Successful: A subtitle that says Sent.
- Errors: A subtitle that says Not sent - <number> error(s).
- Warnings: A subtitle that says Sent - <number> error(s).
- Canceled: A subtitle that says Canceled.

### Analyzing errors

If there were errors during the execution, they are listed at the top of the expanded execution summary. The error details are helpful in resolving issues with the report task. For example, you might have renamed a report filter used in the task, but did not make the corresponding change in the distribution list. In this example, the error title would indicate that this is the issue, and the name of the report filter would be listed in the error details.

Information noteError messages are not translated in the History view.

Click Copy to clipboard to copy the error details. The details also include an error code and trace ID, which you can provide to Qlik [Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport) if you need further assistance.

Expanded details for a report task execution, showing a summary of the error that caused the execution to end with the Errors status.

![The 'History' view for a report task, with an individual task execution expanded. The expanded view shows details about the execution, such as its status, any error codes, and information about the configuration of the report task at the time of the execution](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen-report-task-history-expanded.png "Click to view full size")

Other details are shown in the expanded summary for an execution to help you further troubleshoot:

- How long the execution took to run.
- When the execution ran.
- How it was triggered (that is, manually, on a schedule, or by reload), and who triggered it.
- Delivery channels: Shows whether the execution aimed to create an email, store content in a Microsoft SharePoint location, or both.
- Recipients: The number of recipients.
- Cycles: The fields that were used in any [cycles](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/reports-cycles.htm) applied for the execution.
- Reports generated: The number of unique reports generated.
- Reports failed: The number of unique reports that failed to generate.
- Templates: The number of templates added to the task. Copies of the same template are counted as separate items in this total.
- Task execution ID: The ID for the execution.

## Permissions

To access History in a report task, you need one of the following roles in the space where the application is located:

- Shared space: Can edit, Can edit data in applications, Can manage, or Owner
- Managed space: Can manage or Owner

To access History you need permissions for working with report tasks. For more information, see [*Permissions for report tasks*](cloud-in-app-reports-tasks.htm#Permissi).
