---
title: "Publishing applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/publish-app-cloud-hub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Managing applications"]
---

# Publishing applications

You can publish applications from a [personal](#glossary-0 "Glossary term") or [shared space](#glossary-1 "Glossary term") to a [managed space](#glossary-2 "Glossary term"). Publishing creates a copy of the application in the managed space.

You must have the Owner or Can publish permission in the managed spaces to which you are publishing or republishing the application. If the application being published is in a shared space, you also need the Can edit space role or higher in that shared space in order to publish the application.

You can view the spaces that an application has been published to in Details.

Applications indicate when they were last published to a managed space in the publish dialog.

Information note

Tasks for scheduled reloads are not included for the published copy of an application. Published applications must have their tasks reconfigured on the version in the managed space.

Information note

Applications that have enabled Insight Advisor in the [hub](#glossary-4 "Glossary term") must be reloaded after being published to a managed space.

Information note

Once an on-demand selection application is published to a managed space, you cannot edit the navigation link in the selection application or published application. If you need to update the navigation link, delete the published application. Next, edit the link in the selection application, and publish the application again to the managed space.

For more information about publishing applications in a managed space, see [*Using applications in managed spaces*](../Spaces/managing-apps-in-managed-spaces.htm).

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

Variables can be created in a [managed space](#glossary-5 "Glossary term") application, and are later removed when the application is republished.

An application does not have to be in the same space to republish. For example, you may develop applications with separate developing and verification spaces, each with copies of the original application. Either space can republish their copy of the application to the managed space.

If another copy of the application has republished and replaced the application in the managed space, you will see the publishing dialog. If you change the name when publishing to match the name of the application in the managed space, you will republish that application.

Republishing an application does not affect any tasks for scheduled reloads that have been configured on the existing published copy of the application. These tasks are unchanged after republishing.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Manage > Publish to space.
2. If you want to publish a new version of the application, click Publish new.
3. If you want to replace existing published copies of the application, select the copies to replace.
4. To include data with the application, select Include data.
5. Click Republish.

## Application ownership when publishing applications

When an application is published to a managed space, the published copy of the application has the same owner as the source application.

## Publishing and ownership of scheduled tasks for data refreshes

Publishing or republishing an application to a managed space does not change the owner of any existing tasks within the published copy.
