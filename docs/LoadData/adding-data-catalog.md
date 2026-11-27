---
title: "Loading data from the data catalog"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/adding-data-catalog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data"]
---

# Loading data from the data catalog

You can load data into your application or script from existing datasets to which you have access with the data catalog.

Information noteIf you need to prepare your data before loading it, such as by selecting delimiters, heading rows, or filters, you should load data using Add data. For more information, see [*Adding data to the application from connections and new files*](adding-data.htm).

## Loading data from the data catalog in Data manager

Do the following:

1. Open an application.
2. Open Data manager.
3. Click ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) Add data > Data catalog. You can also click Data catalog in ![Navigation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
4. Select the data you want to load.

   - To load all the data from a dataset, select the checkbox corresponding to that row.
   - To load certain tables or fields from a dataset, click View fields next to the dataset's name. Select the fields from the tables you want to load.
   - To upload files from your computer, click Upload file to browse for files on your computer and add them to the list of available datasets.

   Information note

   Data manager (including its Data catalog interface) does not support adding data from data products. To add data from data products, use Data load editor—either using Data load editor's Data catalog interface or by writing script manually.
5. In Summary, review the data you are adding to your application and click Load into application.

   The tables are added to Data manager.

Information note

When importing a dataset file into a Qlik Sense application or space with Data manager (drag-and-drop or other direct uploads), the maximum number of fields that can be loaded is 5000.

### Next steps

Your selected data is now available in Data manager. You can continue working on your tables in Data manager, making associations or editing your tables using the data profiling options. When you are ready to load the data into your application, click Load data.

Some additional steps you may wish to do before loading data:

- To associate your tables, see [*Managing data associations*](associating-data.htm).
- To edit your tables, adding calculated fields or using the data profiling cards to transform your data, see [*Editing a table*](editing-table.htm).
- To concatenate related tables, see [*Concatenating tables in Data manager*](concatenating-tables-in-data-manager.htm).
- To join tables together, see [*Joining tables in Data manager*](join-keep-tables-in-data-manager.htm).

## Loading data from the data catalog in Data load editor

Do the following:

1. Open an application.
2. Open Data load editor.
3. Under Add data, click Add from data catalog.
4. Select the data you want to load.

   - You can load the data and semantic model (a reusable data model with additional master items) from a data product. For full details, see [*Consuming data products in applications*](../DataIntegration/DataProducts/consuming-data-products-apps.htm).
   - To load all the data from a dataset, select the checkbox corresponding to that row.
   - To load certain tables or fields from a dataset, hover your cursor over the dataset name and click Refine selection. Select the items you want to load.
   - To upload files from your computer, click Upload file to browse for files on your computer and add them to the list of available datasets.

   Information noteYou can filter the data by type (datasets or data products). Data products are available in some subscriptions only. For more information, see [*Working with data products*](../DataIntegration/DataProducts/Data-products.htm).
5. In Summary, review the data you are adding to your application and click Load into application.

   The tables are added to the [load script](#glossary-2 "Glossary term").

## Loading data from the data catalog in Data flow

Do the following:

1. Open a data flow.
2. Open Editor.
3. Under Data catalog, click Browse catalog.
4. Select the data you want to load.

   - To load all the data from a dataset or data product, select the checkbox corresponding to that row.
   - To load certain datasets from a data product, click the arrow next to the data product's name. Select the datasets you want to load.
   - To load certain tables or fields from a dataset, click View fields next to the dataset's name. Select the fields from the tables you want to load.
   - To upload files from your computer, click Upload file to browse for files on your computer and add them to the list of available datasets.

   Information noteYou can filter the data by type (datasets or data products). Data products are available in some subscriptions only. For more information, see [*Working with data products*](../DataIntegration/DataProducts/Data-products.htm).
5. To display the information regarding the dataset or data product quality, click Details. The Details panel opens with all the quality information.
6. Click Next.
7. In Summary, review the data you are adding and click Load into data flow.

   The data is added to the data flow.

## Loading data from the data catalog in Script

Do the following:

1. Open a script.
2. Open Editor.
3. Under Add data, click Add from data catalog.
4. Select the data you want to load.

   - To load all the data from a dataset or data product, select the checkbox corresponding to that row.
   - To load certain datasets from a data product, click the arrow next to the data product's name. Select the datasets you want to load.
   - To load certain tables or fields from a dataset, click View fields next to the dataset's name. Select the fields from the tables you want to load.
   - To upload files from your computer, click Upload file to browse for files on your computer and add them to the list of available datasets.

   Information noteYou can filter the data by type (datasets or data products). Data products are available in some subscriptions only. For more information, see [*Working with data products*](../DataIntegration/DataProducts/Data-products.htm).
5. To display the information regarding the dataset or data product quality, click Details. The Details panel opens with all the quality information.
6. Click Next.
7. In Summary, review the data you are adding to your application and click Insert script.

   The tables are added to the script.

## Loading data from the data catalog in Table recipe

Do the following:

1. Open a table recipe.
2. Open Editor.
3. Click Set source.
4. Browse for previously uploaded datasets, or click Upload file to browse for files on your computer and upload them on the fly.
5. Using the search and filters, select the checkbox in front of a single dataset from your list.
6. To display the information regarding the dataset, click Details. The Details panel opens with all the quality information.
7. Click Next.
8. In Summary, review the data you are adding and click Load into table recipe.

   The data is added to the table recipe.

## Limitations

Data catalog has the following limitations:

- When selecting a [QVD](#glossary-3 "Glossary term") created from an Amazon S3 bucket, data catalog always uses the first [connection](#glossary-4 "Glossary term") in the list if there are multiple connections.

Related learning:

- [How do I load data into a Qlik Sense application?](/lnk/How_load_data_QS_SaaS_app)
