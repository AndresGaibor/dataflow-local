---
title: "Editing a master measure"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Assets/edit-master-measure.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Reusing measures with master measures"]
---

# Editing a master measure

When you update a master [measure](#glossary-0 "Glossary term"), the changes will be reflected in all its instances, including all visualizations that use it.

Edit a master measure from the assets panel or while editing [visualization](#glossary-1 "Glossary term") [properties](#glossary-2 "Glossary term").

## Editing a master measure from the assets panel

Use the assets panel to edit a master measure when you want to preview the measure or edit several master measures.

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.

   The assets panel opens on the left-hand side.
2. Click ![Master items](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Master items in the assets panel.
3. Under Measures, click the measure that you want to edit.

   The preview opens.
4. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) at the bottom of the preview.

   Tip noteYou can also right-click the master item, and then click Edit.

   A dialog is displayed to inform you that any changes to the master measure will be applied to all visualizations that use the measure.
5. Click OK.

   The Edit measure dialog opens, where you update the expression, name, description, color, tags, and other properties.
6. Click Save.

The measure is now updated.

## Editing a master measure from visualization properties

When a measure in a visualization is linked to a master measure, you can edit the master measure from the properties panel. All visualizations in the application that use the master measure will be updated. To edit a linked measure only in this visualization, without affecting the master item, you must first unlink it from the master. See [*Unlinking from a master item*](unlinking-from-a-master-item.htm).

Do the following:

1. In edit mode, select the visualization.
2. In the properties panel, click the Data tab.

   If it is hidden, click Properties from the toolbar.
3. Under Measures, click the linked measure to edit.
4. Under Master item, click Edit.

   A dialog is displayed to inform you that any changes to the master measure will be applied to all visualizations that use the measure.
5. Make your changes to the master measure, and then click Save.

## Considerations

A master measure is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for editing master measures, see [*Permissions for working with master items*](work-with-master-items.htm#MasterItemsPermissions).

## Learn more

- [*Creating a master measure from a field*](../Measures/create-master-measure-field.htm)
- [*Creating a master measure with a common aggregation function*](../Measures/create-master-measure-common-function.htm)
