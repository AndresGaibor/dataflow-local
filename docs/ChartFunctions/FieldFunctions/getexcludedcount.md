---
title: "GetExcludedCount - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FieldFunctions/getexcludedcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Field functions"]
---

# GetExcludedCount - chart function

Expand/Collapse all

# GetExcludedCount - chart function

GetExcludedCount() finds the number of excluded distinct values in the identified field. Only excluded (dark gray) fields are counted. Alternative (light gray) and selected excluded (dark gray with check mark) values are not counted.

Syntax:

GetExcludedCount (field\_name)

Return data type: integer

Information note

The colors used in the selection bar, and for each selection state, can be modified with a custom theme. If you are working with an application that uses a custom theme, you might notice that your selections do not display with the same colors that are described in this help topic.

Arguments

| Arguments | Description |
| --- | --- |
| field\_name | The field containing the range of data to be measured. |

The following table lists other functions that are related to this function.

Related functions

| Function | Interaction |
| --- | --- |
| [*GetStateCounts - chart function*](getstatecounts.htm) | Using GetStateCounts(), you can combine the calculation of the following counts using a single function call:   - Count of selected included values. - Count of possible values. - Count of alternative values. - Count of excluded values, not including alternative and selected excluded values. - Count of selected excluded values. |
| [*GetSelectedCount - chart function*](getselectedcount.htm) | Returns the count of selected included values. |
| [*GetPossibleCount - chart function*](getpossiblecount.htm) | Returns the count of possible values. |
| [*GetAlternativeCount - chart function*](getalternativecount.htm) | Returns the count of alternative values. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| GetExcludedCount( Initials ) | Returns 0 if no selection has been made. If a selection has been made then the value returned is the number of excluded values in Initials with dark gray color. |

## Example - GetExcludedCount fundamentals

Chart expression

Overview

This example shows how values that are returned by the GetExcludedCount function change as additional selections are made.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - FirstName
  - LastName
  - Initials
  - HasCellphone

Load script

```
Example:
LOAD * inline [
FirstName|LastName|Initials|HasCellphone
John|Anderson|JA|Yes
Sue|Brown|SB|Yes
Mark|Carr|MC|No
Peter|Devonshire|PD|No
Jane|Elliot|JE|Yes
Peter|Franc|PF|Yes ] (delimiter is '|');
```

Results

1. Load the data and open a sheet. Create a new filter pane and add these fields as dimensions:

- FirstName
- LastName
- Initials

2. Create three KPI objects and add the following expressions as measures, one per KPI object:

   1. =GetExcludedCount(FirstName), to count the number of excluded values in the FirstName field.
   2. =GetExcludedCount(Initials), to count the number of excluded values in the Initials field.
   3. =GetExcludedCount(LastName), to count the number of excluded values in the LastName field.

   Your sheet will look like the following image because no values have been selected. The GetExcludedCount function returns 0 for each KPI.

   ![A sheet with filter panes for First Name, Initials, and Last Name, as well as three KPI objects that each return a count of any excluded values in these fields. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetExclCnt-example.png)
3. Click Edit sheet to switch to analysis mode, and then make the following selections in order:

   Filter selections and results in analysis mode

   | Filter pane selection | KPI results |
   | --- | --- |
   | Select John in the FirstName filter. | - GetExcludedCount (Initials) returns a value of 5 because there are 5 excluded values in Initials with dark gray color. The JA value remains white as it is associated with the selection John in FirstName. - GetExcludedCount (LastName) returns a value of 5 because there are 5 excluded values in LastName with dark gray color. The Anderson value remains white as it is associated with the selection John in FirstName. |
   | Select John and Peter in the FirstName filter. | - GetExcludedCount (Initials) returns a value of 3 because there are 3 excluded values in Initials with dark gray color. - GetExcludedCount (LastName) returns a value of 3 because there are 3 excluded values in LastName with dark gray color. |
   | With John and Peter selected, select Franc in the LastName filter. | - GetExcludedCount (FirstName) returns a value of 3 because there are 3 excluded values in FirstName with dark gray color and no selection check mark. The GetExcludedCount function counts only excluded values. Alternative and selected excluded values are not included in the count. John is a selected excluded value. - GetExcludedCount (Initials) returns a value of 5 because there are 5 excluded values in Initials with dark gray color. - GetExcludedCount (LastName) returns a value of 3 because there are 3 excluded values in LastName with dark gray color. The 2 light gray color values, Anderson and Devonshire, are alternative values. |
   | Keep the previous selections, and then in the LastName filter, select Anderson. | - GetExcludedCount (FirstName) returns a value of 3 because there are 3 excluded values in FirstName with dark gray color. - GetExcludedCount (Initials) returns a value of 4 because there are 4 excluded values in Initials with dark gray color. - GetExcludedCount (LastName) returns a value of 3 because there are 3 excluded values in LastName with dark gray color. |

You can see the final results of the filter pane selections in the following image.

KPI results of selecting the first names, John and Peter, and last names, Franc and Anderson

![A sheet with selections on the First Name and Last Name fields, and the corresponding KPI results from these selections. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetExclCnt-example2.png "Click to view full size")

## Example - GetExcludedCount scenario

Chart expression

Overview

A sales manager uses the GetExcludedCount function to create a KPI chart to analyze products sold by salesperson.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Salesperson
  - Product
  - SalesAmount

Load script

```
Example:
LOAD * INLINE [
Salesperson, Product, SalesAmount
John, Laptops, 1000
Alice, Smartphones, 800
Bob, Laptops, 1200
Carol, Tablets, 700
Dave, Tablets, 900
];
```

Results

1. Load the data and open a sheet. Create a new filter pane and add these fields as dimensions:

   - Salesperson

- Product

2. Create a new KPI object and add the following measure:

   - =GetExcludedCount(Product), to find the number of excluded values in the Product field.
3. Click Edit sheet to switch to analysis mode, and then select Alice from the Salesperson filter.

   The GetExcludedCount function returns a value of 2 because there are 2 unique and excluded (dark gray) values in the Product field.

   ![A sheet with filter panes for First Name, Initials, and Last Name, as well as three KPI objects that each return a count of any excluded values in these fields. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetExclCnt-example3.png)

The results show how you can use the GetExcludedCount function to analyze the data. The salesperson Alice has not sold any items in 2 of the 3 product groups, Laptop and Tablet products.
