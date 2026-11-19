---
title: "SubField Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/SubField.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# SubField Script and chart function

SubField() is used to extract substring components from a parent string field, where the original record fields consist of two or more parts separated by a delimiter.

The Subfield() function can be used, for example, to extract first name and surname from a list of records consisting of full names, the component parts of a path name, or for extracting data from comma-separated tables.

If you use the Subfield() function in a LOAD statement with the optional field\_no parameter left out, one full record will be generated for each substring. If several fields are loaded using Subfield() the Cartesian products of all combinations are created.

Syntax:

SubField(text,
delimiter[, field\_no ])

Return data type: string

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. This can be a hard-coded text, a [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/SubField.htm#glossary-0 "Glossary term"), a dollar-sign expansion, or another expression. |
| delimiter | A character within the input text that divides the string into component parts. |
| field\_no | The optional third argument is an integer that specifies which of the substrings of the parent string text is to be returned. Use the value 1 to return the first substring, 2 to return the second substring, and so on.   - If field\_no is a positive value, substrings are extracted from left to right. - If field\_no is a negative value, substrings are extracted from right to left. |

> **Tip:** 
> SubField() can be used instead of using complex combinations of functions such as Len(), Right(), Left(), Mid(), and other string functions.

Examples: Chart expressions

| Example | Result |
| --- | --- |
| `SubField( 'abc;cde;efg', ';' ,2 )` | Returns `cde` |
| `SubField( Null, ';' ,1 )` | Returns an empty string |
| `SubField( ';', ';' ,1 )` | Returns an empty string |
| `SubField( '\Users\ext_jrb\Documents\Qlik\Sense\Apps;','\',-3 )` | Returns `Qlik` |

## Example - SubField fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- One field in the data table called `Name`.

Load script

```
Example:
Load * inline [
Name
Dave Owen
Joe Tem
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `Name`

Create the following calculated dimensions:

- `=SubField(Name, ' ',1)`, to extract the first substring that appears before the space `' '` delimiter.
- `=SubField(Name, ' ',-1)`, to extract the first substring that appears before the space `' '` delimiter, starting from the right of the string.

Results table

| Name | SubField(Name, ' ',1) | SubField(Name, ' ',-1) |
| --- | --- | --- |
| Dave Owen | Dave | Owen |
| Joe Tem | Joe | Tem |

The `SubField()` function extracts the first substring of `Name` by setting the `field_no` argument to 1. Since the value of `field_no` is positive, a left to right order is followed for extracting the substring. A second function call extracts the second substring by setting the `field_no` argument to -1, which extracts the substring following a right to left order.

Load script

Load script

Open the Data load editor and add the following load script to a new section.

```
FullName:
LOAD * inline [
Name
'Dave Owen'
'Joe Tem'
];

SepNames:
Load Name,
SubField(Name, ' ',1) as FirstName,
SubField(Name, ' ',-1) as Surname
Resident FullName;
Drop Table FullName;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Name
- FirstName
- SurName

Results table

| Name | FirstName | SurName |
| --- | --- | --- |
| Dave Owen | Dave | Owen |
| Joe Tem | Joe | Tem |

Explanation

The `SubField` function extracts the first substring, `Name`, by setting the `field_no` argument to 1. Since the value of `field_no` is positive, a left to right order is followed for extracting the substring. A second function call extracts the second substring by setting the `field_no` argument to -1, which extracts the substring following a right to left order.

## Example - SubField scenario

Chart expression

Overview

A dataset of products contains a product table. Each product in the table has a tag field that identifies the product area. Products can have multiple values for the tag field. For example, Widget A has the following tags: Electronics, Gadgets, Home. Tag values are separated by the pipe (|) character as delimiter. This example shows you how to extract specific tag values using the `SubField` function.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ProductID`
  - `ProductName`
  - `Tags`
  - `Sales`

Load script

```
Example:
Load  *
INLINE [
ProductID, ProductName, Tags, Sales
1, Widget A, Electronics|Gadgets|Home, 150
2, Widget B, Electronics|Accessories, 200
3, Widget C, Furniture|Home, 100
4, Widget D, Gadgets|Accessories, 250
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ProductID`
- `ProductName`
- `Tags`

Create the following calculated dimensions:

- `=SubField(Tags, '|',1)`, to extract the first item in the `Tags` field.
- `=SubField(Tags, '|',2)`, to extract the second item in the `Tags` field.
- `=SubField(Tags, '|',3)`, to extract the third item in the `Tags` field.

Results table

| ProductID | ProductName | Tags | SubField(Tags, '|', 1) | SubField(Tags, '|', 2) | SubField(Tags, '|', 3) |
| --- | --- | --- | --- | --- | --- |
| 1 | Widget A | Electronics|Gadgets|Home | Electronics | Gadgets | Home |
| 2 | Widget B | Electronics|Accessories | Electronics | Accessories | - |
| 3 | Widget C | Furniture|Home | Furniture | Home | - |
| 4 | Widget D | Gadgets|Accessories | Gadgets | Accessories | - |

The output of the `SubField` functions has successfully returned the tags from the relevant positions in the original `Tags` string.

Load script

Load script

Open the Data load editor and add the following load script to a new section.

```
LOAD DISTINCT
Instrument,
SubField(Player,',') as Player,
SubField(Project,',') as Project;

Load * inline [
Instrument|Player|Project
Guitar|Neil,Mike|Music,Video
Guitar|Neil|Music,OST
Synth|Neil,Jen|Music,Video,OST
Synth|Jo|Music
Guitar|Neil,Mike|Music,OST
] (delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Instrument
- Player
- Project

Results table

| Instrument | Player | Project |
| --- | --- | --- |
| Guitar | Mike | Music |
| Guitar | Mike | Video |
| Guitar | Mike | OST |
| Guitar | Neil | Music |
| Guitar | Neil | Video |
| Guitar | Neil | OST |
| Synth | Jen | Music |
| Synth | Jen | Video |
| Synth | Jen | OST |
| Synth | Jo | Music |
| Synth | Neil | Music |
| Synth | Neil | Video |
| Synth | Neil | OST |

Explanation

This example shows how using multiple instances of the `Subfield()` function, each with the `field_no` parameter left out, from within the same `LOAD` statement creates Cartesian products of all combinations. The `DISTINCT` option is used to avoid creating duplicate records.
