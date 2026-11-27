---
title: "Navigating table recipes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/navigating-table-recipes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe"]
---

# Navigating table recipes

When you open a table recipe, it provides information on the table recipe and its dependencies as well as an editor for designing the recipe. A table recipe contains two sections:

- Overview: Provides a summary of information about the table recipe, including information on dependencies, run history, and published copies.
- Editor: Provides the single table view of a data sample to add transformations steps to your recipe and run it on the full data.

## Overview

The Overview provides general information about a table recipe, its data sources, and its exported files. Four tabs are available in a data flow overview:

- Summary
- Notifications
- Run history
- Published copies

![Overview tab of a table recipe](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_overview.png)

### Summary

The Summary provides general information on the data flow creation, updates and status:

- Owner: Owner of the table recipe
- Creator: Creator of the table recipe
- Contributors: Number of contributors to the table recipe. Click ![Users](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) to view the names of contributors.
- Space: Space where the table recipe is located
- Created date: Date the table recipe was created
- Modified date: Date the table recipe was last modified
- Last modified by: User who last modified the table recipe
- Last run status: Status of the last table recipe run
- Last run duration: Duration of the last table recipe run
- Last run date: Date of the last table recipe run
- Number of steps: Number of transformation steps included in the table recipe
- Table recipe ID: Technical ID of the table recipe

The Summary also has two additional sections, Output and Input:

- Output shows the last file outputted by the table recipe.
- Input shows the source used at the start of your table recipe.

For items listed in Output and Input, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view additional options. You can view the impact analysis or lineage for each item. You can also open items in a new tab.

### Notifications

Notifications lists the different events for which you can receive notifications. You can turn them on or off, and select how you receive the notifications.

![Notifications tab of a table recipe](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/data_flow_notifications.png)

### Run history

Run history shows a list of the previous table recipe runs, with the status, time and duration of the run. Click View to display a summary and optionally download a detailed log.

![Run history tab of a table recipe](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_run_history.png)

### Published copies

Published copies shows in which managed spaces copies of the table recipe were published. Each copy shows the following information:

- Name
- Owner
- Last modified
- Space
- Viewed by

Click on the copy to open it in Table recipe. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view additional options. You can:

- Add it to a collection.
- Rename it.
- View lineage information.
- View impact analysis.
- View the copy run schedule.
- Open it in a new tab.
- Delete the copy.

## Editor

In the Editor, you can work on your table recipe by selecting columns and applying transformation steps.

![A newly created table recipe, with an empty recipe and no target set](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_empty.png)

Actions and panels available in the table recipe editor:

| Option | Description |
| --- | --- |
| More Functions | Show or hide the Rename column button, the Search functions field, the list of functions and the Data distribution panel. |
| Recipe status | Current validity status of the entire table recipe. This validity of the table recipe depends on the status of individual recipe steps and the source and target configuration. |
| More Undo | Undo the latest change (multiple step undo is possible). |
| More Redo | Redo the latest undo. |
| More Recipe | Show or hide the Source, Recipe, and Target configuration panels, as well as the list of keyboard shortcuts. |
| load data Run recipe | Run the table recipe to generate an output. |
| More More actions | Display additional actions such as the View script option, to look at the Qlik script that will be generated by the recipe. |
| Filter Filter | Open the Add filter menu where you can set up one or more queries to only display the data you need. For more information on filters, see [*Filtering data*](working-with-table-recipes.htm#Filterin). |
| visible columns Visible columns | Select which columns to show or hide in the table. The label of the button shows the current number of columns displayed in the table. |
| Row size Row size | Choose between a compact or a large view for the table rows. |
| Row size Rows settings | Select the number of rows to load into the recipe. A high number may impact the performance. |
| Single table | Table view of your data sample where you can explore and select columns to apply recipe steps. |

### Functions

The Functions panel is the main place to browse the different functions available for your data and to gain some insight with your columns statistics. It contains the following elements:

- The column name section, where the name of the currently selected column is displayed, and from where it possible to start configuring a function to rename the column using ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).

  ![Name of the column and the edit button](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_column_title.png)
- The Search functions field, where you can start typing the name of a function or a keyword to try to look for the specific function you need.

  ![Search field for the functions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_search_functions.png)
