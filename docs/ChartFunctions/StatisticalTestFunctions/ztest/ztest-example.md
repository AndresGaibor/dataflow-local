---
title: "Examples of how to use z-test functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/ztest/ztest-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions", "Statistical test function examples"]
---

# Examples of how to use z-test functions

The z-test functions are used to find values associated with z-test statistical analysis for large data samples, usually greater than 30, and where the variance is known.

This section describes how to build [visualizations](#glossary-0 "Glossary term") using sample data to find the values of the z-test functions available in Qlik Sense. Please refer to the individual z-test chart function topics for descriptions of syntax and arguments.

## Loading the sample data

The sample data used here is the same as that used in the t-test function examples. The sample data size would normally be considered too small for z-test analysis, but is sufficient for the purposes of illustrating the use of the different z-test functions in Qlik Sense.

Do the following:

1. Create a new app with a new sheet.

Tip noteIf you created an appfor the t-test functions, you could use that and create a new [sheet](#glossary-2 "Glossary term")for these functions.

2. In the data load editor, enter the following:

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

## Creating the z-test table

Do the following:

1. In the data load editor, click ![compass](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_compass.svg) to go to app view, and then click the sheet you created above.

   The sheet view is opened.
2. Click![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet to edit the sheet.
3. From Charts add a table, and from Fields add Type as a dimension.
4. Add the following expressions to the table as [measures](#glossary-3 "Glossary term")

Example expressions

| Label | Expression |
| --- | --- |
| ZTest Conf | ZTest\_conf(Value) |
| ZTest Dif | ZTest\_dif(Value) |
| ZTest Sig | ZTest\_sig(Value) |
| ZTest Sterr | ZTest\_sterr(Value) |
| ZTest Z | ZTest\_z(Value) |

Tip noteYou might wish to adjust the number formatting of the measures to see meaningful values. The table will be easier to read if you set number formatting on most of the measures to Number>Simple, instead of Auto. But for ZTest Sig, for example, use the number formatting: Custom, and then adjust the format pattern to #.######.

Result:

The resulting table for the z-test functions for the sample data will contain the following values:

z-test results table

| Type | ZTest Conf | ZTest Dif | ZTest Sig | ZTest Sterr | ZTest Z |
| --- | --- | --- | --- | --- | --- |
| Comparison | 6.40 | 11.95 | 0.000123 | 3.27 | 3.66 |
| Observation | 5.48 | 27.15 | 0.000000 | 2.80 | 9.71 |

## Creating the z-testw table

The z-testw functions are for use when the input data series occurs in weighted two-column format. The expressions require a value for the argument weight.

The examples here use the value 2 throughout, but you could use an expression, which would define a value for weight for each observation.

Do the following:

1. In the data load editor, click ![compass](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_compass.svg) to go to app view, and then click the sheet you created above.

   The sheet view is opened.
2. Click![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet to edit the sheet.
3. From Charts add a table, and from Fields add Type as a dimension.
4. Add the following expressions to the table as measures.

   Example expressions

   | Label | Expression |
   | --- | --- |
   | ZTestw Conf | ZTestw\_conf(2,Value) |
   | ZTestw Dif | ZTestw\_dif(2,Value) |
   | ZTestw Sig | ZTestw\_sig(2,Value) |
   | ZTestw Sterr | ZTestw\_sterr(2,Value) |
   | ZTestw Z | ZTestw\_z(2,Value) |

   Use the same number formatting as in the z-test functions example.

Result:

The resulting table for the z-testw functions will contain the following values:

z-testw results table

| Type | ZTestw Conf | ZTestw Dif | ZTestw Sig | ZTestw Sterr | ZTestw Z |
| --- | --- | --- | --- | --- | --- |
| Comparison | 4.47 | 11.95 | 8.037185e-08 | 2.28 | 5.24 |
| Observation | 3.83 | 27.15 | 0 | 1.95 | 13.91 |
