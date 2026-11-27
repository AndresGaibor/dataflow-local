---
title: "Required permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/security-req-mysql-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "MySQL"]
---

# Required permissions

The user specified in the connection settings must have the following permissions:

## Full Load tasks

The ReplicationAdmin role with the SELECT privilege for the designated source tables.

## CDC tasks

The ReplicationAdmin role with the REPLICATION CLIENT and REPLICATION SLAVE privileges.

Information noteWhen capturing changes from Microsoft Azure Database for MySQL 8.0, the user must also have Standard authentication.

### Checking for open XA transactions

When the task is initialized, Data Movement gateway checks whether there are any open XA transactions (transactions that use a two phase commit protocol). To allow this query to be performed, the following permission needs to be granted:

grant XA\_RECOVER\_ADMIN on \*.\* to 'userName'@'%';

Where userName is the user specified in the connector settings.

If this permission is not granted, the following error will be shown when you run the task:

Failed to check for open XA transactions. Verify that the user specified in the endpoint settings has the XA\_RECOVER\_ADMIN permission. Capturing changes while there are open XA transactions might lead to loss of data. If there are no XA transactions in this database, add the internal parameter IgnoreOpenXaTransactionsCheck to skip the XA transactions check.
