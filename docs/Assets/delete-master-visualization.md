---
title: "Deleting a master visualization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Assets/delete-master-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Deleting a master visualization

You can delete [visualizations](#glossary-0 "Glossary term") from the master items.

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.

   The assets panel opens on the left-hand side.
2. Click ![Linked Object](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) to display the master items.
3. Click the visualization that you want to delete.

   The preview opens.
4. Click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) at the bottom of the preview.

   A dialog is displayed stating that wherever this visualization is used on [sheets](#glossary-1 "Glossary term") there will be invalid instances of it.
5. Click OK.

The visualization is deleted from the master items, and on all sheets where this visualization was used, you see invalid visualizations. You now need to replace the invalid visualization with other ones, or delete the instances.

Tip noteYou can also delete visualizations from the preview that is displayed when clicking the visualization in the master items.

## Replacing an invalid visualization on a sheet

The representation of the invalid visualization is there to tell you that there used to be a visualization at a certain location on the sheet, but the invalid visualization serves no purpose.

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.

   The assets panel opens on the left-hand side. Click ![Linked Object](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) to display the master items.
2. Drag a visualization from the master items to the location of the invalid visualization on the sheet.

The invalid visualization is replaced.

## Deleting an invalid visualization

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Right-click on the invalid visualization and select Delete in the shortcut menu.

The invalid visualization is deleted.

## Considerations

A master visualization is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for deleting master visualizations, see [*Permissions for working with master items*](work-with-master-items.htm#MasterItemsPermissions).
