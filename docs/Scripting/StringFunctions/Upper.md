---
title: "Upper Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Upper.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# Upper Script and chart function

Upper() converts all the characters in the input string to upper case for all text characters in the expression. Numbers and symbols are ignored.

Syntax:

Upper(text)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The string to evaluate. |

Example: Chart expression

| Example | Result |
| --- | --- |
| `Upper( ' abcD' )` | Returns `ABCD` |

## Example - Upper fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

A dataset which is loaded into a data table called `Example`.

- One field in the data table called `InputText`.

Load script

```
Example:
Load * inline [
InputText
rHode iSland
washingTon d.C.
new york
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `InputText`

Create the following calculated dimension:

- `=Upper(InputText)`, to convert all the characters in the `InputText` field to uppercase.

Results table

| InputText | Upper(InputText) |
| --- | --- |
| new york | NEW YORK |
| rHode iSland | RHODE ISLAND |
| washingTon d.C. | WASHINGTON D.C. |

The output of the `Upper` function converts all values to uppercase.

Load script

The following code shows how to use the function in a load script.

```
Load
String,Upper(String)
Inline
[String
rHode iSland
washingTon d.C.
new york];
```

Results table

| String | Upper(String) |
| --- | --- |
| rHode iSland | RHODE ISLAND |
| washingTon d.C. | WASHINGTON D.C. |
| new york | NEW YORK |

## Example - Upper scenario

Chart expression

Overview

A dataset contains ISO country codes and country names in various formats, such as all lowercase, all uppercase, or mixed case. The objective is to clean the data so that each country code and name are formatted to use uppercase.

Open the Data load editor and add the load script below to a new section.

The load script contains:

A dataset which is loaded into a data table called `Example`.

- The following fields in the data table:

  - `ISO CountryCode`
  - `CountryName`

Load script

```
Country:
Load  * inline [
​​ISO_CountryCode, CountryName
gbr, United kingdom
Ind, india
CAN, Canada
Are, United arab emirates
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ISO_CountryCode`
- CountryName

Create the following calculated dimensions:

- `=Upper(ISO_CountryCode)`, to create a column of country codes that use all uppercase characters.
- `=Upper(CountryName)`, to create a column of country names that use all uppercase characters.

Results table

| ISO\_CountryCode | CountryName | Upper(ISO\_CountryCode) | Upper(CountryName) |
| --- | --- | --- | --- |
| Are | United arab emirates | ARE | UNITED ARAB EMIRATES |
| CAN | Canada | CAN | CANADA |
| gbr | United Kingdom | GBR | UNITED KINGDOM |
| Ind | india | IND | INDIA |

The `Upper` function has converted all country codes and country names to use uppercase characters.

## Example - Upper advanced scenario

Chart expression

Overview

Using the same dataset as the previous scenario, this example combines country name and country code and formats these strings using the `Capitalize` and `Upper` functions.

Result

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ISO_CountryCode`
- `CountryName`

Create the following calculated dimension:

- `=Capitalize(CountryName) & ' (' & Upper(ISO_CountryCode) & ')'`, to create a new dimension that concatenates `CountryName` and `ISO_CountryCode` and formats the country names to use title case and the country codes to use uppercase.

Results table

| ISO\_CountryCode | CountryName | Capitalize(CountryName) & '(' & Upper(ISO\_CountryCode) & ')' |
| --- | --- | --- |
| Are | United arab emirates | United Arab Emirates (ARE) |
| CAN | Canada | Canada (CAN) |
| gbr | United Kingdom | United Kingdom (GBR) |
| Ind | india | India (IND) |
