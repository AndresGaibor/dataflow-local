---
title: "How to delete specific rows"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/how-to-delete-specific-rows-table-recipe.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe", "Working with table recipes"]
---

# How to delete specific rows

In Table recipe, you cannot manually select one or more rows and delete them with a function. However, it is still possible to target specific rows using filters, and use the Delete filtered rows function.

Let's say that you are using a file with 600 rows as source for your recipe, and you want to delete the first 100 rows of your table:

1. From the functions list in the left panel, select the Create new column function in the Columns category.
2. Choose a column name and an anchor position.
3. In the Fill column with drop down list, select Sequence.
4. Select 1 as Start value,1 as Step value and click Apply.

   A new column containing a sequence from 1 to the last row number is created.

   You need this sequence so that the filter you are going to use is based on fresh new consistent values, and not the content of other columns.
5. Select the header of the column containing the sequence and click the Filter button.
6. Select is lower than or equals as operator, enter 100 as value and click Apply.

   ![Applying a filter on the first 100 rows](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_how_to_delete_specific_rows.png)
7. The filter is applied and only the first 100 rows of the dataset are displayed in the grid.

   In order to target the last 100 rows, you could have selected the is greater than operator with 500 as value for example.
8. From the functions list in the left panel, select the Delete filtered rows function in the General category and click Apply.

All the rows you have targeted with your filter have been deleted and you can now remove the sequence column if you want.

This example was about removing the N first or last rows of your table, but more generally you can build any combination of filters to target and delete the rows that you want.
