---
title: "Working with applications distributed from Qlik Sense Enterprise on Windows"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Applications/working-with-apps-qseow.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with applications in Qlik Answers"]
---

# Working with applications distributed from Qlik Sense Enterprise on Windows

Qlik Answers supports applications distributed to Qlik Cloud from Qlik Sense Enterprise on Windows. To make a distributed application available to Qlik Answers, you must enable business logic for the application and make it available to search in Qlik Sense Enterprise on Windows before you distribute it to Qlik Cloud. Once it is distributed, a tenant administrator can move the application to a managed space, where it will be indexed.

Information noteIf you want to use Qlik Answers with an application already distributed to Qlik Cloud before support was added, you must prepare it using these steps in Qlik Sense Enterprise on Windows and redistribute it.

## Preparing and distributing the application

Do the following:

1. In Qlik Sense Enterprise on Windows, make the application available for search by doing one of the following. The application owner or any user with edit access can do this.

   - Make the application available to Insight Advisor Chat:

     For more information, see [*Making applications available in Insight Advisor Chat*](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/Insights/insight-advisor-available-chat.htm).
   - Add the variable crossAppsSearchEnabled with a definition of 1:

     For more information, see [*Creating a variable*](../../Variables/create-variable-using-dialog.htm).

     Verify that the setting is enabled.
2. Activate business logic for the application:

   For more information, see [Enabling custom business logic](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business-logic-logical-models.htm#anchor-3).
3. Publish the application to a distribution stream and distribute the application to Qlik Cloud.

## Moving the staged application to a managed space

Once the application is distributed to Qlik Cloud, a tenant administrator can move the distributed appl

1. In Qlik Cloud, in the Administration activity center, open Content.
2. Select Staged from the dropdown list.
3. Assign the distributed application to the appropriate managed space.

After the application is moved from staged to a managed space, it is automatically indexed for Qlik Answers. Confirm that Qlik Answers is activated for the application.
