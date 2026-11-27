---
title: "Program authorization groups"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Configuration/Program-authorization-groups.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connector configuration"]
---

# Program authorization groups

Authorization groups secure your tables and programs. The SAP system ensures that users can only access data which they are authorized to access.

Do the following:

1. Use a role that contains the Authorization Object S\_PROGRAM.
2. Update the field P\_GROUP (replace the ‘\*’) in the Authorization Object with the program authorization groups that contain the correct programs.
3. Assign the role to the QlikSAP user.

   Now the user can only execute the programs that are part of the allowed program authorization groups.

This is only valid for executable program types.

Program authorization group for Qlik:

- ZQLIKPGM

Programs assigned to ZQLIKPGM:

- /QTQVC/DELETE\_TABLES
- /QTQVC/PROCESS\_STATUS
- /QTQVC/READ\_DATA
- /QTQVC/READ\_MPDATA
- /QTQVC/UPDATE\_MIGRATION
- /QTQVC/UPLOAD\_EXTRACTOR
