---
title: "Data quality for uploaded files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Data-quality-files.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog", "Assessing data quality"]
---

# Data quality for uploaded files

To benefit from semantic types discovery and data quality readings on your file-based datasets, you need to upload your files in your Catalog.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

## Supported files for data quality

As of now, the supported types for the quality compute are CSV, TXT, Parquet, QVD, XLS and XLSX, within these limits:

- CSV/TXT up to 1 GB
- Parquet up to 1 GB
- QVD up to 100 GB
- XLS/XLSX up to 100 MB

For Parquet files, data quality is supported only for flat schemas. Nested fields (LIST, MAP, STRUCT) are not supported.

Data quality is not supported for file-based datasets that exceed these limits. If your Excel file contains multiple sheets, the quality compute will be done on the first sheet only.

## Uploading your files

In order for you to create datasets from a file, and later have access to their schema and quality in the dataset overview and data product overview, you need to upload them in Qlik Talend Data Integration.

1. From the Catalog, click Create new, and then Dataset.
2. Click Upload data file.
3. Browse to the files you want to upload, select the space in which you want to upload them, and click Upload.

   When you are uploading only one file, you can click Upload and analyze to create both a dataset and an analytics application from this file.

The new dataset is added to the Catalog and you will be able to access quality indicators and more details about their content. This configuration also makes it possible to use the file-based dataset as source for analytics applications.

Since the Catalog can be accessed from both the Qlik Talend Data Integration hub, and Qlik Analytics Services hub, you can open your datasets in your preferred location, and the right connection will be used depending on the context.

## Quality compute

Using the Compute or Refresh button on the Overview of your dataset triggers a quality calculation on a sample of 1,000 rows of the database. This operation happens in pullup mode for file-based datasets.

After computing data quality, a preview of up to 1,000 rows (default) is retrieved and displayed with up-to-date semantic types, validity, and completeness statistics. This sample is then stored on MongoDB. To configure the dataset preview size (100 or 1,000 rows), tenant admins must go to the Settings page in the Administration activity center, for more information see [*Configuring dataset preview size*](../../Admin/mc-dataset-preview-size.htm).
