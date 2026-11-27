---
title: "Examples of how to use linest functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# Examples of how to use linest functions

Expand/Collapse all

# Examples of how to use linest functions

The linest functions are used to find values associated with linear regression analysis. This section describes how to build [visualizations](#glossary-0 "Glossary term") using sample data to find the values of the linest functions available in Qlik Sense. The linest functions can be used in the data [load script](#glossary-1 "Glossary term") and in chart expressions.

Refer to the individual linest chart function and script function topics for descriptions of syntax and arguments.

## Data and script expressions used in the examples

Load the following inline data and script expressions in the data load editor for the linest() examples below.

```
T1:
LOAD *, 1 as Grp;
LOAD * inline [
X|Y
1|0
2|1
3|3
4|8
5|14
6|20
7|0
8|50
9|25
10|60
11|38
12|19
13|26
14|143
15|98
16|27
17|59
18|78
19|158
20|279 ] (delimiter is '|');

R1:
LOAD
Grp,
linest_B(Y,X) as Linest_B,
linest_DF(Y,X) as Linest_DF,
linest_F(Y,X) as Linest_F,
linest_M(Y,X) as Linest_M,
linest_R2(Y,X) as Linest_R2,
linest_SEB(Y,X,1,1) as Linest_SEB,
linest_SEM(Y,X) as Linest_SEM,
linest_SEY(Y,X) as Linest_SEY,
linest_SSREG(Y,X) as Linest_SSREG,
linest_SSRESID(Y,X) as Linest_SSRESID
resident T1 group by Grp;

```

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

## Example 1: Script expressions using linest

Example: Script expressions

### Create a visualization from the data load script calculations

Create a table visualization in a Qlik Sense [sheet](#glossary-2 "Glossary term") with the following fields as columns:

- Linest\_B
- Linest\_DF
- Linest\_F
- Linest\_M
- Linest\_R2
- Linest\_SEB
- Linest\_SEM
- Linest\_SEY
- Linest\_SSREG
- Linest\_SSRESID

### Result

The table containing the results of the linest calculations made in the data load script should look like this:

Results table

| Linest\_B | Linest\_DF | Linest\_F | Linest\_M | Linest\_R2 | Linest\_SEB |
| --- | --- | --- | --- | --- | --- |
| -35.047 | 18 | 20.788 | 8.605 | 0.536 | 22.607 |

Results table

| Linest\_SEM | Linest\_SEY | Linest\_SSREG | Linest\_SSRESID |
| --- | --- | --- | --- |
| 1.887 | 48.666 | 49235.014 | 42631.186 |

## Example 2: Chart expressions using linest

Example: Chart expressions

Create a table visualization in a Qlik Sense sheet with the following fields as [dimensions](#glossary-3 "Glossary term"):

ValueList('Linest\_b', 'Linest\_df','Linest\_f', 'Linest\_m','Linest\_r2','Linest\_SEB','Linest\_SEM','Linest\_SEY','Linest\_SSREG','Linest\_SSRESID')

This expression uses the synthetic dimensions function to create labels for the dimensions with the names of the linest functions. You can change the label to Linest functions to save space.

Add the following expression to the table as a [measure](#glossary-4 "Glossary term"):

Pick(Match(ValueList('Linest\_b', 'Linest\_df','Linest\_f', 'Linest\_m','Linest\_r2','Linest\_SEB','Linest\_SEM','Linest\_SEY','Linest\_SSREG','Linest\_SSRESID'),'Linest\_b', 'Linest\_df','Linest\_f', 'Linest\_m','Linest\_r2','Linest\_SEB','Linest\_SEM','Linest\_SEY','Linest\_SSREG','Linest\_SSRESID'),Linest\_b(Y,X),Linest\_df(Y,X),Linest\_f(Y,X),Linest\_m(Y,X),Linest\_r2(Y,X),Linest\_SEB(Y,X,1,1),Linest\_SEM(Y,X),Linest\_SEY(Y,X),Linest\_SSREG(Y,X),Linest\_SSRESID(Y,X) )

This expression displays the value of the result of each linest function against the corresponding name in the synthetic dimension. The result of Linest\_b(Y,X) is displayed next to linest\_b, and so on.

### Result

Results table

| Linest functions | Linest function results |
| --- | --- |
| Linest\_b | -35.047 |
| Linest\_df | 18 |
| Linest\_f | 20.788 |
| Linest\_m | 8.605 |
| Linest\_r2 | 0.536 |
| Linest\_SEB | 22.607 |
| Linest\_SEM | 1.887 |
| Linest\_SEY | 48.666 |
| Linest\_SSREG | 49235.014 |
| Linest\_SSRESID | 42631.186 |

## Example 3: Chart expressions using linest

Example: Chart expressions

1. Create a barchart visualization in a Qlik Sense sheet with X as a dimension and Y as a measure.
2. Add a linear trend line to the Y measure.
3. Add a KPI visualization to the sheet.
   1. Add slope as a label for the KPI.
   2. Add sum(Linest\_M) as an expression for the KPI.
4. Add a second KPI visualization to the sheet.
   1. Add intercept as a label for the KPI.
   2. Add Sum(Linest\_B) as an expression for the KPI.
5. Add a third KPI visualization to the sheet.
   1. Add coefficient of determination as a label for the KPI.
   2. Add Sum(Linest\_R2) as an expression for the KPI.

### Result

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/linest-charts.png)

### Explanation

The barchart shows the plotting of the X and Y data. Relevant linest() functions provide values for the linear regression equation that the trend line is based on, namely y = m \* x + b. The equation uses the "least squares" method to calculate a straight line (trend line) by returning an array that describes a line that best fits the data.

The KPIs display the results of the linest() functions sum(Linest\_M) for slope and sum(Linest\_B) for the Y intercept, which are [variables](#glossary-5 "Glossary term")in the linear regression equation, and the corresponding aggregated R2 value for coefficient of determination.
