---
title: "Reusing dimensions with master dimensions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Dimensions/create-master-dimension.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Reusing dimensions with master dimensions

When you are working with an unpublished application, you can create master dimensions so that they can be reused. Users of a published application will have access to the master dimensions, but will not be able to modify them.

You can create a master [dimension](#glossary-0 "Glossary term") in different ways.

- [*Creating a master dimension from a field*](create-master-dimension-from-field.htm)
- [*Creating a master dimension from master items*](create-master-dimension-from-assets-panel.htm)
- [*Creating a master dimension from the data model viewer*](create-master-dimension-from-data-model-viewer.htm)
- You can also create a master dimension based on a dimension created in a [visualization](#glossary-1 "Glossary term").

  Click Master item> Add new under the dimension in the property panel of a visualization.

  The Create new dimensions dialog opens, with the dimension value from the property panel in Field.

You can also create drill-down groups and cyclic dimensions:

- [*Creating a drill-down dimension*](create-drill-down-dimension.htm)
- [*Creating a cyclic dimension*](create-cyclic-dimension.htm)

## Considerations

A master measure is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for creating master dimensions, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).

## Learn more

- [*Reusing assets with master items*](../Assets/work-with-master-items.htm)
- [*Measures*](../Measures/measures.htm)
- [*Data grouping with dimensions*](dimensions.htm)
