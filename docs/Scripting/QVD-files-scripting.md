---
title: "QVD files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/QVD-files-scripting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Next steps in scripting"]
---
# QVD files

A [QVD](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/QVD-files-scripting.htm#glossary-0 "Glossary term") (QlikView Data) file is a file containing a table of data exported from Qlik Sense or QlikView. QVD is a native Qlik format and can only be written to and read by Qlik Sense or QlikView. The file format is optimized for speed when reading data from a Qlik Sense script but it is still very compact. Reading data from a QVD file is typically 10-100 times faster than reading from other data sources.

QVD files can be read in two modes: standard (fast) and optimized (faster). The selected mode is determined automatically by the Qlik Sense script engine. Optimized mode can be utilized only when all loaded fields are read without any transformations (formulas acting upon the fields), although renaming of fields is allowed. A Where clause causing Qlik Sense to unpack the records will also disable the optimized load.

A QVD file holds exactly one data table and consists of three parts:

- An XML header (in UTF-8 char set) describing the fields in the table, the layout of the subsequent information and some other metadata.
- Symbol tables in a byte-stuffed format.
- Actual table data in a bit-stuffed format.

QVD files can be used for many purposes. Three major uses can be easily identified. More than one may apply in any given situation:

- Decreasing load on database servers

The amount of data fetched from external data sources can also be greatly reduced. This reduces the workload on external databases and network traffic. Furthermore, when several Qlik Sense scripts share the same data, it is only necessary to load it once from the source database into a QVD file. The other applications can make use of the same data through this QVD file.

- Consolidating data from multiple Qlik Sense applications.

With the Binary script statement it is possible to load data from only one single Qlik Sense application into another one, but with QVD files a Qlik Sense script can combine data from any number of Qlik Sense applications. This opens up possibilities for applications consolidating similar data from different business units etc.

- Incremental load

In many common cases the QVD functionality can be used for facilitating incremental load by exclusively loading new records from a growing database.

> **Note:** To see how the Qlik Community is using Qlik Automate to improve QVD load times, see [How to split QVDs using an automation to improve reloads](https://community.qlik.com/t5/Official-Support-Articles/How-to-split-QVDs-using-an-automation-to-improve-reloads/ta-p/1997153).

## Creating QVD files

A QVD file can be created and named using the store command in the script. State in the script that a previously-read table, or part thereof, is to be exported to
an explicitly-named file at a location of your choice.

### Store

This script statement creates an explicitly named QVD, Parquet, CSV, or TXT file.

Syntax:

Store[ \*fieldlist from] table into filename [ format-spec ];

The statement can only export fields from one data table. If fields from several tables are to be exported, an explicit join must be made previously in the script to create the data table that should be exported.

The text values are exported to the CSV file in UTF-8 format. A delimiter can be specified, see LOAD. The store statement to a CSV file does not support BIFF export.

Examples:

Store mytable into [lib://DataFiles/xyz.qvd];
Store \* from mytable into [lib://DataFiles/xyz.qvd];
Store myfield from mytable into [lib://DataFiles/xyz.qvd];
Store myfield as renamedfield, myfield2 as renamedfield2 from mytable into [lib://DataFiles/xyz.qvd];
Store mytable into [lib://DataFiles/myfile1.txt];
Store mytable into [lib://DataFiles/myfile2.csv];

Do the following:

1. Open the Advanced Scripting Tutorial application.
2. Click the Product script section.
3. Add the following to the end of the script:

```
Store * from Product into [lib://DataFiles/ProductData.qvd](qvd);
```

Your script should look like this:

```
CrossTable(Month, Sales)
LOAD
    Product,
    "Jan 2014",
    "Feb 2014",
    "Mar 2014",
    "Apr 2014",
    "May 2014"
FROM [lib://DataFiles/Product.xlsx] 
(ooxml, embedded labels, table is Product);

Store * from Product into [lib://DataFiles/ProductData.qvd](qvd);
```

4. Click **Load data**.

The Product.qvd file should now be in the list of files.

This data file is the result of the Crosstable script and is a three-column table, one column for each category (Product, Month, Sales). This data file could now be used to replace the entire Product script section.

## Reading data from QVD files

A QVD file can be read into or accessed by Qlik Sense by the following methods:

- Loading a QVD file as an explicit data source. QVD files can be referenced by a load statement in the Qlik Sense script just like any other type of text files (csv, fix, dif, biff, and so on).

Examples:

LOAD \* from [lib://DataFiles/xyz.qvd] (qvd);
LOAD fieldname1, fieldname2 from [lib://DataFiles/xyz.qvd] (qvd);
LOAD fieldname1 as newfieldname1, fieldname2 as newfieldname2 from [lib://DataFiles/xyz.qvd](qvd);

- Accessing QVD files from the script. A number of script functions (all beginning with QVD) can be used for retrieving various information on the data found in the XML header of a QVD file.

Do the following:

1. Comment out the entire script in the Product script section.
2. Enter the following script:

```
Load * from [lib://DataFiles/ProductData.qvd](qvd);			
```

3. Click **Load data**.

The data is loaded from the QVD file.

Data load progress window

![Data load progress window.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load-qvd.png)
> **Note:** To learn about using QVD files for incremental loads, see this blog post in Qlik Community: [Overview of Qlik Incremental Loading](https://community.qlik.com/t5/Qlik-Design-Blog/Overview-of-Qlik-Incremental-Loading/ba-p/1466780)

## Thank you!

Now you have finished this tutorial, and hopefully you have gained some more knowledge about scripting in Qlik Sense. Please visit our website for more information on the further training available.
