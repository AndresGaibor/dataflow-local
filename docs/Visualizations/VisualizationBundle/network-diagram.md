---
title: "Network chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/network-diagram.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Legacy"]
---

# Network chart

The network chart (Network chart) lets you draw a network of connected nodes and edges from a data set to a [sheet](#glossary-0 "Glossary term"). A network chart shows how information flows, how components interact, and where components exist in the network.

Information noteNetwork chart is included as a part of the Visualization bundle. Visualization bundle objects have additional limitations and may not have the same support as other visualizations. For more information, see [*Visualization bundle*](visualization-bundle.htm).

A network chart can provide a broad overview or be very detailed. Nodes represent system components, and edges show the movement of information from one component to another. Network nodes are connected to the nodes they interact with the most. This [visualization](#glossary-1 "Glossary term") uses different styles, colors, sizes, and images to represent different levels of a network.

Interact with the network chart by making [selections](#glossary-2 "Glossary term") one at a time.

## What it contains

You need to define three dimensions with a fourth optional [dimension](#glossary-3 "Glossary term"):

- Node identifier: This dimension controls which nodes are presented in the chart.
- Node label: This dimension sets the label of each node.
- Node parent: This dimension sets the parent of a node, and controls the relationships between nodes. It needs to contain the value of the node identifier of the parent to connect to.
- Node group (optional): You can use this dimension to group nodes. All nodes in the same group will have the same color.

You can use up to three [measures](#glossary-4 "Glossary term") to enhance the diagram. All measures are optional, but you need to add them in the following order:

1. Tooltip: You can set a measure value that is displayed in a tooltip when hovering over a node.
2. Node size: You can set the size of the node according to a measure.
3. Edge size: You can set the width of the lines between nodes according to a measure.

Information noteYou need to add a tooltip before you can set node size. You can set edge size after adding a tooltip and node size.

## When to use the network chart

Network chart diagrams can illustrate computer or telecommunications networks. They show the components of a network and how they interact. For example, a group of connected computers, printers, modems, hubs, and routers. This type of chart is helpful when:

- Planning the structure of a network.
- Coordinating updates to an existing network.
- Reporting and troubleshooting network problems .
- Keeping track of components.
- Documenting detailed network documentation.

## Formatting your data

A network chart requires data that is structured consistently according to a network data model where each record can have multiple parents and children. Each record needs to contain at least:

- A field that identifies the node, the node identifier. Node identifier values must be integer values, starting from 0 and in sequential order.
- A field with the name of the node.
- A field that defines the parent node. This value needs to be the node identifier of another node. If this field is empty, and no other record refers to this node, a disconnected node is created.

Tip noteIt is also possible to use a hierarchical data model where each node has a single parent. This will create a tree-shaped chart.

Here is some example data that you can save in a text editor and load in a new application. You need to load both example files. The example shows passenger flows between different airports.

- ID is the identifier of an airport node.
- Name is the name of an airport node. This is used as label of the node.
- LinkTo contains the node identifier of the parent node.
- Group states the group of a node. This can be used to color the nodes according to group.
- Volume is the passenger flow volume between ID and LinkTo. This can be used as a measure in edge size.
- NodeVolume is the total passenger flow volume for a node. This is loaded in a separate table as the chart cannot aggregate the volumes automatically.

Example 1: Airports1.csv

ID;Name;LinkTo;Group;Volume
0;Frankfurt;;0;
1;London;0;1;5
2;Madrid;0;1;4
2;Madrid;1;1;8
3;Warsaw;0;1;7
4;Arlanda;0;1;1
3;Warsaw;1;1;5
4;Arlanda;1;1;6
5;Tunis;0;2;8
5;Tunis;2;2;4
6;Berlin;0;1;6
6;Berlin;4;1;4
7;Rome;0;1;6
7;Rome;6;1;3
8;San Francisco;0;3;2
9;New York;0;3;9

Example 2: Airports2.csv

ID,NodeVolume
0,48
1,24
2,16
3,12
4,11
5,12
6,13
7,9
8,2
9,9

## Limitations

For information about general limitations, see [*Limitations*](visualization-bundle.htm#Limitati).

- Network chart visualizations cannot be used in Qlik NPrinting reports.
- The maximum size of the data set displayed in the network chart is 1400 rows. If the selected data set is larger, nodes and links can be omitted from the chart.

  Use a smaller data set or employ [selections](#glossary-5 "Glossary term") to limit the data set.

Related learning:

- [How do I configure a Visualization Bundle Network chart?](/lnk/How_configure_Visualization_Bundle_Network_chart)
