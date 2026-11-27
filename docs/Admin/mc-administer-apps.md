---
title: "Managing applications for tenant and analytics administrators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-apps.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources"]
---

# Managing applications for tenant and analytics administrators

If you are a tenant admin or analytics admin, you can move applications between [managed spaces](#glossary-0 "Glossary term") or between self-managed (personal or shared) spaces, change owner of applications, delete applications, and manage reload schedules.

## Administrator access for managing applications

Tenant and analytics administrators have different access to manage applications:

- Tenant administrators can manage all applications in managed, shared, and personal spaces.
- Analytics administrator can manage applications in managed and shared spaces, but not in other users' personal spaces.

  Information noteAnalytics admins can change an application’s owner while the application is in a managed or shared space, even if it moves to the new owner’s personal space. After the change, analytics admins can no longer manage the application.

Application owners and developers can also manage application properties. For more information, see [Managing applications](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/manage-apps.htm).

## Applications overview

To manage applications, go to the Content page in the Administration activity center and open the Applications tab. The tab displays a table with information about the owner, space, and size of the application. The size refers to the base memory footprint of the application. You can also see when the application was last updated and find details about scheduled data reloads. You can sort by the columns Name or Last updated, and filter by Name, ID, Owner or Space.

Select Source, Published, Staged, or Activated for Qlik Answers in the dropdown list above the table:

- Source shows applications that are in personal or shared spaces. As a tenant admin or analytics admin, you can perform the following actions on these applications:

  - Manage the application reload schedule
  - Change the owner of the application
  - Move the application to another space
  - Delete the application
- Published shows applications that are in managed spaces. As a tenant admin or analytics admin, you can perform the following actions on these applications:

  - Manage the application reload schedule
  - Move the application to another space
  - Delete the application
- Staged shows applications that do not have an owner and do not belong to a space. Staged applications are only visible for tenant admins and analytics admins. As a tenant or analytics admin, you can perform the following actions on these applications:

  - Set a space for the application
  - Delete the application
- Activated for Qlik Answers shows the applications that have been activated for use with Qlik Answers. As a tenant or analytics admin, you can perform the following actions on these applications:

  - Deactivate the application for Qlik Answers
  - Delete the applications

  Information noteThis option is only available if you are licensed for Qlik Answers and are using the agentic experience. For more information, see [*Deploying and administering Qlik Answers*](../QlikAnswers/administering-qlik-answers.htm).

## Changing owner of applications

As a tenant or analytics admin, you can change owner of an application.

Do the following:

1. In the Administration activity center, go to Content > Applications.
2. Select Source.
3. Select one or more applications and click Change owner.
4. In the Change owner dialog, select the user you want to make the new owner, and then click Apply.

Tip noteTo change the owner of a published application, first change the owner of the source application and then republish it to the managed space. The published copy of the application will have the same owner as the source application.

### Section access considerations

Tenant administrators cannot directly download applications from other users' personal spaces. However:

- If the application does not have [section access](#glossary-2 "Glossary term"), the tenant administrator can take ownership of the application and then download it.
- Private applications that manage security with section access can be downloaded only by the application owner from their [personal space](#glossary-4 "Glossary term"). If a tenant admin has downloaded an application with section access from a shared or managed space, and they are not the application owner, they will not be able to access the load script upon upload to another Qlik Cloud tenant. The administrator must duplicate the application to access [Data load editor](#glossary-5 "Glossary term") and manage the script.

## Changing space of applications

As a tenant or analytics admin, you can move an application to another space.

Do the following:

1. In the Administration activity center, go to Content > Applications.
2. Select Source or Published.
3. Select one or more applications and click Move.
4. In the Move dialog, select the space where you'd like to move the applications, and then click Confirm.

   Information note

   When changing the space of an application, you might need higher permissions. If required, select the Get elevated privileges checkbox before confirming.

   Elevated privileges are required if you're not the owner of the application or don’t have Can manage permission for either the current or new space. These privileges are temporary and will be reverted after the space change is complete.

## Setting the space for staged applications

As a tenant or analytics admin, you can select a space for staged applications.

Do the following:

1. In the Administration activity center, go to Content > Applications.
2. Select Staged.
3. Select one or more applications and click Set space.
4. In the Select space dialog, select the space where you'd like to add the applications, and then click Confirm.

## Managing scheduled reloads of application data

Reloading an application updates it with the latest data from the application data sources. Applications can be reloaded manually from [activity centers](#glossary-6 "Glossary term") or on a schedule. Scheduled reloads can be configured by creating tasks with time-based or event-based triggers.

As a tenant admin or analytics admin, you can view and delete tasks that have been created for scheduled reloads. This is done in the Administration activity center.
You can see the time of the last reload and the next planned reload. With proper permissions in the spaces where the applications and data sources are stored, you can also create and edit these tasks.

For detailed information about tasks for scheduled reloads of applications, including limitations and considerations, see [*Reloading application data*](../Apps/reloading-apps-cloud-hub.htm). For information about the permissions required to reload data, see [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm) and [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm).

### Viewing status of application reload schedules

The Scheduling column in the applications table displays the status of an application's tasks for scheduled reloads. An empty column means the application has no tasks. The statuses are:

- Scheduled: The application has at least one activated task.
- Schedule disabled: All tasks for the application are currently deactivated. For information about how tasks can be deactivated, see [*Reasons for task deactivation*](../Refresh/refresh-manage-tasks.htm#Reasons).

### Creating or editing reload schedules

To configure reload schedules, [tenant admins](#glossary-7 "Glossary term") and analytics admins with the appropriate space permissions for an application and its data content can create a new task or edit an existing one. The task can be configured to run on a time-based or event-based schedule.

Information noteEditing a task changes the owner of the task. See [*Ownership of tasks for scheduled reloads*](#Ownershi).

Do the following:

1. In the Administration activity center, go to Content > Applications.
2. Select Source or Published and locate the application for which you want to add or edit a task.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then select Schedule.
4. If you are adding a new task, click Create new task in the scheduling dialog. To edit an existing task, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the task and select Edit.
5. Configure the task with your desired scheduling settings.

   For detailed information on how to configure tasks for applications, see [*Reloading application data*](../Apps/reloading-apps-cloud-hub.htm).
6. Click Save.

#### Ownership of tasks for scheduled reloads

A task for data refreshes runs on behalf of the user who owns the task rather than the application owner. For the task to run successfully, the application owner must still have the correct access to the application and its data sources. Certain actions result in changes to who owns the task. The task owner is determined by the following rules:

- When you create a task to schedule refreshes of an application, you become the owner of that task.
- If another user edits or saves an existing task, they become the new owner of that task.
- If another user modifies the load script, they become the new owner of all tasks for refreshes of that application.
- Publishing or republishing an application to a managed space does not change the owner of any existing tasks within the published copy.
- Creating or modifying an application's [distribution list](#glossary-8 "Glossary term"), whether by uploading a source file in the Reporting section or by manually editing the load script, makes you the new owner of all tasks that have been created for scheduled reloads of that application.

### Deleting reload schedules

Tenant admins and analytics admins can delete existing tasks for scheduled reloads from the Administration activity center.

Do the following:

1. In the Administration activity center, go to Content > Applications.
2. Find the application that you want to delete a task from.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then select Schedule.
4. In the scheduling dialog, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the task, and select Delete.

## Deleting applications

As a tenant or analytics admin, you can delete applications.

Do the following:

1. In the Administration activity center, go to Content > Applications.
2. Select Source, Published, or Staged.
3. Select one or more applications and click Delete.
4. In the Delete apps dialog, select the checkbox to confirm the deletion, and then click Delete.

## Monitoring application performance and managing access control

Regular monitoring of application performance, growth, and access control is essential for a positive user experience, efficient resource use, and data security. This section covers key practices to ensure optimal application functionality.

### Monitoring and optimizing application performance

Regular performance assessments keep applications responsive and reliable. Consider these best practices:

- Evaluate performance metrics: Monitor metrics like load times and memory consumption to ensure fast application access and updates. For more information, see [*Application performance evaluation*](../Apps/app-performance-evaluation.htm).
- Optimize application size and data models: Simplify data models to enhance performance and reduce memory usage. Track memory consumption to prevent exceeding tenant quotas. For more information, see [*Optimizing application performance*](../Apps/app-performance.htm).
- Analyze application usage: Use tools like the Application Analyzer to track application adoption rates, reload times, and memory usage trends, helping you identify and resolve performance bottlenecks.

### Managing access control

Access control keeps sensitive data safe while allowing smooth collaboration. Implement the following strategies:

- Spaces for application access: Assign space roles to control user access. Share specific applications with non-space members as needed. For more information, see:

  - [*Working in spaces*](../Spaces/Spaces.htm)
  - [*Sharing applications with users who are not space members*](../Spaces/sharing-content-with-non-space-members.htm)
- Section Access for sensitive data: Restrict visibility of specific data within applications. For more information, see [*Managing data security with Section Access*](../Scripting/Security/manage-security-with-section-access.htm).

### Using monitoring applications

Use specialized applications to track performance and access across your environment:

#### Application analyzer

The App Analyzer monitoring application helps you monitor application performance and resource usage. Key features include:

- Tracking in-memory application size and memory consumption against tenant quotas.
- Analyzing reload times and maximum RAM usage.
- Monitoring user adoption rates and application interactions to identify underperforming applications.

For more information, see:

- [Qlik Community: The Application Analyzer for Qlik Cloud Customers](https://community.qlik.com/t5/Support-Updates/The-App-Analyzer-for-Qlik-Cloud-Customers/ba-p/1734927)
- [GitHub: Qlik Cloud Application Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer)

#### Access Evaluator

The Access Evaluator monitoring application provides insights into roles and access across the tenant. Key features include:

- Viewing user and group access to spaces and applications.
- Analyzing sharing access to applications.

For more information, see:

- [Qlik Community: Access Evaluator - Monitoring Application for Qlik Cloud](https://community.qlik.com/t5/Support-Updates/Access-Evaluator-Monitoring-App-for-Qlik-Cloud/ba-p/1954291)
- [GitHub: Qlik Cloud Access Evaluator](https://github.com/qlik-oss/qlik-cloud-access-evaluator)

#### Installing and updating monitoring applications

The App Analyzer and Access Evaluator applications are part of the Qlik Cloud Monitoring Applications. These community-supported tools can be easily installed and updated using the Qlik Cloud Monitoring Apps Installer with Qlik Automate.

Information noteAs community-supported tools, these applications are maintained by the community rather than Qlik.

For details on installation and support, see [*App Installers*](../../Sense_QlikAutomation/introduction/template-list.htm#App).
