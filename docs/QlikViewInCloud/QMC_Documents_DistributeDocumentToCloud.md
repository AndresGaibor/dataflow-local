---
title: "Publishing a QlikView document in Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikViewInCloud/QMC_Documents_DistributeDocumentToCloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "QlikView applications in Qlik Cloud", "Publishing QlikView documents and links in Qlik Cloud"]
---

# Publishing a QlikView document in Qlik Cloud

You can publish QlikView documents in Qlik Cloud. Published QlikView documents are then available directly from Qlik Cloud.

To publish a QlikView document in Qlik Cloud, you first need to connect your QlikView Server to a Qlik Cloud tenant. You publish the document by creating a task in the QlikView Management Console. Once it is published in Qlik Cloud, access and consumption of the QlikView document is fully handled in the cloud environment. Server bookmarks are not included in published applications and must be migrated after publishing. For more information, see [*Migrating bookmarks from QlikView to Qlik Cloud tenants*](QMC_migrate-bookmarks-qv-saas.htm).

Information noteThis feature is not available in Qlik Sense Business.

## Creating a task to publish a QlikView document

You can use the same task to distribute both a QlikView document and its link. The same settings will apply to both distributions. For optimal performance however, and if you want to apply dedicated settings when distributing a QlikView document or its link to Qlik Cloud, you should use separate tasks to publish QlikView links and documents.

Tip note

Before you create the distribution task, make sure you connect your QlikView Server to your Qlik Cloud deployment.

[*Connecting QlikView Server to a Qlik Cloud deployment*](QMC_ConnectToCloudDeployment.htm)

Do the following:

1. In the QlikView Management Console, go to Documents tab, then open the Source Documents section.

   Information noteYou can only publish documents from any of the source documents folders listed under Distribution Services. The default path is C:\ProgramData\QlikTech\SourceDocuments.
2. Select the source document you want to publish to Qlik Cloud.
3. Select the ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_gen_Plus.png) Add button to create a new document task. Select the ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_gen_Edit.png) Edit Task button to edit an existing task.
4. Tip note For more information about tasks, see [*Source Documents*](/en-US/qlikview/September2026/Subsystems/QMC/Content/QV_QMC/QMC_Documents_SourceDocuments.htm).
5. Configure the document distribution.
   1. Go to the Distribute tab, then open the [*Manually*](/en-US/qlikview/September2026/Subsystems/QMC/Content/QV_QMC/QMC_Documents_SourceDocuments_Distribute_Manually.htm) section.
   2. Go to the Distribute to Cloud Native section.
   3. Select Distribute document. This enables the distribution of the document to Qlik Cloud.
   4. From drop-down menu in the Deployment section, select the Qlik Cloud tenant you want to publish the document to.

   Information noteYou can select only one cloud deployment. To distribute to multiple cloud deployments, create a separate distribution task for each cloud deployment.
6. Add one or more tags to the deployment. Adding tags is optional. Tags are visible in [activity centers](#glossary-0 "Glossary term") with your QlikView document and they are used to filter content in Qlik Cloud.
7. Select Apply to create the task. Tasks are listed in the Status tab, in the Task section.
8. Right-click the task and select Run to distribute the document to Qlik Cloud.

Information noteThe document is distributed to Qlik Cloud as a staged application. For more information on staged applications, see [Managing applications](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-apps.htm).

## Security considerations

When you publish a QlikView document or a link to a QlikView document, they are not published with any existing security rules. It is up to the Qlik Cloud admin to add the published QlikView document to a managed space. Managed spaces are used for providing governed access to applications with strict access control both for the application and the application data. In a managed space, only the space owner and target application consumers can open the applications. No other users can open the applications in the managed space unless they have been given permission. For more information on managed spaces, see [Working in managed spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-managed-spaces.htm).

## Troubleshooting

If your task fails, use the QlikView Server logs to help determine the problem. This section lists possible solutions to tasks that fail.

Possible cause

You do not have access to the document source data and the default data reload causes the task to fail.

When you create a new task, data reload is enabled by default. This means the task attempts to reload the data before publishing the document or link. If you do not have access to the source data, for example you copied the QlikView document file into your source documents folder, the task will fail.

Proposed action

Disable the data reload in the task configuration.

Do the following:

1. In the QlikView Management Console, go to Documents, then open the Source Documentation section.
2. Select the task that is failing.
3. In the task configuration menu that opens, open the Reload tab.
4. Under Perform Reload section, deselect Enable.
5. At the bottom, click Apply.
6. Run the task again.
