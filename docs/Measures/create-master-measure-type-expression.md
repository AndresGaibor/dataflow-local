---
title: "Creating a master measure by typing the expression"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Measures/create-master-measure-type-expression.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Reusing measures with master measures"]
---

# Creating a master measure by typing the expression

When you are working with an application, you can create master measures so that they can be reused. You can add complex expressions by typing the expression into the expression editor.

1. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.

   The assets panel opens on the left-hand side.
2. Click ![Master items](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Master items in the assets panel.
3. Next to Measures, click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
4. Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) in the Expression field to open the Add expression dialog.
5. Type the expression directly in the expression editor (the main window).

   The field names you use in the expression are checked, and the syntax of the expression is validated.

   Tip noteAs you type in the expression editor, the expression is validated continuously. If there is an error, you see a hint about what is incorrect in the lower left-hand corner. Additional error information may be available by clicking the icon next to the hint.

   Each line in the expression editor is numbered and syntax highlighting is used.

   Tip noteYou can open the online help with the full description of how to use the current function by double-clicking the function name in the expression editor and pressing Ctrl+H on the keyboard. This feature becomes available after having entered the first parenthesis of the expression after the function name, and only when using a computer with a keyboard.
6. Click Apply to close the Add expression dialog.

   Now you need to add some descriptive data for the measure.
7. Type a name for the measure.
8. Type a description for the measure (optional).

   If you do not add a description and then link a glossary term to your master item as a definition, the term definition will be used in the description.
9. If you want to specify a color, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_triangle_bottom.svg) in the color drop down and select a color through one of the following methods:

   - Click one of the colors in the palette.
   - Type a 6 character color code in the Hex input field.
   - Click ![Show options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) at the bottom of the dialog, select a color in the color wheel, and optionally adjust the saturation slider.
10. Add tags (optional).
11. Optionally, if you have access to a glossary, link the measure to a glossary term.

    [*Linking terms to master items*](../Catalog/BusinessGlossary/business-glossaries-master-items.htm)
12. If a custom [logical model](#glossary-0 "Glossary term") is activated for the application, optionally select the Logical model group to which the master measure will be added. If you do not select a group, the master measure is ungrouped and therefore cannot be used in Insight Advisor interactions by any user. You can later select or change the group when editing the master measure, or by editing the logical model of the application.

    [*Defining fields and groups in Insight Advisor*](../BusinessLogic/business-logic-fields-groups.htm)
13. Under Number formatting, you can choose:

    - Auto
    - Number
    - Money
    - Date
    - Duration
    - Custom
    - Measure expression
14. Click Create.

The measure is now saved in the Measures category in the master items, and you can use it in [visualizations](#glossary-1 "Glossary term").

## Considerations

A master measure is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for creating master measures, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).

## Learn more

- [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm)
