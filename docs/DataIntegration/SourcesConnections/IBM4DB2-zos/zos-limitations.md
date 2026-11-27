---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-zos/zos-limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for z/OS"]
---

# Limitations and considerations

You should be aware of the following limitations and considerations when using an IBM DB2 for z/OS source.

- Capturing changes from Catalog Tables is not supported.
- During a task with Full Load and Apply Changes enabled, duplicate keys may be moved to the target. This is because records that were updated and cached during the Full Load stage of the task may have the same timestamp as the original records that were inserted during Full Load. Note that this usually only happens when the time difference between the inserted record and the updated (cached) record is very small (milliseconds).
- The "enableWLB" driver option is not supported. To force the connection to automatically switch to another LPAR in a parallel sysplex (i.e. “failover”), set “enableACR” to “true” and “enableWLB” to “false” in the driver configuration.
- Landing of Views is supported during Full Load only (i.e. CDC is not supported).
- Capturing changes from an environment with mixed RBA entries (6 and 10 byte formats) is not supported.
- Moving data with 4-byte emoji characters is not supported.
- Capture of DDL changes on temporal tables is not supported.
