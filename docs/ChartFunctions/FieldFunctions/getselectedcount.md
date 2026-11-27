---
title: "GetSelectedCount - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FieldFunctions/getselectedcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Field functions"]
---

# GetSelectedCount - chart function

Expand/Collapse all

# GetSelectedCount - chart function

GetSelectedCount() finds the number of selected (green) values in a field.

Syntax:

GetSelectedCount (field\_name
[, include\_excluded [, state\_name]])

Return data type:  integer

Information note

The colors used in the selection bar, and for each selection state, can be modified with a custom theme. If you are working with an application that uses a custom theme, you might notice that your selections do not display with the same colors that are described in this help topic.

Arguments

| Arguments | Description |
| --- | --- |
| field\_name | The field containing the range of data to be measured. |
| include\_excluded | If set to True(), the count will include selected values, which are currently excluded by [selections](#glossary-0 "Glossary term") in other fields. If False or omitted, these values will not be included. |
| state\_name | The name of an alternate state that has been chosen for the specific visualization. If the state\_name argument is used, only the selections associated with the specified state name are taken into account.  For more information, see [*Using alternate states for comparative analysis*](../../Visualizations/alternate-states-comparative-analysis.htm). |

The following table lists other functions that are related to this function.

Related functions

| Function | Interaction |
| --- | --- |
| [*GetStateCounts - chart function*](getstatecounts.htm) | Using GetStateCounts(), you can combine the calculation of the following counts using a single function call:   - Count of selected included values. - Count of possible values. - Count of alternative values. - Count of excluded values, not including alternative and selected excluded values. - Count of selected excluded values. |
| [*GetPossibleCount - chart function*](getpossiblecount.htm) | Returns the count of possible values. |
| [*GetAlternativeCount - chart function*](getalternativecount.htm) | Returns the count of alternative values. |
| [*GetSelectedCount - chart function*](#) | Returns the count of excluded values, not including alternative and selected excluded values. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| GetSelectedCount (FirstName) | If no selections are made then 0 is returned. If any selections have been made in the FirstName field then the number of items selected is returned. |
| GetSelectedCount (FirstName, True()) | If no selections are made then 0 is returned. If any selections have been made in the FirstName field then the number of items selected is returned regardless of any subsequent selections in other fields that might reduce the available values in the FirstName field. |

## Example - GetSelectedCount fundamentals

Chart expression

Overview

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
- Initials

2. Create two KPI objects, one for each of the following measure expressions:

   - KPI 1: =GetSelectedCount(FirstName) to return the number of items selected in the FirstName field.
   - KPI 2: =GetSelectedCount(Initials), to return the number of items selected in the Initials field.

   Each KPI returns the number of selected items in each field. With no selections in the filters, both KPIs return the value 0.

   Tip noteIn this example the styling of the KPI has been adjusted to use a responsive layout behavior to make it easier to view the output. For more information about changing the chart layout behavior, see [*Styling the KPI*](../../Visualizations/KPI/create-kpis.htm#Styling)
3. Click Edit sheet to switch to analysis mode, and then select John in the FirstName filter.

   KPI 1 returns the value 1 because there is one item selected in the FirstName filter. KPI 2 still returns 0 because the Initials filter has no selected items.

   ![Two KPIs with two associated filter panes. Each KPI shows the number of selected items for each field from the output of the GetSelectedCount function.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetSelCnt-example.png)

## Example - GetSelectedCount with include\_excluded parameter

Chart expression

Overview

This example uses the same dataset as the previous example, but demonstrates the difference in results when the include\_excluded parameter is set to True().

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

- Initials
- HasCellPhone

2. Create two KPI objects, one for each of the following measure expressions:

   - KPI 1: =GetselectedCount(Initials) to determine the number of values that have been selected in the Initials field.
   - KPI 2: =GetSelectedCount([Initials], True()) to include the selected values which are currently excluded by selections in other fields.

   With no selections in the filter pane, each KPI returns the value 0.

   Tip noteIn this example the styling of the KPI has been adjusted to use a responsive layout behavior to make it easier to view the output. For more information about changing the chart layout behavior, see [*Styling the KPI*](../../Visualizations/KPI/create-kpis.htm#Styling)
3. Click Edit sheet to switch to analysis mode. Select all values in the Initials filter, and then select Yes in the HasCellphone filter.

   ![Two KPIs with two associated filter panes. Each KPI shows the number of possible unique values for each field from the output of the GetPossibleCount function.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetSelCnt-example2.png)

When you compare the results of each KPI, you can see how each returns a different value depending on whether the include\_excluded parameter is set to True() or not. KPI 2 returns the value 6 because it includes all selected values in the Initials filter, even though the selection in the HasCellphone filter has reduced the available items to 4. KPI 1 returns 4 because it does not count the selected excluded values in Initials.
