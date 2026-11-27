---
title: "Install the SAP NetWeaver RFC Client"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-Application-DB/sap-application-netweaver.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP (Application)", "Prerequisites"]
---

# Install the SAP NetWeaver RFC Client

You can install the SAP NetWeaver RFC client using the driver installation utility (recommended) or manually. Manual installation should only be attempted in the unlikely event that you encounter an issue with the driver installation utility.

Information note

Setting up a SAP NetWeaver RFC Client is only required if you opted to work with Data Movement gateway. For information on the benefits of Data Movement gateway and when it is required, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).

### Using the driver installation utility to install the SAP NetWeaver RFC client

This section describes how to install the required SAP NetWeaver RFC client. The process involves downloading the SAP NetWeaver RFC client, copying it to the required folder (see below), and running a script that will automatically install and configure it. You can also run scripts to update and uninstall the SAP NetWeaver RFC client as needed.

### Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version
- Download NetWeaver RFC SDK <version> "nwrfc<version>.zip" from the SAP Service Marketplace. You can find the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/sap.yaml. Once the download completes, copy the file to:

  /opt/qlik/gateway/movement/drivers/sap

### Installing the SAP NetWeaver RFC client

To install the SAP NetWeaver RFC client:

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

   ./install sap

The SAP NetWeaver RFC client will be installed.

5. Wait for the installation to complete (indicated by "Complete!") and then start the Data Movement gateway service:

   sudo systemctl start repagent
6. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Updating the SAP NetWeaver RFC client

Run the update command if you want to uninstall previous versions of the SAP NetWeaver RFC client before installing the provided SAP NetWeaver RFC client.

To update the SAP NetWeaver RFC client:

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

   ./update sap

The old SAP NetWeaver RFC client will be uninstalled and the new SAP NetWeaver RFC client will be installed.

5. Wait for the installation to complete (indicated by "Complete!") and then start the Data Movement gateway service:

   sudo systemctl start repagent
6. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Uninstalling the SAP NetWeaver RFC client

Run the uninstall command if you want to uninstall the SAP NetWeaver RFC client.

To uninstall the SAP NetWeaver RFC client:

1. Stop all tasks configured to use this connector.
2. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
3. Run the following command:

   Syntax:

   ./uninstall sap

   The SAP NetWeaver RFC client will be uninstalled.

### Manually installing the SAP NetWeaver RFC client

Information note

Qlik Talend Data Integration has been certified to work with NetWeaver RFC SDK 7.50 Patch 1021, which can be downloaded from the SAP Service Marketplace. As newer NetWeaver RFC SDK versions are constantly being released, it is not possible to certify compatibility with every version. We therefore recommend working with the certified version, even though later versions might also work without any issues.

You should only attempt to install the SAP NetWeaver RFC client manually if the automated driver installation did not complete successfully.

To do this:

1. Change the working directory to opt/qlik/gateway/movement/bin and run the following command:

   source arep\_login.sh

   This will set the Data Movement gateway installation path.
2. Extract the contents of the NWRFC\_xxx.SAR file and then copy the .so files from the nwrfcsdk/lib directory to the Data Movement gateway lib directory.
