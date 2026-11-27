---
title: "Teradata"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Teradata/Teradata-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# Teradata

This section explains how to set up a Teradata source connection. The connection is available in Replication and Pipeline projects. Before you start, fulfill the [*Prerequisites*](teradata-prerequisites-server.htm), confirm the Teradata account access requirements, review the [*Limitations and considerations*](limitations-teradata-source.htm), and see the [*Supported data types*](teradata-data-types-source.htm). For change processing, Teradata requires context columns to identify updates and deletes, and the same restrictions described in the Qlik Replicate user guide apply here.

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the Teradata source connector and then provide the following settings:

### Data source

- Data gateway

  Select a data gateway to connect to the Teradata source.
- Teradata server(s): Enter the host names or IP addresses of the Teradata servers. You can specify multiple servers.

### Account properties

- User name: Enter the user name of a user authorized to access the Teradata Database.
- Password: Enter the password for that Teradata Database user.

### Database properties

- Default database: Specify the default database in one of the following ways:

  - Select Enter database name manually, and then enter the database name in Default database.
  - Click Load databases, and then select an available database.

  Before you configure the connection, add the Teradata database mapping to the hosts file on the gateway machine. For the procedure, see [*Editing the hosts file*](teradata-hosts-file.htm).

### CDC properties

- Context columns: Enter the context columns used for change processing. Context columns cannot be LOB columns and must be selected carefully for update and delete operations. For more information and examples, see [*Teradata change processing*](teradata-change-processing.htm).
- Context columns sorting order: Select Ascending or Descending.
- Check for changes every (seconds): Enter how often to check the source for changes. The default is 10 seconds.
- Update Expression: Enter the expression used to identify update operations.
- Delete Expression: Enter the expression used to identify delete operations.

Information note

Teradata sources do not generate transaction logs that can be read directly for change processing. To enable source change tracking, you must define context columns and use the relevant update and delete expressions. DDL operations are not supported while change processing is enabled.

### Name

The display name for the source connection.
