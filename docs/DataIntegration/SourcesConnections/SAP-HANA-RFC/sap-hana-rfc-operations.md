---
title: "Monitor and operate CDC"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA-RFC/sap-hana-rfc-operations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA RFC"]
---

# Monitor and operate CDC

Monitor the data task in Qlik Talend Data Integration and use the SAP HANA RFC Endpoint Cockpit to investigate source capture and subscriptions.

## Monitor SAP subscriptions

1. Run transaction /QTQVC/HRFC\_COCKPIT in SAP.
2. Double-click a registered table or click Details.
3. Review Subscriptions, Jobs overview, Change Capture Index, and Diagnostics.

Subscription fields in SAP

| Field | Description |
| --- | --- |
| SUBSCRIBER\_ID | Identifier for a subscriber to the table. |
| INIT\_STREAM\_TS | Timestamp when the subscription started streaming. |
| LAST\_CONSUMED\_TS | Last point through which changes have been consumed and acknowledged. |
| PACKAGE\_SI | Configured subscription package size. |
| CDC\_STATUS | ACTIVE while polling; PAUSED when nothing has consumed changes recently. |

## Monitor retention and storage

All subscribers to a table share one changelog. Changes can be removed only after all subscribers acknowledge them and the retention period elapses. A stopped or lagging subscriber can prevent cleanup for other data tasks reading the same table.

Check whether LAST\_CONSUMED\_TS advances. Before removing a subscription in SAP, confirm that no active data task still uses it. Do not assume deleting a Cloud data task has removed its SAP subscription; check for unused subscriptions with your SAP admin.

## Investigate capture failures

- Authorization failure: Check the connection user's permissions for every selected table. See [*Required permissions*](sap-hana-rfc-permissions.htm).
- Table requires a reload: SAP detected a resynchronization condition. Coordinate a new baseline with your SAP admin before restarting capture.
- Inactive table: Check the table's registration, enabled state, subscriptions, and capture jobs in the cockpit.
- Polling or retention warning: Compare the connection values with SAP's table and global limits. A value adjusted to the SAP limit does not by itself stop capture.
- Timeout or dropped connection: Check connectivity from the Data Movement gateway to SAP, the data task log, and the SAP job log in SM37.

## Restart change processing

Use the run and recovery controls available for your Cloud data task, rather than the Replicate console commands. For replication tasks, see [*Advanced run options*](../../Replicating/replicating_advanced_run.htm). Available recovery options depend on the source, target, and task mode.

A timestamp or checkpoint restart cannot replace a required source rebaseline. If SAP reports a reload requirement after a table change, establish a new baseline before processing further changes.
