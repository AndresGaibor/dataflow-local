---
title: "Creating a master measure with a common aggregation function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Measures/create-master-measure-common-function.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Reusing measures with master measures"]
---

# Creating a master measure with a common aggregation function

When you are working with an application, you can create master measures so that they can be reused. You can easily create a [measure](#glossary-0 "Glossary term") using one of the most common [aggregation](#glossary-1 "Glossary term") functions by selecting the function and the [field](#glossary-2 "Glossary term") from drop-down lists.

When naming an entity, avoid assigning the same name to more than one field, variable, or measure. There is a strict order of precedence for resolving conflicts between entities with identical names. This order is reflected in any objects or contexts in which these entities are used. This order of precedence is as follows:

- Inside an aggregation, a field has precedence over a variable. Measure labels are not relevant in aggregations and are not prioritized.
- Outside an aggregation, a measure label has precedence over a variable, which in turn has precedence over a field name.
- Additionally, outside an aggregation, a measure can be re-used by referencing its label, unless the label is in fact a calculated one. In that situation, the measure drops in significance in order to reduce risk of self-reference, and in this case the name will always be interpreted first as a measure label, second as a field name, and third as a variable name.

Do the following:

1. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.

   The assets panel opens on the left-hand side.
2. Click ![Master items](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Master items in the assets panel.
3. Next to Measures, click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
4. Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) in the Expression field to open the Add expression dialog.

   You find drop-down lists for selecting a field and a common function on the right-hand side.
5. If you want to show fields from a particular table, select this table in the top drop-down list (optional).
6. Select a field from the Field drop-down list.
7. Select a function from the bottom drop-down list.

   Tip noteYou can insert just a field by not selecting a function.
8. Click Insert to insert the field and the function into the expression editor.

   Tip noteYou can open the online help with the full description of how to use the current function by double-clicking the function name in the expression editor and pressing Ctrl+H on the keyboard. This feature becomes available after having entered the first parenthesis of the expression after the function name, and only when using a computer with a keyboard.
9. Click Apply to close the Add expression dialog.

   Now you need to add some descriptive data for the measure.
10. Type a name for the measure.
11. Type a description for the measure (optional).

    If you do not add a description and then link a glossary term to your master item as a definition, the term definition will be used in the description.
12. If you want to specify a color, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_triangle_bottom.svg) in the color drop down and select a color through one of the following methods:

    - Click one of the colors in the palette.
    - Type a 6 character color code in the Hex input field.
    - Click ![Show options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) at the bottom of the dialog, select a color in the color wheel, and optionally adjust the saturation slider.
13. Add tags (optional).
14. Optionally, if you have access to a glossary, link the measure to a glossary term.

    [*Linking terms to master items*](../Catalog/BusinessGlossary/business-glossaries-master-items.htm)
15. If a custom [logical model](#glossary-3 "Glossary term") is activated for the application, optionally select the Logical model group to which the master measure will be added. If you do not select a group, the master measure is ungrouped and therefore cannot be used in Insight Advisor interactions by any user. You can later select or change the group when editing the master measure, or by editing the logical model of the application.

    [*Defining fields and groups in Insight Advisor*](../BusinessLogic/business-logic-fields-groups.htm)
16. Under Number formatting, you can choose:

    - Auto
    - Number
    - Money
    - Date
    - Duration
    - Custom
    - Measure expression
17. Click Create.

The measure is now saved in the Measures category in the master items, and you can use it in [visualizations](#glossary-4 "Glossary term").

## Considerations

A master measure is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for creating master measures, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).

## Learn more

- [*Basic aggregation functions*](../Scripting/AggregationFunctions/basic-aggregation-functions.htm)
