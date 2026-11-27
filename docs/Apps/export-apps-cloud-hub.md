---
title: "Downloading applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/export-apps-cloud-hub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Managing applications"]
---

# Downloading applications

You can download applications from Qlik Cloud as .qvf files. These can be uploaded into other Qlik Cloud tenants or Qlik Sense versions.

Warning note

Tenant admins cannot download applications from other users' personal spaces, but they can take ownership of these applications and then download them.

Private applications that manage security with [section access](#glossary-0 "Glossary term") can be downloaded only by the application owner from their [personal space](#glossary-2 "Glossary term"). If a tenant admin has downloaded an application with section access from a shared space, and they are not the application owner, they will not be able to access the script upon upload to another Qlik Cloud tenant. The admin must duplicate the application to access [Data load editor](#glossary-3 "Glossary term") and create a new script.

Information note
To download an application that uses section access, you must be assigned at least one of the following permissions for shared spaces:

- Can edit
- Can manage

When you download an application, the following content is included:

- Public content (sheets, stories, bookmarks)
- Private content belonging to you
- The media library.
- Data loaded in the application.

The downloaded application is saved in the default download folder of your web browser.

You can download the application without any data. This only exports the sheets and stories of the application. If you have access to a Qlik Sense Enterprise deployment, you can import this into QMC and use it to replace the sheets and stories of an application without changing the data model. For more information, see [Importing applications](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Administer_QSEoW/Managing_QSEoW/import-apps.htm).

## Downloading applications with data

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application you want to export and select Download > Download.

## Exporting applications without data

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application you want to export and select Download > Download without data.
