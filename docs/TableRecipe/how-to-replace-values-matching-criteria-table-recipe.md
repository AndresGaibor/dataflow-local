---
title: "How to replace values matching a condition"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/how-to-replace-values-matching-criteria-table-recipe.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe", "Working with table recipes"]
---

# How to replace values matching a condition

In a table recipe, you can combine filters with the Fill cells function to apply conditional logic and replace values that match a specific criteria.

When a filter is active and you apply Fill cells, you can choose to only apply the effects of the function to the rows currently displayed by the filter. All other rows remain unchanged. The filter condition is saved as part of the recipe step.

Let's say you are preparing an expense report that contains a Cost column. Company policy caps reimbursable expenses at 100 per item. You want to replace any value above 100 with 100 to enforce this maximum before loading the data into your application:

1. Click the Filter button in the table header, or click the column menu of the Cost column and select Filter column.

   The Add filter panel opens.
2. In the filter row, set the column to Cost, select is greater than as the operator, and enter 100 as the value.

   ![Filter configured with Cost column, is greater than operator, and value 100](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_replace_value_matching_criteria_1.png)
3. Click Apply.

   The table now only displays rows where the value in the Cost column is greater than 100.
4. Click the Cost column header to select it.
5. In the Functions panel, select Fill cells in the General category.
6. In the Use with drop-down list, select Value and enter 100 in the Value field.

   ![Fill cells function configured with Value selected and 100 entered as the replacement value](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_replace_value_matching_criteria_2.png)
7. Click Apply.

   A new recipe step is added. Because the filter was active when the step was applied, only the rows where Cost is greater than 100 are updated. All other rows keep their original value.
8. In the table header, click Clear all to remove the filter and display the full dataset.

All costs above 100 have been replaced with 100 in your dataset. The filter condition is stored as part of the recipe step, so it will be applied automatically every time the recipe runs.

This example caps values in a single column, but the same technique works with any operator, threshold, or target value. You can also combine multiple filters to build more complex conditions before applying Fill cells. For more information on filters, see [*Filtering data*](working-with-table-recipes.htm#Filterin).
