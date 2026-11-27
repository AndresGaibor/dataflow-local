---
title: "Hierarchy"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Hierarchy.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# Hierarchy

The hierarchy
prefix is used to transform a parent-child hierarchy table to a table that is useful in a Qlik Sense data model. It can be put in front of a LOAD
or a SELECT
statement and will use the result of the loading statement as input for a table transformation.

The prefix creates an expanded nodes table, which normally has the same number of records as the input table, but in addition each level in the hierarchy is stored in a separate [field](#glossary-0 "Glossary term"). The path field can be used in a tree structure.

Syntax:

Hierarchy (NodeID,
ParentID, NodeName,
[ParentName, [PathSource,
[PathName, [PathDelimiter,
Depth]]]])(loadstatement | selectstatement)

The input table must be an adjacent nodes table. Adjacent nodes tables are tables where each record corresponds to a node and has a field that contains a reference to the parent node. In such a table the node is stored on one record only but the node can still have any number of children. The table may of course contain additional fields describing attributes for the nodes.

The prefix creates an expanded nodes table, which normally has the same number of records as the input table, but in addition each level in the hierarchy is stored in a separate field. The path field can be used in a tree structure.

Usually the input table has exactly one record per node and in such a case the output table will contain the same number of records. However, sometimes there are nodes with multiple parents, i.e. one node is represented by several records in the input table. If so, the output table may have more records than the input table.

All nodes with a parent id not found in the node id column (including nodes with missing parent id) will be considered as roots. Also, only nodes with a connection to a root node - direct or indirect - will be loaded, thus avoiding circular references.

Additional fields containing the name of the parent node, the path of the node and the depth of the node can be created.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| NodeID | The name of the field that contains the node id. This field must exist in the input table. |
| ParentID | The name of the field that contains the node id of the parent node. This field must exist in the input table. |
| NodeName | The name of the field that contains the name of the node. This field must exist in the input table. |
| ParentName | A string used to name the new ParentName field. If omitted, this field will not be created. |
| ParentSource | The name of the field that contains the name of the node used to build the node path. Optional parameter. If omitted, NodeName will be used. |
| PathName | A string used to name the new Path field, which contains the path from the root to the node. Optional parameter. If omitted, this field will not be created. |
| PathDelimiter | A string used as delimiter in the new Path field. Optional parameter. If omitted, '/' will be used. |
| Depth | A string used to name the new Depth field, which contains the depth of the node in the hierarchy. Optional parameter. If omitted, this field will not be created. |

Example:

Hierarchy(NodeID, ParentID, NodeName, ParentName, NodeName, PathName, '\', Depth) LOAD \* inline [

NodeID, ParentID, NodeName

1, 4, London

2, 3, Munich

3, 5, Germany

4, 5, UK

5, , Europe

];

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NodeID | ParentID | NodeName | NodeName1 | NodeName2 | NodeName3 | ParentName | PathName | Depth |
| 1 | 4 | London | Europe | UK | London | UK | Europe\UK\London | 3 |
| 2 | 3 | Munich | Europe | Germany | Munich | Germany | Europe\Germany\Munich | 3 |
| 3 | 5 | Germany | Europe | Germany | - | Europe | Europe\Germany | 2 |
| 4 | 5 | UK | Europe | UK | - | Europe | Europe\UK | 2 |
| 5 |  | Europe | Europe | - | - | - | Europe | 1 |

## Learn more

- [*Load*](../ScriptRegularStatements/Load.htm)
- [*Select*](../ScriptRegularStatements/Select.htm)
- [*Loading hierarchy data*](../../DataSource/hierarchies.htm)
