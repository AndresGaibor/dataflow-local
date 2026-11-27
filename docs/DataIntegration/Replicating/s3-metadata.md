---
title: "Metadata file description"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/s3-metadata.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating a replication project", "Landing data in a data lake with a Standard, Premium, or Enterprise subscription"]
---

# Metadata file description

When the [Create metadata files in the target folder](landing-datalakes-settings.htm) option is selected, for each CSV/JSON/Parquet file the data lake landing task creates a corresponding metadata file under the specified target folder.

The metadata file offers several benefits such as enabling custom batch processes to perform better validation, supporting deeper automation, offering lineage information and improving processing reliability.

The metadata files are described in the tables below.

Information note

All timestamps are in ISO-8601 format, for example 2016-08-02T10:05:04.802.

Task Information file

| Field | Description |
| --- | --- |
| name | The name of the data lake landing task. |
| sourceEndpoint | The name defined in the source endpoint settings. |
| sourceEndpointType | The source connector type (e.g. Oracle, MySQL, etc.). |
| sourceEndpointUser | The user defined in the source endpoint settings. |
| replicationServer | The hostname of the machine on which Data Movement gateway is installed. |
| operation | If a target data file has been created, this field will contain the following value: dataProduced |

File Information file

| Field | Description |
| --- | --- |
| name | The name of the data file without the extension. |
| extension | The extension of the data file (.csv or.json according to the selected target file format). |
| location | The location of the data file. |
| startWriteTimestamp | UTC timestamp indicating when writing to the file started. |
| endWriteTimestamp | UTC timestamp indicating when writing to the file ended. |
| firstTransactionTimestamp | UTC timestamp of the first record in the file. |
| lastTransactionTimestamp | UTC timestamp of the last record in the file. |
| content | The values can either be data (for Full Load landing) or changes (For CDC landing), according to the data in the corresponding CSV file. |
| recordCount | The number of records in the file. |
| errorCount | The number of data errors encountered during file creation. |

Format Information file

| Field | Description |
| --- | --- |
| format | delimited or json according to the selected target file format. |
| options | The options for delimited file format. These options will not be shown for json format as they are not relevant. |
| recordDelimiter | The delimiter used to separate records (rows) in the target files. The default is newline (\n). |
| fieldDelimiter | The delimiter used to separate fields (columns) in the target files. The default is a comma. |
| nullValue | The string used to indicate a null value in the target file. |
| quoteChar | The character used at the beginning and end of a column. The default is the double-quote character ("). |
| escapeChar | The character used to escape a string when both the string and the column containing the string are enclosed in double quotes. Note that the string’s quotation marks will be removed unless they are escaped.  Example (where " is the quote character and \ is the escape character):  1955,"old, \"rare\", Chevrolet",$1000 |

Custom Information file

| Field | Description |
| --- | --- |
| customInfo | This section contains any custom properties that were set using the dfmCustomProperties internal property.  The dfmCustomProperties internal parameter must be specified in the following format:  Parameter1=Value1;Parameter2=Value2;Parameter3=Value3  Example:  Color=Blue;Size=Large;Season=Spring  For an explanation of how to set internal properties, see [*Amazon S3*](../TargetConnections/aws-s3-target.htm#Connecti). |

Data Information file

| Field | Description |
| --- | --- |
| sourceSchema | The schema containing the source table. |
| sourceTable | The name of the source table. |
| targetSchema | The name of the target table schema (if the source schema name was changed). |
| targetTable | The name of the target table (if the source table name was changed). |
| tableVersion | The data lake landing task assigns an internal version number to the table. The version number increases whenever a DDL change occurs in the source table. |
| columns | Information about the table columns. |
| ordinal | The position of the column in the record (1, 2, 3, etc.). |
| name | The column name. |
| type | The column data type. See [*Supported data types*](landing-datalakes-datatypes.htm) for more information. |
| width | The maximum size of the data (in bytes) permitted for the column. |
| scale | The maximum number of digits to the right of the decimal point permitted for a number. |
| primaryKeyPos | The position of the column in the table’s Primary Key or Unique Index. The value is zero if the column is not part of the table’s Primary Key. |
