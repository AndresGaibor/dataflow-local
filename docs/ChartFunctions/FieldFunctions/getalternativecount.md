---
title: "GetAlternativeCount - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FieldFunctions/getalternativecount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Field functions"]
---

# GetAlternativeCount - chart function

Expand/Collapse all

# GetAlternativeCount - chart function

GetAlternativeCount()
is used to find the number of alternative (light gray) values in the identified field.

Syntax:

GetAlternativeCount (field\_name)

Return data type:  integer

Information note

The colors used in the selection bar, and for each selection state, can be modified with a custom theme. If you are working with an application that uses a custom theme, you might notice that your selections do not display with the same colors that are described in this help topic.

Arguments

| Argument | Description |
| --- | --- |
| field\_name | The field containing the range of data to be measured. |

The following table lists other functions that are related to this function.

Related functions

| Function | Interaction |
| --- | --- |
| [*GetStateCounts - chart function*](getstatecounts.htm) | Using GetStateCounts(), you can combine the calculation of the following counts using a single function call:   - Count of selected included values. - Count of possible values. - Count of alternative values. - Count of excluded values, not including alternative and selected excluded values. - Count of selected excluded values. |
| [*GetSelectedCount - chart function*](getselectedcount.htm) | Returns the count of selected included values. |
| [*GetPossibleCount - chart function*](getpossiblecount.htm) | Returns the count of possible values. |
| [*GetAlternativeCount - chart function*](#) | Returns the count of excluded values, not including alternative and selected excluded values. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| GetAlternativeCount ([First name]) | Returns 0 if no selection has been made on the First Name field. If selections have been made, then the value returned is the total number of distinct available values less the number of values selected. |

## Example - GetAlternativeCount fundamentals

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

Load the data and open a sheet. Create a new filter pane and add this field as a dimension:

- FirstName

Add a KPI, and then create the following measure:

- =GetAlternativeCount (FirstName), to find the number of alternative values in the FirstName field.

The KPI with the GetAlternativeCount function appears with a value of 0. If you select Jane from the FirstName filter pane, the KPI returns the value 4 because there are four unique and excluded (gray) values. Now select Mark, so both Jane and Mark are selected. The KPI value for the GetAlternativeCount measure returns 3 because there are 3 unique and excluded values, John, Peter, and Sue.

KPI results showing 3 unique and excluded values after selecting Jane and Mark from the FirstName filter pane

![The filter pane shows two selections so the GetAlternativeCount KPI returns 3, because there are 3 alternative values that are unique and excluded from the selection.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetAltCnt-example.png "Click to view full size")

You can see how the values returned by the GetAlternativeCount function change as additional selections are made.

## Example - GetAlternativeCount scenario

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called CustomerTypeData.
- The following fields in the data table:

  - CustomerID
  - CustomerType

Load script

```
CustomerTypeData:
LOAD * INLINE [
CustomerID, CustomerType
C001, Retail
C002, Wholesale
C003, Distributor
C004, Retail
C005, Wholesale
];
```

Results

Load the data and open a sheet. Create a new filter pane and add this field as a dimension:

- CustomerType

Add a KPI, and then create the following measure:

- =GetAlternativeCount (CustomerType), to find the number of alternative values in the CustomerType field.

  The KPI with the GetAlternativeCount function appears with a value of 0 because no values are selected in the CustomerType field.

Select Retail from the CustomerType filter pane. The GetAlternativeCount returns the value 2 because there are two unique and excluded (light gray) values in the CustomerType field. .

KPI results showing 2 unique and excluded values after selecting Retail from the CustomerType filter pane

![The filter pane shows one selection so the GetAlternativeCount KPI returns 2, because there are 2 alternative values that are unique and excluded from the selection.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetAltCnt-example2.png "Click to view full size")

The results show that although there are multiple values, the GetAlternativeCount function displays only the unique count of the items not selected.

## Example - GetAlternativeCount scenario with available values

Chart expression

Overview

This example builds on the previous scenario. The dataset includes a second data table to demonstrate how selections in each field change the results returned by the GetAlternativeCount function.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into the following 2 inline data tables and corresponding fields:

  - CustomerTypeData: Includes the fields CustomerID and CustomerType.
  - CustomerSegment: Includes the fields CustomerType and Segment.

Load script

```
CustomerTypeData:
LOAD * INLINE [
CustomerID, CustomerType
C001, Retail
C002, Wholesale
C003, Distributor
C004, Retail
C005, Wholesale
];

CustomerSegment:
Load * Inline [
CustomerType, Segment
Retail, Fashion
Retail, Home
Wholesale, Fashion
Wholesale, Drinks
Distributor, Food
];
```

Results

1. Load the data and open a sheet. Create a new filter pane and add these fields as dimensions:

   - CustomerType
   - Segment
2. Add a KPI, and then create the following measure:

   - =GetAlternativeCount (CustomerType), to find the number of alternative values in the CustomerType field.

     The KPI with the GetAlternativeCount function appears with a value of 0 because no values are selected in the CustomerType or Segment fields.
3. Select Drinks and Fashion from the Segment filter. The KPI still returns 0 because no value is selected in the CustomerType field.

KPI results show zero unique and excluded values after selections in the Segment filter

![The GetAlternativeCount KPI returns 0 because no value is selected in the CustomerType filter.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetAltCnt-example3.png "Click to view full size")4. Select Retail in the CustomerType field and keep the selections in the Segment filter.

   The GetAlternativeCount function now returns 1 because there is only one unique and excluded (light gray) value in the CustomerType field, Wholesale.

KPI results show there is 1 unique and excluded value after selections in the CustomerType and Segment filters

![The GetAlternativeCount KPI returns 1 because there is only one alternative value that is unique and excluded from the selections in the CustomerType and Segment filters.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetAltCnt-example4.png "Click to view full size")

Although two values, Wholesale and Distributor, are not selected in the CustomerType field (these appear light gray and dark gray), only one value, Wholesale, is available to select in CustomerType due to selections in the Segment filter.
