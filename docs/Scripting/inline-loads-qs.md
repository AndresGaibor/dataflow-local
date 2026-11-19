---
title: "Using inline loads to load data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data", "Basic syntax example"]
---
Expand/Collapse all

# Using inline loads to load data

Type data manually into a script to define an inline table, which can be loaded into an application. You can work with inline loads in the Data load editor and Script.

You create inline tables by typing data manually into the script, rather than by connecting to files and databases. Use the required syntax to indicate that the script text is to be interpreted as inline data. Data added with inline loads will be contained in the application if the application is exported. Inline tables are readable and editable within the load script.

A basic inline load creates a table, and inserts the data fields and records.

Inline load in data load editor

![Inline load in data load editor.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_inline_load-qcs-rev.png)

## Basic syntax example

The following script contains a simple inline load.

```
MyTable:
Load * Inline [
Country, Year, Sales
Argentina, 2014, 66295.03
Argentina, 2015, 140037.89
Austria, 2014, 54166.09
Austria, 2015, 182739.87
];
```

The following syntax is used for the above inline load:

- Load \* Inline instructs Qlik Sense to load all fields from the inline table that follows.
- MyTable: defines the name of the table. The list of tables in the application can be accessed from [Data model viewer](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#glossary-1 "Glossary term") and other areas.
- Square brackets enclose the data.
- The first line of the load statement defines the data fields.
- Commas separate data fields and records.
- A semi-colon closes the load statement.

## Loading an inline table

Do the following:

1. In an application, open Data load editor.
2. In a new line, define the table using the required syntax.

   [*Basic syntax example*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#BasicSyntax)
3. When done, click **Load data**.

## Why use inline loads?

Inline loads can be helpful in a number of use cases:

- Administering and editing data without needing to connect to external sources.
- Supplementing existing data in the data model. For example, you could add an additional table to a data model that mostly comes from database sources.
- Adding data that you would like to avoid continuously loading from external sources. This can save time if you know the data source might change in the future, but the data values will remain the same.
- Ease-of-use for copying and pasting content into the script from other files. For example, .csv files or tables from word processor documents.
- Creating test scripts that can be copied and pasted quickly.

## Syntax overview

### Naming the table

You can add a name for the inline table, as you would for other loaded tables. Defining the table name is optional.

After the name of the table, insert a colon.

### LOAD and inline statements

An inline table is loaded with the inline clause when you use the LOAD script statement. The inline clause indicates that the subsequent text in the table will contain data that is manually typed into the editor. Unless you indicate otherwise, an inline table uses the txt format, which follows the structure of a delimited text file.

For more information about the LOAD statement, see [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm).

### Enclosures and data entry

Data entered through an inline
clause must be enclosed by specific characters. The following are accepted character combinations for enclosing the data:

- Square brackets: `[` and `]`
- Double quotation marks: `"` and `"`
- Single quotation marks: `'` and `'`
- Back ticks: `` ` `` and `` ` ``

The character you choose as an enclosure can help you load inline data that contains conflicting characters. For example, if your data contains records with square brackets, you can enclose it with quotation marks or back ticks instead.

For an example of alternative enclosures, see [*Example - Alternative data enclosures*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#ExDataEnc).

Unless you specify an alternative table format (default is txt), text between the enclosures is interpreted in the
same way as the content of a file. Hence, where you would insert a new
line in a text file, you should also do it in the text of an inline clause: by pressing the Enter key when typing the script.

### Ending the inline load

The end of the inline load statement is denoted with a semi-colon.

### Data transformations

In a simple inline load with no transformations, the number of columns are defined by the first line. There are three columns in the table loaded by the following example: `Product_ID`, `Supplier_Name`, and `Product_Category`.

```
Products:

Load * Inline [
Product_ID, Supplier_Name, Product_Category
1, Paracel, Home Decor
2, PageWave, Electronics
3, Talarian, Software
4, Userland, Appliances
];
```

You can also perform transformations and create new columns within the same inline table. You can use [preceding loads](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#glossary-3 "Glossary term"), and more than one LOAD statement can be used to load the same table.

For specific examples, see [*Examples - Inline loads with transformations*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#ExTransform).

### Configuring the format specification in an inline load

Like with other loaded tables, you can modify the format specification of the inline table using format specification items. The format specification is added in brackets. It should be added after the data enclosures, but before the semi-colon ending the LOAD statement. Some of the customizations you can add include:

- Changing the delimiter from a comma to another character. For examples, see [*Examples - Alternative delimiters*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#ExDelimiter).

  See: [*Delimiter is*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/delimiter.htm)
- Omitting table column headers. For an example, see [*Example - Omitting column headers*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#ExOmitLabels).

  See: [*Labels*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/labels.htm)
- Using another data format (for example, fixed record format). For an example, see [*Example - Loading another data type*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#ExChangeFormat).

  See: [*Table format*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-format.htm)

  > **Note:** Not all Table format options are supported for inline loads.
- Allowing multi-line content. For an example, see [*Example - Multi-line content*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#ExMultLine).

  See: [*Quotes*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/quotes.htm)

To use multiple format specification items in the same table, separate them with commas. For example: `(Delimiter is '|', no labels)`

For full details about the format specification, see [*Format specification items*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/format-specification-items.htm).

### Operators and other clauses

Additionally, since an inline load is a LOAD statement, you can combine other arguments for the LOAD statement into the inline load. For example, use the where or while clause to define whether to load a specific row or not, based on the text within it.

Similarly, you can also use operators outside of the text content itself. With operators, you can customize how you transform the inline data, and also define when to load certain data or not.

For a specific example, see [*Example - Operators for transformations and clauses*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#ExOpsAndClauses).

## Example - Alternative data enclosures

You can use square brackets, quotation marks, or back ticks to enclose an inline load. This section illustrates this with an example. For more information, see [*Enclosures and data entry*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#Enclosure).

Load script and results

This example demonstrates how you can use back ticks to enclose the inline data. The data in the example contains square bracket characters, which makes square brackets incompatible as enclosures for the LOAD statement.

Overview

Open the Data load editor and add the following load script to a new section.

Load script

```
DataTable:

Load * inline 
`
custom_property, date, amount
[11402], 1/1/2024, 92.99
[11403], 1/2/2024, 102.34
[11404], 1/3/2024, 50.26
[11405], 1/4/2024, 153.69
[11406], 1/5/2024, 75.62
`;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `custom_property`
- `date`
- `amount`

Results table

| custom\_property | date | amount |
| --- | --- | --- |
| [11402] | 1/1/2024 | 92.99 |
| [11403] | 1/2/2024 | 102.34 |
| [11404] | 1/3/2024 | 50.26 |
| [11405] | 1/4/2024 | 153.69 |
| [11406] | 1/5/2024 | 75.62 |

## Examples - Alternative delimiters

You can use a character other than a comma to delimit column values in the table. For more information, see [*Configuring the format specification in an inline load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#FormatSpec).

Load script and results

Overview

Exchanging the delimiter is useful when data in the table contains commas, which would otherwise signal the switch to the next column in the table.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Four tables to be loaded. They are as follows:

  - `Table1`: Delimiter is a vertical bar (pipe). The data in the `Phrase` column contains commas.
  - `Table2`: Delimiter is a colon.
  - `Table3`: Delimiter is a back slash.
  - `Table4`: The table is delimited by pressing the Tab key on the keyboard. This option is useful when you are copying a table from a word processor and pasting it into the script.

  `Table1` shows a practical use case for using an alternative delimiter. The other tables show more delimiter options.

Load script

```
Table1:
LOAD * INLINE [
ID|Phrase
1 | 'The transaction was complete, but the order has not yet shipped.'
2 | 'We need to confirm the following details: sales rep number, order status, and shipping priority.'
] (Delimiter is '|');

Table2:
LOAD * INLINE [
Num1:Chr1
1:A
2:B ] (Delimiter is ':');

Table3:
LOAD * INLINE [
Num2\Chr2
1\A
2\B ] (Delimiter is \\);

Table4:
LOAD * INLINE [
Num3	Chr3
1	A
2	B ] (Delimiter is '\t');
```

Results

Load the data and open a sheet. Create four tables and add the dimensions to them as follows:

- `Table1`: `ID`, `Phrase`
- `Table2`: `Num1`, `Chr1`
- `Table3`: `Num2`, `Chr2`
- `Table4`: `Num3`, `Chr3`

Results table: `Table1`

| ID | Phrase |
| --- | --- |
| 1 | The transaction was complete, but the order has not yet shipped. |
| 2 | We need to confirm the following details: sales rep number, order status, and shipping priority. |

Results table: `Table2`

| Num1 | Chr1 |
| --- | --- |
| 1 | A |
| 2 | B |

Results table: `Table3`

| Num2 | Chr2 |
| --- | --- |
| 1 | A |
| 2 | B |

Results table: `Table4`

| Num3 | Chr3 |
| --- | --- |
| 1 | A |
| 2 | B |

## Example - Mixing inline loads and loads from other data sources

Load script and results

Overview

The following script first loads a series of fields from a connector, then loads an inline table with a common field and an additional field. This new field provides another property about the row item that was not loaded through the data connection. Note that this only works smoothly when there is a single field name in common between the two tables. If there is more than one common field name, a [synthetic key](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#glossary-4 "Glossary term") is produced.

In this truncated example, we load a table of order details from a [data connection](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#glossary-5 "Glossary term"). Then, we use an inline table to add an additional field, `Supplemental Info`. This could, for example, contain details about special comments about specific order IDs.

Load script

```
SET DateFormat='MM/DD/YYYY';

Orders:

LIB CONNECT TO 'My_Generic_Connection';

LOAD PRODUCT_DIVISION_A_ORDER_ID as Order ID, 
PRODUCT_DIVISION_A_ORDER_DATE as ISSUE_KEY as Order Date, 
PRODUCT_DIVISION_A_TYPE as Product Type, 
PRODUCT_DIVISION_A_SALES_MANAGER as Manager,
PRODUCT_DIVISION_A_SHIPPED_STATUS as Shipped Status;

SELECT PRODUCT_DIVISION_A_ORDER_ID,
PRODUCT_DIVISION_A_ORDER_DATE,
PRODUCT_DIVISION_A_TYPE,
PRODUCT_DIVISION_A_SALES_MANAGER,
PRODUCT_DIVISION_A_SHIPPED_STATUS

FROM SourceTable
WITH PROPERTIES (

[...]

);

Orders_Inline_Info:
load * inline [
Order ID,Supplemental Info
PSF-001014,'Bulk order, pending deal with Paracel.'
PSF-001625,'NOTE: Product damaged. Investigation required.'
];
```

Results

After loading the data, let's say we add the following dimensions to a table:

- `Order ID`
- `Order Date`
- `Product Type`
- `Manager`
- `Shipped Status`
- `Supplemental Info`

The resulting chart could look like this.

Results table: `Orders`

| Order ID | Order Date | Product Type | Manager | Shipped Status | Supplemental Info |
| --- | --- | --- | --- | --- | --- |
| PSF-000998 | 1/13/2024 | Electronics | Amanda Honda | Shipped | - |
| PSF-000999 | 1/15/2024 | Automotive | Molly McKenzie | Not Shipped | - |
| PSF-001014 | 1/17/2024 | Home Appliances | Amalia Craig | Undefined | Bulk order, pending deal with Paracel. |
| PSF-001625 | 1/21/2024 | Electronics | Amanda Honda | Undefined | Product damaged. Investigation required. |

Note how all fields from both tables can be added to the same [visualization](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#glossary-6 "Glossary term"). The tables are associated to each other in the data model.

## Example - Omitting column headers

Edit the format specification to load an inline table without defining column headers. This is done with the labels specification (setting it to a value of `no labels`). For more information, see [*Configuring the format specification in an inline load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#FormatSpec).

When you load a table without defining column names, system-defined column names are automatically used.

Load script and results

Overview

This example demonstrates how you can load an inline table without defining column names.

Open the Data load editor and add the following load script to a new section.

Load script

```
Expenses:

Load * inline
[
1,Category1,40566.49
2,Category2,3504.54
3,Category3,593206.30
] (no labels);
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- @1
- @2
- @3

Results table

| @1 | @2 | @3 |
| --- | --- | --- |
| 1 | Category1 | 40566.49 |
| 2 | Category2 | 3504.54 |
| 3 | Category3 | 593206.30 |

## Example - Loading another data type

This example demonstrates how you can load an inline table in fixed record format. See [*Configuring the format specification in an inline load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#FormatSpec).

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- An inline load statement defining the table `DataTable`.
- The use of fix (as part of the Table format specification) to indicate that the data to load is in fixed record format.

Load script

```
DataTable:
LOAD
"@1:4",
"@5:8",
"@9:12",
"@13:16"
INLINE [
a   b   c   d
1   2   3   4
x   y   z   w
] (fix, utf8, embedded labels);
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `a`
- `b`
- `c`
- `d`

Results table

| a | b | c | d |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |
| x | y | z | w |

## Example - Multi-line content

This example demonstrates how you can enter multi-line field content into an inline table. See [*Configuring the format specification in an inline load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#FormatSpec).

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A simple inline load to define the table `T1`.
- Use of the Quotes specifier (with the value `msq`) to support multi-line content.
- Length values specified in feet and inches.
- The double quotation mark symbol (") indicates the end of a multi-line entry. In this example, the same symbol is also used to denote the inch values. This is done to show the syntax and resulting behavior if you need to use both in the same LOAD statement. Essentially, entering the " symbol for two consecutive characters ("") indicates the code is to be interpreted as a single text instance of the symbol.

Load script

```
T1:
Load *, recno() as ID inline [
Length
"1' 2""
22' 10"""
14' 8"  ] (msq);
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ID`
- `Length`

To view multi-line content as intended, The **Wrap text in cells** setting must be turned on in the properties panel. Additionally, the application theme (or [visualization](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#glossary-7 "Glossary term") settings) must allow for the sufficient **Row height (in lines)**.

Results table

| ID | Length |
| --- | --- |
| 1 | 1' 2"  22' 10" |
| 2 | 14' 8" |

In the above table, the record with an `ID` value of 1 contains multi-line content.

## Examples - Inline loads with transformations

These examples show how you can perform calculations on fields loaded inline to create new fields in the data model.

For more information, see [*Data transformations*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#Transform).

Example: Simple renaming of a field

Overview

Open the Data load editor and add the following load script to a new section.

Load script

```
ORDERS:

Load Original as Updated,
* Inline
[
Original
ProductA
ProductB
ProductC
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `Original`
- `Updated`

Results table

| Original | Updated |
| --- | --- |
| ProductA | ProductA |
| ProductB | ProductB |
| ProductC | ProductC |

Example: Simple insertion of an ID field

Overview

This example shows how you can define a calculated field to indicate the ID of each data row, without manually typing each ID value.

Open the Data load editor and add the following load script to a new section.

Load script

```
ORDERS:

Load RowNo() as ID,
* Inline
[
ProductName
A
B
C
D
E
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ID`
- `ProductName`

Results table

| ID | ProductName |
| --- | --- |
| 1 | A |
| 2 | B |
| 3 | C |
| 4 | D |
| 5 | E |

Example: Configuring LOAD statements to handle transformations

Overview

This example shows several ways in which a simple transformation can be applied to inline data. You can use one or multiple LOAD statements, and configure the syntax in different ways, to define whether or not a transformation replaces the original [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#glossary-8 "Glossary term") or if both original and new fields are loaded.

In particular, note the variations in the following and how they affect the output:

- Number of LOAD statements within the table.
- Presence or absence of `*` symbol (loads all subsequent fields).
- Presence or absence of commas (`,` symbol).

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Four tables, all of which reference the same data. The field names are different.

  - `DerivedYears1`: Uses two LOAD statements to load an inline column and a column containing a transformation of the inline column.
  - `DerivedYears2`: Uses two LOAD statements. The script loads an inline column, then loads a calculated field transformed from the original column. With the second LOAD statement, the original column is not loaded into the table, effectively making the new field a replacement of the original field.
  - `DerivedYears3`: Uses a single LOAD statement to load both the original inline column and a transformed column.
  - `DerivedYears4`: Uses a single LOAD statement to define an inline field and a transformation of that original field. Only the transformed field is loaded into the table.

Load script

```
DerivedYears1:

Load *,
Year(initial_date1) as derived_year1
;
    
Load
* inline [
initial_date1
'1/1/2022'
'1/1/2023'
'1/1/2024'
];

DerivedYears2:

Load
Year(initial_date2) as derived_year2
;
    
Load
* inline [
initial_date2
'1/1/2022'
'1/1/2023'
'1/1/2024'
];

DerivedYears3:

Load Year(initial_date3) as derived_year3,
* inline [
initial_date3
'1/1/2022'
'1/1/2023'
'1/1/2024'
];

DerivedYears4:

Load Year(initial_date4) as derived_year4
inline [
initial_date4
'1/1/2022'
'1/1/2023'
'1/1/2024'
];
```

Results

Load the data and open a sheet. Create three tables and add the [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#glossary-9 "Glossary term") to them as follows:

- `DerivedYears1`: `initial_date1`, `derived_year1`
- `DerivedYears2`: `initial_date2`
- `DerivedYears3`: `initial_date3`, `derived_year3`

Results table: `DerivedYears1`

| initial\_date1 | derived\_year1 |
| --- | --- |
| 1/1/2022 | 2022 |
| 1/1/2023 | 2023 |
| 1/1/2024 | 2024 |

Results table: `DerivedYears2`

| derived\_year2 |
| --- |
| 2022 |
| 2023 |
| 2024 |

Results table: `DerivedYears3`

| initial\_date3 | derived\_year3 |
| --- | --- |
| 1/1/2022 | 2022 |
| 1/1/2023 | 2023 |
| 1/1/2024 | 2024 |

Results table: `DerivedYears4`

| derived\_year4 |
| --- |
| 2022 |
| 2023 |
| 2024 |

Example: Modifying field content

Overview

Suppose you are pasting information from a large text file into the script editor, but want to perform additional processing on the records in the dataset. For example, you want to remove certain characters and prefixes, and capitalize each word.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- An inline table, `Transformations`, in which a transformation is defined to change text content of a field. The text being transformed is added after this.
- Two LOAD statements. With the configuration in the example, only the derived field `ProductName_Trimmed` is loaded into the table.

Load script

```
Transformations:

Load 
Capitalize(TextBetween(OrigColumn, '{','}')) as ProductName_Trimmed;

Load * inline [
OrigColumn
Product: {soft drinks and other beverages}
Product:  {snack food}
Product: {electronics and video games}
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: `ProductName_Trimmed`.

Results table

| ProductName\_Trimmed |
| --- |
| Soft Drinks And Other Beverages |
| Snack Food |
| Electronics And Video Games |

## Example - Operators for transformations and clauses

You can use operators to define transformations and specific clauses in the LOAD statement. For more information, see [*Operators and other clauses*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm#OpsAndClauses).

[*Operators*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Operators/operators.htm)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A simple inline load to define the table `Purchases`.
- The insertion of a calculated field, `OrderSize`. This field is a transformation of the `amount` field from the inline dataset. It categorizes purchases as small or large, depending on whether or not the amount surpasses $2000.00.
- A where clause that prevent records from being loaded when the `amount` is less than $0.05.

Load script

```
Purchases:

Load
If(amount<2000,'Small Purchase','Large Purchase') as OrderSize,

* inline
[
ID, amount
1,2660.39
2,100.01
3,500.42
4,5023.99
5,0.04
6,2002.39
7,31034.53
8,1643.58
9,3993.65
10,614.34
11,675.93
]
WHERE
amount>0.05
;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ID`
- `amount`
- `OrderSize`

Results table

| ID | amount | OrderSize |
| --- | --- | --- |
| 1 | 2660.39 | Large Purchase |
| 2 | 100.01 | Small Purchase |
| 3 | 500.42 | Small Purchase |
| 4 | 5023.99 | Large Purchase |
| 6 | 2002.39 | Large Purchase |
| 7 | 31034.53 | Large Purchase |
| 8 | 1643.58 | Small Purchase |
| 9 | 3993.65 | Large Purchase |
| 10 | 614.34 | Small Purchase |
| 11 | 675.93 | Small Purchase |

In the above table, the transaction with an `ID` of 5 was not loaded into the table. This is because the `amount` value is less than $0.05.

## Example - Creating null values in an inline table

This example demonstrates how you can use the NullInterpret variable to create null values in your inline data.

[*NullInterpret*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ValueHandlingVariables/NullInterpret.htm)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A simple inline load to define the table `T2`.
- The NullInterpret variable defined as two single quotation marks. When the script is loaded, records containing this value are processed as null values.

Load script

```
set nullinterpret = '';
T2:
Load * inline [
Test
''
x ];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: `Test`.

Results table

| Test |
| --- |
| x |

In the above table, the first record is a null value. Therefore, it is not included in the visualization. Null values existing in tables with additional dimensions would be denoted with a `-` symbol.

## More examples

For additional examples, see [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm).

Related learning:

- [Introduction to the data load editor](https://help.qlik.com/lnk/Intro_Data_Load_Editor_QS)

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
- [*Format specification items*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/format-specification-items.htm)
- [Introduction to the data load editor](https://help.qlik.com/lnk/Intro_Data_Load_Editor_QS)
