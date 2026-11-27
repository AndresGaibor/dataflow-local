---
title: "Tutorial - Table recipe for beginners"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/table-recipe-tutorial.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe"]
---

# Tutorial - Table recipe for beginners

This tutorial will introduce a basic data preparation use case to make you more familiar with the different steps required in building a table recipe, and the different possibilities that are offered. With the attached dataset, you will be able to reproduce all the steps of this tutorial.

In this scenario, imagine that you are looking at sales data from a pet food online store. The data sample includes customers from around the world, and information on their names, order dates, country of origin, age range, etc. Let's say you want to prepare the data so that it focuses on the customers from France. You will make minor formatting changes, work on the order dates, isolate all the data on french customers from a certain age range, and finally export the data to a new file that you will be able to use as source for an analytics application for example.

## Prerequisites

Download this archive and unzip it on your desktop:

[Table recipe beginner tutorial](/en-US/cloud-services/tutorials/TableRecipeBeginnerTutorial.zip)

The archive contains the orders\_pet\_food.csv data file that you need to complete the tutorial.

## Adding the source file to your catalog

Before starting with the table recipe creation, the file from the package need to be available in the analytics platform. To add the source data to your catalog:

1. From the launcher menu, select Analytics > Catalog.
2. Click the Create new button on the top right and select Dataset.
3. In the window that opens, click Upload data file.
4. Drag and drop the tutorial file from your desktop onto the dedicated area of the Add file window, or click Browse to select it from its location.
5. Click Upload.

## Creating the table recipe and selecting the source

Now that the source is set up, you can start creating the table recipe.

1. From the launcher menu, select Analytics > Prepare data.
2. Click the Table recipe tile or click Create new > Table recipe.
3. In the Create a new table recipe window, set the information of your table recipe as follow and click Create:

   - Table recipe tutorial as Name.
   - Personal as Space.
   - Table recipe to prepare sales data focused on FR customers as Description.
   - Tutorial as Tag.

   The empty table recipe opens, but before you can do anything, you are asked to select the source file from your Data catalog.
4. Use the filtered search to find the order\_pet\_food.csv dataset previously uploaded and select the checkbox before its name.
5. Click Next.
6. Review the dataset and the fields in the summary, and click Load into table recipe.

The data from the dataset is now visible as a table, where fields are displayed as columns. You can easily browse the content of the dataset and you will start preparing the data using functions.

![View of the tutorial data as a table recipe](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_creating_table_recipe_1.png)

## Cleaning the order type

When looking at the sample, one thing that we can notice is that in the order column, listing the type of pet food that was ordered, the word food is redundant and a bit unnecessary. To improve simplicity and clarity, you are going to remove the word food using the Remove part of text function.

![The order column where we will remove part of the text](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_remove_part_of_text_1.png)

1. Click the header of the order column to select its content.
2. From the functions list in the left panel, select the Remove part of text function in the Strings category.

   The configuration form for the function opens in the right panel, with the Columns to process field is already selected.
3. In the Operator drop down list, select Contains.
4. In the Value field, enter Food.
5. Click Apply.

   The word Food has been removed everywhere in the column, and the order type is now easier to read.

   ![Effects of the remove part of text function on the order column](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_remove_part_of_text_2.png)

After completing this operation, you can see that the step is now listed in the recipe in the right panel. After all, the recipe in Table recipe, just like any cooking recipe, is the list of preparation steps applied to your data. You can click a step to see the configuration that was applied, and even edit it.

![The step is added to the recipe](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_remove_part_of_text_3.png)

## Splitting customers names into two columns

The customers first and last names are currently contained in a single column. To better separate information, another step for the recipe will be to split the names into two columns using the Split column function.

![Full names that need to be split into two columns](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_split_column_1.png)

1. Click the header of the full\_name column to select its content.
2. From the functions list in the left panel, select the Split column function in the Strings category.
3. In the Parts field, enter 2, and from the Separator drop down list, select Space.
4. Click Apply.

   Two new columns are created, each containing only one part of the full names. The two new columns have automatically generated names that you are going to change for clarity and consistency.

   ![Full names split into two new columns](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_split_column_2.png)
5. Select the full\_name-split\_1 column and from the functions list, select the Rename column function.

   ![Using the functions list to rename a column](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_split_column_3.png)
6. In the New column name field, enter first\_name and click Apply.

   You will also rename the second column, using another method, directly from the column menu. In both case, a recipe step is created.
