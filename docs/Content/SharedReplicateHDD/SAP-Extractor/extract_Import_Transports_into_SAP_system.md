---
title: "Importing the required transports into the SAP system"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Extractor/extract_Import_Transports_into_SAP_system.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP Extractor", "Prerequisites", "Download the required transports to the SAP Machine"]
---

# Importing the required transports into the SAP system

There are two types of files required to import the ABAP objects into the SAP system: the data-file and the co-file. You also need to import the Qlik SAP connector transports.

## Importing the Data-file

The data-file begins with an "R"

The data-file should be placed in the /usr/sap/trans/datafile system or in the directory of the server where the transports are stored.

- Typically this is a shared directory, but if not, individually place the file into that directory location for all SAP host servers.
- This file must be accessible by all systems where the Data Movement gateway for SAP Extractor is to be installed.
- Set the permissions on the file to `All` for the user, `Read and Execute` for the group, and `Read and Execute` for others.
- The owner of the file should be the `<sid>adm` user of the system to be installed. The group ownership should be `sapsys`.

## Importing the Co-file

The co-file begins with a "K"

The co-file should be placed in the `/usr/sap/trans/cofiles` file system or in the directory of the server where the transports are stored.

- Typically this is a shared directory, but if not, individually place the file into that directory location for all SAP host servers.
- This file must be accessible by all systems where the Data Movement gateway for SAP Extractor is to be installed.
- Set the permissions on the file to `All` for the user, `Read and Execute` for the group, and `Read and Execute` for others.
- The owner of the file should be the `<sid>adm` user of the system to be installed. The group ownership should be `sapsys`.

Once the files are in the correct location, import the transport into the system using either the Operating System level transport tools (TP), or the Transport Management System (TMS) internally within SAP.

## Importing the Qlik SAP connector transports

To import the Qlik SAP connector transports, follow the procedure described in [Importing the SAP transports](/en-US/connectors/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Installation/Importing-the-transports.htm)
