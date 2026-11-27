---
title: "Creating a master dimension from master items"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Dimensions/create-master-dimension-from-assets-panel.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Reusing dimensions with master dimensions"]
---

# Creating a master dimension from master items

When you are working with an application, you can create master [dimensions](#glossary-1 "Glossary term") so that they can be reused.

Do the following:

1. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.

   The assets panel opens on the left-hand side.
2. Click ![Master items](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Master items in the assets panel.
3. Next to Dimensions, click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).

   The Create new dimensions dialog opens.
4. Select if the dimension is to be single, cyclic, or drill-down.

   For drill-down dimensions, see [*Creating a drill-down dimension*](create-drill-down-dimension.htm).

   For cyclic dimensions, see [*Creating a cyclic dimension*](create-cyclic-dimension.htm).
5. Click a [field](#glossary-2 "Glossary term") on the left-hand side to select it.

   The name of the field is automatically added as the name of the dimension.
6. Change the name if you want to.
7. Type a description for the dimension (optional).

   If you do not add a description and then link a glossary term to your master item as a definition, the term definition will be used in the description.
8. If you want to specify a color, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_triangle_bottom.svg) in the color drop down and select a color through one of the following methods:

   - Click one of the colors in the palette.
   - Type a 6 character color code in the Hex input field: #.
   - Click ![Show options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) at the bottom of the dialog, select a color in the color wheel, and optionally adjust the saturation slider.
9. Add tags (optional).
10. Optionally, if you have access to a glossary, link the dimension to a glossary term.

    [*Linking terms to master items*](../Catalog/BusinessGlossary/business-glossaries-master-items.htm)
11. If a custom [logical model](#glossary-3 "Glossary term") is activated for the application, optionally select the Logical model group to which the master dimension will be added. If you do not select a group, the master dimension is ungrouped and therefore cannot be used in Insight Advisor interactions by any user. You can later select or change the group when editing the master dimension, or by editing the logical model of the application.

    [*Defining fields and groups in Insight Advisor*](../BusinessLogic/business-logic-fields-groups.htm)
12. Click Create.
13. Click Close.

The dimension is now saved in the Dimensions category in the master items, and you can use it in [visualizations](#glossary-4 "Glossary term").

Tip noteYou can quickly add several dimensions as master items by clicking Add dimension after adding each dimension. Click Done when you have finished.

## Considerations

A master dimension is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for creating master dimensions, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).
