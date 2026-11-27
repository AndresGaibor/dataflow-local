---
title: "Editing a master dimension"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Assets/edit-master-dimension.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Reusing dimensions with master dimensions"]
---

# Editing a master dimension

When you update a master [dimension](#glossary-0 "Glossary term"), the changes will be reflected in all its instances, including all visualizations that use it.

Edit a master dimension from the assets panel or while editing [visualization](#glossary-1 "Glossary term") [properties](#glossary-2 "Glossary term").

## Editing a master dimension from the assets panel

Use the assets panel to edit a master dimension when you want to preview the dimension or edit several master dimensions

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.

   The assets panel opens on the left-hand side.
2. Click ![Master items](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Master items in the assets panel.
3. Click the dimension that you want to edit.

   The preview opens.
4. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) at the bottom of the preview.

   If the dimension is used on a [sheet](#glossary-3 "Glossary term"), a dialog is displayed to inform you that any changes to the master dimension will be applied to all its instances on the sheets.
5. Click OK.

   The Edit dimension dialog opens, where you update the [field](#glossary-4 "Glossary term") or expression, name, description, tags, and other properties.
6. Click Save.

The master dimension is now updated.

Tip noteYou can also right-click the master item, and then click Edit.

## Editing a master dimension from visualization properties

When a dimension in a visualization is linked to a master dimension, you can edit the master dimension from the properties panel. All visualizations in the application that use the master dimension will be updated. To edit a linked dimension only in this visualization, without affecting the master item, you must first unlink it from the master. See [*Unlinking from a master item*](unlinking-from-a-master-item.htm).

Do the following:

1. In edit mode, select the visualization.
2. In the properties panel, click the Data tab.

   If it is hidden, click Properties from the toolbar.
3. Under Dimensions, click the linked dimension to edit.
4. Under Master item, click Edit.

   A dialog is displayed to inform you that any changes to the master dimension will be applied to all visualization that use the dimension.
5. Make your changes to the master dimension, and then click Save.

## Considerations

A master dimension is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for editing master dimensions, see [*Permissions for working with master items*](work-with-master-items.htm#MasterItemsPermissions).

## Learn more

- [*Creating a master dimension from master items*](../Dimensions/create-master-dimension-from-assets-panel.htm)
- [*Creating a master measure from a field*](../Measures/create-master-measure-field.htm)
