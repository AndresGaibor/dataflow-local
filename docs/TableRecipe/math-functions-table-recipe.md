---
title: "Math functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/math-functions-table-recipe.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe", "Table recipe functions"]
---

# Math functions

## Absolute value

Calculates the absolute value of numerical values in the column.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| - -1989 - 12 | - 1989 - 12 |

## Add

Performs a calculation on this column with another one or a fixed value.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to add a fixed value, set in the Value field. - Column: Select this option to add values from another column, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 10 | - Use with: Value - Value: 2 | 12 |

## Cosine

Computes the trigonometric cosine of the column values.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| 50 | 0.96496602849211 |

## Divide

Performs a calculation on this column with another one or a fixed value.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to divide the column values by a fixed value, set in the Value field. - Column: Select this option to divide the column values with values from another column, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 10 | - Use with: Value - Value: 2 | 5 |

## Exponential

Calculates the exponential of the column values.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| 5 | 148.41315910258 |

## Logarithm

Calculates the base 10 logarithm of the column values.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| 5 | 0.69897000433602 |

## Max

Raises numerical values to reach a specified value or the value from another column.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to use a fixed value as max, set in the Value field. - Column: Select this option to use values from another column as max, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - -150 - 72 - 42 | - Use with: Value - Value: 50 | - 50 - 72 - 50 |

## Min

Lowers numerical values to reach a specified value or the value from another column.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to use a fixed value as min, set in the Value field. - Column: Select this option to use values from another column as min, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - -150 - 72 - 42 | - Use with: Value - Value: 50 | - -150 - 50 - 42 |

## Modulo

Calculates the remainder of a division operation.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to perform the calculation with a fixed value, set in the Value field. - Other column: Select this option to perform the calculation with values from another column, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 10 | - Use with: Value - Value: 3 | 1 |

## Multiply

Performs a calculation on this column with another one or a fixed value.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to multiply the column values by a fixed value, set in the Value field. - Column: Select this option to multiply the column values by values from another column, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 10 | - Use with: Value - Value: 2 | 20 |

## Natural logarithm

Calculates the natural logarithm of the column values.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| 5 | 1.60943791243 |

## Negate

Negates the column values. Positive values become negative and negative values become positive.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| - 75012 - -1500 | - -75012 - 1500 |

## Power

Uses a specific value or the values from another column as exponent for the column values.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to use a fixed value as exponent, set in the Value field. - Other column: Select this option to values from another column as exponent, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - 3 - 10 | - Use with: Value - Value: 3 | - 27 - 1000 |

## Sine

Computes the trigonometric sine of the column values.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| 50 | -0.26237485370393 |

## Square root

Calculates the square root of the column values.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| - 25 - 1600 | - 5 - 40 |

## Subtract

Performs a calculation on this column with another one or a fixed value.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to subtract a fixed value from the column values, set in the Value field. - Column: Select this option to subtract values from another column from the base column, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 10 | - Use with: Value - Value: 2 | 8 |

## Tangent

Computes the trigonometric tangent of the column values.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| 50 | -0.27190061199763 |
