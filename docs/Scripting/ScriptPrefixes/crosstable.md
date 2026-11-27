---
title: "Crosstable"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/crosstable.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# Crosstable

Expand/Collapse all

# Crosstable

The crosstable load
prefix is used to transpose “cross table” or “pivot table” structured data. Data structured this way is commonly encountered when working with spreadsheet sources. The output and aim of the crosstable load
prefix is to transpose such structures into a regular column-oriented table equivalent, as this structure is generally better suited for analysis in Qlik Sense.

Example of data structured as a crosstable and its equivalent structure after a crosstable transformation

![Example that shows a cross table on the left. Table columns are Area, Lisa, James, Sharon. On the right is a table that has been transformed using a crosstable load. The table columns have been changed to Area, Sales Person, Target. The dimension data is the same in both tables.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-crosstable-overview.png "Click to view full size")

Syntax:

crosstable (attribute field name, data field name [ , n ] ) ( loadstatement |
selectstatement )

Arguments

| Argument | Description |
| --- | --- |
| attribute field name | The desired output field name describing the horizontally oriented [dimension](#glossary-0 "Glossary term") that is to be transposed (the header row). |
| data field name | The desired output field name which describes the horizontally oriented data of the dimension that is to be transposed (the matrix of data values beneath the header row). |
| n | The number of qualifier fields, or unchanged dimensions preceding the table to be transformed to generic form. The default value is 1. |

This scripting function is related to the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| [*Generic*](Generic.htm) | A transformation load prefix which takes an entity-attribute-value structured data set and transforms it into a regular relational table structure, separating each attribute encountered into a new field or column of data. |

## Example 1 – Transforming pivoted sales data (simple)

Load scripts and results

Overview

Open the [Data load editor](#glossary-1 "Glossary term") and add the first [load script](#glossary-2 "Glossary term") below to a new tab.

The first load script contains a [dataset](#glossary-3 "Glossary term") to which the crosstable script prefix will be applied later, with the section applying crosstable commented out. This means that comment syntax was used to disable this section in the load script.

The second load script is the same as the first, but with the application of crosstable uncommented (enabled by removing the comment syntax). The scripts are shown this way to highlight the value of this scripting function in transforming data.

First load script (function not applied)

```
tmpData:
//Crosstable (MonthText, Sales)
Load * inline [
Product, Jan 2021, Feb 2021, Mar 2021, Apr 2021, May 2021, Jun 2021
A, 100, 98, 103, 63, 108, 82
B, 284, 279, 297, 305, 294, 292
C, 50, 53, 50, 54, 49, 51];

//Final:
//Load Product,
//Date(Date#(MonthText,'MMM YYYY'),'MMM YYYY') as Month,
//Sales

//Resident tmpData;

//Drop Table tmpData;
```

For more information about using inline loads, see [*Using inline loads to load data*](../inline-loads-qs.htm).

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Product
- Jan 2021
- Feb 2021
- Mar 2021
- Apr 2021
- May 2021
- Jun 2021

Results table

| Product | Jan 2021 | Feb 2021 | Mar 2021 | Apr 2021 | May 2021 | Jun 2021 |
| --- | --- | --- | --- | --- | --- | --- |
| A | 100 | 98 | 103 | 63 | 108 | 82 |
| B | 284 | 279 | 297 | 305 | 294 | 292 |
| C | 50 | 53 | 50 | 54 | 49 | 51 |

This script allows the creation of a crosstable with one column for each month and one row per product. In its current format, this data is not easy to analyze. It would be much better to have all numbers in one field and all months in another, in a three-column table. The next section explains how to do this transformation to the crosstable.

Second load script (function applied)

Uncomment the script by removing the
//. The load script should look like this:

```
tmpData:
Crosstable (MonthText, Sales)
Load * inline [
Product, Jan 2021, Feb 2021, Mar 2021, Apr 2021, May 2021, Jun 2021
A, 100, 98, 103, 63, 108, 82
B, 284, 279, 297, 305, 294, 292
C, 50, 53, 50, 54, 49, 51];

Final:
Load Product,
Date(Date#(MonthText,'MMM YYYY'),'MMM YYYY') as Month,
Sales

Resident tmpData;

Drop Table tmpData;
```

For more information about using inline loads, see [*Using inline loads to load data*](../inline-loads-qs.htm).

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Product
- Month
- Sales

Results table

| Product | Month | Sales |
| --- | --- | --- |
| A | Jan 2021 | 100 |
| A | Feb 2021 | 98 |
| A | Mar 2021 | 103 |
| A | Apr 2021 | 63 |
| A | May 2021 | 108 |
| A | Jun 2021 | 82 |
| B | Jan 2021 | 284 |
| B | Feb 2021 | 279 |
| B | Mar 2021 | 297 |
| B | Apr 2021 | 305 |
| B | May 2021 | 294 |
| B | Jun 2021 | 292 |
| C | Jan 2021 | 50 |
| C | Feb 2021 | 53 |
| C | Mar 2021 | 50 |
| C | Apr 2021 | 54 |
| C | May 2021 | 49 |
| C | Jun 2021 | 51 |

Once the script prefix has been applied, the crosstable is transformed into a straight table with one column for Month and another for Sales. This improves the readability of the data.

## Example 2 – Transforming pivoted sales target data into a vertical table structure (intermediate)

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table named Targets.
- The crosstable load prefix, which transposes the pivoted sales person names into a field of its own, labeled Sales Person.
- The associated sales target data, which is structured into a field called Target.

Load script

```
SalesTargets:
CROSSTABLE([Sales Person],Target,1)
LOAD
*
INLINE [
Area, Lisa, James, Sharon
APAC, 1500, 1750, 1850
EMEA, 1350, 950, 2050
NA, 1800, 1200, 1350
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Area
- Sales Person

Add this [measure](#glossary-4 "Glossary term"):

=Sum(Target)

Results table

| Area | Sales Person | =Sum(Target) |
| --- | --- | --- |
| APAC | James | 1750 |
| APAC | Lisa | 1500 |
| APAC | Sharon | 1850 |
| EMEA | James | 950 |
| EMEA | Lisa | 1350 |
| EMEA | Sharon | 2050 |
| NA | James | 1200 |
| NA | Lisa | 1800 |
| NA | Sharon | 1350 |

If you want to replicate the display of data as the pivoted input table, you can create an equivalent pivot table in a [sheet](#glossary-5 "Glossary term").

Do the following:

1. Copy and paste the table you have just created into the sheet.
2. Drag the Pivot table chart object on top of the newly created table copy. Select Convert.
3. Click Edit sheet to finish editing.
4. Drag the Sales Person field from the vertical column shelf to the horizontal column shelf.

The following table shows the data in its initial table form, as it is displayed in Qlik Sense:

Original results table, as shown in Qlik Sense

| Area | Sales Person | =Sum(Target) |
| --- | --- | --- |
| Totals | - | 13800 |
| APAC | James | 1750 |
| APAC | Lisa | 1500 |
| APAC | Sharon | 1850 |
| EMEA | James | 950 |
| EMEA | Lisa | 1350 |
| EMEA | Sharon | 2050 |
| NA | James | 1200 |
| NA | Lisa | 1800 |
| NA | Sharon | 1350 |

The equivalent pivot table looks similar to the following, with the column for each sales person's name being contained within the larger row for Sales Person:

Equivalent pivot table with the Sales Person field pivoted horizontally

| Area | James | Lisa | Sharon |
| --- | --- | --- | --- |
| APAC | 1750 | 1500 | 1850 |
| EMEA | 950 | 1350 | 2050 |
| NA | 1350 | 1350 | 1350 |

Example of data displayed as a table and an equivalent pivot table with the Sales Person field pivoted horizontally

![Example of data transformation using the crosstable function. The function converts the initial pivot table to an equivalent table with 'Sales Person' field being pivoted horizontally.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-crosstable-example-pivot-table-comp.png "Click to view full size")

## Example 3 – Transforming pivoted sales and target data into a vertical table structure (advanced)

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset representing sales and targets data, organized by area and month of the year. This is loaded into a table called SalesAndTargets.
- The crosstable load prefix. This is used to unpivot the Month Year dimension into a dedicated field, as well as to transpose the matrix of sales and target amounts into a dedicated field called Amount.
- A conversion of the Month Year field from text to a proper date, using the text-to-date conversion function date#. This date-converted Month Year field is joined back onto the SalesAndTarget table via a Join load prefix.

Load script

```
SalesAndTargets:
CROSSTABLE(MonthYearAsText,Amount,2)
LOAD
	*
INLINE [
Area	Type	Jan-22	Feb-22	Mar-22	Apr-22	May-22	Jun-22	Jul-22	Aug-22	Sep-22	Oct-22	Nov-22	Dec-22
APAC	Target	425	425	425	425	425	425	425	425	425	425	425	425
APAC	Actual	435	434	397	404	458	447	413	458	385	421	448	397
EMEA	Target	362.5	362.5	362.5	362.5	362.5	362.5	362.5	362.5	362.5	362.5	362.5	362.5
EMEA	Actual	363.5	359.5	337.5	361.5	341.5	337.5	379.5	352.5	327.5	337.5	360.5	334.5
NA	Target	375	375	375	375	375	375	375	375	375	375	375	375
NA	Actual	378	415	363	356	403	343	401	365	393	340	360	405
] (delimiter is '\t');

tmp:
LOAD DISTINCT MonthYearAsText,date#(MonthYearAsText,'MMM-YY') AS [Month Year]
RESIDENT SalesAndTargets;

JOIN (SalesAndTargets)
LOAD * RESIDENT tmp;

DROP TABLE tmp;
DROP FIELD MonthYearAsText;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Area
- Month Year

Create the following measure, with the label Actual:

=Sum({<Type={'Actual'}>} Amount)

Also create this measure, with the label Target:

=Sum({<Type={'Target'}>} Amount)

Results table (cropped)

| Area | Month Year | Actual | Target |
| --- | --- | --- | --- |
| APAC | Jan-22 | 435 | 425 |
| APAC | Feb-22 | 434 | 425 |
| APAC | Mar-22 | 397 | 425 |
| APAC | Apr-22 | 404 | 425 |
| APAC | May-22 | 458 | 425 |
| APAC | Jun-22 | 447 | 425 |
| APAC | Jul-22 | 413 | 425 |
| APAC | Aug-22 | 458 | 425 |
| APAC | Sep-22 | 385 | 425 |
| APAC | Oct-22 | 421 | 425 |
| APAC | Nov-22 | 448 | 425 |
| APAC | Dec-22 | 397 | 425 |
| EMEA | Jan-22 | 363.5 | 362.5 |
| EMEA | Feb-22 | 359.5 | 362.5 |

If you wish to replicate the display of data as the pivoted input table, you can create an equivalent pivot table in a sheet.

Do the following:

1. Copy and paste the table you have just created into the sheet.
2. Drag the Pivot table chart object on top of the newly created table copy. Select Convert.
3. Click Edit sheet to finish editing.
4. Drag the Month Year field from the vertical column shelf to the horizontal column shelf.
5. Drag the Values item from the horizontal column shelf to the vertical column shelf.

The following table shows the data in its initial table form, as it is displayed in Qlik Sense:

Original results table (cropped), as shown in Qlik Sense

| Area | Month Year | Actual | Target |
| --- | --- | --- | --- |
| Totals | - | 13812 | 13950 |
| APAC | Jan-22 | 435 | 425 |
| APAC | Feb-22 | 434 | 425 |
| APAC | Mar-22 | 397 | 425 |
| APAC | Apr-22 | 404 | 425 |
| APAC | May-22 | 458 | 425 |
| APAC | Jun-22 | 447 | 425 |
| APAC | Jul-22 | 413 | 425 |
| APAC | Aug-22 | 458 | 425 |
| APAC | Sep-22 | 385 | 425 |
| APAC | Oct-22 | 421 | 425 |
| APAC | Nov-22 | 448 | 425 |
| APAC | Dec-22 | 397 | 425 |
| EMEA | Jan-22 | 363.5 | 362.5 |
| EMEA | Feb-22 | 359.5 | 362.5 |

The equivalent pivot table looks similar to the following, with the column for each individual month of the year being contained within the larger row for Month Year:

Equivalent pivot table (cropped) with the Month Year field pivoted horizontally

| Area (Values) | Jan-22 | Feb-22 | Mar-22 | Apr-22 | May-22 | Jun-22 | Jul-22 | Aug-22 | Sep-22 | Oct-22 | Nov-22 | Dec-22 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| APAC - Actual | 435 | 434 | 397 | 404 | 458 | 447 | 413 | 458 | 385 | 421 | 448 | 397 |
| APAC - Target | 425 | 425 | 425 | 425 | 425 | 425 | 425 | 425 | 425 | 425 | 425 | 425 |
| EMEA - Actual | 363.5 | 359.5 | 337.5 | 361.5 | 341.5 | 337.5 | 379.5 | 352.5 | 327.5 | 337.5 | 360.5 | 334.5 |
| EMEA - Target | 362.5 | 362.5 | 362.5 | 362.5 | 362.5 | 362.5 | 362.5 | 362.5 | 362.5 | 362.5 | 362.5 | 362.5 |
| NA - Actual | 378 | 415 | 363 | 356 | 403 | 343 | 401 | 365 | 393 | 340 | 360 | 405 |
| NA - Target | 375 | 375 | 375 | 375 | 375 | 375 | 375 | 375 | 375 | 375 | 375 | 375 |

Example of data displayed as a table and an equivalent pivot table with the Month Year field pivoted horizontally

![Example of data displayed as a table and an equivalent pivot table, with the Month Year field pivoted horizontally.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-crosstable-advanced-example-pivot-table-comp2.png "Click to view full size")

## Learn more

- [*Working with crosstables in the data load script*](../../LoadData/work-with-cross-tables.htm)
- [*Generic*](Generic.htm)
- [*Load*](../ScriptRegularStatements/Load.htm)
- [*Select*](../ScriptRegularStatements/Select.htm)
