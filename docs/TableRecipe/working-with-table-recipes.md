---
title: "Working with table recipes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/working-with-table-recipes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe"]
---

# Working with table recipes

## Creating a table recipe

To create a new table recipe:

1. From the launcher menu, select Analytics > Create or Analytics > Prepare data.
2. Click Table recipe.

   The Create a new table recipe dialog opens.
3. In the corresponding field, enter a Name for your table recipe.
4. From the corresponding drop-down list, select in which Space you want to save the table recipe.
5. Add a Description to document the purpose of the table recipe.
6. Add some Tags to the table recipe to make it easier to find.
7. Optionally select the Open table recipe checkbox to directly view the table recipe once it’s created.
8. Click Create.

Your new table recipe opens in the Editor tab and you are prompted to select a source from your catalog. See [*Selecting a data source*](#Selectin "sdfgh") for more information on how to proceed.

Information noteWhen opening an existing table recipe from your catalog, you will land in the Overview tab.

## Selecting a data source

### Adding a source right after the table recipe creation

Right after Clicking Create in the table recipe creation dialog, a Data catalog window opens. To use as source for your table recipe, you can select any of your catalog datasets based on files or a [data connection](how-to-use-connection-as-source-table-recipe.htm#Creating).

To select a dataset as source for your table recipe:

1. Browse for previously uploaded datasets, or click Upload data file to browse for files on your computer and upload them on the fly.
2. Using the search and filters, select the checkbox in front of a single dataset from your list and click Next.
3. In the Summary tab, you can review the dataset you have selected, check the fields it contains, and exclude some if you want. Click Load into table recipe.

   When the load is successful, a summary opens detailing how many rows and columns will be displayed in the sample table. After you close the summary, you can see the loaded data in the editor in the form of a table with multiple columns corresponding to the selected fields.

### Adding a source some time after the table recipe creation

If a table recipe was created without setting a source by closing the Data catalog window during the process, you can still set a source the next time you open it.

1. Open the table recipe without source.
2. Click one of the two Set source buttons:

   - In the middle of the empty table area.

     ![Setting a source in an empty table recipe](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_set_source_1.png)
   - In the source section of the Table recipe panel.

     ![Setting a source in an empty table recipe](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_set_source_2.png)

   the Data catalog window opens.
3. Browse for previously uploaded datasets, or click Upload data file to browse for files on your computer and upload them on the fly.
4. Using the search and filters, select the checkbox in front of a single dataset from your list and click Next.
5. In the Summary tab, you can review the dataset you have selected, check the fields it contains, and exclude some if you want. Click Load into table recipe.

   When the load is successful, a summary opens detailing how many rows and columns will be displayed in the sample table. After you close the summary, you can see the loaded data in the editor in the form of a table with multiple columns corresponding to the selected fields.

### Changing the source of the table recipe

In the case of an existing table recipe with functions already applied on the table, it is still possible to select different fields to load, or another source for your table recipe altogether.

1. In the source section of the Table recipe panel, click the current source to expand the configuration menu.

   ![The source panel expanded](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_source.png)
2. Click Change source.
3. Click Change source again in the confirmation modal that opens.
4. Browse for the new dataset to use in the Data catalog window, like you would do for a new table recipe.

After loading the new dataset or new fields in the table recipe, the source changes and the data in the table is updated, but the recipe steps are kept. If the schema is not the same as before, the recipe will become invalid and you will need to reconfigure your recipe steps. See [*Editing a function*](#Editing) for more information.

### Configure the file settings of CSV and Excel sources

If you are using a csv or excel file dataset as source, either previously uploaded to your catalog or directly uploaded during the process, and the data does not display properly in the table, it could mean that the file is not properly formatted.

Possible issues include a wrong header size or wrong separator configuration. To troubleshoot these issues, you will need to go to the dataset settings.

1. From the table recipe, point your mouse over the source section of the right panel and click the View dataset in a new tab button.

   You can also open the dataset from your Catalog.

   The dataset opens and in the overview, you can see a warning saying that there is a potential formatting error.

   ![Shortcut to open the dataset in a new tab](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_dataset_settings_1.png)
2. Click the link to the File format settings from the warning message or use the More actions menu on the top right of the overview.

   ![Menu to open the dataset file format settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_dataset_settings_2.png)
3. Use the Delimiter dropdown list to select the expected delimiter, or enter a new value in the Header size field.

   ![Fields to change the dataset configuration like header size or separator](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_dataset_settings_3.png)
4. Click Save.
5. Back in your table recipe, click the current source in the right panel and select Change source. Select the same dataset as before from the catalog and reload the source. This time, the source will reflect the right dataset configuration.

## Assessing the quality of the data

In a similar way to the dataset experience, Table Recipe has native data quality capabilities to detect, visualize, and fix invalid or inconsistent data without scripting. You can benefit from automatic and manual semantic type handling and validity-based filtering.

### Permissions and access

To access to data quality in table recipe, you need:

- A Qlik Talend Cloud Enterprise, Qlik Talend Cloud Premium, Qlik Cloud Analytics Premium, Qlik Cloud Analytics Enterprise, or Qlik Sense Enterprise SaaS subscription.
- At minimum, the Compute data quality permission set to Allowed and the Manage semantic types permission set to Assign only in the Data quality section. These permissions are assigned by a tenant administrator through default permissions or a custom role. For more information, see [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm).

### Data quality indicators

The quality indicators are a quick and easy way to assess the quality of your data, at the column level, as well as the record level. In Table Recipe, data can be categorized as invalid, empty, or valid against the current data type.

![Data quality indicators in the table recipe editor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/ui_gen_table-recipe-data-quality.png)

When looking at the table, you can see that each column header contains a quality bar. The statistics displayed here applies to each specific column and is regularly updated depending on the state of the data sample. Hover over each color for detailed statistics of each category, or click one to create a quick filter:

- Green: Valid values
- Black: Empty or null values
- Red: Invalid values

![Data quality indicators for a specific column](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_quality_bar_1.png)

When looking at the content of a specific column, cells containing invalid values according to the semantic type are displayed with a red vertical bar and a red background.

For more information on how validity percentages are calculated, see [*Semantic types discovery*](../DataIntegration/DataProducts/Managing-semantic-types.htm#Semantic).

## Adding a function

### Applying a function to a column

Functions corresponds to the different transformations you can apply on the data at the column level. Around fifty functions are available, split in different categories depending on the data type. For more information, see [*Table recipe functions*](list-of-table-recipe-functions.htm).

To apply a function on a column:

1. Click anywhere in a column to highlight and select it.

   ![Selecting a column before applying a function](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_select_column.png)
2. In the Functions panel, browse the list of functions or use the search field to find the function to apply.

   ![Browing for a function in the list](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_select_function.png)
3. Click the function of your choice.

   In the Table recipe panel, the function configuration menu opens.
4. Fill the different configuration parameters according to the desired outcome.

   ![Filling a function configuration parameters](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_configure_function.png)
5. Click Apply.

   The transformation is applied to the selected column and is listed in the recipe as an individual step.

   ![A new column created from a function](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_function_result.png)

   Recipe steps can be modified later if needed. See [*Editing a function*](#Editing) for more information.

### Applying a function to multiple columns

Rather than applying the same function to different columns one after the other, you can perform actions on several columns at the same time.

To apply a function to multiple columns, you can:

- Select multiple columns at once before clicking a function, using Ctrl + click or Maj + click.
- Start applying a function to a single column and then change the Columns to process in the function configuration.

![Applying a function on multiple columns at once](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_multi_select.png)

Configure the function and click Apply.

### Editing a function

Any function previously applied can be edited from the recipe. But because each recipe step is based on the previous one, any modification on a step can cause errors to the following ones. Make sure your recipe steps configuration do not reference deleted or renamed columns for example.

To edit a previously applied function:

1. In the recipe section of the Table recipe panel, click the step to edit.

   The step expands and the current configuration is now visible.

   ![Editing a previous recipe step](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_edit_step.png)
2. Directly edit any configuration parameter you want to change.
3. Click Apply.

The table is refreshed with the new effects of the function now active.

If a step is not necessary anymore, you can simply remove it using the trash icon.

### Renaming a recipe step

Rename recipe steps to document their purpose and make recipes easier to share and maintain.

To rename a recipe step:

1. In the recipe section of the Table recipe panel, click the step to edit.
2. The step name displays as an inline text field that you can edit.
3. Enter a descriptive name, such as Parse ISO dates, Clean region codes, or Convert order totals.
4. Apply the change.

Tip noteAlternatively, right-click the step when collapsed and select Rename step.

Tip noteUse a short verb-noun name that describes the result of the step. Avoid technical names that do not explain the step's purpose.

![Renaming a table recipe step](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_rename_step.png)

The renamed step appears in the editor. The information icon still shows the function that the step applies and its description.

### Viewing intermediate data at each step

Select a step to see the recipe's output up to that point and verify that each transformation worked as expected, before reviewing the final result.

To open a step preview:

1. In the recipe section of the Table recipe panel, click the step that you want to inspect.

   The table displays the sample data after that step executes. Steps that follow the selected step are not included.
2. Scroll through the data grid to inspect the intermediate result. You can use the grid controls to explore the sample data.

Tip noteYou can tell whether you are previewing a step by a notice at the bottom of the interface, or by a tag in the top toolbar.

#### Dismiss the preview explanation

When you open a step preview for the first time in a session, a popover explains that the table shows the state of the data at the selected step.

Read the popover, then click Hide to dismiss it if needed. After you hide the popover, a smaller preview indicator remains available while you preview a step.

#### Exit a step preview

To return to the final recipe view, do one of the following:

- In the Table recipe panel, click ![Close](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) to collapse the step you are previewing.
- If a notice for the step preview is shown at the bottom of the screen, click Close step preview.
- If ta tag in the toolbar indicates you are Previewing step <number>, click ![Close](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_close.svg) next to this tag.

## Filtering data

In order to have a more specific idea of the data contained in your table or in order to perform functions on a certain subset of data, you can create up to five filters on your data.

### Creating a quick filter

If you only need to filter similar values in a column, you can create a quick filter without going in the dedicated filter menu.

1. Right-click a specific value in a column.
2. From the quick actions menu that opens, click the Filter rows with this value option.

   ![Right-clicking a value to open the filter menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_quick_filter.png)
3. The filter is directly created, and the column now only displays the rows with the matching value.

   ![A filter based on a single value](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_quick_filter_2.png)

### Creating a complex filter

Complex filters allow you to combine more search criteria.

1. To start creating a filter, you can:

   - Click the Filter button in the table header.
   - Click the column menu of a column and select Filter column.

   Information noteFor any given column, you can also use the column menu to directly filter rows with valid, invalid, empty, or null values.
2. In the filter window that opens, create a filter by using the drop-down lists to select a column, a condition, and—as applicable—a value.

   When you enter filter values, suggested values are shown in the filter panel. If more values are available, click Show more to load additional suggestions.

   By default, the column value correspond to the currently selected one, but you can change it.
3. Combine more filters by clicking the Add filter button.

   Use the trash icon to remove individual filters if needed.

   ![Configuring several filters](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_adding_filters.png)
4. Use the drop-down on the top right of the filters to select if you want to display the rows that match:

   - All filters. Selected by default, this option will combine filters using an AND operator.
   - Any filter. Selecting this option corresponds to an OR operator for your filters.
   - None of the filters. Matching rows will be excluded from the displayed data.
5. Click Apply.

   You can see in the table header that the filters have been correctly applied and the table now only displays the data corresponding to these criteria.

   ![A combination of filters visible in the table header](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_filters_applied.png)

   Information noteIf no data matches your filters, the table will be empty.

   You can apply a function on this subset of data, and the filter will be visible in the recipe step.
6. In the table header, click the cross in an individual filter to remove it, or use the Clear all option to remove all the filters at once and display the whole sample again.

### Creating a filter using the quality bar

The quickest way to identify and filter incorrect data is to use the quality bar.

Under each column header is a quality bar indicating the proportion of valid (green) and invalid (red) data according to the current data type, or empty (black) data. For more information, see [*How to assess data quality in table recipes*](table-recipe-data-quality.htm).

![Quality bar for filtering incorrect data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table-recipe_filter_quality_bar.png)

To create a filter on the invalid, empty, or valid data contained in the column, simply click on the corresponding section of the quality bar.

![A filter on invalid values](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table-recipe_filter_quality_bar_2.png)

The filter is directly created, and the column now only displays the rows with the matching value. The list of active filters can be seen above the table.

## Selecting a target

To output the results of your table recipe, you need to set a target, a file that will be stored in your catalog in Qlik Cloud. The prepared data can be exported as a .qvd, .parquet, .txt, or .csv file.

To set the table recipe target:

1. In the target section of the Table recipe panel, click Set to expand the target configuration menu.

   ![Set target button](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_set_target.png)
2. From the corresponding drop-down list, select in which Space you want to export the target.
3. In the corresponding field, enter a File name for your target.

   Information noteYou can write in a specific folder of the desired space. If you have created a folder called folder\_name in your personal space for example, use folder\_name/table\_recipe\_output.qvd as file name for your target. The resulting file will be directly sent to your folder.
4. From the corresponding drop-down, select the file Extension to use for your target.
5. Click Apply.

## Running a table recipe

Once all the steps of your recipe are correctly configured, a green check mark shows that the table recipe is considered valid and can be run. When running a recipe, the functions that you have used on the sample data will be applied to the entire source data.

![A valid recipe ready to run](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_run_recipe.png)

Warning note

When running a recipe, it will be run with your credentials, and you are responsible for ensuring that it meets the security guidelines of your organization. Therefore, before running a recipe, verify the different steps and optionally make sure that the generated script corresponds to what you want to accomplish.

Pay attention to the origin of a recipe and be careful if the recipe you are about to run is for example:

- A duplicated recipe
- A recipe that was shared with you
- Imported via upload

1. Click Run recipe to start processing the data.

   A notification opens to show the status of the run.
2. When the recipe has successfully completed, you can click the Open target dataset button directly from the notification, or you can find the data that has been output at the following places:

   - In your Catalog among your other assets
   - In the Outputs section of the table recipe Overview.

   If your run happens to fail, you can use the View log button to check the logs for more information on what went wrong.

You can now use this prepared data as clean source to feed an ML experiment, or in a visualization application.
