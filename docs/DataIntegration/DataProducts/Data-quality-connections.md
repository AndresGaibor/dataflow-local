---
title: "Data quality for connection-based datasets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Data-quality-connections.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog", "Assessing data quality"]
---

# Data quality for connection-based datasets

To benefit from semantic types discovery and data quality readings on your connection-based datasets, you need to set up an important prerequisite with your data connections in the context of data products.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

## Supported files, connections and databases

The following file types are supported:

- Excel files: XLS/XLSX
- Delimited text files: CSV/TXT
- JSON files: JSON
- XML files: XML
- Qlik data files: QVD (QlikView Data)/QVX (QlikView Exchange)
- Parquet files: PARQUET
- KML files: KML (Geographic data)

When you add a dataset from a cloud storage, the file cannot exceed 1 GB. This cloud-storage limit is separate from the limits for data-quality computation described below.

As of now, the supported types for the quality compute are CSV, TXT, Parquet, QVD, XLS and XLSX, within these limits:

- CSV/TXT up to 1 GB
- Parquet up to 1 GB
- QVD up to 100 GB
- XLS/XLSX up to 100 MB

For Parquet files, data quality is supported only for flat schemas. Nested fields (LIST, MAP, STRUCT) are not supported.

Data quality is not supported for file-based datasets that exceed these limits. If your Excel file contains multiple sheets, the quality compute will be done on the first sheet only.

- Data quality is supported in both pullup and pushdown modes for Snowflake and Databricks datasets.
- Data quality is supported in pullup mode for the datasets based on the following connections:

  - Amazon Athena
  - Amazon Redshift
  - Amazon S3 V2
  - Apache Hive
  - Apache Phoenix
  - Apache Spark
  - Azure SQL Database
  - Azure Storage
  - Azure Synapse Analytics
  - Cassandra
  - Cloudera Impala
  - Couchbase
  - DynamoDB
  - Dropbox
  - Google BigQuery
  - Google Cloud Storage
  - Google Drive
  - Marketo
  - Microsoft SQL Server
  - MongoDB
  - MySQL Entreprise Edition
  - Office 365 Sharepoint
  - OneDrive
  - Oracle
  - PostgreSQL
  - Presto
  - SAP Hana
  - SFTP
  - Snowflake

## Creating datasets from a table

When you create a dataset, you pick a database from the data source and then select tables in that database. A dataset is created for each table you select.

1. From the Catalog, click Create new > Dataset.
2. Select the connection and click Next.
3. Select the database and the schema from the dropdown list.
4. Select the tables and click Next.
5. Select the space and click Create datasets. You are redirected to the Catalog and you see the new datasets in the list.

You can now compute the data quality and add the datasets to data products. For more information, see [Configuring data quality computing](Configuring-data-quality.htm).

## Creating datasets from a file

1. From the Catalog, click Create new > Dataset.
2. Select the connection and click Next.
3. Select the file and click Next.
4. Select the space and click Create datasets. You are redirected to the Catalog and you see the new datasets in the list.

You can now compute the data quality and add the datasets to data products. For more information, see [Configuring data quality computing](Configuring-data-quality.htm).

## Creating connection-based datasets

You can create connection-based datasets from the Catalog but you can also use pipeline projects.

Creating datasets from a pipeline project lets you perform all your data integration within a project using data tasks. For more information, see [Creating a data pipeline project](/en-US/cloud-services/Introduction/Data-projects.htm).

### Creating datasets from the Catalog

When you do not need to use a pipeline project, you can create datasets to compute the data quality and consume the datasets through data products.

1. In Qlik Talend Data Integration > Catalog, click Create new > Dataset.
2. Select the connection and click Next.
3. Select the datasets and click Next.

   When a dataset is not in the list, it means that it is not in one of the supported formats:
   - Excel files:`.xls`, `.xlsx`
   - Delimited text files:`.csv`, `.txt`
   - Excel files:`.xls`, `.xlsx`
   - JSON files:`.json`
   - XML files:`.xml`
   - Qlik data files:`.qvd (QlikView Data)`, `.qvx (QlikView Exchange)`
   - Parquet files:`.parquet`
   - KML files:`.kml (Geographic data)`

   For quality computation, size limits apply to file-based datasets: CSV, TXT, and Parquet up to 1 GB, QVD up to 100 GB, and XLS/XLSX up to 100 MB.
