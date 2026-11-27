---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-HANA/limitations_saphana_source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA (Database)"]
---

# Limitations and considerations

The following limitations apply when using SAP HANA as a source.

## Limitations and considerations for all tasks

- Change Processing is not supported with SAP BW tables.
- Compatibility views are not supported and will not be available for selection.
- CA views are not supported and will not be available for selection.
- Row store data storage is not supported.
- Multitenant architecture is only supported on a single host.
- Only transparent tables (including SAP S/4HANA transparent tables) are supported.

## Limitations and considerations for replication and landing data tasks

The following limitations only apply when the Record mode in the connector settings is set to Primary key only:

- Soft DELETE operations are not supported and will not be captured.
- The Apply Conflicts error handling policy must be set to the following:

  No record found for applying an UPDATE: INSERT the missing target record
- For replication tasks, the Store Changes replication mode is not supported.
- For replication tasks, the Start from timestamp method of resuming a task is not supported.
- For replication tasks configured with the Apply Changes moving option, transformation filters are only supported with Primary Key columns.

The following limitations apply to both replication tasks and landing tasks:

- Changes to a table's Primary Key will not be replicated to the target.
- DDL operations are not supported.
- Latency when applying changes
- The latency shown in the User Interface is the interval between Data Movement gateway capturing a change from the source (as opposed to the source commit time), and that change existing on the target.

### Unsupported data types

The following data types are not supported:

- ARRAY
- ST\_GEOMETRY
- ST\_POINT
