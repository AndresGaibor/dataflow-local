---
title: "monthsname Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# monthsname Script and chart function

This function returns
a display value representing the range of the months of the period (formatted according
to the MonthNames script variable) as well as the year. The underlying numeric
value corresponds to a timestamp of the first millisecond of the month, bi-month, quarter, four-month period, or half-year containing a base date.

Syntax:

MonthsName(n\_months, date[, period\_no[, first\_month\_of\_year]])

Return data type:  dual

Diagram of monthsname function

![Example diagram showing the range of months  returned by the monthsname function, given a specific input date.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthsname-general.png)

The `monthsname()` function divides the year into segments based on the `n_months` agrument provided. It then evaluates the segment to which each provided `date` belongs, and returns the start and end month names of that segment, as well as the year. The function also provides the ability to return these boundaries from preceding or following segments, as well as redefining which is the first month of the year.

The following segments of the year are available in the function as `n_month` arguments:

Possible `n_month` arguments

| Periods | Number of months |
| --- | --- |
| month | 1 |
| bi-month | 2 |
| quarter | 3 |
| four months | 4 |
| half-year | 6 |

Arguments

| Argument | Description |
| --- | --- |
| n\_months | The number of months that defines the period. An integer or expression that resolves to an integer that must be one of: 1 (equivalent to the inmonth() function), 2 (bi-month), 3 (equivalent to the inquarter()function), 4 (four-month period), or 6 (half year). |
| date | The date or timestamp to evaluate. |
| period\_no | The period can be offset by period\_no, an integer, or expression resolving to an integer, where the value 0 indicates the period that contains base\_date. Negative values in period\_no indicate preceding periods and positive values indicate succeeding periods. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

## When to use monthsname

