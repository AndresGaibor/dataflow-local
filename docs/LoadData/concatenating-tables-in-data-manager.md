---
title: "Concatenating tables in Data manager"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/concatenating-tables-in-data-manager.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager"]
---

# Concatenating tables in Data manager

Concatenation combines two tables into a single table with combined fields. It consolidates content, reducing the number of separate tables and fields that share content. Tables in [Data manager](#glossary-0 "Glossary term") can be automatically or forcibly concatenated.

If you need more granular control over which data is included in combined tables, see [*Joining tables in Data manager*](join-keep-tables-in-data-manager.htm) to learn more about Join operations.

Concatenated table in Tables view and Associations view.

![Concatenated table.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ex_concatenated.png "Click to view full size")

## Automatically concatenating tables

Tables are automatically concatenated in Data manager when Qlik Sense detects that one or more added tables have both the same number of [fields](#glossary-1 "Glossary term") and identical field names as another table. When this happens, Qlik Sense automatically concatenates the tables into a single table. Automatically concatenated tables can be split if they were concatenated erroneously or if you do not want them concatenated. Automatically concatenated tables can be forcibly concatenated to other tables.

Automatically concatenated tables have the following restrictions:

- You cannot change field categories.
- You cannot unpivot an automatically concatenated table.
- You cannot add or remove data with Select data from source.

## Forcing concatenation between tables

Concatenation can be forced between tables in Data manager using the Concatenate or join pane, even if they do not entirely share the same fields or data. Forced concatenation enables you to control mapping and exclude fields from the final concatenated table. Forced concatenation supports additional transformations. Using forced concatenation, you can:

- Concatenate a concatenated table with another table.
- Concatenate an unpivoted table with another table. Forcibly concatenated tables can be unpivoted.
- Concatenate tables with calculated fields. Calculated fields can be concatenated to other fields in a forced concatenation. Calculated fields can be added to forcibly concatenated tables.

Forcibly concatenated tables have the following restrictions:

- Forced concatenation requires at least one field from each table be included in the concatenated table, although they need not be mapped together.
- Date fields cannot be formatted after concatenation. Date fields must have the same format applied to them before concatenation. Concatenated date fields use the default time format set with DateFormat in the Data load editor.
- You cannot change field categories after concatenation.
- Calculated fields that refer to a field mapped to another field in a concatenated table will only contain data for the original field rather than the combined data in the concatenated field. Calculated fields created after two tables are concatenated that refer to a field in the concatenated table will use all data in that field.
- You cannot add or remove data from a concatenated table with Select data from source. You can, however, remove fields by clicking Add data, selecting the source table, and then excluding the fields. Null values are added for the removed field’s data.

The Concatenate or join pane is accessed by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in Data manager, clicking Concatenate or join, and selecting two tables. When tables are selected in Concatenate or join, Qlik Sense analyzes the fields and automatically maps any fields together that match. If there are no clear matches, fields are left unmapped. When the concatenation is applied, mapped fields are combined in the concatenated table, while unmapped fields are included as individual fields with null values for the rows where there is no corresponding value.

The first table selected in Concatenate or join is set as the primary table, the table to which the other table is concatenated. The concatenated table uses the table and field names from the primary table unless these are manually renamed. You can change which table is the primary table with the ![Swap](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_swap.svg) button. Concatenate or join arranges fields in two rows, with the primary table fields in the top row and the secondary table fields on the bottom row. You can swap the primary and secondary tables with the ![Swap](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_swap.svg) button.

You can use Edit mappings to change the default mapping and select which fields to map, leave unmapped, or to exclude from the concatenated table. Edit mappings contains a drag and drop interface for editing mappings and the Fields pane, which lists all table fields. Fields can be mapped by dragging them beneath a primary table field. Fields can be added as a new unmapped field by ![Drop ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_drop.svg) beside the field in the Fields pane or dragging them into the top row of fields. Unmapped fields are marked with ![warning](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning.svg) in the Fields pane. Fields removed from the concatenated table are not included in the table and are not available for use in Qlik Sense after concatenation is applied to the table.

Once mappings are applied and the tables are concatenated, you cannot edit them, but they can be removed from the tables by splitting the concatenated table, which restores the tables to their original state.

To forcibly concatenate tables in Data manager, do the following:

1. Select tables for concatenation.
2. Optionally, rename the concatenated table and the field names.
3. Optionally, edit the concatenation mappings.
4. Select the concatenation operator.
5. Concatenate the tables.

### Selecting tables for concatenation

Do the following:

1. In Data manager, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the bottom row.
2. Click Concatenate or join.

   The Concatenate or join pane opens.
3. Select two tables.

   The fields of both tables will be mapped or left unmapped in the Concatenate or join pane.
4. To preview a sample of unique values in each field, click ![View](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view.svg).
5. To switch the primary and secondary tables, click ![Swap](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_swap.svg).

### Renaming the table and field names

Do the following:

1. In the Concatenate or join pane, in the table name field, enter a new table name.
2. In a field name field, enter a new field name.

### Editing concatenation mappings

Do the following:

1. In the Concatenate or join pane, click Edit mappings.
2. To map two fields, click and drag a table field under a primary table field.
3. To add a new unmapped field, click and drag a table field into the upper row of fields.
4. To remove a field from the concatenated table, in the field click ![Cancel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg).
5. To return a removed field back to the table, click in the Fields pane, click ![Drop ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_drop.svg) beside the field.
6. Click Edit mappings to close Edit mappings.

### Selecting the concatenation operator

Do the following:

1. In the Concatenate or join pane, click Select action.
2. Select Concatenate from the list.

### Concatenating tables

Do the following:

- In the Concatenate or join pane, click Apply.

The tables are now concatenated.

## Splitting concatenated tables

In cases where concatenation is no longer needed, such as when Qlik Sense has performed an unwanted automatic concatenation, you can split the concatenated tables into their source tables.

Information note

Splitting a concatenated table will remove any associations the concatenated table had as well as any associations the primary and secondary tables had with each other. If you want to preserve your associations while splitting concatenated tables, click ![Undo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_back_outline.svg) to undo the concatenation instead of splitting the table. You cannot use ![Undo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_back_outline.svg) to undo concatenation after you load data in Data manager.

### Splitting an automatically concatenated table

Do the following:

1. Select the concatenated table.
2. Click ![Split](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_split.svg).
3. Select the tables to split from the concatenated table.
4. Click Split.

The table is now split into its source tables and all fields in the source tables are qualified. Qualified fields are renamed with the table name followed by the field name, separated by a period punctuation mark (the character “.”).

Example:

Table1 and Table2 both contain the fields Field1 and Field2. When you add them in Data manager, they are concatenated to a table called Table1-Table2 with the same fields, Field1 and Field2.

If you split Table1-Table2, the result is two tables:

- Table1 with fields Table1.Field1 and Table1.Field2
- Table2 with fields Table2.Field1 and Table2.Field2

### Splitting a forcibly concatenated table

Do the following:

1. Select the concatenated table.
2. Click ![Split](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_split.svg).

The table is now split into its source tables. All fields in the source tables and their fields have their pre-concatenation names. Splitting a concatenated table only splits one level of concatenation, so that any concatenated tables that were part of the split concatenated table have their own concatenation preserved.

Related learning:

- [What is concatenate?](/lnk/What_is_concatenate)
- [Reload data for analysis](/lnk/Reload_Data_Analysis_QS)
- [Data manager associations, concatenations and joins](/lnk/Data_Manager_Assocs_Concats_Joins_QS)
