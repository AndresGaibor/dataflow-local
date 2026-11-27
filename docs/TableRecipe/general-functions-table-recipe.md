---
title: "General functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/general-functions-table-recipe.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe", "Table recipe functions"]
---

# General functions

## Cleanse

Replace invalid, empty, or null values of a column with specific values.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Replace | Select the type of values to target and replace. You can use the function to target any of the following:   - Invalid - Null - Empty |
| Use with | - Value: Select this option to fill the column with a fixed value, set in the Value field. - Other column: Select this option to fill the column with values from another column, set in the Column drop-down list. - Null: Select this option to fill the targeted cells with null values. |

Tip noteAlternatively, you can use this function by right-clicking a null or empty cell in the table and selecting the Fill null and empty cells option. A recipe step then opens where you can enter the new value to use. Finish the step configuration and click Apply.

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - 09/05/1969 - Null - 75000 | - Use with: Value - Value: Recipe | - 09/05/1969 - Recipe - Recipe - 75000 |

## Clear cells

Clears the content of all the cells in the column. The resulting cells will contain null values.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| - 09/05/1969 - 12/10/2021 | - Null - Null |

## Delete filtered rows

Deletes all the rows that match the filter currently applied on the table.

### Properties

There are no specific properties to configure for this function. Select the function in the functions list and click Apply.

The filter is automatically cleared once the function is applied.

## Fill cells

Fills cells with a constant value or values from another column.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to fill the column with a fixed value, set in the Value field. - Other column: Select this option to fill the column with values from another column, set in the Column drop-down list. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - 09/05/1969 - Null - 75000 | - Use with: Value - Value: Recipe | - Recipe - Recipe - Recipe - Recipe |

## Keep filtered rows

### Properties

Keeps all the rows that match the filter currently applied on the table by deleting all the non matching rows.

### Properties

There are no specific properties to configure for this function. Select the function in the functions list and click Apply.

The filter is automatically cleared once the function is applied.
