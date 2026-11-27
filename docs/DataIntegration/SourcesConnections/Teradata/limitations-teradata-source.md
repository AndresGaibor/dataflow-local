---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Teradata/limitations-teradata-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Teradata"]
---

# Limitations and considerations

You should be aware of the following limitations and considerations when using a Teradata source.

The following limitations apply when using a Teradata source with Qlik Talend Cloud Data Integration.

## Change processing limitations

- Replicating data with 4-byte emoji characters is not supported.
- When storing changes in Change Tables, the before-image will not be stored.
- The Start from timestamp run option is not supported.
- If one of the context columns is part of the primary key or unique index, UPDATE and DELETE operations are not supported.
- Context columns cannot be LOB columns.
- DDL operations are not supported when change processing is enabled.
- When inserting a record and then updating the same record, set the task error handling policy so that the No record found for applying an update action is INSERT the missing target record.
