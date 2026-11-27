---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Teradata/teradata-prerequisites-server.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Teradata"]
---

# Prerequisites

The following section describes the prerequisites for working with Teradata as a source in Qlik Talend Cloud Data Integration.

## Replicate Server for Windows

Install the Teradata Database ODBC Driver 17.20 or 20.00 for Windows.

Download the driver from the [Teradata Download Center](https://downloads.teradata.com/download/connectivity/odbc-driver/windows).

## Replicate Server for Linux

The following steps describe how to work with Teradata as a source on a Linux data movement gateway. Teradata Database Client requires the DataDirect ODBC driver manager provided with the client.

Information note

These instructions assume that Teradata Database Client 20.00 is installed in /opt/teradata/client/20.00. If you install another version or use a different location, change the paths accordingly.

1. Stop the Data Movement gateway service and confirm that it has stopped.
2. Install Teradata Database Client 20.00 or earlier for Linux.

   Download the driver from <https://downloads.teradata.com/download/connectivity/odbc-driver/linux>.
3. Copy the downloaded client package to /opt/qlik/gateway/movement/drivers/teradata and run install teradata.
4. Set the following environment variables:

   TD\_CLIENT=/opt/teradata/client/20.00/odbc\_64/lib:/opt/teradata/client/17.20/lib64; export TD\_CLIENT

   ODBCINI=/opt/teradata/client/20.00/odbc\_64/odbc.ini; export ODBCINI

   ODBCINST=/opt/teradata/client/20.00/odbc\_64/odbcinst.ini; export ODBCINST
5. Set the library path:

   LD\_LIBRARY\_PATH=$TD\_CLIENT:/opt/qlik/gateway/lib:/lib64:/usr/lib64; export LD\_LIBRARY\_PATH
6. Run echo $LD\_LIBRARY\_PATH to verify that the path is updated.
7. Add the export commands to the gateway service login script so they are available after service restarts.
8. Start the Data Movement gateway service and confirm that it has started.

Information note

A task cannot use endpoints that require different ODBC Driver Managers. Teradata sources use the DataDirect ODBC Driver Manager, while most Linux targets use unixODBC. When the task combines a DataDirect source with a target that requires unixODBC, use the Qlik Replication File Channel.

Before you configure the Teradata source, add the Teradata Database host and database mapping to the hosts file on the gateway machine. For the procedure, see [*Editing the hosts file*](teradata-hosts-file.htm).

This section describes how to install the required driver. The process involves downloading the driver, copying it to the required folder (see below), and running a script that will automatically install and configure it. You can also run scripts to update and uninstall the driver as needed.

### Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version

### Installing the driver

To install the driver:

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

   ./install teradata

   Otherwise, the EULA for the driver will be displayed.
5. Do one of the following:

   - Press [Enter] repeatedly to slowly scroll through the EULA.
   - Press the Spacebar repeatedly to quickly scroll through the EULA.
   - Press q to quit the license text and be presented with the EULA acceptance options.
6. Do one of the following:

   - Type "y" and press [Enter] to accept the EULA and begin the installation.
   - Type "n" and press [Enter] to reject the EULA and exit the installation.
   - Type "v" and press [Enter] to view the EULA again.

The driver will be installed.

7. Wait for the installation to complete (indicated by "Complete!") and then start the Data Movement gateway service:

   sudo systemctl start repagent
8. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Updating the driver

Run the update command if you want to uninstall previous versions of the driver before installing the provided driver.

To update the driver:

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

   ./update teradata

   Otherwise, the EULA for the driver will be displayed.
5. Do one of the following:

   - Press [Enter] repeatedly to slowly scroll through the EULA .
   - Press the Spacebar repeatedly to quickly scroll through the EULA.
   - Press q to quit the license text and be presented with the EULA acceptance options.
6. Do one of the following:

   - Type "y" and press [Enter] to accept the EULA and begin the installation.
   - Type "n" and press [Enter] to reject the EULA and exit the installation.
   - Type "v" and press [Enter] to review the EULA from the beginning.

The old driver will be uninstalled and the new driver will be installed.

7. Wait for the installation to complete (indicated by "Complete!") and then start the Data Movement gateway service:

   sudo systemctl start repagent
8. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Uninstalling the driver

Run the uninstall command if you want to uninstall the driver.

To uninstall the driver:

1. Stop all tasks configured to use this connector.
2. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
3. Run the following command:

   Syntax:

   ./uninstall teradata

   The driver will be uninstalled.

## Provide account access

The user specified in the connector definition must be a valid Teradata Database user and have the privileges required to read the source tables and to perform the change processing operations used by the task.

For more information about Teradata security and access requirements, see the Qlik Replicate user guide for Teradata sources.
