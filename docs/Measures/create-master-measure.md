---
title: "Reusing measures with master measures"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Measures/create-master-measure.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Reusing measures with master measures

When you are working with an application, you can create master [measures](#glossary-1 "Glossary term") so that they can be reused.

A master measure is a combination of an expression and descriptive data, such as name, description and tags. You can create a master measure in different ways.

[*Creating a master measure from a field*](create-master-measure-field.htm)

[*Creating a master measure with a common aggregation function*](create-master-measure-common-function.htm)

[*Creating a master measure by typing the expression*](create-master-measure-type-expression.htm)

[*Creating a master measure from the data model viewer*](create-master-measure-data-model-viewer.htm)

You can also create a master measure based on a measure created in a [visualization](#glossary-2 "Glossary term"). Under the measure in the [properties](#glossary-3 "Glossary term") panel of a visualization, click Add new under Master items.

## Master measure formatting

Number formatting, color, and label can be configured for a master measure. These properties are not applied to a visualization if you reference the master measure using an expression. To apply these properties in a visualization, create a direct link to the master measure when configuring the visualization.

Do the following:

1. Expand Data > Measures in the properties panel.
2. Click Add.
3. In the drop down menu, under Measures, select the master measure.

A direct link is now created to the master measure.

## Considerations

A master measure is a type of master item. When working with master items, consider the following:

- Master items can only be viewed, edited, created, and deleted when editing a private sheet. You cannot perform actions on master items from a public or community sheet.
- Depending on your permissions, your access to master items might be limited. For example, you might be able to view the master items in an application but not create, edit, or delete them. For more information about how permissions affect actions on master items, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).
- You cannot create, edit, or delete the master items of a published application. Instead, perform these actions in the source application and then re-publish the application to the managed space.

## Permissions

For more information about the required permissions for creating master measures, see [*Permissions for working with master items*](../Assets/work-with-master-items.htm#MasterItemsPermissions).

## Learn more

[*Using master measures in expressions*](use-master-measures-expressions.htm)

[*Reusing assets with master items*](../Assets/work-with-master-items.htm)

[*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm)

[*Measures*](measures.htm)

[*Data grouping with dimensions*](../Dimensions/dimensions.htm)
