---
title: "Redo log files - access method guidelines"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/Oracle/Redo_Log_Files_Access_Method_Guidelines.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
---

# Redo log files - access method guidelines

The Oracle source connector can be configured to access online and archived Oracle redo log files using either Oracle LogMiner (Oracle’s built-in method) or Log Reader (Qlik Talend Data Integration’s high-speed redo log reader).

Generally, it is recommended to use Log Reader as it is more efficient, faster, and uses less resources.

Log Reader is especially recommended in the following situations:

- The volume of changes in the redo log is more than 30GB/hour
- The volume of changes is between 10GB/hour and 30GB/hour and the changes need to be processed (i.e. moved to the target) as fast as possible.
- There are multiple tasks moving from the same source. Using Oracle LogMiner is less efficient in this case, as it accesses the redo logs via the database, thereby consuming additional database resources.

Both Log Reader and Oracle LogMiner are subject to certain limitations, support different compression methods, and require different access permissions. It is therefore strongly recommended to review the relevant sections before configuring the connector settings. In the end, your decision whether to use Log Reader or Oracle LogMiner may be based on a limitation that exists in one but not the other, the way your data is compressed, or the permissions that you are willing to grant the Qlik Talend Data Integration user.

## Learn more

- [*Limitations and considerations*](OracleDB_source_limitations.htm)
- [*Supported compression methods*](Supported_Compression_Methods.htm)
- [*Required permissions*](OracleDBSource_Security.htm)