4. Select the space and click Create datasets. You are redirected to the Catalog and you see the new datasets in the list.

You can now compute the data quality and add the datasets to data products. For more information, see [Configuring data quality computing](Configuring-data-quality.htm).

### Creating datasets from a pipeline project

1. In Qlik Talend Data Integration > Connections, click Create connection.
2. Configure your access to the database using the credentials of a user that has sufficient permissions and access to the tables you want to import.
3. In Qlik Cloud Analytics click Create, and then Data connection.
4. Configure your access to the same database as previously, using the credentials of the same user ideally, or one that has at least the READ permissions on the tables.
5. (for Snowflake only) In the Role field, you must enter a role that corresponds to an existing role created in the Snowflake database, and that has the following privileges on these objects.

   - USAGE on WAREHOUSE
   - USAGE on DATABASE
   - USAGE on SCHEMA
   - CREATE TABLE on SCHEMA
   - CREATE FUNCTION on SCHEMA
   - CREATE VIEW on SCHEMA
   - SELECT on TABLE
6. (for Databricks only) In Databricks, you must define the following privileges on the database:

   - CREATE TABLE
   - CREATE VOLUME
   - MODIFY
   - READ VOLUME
   - SELECT
   - USE SCHEMA
   - WRITE VOLUME
7. Back on the Qlik Talend Data Integration homepage, click Create new and then Pipeline project.
8. Use your connection from step 2 as source for your project and start building your pipeline. See [*Creating and managing data pipeline projects*](../Introduction/Data-projects.htm) for more information.
9. At any point in your pipeline, select a data task, go to Settings, and then the Catalog tab where you can select the Publish to Catalog checkbox.

   It means that this version of the dataset will be published to the Catalog when the pipeline project is prepared and run. It's also possible to check this option at the project level.
10. Run your data project.

After running your pipeline project, the new dataset is added to the Catalog and you will be able to access quality indicators and more details about their content. This configuration also makes it possible to use the datasets as a source for analytics applications.

You can add as many datasets as necessary before building your data product. Since the Catalog can be accessed from both the Qlik Talend Data Integration hub, and Qlik Cloud Analytics Services hub, you can open your datasets in your preferred location, and the right connection will be used depending on the context.

## Quality compute in pullup/pushdown

Using the Compute or Refresh button on the Overview of your dataset triggers a quality calculation on a sample of 1,000 rows.

This operation happens in pullup mode by default. For Snowflake and Databricks datasets, this operation can happen both in pullup mode (default), or in pushdown mode, on the database side.

After computing data quality, a preview of up to 1,000 rows (default) is retrieved and displayed with up-to-date semantic types, validity, and completeness statistics. This sample is then stored on MongoDB. To configure the dataset preview size (100 or 1,000 rows), tenant admins must go to the Settings page in the Administration activity center, for more information see [*Configuring dataset preview size*](../../Admin/mc-dataset-preview-size.htm).

Information note

For Databricks datasets computed in pushdown mode, the preview might occasionally contain fewer rows than the configured preview size if the computed sample returns fewer rows than requested. Databricks random sampling uses `TABLESAMPLE`, which returns an approximate number of rows. Since the preview is a subset of the computed sample, it cannot exceed the rows returned by the sample.

For more information, see [the corresponding Databricks documentation](https://docs.databricks.com/gcp/en/sql/language-manual/sql-ref-syntax-qry-select-sampling).

Information noteData quality cannot be computed for datasets that have more than 500 columns.

### Prerequisites for data quality in pushdown mode on Databricks

To compute data quality in pushdown mode on Databricks, Qlik needs to sync certain quality reference data, such as semantic types, to your Databricks instance. It also leverages some advanced features of Databricks.

For this feature to function properly, the following prerequisites must be met on your Databricks instance:

- [Unity Catalog](https://www.databricks.com/product/unity-catalog) must be enabled.
- Users associated with the Databricks connection must have permissions to create a table, [create a schema](https://docs.databricks.com/aws/en/schemas/create-schema), [create a volume](https://docs.databricks.com/aws/en/volumes/utility-commands), and write a volume.

  Qlik will create a schema named qlik\_internal in the database specificed in your connection. This schema will not be automatically removed by Qlik. You will need to delete it manually if you stop using SaaS cloud infrastructure.
- [Collations](https://www.databricks.com/blog/introducing-collations-databricks) must be enabled.

As for limitations, note that Date recognition in string columns is limited to the ISO-8601 format.
