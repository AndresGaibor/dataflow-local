---
title: "Using applications in managed spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-apps-in-managed-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in managed spaces"]
---

# Using applications in managed spaces

Managed spaces share secure applications with a limited group of viewers. Applications are published to [managed spaces](#glossary-0 "Glossary term") from [personal](#glossary-1 "Glossary term") or [shared spaces](#glossary-2 "Glossary term").

Information noteManaged spaces are not available in Qlik Cloud Analytics Starter or Qlik Sense Business.

Applications published to managed spaces maintain a parent-child relationship with the original application. Updates to the parent application can be republished to child applications. Parent applications can be moved between spaces without breaking the relationship. If the parent application is deleted, the application in the managed space will become an orphan and cannot be republished.

Managed space members are limited in how they can add content or change the data model of an application.
For an explanation of managed space permissions, see [*Data sources for applications in managed spaces*](app-data-managed-spaces.htm).

## Limitations

Managed spaces have the following limitations:

- You cannot publish on-demand template applications to a managed space.
- You cannot change the data model of a published application in a managed space.
- Applications in managed spaces can be exported without data only.
- You cannot move an application published in a managed space via the user [activity centers](#glossary-4 "Glossary term"). Administrators can move published applications between spaces in the Administration activity center. See [*Changing space of applications*](../Admin/mc-administer-apps.htm#ChangeSpace).
- You can only use master items when you duplicate a [sheet](#glossary-5 "Glossary term") in an application that is published in a managed space. Fields are not available in the assets panel.
- Once you have created a [data connection](#glossary-6 "Glossary term") in a managed space, the connection cannot be moved to another space without administrator assistance. To move the connection to another space, contact an administrator or recreate the connection in the desired space using the same settings.

  For documentation about how an administrator can move a connection, see [*Managing data connections for administrators*](../Admin/mc-administer-data-connections.htm).

## Publishing applications to managed spaces

A user with the Owner or Can publish space role in a managed space can publish applications to that managed space. If the application being published is in a shared space, you also need the Can edit space role or higher in that shared space in order to publish the application. Publishing an application into a managed space creates a copy of that application in the managed space. The same application can be published to multiple managed spaces.

Applications indicate when they were last published to a managed space in the publish dialog.

Information note

Tasks for scheduled reloads are not included for the published copy of an application. Published applications must have their tasks reconfigured on the version in the managed space.

Information noteApplications that are enabled for Insight Advisor Chat must be reloaded after being published to a managed space.

Information note

All sheets, bookmarks, and stories that are public when an application is published from a shared space to a managed space cannot be unpublished in the copy of the application that exists in the managed space.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Manage > Publish to space.
2. Select a managed space.
3. Optionally, change the Published app name, Description, and Tags of the application.
4. Click Publish.

## Republishing applications

Applications in managed spaces are updated by republishing the source application. When you republish an application, you can either publish a new version of the application or replace existing copies of the application in managed spaces.

Information note

Publishing an application to a managed space that shares a name with an application in a managed space is treated as replacing the application.

For example, you may upload an application that is an older version of an application in a shared space that has previously been published and has the same application name. If you published that application to the same managed space, you would be presented with replacing options rather than publishing options.

If you do not want to replace the application in this way, change the name of the application and publish again or click Publish new.

Information note

Variables can be created in a [managed space](#glossary-7 "Glossary term") application, and are later removed when the application is republished.

An application does not have to be in the same space to republish. For example, you may develop applications with separate developing and verification spaces, each with copies of the original application. Either space can republish their copy of the application to the managed space.

If another copy of the application has republished and replaced the application in the managed space, you will see the publishing dialog. If you change the name when publishing to match the name of the application in the managed space, you will republish that application.

Republishing an application does not affect any tasks for scheduled reloads that have been configured on the existing published copy of the application. These tasks are unchanged after republishing.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Manage > Publish to space.
2. If you want to publish a new version of the application, click Publish new.
3. If you want to replace existing published copies of the application, select the copies to replace.
4. To include data with the application, select Include data.
5. Click Republish.

## Reloading applications in managed spaces

Space owners and users with Can manage permission can manually refresh applications and create tasks for scheduled reloads of applications in the space.

## Exporting applications from managed spaces

You can export an application in a managed space without data. This allows users who might not have access to the source application to create backup copies of the application. This is useful when the source application is deleted or otherwise lost (for example, due to a permissions issue).

To download an application from a managed space, you need the Owner or Can manage role in the space. Tenant administrators cannot download applications from a managed space unless they also have the required space roles.

After an application is download from a managed space, it can be re-uploaded into a shared or personal space and published back to the managed space.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Download > Download without data.

## Publishing content to Community in the application

After the application is published, new sheets, bookmarks, and stories can be added to it, and shared with other space members. For more information, see [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm).

## Deleting applications in managed spaces

Deleting an application in a managed space removes the application from the space. A deleted application cannot be republished. A user with Can publish permission must publish the application to the managed space again.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Delete.
