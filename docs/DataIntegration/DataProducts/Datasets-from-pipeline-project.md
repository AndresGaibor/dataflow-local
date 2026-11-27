---
title: "Creating datasets from a pipeline project"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Datasets-from-pipeline-project.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog"]
---

# Creating datasets from a pipeline project

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

As of now, the supported types for the quality compute are CSV, TXT, Parquet, QVD, XLS and XLSX, within these limits:

- CSV/TXT up to 1 GB
- Parquet up to 1 GB
- QVD up to 100 GB
- XLS/XLSX up to 100 MB

For Parquet files, data quality is supported only for flat schemas. Nested fields (LIST, MAP, STRUCT) are not supported.

Data quality is not supported for file-based datasets that exceed these limits. If your Excel file contains multiple sheets, the quality compute will be done on the first sheet only.

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

After running your pipeline project, the new dataset is added to the Catalog and you will be able to access quality indicators and more details about their content. This configuration also makes it possible to use the datasets as a source for analytics apps.

You can add as many datasets as necessary before building your data product. Since the Catalog can be accessed from both the Qlik Talend Data Integration hub, and Qlik Cloud Analytics Services hub, you can open your datasets in your preferred location, and the right connection will be used depending on the context.
