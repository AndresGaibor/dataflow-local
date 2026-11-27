---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-iseries/prereq-idb2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for iSeries"]
---

# Prerequisites

Before you can land or replicate data, make sure to complete the following prerequisites:

- Install the required driver on the Data Movement gateway server

  Information note

  This is only required if you opted to work with Data Movement gateway. For information on the benefits of Data Movement gateway and when it is required, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Grant the required permissions on the data source
- Configure the data source connector

## Driver setup

You can install the driver using the driver installation utility (recommended) or manually. Manual installation should only be attempted in the unlikely event that you encounter an issue with the driver installation utility.

### Using the driver installation utility to install the driver

This section describes how to install the required driver. The process involves downloading the driver, copying it to the required folder (see below), and running a script that will automatically install and configure it. You can also run scripts to update and uninstall the driver as needed.

### Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version
- Download the IBM i Access Client Solutions Linux Application Package "ibm-iaccess-<version>.x86\_64.rpm" from the IBM web site. You can find the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/db2iseries.yaml. Once the download completes, copy the file to:

  /opt/qlik/gateway/movement/drivers/db2i

### Installing the driver

To install the driver:

1. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
2. Run the following command:

   Syntax:

   ./install db2iseries

   Otherwise, the EULA for the driver will be displayed.
3. Do one of the following:

   - Press [Enter] repeatedly to slowly scroll through the EULA.
   - Press the Spacebar repeatedly to quickly scroll through the EULA.
   - Press q to quit the license text and be presented with the EULA acceptance options.
4. Do one of the following:

   - Type "y" and press [Enter] to accept the EULA and begin the installation.
   - Type "n" and press [Enter] to reject the EULA and exit the installation.
   - Type "v" and press [Enter] to view the EULA again.

The driver will be installed.

### Updating the driver

Run the update command if you want to uninstall previous versions of the driver before installing the provided driver.

To update the driver:

1. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
2. Run the following command:

   Syntax:

   ./update db2iseries

   Otherwise, the EULA for the driver will be displayed.
3. Do one of the following:

   - Press [Enter] repeatedly to slowly scroll through the EULA .
   - Press the Spacebar repeatedly to quickly scroll through the EULA.
   - Press q to quit the license text and be presented with the EULA acceptance options.
4. Do one of the following:

   - Type "y" and press [Enter] to accept the EULA and begin the installation.
   - Type "n" and press [Enter] to reject the EULA and exit the installation.
   - Type "v" and press [Enter] to review the EULA from the beginning.

The old driver will be uninstalled and the new driver will be installed.

### Uninstalling the driver

Run the uninstall command if you want to uninstall the driver.

To uninstall the driver:

1. Stop all tasks configured to use this connector.
2. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
3. Run the following command:

   Syntax:

   ./uninstall db2iseries

   The driver will be uninstalled.

### Manual driver setup

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

Download the IBM i Access Client Solutions Linux Application Package from the IBM website.

Information note

Supports iAccess ODBC driver versions 7.1.26 to 7.1.29 only.

For more information, see <https://www.ibm.com/docs/en/i/7.2?topic=packages-linux-application-package>

Then on the Data Movement gateway machine,
open a shell prompt and do the following:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
3. Install the RPM that is included in the downloaded package.

   Example:

   rpm -i ibm-iaccess-1.1.0.26-1.0.x86\_64

   Information note

   The displayed driver version will different in the Data Movement gateway logs. For instance, assuming the driver version is as in the above example, it will appear as ODBC driver version: '07.01.026' in the Data Movement gateway logs.

   For information on viewing the logs, see [*Troubleshooting data tasks*](../../Deploying/Troubleshooting-data-assets.htm).
4. Change the working directory to <Data Movement gateway\_Install\_Dir>/bin.
5. Add the DB2 driver location to the Linux library path.

   To do this, add the following path to the **site\_ arep\_login.sh** file in <install\_dir>/replicate/bin:

   export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/*path*/lib64

   where path is the path to the driver.

   **Example:**

   echo "export LD\_LIBRARY\_PATH=\$LD\_LIBRARY\_PATH:/opt/ibm/iaccess/lib64" >> site\_arep\_login.sh
6. Optionally, confirm that the driver location was copied:

   `cat site_arep_login.sh`
7. After the installation completes, open the /etc/odbcinst.ini file and make sure it contains the following section:

   [IBM i Access ODBC Driver 64-bit]
   Description = IBM i Access for Linux 64-bit ODBC Driver
   Driver = /opt/ibm/iaccess/lib64/libcwbodbc.so
   Setup = /opt/ibm/iaccess/lib64/libcwbodbcs.so
   Threading = 0
   DontDLClose = 1
   UsageCount = 1
8. Start the Data Movement gateway service:

   sudo systemctl start repagent
9. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

## CDC prerequisites

### Journal prerequisites

All of the source tables for a given moving task need to be journaled to the same journal. The name of the journal and the library in which it is located must be specified in the connector settings. During the task*,* Data Movement gateway polls this journal for changes to the source tables.

When you start journaling the source tables, the Record images parameter can be set to \*BOTH (for capturing before and after images) or \*AFTER.

When the Record images parameter set to \*AFTER. deleted records will contain NULL values in their data fields. To save a copy of the deleted record to the deleted record journal, you must set the Record images parameter set to \*BOTH.

Information note

If you need to run several moving tasks (that Move data from IBM DB2 for iSeries), it is more efficient (though not essential) to create a separate journal for each task. As only one journal can be specified per connector, you would also need to define a separate connector for each task.

### MINENTDTA parameter

The MINENTDTA parameter must be set to \*NONE as \*FILE (minimal logging) is not supported.
