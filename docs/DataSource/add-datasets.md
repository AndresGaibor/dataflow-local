---
title: "Adding datasets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/add-datasets.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Adding and managing your analytics data"]
---

# Adding datasets

Add datasets for use from the catalog. You can upload data files directly to Qlik Cloud, where they can be used as datasets or in load scripts. You can also create datasets that reference data stored outside of Qlik Cloud—specifically, these datasets are defined using a [data connection](#glossary-0 "Glossary term").

## Adding datasets as local files stored within Qlik Cloud

You can upload data files directly to Qlik Cloud. When you upload a data file into Qlik Cloud, it is also created as a dataset containing metadata that can be accessed with catalog, impact analysis, and lineage tools. For additional considerations regarding distinctions between data files and datasets, see [*Distinctions between data files and datasets*](#Distinctions).

For supported file types, see [*Loading data from files*](load-data-from-files.htm).

Data files can be up to 100 GB. However, when uploading very large data files (over 6 GB), you might experience constraints with engine capacity. These constraints are more likely to be encountered with QVD data files due to the memory usage necessary to load QVD files into the engine. For more information about increasing the capacity available, see [*Large application support*](../Admin/large-app-support.htm).

Do the following:

1. Either:

   From the Create page and select Dataset.

   From the Catalog and click Create new > Dataset.
2. Click Upload data file.
3. Drag and drop your data files into the Add file dialog.

   Alternatively, click Browse and navigate to your data files.
4. Specify the Path for the file using the drop down menu. Start by selecting a space, and then navigate to the folder within the space where you want to store the file.

   Alternatively, type the full path manually.
5. Select a destination space for the files.
6. Click Upload.

   Alternatively, to create an application from your dataset immediately, click Upload and analyze.

Information note

When importing a dataset file into a Qlik Sense application or space with Data manager (drag-and-drop or other direct uploads), the maximum number of fields that can be loaded is 5000.

### Distinctions between data files and datasets

File-based data sources stored locally within Qlik Cloud are, at their source, data files. Each data file also exists as a dataset that can be analyzed and edited using catalog, lineage, and impact analysis tools.

When you store a data file directly within Qlik Cloud, the resource is created as a data file. Across Qlik Cloud, the same file will be shown in two different ways:

- In Space settings > Data files, the underlying data file is shown.
- From the general overview in Catalog, as well as in Home, Favorites and Collections, the dataset is shown. Depending on your access and location in the user interface, you might also be able to view the underlying data file for a dataset.

This distinction is important when you edit data files and datasets that are stored within Qlik Cloud. Editing a dataset stored within Qlik Cloud as a file—specifically, renaming it—does not rename the underlying data file. Instead, it simply adds an alias to the dataset. Because analytics content such as applications and scripts reference the underlying data file and not the dataset, you must rename the underlying data file and not its dataset if you need the references to function properly during application and script development.

For more information, see [*Distinctions between data files and datasets*](../Catalog/data-files-and-datasets.htm).

### Other ways to add data files

There are many other ways in which you can upload data files into Qlik Cloud Analytics. For example, it is often possible to add data as you build specific analytics resources.

Common methods include:

- When managing a space.

  [*Adding a data file to a space*](../Spaces/manage-data-files-spaces.htm#UploadFile)
- When building applications and scripts. You can use Data load editor, Data manager, or the Script interface to upload data files.

  [*Loading data from the data catalog*](../LoadData/adding-data-catalog.htm)

  [*Adding data from uploaded data files*](../LoadData/adding-data-datafiles.htm)

  [*Adding data to the application from connections and new files*](../LoadData/adding-data.htm)
- Using the STORE script statement during application and script development.

  [*Store*](../Scripting/ScriptRegularStatements/Store.htm)
- As output from a data flow.

  [*Loading and preparing data with Data flow*](../DataFlow/loading-preparing-with-data-flow.htm)
- As you add training data in an ML experiment.
- As you create a prediction configuration within an ML deployment.
- When working with Qlik Answers.

### Managing data files in spaces

For more information about managing data files stored locally within Qlik Cloud see [*Managing data files*](../Spaces/manage-data-files-spaces.htm).

## Adding datasets from existing connections

Create datasets from existing connections. When you create a dataset from a database connection, you pick a database from the data source and then select tables in that database. A dataset is created for each table you select. Datasets created this way refresh their data every time the dataset is opened.

Creating datasets from connections allows you to use cataloging and lineage options with data from your external data sources.

When you create a dataset from a data connection, the dataset does not contain any underlying data file that can be managed within the space. This is because the dataset is stored outside of Qlik Cloud.

Information note

Datasets created from a connection must reside in the same space as the connection to that data source. If the dataset is moved to a space without that connection, only the dataset name and limited metadata is available from the dataset.

Do the following:

1. Go to the Create page of the Analytics activity center and select Dataset.

   You can also add datasets from your mini-homes and by clicking Create new > Dataset in Catalog.
2. Select a connection to a data source from the available connections and click Next.
3. Under Database, select the database containing the tables for which you want to create datasets.
4. Under Tables, select the tables to create datasets from. Each table will make a new dataset.
5. Click Next.
6. Select the destination space for the data set from Select space.

   If the space does not have access to your selected connection, you need to select Create new connection in <space name>.
7. Click Create datasets.

## Adding datasets from new connections

Add a new connection and create a dataset from it.

When you create a dataset from a data connection, the dataset does not contain any underlying data file that can be managed within the space. This is because the dataset is stored outside of Qlik Cloud.

Information note

Datasets created from a connection must reside in the same space as the connection to that data source. If the dataset is moved to a space without that connection, only the dataset name and limited metadata is available from the dataset.

Do the following:

1. Go to the Create page of the Analytics activity center and select Dataset.

   You can also add datasets from your mini-homes and by clicking Create new > Dataset in Catalog.
2. Click Create connection.
3. Select the destination space for the connection.
4. Under Data connectors, select the data source.
5. Add the details for the connection.
6. Enter the connection settings for the data source.

   For information about supported connections, see [*Loading analytics data*](../LoadData/connect-data-sources.htm).
7. Click Create.
8. Select the connection from the available connections and click Next.
9. Under Database, select the database containing the tables for which you want to create datasets.
10. Under Tables, select the tables to create datasets from. Each table will make a new dataset.
11. Click Next.
12. Select the destination space for the data set from Select space.

    If the space does not have access to your selected connection, you need to select Create new connection in <space name>.
13. Click Create datasets.
