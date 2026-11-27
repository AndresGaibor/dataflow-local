---
title: "Handling hierarchical data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/handling-hierarchical-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Next steps in scripting"]
---

# Handling hierarchical data

Hierarchies are an important part of all business intelligence solutions, used to describe [dimensions](#glossary-0 "Glossary term") that naturally contain different levels of granularity. Some are simple and intuitive whereas others are complex and demand a lot of thinking to be modeled correctly.

From the top of a hierarchy to the bottom, the members are progressively more detailed. For example, in a dimension that has the levels Market, Country, State and City, the member Americas appears in the top level of the hierarchy, the member U.S.A. appears in the second level, the member California appears in the third level and San Francisco in the bottom level. California is more specific than U.S.A., and San Francisco is more specific than California.

Storing hierarchies in a relational model is a common challenge with multiple solutions. There are several approaches:

- The Horizontal hierarchy
- The Adjacency list model
- The Path enumeration method
- The Nested sets model
- The Ancestor list

For the purposes of this tutorial we will be creating an Ancestor list since it presents the hierarchy in a form that is directly usable in a query. Further information on the other approaches can be found in Qlik Community.

## Hierarchy prefix

The Hierarchy prefix is a script command that you put in front of a LOAD or SELECT statement that loads an adjacent nodes table. The LOAD statement needs to have at least three fields: An ID that is a unique key for the node, a reference to the parent and a name.

The prefix will transform a loaded table into an expanded nodes table; a table that has a number of additional columns, one for each level of the hierarchy.

Do the following:

1. Create a new application and give it a name.
2. Add a new script section in the Data load editor.
3. Call the section Wine.
4. Under DataFiles in the right menu, click Select data.
5. Upload and then select Winedistricts.txt.
6. In the Select data from window, uncheck the Lbound and RBound fields so that they are not loaded.
7. Click Add.
8. Enter the following above the LOAD statement:

```
Hierarchy (NodeID, ParentID, NodeName)
```

Your script should look like this:

```
Hierarchy (NodeID, ParentID, NodeName)
LOAD
    NodeID,
    ParentID,
    NodeName
FROM [lib://DataFiles/Winedistricts.txt]
(txt, utf8, embedded labels, delimiter is '\t', msq);
```

9. Click Load data.
10. Use the Preview section of the Data model viewer to view the resulting table.

The resulting expanded nodes table has exactly the same number of records as its source table: One per node. The expanded nodes table is very practical since it fulfills a number of requirements for analyzing a hierarchy in a relational model:

- All the node names exist in one and the same column, so that this can be used for searches.
- In addition, the different node levels have been expanded into one field each; fields that can be used in drill-down groups or as dimensions in pivot tables.
- In addition, the different node levels have been expanded into one field each; fields that can be used in drill-down groups.
- It can be made to contain a path unique for the node, listing all ancestors in the right order.
- It can be made to contain the depth of the node, i.e. the distance from the root.

The resulting table looks like this:

Table showing sample of data loaded using Hierarchy prefix

![Table showing sample of data loaded using Hierarchy prefix.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-hierarchyprefix-table.png "Click to view full size")

## HierarchyBelongsTo prefix

Like the Hierarchy prefix, the HierarchyBelongsTo prefix is a script command that you put in front of a LOAD or SELECT statement that loads an adjacent nodes table.

Also here, the LOAD statement needs to have at least three fields: An ID that is a unique key for the node, a reference to the parent and a name. The prefix will transform the loaded table into an ancestor table, a table that has every combination of an ancestor and a descendant listed as a separate record. Hence, it is very easy to find all ancestors or all descendants of a specific node.

Do the following:

1. Modify the Hierarchy statement in the Data load editor so that it reads as follows:

```
HierarchyBelongsTo (NodeID, ParentID, NodeName, BelongsToID, BelongsTo)
```

1. Click Load data.
2. Use the Preview section of the Data model viewer to view the resulting table.

The ancestor table fulfills a number of requirements for analyzing a hierarchy in a relational model:

- If the node ID represents the single nodes, the ancestor ID represents the entire trees and sub-trees of the hierarchy.
- All the node names exist both in the role as nodes and in the role as trees, and both can be used for searches.
- It can be made to contain the depth difference between the node depth, and the ancestor depth, that is, the distance from the root of the sub-tree.

The resulting table looks like this:

Table showing data loaded using HierarchyBelongsTo prefix

![Table showing data loaded using HierarchyBelongsTo prefix.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-hierarchybelongsto-table.png "Click to view full size")

### Authorization

It is not uncommon that a hierarchy is used for authorization. One example is an organizational hierarchy. Each manager should have the right to see everything pertaining to their own department, including all its sub-departments. But they should not necessarily have the right to see other departments.

Organizational hierarchy example

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_Authorization1.png "Click to view full size")

This means that different people will be allowed to see different sub-trees of the organization. The authorization table may look like the following:

Authorization table

| ACCESS | NTNAME | PERSON | POSITION | PERMISSIONS |
| --- | --- | --- | --- | --- |
| USER | ACME\JRL | John | CPO | HR |
| USER | ACME\CAH | Carol | CEO | CEO |
| USER | ACME\JER | James | Director Engineering | Engineering |
| USER | ACME\DBK | Diana | CFO | Finance |
| USER | ACME\RNL | Bob | COO | Sales |
| USER | ACME\LFD | Larry | CTO | Product |

In this case, Carol is allowed to see everything pertaining to the CEO and below; Larry is allowed to see the Product organization; and James is allowed to see the Engineering organization only.

Example:

Often the hierarchy is stored in an adjacent nodes table. In this example, to solve this, you can load the adjacent nodes table using a HierarchyBelongsTo and name the ancestor [field](#glossary-1 "Glossary term")Tree.

If you want to use Section Access, load an upper case copy of Tree and call this new field PERMISSIONS. Finally, you need to load the authorization table. These two last steps can be done using the following script lines. Note that the TempTrees table is the table created by the HierarchyBelongsTo statement.

Note that this is an example only. There is no accompanying exercise to be completed in Qlik Sense.

Trees:
LOAD \*,
Upper(Tree) as PERMISSIONS
Resident TempTrees;
Drop Table TempTrees;
 
Section Access;
Authorization:
LOAD ACCESS,
NTNAME,
UPPER(Permissions) as PERMISSIONS
From Organization;
Section Application;

This example would produce the following data model:

Data model: Authorization, Trees, Fact, and Nodes tables

![Data model: Authorization, Trees, Fact, and Nodes tables.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_Authorization3.png "Click to view full size")
