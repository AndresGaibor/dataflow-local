---
title: "Examples of how to use chi2-test functions in the data load script"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalTestFunctions/chi2Tests/chi2test-script-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions"]
---
# Examples of how to use chi2-test functions in the data load script

The chi2-test functions are used to find values associated with chi squared statistical analysis. This section describes how to use the chi-squared distribution test functions available in Qlik Sense in the [data load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalTestFunctions/chi2Tests/chi2test-script-example.htm#glossary-0 "Glossary term"). Please refer to the individual chi2-test script function topics for descriptions of syntax and arguments.

This example uses a table containing the number of students achieving a grade (A-F) for two groups of students (I and II).

Data table

| Group | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- |
| I | 15 | 7 | 9 | 20 | 26 | 19 |
| II | 10 | 11 | 7 | 15 | 21 | 16 |

## Loading the sample data

Do the following:

1. Create a new application.
2. In the data load editor, enter the following:

   // Sample\_1 data is pre-aggregated... Note: make sure you set your DecimalSep='.' at the top of the script.

   Sample\_1:

   LOAD \* inline [

   Grp,Grade,Count

   I,A,15

   I,B,7

   I,C,9

   I,D,20

   I,E,26

   I,F,19

   II,A,10

   II,B,11

   II,C,7

   II,D,15

   II,E,21

   II,F,16

   ];
3. Click ![run script](../../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_run_script.svg) to load data.

You have now loaded the sample data.

## Loading the chi2-test function values

Now we will load the chi2-test values based on the sample data in a new table, grouped by Grp.

Do the following:

1. In the data load editor, add the following at the end of the script:

   // Sample\_1 data is pre-aggregated... Note: make sure you set your DecimalSep='.' at the top of the script.

   Chi2\_table:

   LOAD
   Grp,

   Chi2Test\_chi2(Grp, Grade, Count) as chi2,

   Chi2Test\_df(Grp, Grade, Count) as df,

   Chi2Test\_p(Grp, Grade, Count) as p

   resident Sample\_1 group by Grp;
2. Click ![run script](../../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_run_script.svg) to load data.

You have now loaded the chi2-test values in a table named Chi2\_table.

## Results

You can view the resulting chi2-test values in the data model viewer under **Preview**, they should look like this:

Results

| Grp | chi2 | df | p |
| --- | --- | --- | --- |
| I | 16.00 | 5 | 0.007 |
| II | 9.40 | 5 | 0.094 |
