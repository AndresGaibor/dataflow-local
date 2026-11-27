---
title: "Loading hierarchy data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/hierarchies.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Best practices for data modeling"]
---

# Loading hierarchy data

Unbalanced n-level hierarchies are often used to represent geographical or organizational [dimensions](#glossary-0 "Glossary term") in data, among other things.

These types of hierarchies are usually stored in an adjacent nodes table, which is in a table where each record corresponds to a node and has a [field](#glossary-1 "Glossary term") that contains a reference to the parent node.

Nodes table

| NodeID | ParentNodeID | Title |
| --- | --- | --- |
| 1 | - | General manager |
| 2 | 1 | Region manager |
| 3 | 2 | Branch manager |
| 4 | 3 | Department manager |

In such a table, the node is stored on one record only but can still have any number of children. The table may of course contain additional fields describing attributes for the nodes.

An adjacent nodes table is optimal for maintenance, but difficult to use in everyday work. Instead, in queries and analysis, other representations are used. The expanded nodes table is one common representation, where each level in the hierarchy is stored in a separate field. The levels in an expanded nodes table can easily be used e.g. in a tree structure.The hierarchy keyword can be used in the data [load script](#glossary-2 "Glossary term") to transform an adjacent nodes table to an expanded nodes table.

Example:

Hierarchy (NodeID, ParentNodeID, Title, 'Manager') LOAD
NodeID,
ParentNodeID,
Title
FROM 'lib://data/hierarchy.txt' (txt, codepage is 1252, embedded labels, delimiter is ',', msq);

Expanded nodes table

| NodeID | ParentNodeID | Title | Title1 | Title2 | Title4 | Title4 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | - | General manager | General manager | - | - | - |
| 2 | 1 | Region manager | General manager | Region manager | - | - |
| 3 | 2 | Branch manager | General manager | Region manager | Branch manager | - |
| 4 | 3 | Department manager | General manager | Region manager | Branch manager | Department manager |

A problem with the expanded nodes table is that it is not easy to use the level fields for searches or [selections](#glossary-3 "Glossary term"), since prior knowledge about which level to search or select in is needed. An ancestors table is a different representation that solves this problem. This representation is also called a bridge table.

An ancestors table contains one record for every child-ancestor relation found in the data. It contains keys and names for the children as well as for the ancestors. That is, every record describes which node a specific node belongs to. The hierarchybelongsto keyword can be used in the data load script to transform an adjacent nodes table to an ancestors table.

## Learn more

- [*Hierarchy*](../Scripting/ScriptPrefixes/Hierarchy.htm)
