---
title: "Moving nested tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/Oracle/nested_tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
---

# Moving nested tables

Qlik Talend Data Integration supports the moving of Oracle tables containing columns that are nested tables or defined types. To enable this functionality, select the Support nested tables option in the connector settings.

The data task creates the target tables of Oracle nested tables as regular tables without a unique constraint. As you will most likely need join the parent and child tables for meaningful data, it is important to manually create a non-unique index on the NESTED\_TABLE\_ID column in the target child table. The NESTED\_TABLE\_ID column can then be used in the JOIN ON clause, together with the parent column corresponding to the child table name. Additionally, creating such an index will improve performance when the target child table data is updated/deleted by the data task.

It is recommended to [configure the task to stop after Full Load completes](../../../../Sense_Hub/DataIntegration/Replicating/replicating-settings.htm#After). After Full Load completes, manually create non-unique indexes for all the moved child tables on the target, and then resume the task.

If a captured nested table is added to an existing parent table (captured or not captured), the data task will handle it correctly, but the non-unique index for the corresponding target table will not be created. Note that in this case, if the target child table becomes extremely large, performance may be impacted. In such a case, it is recommended to stop the task, create the index, and then resume the task. Before resuming the task, however, we recommend that you create views that will enable the moved tables to be flattened. These views should contain JOIN statements that correspond to your specific flattening needs, as explained in the example below.

## Prerequisites

Make sure that you Move parent tables for all the moved nested tables. Both the parent tables (the tables containing the nested table column) and the child (i.e. nested) tables will be available for selection in Qlik Talend Data Integration.

## Supported nested table types

The following nested table types are supported:

- Data type
- User defined Object

## Limitations

- Only one level of nesting is supported.
- Qlik Talend Data Integration does not verify that both the parent and child table(s) are selected for moving. In other words, it's possible to select a parent table without a child and vice versa.

## How nested tables are moved

The parent and nested tables are moved to the target as follows:

- The parent table is created on the target similar to the source, where each nested column is defined as RAW(16). In each parent table row, this column will contain the same value as the corresponding child table nested rows in the NESTED\_TABLE\_ID column.
- The child table is created identical to the source, but with an additional NESTED\_TABLE\_ID column, as mentioned earlier.

## JOIN statement example

Let's assume that the following definitions exist in the Oracle source:

- CREATE OR REPLACE TYPE my\_tab\_t AS TABLE OF VARCHAR2(30);
- CREATE TABLE my\_parent\_table (id NUMBER PRIMARY KEY, col1 my\_tab\_t) NESTED TABLE col1 STORE AS col1\_tab;

In this case, the data task will usually create two target tables, like this:

- CREATE TABLE my\_parent\_table (id NUMBER PRIMARY KEY, col1 RAW(16));
- CREATE TABLE col1\_tab(nested\_table\_id RAW(16), column\_value VARCHAR2(30));

The JOIN statement for flattening the two target tables could be defined as follows:

- Select id, column\_value from my\_parent\_table LEFT OUTER JOIN col1\_tab child ON child.nested\_table\_id = parent.col1;

Information noteLEFT OUTER JOIN should be used if the parent tables contains records that do not exist in the child table.