7. In the header of the full\_name-split\_2 column, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to display the column menu and select Rename column.

   ![Using the column menu to rename a column](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_split_column_4.png)
8. In the New column name field, enter last\_name and click Apply.

   You now have two clean columns containing first names and last names. The initial full\_name column has no purpose anymore, and you will be able to simply delete it.

   ![First names and last names split into two columns](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_split_column_5.png)
9. In the header of the full\_name column, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) to display the column menu, select Delete column and click Apply.

## Formatting dates

Table recipe also offers a lot of functions to work on dates. In the dataset, there are three columns containing dates to track the date a customer placed an order, the date the order was shipped, and when it was received by the customer. The first step before further exploiting this data will be to convert and format it so that it is usable. Because the idea behind the tutorial is to focus on French customers, you will apply the french date format to these dates that are currently in the YYYY-MM-DD format.

![Three columns contianing dates that we will format](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_formatting_dates_1.png)

1. Select the order\_date column, and while pressing the Shift key, click the reception\_date column header.

   The three columns, including the shipment\_date column are selected. The Ctrl + click shortcut also works to select multiple columns.
2. From the functions list, select the Convert to date function in the Dates category.
3. From the Input format drop down list, select Auto and click Apply.

   The purpose of this function is to convert data from your table so that it is properly interpreted as date in the system. This will allow you to perform more operations based on dates. In this case you will be able to safely change the date format in these three columns.
4. Select the order\_date column and from the Suggestions in the functions list, select the Format date function.

   According to the type of the currently selected column, related functions will be dynamically suggested in the functions list. You can also use the search field to look for a function using its name or related keywords.

   ![Dynamic functions suggestions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_formatting_dates_4.png)

   So far when configuring a function, the Column to process field was already filled based on the currently selected columns. The next step will showcase another way to apply a function on multiple columns.
5. Open the Columns to process drop down list and select the order\_date, shipment\_date and reception\_date checkboxes.

   ![Applying a function on multiple columns](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_formatting_dates_2.png)
6. From the Date format drop down list, select Custom.
7. In the Date pattern field, enter DD-MM-YYYY, which is the official French date format.
8. Click Apply.

All three columns are now in the proper format, which makes it easier to read for the intended target audience.

![The dates columns in their new french format](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_formatting_dates_3.png)

## Calculating the order processing time

Now that your dates columns are properly formatted, you will use the Calculate date difference function, to calculate how many days is needed for a customer to receive their order after placing it.

1. Select the order\_date column.
2. From the functions list in the left panel, select the Calculate date difference function in the Dates category.
3. From the time unit drop down list, select Day.
4. From the Until drop down list, select Other column.

   You can also use this function to calculate a time difference with a specific date, but in this case, you will compare two columns.
5. From the Column drop down list, select reception\_date.
6. In the New column name field, enter time\_to\_receive.
7. Click Apply.

   A new column is created on the right of the order\_date column, containing the number of days between the order date and the reception date. To keep the dataset clean and readable, you will move the new time\_to\_receive column to the right of the three dates columns.

   ![New column with the date difference in days](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_calculating_time_since_1.png)
8. Move the time\_to\_receive column by dragging and dropping the header of the column to the right of the reception\_date column.

   ![The column with the date difference after the other dates columns](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_calculating_time_since_2.png)

In Table recipe, you can also benefit from profiling features to gain insight on your current data. For instance, while the time\_to\_receive column is selected, you can see some useful information in the Data distribution panel on the bottom left. A graphical representation of the numerical values of the column is displayed, and you see that the average time for customers to receive their order is between six and seven days.

![Average number of days to receive the shipment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_calculating_time_since_3.png)

## Adding a quick filter on the country

Let's say that you want to put the country names in upper case, but only for the occurrences of France. You will first apply a quick filter on the country column, and then apply the function on the matching rows only.

1. In the country column, right-click one of the occurrences of the value France and from the menu that opens, select Filter rows with this value.

   ![Using the quick action menu to create a filter](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_quick_filter_1.png)

   You can see above the data that the filter has been correctly applied, with the is equal to operator, and only rows that contain the value France are now displayed.

   ![Filter applied on the country column](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_quick_filter_2.png)
2. From the functions list in the left panel, select the Change to upper case function in the Strings category and click Apply.

   The function was only applied to the filtered rows as you can see in the step summary. Because values are now in upper case, they do not match the filter based on the original case anymore, so it is normal that the grid is empty at this time.

   ![A function configuration summary with a filter applied](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_quick_filter_3.png)

   You will now clear the filter before moving on.