- The list of functions, where you can browse for functions to apply, sorted by categories. Click a function to start configuring it.

  ![List of available functions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_functions_list.png)
- The Data distribution section, that you can choose to show or hide, contains statistics on the data contained in the selected column, and takes into account any potential filter. The way data is displayed depends on the data type:

  - For text, the number of occurrences of strings is displayed in the form of a bar chart.
  - For numerical values, you can choose to show the distribution as a curve, with information on the min, max, and average values, or display it as a bar chart as well. To switch between the two displays, use ![Line chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_chart_area.svg) or ![Bar chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bars_horizontal.svg).

  ![Two types of charts depending on the data type](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_data_distribution.png)

### Single Table

At the center of the page, a sample of your table data is displayed as a spreadsheet that you can interact with. The main elements of this table view are the following:

- The row number: This number is a visual help to identify the content of a row, but does not work as an ID. It is not tied to the content of the row.
- The column title area: Visible in the column header, it shows some or all of the following:

  - Column title: The name given to the column. It can be changed from the Functions panel or the column menu, using the Rename column function.
  - Column type: The semantic type assigned to the column. It can be changed using the Change type... column action. For more information, see [*How to change the data type of a column*](how-to-change-semantic-type.htm).
  - Quality bars: Data quality indicators show the proportions of valid, invalid, empty, and null values in the sample. For more information, see [*Assessing the quality of the data*](working-with-table-recipes.htm#Assessin).
  - Function suggestions: Click the lightbulb icon to see suggestions of data types you can convert the column to.
- The column menu, accessible by right-clicking the column header or clicking ![Menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg). The following column actions are available:

  - Change type... to change the semantic type of a column.
  - Rename column to change the name of a column.
  - Duplicate column to duplicate a column and its content.
  - Filter column to start creating a filter on your data. For more information, see [*Filtering data*](working-with-table-recipes.htm#Filterin).
  - Filter invalid values to isolate invalid values in this column. For more information, see [*Filtering data*](working-with-table-recipes.htm#Filterin).
  - Filter empty or null values to isolate empty and null values in this column. For more information, see [*Filtering data*](working-with-table-recipes.htm#Filterin).
  - Filter valid values to isolate valid values in this column. For more information, see [*Filtering data*](working-with-table-recipes.htm#Filterin).
  - Hide column to reduce the number of visible columns in your table. Use the Visible columns button to manage which column are visible.
  - Pin column to the left to keep a column visible on the left of the table when horizontally scrolling. Select Unpin column from the column menu to move it back to its original place in the table.
  - Delete column to remove a column and its content from the table.

  ![Actions available on a column](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table-recipe_column_menu.png)
- The column content: The actual values contained in each row of your columns, allowing you to explore, analyze and fix the content of the table.

  ![Example of data in a column](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_column_content.png)

### Table recipe

The Table recipe panel is the place where you manage the source data, and the output you want to create, via the recipe and the target configuration. It contains the following elements:

- The source, to select the data you want to prepare. Expand the section to change the fields to load or the source file itself.

  ![Source configuration panel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_source.png)
- The recipe, where the successive functions applied to your table are listed. Click a step to view the intermediate data, edit a function configuration, or delete the step altogether.

  ![List of steps applied on the data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_steps.png)
- The target, to choose how and where to export the prepared data.

  ![Target configuration panel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_target.png)
- The list of keyboard shortcuts, that you can expand or collapse.

  | Keyboard shortcut | Action |
  | --- | --- |
  | CTRL + Click | Select multiple columns |
  | CTRL + SHIFT + Click | Select a range of columns |
  | CTRL + A | Select all columns |
  | CTRL + SHIFT + A | Select the inverse of the current column selection |
  | CTRL + Backspace | Delete the selected columns |
  | CTRL + S | Search the functions |
  | CTRL + D | Focus on the recipe steps |
  | CTRL + G | Focus on the grid controls |
  | CTRL + C | Copy the cell value |
  | CTRL + Z | Undo a recipe step |
  | CTRL + SHIFT + Z | Redo a recipe step |
  | CTRL + ENTER | Run the recipe |
