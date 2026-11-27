---
title: "Working with report filters"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Generate/cloud-in-app-reports-filters.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Configuring report generation"]
---

# Working with report filters

Create [report filters](#glossary-0 "Glossary term") to reduce the application data that is visible in reporting output. Each filter can contain definitions for one or multiple fields. Filters can be applied to [report tasks](#glossary-1 "Glossary term") and to individual objects when authoring [templates](#glossary-2 "Glossary term").

Create and manage the application's report filters in the Filters tab of the Reporting section in the application.

The Filters tab in the Reporting section of an application

![The 'Filters' tab in the 'Reporting' section of an app, which is located in the 'Prepare' tab](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CloudExcelReportAppFilters-rev.png "Click to view full size")

After you've created a report filter, there are two ways you can use it in reporting:

- [*Using filters in report tasks*](#Tasks)
- [*Using object-level filters in report templates*](#ObjectLevel)

## Creating report filters

When you create a report filter, it is added as a group of filters. A filter group can filter data from multiple fields, master items, and variables.

Do the following:

1. On the Filters tab in the Reporting section of an application, click Add filter.
2. Click New filter.
3. Type a Name for your filter. Optionally, add a Description.
4. To add a filter to the filter group, click ![Plus symbol](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg)Add.
5. Select a field, master item, or variable to use for the filter. Use the search to refine the results.
6. Configure the filter using the available options. Depending on the object you have selected, available settings might be different.

   Configuring a filter using the Region field

   !['Filters' side pane dialog, with 'Region' selected as a field to be filtered](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CloudExcelReportFiltersField.png "Click to view full size")
7. Once you have defined the selections to include in your filter, click outside the panel (or press the Esc key) to close it.
8. Add more filters to the filter group by clicking ![Plus symbol](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg)Add again.
9. When done, click Add filter.

To delete a filter from the filter group, expand it and click ![Garbage can](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg).

The table below explains how each parameter works.

Options when configuring report filters

| Parameter | Description and configurations |
| --- | --- |
| Exclude | Select this checkbox to exclude the selected values from the filter. |
| Override | Select this checkbox to ensure that these values are included, even if it means overriding other filters. |
| Alternate states | You can toggle on alternate states for your fields and variables. This setting can be used for any selection method listed below.  Alternate states allow you to make different selections on the same dimension and compare the selections in a single visualization, or in two or more visualizations side-by-side. See [*Using alternate states for comparative analysis*](../../Visualizations/alternate-states-comparative-analysis.htm).  If you toggle on alternate states, use the drop down to select the State you want to use for the filter. |
| Selection method | - Values: This is the default configuration for the filter. Select the field values to which you want to apply filtering. - Evaluate: Type in an expression or open the Expression editor. The returned result from the expression will be the filter value used. - Search: Apply filtering using the same Qlik Sense selection search you would use when searching a visualization. There are limitations on which selection search features you can use in your report filters. For more information, see [*Unsupported selection search features for Search filters*](#Supporte). |

### Example 1: Adding an Evaluate filter with an expression

The Evaluate filter selection option is helpful when you want filter values to be relative, not exact.

For example, to filter Year field values to include only those from last year, use: year(now())-1

Using the Evaluate selection option to define a relative filter

!['Filters' side pane dialog, with 'Region' selected as a field to be filtered](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CloudExcelReportFiltersEvaluate1.png "Click to view full size")

### Example 2: Adding an Evaluate filter with a variable expression

When using the Evaluate selection option, you can also specify a variable in the expression.

First, define a variable in your application to define a value of interest that will likely change over time. For more information about how to do this, see:

- [*Using variables in expressions*](../../Variables/work-with-variables.htm)
- [*Working with variables in the data load editor*](../../Scripting/work-with-variables-in-data-load-editor.htm)

For example, you could have a variable for the current year, or for the Product Group with the highest sales.

When configuring the Evaluate filter, simply enter the name of the variable into the Expression field.

### Example 3: Adding a Search filter with an expression

With the Search filter selection option, you can define the filter values based on a search entry using Qlik Sense selection search. For a list of search types and required syntax, see [*Searching within selections or visualizations*](../../Selections/SelectionsToolbar/search-selections.htm).

Information noteThere are limitations on which selection search features you can use in your report filters. For more information, see [*Unsupported selection search features for Search filters*](#Supporte).

For example, for a filter on a Customer field, you could enter the following expression search to only include records for Customer values which have total sales of greater than $1,000,000.00: =sum(Sales)>1000000

### Example 4: Creating a filter based on an application variable definition

A [variable](#glossary-3 "Glossary term") can be used directly as the input entity for a filter, rather than a field. Using a variable filter offers flexibility to your reports.

A variable filter overrides the existing variable definition only for the report generation, replacing it with the value or expression you define in the filter. The temporarily overridden value is used in all report elements which reference it.

1. Create the filter group using the same procedure above.
2. To add a filter to the filter group, click ![Plus symbol](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg)Add.
3. Select the variable you want to use.
4. In the input value box, the existing variable definition is shown. Change the value to what you need it to be for your report use case. If you need to override the variable definition with an expression, rather than a value, you must select the Evaluate checkbox.
5. When you are done configuring the value or expression, click outside the panel (or press the Esc key) to close it.

Using variables directly as the input for the filter. This image shows two variables within the filter. You use the Evaluate option to override the variable definition with an expression instead of a value.

![Filter group creation dialog window, showing two filters which have been defined using a variables, rather than a fields](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CloudExcelReportFilterVariable.png "Click to view full size")

Let's say you have defined the following variables in the application:

- vCurrentYear: this could be a scripted variable calculating the current year.
- vContinent: contains the value of a Continent field. The definition could be simply a text value. Let's say its definition in the application is Europe.

Next, construct a table chart in the application using variable definitions. To analyze a Sales measure across time and regional dimensions, you could use:

- Sales by continent, current year: sum({$< Continent={"$(vContinent)"}, Year={$(vCurrentYear)}>} Sales)
- Sales by continent, all-time: sum({$< Continent={"$(vContinent)"}>} Sales)

When you create a filter based on each of the variables, you can override their definitions if you want to use the same chart data structure, but want different values. For example, the current year definition could be changed to year(now())-1 to make the report show a summary of last year's sales, rather than the source chart which summarizes the current year's data.

## Using filters in report tasks

You can use both task-level and recipient-level filters in the same report task. If a task-level filter is defined, its selections are applied before any filters applied to individual recipients. As a result, when both a task-level and recipient-level filter are applied in the same report task, the filters ultimately applied will be those that each of the individual recipient filters have in common with the task-level filter. This could mean that filters applied to individual recipients are ignored in output.

You can override this behavior by applying the Override setting when configuring the filter you want to apply at the recipient level. This overrides any task-level filter for outputs using the filter applied at the recipient level. For more information, see [*Creating report filters*](#Creating).

### Applying a filter at the task level

Task-level filters are applied to all recipients and groups who receive the output of the report task. They are added when you create or edit the report task. Each report task can have one task-level filter.

For more information, see [*Part 3: Configure the output*](cloud-in-app-reports-tasks.htm#ConfigureOutput).

### Applying a filter at the recipient level

Filters can also be applied to specific recipients of reporting output. The filter names are added to the [distribution list](#glossary-4 "Glossary term") for each applicable recipient. Multiple filters can be associated to a single recipient in the distribution list, but each distributed report can only apply one recipient-level filter per recipient. You can still configure the [report task](#glossary-5 "Glossary term") to send more than one report to a single recipient at a time, applying a different recipient-level filter with each generated report.

For more information, see [*Creating a distribution list for your report*](cloud-in-app-reports-distribution.htm).

For information about how recipient-level filters are handled in report file generation, see [*How report generation works*](cloud-in-app-reports-tasks.htm#How).

Information noteFilter names in a distribution list are name-matched references to existing filters created using the Filters tab in the Reporting section of the application. If a filter is renamed, the references to it within the distribution list will also need to be updated. For more information, see [*Considerations when renaming report filters*](#Consider).

## Using object-level filters in report templates

Object-level filters let you apply a filter to specific report objects instead of applying the same filter context to the entire template. Report filters can be applied to tabular data and chart images when authoring certain report templates.

This is useful when you need different selection states for different objects in the same report output.

Object-level filters are supported for the following template types:

- Tabular (Excel)
- HTML
- PowerPoint
- Word

### How object filters work

Object-level filters apply data reduction as follows:

- Report preview: Data is reduced by current selections in application and object-level filters.
- Report generated from task: Object-level filters apply selections after all other report filters used in the task or distribution (see [*How report filters are evaluated*](#Evaluated)).

### Managing object filters in published applications

For more information about working with object filters in applications published to managed spaces, see [*In-application reporting in managed spaces*](../InAppGeneral/cloud-in-app-reports-managed-space.htm).

### Considerations for templates migrated from Qlik NPrinting

- If an object in the template cannot be matched in the application, the intended object-level filter effect might not be applied to that object.
- After replacing or changing the connected application, validate report output before production scheduling.
- Use template preview and test tasks to confirm that each filtered object returns expected data.

## Editing and deleting report filters

For an application in a shared space, report filters can be edited and deleted by the filter owner and other users with Can edit access.

Do the following:

1. In the Filters tab of the Reporting section of the application, click ![Three dot menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a filter.
2. To edit the filter, click Edit. You can change any of settings that were initially configured for it.
3. To delete the filter, click Delete.

## How report filters are evaluated

For reports generated from a report task, the order in which the filters are applied is as follows:

1. Task-level filter
2. Recipient-level filter
3. Object-level filter

### Expected data

After all filters are applied, the data expected in report objects are the intersection of all selections defined through the report filters. If report objects do not contain any intersecting selections, the objects display as empty in reports.

## Considerations when renaming report filters

If you rename a filter, instances of that filter being defined for a recipient will not be automatically updated in the [distribution list](#glossary-6 "Glossary term"). If any recipients using the outdated filter name are included in the report task, the task will fail for those recipients.

To fix this, the distribution list file must be edited to reference the updated filter name, then re-uploaded.

Do the following:

1. Edit the original distribution list file to reference the updated filter name, then re-upload it.
2. Edit the report task which uses those recipients. You might have to remove, then re-add, the recipients to which those filters apply.
3. Save the report task.

If the distribution list is instead defined manually in the script, update the Filters field values in the source table and reload the application.

For information about configuring the distribution list for an application, see [*Creating a distribution list for your report*](cloud-in-app-reports-distribution.htm).

## Section access considerations

If the application uses section access, report generation works differently. For more information, see [*In-application reporting and section access*](cloud-in-app-reports-section-access.htm).

## Report filter limitations

### Unsupported selection search features for Search filters

Report filters allow you to use the native Qlik Sense selection search to filter your report data. More information about selection search can be found at [*Searching within selections or visualizations*](../../Selections/SelectionsToolbar/search-selections.htm).

The following selection search features are not available in report filters:

- Normal search
- Search using quotation marks
- - Modifier
- + Modifier
- Fuzzy search

### Star statements

Report filters are not compatible with Star statements. If an application contains this statement in the script, reports with filters might show unexpected results.

For more information about limitations for in-application reporting, see [*Limitations for in-application reporting*](../Reporting-service-specifications-limitations.htm#Limitati2).

### Always one selected value property

If an application contains one or more fields configured with the Always one selected value property, you need to configure your report filters so that the filters select exactly one value for each of these fields. These report filters need to be applied to the report task.

If a filter doesn't contain a value for these fields, or no filters are associated at all to the task, the report task will fail.

### Availability of hidden and system fields

Hidden and system fields are not visible in the list of fields to use in a report filter.

## Report filters and report task ownership

When a report filter is created, the user who created it is assigned as its owner.

Changing the owner of a [report task](#glossary-7 "Glossary term") does not change the owner of any report filters used by the report task.

## Learn more

- [*Delivering reports to a distribution folder*](cloud-in-app-reports-output-folder.htm)
