---
title: "addmonths Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addmonths.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# addmonths Script and chart function

This function returns the date occurring n months after startdate or, if
n is negative, the date occurring
n months before startdate.

Syntax:

AddMonths(startdate, n
, [ , mode])

Return data type:  dual

The `addmonths()` function adds or subtracts a defined number of months, `n`, from a `startdate` and returns the resultant date.

The `mode` argument will impact `startdate` values on or after the 28th of the month. By setting the `mode` argument to 1, the `addmonths()` function returns a date that is equal in relative distance to the end of the month as the `startdate`.

Example diagram of `addmonths()` function

![Example diagram showing how the various components of the addmonths function come together to produce an output date.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-addmonths-overview.png)

For example, February 28 is the last day of the month. If the `addmonths()` function, with a `mode` of 1, is used to return the date two months later, the function will return the last date of April, April 30.

Example diagram of `addmonths()` function, with `mode=1`

![Example diagram showing how the 'mode' argument can be altered to change the output date of the addmonths function.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-addmonths-overview-n-mode-arguments.png)

Arguments

| Argument | Description |
| --- | --- |
| startdate | The start date as a time stamp, for example '2012-10-12'. |
| n | Number of months as a positive or negative integer. |
| mode | Specifies if the month is added relative to the beginning or to the end of the month. Default mode is 0 for additions relative to the beginning of the month. Set mode to 1 for additions relative to the end of the month. When mode is set to 1 and the input date is the 28th or above, the function checks how many days are left to reach the end of the month on the startdate. The same number of days to reach the end of the month are set on the date returned. |

## When to use addmonths

The `addmonths()` function will commonly be used in an expression to find a date a given number of months before or after a period of time.

For example, the `addmonths()` function can be used to identify the end date of mobile phone contracts.

Function examples

