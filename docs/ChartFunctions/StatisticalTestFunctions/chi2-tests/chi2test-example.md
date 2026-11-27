---
title: "Examples of how to use chi2-test functions in charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/chi2-tests/chi2test-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions", "Statistical test function examples"]
---

# Examples of how to use chi2-test functions in charts

The chi2-test functions are used to find values associated with chi squared statistical analysis.

This section describes how to build [visualizations](#glossary-0 "Glossary term") using sample data to find the values of the chi-squared distribution test functions available in Qlik Sense. Please refer to the individual chi2-test chart function topics for descriptions of syntax and arguments.

## Loading the data for the samples

There are three sets of sample data describing three different statistical samples to be loaded into the script.

Do the following:

1. Create a new app.
2. In the data load, enter the following:

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

   // Sample\_2 data is pre-aggregated: If raw data is used, it must be aggregated using count()...

   Sample\_2:

   LOAD \* inline [

   Sex,Opinion,OpCount

   1,2,58

   1,1,11

   1,0,10

   2,2,35

   2,1,25

   2,0,23 ] (delimiter is ',');

   // Sample\_3a data is transformed using the crosstable statement...

   Sample\_3a:

   crosstable(Gender, Actual) LOAD

   Description,

   [Men (Actual)] as Men,

   [Women (Actual)] as Women;

   LOAD \* inline [

   Men (Actual),Women (Actual),Description

   58,35,Agree

   11,25,Neutral

   10,23,Disagree ] (delimiter is ',');

   // Sample\_3b data is transformed using the crosstable statement...

   Sample\_3b:

   crosstable(Gender, Expected) LOAD

   Description,

   [Men (Expected)] as Men,

   [Women (Expected)] as Women;

   LOAD \* inline [

   Men (Expected),Women (Expected),Description

   45.35,47.65,Agree

   17.56,18.44,Neutral

   16.09,16.91,Disagree ] (delimiter is ',');

   // Sample\_3a and Sample\_3b will result in a (fairly harmless) Synthetic Key...
3. Click ![run script](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_run_script.svg) to load data.

## Creating the chi2-test chart function visualizations

Example: Sample 1

Do the following:

1. In the data load editor, click ![compass](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_compass.svg) to go to the app view and then click the [sheet](#glossary-1 "Glossary term") you created before.

   The sheet view is opened.
2. Click![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet to edit the sheet.
3. From Charts add a table, and from Fields add Grp, Grade, and Count as [dimensions](#glossary-2 "Glossary term").

   This table shows the sample data.
4. Add another table with the following expression as a dimension.

   ValueList('p','df','Chi2')

   This uses the synthetic dimensions function to create labels for the dimensions with the names of the three chi2-test functions.
5. Add the following expression to the table as a [measure](#glossary-3 "Glossary term").

   IF(ValueList('p','df','Chi2')='p',Chi2Test\_p(Grp,Grade,Count),

   IF(ValueList('p','df','Chi2')='df',Chi2Test\_df(Grp,Grade,Count),

   Chi2Test\_Chi2(Grp,Grade,Count)))

   This has the effect of putting the resulting value of each chi2-test function in the table next to its associated synthetic dimension.
6. Set the Number formatting of the measure to Number and 3Significant figures.

Tip noteIn the expression for the measure, you could use the following expression instead: Pick(Match(ValueList('p','df','Chi2'),'p','df','Chi2'),Chi2Test\_p(Grp,Grade,Count),Chi2Test\_df(Grp,Grade,Count),Chi2Test\_Chi2(Grp,Grade,Count))

Result:

The resulting table for the chi2-test functions for the Sample 1 data will contain the following values:

Results table

| p | df | Chi2 |
| --- | --- | --- |
| 0.820 | 5 | 2.21 |

Example: Sample 2

Do the following:

1. In the sheet you were editing in the example Sample 1, from Charts add a table, and from Fields add Sex, Opinion, and OpCount as dimensions.
2. Make a copy of the results table from Sample 1 using the Copy and Paste commands. Edit the expression in the measure and replace the arguments in all three chi2-test functions with the names of the fields used in the Sample 2 data, for example: Chi2Test\_p(Sex,Opinion,OpCount).

Result:

The resulting table for the chi2-test functions for the Sample 2 data will contain the following values:

Results table

| p | df | Chi2 |
| --- | --- | --- |
| 0.000309 | 2 | 16.2 |

Example: Sample 3

Do the following:

1. Create two more tables in the same way as in the examples for Sample 1 and Sample 2 data. In the dimensions table, use the following fields as dimensions: Gender, Description, Actual, and Expected.
2. In the results table, use the names of the fields used in the Sample 3 data, for example: Chi2Test\_p(Gender,Description,Actual,Expected).

Result:

The resulting table for the chi2-test functions for the Sample 3 data will contain the following values:

Results table

| p | df | Chi2 |
| --- | --- | --- |
| 0.000308 | 2 | 16.2 |
