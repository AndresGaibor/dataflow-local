---
title: "Working with Change Tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/use_change_table_model.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating a replication project", "Using Change Tables"]
---

# Working with Change Tables

In addition to replicating changes from source endpoint tables to corresponding tables in a target endpoint, you can also replicate changes to corresponding Change Tables in the target endpoint. This process occurs simultaneously when applying changes to the target tables. You can choose whether to replicate the changes to the target only, store changes in the Change Tables, or both. See [*Using the Change Table model*](#ar_chg_tbls_3080803564_ciheeejg) below for more information.

Information note

UPDATEs applied to the source *that do not* change the source data will be applied to the target but will not be applied to the corresponding Change Table. For example, if an UPDATE operation on Column A in the source changes all values greater than 10 to 1, and one of the records in Column A is *already* 1, then the UPDATE for that record will not be written to the Change Table.

The Change Tables have the same names as the tables that are being replicated, but are appended with a `__ct` suffix.

In addition to the selected columns from the source table, the Change Table also includes special header columns that provide more information on the change the row represents such as the operation, the transaction and the timestamp. This lets you use SQL Query Language to carry out various analysis of the change events, such as fraud detection, trend analysis, triggering of business processes, and Disaster Recovery. For more information about reading the Change Tables, see Reading the Change Tables.

## Handling truncate operations

TRUNCATE operations will *not* truncate the Change Table. Instead, an additional record will be added to the table with `operation=TRUNCATE.`

Regarding the actual target table, if both the Apply Changes *and* Store Changes replication options are enabled, the target table will be truncated.

To apply TRUNCATE operations to both the Change Table and the Target Table (for sources that support TRUNCATE):

1. In the task settings' Store Changes Settings tab, make sure that Apply to Change Table (the default) is selected from the DDL options drop-down list.
2. In the task settings' Apply Changes Settings tab, make sure that TRUNCATE target table (the default) is selected from the When source table is truncated drop-down list.

## Using the Change Table model

When you work with Change Tables you can determine whether to store the changes in the Change Tables, apply the changes to the target tables, or both store and apply the changes. You determine this when you define the replication task. For more information on this setting, see Store Changes Settings.

In cases where you are both applying and storing the changes, the following is true:

- The target and Change Tables must be in the same endpoint, although they can have different schemas. For example, the Change Tables will contain the metadata headers.

  For further details about changing the schema, see Rename Change Table Schema.
- Changes applied to the Change Table will be handled exactly the same as the changes performed in the corresponding transaction in the source database. Therefore, when using Transactional apply mode or Batch optimized apply mode with the Preserve transaction consistency option selected, the changes will be processed as a single transaction.

  The exception to this is when an error is encountered and the data task switches to "one-by-one" apply mode in order to determine which of the Change operations is responsible for the error.
- The same data columns are both applied and stored with the exception of the change header columns, which are only added to the stored Change Tables.
