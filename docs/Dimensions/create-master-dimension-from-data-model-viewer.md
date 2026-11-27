---
title: "Creating a master dimension from the data model viewer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Dimensions/create-master-dimension-from-data-model-viewer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Viewing and transforming the data model"]
---

# Creating a master dimension from the data model viewer

When you are working with an unpublished application, you can create master dimensions so that they can be reused. Users of a published application will have access to the master dimensions, but will not be able to modify them.
The data model viewer is not available in a published application.

Do the following:

1. In the data model viewer, select a [field](#glossary-1 "Glossary term") and open the Preview panel.
2. Click Add as dimension.

   The Create new dimension dialog opens, with the selected field. The name of the selected field is also used as the default name of the dimension.
3. Change the name if you want to, and optionally add a description, color, and tags.
4. If a custom [logical model](#glossary-2 "Glossary term") is activated for the application, optionally select the Logical model group to which the master dimension will be added. If you do not select a group, the master dimension is ungrouped and therefore cannot be used in Insight Advisor interactions by any user. You can later select or change the group when editing the master dimension, or by editing the logical model of the application.

   [*Defining fields and groups in Insight Advisor*](../BusinessLogic/business-logic-fields-groups.htm)
5. Click Create.
6. Click Done to close the dialog.

The dimension is now saved to the master items tab of the assets panel.

Tip noteYou can quickly add several dimensions as master items by clicking Add dimension after adding each dimension. Click Done when you have finished.

## Considerations

A master dimension is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for creating master dimensions, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).

## Learn more

- [*Data grouping with dimensions*](dimensions.htm)
- [*Measures*](../Measures/measures.htm)
