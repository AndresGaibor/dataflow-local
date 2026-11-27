---
title: "Numbers functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/numbers-functions-table-recipe.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe", "Table recipe functions"]
---

# Numbers functions

In the case that your data is not detected as numbers, you need to first apply the Convert to numbers function to the column with numbers before applying any other number-related function. The separator information that you have to fill correspond to the input format separators to parse a text into number, not the display format separator of numbers.

## Compare numbers

Compares the numbers in the column with a specific value, or values from another column. The function will return TRUE if the condition set by the operator is met, otherwise it will return FALSE.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Comparison operator | Select the operator to use for the comparison:   - = equals - != is not equal - > is greater than - >= is greater than or equals - < is lower than - <= is lower than or equals |
| Use with | - Value: Select this option to compare the column against a fixed value, set in the Value field. - Other column: Select this option to compare the column with values from another column, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - 12345 - 42 - 365 | - Comparison operator: > - Use with: Value - Value: 300 | - TRUE - FALSE - TRUE |

## Convert to numbers

Converts the type of data contained in the column so that it is interpreted as numbers in the system.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Decimal separator | Enter a character to act as decimal separator for number data. |
| Thousand separator | Enter a character to act as decimal separator for number data. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

## Format number

Changes how numeric values are displayed using predefined or custom patterns.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function. |
| Output format | Select one of the predefined patterns from the drop-down list or enter a custom format to apply on the numbers:   - 1,000 (#,##0) - 1,000.1 (#,##0.0) - 1,000.12 (#,##0.00) - 12% (0%) - 12.3% (0.0%) - 12.34% (0.00%) - Custom, to enter your specific number format, set in the Custom format field. |
| Decimal separator | Optionally enter a character to act as decimal separator for the output. |
| Thousand separator | Optionally enter a character to act as thousand separator for the output. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - 0 - 19021.04 - 1429.68 | - Output format: 1,000.12 (#,##0.00) - Decimal separator: . - Thousand separator: , | - 0.00 - 19,021.04 - 1,429.68 |

## Remove fractional part

Removes the fractional part of a number to round towards zero.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| - 3.14 - -19.89 | - 3 - -19 |

## Remove negative values

Replaces negative integers or decimal values with a null value.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| - 121021 - -365 | - 121021 - null |

## Round value using ceil mode

Rounds up values to the nearest number, depending on the precision you set.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Precision | Set the number of decimals that you want to keep. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 3.14 | Precision: 0 | 3 |
| 3.14 | Precision:1 | 3.2 |

## Round value using down mode

Rounds a value towards zero.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Precision | Set the number of decimals that you want to keep. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 3.74 | Precision: 0 | 3 |
| -3.74 | Precision: 1 | -3.7 |

## Round value using floor mode

Rounds down value to the nearest number, depending on the precision you set.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Precision | Set the number of decimals that you want to keep. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 3.74 | Precision: 0 | 3 |
| 3.74 | Precision: 1 | 3.7 |

## Round value using half up mode

Rounds value to the closest number, depending on the precision you set.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Precision | Set the number of decimals that you want to keep. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 3.14 | Precision: 0 | 3 |
| 3.74 | Precision: 0 | 4 |
| 3.74 | Precision: 1 | 3.7 |
| 3.78 | Precision: 1 | 3.8 |
