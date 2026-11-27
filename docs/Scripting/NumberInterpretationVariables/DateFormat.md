---
title: "DateFormat"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DateFormat.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---

# DateFormat

Expand/Collapse all

# DateFormat

This environment [variable](#glossary-0 "Glossary term") defines the date format used as the default in the application and by date returning functions like date() and date#(). The format is used to interpret and format dates. If the variable is not defined, the date format set by your regional settings is fetched when the script runs.

Syntax:

DateFormat

DateFormat Function examples

| Example | Result |
| --- | --- |
| Set DateFormat='M/D/YY'; //(US format) | This use of the DateFormat function defines the date as the US format, month/day/year. |
| Set DateFormat='DD/MM/YY'; //(UK date format) | This use of the DateFormat function defines the date as the UK format, day/month/year. |
| Set DateFormat='YYYY/MM/DD'; //(ISO date format) | This use of the DateFormat function defines the date as the ISO format, year/month/day. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – System variables default

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-2 "Glossary term") of dates.
- The DateFormat function, which will use the US date format.

In this example, a dataset is loaded into a table named 'Transactions'. It includes a date [field](#glossary-3 "Glossary term"). The US DateFormat definition is used. This pattern will be used for implicit text to date conversion when the text dates are loaded.

Load script

```
Set DateFormat='MM/DD/YYYY';

Transactions:
LOAD
date,
month(date) as month,
id,
amount
INLINE
[
date,id,amount
01/01/2022,1,1000
02/01/2022,2,2123
03/01/2022,3,4124
04/01/2022,4,2431
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- month

Create this [measure](#glossary-4 "Glossary term"):

=sum(amount)

Results table

| date | month | =sum(amount) |
| --- | --- | --- |
| 01/01/2022 | Jan | 1000 |
| 02/01/2022 | Feb | 2123 |
| 03/01/2022 | Mar | 4124 |
| 04/01/2022 | Apr | 2431 |

The DateFormat definition MM/DD/YYYY is used for implicit conversion of text to dates, which is why the date field is properly interpreted as a date. The same format is used to display the date, as shown in the results table.

## Example 2 – Change system variable

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset from the previous example.
- The DateFormat function, which will use the ‘DD/MM/YYYY’ format.

Load script

```
SET DateFormat='DD/MM/YYYY';
Transactions:
LOAD
date,
month(date) as month,
id,
amount
INLINE
[
date,id,amount
01/01/2022,1,1000
02/01/2022,2,2123
03/01/2022,3,4124
04/01/2022,4,2431
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- month

Create this measure:

=sum(amount)

Results table

| date | month | =sum(amount) |
| --- | --- | --- |
| 01/01/2022 | Jan | 1000 |
| 02/01/2022 | Jan | 2123 |
| 03/01/2022 | Jan | 4124 |
| 04/01/2022 | Jan | 2431 |

Because the DateFormat definition was set to ‘DD/MM/YYYY’, you can see that the two digits after the first “/” symbol have been interpreted as the month, resulting in all records being from the month of January.

## Example 3 – Date interpretation

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset with dates in numerical format.
- The DateFormat variable, which will use the ‘DD/MM/YYYY’ format.
- The date() variable.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
date(numerical_date),
month(date(numerical_date)) as month,
id,
amount
Inline
[
numerical_date,id,amount
43254,1,1000
43255,2,2123
43256,3,4124
43258,4,2431
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- month

Create this measure:

=sum(amount)

Results table

| date | month | =sum(amount) |
| --- | --- | --- |
| 06/03/2022 | Jun | 1000 |
| 06/04/2022 | Jun | 2123 |
| 06/05/2022 | Jun | 4124 |
| 06/07/2022 | Jun | 2431 |

In the [load script](#glossary-5 "Glossary term"), you use the date() function to convert the numerical date into a date format. Because you do not provide a specified format as a second argument in the function, the DateFormat is used. This results in the date field using the format ‘MM/DD/YYYY’.

## Example 4 – Foreign date formatting

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of dates.
- The DateFormat variable, which uses the ‘DD/MM/YYYY' format but is uncommented by forward slashes.

Load script

```
// SET DateFormat='DD/MM/YYYY';

Transactions:
Load
date,
month(date) as month,
id,
amount
Inline
[
date,id,amount
22-05-2022,1,1000
23-05-2022,2,2123
24-05-2022,3,4124
25-05-2022,4,2431
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- month

Create this measure:

=sum(amount)

Results table

| date | month | =sum(amount) |
| --- | --- | --- |
| 22-05-2022 | - | 1000 |
| 23-05-2022 | - | 2123 |
| 24-05-2022 | - | 4124 |
| 25-05-2022 | - | 2431 |

In the initial load script, the DateFormat being used is the default ‘MM/DD/YYYY’. Because the date field in the transactions dataset is not in this format, the field is not interpreted as a date. This is shown in the results table where the month field values are null.

You can verify the interpreted data types in the [Data model viewer](#glossary-6 "Glossary term") by inspecting the date field’s “Tags” [properties](#glossary-7 "Glossary term").

Preview of the Transactions table. Note the “Tags” for the date field indicating that the textual input data has not been implicitly converted to a date/timestamp.

![Preview of the 'Transactions' table, with details of the 'date' field highlighted. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dmv_TransactionsTablePreview1.png "Click to view full size")

This can be solved by enabling the DateFormat system variable:

// SET DateFormat='DD/MM/YYYY';

Remove the double forward slashes and reload the data.

Preview of the Transactions table. Note the “Tags” for the date field indicating that the textual input data has been implicitly converted to a date/timestamp.

![Preview of the 'Transactions' table after modifying the DateFormat system variable. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dmv_TransactionsTablePreview2.png "Click to view full size")
