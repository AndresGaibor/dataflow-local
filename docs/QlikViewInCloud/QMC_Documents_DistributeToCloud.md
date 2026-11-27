---
title: "Publishing QlikView documents and links in Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikViewInCloud/QMC_Documents_DistributeToCloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "QlikView applications in Qlik Cloud"]
---

# Publishing QlikView documents and links in Qlik Cloud

You can publish your QlikView documents, and links to documents, in Qlik Cloud. QlikView documents open directly in Qlik Cloud Analytics [activity centers](#glossary-0 "Glossary term"). Users do not need special permissions to open a published document. Links that are published in Qlik Cloud Analytics redirect the user to the QlikView Server installation. The user must be able to access the QlikView Server.

Information noteThis feature is not available in Qlik Sense Business.

To publish QlikView documents or links in Qlik Cloud Analytics activity centers, you must do the following tasks:

- Connect your QlikView Server deployment to an existing Qlik Cloud deployment.

[*Connecting QlikView Server to a Qlik Cloud deployment*](QMC_ConnectToCloudDeployment.htm)

- Create tasks to publish QlikView documents and links in the activity centers of the connected Qlik Cloud deployment.

[*Publishing a QlikView document in Qlik Cloud*](QMC_Documents_DistributeDocumentToCloud.htm)

[*Publishing a link to a QlikView document in Qlik Cloud*](QMC_Documents_DistributeLinkToCloud.htm)

- Optionally, migrate server bookmarks to QlikView documents in managed spaces in Qlik Cloud.

  [*Migrating bookmarks from QlikView to Qlik Cloud tenants*](QMC_migrate-bookmarks-qv-saas.htm)

## Choosing between publishing a document and a link

Publishing a QlikView document or a link to a document gives Qlik Cloud users a range of capabilities for interacting with QlikView content.

When you publish a QlikView document in Qlik Cloud Analytics, access and consumption of the document are handled in the Qlik Cloud environment.
Access is managed by the Qlik Cloud admin. Users can open sheets and make selections in objects but they cannot create new sheets or objects.

When you publish a link in Qlik Cloud, the document is handled by the QVS service in the QlikView Server environment.
When the user clicks the link, the document opens in the QlikView Server environment. Only users who have access to the QlikView Server can open a document from a published link. Access is managed by the QlikView admin.
