---
title: "Install the SAP Java Connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-Extractor/extractor-prerequisites-java-driver.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP Extractor", "Prerequisites"]
---

# Install the SAP Java Connector

To work with the SAP Extractor connector, you need to install the SAP Java Connector on the Qlik Talend Data Integration server.

Information note

Setting up a driver is only required if you opted to work with Data Movement gateway. For information on the benefits of Data Movement gateway and when it is required, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).

## SAP Java Connector setup

You can install the SAP Java Connector using the driver installation utility (recommended) or manually. Manual installation should only be attempted in the unlikely event that you encounter an issue with the driver installation utility.

### Using the driver installation utility to install the SAP Java Connector

This section describes how to install the required SAP Java Connector. The process involves downloading the SAP Java Connector, copying it to the required folder (see below), and running a script that will automatically install and configure it. You can also run scripts to update and uninstall the SAP Java Connector as needed.

### Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version
- Download SAP Java Connector <version> "sapjco<version>.zip" from the SAP Support Portal. You can find the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/sapextractor.yaml. Once the download completes, copy the file to:

  /opt/qlik/gateway/movement/drivers/sapextractor

### Installing the SAP Java Connector

To install the SAP Java Connector:

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

   ./install sapextractor

The SAP Java Connector will be installed.

5. Wait for the installation to complete (indicated by "Complete!") and then start the Data Movement gateway service:

   sudo systemctl start repagent
6. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Updating the SAP Java Connector

Run the update command if you want to uninstall previous versions of the SAP Java Connector before installing the provided SAP Java Connector.

To update the SAP Java Connector:

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

   ./update sapextractor

The old SAP Java Connector will be uninstalled and the new SAP Java Connector will be installed.

5. Wait for the installation to complete (indicated by "Complete!") and then start the Data Movement gateway service:

   sudo systemctl start repagent
6. Optionally confirm that the service has started:

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

   ./uninstall sapextractor

   The SAP Java Connector will be uninstalled.

### Installing the SAP Java Connector manually

You should only attempt to install the SAP Java Connector manually if the automated driver installation did not complete successfully.

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

The SAP Extractor connector will not be available for selection until the Java connector libraries have been installed and the Data Movement gateway service has been restarted.
