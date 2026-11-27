---
title: "Troubleshooting - Working in spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Troubleshooting/troubleshooting-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces"]
---

# Troubleshooting - Working in spaces

This page suggests solutions to common issues you might encounter when working in shared and managed spaces.

## A load script needs to be updated, but the application owner is unavailable

In a collaborative setting, there might be times when a data load script needs to be updated but the application owner is not available.

Space managers (users with the Owner or Can manage role in the space) can assign permissions to an eligible user to manage the load script.

Try one of the following:

- Assign the Can edit data in applications role to specific users in the shared space. These users will be able to edit the load script or manage the data.
- Duplicate the application. When you duplicate an application, you become the owner of the new copy.

For both of the above solutions, users need access to the data sources used in the application or script to be able to reload it. If they do not have access, contact a tenant administrator move or change ownership of any required data sources, or provide the required space permission to access the data sources. New credentials need to be entered when editing a connection.

For more information, see [*Managing data connections for administrators*](../Admin/mc-administer-data-connections.htm).

## The source application for a published application was deleted

If the source application for an application in a managed space is deleted, the published copy of the application cannot be updated and republished as needed.

You need to re-establish the parent-child relationship between a source application and the published application. You can do this by saving a backup copy of the published application, then re-publishing this backup copy from a personal or shared space.

Do the following:

1. Export the published copy of the application without data.

   [*Exporting applications from managed spaces*](../Spaces/managing-apps-in-managed-spaces.htm#ExportingAppsFromManagedSpaces)
2. Re-upload the application to a personal or shared space.
3. Publish the application back to the same managed space, with the same name as the existing published application.

   When prompted, select Replace to replace the existing published copy of the application.

## I made changes to the roles of space members, but their access has not changed

When you make any changes to user's permissions for applications or scripts, these changes are not instantly reflected in actively opened applications and scripts. To ensure that the changes to the user's permissions are updated, the user must close all browser tabs belonging to the affected application or script and wait at least two minutes (application session's Time To Live), then re-open the application. This applies to application and script permissions in personal, shared, and managed spaces. Changes in permissions for newly opened applications are reflected instantly.

## The owner of a space, application, or other entity has left the tenant

When a user is deleted from Qlik Cloud, such as when a user leaves an organization, assets they own will no longer have an owner. This can cause application and script reloads to fail, and cause other access issues.

A [tenant administrator](#glossary-0 "Glossary term") can reassign ownership of spaces, applications, scripts, and data connections. As a side note, analytics administrators and [data administrators](#glossary-1 "Glossary term") can perform similar management tasks in shared and managed spaces, and [data spaces](#glossary-2 "Glossary term"), respectively.

Contact your tenant administrator to inquire about reassigning ownership of assets, and moving them to other spaces as needed.

For more information, see:

- [*Managing applications for tenant and analytics administrators*](../Admin/mc-administer-apps.htm)
- [*Managing scripts for tenant and analytics administrators*](../Admin/mc-administer-scripts.htm)
- [*Managing data connections for administrators*](../Admin/mc-administer-data-connections.htm)
- One of the following, depending on the type of Qlik Cloud subscription:

  - [*Adding users to Qlik Cloud*](../Admin/SaaS-invite-users-capacity-model.htm) (Capacity-based subscriptions)
  - [*Adding users to Qlik Cloud*](../Admin/SaaS-invite-users.htm) (User-based subscriptions)
  - [*Adding users to a Qlik Anonymous Access tenant*](../Admin/SaaS-invite-users-anonymous.htm) (Qlik Anonymous Access subscriptions)

## Backing up content added to published applications in managed spaces

After an application is published to a managed space, space members can create new sheets and visualizations in the published copy.

If a published application is deleted, the content that has been added to it since it was published cannot be recovered.

As a preventative measure, it is recommended to frequently create backup copies of the published application. From the Analytics [activity center](#glossary-3 "Glossary term"), use the Download without data option. Another best practice is to periodically copy important Community sheets from the published application, and paste them into the source application. The sheets can be made public before republishing to add them as base content in the application.

If the application is ever deleted, it can be republished from the source application, or the backup copy can be uploaded to the development space then published back to the managed space.

For more information, see [*Exporting applications from managed spaces*](../Spaces/managing-apps-in-managed-spaces.htm#ExportingAppsFromManagedSpaces).

## I built an application using a data source in another space, but I have lost access to that space

When working in a shared space, you can build analytics content in a shared space using data sources from other spaces. If you lose access to any of the spaces containing the data sources, you might encounter reload failures and access issues.

As a first step, confirm that you have indeed lost access to the spaces in which the sources are located. If this is the case, you can:

- If the access issues are caused by the space owner leaving the tenant (deleted as a user), contact a tenant administrator to reassign ownership and move the data sources as needed. User credentials will be required to edit data connections.
- Consider recreating any data connections yourself.

## I have space permissions, but I still cannot work with certain content

For certain content — for example, ML resources and business glossaries — you need to be assigned certain permissions by a tenant administrator. These administrator-assigned permissions are prerequisites for working in spaces.

For full Qlik Predict access, you need the Automl Experiment Contributor and Automl Deployment Contributor roles, and often a combination of permissions assigned in the default permissions and custom roles.

For most business glossary actions, you need the Steward built-in security role.
