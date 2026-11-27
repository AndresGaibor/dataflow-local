---
title: "Deleting a master dimension or master measure"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Assets/delete-master-dimension-measure.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Deleting a master dimension or master measure

You can delete [dimensions](#glossary-0 "Glossary term") and [measures](#glossary-1 "Glossary term") from the [master items](#glossary-2 "Glossary term").

Information noteIf you delete a master dimension or master measure the [visualizations](#glossary-3 "Glossary term") that use the deleted master items will not work unless you replace it with a new dimension or measure.

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.

   The assets panel opens on the left-hand side.
2. Click ![Master items](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Master items in the assets panel.
3. Click the dimension or measure that you want to delete.

   The preview opens.
4. Click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) at the bottom of the preview.

   A dialog is displayed stating that all visualizations that use the dimension or measure will stop working.
5. Click OK.

The dimension or measure is deleted from the master items, and all visualizations on the [sheets](#glossary-4 "Glossary term") that used the deleted item do not work anymore. You see the text Dimension not found or Measure not found on those visualizations.

A visualization that is lacking both a dimension and a measure, both which have been deleted from the master items.

![Broken item.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_InvalidDimension2.png "Click to view full size")

## Replacing an invalid dimension or measure

When a dimension or measure has been deleted from the master items, all visualizations that reference to the deleted master item will not work anymore, until the missing dimension or measure is replaced.

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.

   The assets panel opens on the left-hand side.
2. Click ![Master items](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Master items in the assets panel.
3. Drag a dimension or measure from the Dimensions or Measures sections to the visualization on the sheet.

   The shortcut menu opens.
4. Select Replace invalid dimension or Replace invalid measure.

The visualization is complete and works again.

## Considerations

Master dimensions and master measures are types of master items. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for deleting master dimensions and measures, see [*Permissions for working with master items*](work-with-master-items.htm#MasterItemsPermissions).
