---
title: "Adding and managing your analytics data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-data-resources-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data"]
---

# Adding and managing your analytics data

Add data files and connections from your data sources to your spaces in Qlik Cloud Analytics.
You or other users can then use them to add data in applications and scripts.

Applications and scripts require sources of data. Qlik Cloud Analytics supports the following types of data sources:

- [Datasets](#glossary-0 "Glossary term"): You can upload data files to Qlik Sense, which are stored in Qlik Cloud. Qlik Sense automatically adds an additional layer of metadata to uploaded data files, creating datasets. You can also create datasets for tables from existing data connections.

  The metadata added to a dataset enables you to use additional Qlik Sense tools for managing your data in the catalog, including catalog tools and other resources.
  For more information on cataloging, see [*Understanding your data with catalog tools*](../Catalog/catalog-overview.htm).

  Qlik Sense supports the following file types:

  - Text files: Data in fields must be separated by delimiters such as commas, tabs, or semicolons. For example: comma-separated variable (CSV) files.
  - HTML tables
  - Excel files

    Information noteYou cannot load data from password-protected Excel files, or Excel Binary Workbook files (.xlsb).

    For more information, see [*Loading data from Microsoft Excel spreadsheets*](../DataSource/load-data-from-Excel.htm).
  - XML files
  - Qlik native QVD and QVX files

    For more information, see [*Working with QVD files*](../Scripting/work-with-QVD-files.htm).
  - Apache Parquet files

    For more information, see [*Working with Apache Parquet files*](../Scripting/work-with-parquet-files.htm).
  - JSON files

    For more information, see [*Working with JSON files*](../Scripting/working-with-JSON.htm).
  - Fixed record length files
  - Data Interchange Format (DIF) files: DIF files can only be loaded with the data load editor.
  - Geographic data files:

    - GEOJSON
    - ESRIJSON
    - GML
    - KML
    - SHPZIP
    - DXF

    Information note

    The following file types must be loaded using a GeoOperations connection:

    - GEOJSON
    - ESRIJSON
    - GML
    - SHPZIP
    - DXF

    For more information, see [*Qlik GeoOperations analytics sources*](../../Global_Common/GeoOperationsFunctions/GeoOperations.htm).
  - QlikView script files (QVS)

  For a summary of where in Qlik Cloud you can add different file types as datasets, see [*Dataset support in Qlik Cloud*](../LoadData/import-support-Qlik-Cloud.htm).

  Data files can be up to 100 GB. However, when uploading very large data files (over 6 GB), you might experience constraints with engine capacity. These constraints are more likely to be encountered with QVD data files due to the memory usage necessary to load QVD files into the engine. For more information about increasing the capacity available, see [*Large application support*](../Admin/large-app-support.htm).
- [Data connections](#glossary-1 "Glossary term"): Connections allow you to bring data from external data sources, such as databases or remotely stored files, into applications. You can create datasets from connections. For more on supported data sources, see [Data sources in Qlik Cloud Analytics](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Helpsites/Connectors_SaaS.htm).
- Data products: You can browse the data marketplace for a data product to use in a new application. Data products are a grouping of multiple datasets, which means you can load a whole set of data related to a common domain in one operation. For more information, see [*Working with data products*](../DataIntegration/DataProducts/Data-products.htm).

Add datasets and data sources in Create by selecting Dataset, and then selecting Dataset or Connect to data.
Once added, they can be managed from Data sources in their space. For more information, see [*Adding and managing your analytics data*](#Managing).

Datasets and connections can be used in applications with [Data manager](#glossary-2 "Glossary term"), [Data load editor](#glossary-3 "Glossary term"), or the [data catalog](#glossary-4 "Glossary term"). Datasets and connections to data sources can also be added inside an application with Data manager or Data load editor. For information on working with datasets and connections with Data manager, Data load editor, or the data catalog, see:

- [*Loading data from the data catalog*](../LoadData/adding-data-catalog.htm)
- [*Loading and managing data with Data Manager*](../LoadData/managing-data.htm)
- [*Loading and transforming data with scripting*](../Scripting/introduction-data-modeling.htm)
- [*Loading data from the data marketplace*](../DataIntegration/Marketplace/loading-data-from-marketplace.htm)

Datasets and connections can be used in scripts with Script. Datasets and connections to data sources can also be added inside a script in Editor. For more information on working with scripts, see [*Working with scripts in the catalog*](../ScriptEditor/using-the-script-editor.htm).

Datasets and connections to data sources can also be added in Data manager and Data load editor while you are working on an application. For more information, see:

- [*Adding data to the application from connections and new files*](../LoadData/adding-data.htm)
- [*Using Data load editor*](../LoadData/use-data-load-editor.htm)

## Data and spaces

When you add datasets and connections, you must select a destination space. Spaces are private, such as your personal space, or they are communal spaces with other users, such as shared or managed spaces. Adding data sources to shared or managed spaces allows other users to access your data sources and use them in their own applications. Access to data can be controlled for different space members through space permissions. For more information on spaces, see [*Working in spaces*](Spaces.htm).

You can manage datasets or connections in a space by clicking Space settings and selecting Data files or Connections.

Information noteData spaces are not supported with Qlik Cloud Analytic Services. They are supported with Qlik Talend Data Integration only.

If you have on-premise data sources you want to use in your tenant, you can upload them to spaces using Qlik DataTransfer. For more information, see [*Uploading on-premises data with Qlik DataTransfer*](../QlikDataTransfer/qlik-datatransfer.htm).

## Adding and managing datasets

You can add and manage datasets for use from the catalog. You can create the following types of datasets:

- Add datasets as data files, which are stored locally within Qlik Cloud. You can add locally stored datasets in multiple ways, such as from the Analytics [activity center](#glossary-5 "Glossary term"), or from the Data files section when you are managing a space.

  [*Adding datasets as local files stored within Qlik Cloud*](../DataSource/add-datasets.htm#Adding)

  [*Managing data files*](manage-data-files-spaces.htm)
- Add datasets from external data connections. Data is available for use from the catalog, but is not stored within Qlik Cloud.

  [*Adding datasets from existing connections*](../DataSource/add-datasets.htm#AddFromConnectionExisting)

  [*Adding datasets from new connections*](../DataSource/add-datasets.htm#Adding4)

## Adding and managing data connections

You can create data connections in a number of ways, such as:

- From the Analytics [activity center](#glossary-6 "Glossary term").
- From the Connections section when you are managing a space.
- From the Data load editor or Data manager when working in an application.

For more information, see [*Adding data connections*](../DataSource/add-data-connections.htm) and [*Managing data connections*](manage-data-connections-spaces.htm).

Related learning:

- [How do I manage data files in Qlik Cloud?](/lnk/How_manage_data_files_Cloud)
