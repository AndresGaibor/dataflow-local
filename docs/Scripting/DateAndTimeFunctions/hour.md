---
title: "hour Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/hour.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# hour Script and chart function

This function returns an integer representing the hour when the fraction of the
expression is interpreted as a time
according to the standard number interpretation.

Syntax:

hour(expression)

Return data type:  integer

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| `hour( '09:14:36' )` | The text string supplied is implicitly converted to a timestamp as it matches the timestamp format defined in the TimestampFormat [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/hour.htm#glossary-0 "Glossary term"). The expression returns 9. |
| `hour( '0.5555' )` | The expression returns 13 ( Because 0.5555 = 13:19:55 ). |

## Example 1 – Variable (script)

Load script and results

Overview

Open the Data load editor and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/hour.htm#glossary-1 "Glossary term") below to a new tab.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/hour.htm#glossary-2 "Glossary term") containing transactions by timestamp
- The default `TimeStamp` system variable `(M/D/YYYY h:mm:ss[.fff] TT)`

Create a [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/hour.htm#glossary-3 "Glossary term") '`hour`', calculating when purchases took place.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';
						
Transactions: 			
  Load 
    *, 
    hour(date) as hour 
    ; 
Load 
* 
Inline  
[ 
id,date,amount 
9497,'2022-01-05 19:04:57',47.25, 
9498,'2022-01-03 14:21:53',51.75, 
9499,'2022-01-03 05:40:49',73.53, 
9500,'2022-01-04 18:49:38',15.35, 
9501,'2022-01-01 22:10:22',31.43, 
9502,'2022-01-05 19:34:46',13.24, 
9503,'2022-01-04 22:58:34',74.34, 
9504,'2022-01-06 11:29:38',50.00, 
9505,'2022-01-02 08:35:54',36.34, 
9506,'2022-01-06 08:49:09',74.23 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `hour`

Results table

| date | hour |
| --- | --- |
| 2022-01-01 22:10:22 | 22 |
| 2022-01-02 08:35:54 | 8 |
| 2022-01-03 05:40:49 | 5 |
| 2022-01-03 14:21:53 | 14 |
| 2022-01-04 18:49:38 | 18 |
| 2022-01-04 22:58:34 | 22 |
| 2022-01-05 19:04:57 | 19 |
| 2022-01-05 19:34:46 | 19 |
| 2022-01-06 08:49:09 | 8 |
| 2022-01-06 11:29:38 | 11 |

The values in the hour field are created by using the `hour()` function and passing the date as the expression in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/hour.htm#glossary-4 "Glossary term") statement.

## Example 2 – Chart object (chart)

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- The same dataset from the first example.
- The default `TimeStamp` system variable `(M/D/YYYY h:mm:ss[.fff] TT)`.

However, in this example, the dataset, unchanged, is loaded into the application. The ‘`hour`’ values are calculated via a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/hour.htm#glossary-5 "Glossary term") in a chart object.

Load Script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT'; 
			 
Transactions: 
Load 
* 
Inline  
[ 
id,date,amount 
9497,'2022-01-05 19:04:57',47.25, 
9498,'2022-01-03 14:21:53',51.75, 
9499,'2022-01-03 05:40:49',73.53, 
9500,'2022-01-04 18:49:38',15.35, 
9501,'2022-01-01 22:10:22',31.43, 
9502,'2022-01-05 19:34:46',13.24, 
9503,'2022-01-04 22:58:34',74.34, 
9504,'2022-01-06 11:29:38',50.00, 
9505,'2022-01-02 08:35:54',36.34, 
9506,'2022-01-06 08:49:09',74.23 
]; 
				
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: `date`.

To calculate the ‘`hour`’, create the following measure:

`=hour(date)`

Results table

| due\_date | =hour(date) |
| --- | --- |
| 2022-01-01 22:10:22 | 22 |
| 2022-01-02 08:35:54 | 8 |
| 2022-01-03 05:40:49 | 5 |
| 2022-01-03 14:21:53 | 14 |
| 2022-01-04 18:49:38 | 18 |
| 2022-01-04 22:58:34 | 22 |
| 2022-01-05 19:04:57 | 19 |
| 2022-01-05 19:34:46 | 19 |
| 2022-01-06 08:49:09 | 8 |
| 2022-01-06 11:29:38 | 11 |

The values for ‘`hour`’ are created by using the `hour()` function and passing the date as the expression in a measure for the chart object.
