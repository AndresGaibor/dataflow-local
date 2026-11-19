---
title: "XNPV Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/XNPV.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Financial aggregation functions"]
---
Expand/Collapse all

# XNPV Script function

XNPV() returns the aggregated net present
value for a schedule of cashflows (not necessarily periodic) represented
by paired numbers in pmt and date. All payments are discounted based on a 365-day year.

Syntax:

XNPV(discount\_rate, pmt,
date)

Return data type:  numeric

> **Note:** By default, the result will be formatted as currency.

The formula to calculate XNPV is shown below:

XNPV aggregation formula

![Image of formula for XNPV script function.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-xnpv-formula.png)

where:

- `P`i = Net cash inflow-outflows during a single period `i`
- `d`1= the first payment date
- `d`i = the `i`th payment date
- `rate` = discount rate

Net present value, or NPV, is used to calculate the current total value of a future stream of cash flows given a discount rate. To calculate XNPV, we need to estimate future cash flows with corresponding dates. After this, for each payment, we apply the compounded discount rate based on the date of the payment.

Performing the XNPV aggregation over a series of payments is similar to performing a Sum aggregation over those payments. The difference is that each amount is modified (or “discounted”) according to the chosen discount rate (similar to interest rate) and how far into the future the payment is. Performing XNPV with the discount\_rate parameter set to zero will make XNPV equivalent to a Sum operation (the payments will not be modified before being summed). In general, the closer the discount\_rate is set to zero, the more similar the XNPV result will be to that of a Sum aggregation.

Arguments

| Argument | Description |
| --- | --- |
| discount\_rate | **discount\_rate** is the yearly rate that the payments should be discounted by.  A value of 0.1 would indicate a 10% discount rate. |
| pmt | Payments. The expression or field containing the cash flows corresponding to the payment schedule given in date. Positive values are assumed to be inflows, and negative values are assumed to be outflows.  **Note:** XNPV() does not discount the initial cash flow since it will always happen on the start date. Subsequent payments are discounted based on a 365-day year. This is different from NPV(), where also the first payment is discounted. |
| date | The expression or field containing the schedule of dates corresponding to the cash flow payments given in pmt. The first value is used as the start date for calculating the time offsets for future cashflows. |

When working with this function, the following limitations apply:

- Text values, NULL values and missing values in any or both pieces of a data-pair result in the entire data-pair being disregarded.

## When to use NPV

