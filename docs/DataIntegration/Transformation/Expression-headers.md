---
title: "Expression headers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Expression-headers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Managing datasets", "Building expressions"]
---

# Expression headers

Use headers in column expressions to retain change metadata, such as an operation name or source stream position.

The `Q_H_` headers are available in SaaS-managed landing, lake landing, and replication tasks. Insert a header from the editor's Headers list when [*Building expressions*](Building-expressions.htm). The table below identifies source endpoint applicability and values during full load and change processing.

## Headers for all source endpoints

General headers and processing-phase values

| Header and data type | Value during change processing | Value during full load |
| --- | --- | --- |
| `Q_H_CHANGE_SEQ` `STRING(50)` | Monotonically increasing change sequence across the task's change tables. Combines a timestamp with a zero-prefixed change counter to order changes within a task. | Empty. |
| `Q_H_STREAM_POSITION` `STRING(50)` | Position in the source change stream, usually an SCN or LSN. Identifies a source stream location, not a timestamp or a sequence comparable across tasks. | Empty string. |
| `Q_H_TIMESTAMP` `DATETIME(0)` | Timestamp of the change operation. This is an operation timestamp, not the transaction commit timestamp. | Current timestamp. |
| `Q_H_TRANSACTION_ID` `STRING(50)` | Transaction containing the change, represented as a hexadecimal 128-bit transaction ID. The ID is not guaranteed to be unique. | Empty. |
| `Q_H_COMMIT_TIMESTAMP` `DATETIME(0)` | Source transaction commit timestamp, as represented by the processing runtime. Distinct from the source database-server time in `Q_H_DB_COMMIT_TIMESTAMP`. | Current timestamp. |
| `Q_H_DB_COMMIT_TIMESTAMP` `DATETIME(0)` | Source transaction commit timestamp according to the source database server's time. | NULL. |
| `Q_H_OPERATION` `STRING(50)` | `INSERT`, `UPDATE`, or `DELETE`. | `INSERT`. |

The change sequence combines a timestamp formatted as `YYYYMMDDHHmmSShh` with a 19-digit, zero-prefixed change counter. The timestamp fields are year, month, day, hour, minute, second, and hundredths of a second. The timestamp portion can repeat while the counter increases. The declared `STRING(50)` capacity is not the length of the sequence format.

Do not rely on `Q_H_TRANSACTION_ID` as a unique key. Use `Q_H_CHANGE_SEQ` for task-level change ordering rather than comparing timestamps alone.

## Source-specific headers

The following source restrictions apply to the named endpoints. They do not imply support for other SQL Server variants or other file sources.

Source-specific headers and processing-phase values

| Header and data type | Source endpoints | Value during change processing | Value during full load |
| --- | --- | --- | --- |
| `Q_H_USER` `STRING(50)` | Microsoft SQL Server; Microsoft Azure SQL Managed Instance; Amazon RDS for SQL Server; IBM Informix; IBM DB2 for z/OS; IBM DB2 for LUW; Oracle; File; SAP Sybase ASE. | User who made the source change. | Empty. |
| `Q_H_JOB_NAME` `STRING(50)` | IBM DB2 for iSeries only. | Job that made the source change. | Empty. |
| `Q_H_PROGRAM_NAME` `STRING(50)` | IBM DB2 for iSeries only. | Program that made the source change. | Empty. |
| `Q_H_XACT_ID` `STRING(50)` | Microsoft SQL Server; Microsoft Azure SQL Managed Instance; Amazon RDS for SQL Server. | Transaction-time identifier: the LSN of the first record for the server's last distributed transaction. All records in the transaction share this ID. This differs from `Q_H_TRANSACTION_ID`, which is obtained from the physical transaction log. | Empty. |

## Using operation metadata

Add a column and insert `Q_H_OPERATION` to record the source operation. During full load, its value is `INSERT`. During change processing, an update has the value `UPDATE`.

The operation header describes the operation; it does not change target deletion handling. To return custom flags for source operations, see `$OPERATION_INDICATOR` in [*Expression functions*](Expression-functions.htm).

## Streaming landing header columns

Streaming Transform tasks use source columns such as `hdr__kafka_partition`, `hdr__kinesis_offset`, or `hdr__file_name`. These are not aliases for the `Q_H_` headers. Select streaming landing headers from Columns. For the source-specific lists, see [*Landing tables*](../Lakehouse/lakehouse-datasets-architecture-streaming.htm#Landing).
