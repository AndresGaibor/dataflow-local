---
title: "Known limitations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/known-limitations-table-recipe.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe"]
---

# Known limitations

## General

- The Modified date available in the Overview tab will only be updated after a run or when any of the name, description or tags of the table recipe are edited, and not when the steps of the table recipe themselves are changed.
- Empty and Null values contained in columns will appear as "NaN" in the Data distribution area instead of the proper label.
- Table recipes can't fully display on small screens. For the best experience, use a screen size that provides enough space for the table recipe interface.
- Table recipes are subject to the same data and field limits that apply when loading data in Qlik Cloud Analytics. For example, a field cannot have more than 2,147,483,648 distinct values, and the total number of fields and rows that can be loaded is limited by available memory. For details, see [*Guidelines for data and fields*](../Introduction/guidelines-data-fields.htm).

## Sources and targets

- Header detection for CSV and Excel files is not always accurate. If your column names look wrong, try editing file settings. See [*Configure the file settings of CSV and Excel sources*](working-with-table-recipes.htm#Configur) for more information.

## Functions

- When working on columns with the date type, the Convert to date function disappears from the suggestions when using a filter.

## Collaborative work

- Although collaboration from two users or more on a single table recipe is limited at this time, it is possible for multiple users to edit a table recipe in a shared space. If you open a table recipe, and someone makes a concurrent change, a prompt will open to notify that you need to reload the table recipe. After you get the latest version, you can make your change.
- Table recipes do not currently support the versioning feature found in Scripts and Applications.

## Create calculated column function

- Column references must be surrounded by brackets or quotes.
- Some script functions are not supported, even though they are displayed as valid in the expression editor:

  For aggregation functions that exist in both script and chart variants, the script variant is not supported.

  - Aggregation functions (script variant): FirstSortedValue, Max, Min, Mode, Only, Sum, Count, MissingCount, NullCount, NumericCount, TextCount, IRR, NPV, XIRR, XNPV, Avg, Correl, Fractile, FractileExc, Kurtosis, LINEST\_B, LINEST\_DF, LINEST\_F, LINEST\_M, LINEST\_R2, LINEST\_SEB, LINEST\_SEM, LINEST\_SEY, LINEST\_SSREG, LINEST\_SSRESID, Median, Skew, Stdev, Sterr, STEYX, Chi2Test\_chi2, Chi2Test\_df, TTest\_conf, TTest\_df, TTest\_dif, TTest\_lower, TTest\_sig, TTest\_sterr, TTest\_t, TTest\_upper, TTestw\_conf, TTestw\_df, TTestw\_dif, TTestw\_lower, TTestw\_sig, TTestw\_sterr, TTestw\_t, TTestw\_upper, TTest1\_conf, TTest1\_df, TTest1\_dif, TTest1\_lower, TTest1\_sig, TTest1\_sterr, TTest1\_t, TTest1\_upper, TTest1w\_conf, TTest1w\_df, TTest1w\_dif, TTest1w\_lower, TTest1w\_sig, TTest1w\_sterr, TTest1w\_t, TTest1w\_upper, ZTest\_conf, ZTest\_dif, ZTest\_lower, ZTest\_sig, ZTest\_sterr, ZTest\_upper, ZTest\_z, ZTestw\_conf, ZTestw\_dif, ZTestw\_lower, ZTestw\_sig, ZTestw\_sterr, ZTestw\_upper, ZTestw\_z, Concat, MaxString, MinString, FirstValue, LastValue.
  - Counter functions: autonumber, autonumberhash128, autonumberhash256, IterNo, RecNo, RowNo.
  - File functions: Attribute, ConnectString, FileBaseName, FileDir, FileExtension, FileName, FilePath.
  - Inter-record functions: Exists, LookUp, Peek, Previous.
  - Mapping functions: ApplyMap, MapSubstring.
  - String functions: Evaluate.
  - System functions: IsPartialReload.
  - Table functions: FieldName, FieldNumber, NoOfFields.
  - Window functions: Window, WRank.

## Data quality

- In table recipes, data quality indicators cover semantic types only. Validation rules and classifications are not applied in table recipes.
- After you apply the Format Number function with thousands separators to an integer column, data quality can flag values as invalid. To avoid this behavior, change the column type to decimal before applying the formatting.
- Data quality indicators may take longer to compute in table recipes with many preparation steps. The system re-executes all prior recipe steps to evaluate the current state of the data before displaying quality results.
- When a table recipe is embedded in a data flow, semantic types are not propagated from the source to the target dataset. Semantic type propagation is only available in standalone table recipes.
