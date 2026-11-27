---
title: "Creating a typical t-test report"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/ttest/ttest_t_example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions", "Statistical test function examples"]
---

# Creating a typical t-test report

A typical student t-test report can include tables with Group Statistics and Independent Samples Test results.

In the following sections we will build these tables using Qlik Senset-test functions applied to two independent groups of samples, Observation and Comparison. The corresponding tables for these samples would look like this:

Group statistics

| Type | N | Mean | Standard Deviation | Standard Error Mean |
| --- | --- | --- | --- | --- |
| Comparison | 20 | 11.95 | 14.61245 | 3.2674431 |
| Observation | 20 | 27.15 | 12.507997 | 2.7968933 |

Independent sample test

| Type | conf | t | df | Sig. (2-tailed) | Mean Difference | Standard Error Difference | 95% Confidence Interval (Lower) | 95% Confidence Interval (Upper) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Equal Variance not Assumed | 0 | 3.534 | 37.116717335823 | 0.001 | 15.2 | 4.30101 | 6.48625 | 23.9137 |
| Equal Variance Assumed | 8.706939 | 3.534 | 38 | 0.001 | 15.2 | 4.30101 | 6.49306 | 23.9069 |

## Loading the sample data

Do the following:

1. Create a new app with a new sheet.
2. Enter the following in the data load editor:

   ```
   Table1:
   Crosstable (Type, Value)
   Load recno() as ID, * inline [
   Observation|Comparison
   35|2
   40|27
   12|38
   15|31
   21|1
   14|19
   46|1
   10|34
   28|3
   48|1
   16|2
   30|3
   32|2
   48|1
   31|2
   22|1
   12|3
   39|29
   19|37
   25|2 ] (delimiter is '|');
   ```

   In this load script, recno() is included because crosstable requires three arguments. So, recno() simply provides an extra argument, in this case an ID for each row. Without it, Comparison sample values would not be loaded.
3. Click ![run script](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_run_script.svg) to load data.

## Creating the Group statistics table

Do the following:

1. In the data load editor, click ![compass](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_compass.svg) to go to app view, and then click the [sheet](#glossary-0 "Glossary term") you created before.

   This opens the sheet view.
2. Click![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet to edit the sheet.
3. From Charts, add a table, and from Fields, add Type as a [dimension](#glossary-1 "Glossary term") to the table.
4. Add the following expressions as [measures](#glossary-2 "Glossary term").

   Example expressions

   | Label | Expression |
   | --- | --- |
   | N | Count(Value) |
   | Mean | Avg(Value) |
   | Standard Deviation | Stdev(Value) |
   | Standard Error Mean | Sterr(Value) |
5. Click Sorting and make sure Type is at the top of the sorting list.

Result:

A Group statistics table for these samples would look like this:

Group statistics

| Type | N | Mean | Standard Deviation | Standard Error Mean |
| --- | --- | --- | --- | --- |
| Comparison | 20 | 11.95 | 14.61245 | 3.2674431 |
| Observation | 20 | 27.15 | 12.507997 | 2.7968933 |

## Creating the Independent sample test table

Do the following:

1. Click![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet to edit the sheet.
2. From Charts add a table with the following expression as a dimension to the table. =ValueList (Dual('Equal Variance not Assumed', 0), Dual('Equal Variance Assumed', 1)) and give it the label Type.
3. Add the following expressions as measures:

   Example expressions

   | Label | Expression |
   | --- | --- |
   | conf | if(ValueList (Dual('Equal Variance not Assumed', 0), Dual('Equal Variance Assumed', 1)),TTest\_conf(Type, Value),TTest\_conf(Type, Value, 0)) |
   | t | if(ValueList (Dual('Equal Variance not Assumed', 0), Dual('Equal Variance Assumed', 1)),TTest\_t(Type, Value),TTest\_t(Type, Value, 0)) |
   | df | if(ValueList (Dual('Equal Variance not Assumed', 0), Dual('Equal Variance Assumed', 1)),TTest\_df(Type, Value),TTest\_df(Type, Value, 0)) |
   | Sig. (2-tailed) | if(ValueList (Dual('Equal Variance not Assumed', 0), Dual('Equal Variance Assumed', 1)),TTest\_sig(Type, Value),TTest\_sig(Type, Value, 0)) |
   | Mean Difference | TTest\_dif(Type, Value) |
   | Standard Error Difference | if(ValueList (Dual('Equal Variance not Assumed', 0), Dual('Equal Variance Assumed', 1)),TTest\_sterr(Type, Value),TTest\_sterr(Type, Value, 0)) |
   | 95% Confidence Interval (Lower) | if(ValueList (Dual('Equal Variance not Assumed', 0), Dual('Equal Variance Assumed', 1)),TTest\_lower(Type, Value,(1-(95)/100)/2),TTest\_lower(Type, Value,(1-(95)/100)/2, 0)) |
   | 95% Confidence Interval (Upper) | if(ValueList (Dual('Equal Variance not Assumed', 0), Dual('Equal Variance Assumed', 1)),TTest\_upper(Type, Value,(1-(95)/100)/2),TTest\_upper(Type, Value,(1-(95)/100)/2, 0)) |

   Result:

   Independent sample test

   | Type | conf | t | df | Sig. (2-tailed) | Mean Difference | Standard Error Difference | 95% Confidence Interval (Lower) | 95% Confidence Interval (Upper) |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | Equal Variance not Assumed | 0 | 3.534 | 37.116717335823 | 0.001 | 15.2 | 4.30101 | 6.48625 | 23.9137 |
   | Equal Variance Assumed | 8.706939 | 3.534 | 38 | 0.001 | 15.2 | 4.30101 | 6.49306 | 23.9069 |
