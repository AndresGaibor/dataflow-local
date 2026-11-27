---
title: "Importing the transports via TP"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Shared/Import_Transports_via_TP.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP (Application)", "Prerequisites", "Install the Replicate for SAP Client on the SAP machine", "Importing the Replicate transports into the SAP system"]
---

# Importing the transports via TP

1. Log on to the system at the Operating System level as the <sid> adm.
2. Change the directory to /usr/sap/trans
3. Add the transport to the R/3 buffer with the following command:

   # tp ‘addtobuffer SID’
4. Import the transport to the target R/3 system with the following command:

   # tp ‘import SID client=000 U16’

The expected result of the addtobuffer step is a successful return code of `0’.

If problems occur during the addtobuffer step, it is likely there is a problem with the files. They may be missing, in the wrong location, or have incorrect ownership or permissions.

The expected result of the import step is a successful return code of either `0’ or `4’. A return code of `8’, `12’ or `16’ indicates transport failure. Return codes higher than `16’ indicate a major failure within the transport tool. If this occurs, check the present working directory to ensure the correct location. Also, check the files for existence, location, and proper ownership and access.

If problems exist during the import, retry the import step. If problems persist, check the import and activation logs for failure reason. These files are in the /usr/sap/trans/log location and named.R6U (the `?’ stands in as a wildcard).
