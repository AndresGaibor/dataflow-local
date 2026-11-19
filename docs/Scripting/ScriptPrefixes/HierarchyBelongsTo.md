---
title: "HierarchyBelongsTo"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/HierarchyBelongsTo.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---
# HierarchyBelongsTo

This prefix is used to transform a parent-child hierarchy table to a table that is useful in a Qlik Sense data model. It can be put in front of a LOAD or a SELECT statement and will use the result of the loading statement as input for a table transformation.

The prefix creates a table containing all ancestor-child relations of the hierarchy. The ancestor fields can then be used to select entire trees in the hierarchy. The output table in most cases contains several records per node.

Syntax:

HierarchyBelongsTo (NodeID, ParentID,
NodeName, AncestorID,
AncestorName, [DepthDiff])(loadstatement
| selectstatement)

The input table must be an adjacent nodes table. Adjacent nodes tables are tables where each record corresponds to a node and has a [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/HierarchyBelongsTo.htm#glossary-0 "Glossary term") that contains a reference to the parent node. In such a table the node is stored on one record only but the node can still have any number of children. The table may of course contain additional fields describing attributes for the nodes.

The prefix creates a table containing all
ancestor-child relations of the hierarchy. The ancestor fields can then
be used to select entire trees in the hierarchy. The output table in most cases
contains several records per node.

An additional field containing the depth difference
of the nodes can be created.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| NodeID | The name of the field that contains the node id. This field must exist in the input table. |
| ParentID | The name of the field that contains the node id of the parent node. This field must exist in the input table. |
| NodeName | The name of the field that contains the name of the node. This field must exist in the input table. |
| AncestorID | A string used to name the new ancestor id field, which contains the id of the ancestor node. |
| AncestorName | A string used to name the new ancestor field, which contains the name of the ancestor node. |
| DepthDiff | A string used to name the new DepthDiff field, which contains the depth of the node in the hierarchy relative the ancestor node. Optional parameter. If omitted, this field will not be created. |

Example:

HierarchyBelongsTo (NodeID, AncestorID, NodeName, AncestorID, AncestorName, DepthDiff) LOAD \* inline [

NodeID, AncestorID, NodeName

1, 4, London

2, 3, Munich

3, 5, Germany

4, 5, UK

5, , Europe

];

Results

| NodeID | AncestorID | NodeName | AncestorName | DepthDiff |
| --- | --- | --- | --- | --- |
| 1 | 1 | London | London | 0 |
| 1 | 4 | London | UK | 1 |
| 1 | 5 | London | Europe | 2 |
| 2 | 2 | Munich | Munich | 0 |
| 2 | 3 | Munich | Germany | 1 |
| 2 | 5 | Munich | Europe | 2 |
| 3 | 3 | Germany | Germany | 0 |
| 3 | 5 | Germany | Europe | 1 |
| 4 | 4 | UK | UK | 0 |
| 4 | 5 | UK | Europe | 1 |
| 5 | 5 | Europe | Europe | 0 |

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
- [*Select*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Select.htm)
- [*Loading hierarchy data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/hierarchies.htm)
