---
title: "SAP ODP Connector user configuration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_ODP_Connectors_Help/Content/Connectors_SAP_ODP/SAP-ODP-user-configuration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP ODP"]
---

# SAP ODP Connector user configuration

A user profile transport is not supplied for the SAP ODP connector. You will need to configure the user authorizations in the SAP system. To use the SAP ODP connector, the following permission are required:

- A SAP user with authorization to monitor and delete delta initializations in transaction ODQMON.
- A SAP user configured with the following authorization settings (as a minimum):

  ### Function modules

  | Authorization object | RFC name | Activity |
  | --- | --- | --- |
  | S\_RFC | RFCPING | 16 |
  |  | RFC\_FUNCTION\_SEARCH | 16 |
  |  | RFC\_GET\_FUNCTION\_INTERFACE | 16 |
  |  | RFC\_METADATA\_GET | 16 |
  |  | RODPS\_REPL\_CONTEXT\_GET\_LIST | 16 |
  |  | RODPS\_REPL\_ODP\_FETCH | 16 |
  |  | RODPS\_REPL\_ODP\_GET\_DETAIL | 16 |
  |  | RODPS\_REPL\_ODP\_GET\_LIST | 16 |
  |  | RODPS\_REPL\_ODP\_OPEN | 16 |
  |  | RODPS\_REPL\_ODP\_READ\_DIRECT | 16 |
  |  | RODPS\_REPL\_ODP\_RESET | 16 |
  |  | SADT\_REST\_RFC\_ENDPOINT | 16 |
  |  | SCSI\_GET\_SYSTEM\_INFO | 16 |
  |  | RFC1 (Only required when replicating from an SLT Replication Server) | 16 |

  ### Data objects

  | Authorization object | Field name | Value | Activity |
  | --- | --- | --- | --- |
  | S\_RS\_ADSO | RSINFOAREA | \* | 23 |
  |  | RSOADSONM | \* |  |
  | S\_RS\_COMP | RSINFOAREA | \* | 23 |
  |  | RSINFOCUBE | \* |  |
  |  | RSZCOMPTP | \* |  |
  |  | RSZCOMPID | \* |  |
  | S\_RS\_COMP1 | RSZCOMPID | \* | 23 |
  |  | RSZCOMPTP | \* |  |
  |  | RSZOWNER | \* |  |
  | S\_RS\_DS | RSDS | \* | 23 |
  |  | RSDSPART | \* |  |
  |  | RSLOGSYS | \* |  |
  | S\_RS\_HCPR | RSINFOAREA | \* | 23 |
  |  | RSHCPR | \* |  |
  |  | RSHCPROBJ | \* |  |
  | S\_RS\_HYBR | RSHYBRPROV | \* | 23 |
  |  | RSHYBROBJ | \* |  |
  | S\_RS\_ICUBE | RSINFOAREA | \* | 23 |
  |  | RSINFOCUBE | \* |  |
  |  | RSICUBEOBJ | \* |  |
  | S\_RS\_IOBJ | RSIOBJ | \* | 23 |
  |  | RSIOBJCAT | \* |  |
  |  | RSIOBJPART | \* |  |
  | S\_RS\_IOMAD | RSINFOAREA | \* | 23 |
  |  | RSAPPLNM | \* |  |
  |  | RSIOBJNM | \* |  |
  | S\_RS\_ISET | RSINFOAREA | \* | 23 |
  |  | RSINFOSET | \* |  |
  |  | RSISETOBJ | \* |  |
  | S\_RS\_MPRO | RSINFOAREA | \* | 23 |
  |  | RSMPRO | \* |  |
  |  | RSMPROOBJ | \* |  |
  | S\_RS\_ODSO | RSINFOAREA | \* | 23 |
  |  | RSODSOBJ | \* |  |
  |  | RSODSPART | \* |  |
  | S\_RS\_ODP\_H | RSODPHNAME | \* | 23 |
  |  | RSODPHPKG | \* |  |
  | S\_RS\_ODSV | RSFBPNAME | \* | 23 |
  |  | RSFBPOBJ | \* |  |
  |  | RSINFOAREA | \* |  |
  | S\_RO\_OSOA | OLTPSOURCE | \* | 23 |
  |  | OSOAAPCO | \* |  |
  |  | OSOAPART | \* |  |

  ### Other

  | Authorization object | Field name | Value | Activity |
  | --- | --- | --- | --- |
  | S\_ADMI\_FCD | S\_ADMI\_FCD | PADM, ST22 |  |
  | S\_ADT\_RES | URI | /sap/bc/adt/\* |  |
  | S\_DEVELOP | OBJTYPE | DEBUG, ST22 | 03 |
  | S\_TCODE | TCD | ST22 |  |
  | S\_BTCH\_ADM | BTCADMIN | Y |  |
  | S\_BTCH\_JOB | JOBACTION | RELE |  |
  |  | JOBGROUP | \* |  |
  | S\_BTCH\_NAM | BTCUNAME | BWREMOTE |  |
  | S\_DMIS (Only required when replicating from an SLT Replication Server) | MBT\_PR\_ARE | SLOP | 03 |
  |  | MBT\_PR\_LEV | PACKAGE |  |
