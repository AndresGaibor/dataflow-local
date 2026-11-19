---
title: "Working with Apache Parquet files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-parquet-files.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading data from files"]
---
# Working with Apache Parquet files

Apache Parquet is a columnar storage format, highly efficient for storing and querying large datasets. In Qlik Sense, you can read data from Parquet files, and store tables as Parquet files.

Parquet allows for efficient querying of specific columns in a table rather than reading the entire table. This makes it well-suited for use with big data processing. Also, Parquet supports efficient compression and encoding of data. This can further reduce storage space and improve query performance.

## Creating Parquet files

You can create Parquet files using the Store command in the script. State in the script that a previously-read table, or part thereof, is to be exported to
an explicitly-named file at a location of your choice. You can nest the data your store in data in Parquet files.

For more information, see [*Store*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Store.htm).

## Reading data from Parquet files

You can read data from a Parquet file just like any other data file supported by Qlik Sense. This includes [Data manager](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-parquet-files.htm#glossary-0 "Glossary term"), [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-parquet-files.htm#glossary-1 "Glossary term"), or when you add data to a new application.

For more information, see [*Loading data from files*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/load-data-from-files.htm).

You can also load data from a Parquet file in the data [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-parquet-files.htm#glossary-3 "Glossary term") with the LOAD command. For example:

LOAD \* from [lib://DataFiles/xyz.parquet] (parquet);

For more information, see [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm).

### Loading data from nested Parquet files

If a Parquet file contains nested data, it needs to be loaded in multiple load statements, each specifying which subset should be loaded into each table. The **Table is** specifier is used to prove a path to the group node in the schema to be loaded.

You can use the specifer **Delimiter is** to specify how nodes should be combined. A LOAD statement loading a file with nested data that does not include delimiter is uses that value specified in by the script variable `FieldNameDelimiter`. If no delimiter is supplied and `FieldNameDelimiter` is not set, then the default delimiter will be `'.'`.

Only nodes that match the **Table is** path are loaded.

Data node are loaded into a file without nesting.

Group nodes will group the fields in the group by adding their name to the field name. For example, a group with field1 and field2 are loaded as group.field1 and group.field2.

List nodes will generate key fields that are used to link the tables. For example, %Key\_group.list. Any group or data node inside the list need to be loaded in a separate load statement. A key field to the parent list will also be added.

The following examples shows the same nested Parquet file, created in the example in [*Storing nested data in Parquet files*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Store.htm#Storing), loaded into an application, using Data manager and Data load editor (with the default scripting from Select data and custom scripting).

Example: Data manager

If you load customer.parquet in Data manager and apply all recommended associations, you end up with the following data model:

Data model for loading company.parquet with Data manager

![Data model showing the tables company:salesrep.salesrep, company, company:headquarter.headquarter, and company:headquarter.headquarter.city:region.region](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_parquet-load-script-dm-dmv.png)

Example: Data load editor (**Select data**)

If you load the data using **Select data** in Data load editor, you end up with the following script:

LOAD
company,
contact,
"%Key\_company:headquarter",
"%Key\_company:salesrep"
FROM [lib://DataFiles/company.parquet] (parquet);
LOAD
country,
city,
"%Key\_city:region",
"%Key\_company:headquarter"
FROM [lib://DataFiles/company.parquet] (parquet, table is [company:headquarter.headquarter]);
LOAD
region,
"%Key\_city:region"
FROM [lib://DataFiles/company.parquet] (parquet, table is [company:headquarter.headquarter.city:region.region]);
LOAD
salesrep,
"%Key\_company:salesrep"
FROM [lib://DataFiles/company.parquet] (parquet, table is [company:salesrep.salesrep]);

The data model looks like this in Data model viewer.

Data model for loading company.parquet with **Select data** in Data load editor

![Data model showing the tables salesrep, company, headquarter, and region.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_parquet-load-select-dmv.png)

Example: Data load editor (Custom load script)

If you use a custom load script, you have more control over how the fields and tables are loaded from customer.parquet. The following load script loads the tables and fields from company.parquet:

LOAD \* FROM [lib://DataFiles/company.parquet] (parquet);
LOAD \*, Lookup('company', '%Key\_company:salesrepo', [%Key\_company:salesrep], 'company') as company;
LOAD \* FROM [lib://DataFiles/company.parquet] (parquet, table is [company:salesrep.salesrep]);
DROP FIELD [%Key\_company:salesrep];
LOAD \*, Lookup('company', '%Key\_company:headquarter', [%Key\_company:headquarter], 'company') as company;
LOAD \* FROM [lib://DataFiles/company.parquet] (parquet, table is [company:headquarter.headquarter]);
DROP FIELD [%Key\_company:headquarter];
LOAD \*, Lookup('city', '%Key\_city:region', [%Key\_city:region], 'headquarter') as city;
LOAD \* FROM [lib://DataFiles/company.parquet] (parquet, table is [company:headquarter.headquarter.city:region.region]);
DROP FIELD [%Key\_city:region];

This results in the following data model, which is identical to the original data model before the data was stored in the Parquet file.

Data model for loading company.parquet with a custom script in Data load editor

![Data model with the tables headquarter, region, salesrep, and company, mirroring the exact data model from the source app.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_parquet-load-script-dmv.png)

## Limitations

Parquet files have the following limitations:

- Parquet files that contain an int96 timestamp field may not be loaded correctly.

  Int96 is a deprecated data type that contains a timestamp without timezone information. An attempt will be made to read the field as UTC, but as there are different vendor implementations there is no guarantee for success.

  Verify the loaded data and adjust it to the correct timezone with an offset if required.
