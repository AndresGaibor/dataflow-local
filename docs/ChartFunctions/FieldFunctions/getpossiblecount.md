---
title: "GetPossibleCount - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FieldFunctions/getpossiblecount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Field functions"]
---

# GetPossibleCount - chart function

Expand/Collapse all

# GetPossibleCount - chart function

GetPossibleCount() is used to find the number of possible values in the identified field. If the identified field includes selections, then the selected (green) fields are counted. Otherwise associated (white) values are counted.

For fields with [selections](#glossary-0 "Glossary term"), GetPossibleCount() returns the number of selected (green) fields.

Syntax:

GetPossibleCount (field\_name)

Return data type:  integer

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
| [*GetAlternativeCount - chart function*](getalternativecount.htm) | Returns the count of alternative values. |
| [*GetPossibleCount - chart function*](#) | Returns the count of excluded values, not including alternative and selected excluded values. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| GetPossibleCount( Initials ) | If no selections are made then it returns the total number of unique values in the field Initials. If one value in this field is selected then it returns 1. If a selection is made on another field then the value returned is the number of unique values in the Initials field that relate to the values selected in the second field. |

## Example - GetPossibleCount fundamentals

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

   - KPI 1: =GetPossibleCount(FirstName) to return the number of possible unique values in the FirstName field.
   - KPI 2: =GetPossibleCount(Initials), to return the number of possible unique values in the Initials field.

   Each KPI returns the number of possible unique values. With no selections in the filter, KPI 1 returns the value 5 and KPI 2 returns the value 6.

   Tip noteIn this example the styling of the KPI has been adjusted to use a responsive layout behavior to make it easier to view the output. For more information about changing the chart layout behavior, see [*Styling the KPI*](../../Visualizations/KPI/create-kpis.htm#Styling)
3. Click Edit sheet to switch to analysis mode and select John in the FirstName filter.

   Both KPIs return the value 1 because there is one value selected in the FirstName field and JA is the only associated value in the Initials field.
4. Clear the FirstName filter selection, and then select Peter.

   KPI 1 returns the value 1 because there is one possible unique value available in the FirstName field. KPI 2 returns 2 because there are two possible unique values available in the Initials field.

   ![Two KPIs with two associated filter panes. Each KPI shows the number of possible unique values for each field from the output of the GetPossibleCount function.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetPosCnt-example.png)

## Example - GetPossibleCount scenario

Chart expression

Overview

A manager wants to filter employee data to determine which employees have experience in different skill areas.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Project
  - Employee
  - Skill

Load script

```
Example:
LOAD * INLINE [
Project, Employee, Skill
Project X, John, Java
Project X, Mary, SQL
Project Y, James, Python
Project Y, Linda, Java
Project Z, Robert, SQL
];
```

Results

1. Load the data and open a sheet. Create a new filter pane and add this field as a dimension:

- Skill

2. Create a KPI object, and add the following measure:

   - =GetPossibleCount(Employee) to determine the number of employees.

   With no selections in the filter pane, the KPI returns the value 5 because there are five employees.

   Tip noteIn this example the styling of the KPI has been adjusted to use a responsive layout behavior to make it easier to view the output. For more information about changing the chart layout behavior, see [*Styling the KPI*](../../Visualizations/KPI/create-kpis.htm#Styling)
3. Click Edit sheet to switch to analysis mode and select Java in the Skill filter.

   The KPI returns the value 2 because there are two employees who have the skill Java.

   ![Two KPIs with two associated filter panes. Each KPI shows the number of possible unique values for each field from the output of the GetPossibleCount function.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetPosCnt-example2.png)
