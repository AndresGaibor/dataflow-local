---
title: "GetFieldSelections - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FieldFunctions/getfieldselections.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Field functions"]
---

# GetFieldSelections - chart function

Expand/Collapse all

# GetFieldSelections - chart function

GetFieldSelections() returns a string with the current selections in a field.

If all but two, or all but one of the values are selected, the format 'NOT x,y' or 'NOT y' will be used respectively. If you select all values and the count of all values is greater than max\_values, the text ALL will be returned.

Syntax:

GetFieldSelections (
field\_name [, value\_sep [, max\_values [, state\_name]]])

Return data type:  string

Return string formats

| Format | Description |
| --- | --- |
| 'a, b, c' | If the number of selected values is max\_values or less, the string returned is a list of the selected values.  The values are separated with value\_sep as delimiter. |
| 'NOT a, b, c' | If the number of non-selected values is max\_values or less, the string returned is a list of the non-selected values with NOT as a prefix.  The values are separated with value\_sep as delimiter. |
| 'x of y' | x = the number of selected values  y = the total number of values  This is returned when max\_values < x < ( y - max\_values). |
| 'ALL' | Returned if all values are selected. |
| '-' | Returned if no value is selected. |
| <search string> | If you have selected using search, the search string is returned. |

Arguments

| Arguments | Description |
| --- | --- |
| field\_name | The field containing the range of data to be measured. |
| value\_sep | The separator to be put between field values. The default is ', '. |
| max\_values | The maximum number of field values to be individually listed. When a larger number of values is selected, the format 'x of y values' will be used instead. The default is 6. |
| state\_name | The name of an alternate state that has been chosen for the specific visualization. If the state\_name argument is used, only the selections associated with the specified state name are taken into account.  For more information, see [*Using alternate states for comparative analysis*](../../Visualizations/alternate-states-comparative-analysis.htm). |

Example: Chart expressions

| Example | Result |
| --- | --- |
| GetFieldSelections( FirstName ) | Returns '-' (NULL) if no selection has been made in the FirstName field. Otherwise, it returns the value of the selections, for example John. |

## Example - GetFieldSelections fundamentals

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

1. Load the data and open a sheet. Create a new filter pane and add this field as a dimension:

   - FirstName
2. Create a KPI object and add the following measure:

   - =GetFieldSelections(FirstName), to return the values of the selection made in the FirstName field.

   Tip noteIn this example the styling of the KPI has been adjusted to use a responsive layout behavior to make it easier to view the output. For more information about changing the chart layout behavior, see [*Styling the KPI*](../../Visualizations/KPI/create-kpis.htm#Styling)
3. Click Edit sheet to switch to analysis mode, and do the following actions in the order that they appear in the table:

   Actions and results in analysis mode

   | Action | KPI results |
   | --- | --- |
   | Select John in the FirstName filter. | The measure returns the value: John. |
   | Select John and Peter in the FirstName filter. | The measure returns the values: John, Peter. |
   | Click Edit sheet to switch to edit mode, and then edit the KPI measure expression to the following: =GetFieldSelections(FirstName,'; ') | The measure returns the values with the new value\_sep format: John; Peter. |
   | Edit the KPI measure expression to the following: =GetFieldSelections(FirstName,';', 2) | The measure returns the values with the new value\_sep format spacing: John;Peter. |
   | Click Edit sheet to switch back to analysis mode. Clear the selections from the FirstName filter, and then select John, Sue, and Mark. | The measure returns NOT Jane;Peter, because the number of selections exceeds the max\_value argument of 2. If no max\_value is set, all selected names will appear: John; Sue; Mark. |

The following image shows the results of the last action in the table where the number of selections exceeds the max\_values argument.

KPI results when selecting the first names John, Sue, and Mark

![KPI and filter pane showing selections that exceed the maximum values in the GetFieldSelections function.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetFldSel-example.png "Click to view full size")

In this example you can see how the values returned by the GetFieldSelections function change as selections are made.

## Example - GetFieldSelections scenario

Chart expression

Overview

The GetFieldSelections function is used to highlight customer names as they are selected.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - OrderID
  - CustomerName
  - Product
  - Quantity

Load script

```
Example:
LOAD * INLINE [
OrderID, CustomerName, Product, Quantity
1, John Doe, Laptop, 2
2, Jane Smith, Smartphone, 1
3, Ahmed Khan, Desk, 3
4, Maria Garcia, Chair, 1
5, Li Wei, Blender, 2
];
```

Results

1. Load the data and open a sheet. Create a new filter pane and add these fields as dimensions:

- CustomerName
- Product

2. Create a KPI object and add the following measure:

   - =GetFieldSelections(CustomerName).

   Tip noteIn this example the styling of the KPI has been adjusted to use a responsive layout behavior to make it easier to view the output. For more information about changing the chart layout behavior, see [*Styling the KPI*](../../Visualizations/KPI/create-kpis.htm#Styling).
3. Click Edit sheet to switch to analysis mode, and then select Jane Smith and John Doe from the CustomerName filter.

   The GetFieldSelections function returns the values: Jane Smith, John Doe.

   ![KPI results show which names are selected in the Customer Name filter.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetFldSel-example2.png)

You can see the customers selected in the filter pane in the KPI.