| Example | Result |
| --- | --- |
| `addmonths ('01/29/2003' ,3)` | Returns '04/29/2003'. |
| `addmonths ('01/29/2003',3,0)` | Returns '04/29/2003'. |
| `addmonths ('01/29/2003',3,1)` | Returns '04/28/2003'. |
| `addmonths ('01/29/2003',1,0)` | Returns '02/28/2003'. |
| `addmonths ('01/29/2003',1,1)` | Returns '02/26/2003'. |
| `addmonths ('02/28/2003',1,0)` | Returns '03/28/2003'. |
| `addmonths ('02/28/2003',1,1)` | Returns '03/31/2003'. |
| `addmonths ('01/29/2003',-3)` | Returns '10/29/2002'. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addmonths.htm#glossary-0 "Glossary term") containing a set of transactions between 2020 and 2022, which is loaded into a table called `Transactions`.
- The date [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addmonths.htm#glossary-1 "Glossary term") provided in the `DateFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addmonths.htm#glossary-2 "Glossary term") (MM/DD/YYYY) format.
- The creation of a field, `two_months_later`, that returns the date for two months after the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        addmonths(date,2) as two_months_later
        ;
Load
*
Inline 
[
id,date,amount
8188,'01/10/2020',37.23
8189,'02/28/2020',17.17
8190,'04/09/2020',88.27
8191,'04/16/2020',57.42
8192,'05/21/2020',53.80
8193,'08/14/2020',82.06
8194,'10/07/2020',40.39
8195,'12/05/2020',87.21
8196,'01/22/2021',95.93
8197,'02/03/2021',45.89
8198,'03/17/2021',36.23
8199,'04/23/2021',25.66
8200,'05/04/2021',82.77
8201,'06/30/2021',69.98
8202,'07/26/2021',76.11
8203,'12/27/2021',25.12
8204,'02/02/2022',46.23
8205,'02/26/2022',84.21
8206,'03/07/2022',96.24
8207,'03/11/2022',67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `two_months_later`

Results table

| date | two\_months\_later |
| --- | --- |
| 01/10/2020 | 03/10/2020 |
| 02/28/2020 | 04/28/2020 |
| 04/09/2020 | 06/09/2020 |
| 04/16/2020 | 06/16/2020 |
| 05/21/2020 | 07/21/2020 |
| 08/14/2020 | 10/14/2020 |
| 10/07/2020 | 12/07/2020 |
| 12/05/2020 | 02/05/2021 |
| 01/22/2021 | 03/22/2021 |
| 02/03/2021 | 04/03/2021 |
| 03/17/2021 | 05/17/2021 |
| 04/23/2021 | 06/23/2021 |
| 05/04/2021 | 07/04/2021 |
| 06/30/2021 | 08/30/2021 |
| 07/26/2021 | 09/26/2021 |
| 12/27/2021 | 02/27/2022 |
| 02/02/2022 | 04/02/2022 |
| 02/26/2022 | 04/26/2022 |
| 03/07/2022 | 05/07/2022 |
| 03/11/2022 | 05/11/2022 |

The `two_months_later` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addmonths.htm#glossary-3 "Glossary term") statement by using the `addmonths()` function. The first argument provided identifies which date is being evaluated. The second argument is the number of months to add or subtract from the `startdate`. In this instance, the value of 2 is provided.

Diagram of `addmonths()` function, example with no additional arguments

![Diagram of addmonths function showing how Transaction 8193 from the load script is converted from an input date to a resulting output date. This example contains no additional arguments.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-addmonths-examples-no-add-arg.png)

Transaction 8193 took place on August 14. Therefore, the `addmonths()` function returns October 14, 2020 for the `two_months_later` field.

## Example 2 – Relative month end

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of month-end transactions in 2022, which is loaded into a table called `Transactions`.
- The date field provided in the `DateFormat` system variable (MM/DD/YYYY) format.
- The creation of a field, `relative_two_months_prior`, that returns the relative month-end date for two months before the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        addmonths(date,-2,1) as relative_two_months_prior
        ;
Load
*
Inline 
[
id,date,amount
8188,'01/28/2022',37.23
8189,'01/31/2022',57.54
8190,'02/28/2022',17.17
8191,'04/29/2022',88.27
8192,'04/30/2022',57.42
8193,'05/31/2022',53.80
8194,'08/14/2022',82.06
8195,'10/07/2022',40.39
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `relative_two_months_prior`

Results table

| date | relative\_two\_months\_prior |
| --- | --- |
| 01/28/2022 | 11/27/2021 |
| 01/31/2022 | 11/30/2021 |
| 02/28/2022 | 12/31/2021 |
| 04/29/2022 | 02/27/2022 |
| 04/30/2022 | 02/28/2022 |
| 05/31/2022 | 03/31/2022 |
| 08/14/2022 | 06/14/2022 |
| 10/07/2022 | 08/07/2022 |

The `relative_two_months_prior` field is created in the preceding load statement by using the `addmonths()` function. The first argument provided identifies which date is being evaluated. The second argument is the number of months to add or subtract from the `startdate`. In this instance, the value of -2 is provided. The final argument is the mode, with a value of 1, which forces the function to calculate the relative month-end date for all dates greater than or equal to 28.

Diagram of `addmonths()` function, example with `n=-2`

![Diagram of addmonths function showing how Transaction 8191 from the load script is converted from an input date to a resulting output date. This example uses a negative 'n' value to demonstrate the functionality.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-addmonths-examples-rel-mth-end.png)

Transaction 8191 takes place on April 29, 2022. Initially, two months prior would set the month to February. Then, due to the third argument of the function setting the mode to 1 and the day value being later than the 27th, the function calculates the relative month-end value. The function identifies that the 29th is the second last day of April and therefore returns the second last day of February, the 27th.

## Example 3– Chart object example

Load script and chart expression

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addmonths.htm#glossary-4 "Glossary term") and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addmonths.htm#glossary-5 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that returns the date for two months after the transaction took place is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addmonths.htm#glossary-6 "Glossary term") in a chart object.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline 
[
id,date,amount
8188,'01/10/2020',37.23
8189,'02/28/2020',17.17
8190,'04/09/2020',88.27
8191,'04/16/2020',57.42
8192,'05/21/2020',53.80
8193,'08/14/2020',82.06
8194,'10/07/2020',40.39
8195,'12/05/2020',87.21
8196,'01/22/2021',95.93
8197,'02/03/2021',45.89
8198,'03/17/2021',36.23
8199,'04/23/2021',25.66
8200,'05/04/2021',82.77
8201,'06/30/2021',69.98
8202,'07/26/2021',76.11
8203,'12/27/2021',25.12
8204,'02/02/2022',46.23
8205,'02/26/2022',84.21
8206,'03/07/2022',96.24
8207,'03/11/2022',67.67
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: `date`.

Create the following measure:

`=addmonths(date,2)`

Results table

| date | =addmonths(date,2) |
| --- | --- |
| 01/10/2020 | 03/10/2020 |
| 02/28/2020 | 04/28/2020 |
| 04/09/2020 | 06/09/2020 |
| 04/16/2020 | 06/16/2020 |
| 05/21/2020 | 07/21/2020 |
| 08/14/2020 | 10/14/2020 |
| 10/07/2020 | 12/07/2020 |
| 12/05/2020 | 02/05/2021 |
| 01/22/2021 | 03/22/2021 |
| 02/03/2021 | 04/03/2021 |
| 03/17/2021 | 05/17/2021 |
| 04/23/2021 | 06/23/2021 |
| 05/04/2021 | 07/04/2021 |
| 06/30/2021 | 08/30/2021 |
| 07/26/2021 | 09/26/2021 |
| 12/27/2021 | 02/27/2022 |
| 02/02/2022 | 04/02/2022 |
| 02/26/2022 | 04/26/2022 |
| 03/07/2022 | 05/07/2022 |
| 03/11/2022 | 05/11/2022 |

The `two_months_later` measure is created in the chart object by using the `addmonths()` function. The first argument provided identifies which date is being evaluated. The second argument is the number of months to add or subtract from the `startdate`. In this instance, the value of 2 is provided.

Diagram of `addmonths()` function, chart object example

![Diagram of addmonths function showing how Transaction 8193 from the load script is converted from an input date to a resulting output date. This example uses a chart object to obtain the result.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-addmonths-examples-chart-object.png)

Transaction 8193 took place on August 14. Therefore, the `addmonths()` function returns the October 14, 2020 for the `two_months_later` field.

## Example 4 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called `Mobile_Plans`.
- Information with the contract ID, start date, contract length, and monthly fee.

The end user would like a chart object that displays, by contract ID, the termination date of each phone contract.

Load script

```
Mobile_Plans:
Load
*
Inline 
[
contract_id,start_date,contract_length,monthly_fee
8188,'01/13/2020',18,37.23
8189,'02/26/2020',24,17.17
8190,'03/27/2020',36,88.27
8191,'04/16/2020',24,57.42
8192,'05/21/2020',24,53.80
8193,'08/14/2020',12,82.06
8194,'10/07/2020',18,40.39
8195,'12/05/2020',12,87.21
8196,'01/22/2021',12,95.93
8197,'02/03/2021',18,45.89
8198,'03/17/2021',24,36.23
8199,'04/23/2021',24,25.66
8200,'05/04/2021',12,82.77
8201,'06/30/2021',12,69.98
8202,'07/26/2021',12,76.11
8203,'12/27/2021',36,25.12
8204,'06/06/2022',24,46.23
8205,'07/18/2022',12,84.21
8206,'11/14/2022',12,96.24
8207,'12/12/2022',18,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `contract_id`
- `start_date`
- `contract_length`

Create the following measure to calculate the end date of each contract:

`=addmonths(start_date,contract_length, 0)`

Results table

| contract\_id | start\_date | contract\_length | =addmonths(start\_date,contract\_length,0) |
| --- | --- | --- | --- |
| 8188 | 01/13/2020 | 18 | 07/13/2021 |
| 8189 | 02/26/2020 | 24 | 02/26/2022 |
| 8190 | 03/27/2020 | 36 | 03/27/2023 |
| 8191 | 04/16/2020 | 24 | 04/16/2022 |
| 8192 | 05/21/2020 | 24 | 05/21/2022 |
| 8193 | 08/14/2020 | 12 | 08/14/2021 |
| 8194 | 10/07/2020 | 18 | 04/07/2022 |
| 8195 | 12/05/2020 | 12 | 12/05/2021 |
| 8196 | 01/22/2021 | 12 | 01/22/2022 |
| 8197 | 02/03/2021 | 18 | 08/03/2022 |
| 8198 | 03/17/2021 | 24 | 03/17/2023 |
| 8199 | 04/23/2021 | 24 | 04/23/2023 |
| 8200 | 05/04/2021 | 12 | 05/04/2022 |
| 8201 | 06/30/2021 | 12 | 06/30/2022 |
| 8202 | 07/26/2021 | 12 | 07/26/2022 |
| 8203 | 12/27/2021 | 36 | 12/27/2024 |
| 8204 | 06/06/2022 | 24 | 06/06/2024 |
| 8205 | 07/18/2022 | 12 | 07/18/2023 |
| 8206 | 11/14/2022 | 12 | 11/14/2023 |
| 8207 | 12/12/2022 | 18 | 06/12/2024 |
