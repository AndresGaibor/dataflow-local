---
title: "Creating a calculated dimension"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Dimensions/create-calculated-dimension.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Reusing dimensions with master dimensions"]
---

# Creating a calculated dimension

You can create a calculated [dimension](#glossary-0 "Glossary term") from the Master items tab in the assets panel. The expression editor opens from the Create new dimensions dialog.

Do the following:

1. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.

   The assets panel opens on the left-hand side.
2. Click ![Master items](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Master items in the assets panel.
3. Next to Measures, click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).

   The Create new dimensions dialog opens.
4. Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) in the Field text box to open the Add expression dialog.

You will now be able to add expressions in different ways and with different levels of complexity, depending on your preferences.

Tip noteYou can also add an expression by typing directly into the Field text box, but you will then not be provided with syntax highlighting and syntax check.

## Using a common function

1. Select a [field](#glossary-1 "Glossary term") from the drop-down list.
2. Click the [aggregation](#glossary-2 "Glossary term") function you want to use.
3. Click Insert to insert the function and the field into the expression editor.

   Tip noteYou can insert just a function or just a field by selecting only one of them.
4. Click Apply to close the Add expression dialog.

   Continue by adding the descriptive data for the dimension.

## Adding an expression by typing

1. Type the expression directly in the expression editor.

   The field names you use in the expression are checked, and the syntax of the expression is validated.

   Tip noteAs you type in the expression editor, the expression is validated continuously. If there is an error, you see a hint about what is incorrect. Additional error information may be available by clicking the icon next to the hint.

   Each line in the expression editor is numbered and syntax highlighting is used.
2. Click Apply to close the Add expression dialog.

   For a [measure](#glossary-3 "Glossary term"), you continue by adding the descriptive data for the measure.

## Adding an expression through the properties panel

You can add an expression to a [visualization](#glossary-4 "Glossary term") through the [properties](#glossary-5 "Glossary term") panel.

1. Open the [sheet](#glossary-6 "Glossary term") with the visualization that you want to edit.
2. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet to open the properties panel (If it is hidden, click Properties).
3. Click the visualization that you want to edit.

   The properties panel for that visualization is displayed on the right-hand side.
4. Under Data, click Add data and select Dimension.

   A dimension text box is displayed.
5. Type your expression. The expression must begin with an equals sign (=), otherwise the string will be interpreted as text.

## Detailed syntax help

You can open the online help with the full description of how to use the current function by double-clicking the function name in the expression editor and pressing Ctrl+H on the keyboard. This feature becomes available after having entered the first parenthesis of the expression after the function name.

Information noteThis feature is supported only when using a computer with a keyboard.

## Adding the descriptive data for the dimension

After having entered the expression, you need to add some descriptive information.

1. Type a name for the dimension.
2. Type a description for the dimension (optional).

   If you do not add a description and then link a glossary term to your master item as a definition, the term definition will be used in the description.
3. Optionally, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_triangle_bottom.svg) in the color drop down and select a color through one of the following methods:

   - Click one of the colors in the palette.
   - Type a 6 character color code in the Hex input field: #.
   - Click ![Show options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) at the bottom of the dialog, select a color in the color wheel, and optionally adjust the saturation slider.
4. Add tags (optional).
5. Optionally, if you have access to a glossary, link the dimension to a glossary term.

   [*Linking terms to master items*](../Catalog/BusinessGlossary/business-glossaries-master-items.htm)
6. If a custom [logical model](#glossary-7 "Glossary term") is activated for the application, optionally select the Logical model group to which the master dimension will be added. If you do not select a group, the master dimension is ungrouped and therefore cannot be used in Insight Advisor interactions by any user. You can later select or change the group when editing the master dimension, or by editing the logical model of the application.

   [*Defining fields and groups in Insight Advisor*](../BusinessLogic/business-logic-fields-groups.htm)
7. Click Create.
8. Click Close.

The calculated dimension is now saved in the Dimensions category of the Master items, and you can use it in visualizations.

## Learn more

- [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm)
- [*Calculated dimensions*](calculated-dimensions.htm)
