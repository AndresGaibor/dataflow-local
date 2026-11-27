---
title: "In-application reporting with exported or migrated applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Generate/cloud-in-app-reports-exported-migrated.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Configuring report generation"]
---

# In-application reporting with exported or migrated applications

In-application reporting is available for applications that have been exported and uploaded into Qlik Cloud Analytics.

After uploading an exported or migrated application, you need to add the required data sources to the space, update the application's load script as needed, and build the remaining reporting assets in the application.

There are a number of scenarios in which you might need to work with exported applications:

- Applications that are migrated (exported) from Client-Managed Qlik Sense or Qlik Sense Desktop to Qlik Cloud.
- Applications that are exported from Qlik Cloud and re-uploaded into the same or a different Qlik Cloud environment.

The following sections outline the required processes for working with exported and migrated applications.

## Exported applications from Qlik Cloud

When a Qlik Sense application is exported from Qlik Cloud, it can re-uploaded into the same or another Qlik Cloud environment. This is common, for example, when sharing applications with other users. You can use in-application reporting with these applications.

Some of the reporting assets will need to be recreated in an uploaded application. The following table outlines what you will need to recreate.

Which reporting assets are preserved when I export and re-upload an application into Qlik Cloud?

| Application export option | Report tasks | Report filters | Recipients | Groups | Templates |
| --- | --- | --- | --- | --- | --- |
| With data | Not preserved | Preserved | Preserved | Preserved | Not preserved |
| Without data | Not preserved | Preserved | Preserved if compatible data sources exist in space  Information noteThe application also needs to be reloaded. | Preserved if compatible data sources exist in space  Information noteThe application also needs to be reloaded. | Not preserved |

## Applications migrated or exported from Client-Managed Qlik Sense or Qlik Sense Desktop

You can use in-application reporting with applications that were created with Client-Managed Qlik Sense or Qlik Sense Desktop.

Here is a general workflow for using in-application reporting with applications from Client-Managed Qlik Sense and Qlik Sense Desktop:

1. If you are manually migrating the application, export the application from the environment in which it is located, and then upload it into a [personal](#glossary-1 "Glossary term") or [shared space](#glossary-2 "Glossary term") in Qlik Cloud.
2. Comprehensive tools are also available to facilitate the migration process for applications created in Client-Managed Qlik Sense. Applications migrated to Qlik Cloud using these tools can be used for in-application reporting. For more information about the process, see [Migrating from Client-Managed Qlik Sense](/en-US/migration/Content/Migration/moving-from-client-managed-qlik-sense-to-qlik-sense-saas.htm).
3. In the space where you uploaded the application, add the data sources used by the application.
4. Modify the load script in the newly uploaded application. The script needs to use syntax and functions that are compatible with Qlik Cloud.

   For example, the load script might reference a data source location named AttachedFiles. In Qlik Cloud, this location is instead named DataFiles, in addition to referencing the space location.
5. For Qlik Sense Client-Managed applications, you can migrate the following Qlik NPrinting template types for compatibility with Qlik Cloud reporting:

   - Excel
   - PixelPerfect
   - HTML

   For a full guide, see [Exporting report templates from Qlik NPrinting to Qlik Cloud](/en-US/migration/Content/Migration/NPrinting/exporting-nprinting-excel-to-qlik-cloud.htm).
6. If you are instead creating [report templates](#glossary-3 "Glossary term") from scratch, you can start creating the templates after the application has been uploaded into Qlik Cloud.
7. In the application, build the remaining reporting assets and add all required templates.

## Applications published or distributed from Client-Managed Qlik Sense

In-application reporting is not available for applications published or distributed from Client-Managed Qlik Sense (including multi-cloud deployments) to Qlik Cloud. To use in-application reporting with these applications, migrate the application using the [Qlik Analytics Migration Tool](/en-US/migration/Subsystems/AnalyticsMigrationTool/Content/Qlik-Analytics-Migration-Tool-Overview.htm), or manually export the application and re-upload it into Qlik Cloud.

To learn more about using in-application reporting with migrated and exported applications, refer to [*Applications migrated or exported from Client-Managed Qlik Sense or Qlik Sense Desktop*](#MigratedExportedApp).

## Learn more

- [*In-application reporting in managed spaces*](../InAppGeneral/cloud-in-app-reports-managed-space.htm)
