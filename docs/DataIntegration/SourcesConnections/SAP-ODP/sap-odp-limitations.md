---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-ODP/sap-odp-limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP ODP"]
---

# Limitations and considerations

When using SAP ODP as a source, the following limitations apply:

## Limitations and considerations for all data tasks

- The SAP ODP connector uses the metadata of the ODP node. Consequently, the target tables will be created with these ODP-provided columns.
- Hierarchy objects and columns are not supported.

## Limitations and considerations for replication and landing tasks

- The "Start from timestamp" and "Start from position" options for running tasks are not supported.
- Capture of changes to the source metadata is not supported. In order to replicate changes to the ODP node's metadata, the task must be reloaded.
- The ["Allow unlimited LOB size" and "Optimize handling when LOB size is less than"](../../Replicating/replicating-settings-metadata.htm) LOB handling options are not supported.
