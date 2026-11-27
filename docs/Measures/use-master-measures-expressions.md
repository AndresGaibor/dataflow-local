---
title: "Using master measures in expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Measures/use-master-measures-expressions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Reusing measures with master measures"]
---

# Using master measures in expressions

You can use master measures in expressions. You can use the master measure by itself, or use it to build a more complex expression.

When you type in the Expression editor, an auto-complete list of matching master measures opens.

Master measure in Expression editor

![Master measure in expression editor.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_MasterMeasureAutofill.png "Click to view full size")

## Considerations

When working with master measures, consider the following:

- If the master measure is renamed or deleted, references in expressions are not automatically updated. The old reference will return NULL in the expression as there is no measure by that name.

### Master measure formatting

Number formatting, color, and label can be configured for a master measure. These properties are not applied to a visualization if you reference the master measure using an expression. To apply these properties in a visualization, create a direct link to the master measure when configuring the visualization.

Do the following:

1. Expand Data > Measures in the properties panel.
2. Click Add.
3. In the drop down menu, under Measures, select the master measure.

A direct link is now created to the master measure.

## Example: Using a master measure in an expression

This example creates a master measure, and then uses the master measure in a chart expression.

1. Create the master measure.

   1. Click Master items in the assets panel.
   2. Beside Measures, click Create new.

      Create new measure button

      ![Create new measure button.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_gen_MasterMeasureCreate-saas.png "Click to view full size")
   3. In the Create new measure dialog box, enter a Name for the master measure, and then click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the Expression editor.

      Create new measure dialog box

      ![Create new measure window.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_MasterMeasureOpenEditor.png "Click to view full size")
   4. In the Expression editor, create the expression.

      You can type the expression, or use the options available in the expression builder panel. For more information, see [*Working with the expression editor*](../Expressions/work-with-expression-editor.htm).

      Insert the expression using the expression builder Count(distinct item), and then click Apply.

      Add expression in Expression editor

      ![Add expression window.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_MasterMeasureInsertExpression.png "Click to view full size")
   5. In the Create new measure dialog box, click Create.

      Create measure

      ![Create measure.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_MasterMeasureCreateButton.png "Click to view full size")

      The new master measure is created.

      New master measure

      ![Create variable for master measure.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_gen_MasterMeasureCreateButton-saas.png "Click to view full size")
2. Use the master measure in a chart expression.
   1. Add a KPI chart to a [sheet](#glossary-0 "Glossary term") in an application.

      New KPI

      ![New KPI.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_MasterMeasureKPI.png "Click to view full size")
   2. Click Add measure, and then click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the Expression editor for the KPI.

      Open Expression editor

      ![Open expression editor.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_MasterMeasureKPIExpression.png "Click to view full size")
   3. Type the master measure into the expression. As you type, you will get an auto-complete list of any available master measures. If required, the master measure can be used to build more complex expressions in the Expression editor.

      Add expression for KPI

      ![Create variable for master measure.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_MasterMeasureKPIExpressionEditor.png "Click to view full size")
   4. Close the Expression editor to view the KPI. You can change [properties](#glossary-2 "Glossary term") for the KPI, including the label, in the properties panel.

      Master measure in KPI

      ![Create variable for master measure.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_MasterMeasureKPIDone.png "Click to view full size")

## Learn more

- [*Working with the expression editor*](../Expressions/work-with-expression-editor.htm)
- [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm)
- [*Using variables in expressions*](../Variables/work-with-variables.htm)
