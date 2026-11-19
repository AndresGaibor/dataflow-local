---
title: "addyears Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addyears.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# addyears Script and chart function

This function returns the date occurring n years after startdate or, if
n is negative, the date occurring
n years before startdate.

Syntax:

AddYears(startdate, n)

Return data type:  dual

Example diagram of `addyears()` function

![Example diagram showing how the various components of the addyears function come together to produce an output date.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-addyears_overview.png)

The `addyears()` function adds or subtracts a defined number of years, `n`, from a `startdate`. It then returns the resulting date.

Arguments

| Argument | Description |
| --- | --- |
| startdate | The start date as a time stamp, for example '2012-10-12'. |
| n | Number of years as a positive or negative integer. |

Function examples

| Example | Result |
| --- | --- |
| `addyears ('01/29/2010',3)` | Returns '01/29/2013'. |
| `addyears ('01/29/2010',-1)` | Returns '01/29/2009'. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – Simple example

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addyears.htm#glossary-0 "Glossary term") containing a set of transactions between 2020 and 2022, which is loaded into a table called `Transactions`.
- The date [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addyears.htm#glossary-1 "Glossary term") provided in the `DateFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addyears.htm#glossary-2 "Glossary term") (MM/DD/YYYY) format.
- The creation of a field, `two_years_later`, that returns the date for two years after the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        addyears(date,2) as two_years_later
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
- `two_years_later`

Results table

| date | two\_years\_later |
| --- | --- |
| 01/10/2020 | 01/10/2022 |
| 02/28/2020 | 02/28/2022 |
| 04/09/2020 | 04/09/2022 |
| 04/16/2020 | 04/16/2022 |
| 05/21/2020 | 05/21/2022 |
| 08/14/2020 | 08/14/2022 |
| 10/07/2020 | 10/07/2022 |
| 12/05/2020 | 12/05/2022 |
| 01/22/2021 | 01/22/2023 |
| 02/03/2021 | 02/03/2023 |
| 03/17/2021 | 03/17/2023 |
| 04/23/2021 | 04/23/2023 |
| 05/04/2021 | 05/04/2023 |
| 06/30/2021 | 06/30/2023 |
| 07/26/2021 | 07/26/2023 |
| 12/27/2021 | 12/27/2023 |
| 02/02/2022 | 02/02/2024 |
| 02/26/2022 | 02/26/2024 |
| 03/07/2022 | 03/07/2024 |
| 03/11/2022 | 03/11/2024 |

The `two_years_later` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addyears.htm#glossary-3 "Glossary term") statement by using the `addyears()` function. The first argument provided identifies which date is being evaluated. The second argument is the number of years to add or subtract from the start date. In this instance, the value of 2 is provided.

Diagram of `addyears()` function, basic example

![Diagram of addyears function showing how Transaction 8193 from the load script is converted from an input date to a resulting output date.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-addyears-examples-basic.png)

Transaction 8193 took place on August 14, 2020. Therefore, the `addyears()` function returns August 14, 2022 for the `two_years_later` field.

## Example 2 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions between 2020 and 2022, which is loaded into a table called `Transactions`.
- The date field provided in the `DateFormat` system variable (MM/DD/YYYY) format.

In a chart object, create a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addyears.htm#glossary-4 "Glossary term"), `prior_year_date`, that returns the date one year prior to when the transaction takes place.

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

Create the following measure to calculate the date one year prior to each transaction:

`=addyears(date,-1)`

Results table

| date | =addyears(date,-1) |
| --- | --- |
| 01/10/2020 | 01/10/2019 |
| 02/28/2020 | 02/28/2019 |
| 04/09/2020 | 04/09/2019 |
| 04/16/2020 | 04/16/2019 |
| 05/21/2020 | 05/21/2019 |
| 08/14/2020 | 08/14/2019 |
| 10/07/2020 | 10/07/2019 |
| 12/05/2020 | 12/05/2019 |
| 01/22/2021 | 01/22/2020 |
| 02/03/2021 | 02/03/2020 |
| 03/17/2021 | 03/17/2020 |
| 04/23/2021 | 04/23/2020 |
| 05/04/2021 | 05/04/2020 |
| 06/30/2021 | 06/30/2020 |
| 07/26/2021 | 07/26/2020 |
| 12/27/2021 | 12/27/2020 |
| 02/02/2022 | 02/02/2021 |
| 02/26/2022 | 02/26/2021 |
| 03/07/2022 | 03/07/2021 |
| 03/11/2022 | 03/11/2021 |

The `one_year_prior` measure is created in the chart object by using the `addyears()` function. The first argument provided identifies which date is being evaluated. The second argument is the number of years to add or subtract from the `startdate`. In this instance, the value of -1 is provided.

Diagram of `addyears()` function, chart object example

![Diagram of addyears function showing how Transaction 8193 from the load script is converted from an input date to a resulting output date. This example uses a chart object to obtain the result.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-addyears-examples-chart-object.png)

Transaction 8193 took place on August 14. Therefore, the `addyears()` function returns August 14, 2019 for the `one_year_prior` field.

## Example 3 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called `Warranties`.
- Information with the product ID, purchase date, warranty length, and purchase price.

The end user would like a chart object that displays, by product ID, the warranty termination date of each product.

Load script

```
Warranties:
Load
*
Inline 
[
product_id,purchase_date,warranty_length,purchase_price
8188,'01/13/2020',4,32000
8189,'02/26/2020',2,28000
8190,'03/27/2020',3,41000
8191,'04/16/2020',4,17000
8192,'05/21/2020',2,25000
8193,'08/14/2020',1,59000
8194,'10/07/2020',2,12000
8195,'12/05/2020',3,12000
8196,'01/22/2021',4,24000
8197,'02/03/2021',1,50000
8198,'03/17/2021',2,80000
8199,'04/23/2021',3,10000
8200,'05/04/2021',4,30000
8201,'06/30/2021',3,30000
8202,'07/26/2021',4,20000
8203,'12/27/2021',4,10000
8204,'06/06/2022',2,25000
8205,'07/18/2022',1,32000
8206,'11/14/2022',1,30000
8207,'12/12/2022',4,22000
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `product_id`
- `purchase_date`
- `warranty_length`

Create the following measure to calculate the end date of each product's warranty:

`=addyears(purchase_date,warranty_length)`

Results table

| product\_id | purchase\_date | warranty\_length | =addyears(purchase\_date,warranty\_length) |
| --- | --- | --- | --- |
| 8188 | 01/13/2020 | 4 | 01/13/2024 |
| 8189 | 02/26/2020 | 2 | 02/26/2022 |
| 8190 | 03/27/2020 | 3 | 03/27/2023 |
| 8191 | 04/16/2020 | 4 | 04/16/2024 |
| 8192 | 05/21/2020 | 2 | 05/21/2022 |
| 8193 | 08/14/2020 | 1 | 08/14/2021 |
| 8194 | 10/07/2020 | 2 | 10/07/2022 |
| 8195 | 12/05/2020 | 3 | 12/05/2023 |
| 8196 | 01/22/2021 | 4 | 01/22/2025 |
| 8197 | 02/03/2021 | 1 | 02/03/2022 |
| 8198 | 03/17/2021 | 2 | 03/17/2023 |
| 8199 | 04/23/2021 | 3 | 04/23/2024 |
| 8200 | 05/04/2021 | 4 | 05/04/2025 |
| 8201 | 06/30/2021 | 3 | 06/30/2024 |
| 8202 | 07/26/2021 | 4 | 07/26/2025 |
| 8203 | 12/27/2021 | 4 | 12/27/2025 |
| 8204 | 06/06/2022 | 2 | 06/06/2024 |
| 8205 | 07/18/2022 | 1 | 07/18/2023 |
| 8206 | 11/14/2022 | 1 | 11/14/2023 |
| 8207 | 12/12/2022 | 4 | 12/12/2026 |