The `monthsname()` function is useful when you would like to provide the user with the functionality to compare aggregations by a period of their choosing. For example, you could provide an input [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm#glossary-0 "Glossary term") to let the user see the total sales of products by month, quarter, or half-year.

These dimensions can be created either in the load script by adding the function as a field in a Master Calendar table, or alternatively, by creating the dimension directly in a chart as a calculated dimension.

Function examples

| Example | Result |
| --- | --- |
| `monthsname(4, '10/19/2013')` | Returns 'Sep-Dec 2013.' In this and the other examples, the SET Monthnames statement is set to Jan;Feb;Mar, and so on. |
| `monthsname(4, '10/19/2013', -1)` | Returns 'May-Aug 2013'. |
| `monthsname(4, '10/19/2013', 0, 2)` | Returns 'Oct-Jan 2014', since the year is specified to begin in month 2. Therefore, the four-month period ends on the first month of the following year. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – Basic example

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm#glossary-1 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called `Transactions`.
- The date [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm#glossary-2 "Glossary term") provided in the `DateFormat` system variable (MM/DD/YYYY) format.
- The creation of a field, `bi_monthly_range`, that groups transactions into bi-monthly segments and returns the boundary names of that segment for each transaction.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        monthsname(2,date) as bi_monthly_range
        ;
Load
*
Inline
[
id,date,amount
8188,2/19/2022,37.23
8189,3/7/2022,17.17
8190,3/30/2022,88.27
8191,4/5/2022,57.42
8192,4/16/2022,53.80
8193,5/1/2022,82.06
8194,5/7/2022,40.39
8195,5/22/2022,87.21
8196,6/15/2022,95.93
8197,6/26/2022,45.89
8198,7/9/2022,36.23
8199,7/22/2022,25.66
8200,7/23/2022,82.77
8201,7/27/2022,69.98
8202,8/2/2022,76.11
8203,8/8/2022,25.12
8204,8/19/2022,46.23
8205,9/26/2022,84.21
8206,10/14/2022,96.24
8207,10/29/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `bi_monthly_range`

Results table

| date | bi\_monthly\_range |
| --- | --- |
| 2/19/2022 | Jan-Feb 2022 |
| 3/7/2022 | Mar-Apr 2022 |
| 3/30/2022 | Mar-Apr 2022 |
| 4/5/2022 | Mar-Apr 2022 |
| 4/16/2022 | Mar-Apr 2022 |
| 5/1/2022 | May-Jun 2022 |
| 5/7/2022 | May-Jun 2022 |
| 5/22/2022 | May-Jun 2022 |
| 6/15/2022 | May-Jun 2022 |
| 6/26/2022 | May-Jun 2022 |
| 7/9/2022 | Jul-Aug 2022 |
| 7/22/2022 | Jul-Aug 2022 |
| 7/23/2022 | Jul-Aug 2022 |
| 7/27/2022 | Jul-Aug 2022 |
| 8/2/2022 | Jul-Aug 2022 |
| 8/8/2022 | Jul-Aug 2022 |
| 8/19/2022 | Jul-Aug 2022 |
| 9/26/2022 | Sep-Oct 2022 |
| 10/14/2022 | Sep-Oct 2022 |
| 10/29/2022 | Sep-Oct 2022 |

The `bi_monthly_range` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm#glossary-3 "Glossary term") statement by using the `monthsname()` function. The first argument provided is 2, dividing the year into bi-monthly segments. The second argument identifies which field is being evaluated.

Diagram of monthsname function, basic example

![Diagram showing the results of using the monthsname function to determine the range of months within which a transaction took place. In this case, it determines that transaction number 8195, which took place on May 22, will return the value indicating a range of May to June 2022.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthsname-basic-example.png)

Transaction 8195 takes place on May 22. The `monthsname()` function initially divides the year into bi-monthly segments. Transaction 8195 falls into the segment between May 1 and June 30. Therefore, the function returns these months in the `MonthNames` system variable format, as well as the year, May-Jun 2022.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same inline dataset and scenario as the first example.
- The creation of a field, `prev_bi_monthly_range`, that groups transactions into bi-monthly segments and returns the previous segment boundary names for each transaction.

Add your other text here, as needed, with lists etc.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        MonthsName(2,date,-1) as prev_bi_monthly_range
        ;
Load
*
Inline
[
id,date,amount
8188,2/19/2022,37.23
8189,3/7/2022,17.17
8190,3/30/2022,88.27
8191,4/5/2022,57.42
8192,4/16/2022,53.80
8193,5/1/2022,82.06
8194,5/7/2022,40.39
8195,5/22/2022,87.21
8196,6/15/2022,95.93
8197,6/26/2022,45.89
8198,7/9/2022,36.23
8199,7/22/2022,25.66
8200,7/23/2022,82.77
8201,7/27/2022,69.98
8202,8/2/2022,76.11
8203,8/8/2022,25.12
8204,8/19/2022,46.23
8205,9/26/2022,84.21
8206,10/14/2022,96.24
8207,10/29/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `prev_bi_monthly_range`

Results table

| date | prev\_bi\_monthly\_range |
| --- | --- |
| 2/19/2022 | Nov-Dec 2021 |
| 3/7/2022 | Jan-Feb 2022 |
| 3/30/2022 | Jan-Feb 2022 |
| 4/5/2022 | Jan-Feb 2022 |
| 4/16/2022 | Jan-Feb 2022 |
| 5/1/2022 | Mar-Apr 2022 |
| 5/7/2022 | Mar-Apr 2022 |
| 5/22/2022 | Mar-Apr 2022 |
| 6/15/2022 | Mar-Apr 2022 |
| 6/26/2022 | Mar-Apr 2022 |
| 7/9/2022 | May-Jun 2022 |
| 7/22/2022 | May-Jun 2022 |
| 7/23/2022 | May-Jun 2022 |
| 7/27/2022 | May-Jun 2022 |
| 8/2/2022 | May-Jun 2022 |
| 8/8/2022 | May-Jun 2022 |
| 8/19/2022 | May-Jun 2022 |
| 9/26/2022 | Jul-Aug 2022 |
| 10/14/2022 | Jul-Aug 2022 |
| 10/29/2022 | Jul-Aug 2022 |

In this example, -1 is used as the `period_no` argument in the `monthsname()` function. After initially dividing a year into bi-monthly segments, the function then returns the previous segment boundaries for when a transaction takes place.

Diagram of monthsname function, period\_no example

![Diagram showing the results of using the monthsname function to determine the range of months within which a transaction took place. The period_no is set at -1. Transaction number 8195, which took place between May and June, will return the value indicating a range of March to April 2022.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthsname-example-period-no.png)

Transaction 8195 occurs in the segment between May and June. Therefore, the previous bi-monthly segment was between March 1 and April 30, and so the function returns Mar-Apr 2022.

## Example 3 – first\_month\_of\_year

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same inline dataset and scenario as the first example.
- The creation of a different field, `bi_monthly_range`, that groups transactions into bi-monthly segments and returns the segment boundaries for each transaction.

However, in this example, we also need to set April as the first month of the financial year.

Load script

```
SET DateFormat='MM/DD/YYYY';
						
Transactions:
    Load
        *,
        MonthsName(2,date,0,4) as bi_monthly_range
        ;
Load
*
Inline
[
id,date,amount
8188,2/19/2022,37.23
8189,3/7/2022,17.17
8190,3/30/2022,88.27
8191,4/5/2022,57.42
8192,4/16/2022,53.80
8193,5/1/2022,82.06
8194,5/7/2022,40.39
8195,5/22/2022,87.21
8196,6/15/2022,95.93
8197,6/26/2022,45.89
8198,7/9/2022,36.23
8199,7/22/2022,25.66
8200,7/23/2022,82.77
8201,7/27/2022,69.98
8202,8/2/2022,76.11
8203,8/8/2022,25.12
8204,8/19/2022,46.23
8205,9/26/2022,84.21
8206,10/14/2022,96.24
8207,10/29/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `bi_monthly_range`

Results table

| date | bi\_monthly\_range |
| --- | --- |
| 2/19/2022 | Feb-Mar 2021 |
| 3/7/2022 | Feb-Mar 2021 |
| 3/30/2022 | Feb-Mar 2021 |
| 4/5/2022 | Apr-May 2022 |
| 4/16/2022 | Apr-May 2022 |
| 5/1/2022 | Apr-May 2022 |
| 5/7/2022 | Apr-May 2022 |
| 5/22/2022 | Apr-May 2022 |
| 6/15/2022 | Jun-Jul 2022 |
| 6/26/2022 | Jun-Jul 2022 |
| 7/9/2022 | Jun-Jul 2022 |
| 7/22/2022 | Jun-Jul 2022 |
| 7/23/2022 | Jun-Jul 2022 |
| 7/27/2022 | Jun-Jul 2022 |
| 8/2/2022 | Aug-Sep 2022 |
| 8/8/2022 | Aug-Sep 2022 |
| 8/19/2022 | Aug-Sep 2022 |
| 9/26/2022 | Aug-Sep 2022 |
| 10/14/2022 | Oct-Nov 2022 |
| 10/29/2022 | Oct-Nov 2022 |

By using 4 as the `first_month_of_year` argument in the `monthsname()` function, the function begins the year on April 1. It then divides the year into bi-monthly segments: Apr-May,Jun-Jul,Aug-Sep,Oct-Nov,Dec-Jan,Feb-Mar.

Paragraph text for Results.

Transaction 8195 took place on May 22 and falls into the segment between April 1 and May 31. Therefore, the function returns Apr-May 2022.

Diagram of monthsname function, first\_month\_of\_year example

![Diagram showing the results of using the monthsname function to determine the range of months within which a transaction took place. Since the year is set to begin on April 1, transaction number 8195 will return a value indicating a range of April to May 2022.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthsname-example-first-month-of-year.png)

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm#glossary-4 "Glossary term") and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm#glossary-5 "Glossary term") below to a new tab.

The load script contains the same inline dataset and scenario as the first example. However, in this example, the unchanged dataset is loaded into the application. The calculation that groups transactions into bi-monthly segments and returns the segment boundaries for each transaction is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm#glossary-6 "Glossary term") in a chart object of the application.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8188,2/19/2022,37.23
8189,3/7/2022,17.17
8190,3/30/2022,88.27
8191,4/5/2022,57.42
8192,4/16/2022,53.80
8193,5/1/2022,82.06
8194,5/7/2022,40.39
8195,5/22/2022,87.21
8196,6/15/2022,95.93
8197,6/26/2022,45.89
8198,7/9/2022,36.23
8199,7/22/2022,25.66
8200,7/23/2022,82.77
8201,7/27/2022,69.98
8202,8/2/2022,76.11
8203,8/8/2022,25.12
8204,8/19/2022,46.23
8205,9/26/2022,84.21
8206,10/14/2022,96.24
8207,10/29/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:`date`.

Create the following measure:

`=monthsname(2,date)`

Results table

| date | =monthsname(2,date) |
| --- | --- |
| 2/19/2022 | Jan-Feb 2022 |
| 3/7/2022 | Mar-Apr 2022 |
| 3/30/2022 | Mar-Apr 2022 |
| 4/5/2022 | Mar-Apr 2022 |
| 4/16/2022 | Mar-Apr 2022 |
| 5/1/2022 | May-Jun 2022 |
| 5/7/2022 | May-Jun 2022 |
| 5/22/2022 | May-Jun 2022 |
| 6/15/2022 | May-Jun 2022 |
| 6/26/2022 | May-Jun 2022 |
| 7/9/2022 | Jul-Aug 2022 |
| 7/22/2022 | Jul-Aug 2022 |
| 7/23/2022 | Jul-Aug 2022 |
| 7/27/2022 | Jul-Aug 2022 |
| 8/2/2022 | Jul-Aug 2022 |
| 8/8/2022 | Jul-Aug 2022 |
| 8/19/2022 | Jul-Aug 2022 |
| 9/26/2022 | Sep-Oct 2022 |
| 10/14/2022 | Sep-Oct 2022 |
| 10/29/2022 | Sep-Oct 2022 |

The `bi_monthly_range` field is created as a measure in the chart object by using the `monthsname()` function. The first argument provided is 2, dividing the year into bi-monthly segments. The second argument identifies which field is being evaluated.

Diagram of monthsname function, chart object example

![Diagram showing the results of using the monthsname function with a chart object. Like the other examples, the function is used to determine the range of months within which a transaction took place. Transaction number 8195 returns a value of May-Jun 2022.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthsname-example-chart-object.png)

Transaction 8195 takes place on May 22. The `monthsname()` function initially divides the year into bi-monthly segments. Transaction 8195 falls into the segment between May 1 and June 30. Therefore, the function returns these months in the `MonthNames` system variable format, as well as the year, May-Jun 2022.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing transactions for 2022, which is loaded into a table called `Transactions`.
- The date field provided in the `DateFormat` system variable (MM/DD/YYYY) format.

The end user would like a chart object that displays total sales by a period of their own choosing. This could be achieved even when this [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm#glossary-7 "Glossary term") is not available in the data model, using the `monthsname()` function as a calculated dimension that is dynamically modified by a variable input control.

Load script

```
SET vPeriod = 1;
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8188,'1/7/2022',17.17
8189,'1/19/2022',37.23
8190,'2/28/2022',88.27
8191,'2/5/2022',57.42
8192,'3/16/2022',53.80
8193,'4/1/2022',82.06
8194,'5/7/2022',40.39
8195,'5/16/2022',87.21
8196,'6/15/2022',95.93
8197,'6/26/2022',45.89
8198,'7/9/2022',36.23
8199,'7/22/2022',25.66
8200,'7/23/2022',82.77
8201,'7/27/2022',69.98
8202,'8/2/2022',76.11
8203,'8/8/2022',25.12
8204,'8/19/2022',46.23
8205,'9/26/2022',84.21
8206,'10/14/2022',96.24
8207,'10/29/2022',67.67
];
```

Results

Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm#glossary-8 "Glossary term").

At the start of the load script, a variable (`vPeriod`) has been created that will be tied to the variable input control. Next, configure the variable as a [custom object](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm#glossary-9 "Glossary term") in the sheet.

Do the following:

1. In the assets panel, click **Charts**.
2. Under **Dashboard objects**, drag a **Variable input** onto the sheet.
3. Enter a title for the chart object.
4. Under **Variable**, select **vPeriod** as the Name and set the object to show as a **Drop down**.
5. Under **Values**, configure the object to use dynamic values. Enter the following:

   `='1~month|2~bi-month|3~quarter|4~tertial|6~half-year'`

Next, create the results table.

Do the following:

1. Create a new table and add the following calculated dimension:

   `=monthsname($(vPeriod),date)`
2. Add this measure to calculate the total sales:

   `=sum(amount)`
3. Set the measure's **Number formatting** to **Money**.Click Edit sheet to finish editing. You can now modify the data shown in the table by adjusting the time segment in the variable object.

This is what the results table will look like when the `tertial` option is selected:

Results table

| monthsname($(vPeriod),date) | =sum(amount) |
| --- | --- |
| Jan-Apr 2022 | 253.89 |
| May-Aug 2022 | 713.58 |
| Sep-Dec 2022 | 248.12 |