3. To remove the filter, click the cross directly in the filter or use the Clear all option.

All the rows are now displayed again, but only occurrences of France are now in upper case.

## Reordering recipe steps

Looking at the country column again, you can notice that not all occurrences of France were actually changed to upper case. Since the filter that you created earlier was based on the exact France value, other occurrences with typos, like Franc illustrated below, were not included in the function scope.

The next step in your preparation will be to fix the typos, and using the step reordering feature of Table recipe, to move the new recipe step before the upper case transformation. Because in Table recipe a step impacts all the subsequent ones, in doing so, you will be automatically reapplying the Change to upper case function to all the fixed values as well.

![A typo is present in some occurrences of France](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_reordering_steps_1.png)

1. Select the country column.
2. From the functions list in the left panel, select the Search and replace function in the Strings category.
3. From the Operator drop down list, select Equals.
4. In the Value field, enter Franc.
5. From the Replace drop down list, select Entire cell with replace value.
6. In the Replace with field, enter France.
7. Click Apply.

   The typos are now fixed, but still not in upper case. Instead of reapplying the same function as before, you are simply going to reorder the steps in the recipe.

   ![Fixing the typo using a search and replace](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_reordering_steps_2.png)
8. In the recipe panel on the right, move the Search and replace step by dragging and dropping it before the Change to upper case step.

   ![Moving the search and replace step before the upper case formatting step](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_reordering_steps_3.png)

   The search and replace step that was in the 11th place, is now in the 10th place, and this time, all occurrences of France including ones with typos, are displayed in upper case.

   ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_reordering_steps_4.png "The switch to upper case takes into account all occurrences now")

## Filtering a specific range of customers

You are almost done with you recipe. After cleaning and improving the dataset, you are now going to extract the data only relevant to French customers of a specific age range. In order to do that you will create a filter again, but slightly more complex this time, by combining two criteria.

1. Click the Filter button on the top left of your table.
2. In the first filter row, select country from the column drop down list, is equal to as operator, and enter FRANCE in upper case as value.
3. Click Add filter.

   A second row becomes available.
4. In the second filter row, select age\_range from the column drop down list, is equal to as operator, and enter 18-25 as value.

   When combining filters, the operator between them is AND.
5. Click Apply.

   ![Applying two filters on the data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_filters_1.png)

   You can see above your table that the two filters are currently applied and only the matching rows are displayed in the table. The final step of the recipe will be to remove all the non matching rows from the dataset, and only keep data on French customers from age 18 to 25.

   ![The filters on the coutry and age is applied](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_filters_2.png)
6. From the functions list in the left panel, select the Keep filtered rows function in the General category and click Apply.

You have now finalized your table recipe. The scope and size of the data is reduced, but easier to read, and targeted as a specified audience. In addition, you have gained information on the time needed for your customers to receive their order.

![The resulting data after keeping only the data matching the filters](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_filters_3.png)

## Setting a target and running the recipe

Now that the data has been prepared and ready to be used in an application for instance, the only thing left is to configure how to run and export the resulting data. The result of your table recipe can be output in different file formats directly to your catalog, making it easy to reuse in the Qlik Cloud ecosystem. In this scenario you will run and export the prepared data as a .qvd file.

1. In the target section of the Table recipe panel, below the recipe steps, click Set.
2. In the Space drop down list, select Personal.
3. In the File name field, enter tutorial\_output.
4. In the Extension drop down list, select .qvd.
5. Click Apply.

   ![Target configuration for the tutorial](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_target_1.png)

   Your table recipe is now complete and valid as shown by the status in the header bar.
6. Click the Run recipe button on the top right of the window.

   A modal opens to show the progress of the run.

   ![The recipe running to output the data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/tutorial_target_2.png)

   After some time, the window closes and a notification opens to tell you if the run was successful or not. The output of the table recipe can now be found in your catalog, or in the Outputs section of the table recipe Overview panel.

   The status of all your runs can also be found in the Run history section.

## What's next

You have learned how to import source data into your catalog, build a simple table recipe to filter and improve your data, and export the result of you preparation as a ready to use file.

To learn about the multiple ways to use Table recipe for your own use cases, you can take a look at the full list of [*Table recipe functions*](list-of-table-recipe-functions.htm).

To learn how to use your prepared data in analytics applications, see [Creating analytics and visualizing data](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/creating-analytics-and-visualizing-data.htm).
