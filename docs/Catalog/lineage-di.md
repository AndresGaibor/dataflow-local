---
title: "Analyzing lineage in Data Integration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/lineage-di.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Working with lineage and impact analysis in Data Integration"]
---

# Analyzing lineage in Data Integration

Lineage tracks data and data transformations backwards to the original source. Qlik Cloud provides a detailed visual representation of the history of this flow, where you can interactively examine the upstream lineage of a given [data task](#glossary-0 "Glossary term"), and the datasets and fields that are created by the data task.

The lineage of a data task summarizes its most important dependencies:

- Data tasks that are used to derive it
- Direct associations and dependencies, including owner and space
- Original source (the first known source)

To view downstream or forward-looking dependencies, you can investigate what elements would be affected by a change to the object by viewing Impact analysis. See [*Analyzing impact analysis in Data Integration*](impact-analysis-di.htm).

Information note

To use lineage, you also need View lineage set to Allowed through the default permissions or a custom security role.

## The lineage graph

The lineage graph shows the flow of data through data tasks in an interactive, graphical chart. A data task is called a node in a lineage graph. When a node is the base node being investigated, it is said to be in focus and displays as the last element in the graph. At the most granular level, field-level lineage graphs show the data sources and transformations that a node is sourced from or dependent on.

Each node represents a step in the lineage of the selected data task. This lineage information is compiled whenever a data task is prepared or run.

Typical input nodes include data sources that are used by the base node. Field-level lineage allows for detailed investigation into how fields have been calculated and their specific origin across transforms.

Information noteField level lineage is not available for datasets created in SQL transformations or transformation flows.

The nodes available in a lineage graph are the inputs to your selected data task. Select a data task, dataset or field, to designate it as the base node. Input nodes are nodes that are upstream from the base node.

Field-level lineage graph

![Field-level lineage graph](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_LineageGraph_DI.png "Click to view full size")

The nodes available in a lineage graph are the inputs to your selected base node, in other words the node in focus. The base node is the singular node for which you want to retrieve lineage; it is a data task, dataset, or field.

It will be the right-most node on your screen and outlined in blue. It is the focus of your investigation and only inputs to that base node will be presented.

While you explore the lineage, you can interactively change the base node to another data task, dataset, or field on the screen to focus your investigation.

The lines connecting the nodes are edges. Edges represent the relationship of a node to another node. They represent relationships indicating associations such as a dataset that is landed by a landing task. They can also represent data that is produced by a transformation. The collection of nodes and edges together make the lineage graph.

Nodes collapse or expand to reveal hierarchy levels from coarse to finer granularity beginning with the higher-level object down to the most granular level which is the field level.

Lineage node levels

![A node with asset, resource, table, and field levels](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_Lineage_Node_Levels_DI.png "Click to view full size")

## Node details

Details are limited by your access to that object. Details can provide the following information:

- Name
- Description
- Project
- Data store
- Space
- Owner
- Creator
- Last modified

## Navigating the lineage graph

Click and drag the graph to navigate and center the lineage graph. You can also use the navigation buttons. Select Home ![Home icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_home.svg) to center the lineage graph on the base node. Click back and forward to move around in your selections.

Lineage graph navigation

![Navigation buttons for the lineage graph.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_impact-analysis-lineage-navigation.png "Click to view full size")

You can access lineage by selecting Lineage in the context menu ![More icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on:

- A data task in a pipeline project.
- A dataset in a data task.
- A field in a dataset.

Expand ![Arrow down icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) or collapse ![Arrow up icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_up.svg) the nodes to expand or collapse groups of objects at the same level.

You can return to the pipeline project or the data task.

- Click ![More icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on any object, and then Open project to return to the pipeline project.
- Click ![More icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on any object, and then Open data task to return to the data task.

## Permissions

You must have permission to view tasks in the data space of the pipeline project to view lineage. This means that you need to have either of the following roles:

- Is owner
- Can view
- Can operate
- Can edit

If you can see the lineage graph for a base node, you are able to see basic details for the upstream lineage objects.

## Troubleshooting

For information about troubleshooting lineage errors, see[*Troubleshooting - Lineage messages*](lineage-errors.htm).
