---
title: "Editing a master visualization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Assets/edit-master-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Reusing visualizations with a master visualization"]
---

# Editing a master visualization

When you update a [visualization](#glossary-0 "Glossary term") in the master items, the changes will be reflected in all instances of the master visualization.

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Click ![Master items](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Master items in the assets panel.
3. Click the visualization that you want to edit.

   The preview opens.
4. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) at the bottom of the preview.

If the visualization is used on a [sheet](#glossary-1 "Glossary term"), a dialog is displayed to inform you that any changes to the master visualization will be applied to all its instances on the sheets.

5. Click OK.

   The visualization opens for editing.

Tip noteYou can also right-click the master item, and then click Edit.

6. Make the changes you want, and click Done in the upper right corner of the visualization to finish editing.

The visualization is updated and reflected in all its instances.

Tip noteYou can also edit a master visualization by selecting a linked visualization on a sheet, and clicking Edit in the [properties](#glossary-2 "Glossary term") panel. You must be in sheet edit mode.

## Considerations

A master visualization is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for editing master visualizations, see [*Permissions for working with master items*](work-with-master-items.htm#MasterItemsPermissions).
