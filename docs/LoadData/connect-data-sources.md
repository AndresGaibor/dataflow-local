---
title: "Loading analytics data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/connect-data-sources.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data"]
---

# Loading analytics data

Qlik Cloud Analytics lets you to connect to your data, wherever it is stored, with a wide range of Qlik Connectors and other [data connection](#glossary-0 "Glossary term") types.

When you create a data connection it is saved, so you can quickly select and load data from the data sources that you commonly use.

## Adding and loading data

There are different ways you can add and load data.

- Add data to spaces

  You can add data files and data connections directly in spaces. You can also add data sources when managing spaces. Once data sources are added to a space, you can load data from them in your applications and scripts. Applications can use Data Catalog, data manager or data load editor. Scripts can use Script.

  For more information, see [*Adding and managing your analytics data*](../Spaces/managing-data-resources-spaces.htm).

  If you have on-premise data sources you want to use in your tenant, you can upload them using Qlik DataTransfer. For more information, see [*Uploading on-premises data with Qlik DataTransfer*](../QlikDataTransfer/qlik-datatransfer.htm).
- Load data into applications and scripts from the [data catalog](#glossary-1 "Glossary term")

  You can load data from datasets in the spaces to which you have access. Once loaded into your application, you can make associations and edit your data tables in Data manager.

  For more information, see [*Loading data from the data catalog*](adding-data-catalog.htm).
- Loading data into applications with [Data manager](#glossary-2 "Glossary term")

  There are different ways of adding data using Data manager. You can add data to your application from a new or an existing data source. You can also upload certain file types and load that data in Data manager. There is also the option to manually enter data into an editor and add it as a table in Data manager.

  For more information, see [*Loading and managing data with Data Manager*](managing-data.htm).
- Loading data into applications with [Data load editor](#glossary-3 "Glossary term")

  With Data load editor, you can select data from a new or existing data connection, or use the script editor to load data from a data connection. You can also edit existing data connections.

  For more information, see [*Loading and transforming data with scripting*](../Scripting/introduction-data-modeling.htm).
- Loading data into scripts with Script

  With Script, you can select data from a new or existing connection or use the script editor to load data from a data connection. You can also edit existing data connections.

  For more information, see [*Loading and transforming data with scripting*](../Scripting/introduction-data-modeling.htm).

Information noteDepending on your access to [shared](#glossary-4 "Glossary term") and [managed spaces](#glossary-5 "Glossary term"), you may have access to connections owned by others. You cannot change the owner of a connection.

## Data sources

You can load data from a variety of file formats. For more information, see [*Loading data from files*](../DataSource/load-data-from-files.htm).

You can also connect to a large number of data sources.

- ODBC and JDBC databases
- REST data sources
- Salesforce
- SAP NetWeaver
- Social media or web-based data sources
- Web storage providers

To see which data sources are available, see [Data sources in Qlik Cloud](/en-US/cloud-services/Content/Sense_Helpsites/Connectors_SaaS.htm).

## Refreshing data

After you have added your data and performed an initial load, you will likely need to refresh it regularly to allow analysis on the most current data. There are many ways in which you can refresh your data, such as manually, on a schedule using tasks, or with Qlik Automate.

For more information, see [*Refreshing analytics data*](../Refresh/refresh-analytics-data.htm).

Related learning:

- [How do I load data into a Qlik Sense application?](/lnk/How_load_data_QS_SaaS_app)
- [Loading Data from a Database](/lnk/Loading_data_from_database_QS)
