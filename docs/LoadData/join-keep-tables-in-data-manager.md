---
title: "Joining tables in Data manager"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/join-keep-tables-in-data-manager.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager"]
---

# Joining tables in Data manager

Join is an operation that can be used to manually combine two tables' data, producing varied results depending on the configuration you select.

This allows more granular control over combined tables than with concatenation. See [*Concatenating tables in Data manager*](concatenating-tables-in-data-manager.htm) to learn more about concatenation.

The Join operation takes two tables and combines them into one, which will be a combination of the fields in both original tables, based on the overlap of a common value for one or several common fields. There are multiple operators that can be applied to Join operations: Outer, Inner, Left, and Right.

Warning noteA joined table still occupies the amount of memory as the tables combined in it. Excessive use of joined tables may cause Qlik Sense to slow down. The information that is excluded by a join operation will not be accessible by Qlik Sense until the table is split.

## Join operators

There are four join operators: Outer join, Inner join, Left join, and Right join. The selected operator determines which overlapping fields or values are included or excluded.

Information noteWhen the join operators refer to Left and Right tables, they are referring to the first and second tables respectively, in order of selection.

### Outer join

The Outer join operator contains all possible combinations of values from the two tables, if the overlapping field values are represented in either one or both tables. For a more detailed explanation and examples, see the scripting reference entry: [*Outer*](../Scripting/ScriptPrefixes/Outer.htm).

Example:

First table

| A | B |
| --- | --- |
| 1 | aa |
| 2 | cc |
| 3 | ee |

Second table

| A | C |
| --- | --- |
| 1 | xx |
| 4 | yy |

Joined table

| A | B | C |
| --- | --- | --- |
| 1 | aa | xx |
| 2 | cc | - |
| 3 | ee | - |
| 4 | - | yy |

### Inner join

The Inner join operator only contains combinations of values from the two tables, if the overlapping field values are represented in both tables. For a more detailed explanation and examples, see the scripting reference entry: [*Inner*](../Scripting/ScriptPrefixes/Inner.htm).

Example:

First table

| A | B |
| --- | --- |
| 1 | aa |
| 2 | cc |
| 3 | ee |

Second table

| A | C |
| --- | --- |
| 1 | xx |
| 4 | yy |

Joined table

| A | B | C |
| --- | --- | --- |
| 1 | aa | xx |

### Left join

The Left join operator contains combinations of values from the two tables, if the overlapping field values are represented in the first table. For a more detailed explanation and examples, see the scripting reference entry: [*Left*](../Scripting/ScriptPrefixes/Left.htm).

Example:

First table

| A | B |
| --- | --- |
| 1 | aa |
| 2 | cc |
| 3 | ee |

Second table

| A | C |
| --- | --- |
| 1 | xx |
| 4 | yy |

Joined table

| A | B | C |
| --- | --- | --- |
| 1 | aa | xx |
| 2 | cc | - |
| 3 | ee | - |

### Right join

The Right join operator contains combinations of values from the two tables, if the overlapping field values are represented in the second table. For a more detailed explanation and examples, see the scripting reference entry: [*Right*](../Scripting/ScriptPrefixes/Right.htm).

Example:

First table

| A | B |
| --- | --- |
| 1 | aa |
| 2 | cc |
| 3 | ee |

Second table

| A | C |
| --- | --- |
| 1 | xx |
| 4 | yy |

Joined table

| A | B | C |
| --- | --- | --- |
| 1 | aa | xx |
| 4 | - | yy |

## Joining tables

The Concatenate or join pane is accessed by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in Data manager, clicking Concatenate or join, and selecting two tables. When tables are selected in Concatenate or join tables, Qlik Sense analyzes the fields and automatically maps any fields together that match. If there are no clear matches, fields are left unmapped. When the join is applied, mapped fields are combined in the joined table. Unmapped fields are either included as individual fields with null values for the rows where there is no corresponding value, or excluded entirely if there are no overlapping instances of the value.

The first table selected in Concatenate or join tables is set as the primary table, the table to which the other table is joined. The joined table uses the table and field names from the primary table unless these are manually renamed. You can change which table is the primary table with the ![Swap](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_swap.svg) button. Concatenate or join tables arranges fields in two rows, with the primary table fields in the top row and the secondary table fields on the bottom row. You can swap the primary and secondary tables with the ![Swap](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_swap.svg) button.

You can use Edit mappings to change the default mapping and select which fields to map, leave unmapped, or to exclude from the joined table. Edit mappings contains a drag and drop interface for editing mappings and the Fields pane, which lists all table fields. Fields can be mapped by dragging them beneath a primary table field. Fields can be added as a new unmapped field by ![Drop ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_drop.svg) beside the field in the Fields pane or dragging them into the top row of fields. Unmapped fields are marked with ![warning](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning.svg) in the Fields pane. Fields removed from the joined table are not included in the table and are not available for use in Qlik Sense after joins are applied to the table.

Once mappings are applied and the tables are joined, you cannot edit the mapped fields, but they can be removed from the tables by splitting the joined table, which restores the tables to their original state.

To join tables in [Data manager](#glossary-0 "Glossary term"), do the following:

1. Select tables for joining.
2. Optionally, rename the joined table and the field names.
3. Optionally, edit mappings.
4. Select the join operator.
5. Join the tables.

### Selecting tables for joining

Do the following:

1. In Data manager, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the bottom row.
2. Click Concatenate or join.

   The Concatenate or join pane opens.
3. Select two tables.

   The fields of both tables will be mapped or left unmapped in the Concatenate or join tables pane.
4. To preview a sample of unique values in each field, click ![View](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view.svg).
5. To switch the primary and secondary tables, click ![Swap](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_swap.svg).

### Renaming the table and field names

Do the following:

1. In the Concatenate or join pane, in the table name field, enter a new table name.
2. In a field name field, enter a new field name.

### Editing mappings

Do the following:

1. In the Concatenate or join pane, click Edit mappings.
2. To map two fields, click and drag a table field under a primary table field.
3. To add a new unmapped field, click and drag a table field into the upper row of fields.
4. To remove a field from the joined table, in the field click ![Cancel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg).
5. To return a removed field back to the table, click in the Fields pane, click ![Drop ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_drop.svg) beside the field.
6. Click Edit mappings to close Edit mappings.

### Selecting the join operator

Do the following:

1. In the Concatenate or join pane, click Select action.
2. Select an operator from the list: Outer join, Inner join, Left join, or Right join.

### Joining tables

Do the following:

- In the Concatenate or join pane, click Apply.

The tables are now joined.

## Splitting joined tables

In cases where joining is no longer needed, you can split the joined tables into their source tables.

Information note

Splitting a joined table will remove any associations the joined table had as well as any associations the primary and secondary tables had with each other. If you want to preserve your associations while splitting joined tables, click ![Undo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_back_outline.svg) to undo the join instead of splitting the table. You cannot use ![Undo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_forward_outline.svg) to undo joins after you load data in Data manager.

### Splitting a joined table

Do the following:

1. Select the joined table.
2. Click ![Split](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_split.svg).

The table is now split into its source tables. All fields in the source tables and their fields have their pre-join names. Splitting a joined table only splits one level of joining, so that any joined tables that were part of the split joined table have their own join preserved.

Related learning:

- [Data manager associations, concatenations and joins](/lnk/Data_Manager_Assocs_Concats_Joins_QS)
