---
title: "Teradata"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/teradata-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to databases"]
---

# Teradata

Teradata is available as a target only in Qlik Talend Cloud data replication projects. The connection uses the Teradata Parallel Transporter (TPT) API for data loading and ODBC for metadata queries, DDL requests, and information from Teradata error tables.

## Set up the connection

Before you create a replication task, create and test a connection to the Teradata target.

1. In Connections, click Create connection.
2. Select the Teradata target connector.
3. Enter the connection properties described in [Teradata connection properties](#ConnectionProperties).
4. Click Test connection and resolve any reported errors.
5. Save the connection.

## Teradata connection properties

Configure the following properties for the Teradata target connection:

Teradata target connection properties

| Section | Property | Description |
| --- | --- | --- |
| Data target | Data gateway (required) | Select the data gateway that can reach the Teradata server and has the required Teradata client components installed. |
| Connection properties | Teradata server(s) (required) | Enter the Teradata server name or IP address. Ensure that the server is reachable from the selected data gateway. |
| Account properties | User (required) | Enter the Teradata database user name. This is a database credential, not the account string. |
| Password (required) | Enter the password for the Teradata server database user. This is a database credential, not the account string. |
| Account string | Enter the account string that the Teradata database administrator assigned to the user. This is the database server login account and is distinct from the User and Password credentials. |
| Database properties | Enter database name manually | Select this option to enter the database name. |
| Default database (required) | Enter the Teradata database where data is replicated. The database must be accessible to the specified user. |
| Load databases | Click to discover databases available to the specified user. The list depends on successful connectivity and the user's database permissions. |
| Additional connection properties | ODBC properties | Enter additional ODBC connection properties as Name and Value pairs. Confirm property names and values with your Teradata or ODBC administrator. |

## Prerequisites

Prepare the Teradata environment and access required by the connection before you create the target connection.

- Ensure that the Teradata server is installed in your network and reachable from the computer running the selected data gateway.
- Install and configure the Teradata ODBC driver and required Teradata client components on the data gateway. Do not assume that a driver installed on another computer is available to the gateway.
- Ask a Teradata database administrator to create or identify a database user and provide the user's password and account string, when required.

If you are adapting the Teradata target capability to your environment, ask a Teradata database administrator to verify whether the following privileges are required for your task. The grants apply to the target database unless noted otherwise; they are not necessarily the minimum permissions for every Qlik Talend Cloud task:

- `GRANT SELECT ON <database>`
- `GRANT INSERT ON <database>`
- `GRANT DELETE ON <database>`
- `GRANT UPDATE ON <database>`
- `GRANT EXECUTE ON <database>`
- `GRANT EXECUTE FUNCTION ON <database>`
- `GRANT EXECUTE PROCEDURE ON <database>`
- `GRANT CREATE TABLE ON <database>`
- `GRANT DROP TABLE ON <database>`
- `GRANT CREATE VIEW ON <database>`
- `GRANT DROP VIEW ON <database>`
- `GRANT NONTEMPORAL ON <database>`
- `GRANT CHECKPOINT ON <database>`

The database user may also require the following grant for stream processing:

- `GRANT CREATE MACRO ON <database>`

## Provide access to the Teradata database

The user entered in the connection's User property must be registered as a user in the Teradata database. A Teradata database administrator must grant this same user access before you configure the Teradata target connection and database. Use the credentials for this registered user in the connection's User and Password properties.

For the required grants, see the existing grant list in the [prerequisites](#Prerequisites).

## Edit the hosts file

To enable the selected data gateway to access the Teradata database, add the Teradata mapping to the hosts file on the data gateway machine.

1. On the selected data gateway machine, open the Windows or Linux hosts file. The default paths are:
   - Windows: `~:\Windows\System32\drivers\etc\hosts`
   - Linux: `/etc/hosts`
2. Add the Teradata mapping in the following format. Include the `cop1` suffix after the database name:

   `<Teradata Database IP address/hostname> <Teradata Database name>cop1`

   For example: `123.123.123.1 teradatadbonecop1`

   Make sure that the database name in the hosts file matches the Default database connection property.
3. Save the changes.

## Troubleshoot connection errors

If the connection test fails, review the reported error and check the following items before testing the connection again:

- **Gateway or network:** Confirm that the selected data gateway is running and can reach the Teradata server. Check the server name or IP address and any network rules between the gateway and server.
- **Driver or client:** Confirm that the Teradata ODBC driver and required client components are installed and configured on the selected gateway. A driver installed on the local computer is not used by a remote gateway.
- **Credentials or permissions:** Confirm the case-sensitive User and Password, the optional Account string, and the required database grants with a DBA.
- **Database discovery:** If Load databases returns no databases or an error, first test connectivity and then confirm that the user can discover and access the databases. You can enter a known database with Enter database name manually if appropriate.
- **ODBC properties:** Check every Name and Value pair for spelling, supported values, and conflicts with the driver configuration. Remove an optional property that causes the connection test to fail, or ask an ODBC administrator to verify it.

## Data types

The following table describes the default mappings from Qlik Talend Cloud data types to Teradata data types.

Information note

Teradata does not support applying changes to binary data types in Batch optimized apply mode.

Teradata target data type mappings

| Qlik Talend Cloud data type | Teradata data type |
| --- | --- |
| BOOLEAN | BYTEINT |
| BYTES | VARBYTE (size). The maximum size is 640,000 bytes. |
| DATE | DATE |
| TIME | TIME (precision) |
| DATETIME | TIMESTAMP (precision) |
| INT1 | BYTEINT |
| INT2 | SMALLINT |
| INT4 | INTEGER |
| INT8 | BIGINT |
| NUMERIC | If the scale is 0 through 37, NUMERIC (precision, scale). If the scale is 38 or greater, VARCHAR (45). |
| REAL4 | FLOAT. Teradata FLOAT is equivalent to REAL and DOUBLE PRECISION. |
| REAL8 | FLOAT |
| STRING | VARCHAR (size), up to 64,000 bytes. If the subtype is JSON, JSON is used instead. |
| UINT1 | BYTEINT |
| UINT2 | SMALLINT |
| UINT4 | INTEGER |
| UINT8 | BIGINT |
| WSTRING | VARCHAR (size), up to 640,000 bytes. If the subtype is JSON, JSON is used instead. |
| BLOB | VARBYTE(${MAX\_LOB\_SIZE}). MAX\_LOB\_SIZE is the maximum LOB size specified for limited-size LOB processing. |
| CLOB | VARCHAR(${MAX\_LOB\_SIZE}), using a Unicode case-insensitive character set. MAX\_LOB\_SIZE is the maximum LOB size specified for limited-size LOB processing. If the subtype is JSON, JSON is used instead. |
| NCLOB | VARCHAR(${MAX\_LOB\_SIZE}), using a case-insensitive character set. MAX\_LOB\_SIZE is the maximum LOB size specified for limited-size LOB processing. If the subtype is JSON, JSON is used instead. |

Information note

**LOB limitations:** Teradata does not support full LOB data types. The target uses limited-size LOB mappings instead. The total size of a Teradata row cannot exceed 64 KB, so include the sizes of all columns when setting the maximum LOB size.

For CLOB and NCLOB columns, character lengths are multiplied by three by default to support NLS. This can increase the resulting Teradata column and row sizes.

The Teradata PERIOD data type is not supported.

## Limitations and considerations

- The available replication modes are Full load, Apply changes, and Store changes.
- For tasks that use Apply changes or Store changes, DDL operations and automatic schema evolution are not supported. This limitation does not apply to a Full load-only task.
- For Load mode, the target table must be empty and must not have secondary indexes. Select Stream when the task requires ongoing DML processing or concurrent table queries.

## Related information

- [*Creating a replication project*](../Replicating/data-replication-task.htm)
