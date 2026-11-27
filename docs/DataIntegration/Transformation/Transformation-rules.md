---
title: "Creating rules to transform datasets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Transformation-rules.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Managing datasets"]
---

# Creating rules to transform datasets

You can create re-usable transformation rules to perform global transformation on datasets in Replication, Landing, Storage, Transform, and Data mart data tasks.

Information noteGlobal transformations are not supported with datasets and columns that are added to tasks due to [schema evolution](../Landing/Landing-data-data-sources.htm#Schema).

Select Datasets, Click Transformation rules, and then Add transformation rule to create a new transformation rule.

1. Select the transformation type and click Next.

   You can perform the following transformations:

   - Rename datasets
   - Override data message publishing

     Information note
     - Available for Kafka target only.
     - If you are using Data Movement gateway (required with on-premises Kafka), version 2025.5.40 or later is required.
   - Rename columns
   - Add columns
   - Drop columns
   - Convert data types
   - Replace column values
2. Select the transformation scope and click Next.
3. Select which transformation action to perform and click Next.
4. Add a name and a description for the rule and click Finish.

The rule will be applied when you run the data task. If you add more than one rule, the rules are executed in the order they are listed.

Tip noteYou can use variables, for example column names, in an expression in a rule. For more information, see [*Including metadata in an expression*](#Using).

## Transformation scope

When several transformations apply to the same dataset or columns, the scope is always on the original source names, while the action relates to the value after the previous rule was applied. For example, if you have these rules:

1. Rename all datasets that start with Abc\_ (Abc\_%) to change prefix to ABC\_.
2. Add suffix \_zzz to datasets that start with ABC\_ (ABC\_%).

Applying the rules to these datasets would provide these results. Note that after the second rule, the \_zzz suffix is not added to ABC\_customers as the scope is always on the original name (Abc\_customers).

| Original dataset name | Dataset name after rule 1 | Dataset name after rule 2 |
| --- | --- | --- |
| Abc\_customers | ABC\_customers | ABC\_customers |
| ABC\_Suppliers | ABC\_Suppliers | ABC\_Suppliers\_zzz |

## Renaming datasets

1. Select Rename dataset, and then click Next.
2. Set the transformation scope, that is, which datasets to rename. You can use % as a wild card character to select several datasets from one or more data assets.

   Click Next.
3. Set the transformation action. You can perform the following actions:

   - Rename dataset to a fixed name.
   - Add a prefix or suffix.
   - Remove a prefix or suffix.
   - Replace a prefix or suffix.
   - Change case to lowercase or uppercase.
   - Replace dataset names using an expression.
   - Replace dataset names using a dictionary.

     For more information, see [*Renaming datasets or columns using a dictionary*](#Renaming).

   Click Next when you are ready.
4. Set the name of the rule, and click Finish.

## Customizing data message publishing

Information noteAvailable for Kafka target only.

1. Select Customize data message publishing, and then click Next.
2. Set the transformation scope, that is, for which datasets to override the data message publishing settings. You can use % as a wild card character to select several datasets from one or more data assets.

   Click Next.
3. Set the transformation action.

   For each setting, the current task setting is indicated by the field Task setting: <setting> (for example, Task setting: Specific topic).

   For a description of these settings, see [*Data message publishing*](../Replicating/replicating-settings.htm#Data3).

   You can either retain the task setting or use the Expression Builder to specify a custom topic, message key, or partition key.

   Information noteThese settings will override the tasks settings, but they will not override settings configured for individual datasets.

   To use the Expression Builder:

   1. Select the Custom topic, Custom message key, or Custom partition key field as appropriate, and click ![Expression icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression.svg).

      Information noteCustom topics must already exist or the broker must be configured to create them.

      The Expression Builder opens.
   2. Build an expression.

      You can use functions, operators, and metadata to build the expression.

      Click ![Right arrow icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to move an item to the expression.

      You can also use all functions supported by Kafka in the expression.
   3. Click Extract parameters.

      You can now add a test value to Value to test for all parameters.
   4. Click Test expression.

      You should now see the result of the expression, using the test values.
   5. When you are ready, click OK.

      The expression is added to the field.

   ### Building expressions

   You need to build an expression that defines custom values. You can use:

   - Functions

     String functions, numeric functions, null check functions, data and time functions, and logical functions.
   - Operators

     Mathematical and logical operators. Some operators are also available in the toolbar above the expression. This is also where you find the operator for string concatenation, ||.
   - Metadata

     The following metadata is available:

     - $Q\_M\_SCHEMA\_NAME
     - $Q\_M\_SOURCE\_SCHEMA\_NAME
     - $Q\_M\_SOURCE\_TABLE\_NAME
     - $Q\_M\_TABLE\_NAME

   Click ![Right arrrow icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to move an item to the expression.

   You can also use all functions supported by Kafka in the expression.

   Click Next when you are ready.
4. Set the name of the rule, and click Finish.

## Renaming columns

1. Select Rename column, and then click Next.
2. Set the transformation scope, that is, which columns to rename. You can use % as a wild card character to select several columns from one or more data tasks and datasets.

   You can also limit the action to a certain data type. Set data type to UNSPECIFIED to perform the action for all matching columns, regardless of data type.

   Click Next.

   You can also limit the scope to columns that are keys or nullable.
3. Set the transformation action. You can perform the following actions:

   - Rename column to a fixed name.
   - Add a prefix or suffix.
   - Remove a prefix or suffix.
   - Replace a prefix or suffix.
   - Change column case to lowercase or uppercase.
   - Replace column names using an expression.
   - Replace column names using a dictionary.

     For more information, see [*Renaming datasets or columns using a dictionary*](#Renaming).

   Click Next when you are ready.
4. Set the name of the rule, and click Finish.

## Adding columns

1. Select Add column, and then click Next.
2. Set the transformation scope, that is, which dataset to add the column. You can use % as a wild card character to add the column to one or more datasets.

   Click Next.
3. Set the details of the new column:

   - Column name.
   - Use the expression builder to set Value for the column.
   - Select Add to primary key to use this column as a primary key.
   - Set the data type in Target data type.
   - If data type is BYTES, STRING, or WSTRING, specify a Length as well.

     If data type is NUMERIC, specify Precision and Scale as well.

   Click Next when you are ready.
4. Set the name of the rule, and click Finish.

## Dropping columns

1. Select Drop column, and then click Next.
2. Set the transformation scope, that is, which columns to drop. You can use % as a wild card character to select several columns from one or more data assets and datasets.

   You can also limit the action to a certain data type. Set data type to UNSPECIFIED to perform the action for all matching columns, regardless of data type.

   Click Next.

   You can also limit the scope to columns that are keys or nullable.
3. Set the name of the rule, and click Finish.

## Converting data types

1. Select Convert data type, and then click Next.
2. Set the transformation scope, that is, which columns to convert data type. You can use % as a wildcard character to select several columns from one or more data assets and datasets.

   You can also limit the action to a certain data type. Set data type to UNSPECIFIED to perform the action for all matching columns, regardless of data type.

   Click Next.

   You can also limit the scope to columns that are keys or nullable.
3. Set the transformation action.

   - Set Target data type to the data type to convert into.

     - If data type is BYTES, STRING, or WSTRING, choose one of the following to change its length:

       - Fixed value: Specify a length.
       - Expression: Create an expression as described in [*Creating an expression*](#Creating) below.
     - If data type is NUMERIC or DATETIME, choose one of the following for Precision and Scale:

       - Fixed value: Specify a value.
       - Expression: Create an expression as described in [*Creating an expression*](#Creating) below.
4. Click Next when you are ready.
5. Set the name of the rule, and click Finish.

See also: [*Managing data types*](../Introduction/Managing-data-types.htm)

### Creating an expression

For shared editor guidance and movement-task references, see [*Building expressions*](Building-expressions.htm). The following procedure also supports rule metadata expressions.

To create an expression:

1. Use the Functions, Operators, and Metadata to build the expression.

   Click ![Right arrow icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to move an item to the Build expression area.

   You can also use all functions supported by the cloud data platform in the expression.
2. Click Extract parameters.

   You can now add a test value to Value to test for all parameters.
3. Click Test expression.

   You should now see the result of the expression, using the test values.
4. When you are ready, click OK.

The expression defines the target data type.

Example expression for data type length:

$Q\_M\_DATATYPE\_LENGTH\*2

## Replacing column values

1. Select Replace column values, and then click Next.
2. Set the transformation scope, that is, which columns to replace values for. You can use % as a wild card character to select several columns from one or more data assets and datasets.

   You can also limit the action to a certain data type. Set data type to UNSPECIFIED to perform the action for all matching columns, regardless of data type.

   Click Next.

   You can also limit the scope to columns that are keys or nullable.
3. Set the transformation action.

   - Set an expression to define the replacement values in Target value.
   - Set Target data type to the data type for the replaced columns.
   - If data type is BYTES, STRING, or WSTRING, specify a Length as well.

     If data type is NUMERIC, specify Precision and Scale as well.

   Click Next when you are ready.
4. Set the name of the rule, and click Finish.

## Renaming datasets or columns using a dictionary

You can use a dictionary to rename datasets or columns. This is useful when you are working with a large number of objects that use cryptic naming conventions. You can add translations in a dictionary editor or import a CSV file containing the translations. You can also export the dictionary to a CSV file and reuse it in another data asset.

Rename by dictionary is available in Transformation actions when you have selected Rename datasets or Rename columns. Click ![Book](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_book.svg) to open the dictionary editor.

- Click Add translation and fill in Source name and Translated name to add a translation to the dictionary.

When you have created the translations you need, click OK to close the dictionary editor.

Information noteThe name will only be replaced if there is a full match with the source name in the dictionary. Partial matches are not supported.

### Importing translations

You can import translations from a CSV file containing a dictionary. The file should contain one translation per row. Example:

sourcename1,translatedname1
sourcename2,translatedname2
sourcename3,translatedname3

- Click Append from CSV and select the CSV file to import.

The translations in the imported dictionary are appended to your dictionary.

### Exporting translations

You can export your dictionary to a CSV file to be able to reuse it in other data assets.

- Click Export to CSV.

The dictionary is exported to a CSV file.

## Including metadata in an expression

The Metadata tab in the expression editor contains the following variables that you can use in an expression in a transformation rule.

Information noteDuring data movement, the original source data types are mapped to Qlik Talend Data Integration data types, before being optionally transformed and mapped to the target. For example, the BIT data type in MySQL is mapped to the BOOLEAN data type in Qlik Talend Data Integration. Consequently, variables with DATATYPE in their names either refer to the Qlik Talend Data Integration data type or to the transformed data type, and not the original source data type.

Variables that can be used in transformation rules

| Variable | Description |
| --- | --- |
| $Q\_D\_COLUMN\_DATA | The column value in the source table. |
| $Q\_M\_COLUMN\_NAME | The modified column name. |
| $Q\_M\_DATATYPE\_LENGTH | The modified data type length of a column. |
| $Q\_M\_DATATYPE\_NAME | The modified data type of a column. |
| $Q\_M\_DATATYPE\_PRECISION | The modified data type precision of a column. |
| $Q\_M\_DATATYPE\_SCALE | The modified data type scale of a column. |
| $Q\_M\_SCHEMA\_NAME | The name of the source schema. |
| $Q\_M\_SOURCE\_COLUMN\_NAME | The name of a column in the source table. |
| $Q\_M\_SOURCE\_DATATYPE\_LENGTH | The data type length of a column in the source table. |
| $Q\_M\_SOURCE\_DATATYPE\_NAME | The data type of a column in the source table. |
| $Q\_M\_SOURCE\_DATATYPE\_PRECISION | The data type precision of a column in the source table. |
| $Q\_M\_SOURCE\_DATATYPE\_SCALE | The data type scale of a column in the source table. |
| $Q\_M\_SOURCE\_TABLE\_NAME | The name of the source table. |
| $Q\_M\_TABLE\_NAME | The modified name of the source table. |

Example:

You can rename all tables that are in the transformation scope to add the schema name as prefix with the following expression:

${Q\_M\_SCHEMA\_NAME}||'.'||${Q\_M\_SOURCE\_TABLE\_NAME}.

This would for example rename the table products in the dwprod schema to dwprod.products.

## Managing rules

You can manage rules in the Rules pane.

- Click Rules.

You can enable/disable a rule, delete a rule, and edit a rule.
