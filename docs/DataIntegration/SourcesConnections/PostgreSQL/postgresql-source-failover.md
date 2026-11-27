---
title: "Setting up failover"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/postgresql-source-failover.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "PostgreSQL"]
---

# Setting up failover

Information note

- The procedures described in this topic should be performed by your PostgreSQL DBA.
- Requires Data Movement gateway 2024.11.14 or later

This topic explains how to set up PostgreSQL and Data Movement gateway to support a failover scenario. The procedure you need to perform depends on your specific PostgreSQL failover setup.

If the database object ID for the primary and secondary database remains the same after a failover (which is usually the case), you only need to update the hosts file on the Data Movement gateway machine with the secondary database server's IP address. However, if the database object ID of the secondary database is not the same as the primary database after a failover, additional configuration is required. It's usually not possible to know beforehand whether the object ID will change, but if you do know, perform the Setting up failover when the object ID for the primary and secondary database is different procedure described below. If you do not know whether the object ID will change, we recommend performing the simpler procedure described in Setting up failover when the object ID for the primary and secondary database is the same, as the object ID will usually remain the same after a failover.

If you performed the simpler setup and Data Movement gateway fails to recover during failover, then you will need to perform the Setting up failover when the object ID for the primary and secondary database is different procedure.

Information noteWhile the Setting up failover when the object ID for the primary and secondary database is the same procedure is supported with both Replication projects and landing tasks in Data pipeline projects , the Setting up failover when the object ID for the primary and secondary database is different procedure is supported with Replication projects only.

## Setting up failover when the object ID of the primary and secondary database is the same

When a failover occurs, the data task will encounter a recoverable error and will try to reconnect to the IP address of the primary database server. However, it will usually not succeed as the secondary database server will (almost always) have a different IP address.

If the switch of IP addresses is not handled by a DNS failover service, you will need to specify the new IP address in the hosts file on the Data Movement gateway machine. The path to the hosts file is /etc/hosts. After the hosts file has been updated, the data task will resume automatically.

## Setting up failover when the object ID of the primary and secondary database is different

Information noteSupported with Replication projects only.

In standard operation, the data task creates a slot automatically when moving data from a PostgreSQL source. The slot names contain the object ID of the database in its name. In rare cases, the object ID of the primary and secondary databases will be different. In such a case, the data task will fail during a failover as it will not be able to find the slot it created for the primary database in the secondary database. In this case, the following error will occur:

[SOURCE\_CAPTURE ]E: Can't resume task after replication slot was dropped. [1020101] (postgres\_endpoint\_capture.c:445)

If you encounter such an error, do the following:

1. In the connector settings Internal properties section, add the internal property slotName and set the slot name value.

   The specified slotName must already exist in the primary PostgreSQL server. You can either create a new slot or use an existing slot.

   To create a new slot and retrieve its LSN, run the following query:

   SELECT lsn FROM pg\_create\_logical\_replication\_slot ('user\_provided\_slot\_name', 'test\_decoding');

   For a list of available slots and their LSNs, run the following query:

   SELECT slot\_name, restart\_lsn FROM pg\_replication\_slots WHERE slot\_type = 'logical';
2. Enter the LSN for the specified slotName in the Advanced run options dialog's Source change position field and then prepare and start the data task.

   If a failover occurs, the secondary server will take over almost immediately and become the primary server. The failover should be handled by pg\_failover\_slots extension.
3. When a failover occurs, the data task will encounter a recoverable error and will try to reconnect to the IP address of the primary database server. However, it will usually not succeed as the secondary database server will (almost always) have a different IP address.If the switch of IP addresses is not handled by a DNS failover service, you will need to specify the new IP address in the hosts file on the Data Movement gateway machine. The path to the hosts file is /etc/hosts. After the hosts file has been updated, the data task will resume automatically.
