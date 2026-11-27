---
title: "GetStateCounts - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FieldFunctions/getstatecounts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Field functions"]
---

# GetStateCounts - chart function

Expand/Collapse all

# GetStateCounts - chart function

The
GetStateCounts() chart function is used to calculate the total number of unique values matching the specified [selection](#glossary-0 "Glossary term") states.

With
GetStateCounts(), you can combine the calculations from the following functions into a single function call: GetSelectedCount(), GetNotSelectedCount(), GetAlternativeCount(), GetPossibleCount(), and GetExcludedCount(). The count of selected excluded values is also available to add to the calculation. You can specify whether each function calculation adds or subtracts from the returned total.

Syntax:

GetStateCounts (field\_name, state\_name [, state\_type1,...state\_typeN])

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| field\_name | The field for which you are calculating the selection state. A non-existing field name results in a null outcome. |
| state\_name | The name of the alternate state. If the argument is empty ('') or null, the inherited alternate state is used. Use $ to explicitly use the default state. A named (non-empty) state name that doesn't match an existing state results in a null outcome. |
| state\_type | A list of one or more state types for the field value. These state types will be aggregated into a count. A state type is specified using a key. Enter each key with single quotation marks.  When this argument is omitted, the function returns a string with all available state counts for the field, in the same order as the enumeration.  For a list of states you can use, see the table below. |

State types are referenced using specific keys. You can use the numeric or textual version of the key. Combine more than one key in the same expression to further customize the result. You can subtract the state count from the total, rather than adding it. To do this, use the textual key and prefix the state type with a minus symbol (-).

The state type, and if applicable, the minus symbol, need to be enclosed in a set of single quotation marks.

Keys for each field state type

| Field state type | Description | Numeric key | Textual key |
| --- | --- | --- | --- |
| Selected | Includes selected values in the calculation. For the equivalent function, see [*GetSelectedCount - chart function*](getselectedcount.htm). | 1 | S |
| Optional | Includes optional (not selected, but possible to select) values in the calculation. For the equivalent function, see [*GetPossibleCount - chart function*](getpossiblecount.htm). | 2 | O |
| Deselected | Includes not-selected values in the calculation. This state type is only available when the field is in AND-mode. | 3 | D |
| Alternative | Includes alternative values in the calculation. For the equivalent function, see [*GetAlternativeCount - chart function*](getalternativecount.htm). | 4 | A |
| Excluded | Includes excluded (not selected) values in the calculation. For the equivalent function, see [*GetExcludedCount - chart function*](getexcludedcount.htm). | 5 | X |
| Selected excluded | Includes selected excluded values in the calculation. | 6 | XS |

## When to use GetStateCounts

With
GetStateCounts(), you can calculate a custom selection state. The function allows you to consolidate multiple function calls into a single function call, simplifying the process of writing your expression.

For example, you might need to calculate the total number of excluded, alternative, and selected excluded values for a field. You can use
GetStateCounts() to calculate this total.

Examples: Chart expressions

| Examples | Results |
| --- | --- |
| =GetStateCounts( ProductName, Null(), 'S' ) | Returns the selected count for ProductName, in the inherited alternate state. |
| =GetStateCounts( ProductName, '', 'X', 'A', 'XS' ) | Returns the total count of excluded, selected excluded, and alternative values for ProductName. The inherited alternate state is used. |
| =GetStateCounts( ProductName, '', 'S', 'XS' ) | Returns the total count of user selections for ProductName, in the inherited state. |
| Given that the ProductName field is in and-mode.  =GetStateCounts(ProductName, '', 'D', '-O') | Returns the number of not-selected values, subtracted by the number of possible values, for ProductName. The inherited alternate state is used. |
| =GetStateCounts(ProductName, '', 'X', , 'A', 'XS') | Returns the total count of excluded, selected excluded, and alternative values for ProductName. The inherited alternate state is used. |
| =GetStateCounts(ProductName, '$', 'O') | Returns the possible count for ProductName, in the default alternate state. |
| =GetStateCounts(ProductName, 'StateA', 'S') | Returns the selected count of ProductName, in the alternate state named StateA. |

## Example 1 – Counting total number of user selections (including selected excluded values)

Chart expression

Overview

The GetSelectedCount() function returns the total number of selected values, not including the total number of selected excluded values. With GetExcludedCount(), you can include the count of selected excluded values in the chart's calculation.

Open the Data load editor and add the following load script to a new section.

Load script

```
Names:
LOAD * inline [
First name|Last name|Initials|Has cellphone
John|Anderson|JA|Yes
Sue|Brown|SB|Yes
Mark|Carr|MC|No
Peter|Devonshire|PD|No
Jane|Elliot|JE|Yes
Peter|Franc|PF|Yes ] (delimiter is '|');
```

Results

Do the following:

1. Load the data and open a sheet.
2. Create two filter panes.
3. Add First name as a [dimension](#glossary-1 "Glossary term") in the first filter pane. Add Last name as a dimension in the second filter pane.
4. Next, create a KPI with this [measure](#glossary-2 "Glossary term"):

   =GetStateCounts([First Name],'', 'S','XS')
5. In the First name filter pane, select the values Mark and Peter. In the Last name filter pane, select the value Carr.
6. Observe that the KPI shows a value of 2. This reflects that all values you selected, including the selected excluded value Peter, are counted.

## Example 2 – Combining excluded, selected excluded, and alternative counts

Chart expressions

Overview

The GetExcludedCount() function returns the total number of unique values that are not selected and excluded. If you want to include selected excluded and alternative counts in your visualization, you can use the
GetStateCounts() function as follows.

Open the Data load editor and add the following load script to a new section.

Load script

```
Names:
LOAD * inline [
First name|Last name|Initials|Has cellphone
John|Anderson|JA|Yes
Sue|Brown|SB|Yes
Mark|Carr|MC|No
Peter|Devonshire|PD|No
Jane|Elliot|JE|Yes
Peter|Franc|PF|Yes ] (delimiter is '|');
```

Results

Do the following:

1. Load the data and open a sheet.
2. Create two filter panes.
3. Add First name as a [dimension](#glossary-3 "Glossary term") in the first filter pane. Add Last name as a dimension in the second filter pane.
4. Next, create a KPI with this [measure](#glossary-4 "Glossary term"):

   =GetStateCounts([First name], '', 'X', 'A', 'XS')
5. In the First name filter pane, select the values John and Peter. In the Last name filter pane, select the value Franc.
6. Observe that the KPI shows a value of 4. This reflects that the selected excluded value John is included in the count, in addition to the count of the excluded values.
7. Edit the KPI and replace the existing measure with the following:

   =GetStateCounts([Last name], '', 'X', 'A', 'XS')
8. Keeping the existing selections, select the value Anderson in the Last name filter pane.
9. Observe that the KPI still shows a value of 4. This reflects that the alternative value Devonshire is included in the count, in addition to the count of the excluded values.
