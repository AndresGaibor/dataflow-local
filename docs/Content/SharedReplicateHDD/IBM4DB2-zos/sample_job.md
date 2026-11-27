---
title: "Sample XMIT files “Receive” job"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/IBM4DB2-zos/sample_job.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for z/OS"]
---

# Sample XMIT files “Receive” job

The following is a sample job for receiving the LOAD and INSTALL libraries.

```
//*******************************************************************
//*                     Sample JCL for receiving                    *
//* IBM DB2 for z/OS connector installation kit   *
//* 1. Add a jobcard                                                *
//* 2. Replace all <xmit-HLQ> with the High Level Qualifier used      *
//*    for receive files                                            *
//* 3. Replace all <r4z-vn-hlq> with the High Level Qualifier chosen  *
//*    for the installation files                                   *
//*******************************************************************
//RCVLOAD  EXEC PGM=IKJEFT01,DYNAMNBR=20
//SYSPRINT DD SYSOUT=*
//SYSTSPRT DD SYSOUT=*
//SYSTSIN DD *
RECEIVE INDSN('<xmit-HLQ>.LOAD.XMIT') NODISPLAY
DATASET('<r4z-vn-hlq>.LOAD')
/*
//RCVINSTL EXEC PGM=IKJEFT01,DYNAMNBR=20
//SYSPRINT DD SYSOUT=*
//SYSTSPRT DD SYSOUT=*
//SYSTSIN DD *
RECEIVE INDSN('<xmit-HLQ>.INSTALL.XMIT') NODISPLAY
DATASET('<r4z-vnd-hlq>.INSTALL')
/*
```
