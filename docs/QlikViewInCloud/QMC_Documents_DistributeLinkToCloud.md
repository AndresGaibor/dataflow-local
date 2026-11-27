---
title: "Publishing a link to a QlikView document in Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikViewInCloud/QMC_Documents_DistributeLinkToCloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "QlikView applications in Qlik Cloud", "Publishing QlikView documents and links in Qlik Cloud"]
---

# Publishing a link to a QlikView document in Qlik Cloud

You can publish links to QlikView documents in Qlik Cloud. Users access the link from Qlik Cloud and open the document in a QlikView Server environment.

To publish a link to a QlikView document in Qlik Cloud, you first need to connect your QlikView Server to a Qlik Cloud tenant. You publish the link by creating a task in the QlikView Management Console. Once it is published in Qlik Cloud, the link is accessible from Qlik Cloud. The QlikView document is opened in QlikView Server.

Information noteThis feature is not available in Qlik Sense Business.

Information noteWhen distributing links to a cloud deployment, ensure that the HTTPS protocol is used and that the Fully Qualified Domain Name (FQDN) is included in the link URL. For detailed instructions on setting up HTTPS, see [How To Setup HTTPS / SSL with QlikView AccessPoint (WebServer and IIS)](https://community.qlik.com/t5/Official-Support-Articles/How-To-Setup-HTTPS-SSL-with-QlikView-AccessPoint-WebServer-and/ta-p/1710263).

## Creating a task to publish a link to QlikView document

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
5. Configure the link distribution.
   1. Navigate to the Distribute tab, then open the [*Manually*](/en-US/qlikview/September2026/Subsystems/QMC/Content/QV_QMC/QMC_Documents_SourceDocuments_Distribute_Manually.htm) section.
   2. In the Distribute to QlikView Server section, select ![Plus icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_gen_Plus.png)Add recipients button.
   3. From the drop-down menu that is now visible, select a server and a user type.
   4. In the Distribute to Cloud Native section, select Distribute link to enable the distribution of the link to Qlik Cloud.
   5. In the Cloud Deployment drop-down menu select the Qlik Cloud deployment you want to distribute the link to.

   Information noteYou can select only one cloud deployment. To distribute to multiple cloud deployments, create a separate distribution task for each cloud deployment.
6. Add one or more tags to the deployment. Adding tags is optional. Tags are visible in your [activity center](#glossary-0 "Glossary term") with your QlikView document link and they are used to filter content in Qlik Cloud.
7. Select Apply to create the task. Tasks are listed in the Status tab, in the Task section.
8. Right-click the task and select Run to distribute the document link to Qlik Cloud.

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
