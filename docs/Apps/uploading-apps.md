---
title: "Uploading applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/uploading-apps.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Managing applications"]
---

# Uploading applications

You can upload an application you exported from another Qlik Cloud tenant or another Qlik Sense version.

You can upload applications going to the Create page of the Analytics [activity center](#glossary-1 "Glossary term") and selecting Upload. Select App and then add your application .qvf file to Upload.
You can upload multiple applications at once. Application properties such as custom attributes, are included when an application is uploaded.

After uploading the application, you need to add data sources to the uploaded application.

You can continue working on the application. If the application is ready, share the application with other users, or move the application to a [shared space](#glossary-2 "Glossary term").

Information note

You can upload applications exported from other Qlik Cloud tenants and Qlik Sense 3.1 or later.

You cannot upload On-Demand applications to Qlik Cloud.

Information note

The Qlik GeoAnalytics Connector is not supported in Qlik Cloud (including Qlik Cloud Government). If your uploaded application used the GeoAnalytics Connector, you can change your application [load script](#glossary-3 "Glossary term") to use Qlik Sense GeoOperations instead.

[Migrating from GeoAnalytics Connector to Qlik GeoOperations](/en-US/migration/Content/Migration/migrate-geo-analytics.htm)

Qlik Cloud Government noteQlik Cloud Government users cannot import applications exported from QlikView.

## Preparing applications from other versions of Qlik Sense for upload

While Qlik Cloud supports uploading applications from other versions of Qlik Sense, there are limitations:

- Upload size limits vary by subscription tier. See [*Qlik Cloud Analytics capacity limits*](../Introduction/qcs-specs-capacity.htm) for details.
- Uploaded applications include data already loaded into the application, but the data sources are removed. If you want to reload attached files and [data connections](#glossary-4 "Glossary term") you will need to re-add them. Ensure you have the information to add the connections to your application again.
- Uploaded applications do not include any community or private sheets. You need to approve all sheets and stories you want to keep as base sheets and stories before you export the application.

Related learning:

- [Getting Started with Qlik Cloud](/lnk/Getting_started_Qlik_Cloud)
- [How do I upload an application with a drag and drop?](/lnk/How_upload_app_drag_and_drop)
