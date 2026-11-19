---
title: "NPV Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/NPV.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Financial aggregation functions"]
---
Expand/Collapse all

# NPV Script function

The NPV() script function takes a discount rate and multiple values ordered by period. Inflows (incomes) are positive, and outflows (future payments) are assumed to be negative values for these calculations. These occur at the end of each period.

Net Present Value, or NPV, is used to calculate the current total value of a future stream of cash flows. To calculate NPV, we need to estimate future cash flows for each period and determine the correct discount rate.
The NPV() script function takes a discount rate and multiple values ordered by period. Inflows (incomes) are positive, and outflows (future payments) are assumed to be negative values for these calculations. These occur at the end of each period.

Syntax:

NPV(discount\_rate, value)

Return data type:  numeric. By default, the result will be formatted as currency.

The formula to calculate net present value is:

![Formula for calculating NPV.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-npv-formula.png)

where:

- `R`t= Net cash inflow-outflows during a single period `t`
- `i` = Discount rate or return that could be earned in alternative investments
- `t` = Number of timer periods

Arguments

| Argument | Description |
| --- | --- |
| discount\_rate | discount\_rate is the percentage rate of discount applied.  A value of 0.1 would indicate a 10% discount rate. |
| value | This [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/NPV.htm#glossary-0 "Glossary term") holds values for multiple periods ordered by period. The first value is assumed to be the cashflow at the end of period 1, and so on. |

Limitations:

The `NPV()` function has the following limitations:

- Text values, NULL values and missing values are disregarded.
- Cashflow values must be in order of ascending period.

## When to use NPV

`NPV()` is a financial function used to check project profitability and to derive other [measures](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/NPV.htm#glossary-1 "Glossary term"). This function is useful when cashflows are available as raw data.

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – Single payment (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/NPV.htm#glossary-2 "Glossary term") of one project and its cashflow for one period, which is loaded into a table named `CashFlow`.
- A [resident load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/NPV.htm#glossary-3 "Glossary term") from the `CashFlow` table, which is used to calculate the NPV field for the project in a table named `NPV`.
- A hard-coded discount rate of 10% , which is used in the NPV calculation.
- A `Group By` statement, which is used to group all the payments for the project.

Load script

```
CashFlow:
Load
*
Inline 
[	
PrjId,PeriodId,Values
1,1,1000
];

NPV:
Load 
	PrjId,
	NPV(0.1,Values) as NPV //Discount Rate of 10%
Resident CashFlow
Group By PrjId;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `PrjId`
- `NPV`

Results table

| PrjId | NPV |
| --- | --- |
| 1 | $909.09 |

For a single payment of $1000 to be received at the end of one period, at a discount rate of 10% per period, the NPV is equal to $1000 divided by (1 + discount rate). The effective NPV is equal to $909.09

## Example 2 – Multiple payments (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of one project and its cashflow for multiple periods, which is loaded into a table named `CashFlow`.
- A resident load from the `CashFlow` table, which is used to calculate the NPV field for the project in a table named `NPV`.
- A hard-coded discount rate of 10% (0.1) is used in the NPV calculation.
- A `Group By` statement, which is used to group all the payments for the project.

Load script

```
CashFlow:
Load
*
Inline 
[	
PrjId,PeriodId,Values
1,1,1000
1,2,1000
];

NPV:
Load 
	PrjId,
	NPV(0.1,Values) as NPV //Discount Rate of 10%
Resident CashFlow
Group By PrjId;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `PrjId`
- `NPV`

Results table

| PrjId | NPV |
| --- | --- |
| 1 | $1735.54 |

For payments of $1000 to be received at the end of two periods, at a discount rate of 10% per period, the effective NPV is equal to $1735.54.

## Example 3 – Multiple payments (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Discount rates for two projects, which is loaded into a table named `Project`.
- Cashflows for multiple periods for each project by project ID and period ID. This period ID could be used to order the records in case the data is not ordered.
- The combination of `NoConcatenate`, Resident loads, and the `Left Join` function to create a temporary table, `tmpNPV`. The table combines the records of `Project` and `CashFlow` tables into one flat table. This table will have discount rates repeated for each period.
- A resident load from the `tmpNPV` table, which is used to calculate the NPV field for each project in a table named `NPV`.
- The single value discount rate associated to each project. This is retrieved using the `only()` function and is used in the NPV calculation for each project.
- A `Group By` statement, which is used to group all the payments for each project by project ID.

To avoid any synthetic or redundant data being loaded into the data model, the `tmpNPV` table is dropped at the end of the script.

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
PrjId,PeriodId,Values
1,1,1000
1,2,1000
1,3,1000
2,1,500
2,2,500
2,3,1000
2,4,1000
];

tmpNPV:
NoConcatenate Load *
Resident Project;
Left Join
Load * 
Resident CashFlow;

NPV:
Load 
	PrjId,
	NPV(Only(Discount_Rate),Values) as NPV //Discount Rate will be 10% for Project 1 and 15% for Project 2
Resident tmpNPV
Group By PrjId;

Drop table tmpNPV;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `PrjId`
- `NPV`

Results table

| PrjId | NPV |
| --- | --- |
| 1 | $2486.85 |
| 2 | $2042.12 |

Project ID 1 expects for payments of $1000 to be received at the end of three periods, at a discount rate of 10% per period. Therefore, the effective NPV is equal to $2486.85.

Project ID 2 expects two payments of $500 and two further payments of $1000 across four periods at a discount rate of 15%. Therefore, the effective NPV is equal to $2042.12.

## Example 4 – Project profitability example (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Discount rates and initial investments (period 0) for two projects, loaded into a table named `Project`.
- Cashflows for multiple periods for each project by project ID and period ID. This period ID could be used to order the records in case the data is not ordered.
- The combination of `NoConcatenate`, Resident loads, and the `Left Join` function to create a temporary table, `tmpNPV`. The table combines the records of `Project` and `CashFlow` tables into one flat table. This table will have discount rates repeated for each period.
- The single value discount rate associated to each project, which is retrieved using the `only()` function and is used in the NPV calculation for each project.
- A resident load from the tmpNPV table is used to calculate the NPV field for each project in a table named NPV.
- An additional field that divides the NPV by the initial investment of each project is created to calculate the project profitability index.
- A group by statement, grouping by project ID, is used to group all the payments for each project.

To avoid any synthetic or redundant data being loaded into the data model, the `tmpNPV` table is dropped at the end of the script.

Load script

```
Project:
Load * inline [
PrjId,Discount_Rate, Initial_Investment
1,0.1,100000
2,0.15,100000
];

CashFlow:
Load
*
Inline 
[	
PrjId,PeriodId,Values,
1,1,35000
1,2,35000
1,3,35000
2,1,30000
2,2,40000
2,3,50000
2,4,60000
];

tmpNPV:
NoConcatenate Load *
Resident Project;
Left Join
Load * 
Resident CashFlow;

NPV:
Load
        PrjId,
        NPV(Only(Discount_Rate),Values) as NPV, //Discount Rate will be 10% for Project 1 and 15% for Project 2
    NPV(Only(Discount_Rate),Values)/ Only(Initial_Investment) as Profitability_Index
Resident tmpNPV
Group By PrjId;

Drop table tmpNPV;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `PrjId`
- `NPV`

Create the following measure:

`=only(Profitability_Index)`

Results table

| PrjId | NPV | =only(Profitability\_Index) |
| --- | --- | --- |
| 1 | $87039.82 | 0.87 |
| 2 | $123513.71 | 1.24 |

Project ID 1 has an effective NPV of $87039.82 and an initial investment of $100000. Therefore, the profitability index is equal to 0.87. Because it is less than 1, the project is not profitable.

Project ID 2 has an effective NPV of $123513.71 and an initial investment of $100000. Therefore, the profitability index is equal to 1.24. Because it is greater than 1, the project is profitable.

## Learn more

- [*Drop table*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/drop-table.htm)
- [*group by*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#group_by)
- [*Join*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Join.htm)
- [*Max Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/max.htm)
- [*NoConcatenate*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/NoConcatenate.htm)
- [NPV - chart function](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FinancialAggregationFunctionsInCharts/npv.htm)
- [*Only Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/only.htm)
- [*Resident LOAD*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/load-data-from-previously-loaded-table.htm#Resident)
