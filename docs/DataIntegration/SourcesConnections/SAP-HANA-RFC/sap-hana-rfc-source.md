---
title: "SAP HANA RFC"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA-RFC/sap-hana-rfc-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources"]
---

# SAP HANA RFC

Use the SAP HANA RFC source to capture inserts, updates, and deletes from registered SAP HANA column-store tables. The endpoint compares snapshots on the SAP system and sends changes to Qlik Talend Data Integration over RFC through the SAP application server.

## Before you start

Install the SAP-side package, register the tables, and install the SAP NetWeaver RFC SDK on the Data Movement gateway. For details, see [*Prerequisites*](sap-hana-rfc-prereq.htm) and [*SAP Application setup*](sap-hana-rfc-sap-setup.htm).

In this section:

- [*Prerequisites*](sap-hana-rfc-prereq.htm)
- [*Required permissions*](sap-hana-rfc-permissions.htm)
- [*SAP Application setup*](sap-hana-rfc-sap-setup.htm)
- [*Schedule and manage capture jobs*](sap-hana-rfc-scheduling.htm)
- [*Limitations and considerations*](sap-hana-rfc-limitations.htm)
- [*Monitor and operate CDC*](sap-hana-rfc-operations.htm)
- [*Source data types*](sap-hana-rfc-data-types.htm)

## Create a connection

1. In Create connection, select SAP HANA RFC.
2. On the General tab, set Connection mode to Connect to a specific SAP SERVER and enter the following information:

   - Server Name: The SAP application server name or address.
   - Instance number: The SAP instance number.
   - Client: The SAP client number.
   - Username and Password: Credentials for the SAP user.

   If required by your SAP landscape, configure Secure Network Communication (SNC). Click Test Connection before you save the connection.
3. On the Advanced tab, configure the following properties:

   - Maximum package records size: The maximum number of rows fetched in each batch. Range: 0 to 1,000,000.
   - Retrieve changes every (min): How often the pipeline polls SAP for changes. Range: 5 to 2,880 minutes.
   - Retention time every (hrs): How long SAP retains acknowledged changes. Range: 24 to 84 hours.

   SAP enforces the registered table's minimum polling interval and maximum retention. If a requested value exceeds those limits, SAP applies the limit and the pipeline logs a warning.

## Use the source in a data task

Only tables that an SAP admin has registered and enabled for change capture appear in the table selector. A data task performs a full load, then transitions to CDC.

Information note

Snapshot-based change capture reports the net change for each primary key during a polling interval. For example, an insert followed by a delete within one interval produces no change record.

For replication tasks, configure Apply conflicts to update the existing target record for a duplicate-key INSERT and ignore a missing record for an UPDATE or DELETE. This handles repeated change delivery and full-load/CDC overlap. See [*Apply conflicts*](../../Replicating/replicating-settings.htm#Apply2). Other data task types have different settings; do not assume the replication-task controls are available.

For source capture restrictions and baseline requirements, see [*Limitations and considerations*](sap-hana-rfc-limitations.htm). For SAP-side troubleshooting, see [*Monitor and operate CDC*](sap-hana-rfc-operations.htm).