- `XNPV()` is used in financial modeling for calculating the net present value (NPV) of an investment opportunity.
- Due to its higher precision, XNPV is preferred over NPV, for all types of financial models.

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – Single payment (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/XNPV.htm#glossary-0 "Glossary term") of one project and its cashflow for one year, in a table named `CashFlow`. The initial date for calculation is set to July 1, 2022, with a net cashflow of 0. After one year, a cashflow of $1000 occurs.
- A [resident load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/XNPV.htm#glossary-1 "Glossary term") from the `CashFlow` table, which is used to calculate the `XNPV` field for the project in a table named `XNPV`.
- A hard-coded discount rate of 10% (0.1) is used in the XNPV calculation.
- A `Group By` statement is used to group all the payments for the project.

Load script

```
CashFlow:
Load
*
Inline 
[	
PrjId,Dates,Values
1,'07/01/2022',0
1,'07/01/2023',1000
];

XNPV:
Load 
	PrjId,
	XNPV(0.1,Values,Dates) as XNPV //Discount Rate of 10%
Resident CashFlow
Group By PrjId;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `PrjId`
- `XNPV`

Results table

| PrjId | XNPV |
| --- | --- |
| 1 | $909.09 |

As per the formula, the XNPV value for the first record is 0, and for the second record, the XNPV value is $909.09 Thus, the total XNPV is $909.09.

## Example 2 – Multiple payments (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of one project and its cashflow for one year, in a table named `CashFlow`.
- A resident load from the `CashFlow` table, which is used to calculate the `XNPV` field for the project in a table named `XNPV`.
- A hard-coded discount rate of 10% (0.1) is used in the XNPV calculation.
- A `Group By` statement is used to group all the payments for the project.

Load script

```
CashFlow:
Load
*
Inline 
[	
PrjId,Dates,Values
1,'07/01/2022',0
1,'07/01/2024',500
1,'07/01/2023',1000
];

XNPV:
Load 
	PrjId,
	XNPV(0.1,Values,Dates) as XNPV //Discount Rate of 10%
Resident CashFlow
Group By PrjId;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `PrjId`
- `XNPV`

Results table

| PrjId | XNPV |
| --- | --- |
| 1 | $1322.21 |

In this example, a payment of $1000 is received at the end of first year, and a payment of $500 is received at the end of second year. With a discount rate of 10% per period, the effective XNPV is equal to $1322.21.

Note that only the first row of data should refer to the base date for calculations. For rest of the rows, order is not important, since the date parameter is used to calculate the elapsed period.

## Example 3 – Multiple payments and irregular cashflows (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Discount rates for two projects in a table named `Project`.
- Cashflows for multiple periods for each project by project ID and Dates. The `Dates` field is used to calculate the duration for which discount rate is applied to the cash flow. Apart from the first record (initial cashflow and date), order of records is not important, and changing it should not impact the calculations.
- Using a combination of `NoConcatenate`, Resident loads, and the `Left Join` function, a temporary table, `tmpNPV`, is created that combines the records of the `Project` and `CashFlow` tables in one flat table. This table will have discount rates repeated for each cashflow.
- A resident load from the `tmpNPV` table, which is used to calculate the `XNPV` field for each project in a table named `XNPV`.
- The single value discount rate associated to each project is fetched using the `only()` function and is used in the `XNPV` calculation for each project.
- A `Group By` statement, grouping by project ID, is used to group all the payments and corresponding dates for each project.
- To avoid any synthetic or redundant data being loaded into the data model, the `tmpXNPV` table is dropped at the end of the script.

Load script

```
Project:
Load * inline [
PrjId,Discount_Rate
1,0.1
2,0.15
];

CashFlow:
Load
*
Inline 
[	
PrjId,Dates,Values
1,'07/01/2021',0
1,'07/01/2022',1000
1,'07/01/2023',1000
2,'07/01/2020',0
2,'07/01/2023',500
2,'07/01/2024',1000
2,'07/01/2022',500
];

tmpXNPV:
NoConcatenate Load *
Resident Project;
Left Join
Load * 
Resident CashFlow;

XNPV:
Load 
	PrjId,
	XNPV(Only(Discount_Rate),Values,Dates) as XNPV //Discount Rate will be 10% for Project 1 and 15% for Project 2
Resident tmpXNPV
Group By PrjId;

Drop table tmpXNPV;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `PrjId`
- `XNPV`

Results table

| PrjId | XNPV |
| --- | --- |
| 1 | $1735.54 |
| 2 | $278.36 |

Project ID 1 has an initial cashflow of $0 on July 1, 2021. There are two payments of $1000 to be received at the end of two subsequent years, at a discount rate of 10% per period. Therefore, the effective XNPV is equal to $1735.54.

Project ID 2 has an initial outflow of $1000 (thus the negative sign) on July 1, 2020. After two years, a payment of $500 is expected. After 3 years, another $500 payment is expected. Finally, on July 1, 2024, a payment of $1000 is expected. With the discount rate of 15%, the effective XNPV is equal to $278.36.

## Learn more

- [*Drop table*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/drop-table.htm)
- [*group by*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#group_by)
- [*Join*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Join.htm)
- [*Max Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/max.htm)
- [*NoConcatenate*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/NoConcatenate.htm)
- [*NPV - chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FinancialAggregationFunctionsInCharts/npv.htm)
- [*Only Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/only.htm)
- [*Resident LOAD*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/load-data-from-previously-loaded-table.htm#Resident)
