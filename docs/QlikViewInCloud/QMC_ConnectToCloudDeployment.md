---
title: "Connecting QlikView Server to a Qlik Cloud deployment"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikViewInCloud/QMC_ConnectToCloudDeployment.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "QlikView applications in Qlik Cloud", "Publishing QlikView documents and links in Qlik Cloud"]
---

# Connecting QlikView Server to a Qlik Cloud deployment

Before you can publish QlikView documents or links, you must first connect your QlikView Server installation to a Qlik Cloud deployment.

## Prerequisites

To publish QlikView documents or a links to a QlikView document, you must have:

- A supported version of QlikView Server.
- A valid Publisher license.
- A configured Qlik Cloud cloud installation.

Information noteTo access QlikView documents from a published link in an [activity center](#glossary-0 "Glossary term"), the user will need to be able to access the QlikView server the link was distributed from.

## Connecting QlikView Server to a Qlik Cloud deployment

Do the following:

1. In the QlikView Management Console, go to the System tab, open the Setup section, then select the Cloud Deployments folder.
2. Select the ![Plus icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_gen_Plus.png) Add button to create a new cloud deployment connection.
3. In the Service URL field, enter the first part of the cloud tenant URL, for example <tenant\_name>.<region>.qlikcloud.com/.
   Select Apply to create the connection. Under Cloud Deployments you will see connection you just created.
4. Select the connection, then select the General tab.

   1. In the Deployment name field, enter a name for the cloud deployment.
   2. In the API endpoint field, enter the URL to the Qlik Cloud deployment that you want to publish to.
   3. Select a web server from the Web Server drop-down menu.
   4. Under Distribution Settings, you can disable the distribution of links, documents, or both.
5. In the Issuer configuration section, click Generate configuration to generate the local bearer token.

   - To connect to a Qlik Cloud deployment, select Qlik Cloud format.
6. Copy and save the local bearer token to a preferred location. You will need to add it to the Qlik Cloud deployment to complete the connection with your QlikView Server deployment.
   [*Adding the bearer token to Qlik Cloud Analytics*](#Adding)
7. Select Apply to confirm the configuration.

## Adding the bearer token to Qlik Cloud Analytics

To create a secure connection between your QlikView Server and Qlik Cloud Analytics, the QlikView Distribution Service (QDS) generates a bearer token that you add to your Qlik Cloud deployment.
The bearer token has a signed key that is used in all API calls between the Qlik Cloud tenant and the QlikView Server.

### For Qlik Cloud

To add your bearer token on Qlik Cloud:

1. In the Administration activity center, go to Identity provider, then Create new.
2. From the drop-down menu, select Multi-cloud.
3. Add a description for this identity provider.
4. In the Local bearer token section, paste the bearer token that you generated in the QlikView Management Console.
5. Click Create to complete the identity provider setup.

Information noteIf you are setting up your Qlik Cloud tenant for the first time, see [Setup with a local bearer token](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Administer_QSEoW/Managing_QSEoW/deployment-cloud-distribution.htm).

Once the connection between the QlikView Server and Qlik Cloud is complete, you can create tasks to distribute QlikView documents or links to the connected cloud deployments.

[*Publishing a QlikView document in Qlik Cloud*](QMC_Documents_DistributeDocumentToCloud.htm)

[*Publishing a link to a QlikView document in Qlik Cloud*](QMC_Documents_DistributeLinkToCloud.htm)
