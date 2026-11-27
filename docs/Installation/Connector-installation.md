---
title: "SAP Connectors installation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Installation/Connector-installation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver"]
---

# SAP Connectors installation

Qlik connectors that are used with SAP NetWeaver on Qlik Cloud are installed and updated automatically. However, the transports are not and need to be installed on the SAP system. If you are using Qlik Data Gateway - Direct Access, SAP NetWeaver RFC SDK needs to be made available on the Qlik Data Gateway - Direct Access machine. For more information, see [*Installing SAP NetWeaver RFC SDK for Qlik Data Gateway - Direct Access*](Installing-sap-connectors-for-direct-access-gw.htm).

Information noteThe SAP NetWeaver connector is not available on Qlik Sense Business.

## Objects, roles, and transports

When extracting data, the connectors use Qlik objects in the SAP system to communicate with the client. These objects are stored in:

- /QTQVC/QTDEV\_BW for the BW connector
- /QTQVC/QTDEV for all others

All objects are unique and prefixed with the reserved name space /QTQVC/. After the objects have been imported in an SAP system, it is possible to import a deletion transport to remove them.

The SAP user ID needs to have a role assigned that includes authorization objects. The provided roles contain the necessary authorization objects, and can be checked by Qlik objects and by standard SAP objects. Using the provided roles is not mandatory. Roles can be copied or modified, and custom roles containing the necessary authorization objects can be used instead.

Objects (such as ABAP programs, function modules, and dictionary objects) are distributed using data extraction transports, and roles are distributed using user profile transports. The transports are imported into the SAP system using the SAP transport management system.

## License when using SAP NetWeaver with Qlik Data Gateway - Direct Access

To use SAP NetWeaver with Qlik Data Gateway - Direct Access, an additional license is required, but does not need to be installed.

For more information on Qlik Data Gateway - Direct Access, see [Setting up Qlik Data Gateway - Direct Access](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm).

## What you need to install

1. [*Installing SAP NetWeaver RFC SDK for Qlik Data Gateway - Direct Access*](Installing-sap-connectors-for-direct-access-gw.htm)
2. [*Installing the SAP transports*](Installing-the-transports-qcs.htm)
3. [*Importing the SAP transports*](Importing-the-transports.htm)
4. [*Installing and updating the license*](License_installation_update.htm)
