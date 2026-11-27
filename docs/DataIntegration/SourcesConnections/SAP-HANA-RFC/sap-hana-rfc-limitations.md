---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA-RFC/sap-hana-rfc-limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA RFC"]
---

# Limitations and considerations

The SAP HANA RFC source detects changes by comparing snapshots on the SAP system. It does not provide a history of every transaction between capture cycles.

## Changes between capture cycles

The SAP add-on compares table keys and HANA row IDs. An unchanged row ID indicates no change. A higher row ID indicates an update. A missing key indicates a delete, and a new key indicates an insert. The add-on reads the full row for inserts and updates and stores the changes in the table's changelog.

Net changes for one primary key

| Operations during one capture interval | Captured change |
| --- | --- |
| Insert, then update | Insert |
| Insert, then delete | No change |
| Multiple updates | Update with the last image |
| Update, then delete | Delete |
| Delete, then insert with the same key | Update |

## Source restrictions

- Only S/4HANA and ECC on HANA with SAP\_ABAP component 750 or greater are supported.
- Only registered and enabled HANA column-store tables with a key defined in the ABAP Dictionary (DDIC) are available.
- Row-store tables and SAP S/4HANA Public Cloud systems are not supported.
- The source does not support CDS views or extractors. It does not use ODP, database triggers, or database logs.
- Captured timestamps identify when changes were detected, not the original transaction time. The user who made the change is not available.
- HANA multi-node redistribution can reassign row IDs and produce captured updates even when row values have not changed.

## Changes requiring a new baseline

If a row ID moves backwards, the SAP add-on suspends capture for that table and requires a reload. This can occur after repartitioning, restructuring, or truncating a table. A source DDL change also requires a full rebaseline.

Coordinate source schema and table maintenance with your SAP admin. Check the table status in the SAP HANA RFC Endpoint Cockpit before restarting a data task.
