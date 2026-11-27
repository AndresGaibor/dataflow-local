---
title: "Administering Talend Management Console in Qlik Cloud - Qlik Talend Cloud subscriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/administer-tmc-from-qc.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud"]
---

# Administering Talend Management Console in Qlik Cloud - Qlik Talend Cloud subscriptions

In addition to the Unified Administration between Qlik and Talend, the Talend menu gives you access to the rest of Talend Management Console services directly from Qlik Cloud. This menu is available from the  [Qlik Talend Data Integration activity center](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/NewNavigation/new-navigation-talend-data-integration.htm).

This feature will be available progressively to all customers with the activation of the Unified Administration.

Information noteThis topic applies only to customers with a Qlik Talend Cloud subscription.

Under the Talend menu, you can see the following menu entries, depending on the assigned user permissions and roles.

## Operations

The Operations menu allows you to monitor operations like inspecting a single task or plan run or viewing past runs.

To see this menu, you require the Operator role distributed from Talend or a role with the Tasks and Plans - Edit (TMC\_OPERATOR) Talend Cloud permission assigned.

For more information, see [Monitoring operations](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/monitoring) (Talend Help)

## Management

The Management menu allows you to create and manage Talend assets like artifacts, tasks, plans, Studio connections and resources.

To see this menu, you require the Operator or Assets Manager roles from Talend or a role with the Tasks and Plans - Edit (TMC\_OPERATOR) or Studio connections and Studio resources - Edit (TMC\_CONNECTION\_RESOURCE\_EDIT) Talend Cloud permissions assigned.

For more information on how to:

- Manage artifacts, see [Managing artifacts](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/tmc-artifacts) (Talend Help)
- Manage Job tasks, see [Managing Jobs](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/tmc-managing-jobs) (Talend Help)
- Manage plans, see [Managing plans](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/managing-plans) (Talend Help)
- Manage Pipeline Designer tasks, see [Managing Pipeline Designer tasks](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/managing-pipelines) (Talend Help)
- Manage Route and Data Service tasks, see [Managing Routes and Data Services](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/managing-routes-and-data-services) (Talend Help)
- Manage Studio connections and resources, see [Managing Studio connections](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/tmc-connections) and [Managing Studio resources](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/tmc-resources) (Talend Help)

## Processing

The Processing menu allows you to create and manage the execution engines like Cloud Engines and run profiles.

To see this menu, you require the Infrastructure Administrator role from Talend or a role with the Engines - Manage (TMC\_CLUSTER\_MANAGEMENT) or Run Profiles - Manage (TMC\_RUN\_PROFILE\_MANAGEMENT) Talend Cloud permissions assigned.

For more information about the Processing menu, see [Managing Talend Studio connections](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/tmc-connections) and [Execution engines](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/tmc-engines) (Talend Help).

## Promotions

The Promotions menu allows you to manage your Software Development Life Cycle when working with several environments, spaces, and artifacts.

To see this menu, you require the Environment Administrator role distributed from Talend or a role with the Promotion - Start (TMC\_PROMOTION\_EXECUTION) or Promotion - Manage (TMC\_PIPELINE\_MANAGEMENT) Talend Cloud permissions assigned.

For more information on how to manage promotions, see [Managing promotions](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/manage-promotion) (Talend Help).

## Studio projects

The Studio Projects menu allows you to create and manage Talend Studio projects and configurations.

To see this menu, you require the Project Administrator role distributed from Talend or a role with the Studio projects - Manage (TMC\_PROJECT\_MANAGEMENT) Talend Cloud permission assigned.

For more information on how to manage Studio projects and configurations, see [Managing Studio projects](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/tmc-proj-man) and [Managing Studio configurations](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/managing-studio-configurations) (Talend Help).

## Who can access Talend menu

You can see the Talend menu entries depending on the assigned user permissions and roles.

Synchronized Talend roles appear as custom roles in the Administration activity center and are labeled as role distributed from Talend.

Talend permissions are grouped under the Talend Cloud permissions section in the custom roles settings. You can add these permissions to any custom role in Qlik Cloud.

For more information, see [*Synchronizing roles and permissions*](synchronized-resources-roles.htm).

|  |  |  |
| --- | --- | --- |
| Menu entry | Talend Cloud permissions in Qlik Cloud | Permissions in Talend Cloud |
| Operations | Tasks & Plans - Edit (tmc-operator:full) | Tasks and Plans - Edit (TMC\_OPERATOR) |
| Management | Tasks & Plans - Edit (tmc-operator:full)  or  Connections and resources - Edit (tmc-connection-resource:update) | Tasks and Plans - Edit (TMC\_OPERATOR)  or  Studio connections and Studio resources - Edit (TMC\_CONNECTION\_RESOURCE\_EDIT) |
| Processing | Engines - Manage (tmc-cluster:manage)  or  Run Profiles - Manage) (tmc-run-profile:manage) | Engines - Manage (TMC\_CLUSTER\_MANAGEMENT)  or  Run Profiles - Manage) (TMC\_RUN\_PROFILE\_MANAGEMENT) |
| Promotions | Promotion - Start (tmc-promotion:execute)  or  Promotion - Manage ( tmc-pipeline:manage) | Promotion - Start (TMC\_PROMOTION\_EXECUTION)  or  Promotion - Manage (TMC\_PIPELINE\_MANAGEMENT) |
| Studio projects | Projects - Manage (tmc-project:manage) | Studio projects - Manage (TMC\_PROJECT\_MANAGEMENT) |

## Limitations

If you add users to a group with Talend Cloud permissions assigned in Qlik Cloud, they can see the Talend menu in Qlik Cloud. However, they cannot access Talend Management Console in Talend Cloud if Talend Cloud permissions are not assigned directly to these users. For more information, see [What is not synchronized](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/synchronized-resources.htm#anchor-2) or [Synchronization behavior](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/synchronized-resources-roles.htm#anchor-1).
