---
title: "Handling actions resulting in subtype 83"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/IBM4DB2-zos/handling_sub83_utilities.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for z/OS"]
---

# Handling actions resulting in subtype 83

Subtype 83 is a special diagnostic log record. The following topic describes how Data Movement gateway handles actions resulting in subtype 83.

Subtype 83 commands

| Action | How it is Handled by Data Movement gateway |
| --- | --- |
| ALTER TABLE  (With some variations, e.g. ADD COLUMN) | Handled without issue. |
| MODIFY RECOVERY  (With some variations) | Handled without issue. |
| LOAD REPLACE  (All variations) | A warning message will be generated, with the following text (example):  DB2z utility (subtype 83) variation 4 (LOAD REPLACE) at LSN=0000000000123abc0000  Additionally, the table will be suspended if the internal Data Movement gateway parameter "db2LoadOption" is set to "SUSPEND". The default is "IGNORE", in which case a warning message will still be printed. |
| LOAD RESUME YES  (All variations except SHRLEVEL CHANGE) | A warning message will be generated, with the following text (example):  DB2z utility (subtype 83) variation 3 (LOAD RESUME YES) at LSN=0000000000123abc0000  Additionally, the table will be suspended if the internal Replicate parameter "db2LoadOption" is set to "SUSPEND". The default is "IGNORE", in which case a warning message will still be printed. |
| REORG DISCARD  (If any rows are discarded) | A warning message will be generated, with the following text (example):  DB2z utility (subtype 83) variation 5 (REORG DISCARD) at LSN=0000000000123abc0000  Additionally, the table will be suspended if the internal Replicate parameter "db2LoadOption" is set to "SUSPEND". The default is "IGNORE", in which case a warning message will still be printed. |
| CHECK DATA DELETE  (If any rows are deleted) | A warning message will be generated, with the following text (example):  DB2z utility (subtype 83) variation 6 (CHECK DATA DELETE) at LSN=0000000000123abc0000  Additionally, the table will be suspended if the internal Replicate parameter "db2LoadOption" is set to "SUSPEND". The default is "IGNORE", in which case a warning message will still be printed. |
| RECOVER TO POINT IN TIME | A warning message will be generated, with the following text (example):  DB2z utility (subtype 83) variation 7 (RECOVER TO POINT IN TIME) at LSN=0000000000123abc0000  Additionally the table will be suspended if the internal Replicate parameter "db2LoadOption" is set to "SUSPEND". The default is "IGNORE", in which case a warning message will still be printed. |

Information note

It's possible that LOAD RESUME NO, without REPLACE, may also create the subtype 83 log record. In such a case, the warning message shown above would indicate an unknown variation number, with `(UNIDENTIFIED)` as the description. All other actions would be the same as described above.

It is important to note that data loaded by this utility variation will not be captured. Consequently, this utility variation should be avoided.
