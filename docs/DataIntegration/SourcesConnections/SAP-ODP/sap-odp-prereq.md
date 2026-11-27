---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-ODP/sap-odp-prereq.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP ODP"]
---

# Prerequisites

The following section describes the prerequisites for working with the SAP ODP source connector.

Before you can land or replicate data, make sure to complete the following prerequisites:

- Install the required SAP Java Connector on the Data Movement gateway server

  Information note

  This is only required if you opted to work with Data Movement gateway. For information on the benefits of Data Movement gateway and when it is required, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Grant the required permissions on the data source
- Configure the data source connector

## ODP API

The SAP ODP endpoint uses ODP API 2.0 which is available from the following SAP basis levels and above:

- PI\_BASIS 730 SP 14 (part of SAP NetWeaver 7.30 SP 14)
- PI\_BASIS 731 SP 16 (part of SAP NetWeaver 7.03 SP 16 and 7.31 SP 16)
- PI\_BASIS 740 SP 11 (part of SAP NetWeaver 7.40 SP 11)
- SAP\_BW 750 SP 0 (incl. former PI\_BASIS packages)

Information noteSAP\_BASIS and PI\_BASIS are interchangeable. In newer systems, the component name is SAP\_BASIS.

For more information, see SAP Note 1931427.

For information on how to release extractors so that they are available for the ODP API, see SAP Note 2232584.

## Driver setup

You can install the driver using the driver installation utility (recommended) or manually. Manual installation should only be attempted in the unlikely event that you encounter an issue with the driver installation utility.

### Using the driver installation utility to install the driver

This section describes how to install the required SAP Java Connector. The process involves running a script that will automatically download, install and configure the required SAP Java Connector. You can also run scripts to update and uninstall the SAP Java Connector as needed.

### Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version
- Download SAP Java Connector <version> "sapjco<version>.zip" from the SAP Support Portal. You can find the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/sapodp.yaml. Once the download completes, copy the file to:

  /opt/qlik/gateway/movement/drivers/sapodp

### Installing the SAP Java Connector

To download and install the SAP Java Connector:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
3. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
4. Run the following command:

   Syntax:

   ./install sapodp

   If the SAP Java Connector cannot be downloaded (due to access restrictions or technical issues), a message will be displayed instructing you where to download the SAP Java Connector and where to copy it on the Data Movement gateway machine. Once you have done that, run the install sapodp command again.

   Otherwise, the EULA for the SAP Java Connector will be displayed.
5. Do one of the following:

   - Press [Enter] repeatedly to slowly scroll through the EULA.
   - Press the Spacebar repeatedly to quickly scroll through the EULA.
   - Press q to quit the license text and be presented with the EULA acceptance options.
6. Do one of the following:

   - Type "y" and press [Enter] to accept the EULA and begin the installation.
   - Type "n" and press [Enter] to reject the EULA and exit the installation.
   - Type "v" and press [Enter] to view the EULA again.

The SAP Java Connector will be installed.

7. Wait for the installation to complete (indicated by "Complete!") and then start the Data Movement gateway service:

   sudo systemctl start repagent
8. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Updating the SAP Java Connector

Run the update command if you want to uninstall previous versions of the SAP Java Connector before installing the provided SAP Java Connector.

To download and update the SAP Java Connector:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
3. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
4. Run the following command:

   Syntax:

   ./update sapodp

   If the SAP Java Connector cannot be downloaded (due to access restrictions or technical issues), a message will displayed instructing you where to download the SAP Java Connector and where to copy it on the Data Movement gateway machine. Once you have done that, run the update sapodp command again.

   Otherwise, the EULA for the SAP Java Connector will be displayed.
5. Do one of the following:

   - Press [Enter] repeatedly to slowly scroll through the EULA .
   - Press the Spacebar repeatedly to quickly scroll through the EULA.
   - Press q to quit the license text and be presented with the EULA acceptance options.
6. Do one of the following:

   - Type "y" and press [Enter] to accept the EULA and begin the installation.
   - Type "n" and press [Enter] to reject the EULA and exit the installation.
   - Type "v" and press [Enter] to review the EULA from the beginning.

The old SAP Java Connector will be uninstalled and the new SAP Java Connector will be installed.

7. Wait for the installation to complete (indicated by "Complete!") and then start the Data Movement gateway service:

   sudo systemctl start repagent
8. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Uninstalling the SAP Java Connector

Run the uninstall command if you want to uninstall the SAP Java Connector.

To uninstall the SAP Java Connector:

1. Stop all tasks configured to use this connector.
2. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
3. Run the following command:

   Syntax:

   ./uninstall sapodp

   The SAP Java Connector will be uninstalled.

### Installing the driver manually

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

Download the SAP Java Connector 3.x (64-bit) for Linux from <https://support.sap.com/en/product/connectors/jco.html>.

Then,
open a shell prompt and do the following:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
3. Change the working directory to opt/qlik/gateway/movement/bin and run the following command:

   source arep\_login.sh

   This will set the Data Movement gateway installation path.
4. Unzip the file you downloaded to a folder of your choice.

   The folder should contain the Sapjco3.jar and libsapjco3.so files.
5. Copy these files to the following location under the Data Movement gateway installation directory:

   <Data Movement gateway\_Install\_Dir>/endpoint\_srv/endpoints/SAP.
6. Start the Data Movement gateway service:

   sudo systemctl start repagent
7. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

Information note

The SAP ODP connector will not be available for selection until the Java connector libraries have been installed and the Data Movement gateway service has been restarted.

## STXL table support

To expose the table STXL for extraction using the SAP ODP endpoint, a custom extractor needs to be created in transaction RSO2 in SAP GUI. This extractor can then be called by the SAP ODP endpoint.

## Setting up SLT on SAP

In order to replicate data, you must first define the parameters that SAP Landscape Transformation Replication Server will use to replicate data from a source system to a target system. You specify this information in a configuration. A configuration contains information about the source system, the target system, and the relevant connections.

You create a configuration in SAP Landscape Transformation Replication Server system. To create a configuration, open the SAP LT Replication Server Cockpit (transaction LTRC) and choose Create Configuration.

Creating a configuration involves the following steps:

1. In the Specify General Data tab, provide the following information:

   - Configuration Name: You must specify a name for the configuration. This name is used for the schema that is created automatically in the target system.
   - Description (Optional): Optionally, specify a description for the configuration.
2. In the Specify Source System tab, select the RFC Connection option and provide the following information:

   - RFC Destination: Enter NONE.
   - Allow Multiple Usage: Select this option.
3. In the Specify Target System tab, select the Other option and provide the following information:

   - Scenario: Select Operational Data Provisioning (ODP) from the drop-down list.
   - Queue Alias: Specify a name.
4. In the Specify Transfer Settings tab, specify transfer settings appropriate for your environment. Under Job Options, we recommend setting at least five Data Transfer, Initial Load, and Calculation Jobs.
5. In the Review and Create tab, review your settings and create the configuration.
6. Grant the [*Required permissions*](sap-odp-permissions.htm).

Once you have created a configuration, you can then proceed to configure the relevant connector settings.
