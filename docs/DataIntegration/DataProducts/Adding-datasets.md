---
title: "Adding datasets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Adding-datasets.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog"]
---

# Adding datasets

Adding datasets lets you use them from the catalog. You can upload files directly to Qlik Cloud, where they can be used as datasets or in load scripts. You can also create datasets that reference data stored outside of Qlik Cloud—specifically, these datasets are defined using a [data connection](#glossary-0 "Glossary term").

## Supported files

When you connect to a file from a cloud storage, the following file types are supported:

- Excel files: XLS/XLSX
- Delimited text files: CSV/TXT
- JSON files: JSON
- XML files: XML
- Qlik data files: QVD (QlikView Data)/QVX (QlikView Exchange)
- Parquet files: PARQUET
- KML files: KML (Geographic data)

When you upload a file or connect to a file from a cloud storage, some restrictions apply to the quality compute.

As of now, the supported types for the quality compute are CSV, TXT, Parquet, QVD, XLS and XLSX, within these limits:

- CSV/TXT up to 1 GB
- Parquet up to 1 GB
- QVD up to 100 GB
- XLS/XLSX up to 100 MB

For Parquet files, data quality is supported only for flat schemas. Nested fields (LIST, MAP, STRUCT) are not supported.

Data quality is not supported for file-based datasets that exceed these limits. If your Excel file contains multiple sheets, the quality compute will be done on the first sheet only.

## Uploading your files

You can upload files directly to the Catalog. When you upload a file into Qlik Cloud, it is also created as a dataset containing metadata that can be accessed with catalog, impact analysis, and lineage tools. For additional considerations regarding distinctions between files and datasets, see [*Distinctions between files and datasets*](#Distinctions).

Data files can be up to 100 GB. However, when uploading very large data files (over 6 GB), you might experience constraints with engine capacity. These constraints are more likely to be encountered with QVD data files due to the memory usage necessary to load QVD files into the engine. For more information about increasing the capacity available, see [*Large application support*](../../Admin/large-app-support.htm).

1. From the Catalog, click Create new, and then Dataset.
2. Click Upload file.
3. Browse to the files you want to upload, select the space in which you want to upload them, and click Upload.

   When you are uploading only one file, you can click Upload and analyze to create both a dataset and an analytics application from this file.

Information note

When importing a dataset file into a Qlik Sense application or space with Data manager (drag-and-drop or other direct uploads), the maximum number of fields that can be loaded is 5000.

## Adding datasets from connections

Creating datasets from connections lets you use cataloging and lineage options with data from your external data sources.

When you create a dataset from a data connection, the dataset does not contain any underlying data file that can be managed within the space. This is because the dataset is stored outside of Qlik Cloud.

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

## Distinctions between files and datasets

File-based data sources stored locally within Qlik Cloud are, at their source, data files. Each data file also exists as a dataset that can be analyzed and edited using catalog, lineage, and impact analysis tools.

When you store a data file directly within Qlik Cloud, the resource is created as a data file. Across Qlik Cloud, the same file will be shown in two different ways:

- In Space settings > Data files, the underlying data file is shown.
- From the general overview in Catalog, as well as in Home, Favorites and Collections, the dataset is shown. Depending on your access and location in the user interface, you might also be able to view the underlying data file for a dataset.

This distinction is important when you edit files and datasets that are stored within Qlik Cloud. Editing a dataset stored within Qlik Cloud as a file—specifically, renaming it—does not rename the underlying file. Instead, it simply adds an alias to the dataset. Because analytics content such as apps and scripts reference the underlying file and not the dataset, you must rename the underlying file and not its dataset if you need the references to function properly during app and script development.

For more information, see [*Distinctions between data files and datasets*](../../Catalog/data-files-and-datasets.htm).

### Managing files in spaces

For more information about spaces, see [*Working in spaces in Data Integration*](../DataSpaces/working-spaces.htm).
