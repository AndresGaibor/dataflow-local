---
title: "Calculate fields processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-calculate-fields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Calculate fields processor

Adds new fields based on Qlik script expressions.

The **Calculate fields** processor allows you to create new fields in the schema of your data, and fill each of them using Qlik script expressions. Your script can use everything from the input schema, allowing you to use combinations or transformed versions of existing fields.

## Usage

- The Calculate fields processor requires one input flow and can generate only one output flow.
- Click the **+** icon in the processor configuration panel to create more than one calculated field.

## Limitations

- The Calculate fields processor executes expressions in a load script context. Aggregation functions such as `firstSortedValue`, `sum`, `avg`, and `count` do not work in this processor because it processes each row individually, not within a GROUP BY aggregation. To use aggregation functions, see [*Aggregate processor*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-aggregate.htm).
- Chart-specific functions do not work in this processor because it operates in the data load layer.
- At this moment, it is not possible to create a new field and reference it within the same Calculate fields processor. It is recommended to use two distinct processors.

## Properties

Properties to configure to calculate new fields.

Configuration

| Property | Configuration |
| --- | --- |
| **Name** | Give a custom name to the newly created field. |
| **Expression** | Enter your Qlik script expression in the field to set the values of the new field. For more information on the Qlik script syntax, see [Script syntax and chart functions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/script-syntax-functions.htm). |
| **Open editor** | Use this option to use a more powerful script editor, where you can benefit from tools to help you build your expression more easily. For more information, see [*Using the expression editor*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-calculate-fields.htm#Using). |

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.

## Using the expression editor

Clicking the **Open editor** button in the configuration panel opens the **Expression editor**, a powerful script editor to help you create your new fields. Easily insert field names or functions, open documentation and check the validity of your expressions.

![Using the expression editor to create a calculated field](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/calculate_fields_expression_editor.png)

In the left panel, you can view the field currently loaded in your data flow and browse a wide range of Qlik script functions. This panel is organized in two tabs:

- **Fields**, where the fields available at this point of the flow are listed. Point your mouse over any of the field names and click **+** to directly insert it in the expression.
- **Functions**, where you can browse Qlik functions. You can use the search field to look for a specific function, or use the **Function category** drop-down to filter them.

  Point your mouse over any of the functions and click **+** to directly insert it in the expression.
- If you select the **Explainer guide** toggle, a short description and a link to the documentation will be displayed when clicking a function.

In the top panel, you can enable or disable three tools to help and guide you while writing script, as well as undo and redo buttons to fix potential mistakes.

- **Search and replace**, to automatically look for specific values and replace them if needed.

  ![Search and replace feature of the expression editor](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/calculate_fields_search_replace.png)
- **Help mode**, to turn any function you write in the script into clickable links that will take you to the documentation.

  ![Activating the help mode in the script editor](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/calculate_fields_help_mode.png)
- **Autocomplete**, to display suggestions as you type, with a short description and example of a function.

  ![Using autocomplete to write a script function](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/calculate_fields_autocomplete.png)

The bottom panel describes any potential error with your script, such as incorrect field names or invalid expressions.

![The validation tool showing an error in the script](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/calculate_fields_expression_validation.png)

When the status panel shows a green **Ok**, your expression is valid. Click **Confirm** to use this expression for your calculated field and go back to the data flow editor. You can then validate the processor configuration.

## Examples

- Setting a incremental value to use as id for the new field rows:

  ```
  RecNo()
  ```

  For more information, see [Counter functions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/counter-functions.htm).
- Using if/then/else conditions. In this example, you have loaded data with temperature, and want to include additional information depending on the values:

  ```
  If(Temperature <= 0 , 'Freezing',
  If(Temperature >= 100, 'Boiling',
  If(Temperature >0 AND Temperature < 100, 'Between')))
  ```

  For more information, see [if - script and chart function](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/if.htm).
- Performing multiple math operations in a single processor. In a dataset containing fields with a number of units sold, as well as the unit price and unit cost, then you can create two new fields for the total revenue and total cost.

  1. In the first field, enter total\_revenue as the new field name, and the following expression:

     ```
     [Units Sold] * [Unit Price]
     ```
  2. Click the **+** icon in the processor configuration panel to create another calculated field.
  3. In the second field, enter total\_cost as the new field name, and the following expression:

     ```
     [Units Sold] * [Unit Cost]
     ```

For more examples of script expressions, see [Regular statements](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/modifier-regular-statements.htm) and [Script and chart functions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/functions-in-scripts-chart-expressions.htm).
