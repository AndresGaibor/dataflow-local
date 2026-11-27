---
title: "Supported standby configurations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/Oracle/supported_standby_configuraitons.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
---

# Supported standby configurations

The following table lists the supported Oracle Standby configurations.

Supported configurations

| Standby Configuration | Supported | Notes |
| --- | --- | --- |
| Snapshot Standby | Yes | - |
| Physical Standby | Yes | - The Physical Standby database must have Active Data Guard enabled (available from Oracle 11g or later). - When the Oracle LOG\_ARCHIVE\_DEST\_n initialization parameter is configured with the DELAY option, running a Full Load and Apply Changes task on an Oracle Physical Standby instance may result in missing or erroneous data in the target database.  This happens because Qlik Talend Data Integration interprets the timestamp of changes in the Redo log as the timestamp of the Oracle instance from where it performed the Full Load, whereas it is in fact the timestamp of the Oracle instance *where the changes occurred* (i.e. the Primary Oracle instance). The resulting timestamp discrepancy means that some of the changes in the Redo log may be interpreted as “old” and not be moved.  This issue can be resolved using an internal parameter. For information on this parameter, please contact Qlik Support. - Oracle Physical Standby only supports an Oracle Primary RAC instance where all nodes are open (available). In other words, an Oracle Primary RAC instance where some nodes are available and some are not is not supported. |
| Logical Standby | No | - |
| Hot Standby | No | - |
