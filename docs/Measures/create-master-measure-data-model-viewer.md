---
title: "Creating a master measure from the data model viewer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Measures/create-master-measure-data-model-viewer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Viewing and transforming the data model"]
---

# Creating a master measure from the data model viewer

When you are working with an unpublished application, you can create master measures so that they can be reused. Users of a published application will have access to the master measures, but will not be able to modify them.

Do the following:

1. In the data model viewer, select a [field](#glossary-0 "Glossary term") and open the Preview panel.
2. Click Add as measure.

   The Create new measure dialog opens, with the selected field. The name of the selected field is also used as the default name of the measure.
3. Enter an expression for the measure.
4. Change the name if you want to, and optionally add a description, color, and tags.
5. If a custom [logical model](#glossary-1 "Glossary term") is activated for the application, optionally select the Logical model group to which the master measure will be added. If you do not select a group, the master measure is ungrouped and therefore cannot be used in Insight Advisor interactions by any user. You can later select or change the group when editing the master measure, or by editing the logical model of the application.

   [*Defining fields and groups in Insight Advisor*](../BusinessLogic/business-logic-fields-groups.htm)
6. Click Create.

The measure is now saved to the master items tab of the assets panel.

## Considerations

A master measure is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for creating master measures, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).

## Learn more

- [*Measures*](measures.htm)
- [*Data grouping with dimensions*](../Dimensions/dimensions.htm)
- [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm)
