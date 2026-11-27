---
title: "Synchronizing and managing environments"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-environments.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions"]
---

# Synchronizing and managing environments

Environments provide a structured way to manage spaces, configurations, settings, and resources across different stages of development and deployment. Environments and their assigned spaces are synchronized between Qlik Cloud and Talend Cloud.

Information noteThis topic applies only to customers with a Qlik Talend Cloud subscription.

## Overview of environments

Environments help manage resources throughout the software development life cycle, including development, testing, and production. They ensure smooth transitions while maintaining security, governance, and control over data resources. By using environments, you can:

- Keep development (DEV), testing (TEST), and production (PROD) separate.
- Organize data spaces effectively to simplify permission and access control.

## Synchronizing environments and spaces

Environments and spaces are synchronized between Qlik Cloud and Talend Cloud to help manage resources consistently across both systems. You can create and manage environments in the Qlik Cloud Administration activity center and in Talend Management Console. Changes such as creation, updates, deletions, and space assignments are synchronized between both systems.

### Mapping between Qlik Cloud and Talend Cloud

- Data spaces in Qlik Cloud appear as spaces in Talend Cloud.
- Spaces in Talend Cloud appear as data spaces in Qlik Cloud.

### Synchronization behavior

- New environments created in either system appear in both systems.
- Environments and their assigned spaces synchronize in both directions.
- Assigned users and permissions for each space are preserved during synchronization.
- Updates to data spaces (such as name, assigned users, or assigned roles) are synchronized.
- Deleting a data space or Talend space removes it from both systems.
- Only data spaces that are assigned to an environment are synchronized. Data spaces not assigned to an environment remain local to Qlik Cloud.

### Local-only resources

- Managed spaces and shared spaces remain local to Qlik Cloud.
- Content within data spaces and Talend spaces (such as files, applications, or datasets) is not synchronized.

For more information, see [*Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions*](synchronized-resources.htm).

## Permissions required to manage environments

To create and manage environments in Qlik Cloud, you need one of the following roles:

- Tenant Admin or Data Admin: Full access to create and manage environments and assign data spaces.
- Custom role with the Manage environments permission: Administrator-level access to manage environments and assign data spaces.

To manage environments in Talend Management Console, you need the Environments - Manage permission.

For more information, see:

- [*Managing custom roles*](permissions-custom-roles-capacity-model.htm)
- [Managing environments](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/managing-environments) (Talend Help)

## Creating environments

Do the following:

1. In the Administration activity center, go to Environments & spaces.
2. On the Environments tab, click Create new.
3. Enter a name for the environment.
4. Optionally, add a description.
5. Optionally, search for and assign one or more data spaces to the environment. (You can also assign spaces later.)
6. Click Create.

The environment appears in both the Administration activity center and in Talend Management Console.

## Assigning data spaces to environments

Do the following:

1. In the Administration activity center, go to Environments & spaces.
2. On the Environments tab, locate the environment.
3. Click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) to view the list of assigned spaces.
4. Click Assign.
5. In the Assign spaces dialog, search for and select the spaces to add.
6. Click Assign.

### Assignment notes and tips

- Each data space can belong to only one environment. You can reassign a data space to a different environment or set it to None. However, spaces restricted by services—for example, those used in Talend promotion—can't be reassigned to avoid disrupting dependent processes.
- Data space names need to be unique within their environment. If the same name exists in multiple environments, the environment name is shown alongside the space name in Catalog and space lists.
- You can also assign an environment when creating a data space from the Spaces tab on the Environments & spaces page.

For more information about data spaces, see [*Working in spaces in Data Integration*](../DataIntegration/DataSpaces/working-spaces.htm).

## Editing environments

Do the following:

1. In the Administration activity center, go to Environments & spaces.
2. On the Environments tab, locate the environment.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit.
4. Modify the name and description as needed.
5. Click Save.

## Deleting environments

You can delete an environment only if no spaces are assigned to it.

Do the following:

1. In the Administration activity center, go to Environments & spaces.
2. On the Environments tab, locate the environment
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Delete.
4. Confirm the deletion.

## Limits and considerations

- You can create up to 1,000 environments per tenant.
- Only data spaces (not managed or shared spaces) can be assigned to an environment.
- Each environment can have up to 1,000 data spaces assigned.
- Each data space can belong to only one environment.
- There can be up to 10,000 spaces in total, across all space types.
- Environments created in Talend Management Console appear with empty values in the Created by and Updated by columns on the Environments tab in the Administration activity center. This is expected behavior in the current release.
