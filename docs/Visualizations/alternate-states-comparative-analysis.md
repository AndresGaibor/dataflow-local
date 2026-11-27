---
title: "Using alternate states for comparative analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/alternate-states-comparative-analysis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations"]
---

# Using alternate states for comparative analysis

If you want to perform comparative analysis you can use alternate states in Qlik Sense. Alternate states allow you to make different selections on the same dimension, and compare the selections in a single [visualization](#glossary-0 "Glossary term") or in two or more visualizations side by side.

You can use alternate states in visualizations in two different ways:

- Applying a state to the visualization. This connects the selection of the visualization to the selection of the state.
- Using states in the set expression of a [measure](#glossary-1 "Glossary term"). This is useful to compare measure values of different states.

## Creating alternate states

You can create a new alternate state in Master items:

1. Next to Alternate states, click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
2. Provide a name for the new state. There are some naming limitations:

   - Do not use $, 0, or 1 as a state name.
   - Do not use a state name starting with $ or $\_ followed by a number, for example, $3.
   - Do not use a state name already used as a bookmark name.

You have now created a new alternate state that you can use to perform comparative analysis. Typically you would want to create another new state to compare the two states.

## Applying alternate states to sheets and visualizations

You can apply a state to a visualization or a [sheet](#glossary-2 "Glossary term"). If you apply a state to a sheet, all visualizations on the sheet inherit the state unless you apply another state to a specific visualization. When you apply a state to a visualization, it reflects the [selections](#glossary-3 "Glossary term") made in the state. Any selections you make will be applied to the state and be reflected in other visualizations that have the same state applied.

The easiest way to apply an alternate state is dropping it on a sheet or a visualization, and then selecting Apply state.

You can also apply an alternate state with the State setting in the property panel:

- For a sheet, you find the setting under Alternate states.
- For a visualization, you find the setting under Appearance > Alternate states.

You can select:

- Any alternate state defined in Master items.
- <inherited>, in which case the state defined for the sheet is used.
- <default state>, which represents the state where no alternate state is applied.

## Using alternate states in visualizations

Besides applying a state to a visualization you can also use alternate states in the set expression of a measure. This is useful when you want to compare measure values for different dimension selections side by side.

You can set the alternate state as an identifier in the set expression. If you want to use the measure Sum(Sales) in your visualization, for example a bar chart, with a state called Group1 you use the following expression as measure:

Sum({Group1}Sales)

To compare with a different state called Group2, you can create another measure with the expression Sum({Group2}Sales).

The bar chart will now show sales for the selection in Group1 side by side with sales for Group2.

For more information about set expressions, see [*Set analysis*](../ChartFunctions/SetAnalysis/set-analysis-expressions.htm).

## Getting information about the selection of an alternate state

You can see the selections of different states in the selections bar.

For more information, see [*Exploring with selections*](../Selections/SelectionsToolbar/work-with-selections.htm).

You may also want to be able to use information about which, and how many selections are made in an alternate state in labels or titles of visualizations. You can use the following chart functions with the state\_name parameter to return selections associated with the specified state name:

- GetCurrentSelections() to return all current selections.

  [*GetCurrentSelections - chart function*](../ChartFunctions/FieldFunctions/getcurrentselections.htm)
- GetFieldSelections() to return current selections of a [field](#glossary-4 "Glossary term").

  [*GetFieldSelections - chart function*](../ChartFunctions/FieldFunctions/getfieldselections.htm)
- GetSelectedCount() to return the number of selected values in a field.

  [*GetSelectedCount - chart function*](../ChartFunctions/FieldFunctions/getselectedcount.htm)

## Expanding variables in alternate states

You can specify which state to use when expanding a [variable](#glossary-5 "Glossary term"). Changes in a specific state do not affect variable values that are expanded in another state. If you do not specify a state, the variable is expanded in the default state.

Example:

If you have a state named MyState, and a variable named vMyVar:

- $(vMyVar) expands the variable in the default state.
- $({MyState} vMyVar) expands the variable in the MyState state.

## Limitations

It is not possible to add visualizations to master items if you have set the state of the visualization to any other value than <inherited>.

## Comparative analysis example

In this example we want to be able to compare the sales numbers of product lines for different selections of sales regions. We want to select the regions we compare dynamically, either as single regions or a combination of regions.

### Dataset and application

If you want to follow this example, you need to download the Qlik Sense Tutorial - Building an App to get the [dataset](#glossary-6 "Glossary term"). If you have completed the tutorial you can use the application you created. Otherwise you need to create an application, add all six data files in the Tutorials source folder, and associate them using automatic recommendations in the data manager.

### Create alternate states

For this example we need two alternate states. In Master items > Alternate states:

1. Create a new state called Group 1.
2. Create a new state called Group 2.

You have now created the two alternate states we need in this example.

### Create filter panes for selection

Do the following:

1. Add a filter pane with the field Region.
2. Edit the label of the filter pane to say =StateName(). This is to make it easier to tell them apart, as the state is not indicated in the filter pane. The StateName() function returns the state that is applied to the function.
3. Drop the state Group 1 on the filter pane and select Apply state.
4. Add another filter pane with the field Region.
5. Edit the label of the second filter pane to say =StateName().
6. Drop the state Group 2 on the second filter pane and select Apply state.

You have now created the two filter panes that are used to control the selections of each of the two states. When you make a selection in the Group 1 filter pane, the same selection is applied to the state Group 1 which is reflected in all visualizations connected to that state.

### Create a bar chart for analysis

Do the following:

1. Create a [master item](#glossary-8 "Glossary term") measure with name Group1Sales.

   Set Expression to Sum({[Group 1]}[Sales]).

   This expression sums the sales for all selections in the Group 1 state.

   Set Label expression to 'Sales '&GetCurrentSelections(chr(13)&chr(10), '=', ',' ,9,'Group 1').

   We use a label expression to be able to show the current selection of the state as a label in the chart, instead of the default label.
2. Create another master item measure with name Group2Sales.

   Set Expression to Sum({[Group 2]}[Sales]).

   Set Label expression to 'Sales '&GetCurrentSelections(chr(13)&chr(10), '=', ',' ,9,'Group 2').
3. Add a bar chart to the sheet.
4. Set the Product Line field as dimension.
5. Add the measures Group1Sales and Group2Sales.

You have now created a bar chart that shows the sales by product line for the two groups of regions selected in the filter panes. When you make a new selection in one of the filter panes, the corresponding measure value changes according to the new selection.

### Discovery

You can now make selections in Group 1 and Group 2, and see the results of the selected combinations of regions in the bar chart.

## Permissions

For more information about the required permissions for creating and deleting alternate states, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).
