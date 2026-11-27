---
title: "Reusing visualizations with a master visualization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/create-master-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Reusing visualizations with a master visualization

You can create a master [visualization](#glossary-0 "Glossary term") to be able to reuse it. Users of a published application will have access to the master visualization but will not be able to modify them.

Information noteYou can only create master visualizations when you are working with an unpublished application. Visualizations with Chart suggestions enabled cannot be made into a master visualization.

Do the following:

1. Add a name, or change the name if you want to.
2. Type a description for the visualization (optional).
3. Add tags (optional).
4. Click Add.

The visualization is now saved to the master items tab.

Tip noteYou can also add a visualization to the master items by right-clicking it on the sheet, and selecting ![Linked Object](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Add to master items.

## Considerations

A master visualization is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for editing master visualizations, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).

## Learn more

- [*Reusing assets with master items*](../Assets/work-with-master-items.htm)
- [*Assets panel in edit mode*](../Sheets/sheet-view.htm#Assets)
- [*Assets panel*](../Sheets/sheet-advanced.htm#Assets)
