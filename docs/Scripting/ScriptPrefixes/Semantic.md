---
title: "Semantic"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Semantic.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# Semantic

The semantic load prefix creates a special type of [field](#glossary-0 "Glossary term") that can be used in Qlik Sense to connect and manage relational data, such as tree structures, self-referencing parent-child structured data and/or data that can be described as a graph.

Note that the semantic load can function similarly to the [*Hierarchy*](Hierarchy.htm) and [*HierarchyBelongsTo*](HierarchyBelongsTo.htm) prefixes. All three prefixes can be used as building blocks in effective front-end solutions for traversing relational data.

Syntax:

Semantic( loadstatement
| selectstatement)

A semantic load expects an input that is exactly three or four fields wide with a strict definition of what each ordered field represents, as shown in the table below:

Semantic load fields

| Field name | Field description |
| --- | --- |
| 1st Field: | This tag is a representation of the first of two objects between which there is a relationship. |
| 2nd Field: | This tag will be used to describe the “forward” relationship between the first and second object. If the first object is a child and the second object is a parent, you can create a relationship tab that states “parent” or “parent of”  as if you are following the relationship from child to parent. |
| 3rd Field: | This tag is a representation of the second of two objects between which there is a relationship. |
| 4th Field: | This field is optional. This tag describes the “backward” or “inverse” relationship between the first and second object. If the first object is a child and the second object is a parent, a relationship tab could state “child” or “child of” as if you are following the relationship from parent to child. If you do not add a fourth field, then the second field tag will be used to describe the relationship in either direction. In that case, an arrow symbol is automatically added as part of the tag. |

The following code is an example of the semantic prefix.

```
Semantic
Load
Object,
‘Parent’ AS Relationship,
NeighbouringObject AS Object,
‘Child’ AS Relationship
from graphdata.csv;
```

Information noteIt is allowed and typical practice to label the third field the same as the first field. This creates a self-referencing lookup, so that you can follow object(s) to the related object(s) one relationship step away at a time. If the 3rd field does not carry the same name, then the end result will be a simple lookup from an object(s) to its direct relational neighbor(s) one step away only, which is an output of little practical use.

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Related functions

| Functions | Interaction |
| --- | --- |
| [*Hierarchy*](Hierarchy.htm) | The Hierarchy load prefix is used to divide and organize nodes in parent-child and other graph-like data structures and transform them into tables. |
| [*HierarchyBelongsTo*](HierarchyBelongsTo.htm) | The HierarchyBelongsTo load prefix is used to locate and organize the ancestors of parent-child and other graph-like data structures and transform them into tables. |

## Example - Creating a special field for connecting relationships using the semantic prefix

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") representing geography relation records which is loaded into a table named GeographyTree.

  - Each entry has an ID at the beginning of the line and a ParentID at the end of the line.
- The semantic prefix which will add one special behavior field labeled, Relation.

Load script

```
GeographyTree:
LOAD
    ID,
    Geography,
    if(ParentID='',null(),ParentID) AS ParentID

INLINE [
ID,Geography,ParentID
1,World
2,Europe,1
3,Asia,1
4,North America,1
5,South America,1
6,UK,2
7,Germany,2
8,Sweden,2
9,South Korea,3
10,North Korea,3
11,China,3
12,London,6
13,Birmingham,6
];

SemanticTable:
Semantic Load
	ID as ID,
	'Parent' as Relation,
	ParentID as ID,
	'Child' as Relation
resident GeographyTree;
```

Results

Load the data and open a [sheet](#glossary-2 "Glossary term"). Create a new table and add these fields as [dimensions](#glossary-3 "Glossary term").

- Id
- Geography

Then, create a filter pane with Relation as a [dimension](#glossary-4 "Glossary term"). Click Done editing.

Results table

| Id | Geography |
| --- | --- |
| 1 | World |
| 2 | Europe |
| 3 | Asia |
| 4 | North America |
| 5 | South America |
| 6 | UK |
| 7 | Germany |
| 8 | Sweden |
| 9 | South Korea |
| 10 | North Korea |
| 11 | China |
| 12 | London |
| 13 | Birmingham |

Filter pane

| Relation |
| --- |
| Child |
| Parent |

Click Europe from the Geography dimension in the table and click Child from the Relation dimension in the filter pane. Note the expected result in the table:

Results table showing "children" of Europe

| Id | Geography |
| --- | --- |
| 6 | UK |
| 7 | Germany |
| 8 | Sweden |

Clicking Child again will show places that are "children" of the UK, one step further down.

Results table showing "children" of UK

| Id | Geography |
| --- | --- |
| 12 | London |
| 13 | Birmingham |
