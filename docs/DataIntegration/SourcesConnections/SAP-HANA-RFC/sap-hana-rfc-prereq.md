---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA-RFC/sap-hana-rfc-prereq.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA RFC"]
---

# Prerequisites

Prepare the SAP system, the tables to capture, and the Data Movement gateway before creating the SAP HANA RFC connection.

## Prepare the SAP system

- Install the Qlik-delivered ABAP package in its registered SAP namespace.
- Have an SAP admin account that can register tables and set global capture configuration.
- Prepare the SAP credentials used by the connection.
- Identify the tables to capture. Only tables explicitly registered and enabled by an SAP admin appear in the source.
- Use HANA column-store tables with at least one key field defined in the ABAP Dictionary (DDIC). Registration is rejected if a table has no DDIC key.

Information note

Row-store tables and SAP S/4HANA Public Cloud systems are not supported. CDS views and extractors are also out of scope.

Some core tables, such as ACDOCA, define their key in DDIC but not as a HANA database constraint. The endpoint checks the DDIC key. For other source restrictions, see [*Limitations and considerations*](sap-hana-rfc-limitations.htm).

## Install the SAP add-on

Download the SAP HANA RFC endpoint SAR file from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads). An SAP admin installs this package on the SAP system, not on the Data Movement gateway.

1. Log on to SAP client 000 and run transaction SAINT.
2. Click Installation Package > Load Packages > SAR Archive from Frontend. Select the downloaded SAR file and click Open.
3. Confirm that SAPK-100COINQTQVC is loaded. Select QTQVC HANA RFC Endpoint and click Continue.
4. Review the calculated package, SAPK-1##COINQTQVC. Leave optional target support package fields empty unless the package instructions require a value. Click Continue.
5. Review the component, release, and prerequisites shown by SAINT, then click Continue.
6. When asked whether modification adjustment transports are required, click No.
7. Open Start Options, select Start in background immediately, and confirm to start the import.
8. Follow the SAINT phases. If a phase stops, review its logs, fix the cause, and click Continue. Monitor background job OCS\_QUEUE\_IMPORT in SM37.
9. After a successful import, review the logs, click Finish, and verify QTQVC release 1## in the installed add-ons list.

## Install the RFC driver on the gateway

The connection uses the SAP NetWeaver RFC SDK. SAP distributes the SDK through the SAP Support Portal; Qlik does not bundle it. For the gateway, install the SDK through the shared driver setup facility instead of copying libraries into a system directory.

1. Download the SAP NetWeaver RFC SDK package that matches the manifest, for example nwrfc750P\_19-\*.zip, from the SAP Support Portal.
2. Copy the SDK zip file to /opt/qlik/gateway/movement/drivers/saphanarfc.
3. Copy saphanarfc.yaml to /opt/qlik/gateway/movement/drivers/manifests.
4. Run the installer and accept the license: sudo /opt/qlik/gateway/movement/drivers/bin/install saphanarfc -a.

The installer copies the SDK libraries into the gateway library path and updates drivers/bin/drivers\_login.sh. A manual LD\_LIBRARY\_PATH configuration is not required.

To remove the driver, run sudo /opt/qlik/gateway/movement/drivers/bin/uninstall saphanarfc.

## Authorize the SAP user

Configure the connection user's SAP authorization and the SAP admin's cockpit access before running a data task. See [*Required permissions*](sap-hana-rfc-permissions.htm).
