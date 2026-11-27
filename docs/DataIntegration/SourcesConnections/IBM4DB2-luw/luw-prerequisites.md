---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-luw/luw-prerequisites.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for LUW"]
---

# Prerequisites

The following section describes the prerequisites for working with the IBM DB2 for LUW connector.

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
- Download the IBM Data Server Client "<version>\_linuxx64\_client.tar.gz" from the IBM web site. You can find the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/db2.yaml. Once the download completes, copy the file to:

  /opt/qlik/gateway/movement/drivers/db2

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

   ./install db2

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

   ./update db2

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

   ./uninstall db2

   The driver will be uninstalled.

### Manually installing the driver

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

On the Data Movement gateway machine, open a shell prompt and do the following:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
3. Install IBM Data Client v11.5.8\_linuxx64\_server\_t.tar.gz; choose to install “CLIENT”.
4. If the Data Movement gateway machine does not have a DB2 instance, create a DB2 instance by running the following commands:

   adduser <db2\_instance\_name>

   /opt/ibm/db2/V11.5/instance/db2icrt <db2\_instance\_name>
5. Add the DB2 driver location to the Linux library path.

   To do this, add the following line to the **site\_ arep\_login.sh** file as follows:

   export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/path/lib

   where path is the CLIENT path to the driver.

   **Example (with db2clnt1 as the instance name):**

   export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/home/db2clnt1/sqllib/lib:/home/db2clnt1/sqllib/lib64/gskit

   export DB2INSTANCE=db2clnt1
6. Create a new file named odbcinst.ini under **/etc** and add the following entry:

   [IBM DB2 ODBC DRIVER]

   Driver = /home/db2clnt1/sqllib/lib/libdb2o.so

   fileusage=1

   dontdlclose=1
7. Start the Data Movement gateway service:

   sudo systemctl start repagent
8. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago
9. Define the IBM DB2 for LUW connection settings as described in [*IBM DB2 for LUW*](IBM4DB2-luw-source.htm) and click Test Connection.

   If you get the following error:

   Cannot connect to DB2 LUW Server ODBC unknown error.

   RetCode: SQL\_ERROR SqlState: NativeError: -1390 Message: [unixODBC][IBM][CLI Driver] SQL10007N Message "0" could not be retrieved. Reason code: "3". ODBC general error.

   1. Run the following command:

      /opt/ibm/db2/V11.5/bin /db2cli writecfg add -database <db\_name\_from\_connector\_connection\_settings> -host <server\_name\_from\_connector\_connection\_settings> -port <port\_from\_connector\_connection\_settings>
   2. Change to the Data Movement gatewaybin directory (<install\_dir>/bin). Then, stop and start the Data Movement gateway service as described above.

## Enabling CDC on the database

To enable CDC (Change Data Capture):

- Set the database to be recoverable - To capture changes, Data Movement gateway requires the database to be configured as recoverable. A database is recoverable if either or both of the database configuration parameters LOGARCHMETH1 and LOGARCHMETH2 are not set to OFF.
- Permissions - The Qlik user must be granted the following permissions:

  - SYSADM or DBADM
  - DATAACCESS

- To enable data capture from IBM DB2 for LUW, the source tables need to be created as follows:

  CREATE / ALTER TABLE table-name …. DATA CAPTURE CHANGES [INCLUDE LONGVAR COLUMNS];

  You can either configure Data Movement gateway to perform this operation by selecting Automatically enable DATA CAPTURE CHANGES (requires admin privilege) in the connector settings or you can do this manually.

Information note

When the Automatically enable DATA CAPTURE CHANGES (requires admin privilege) option is selected, Data Movement gateway performs the ALTER TABLE operation when the task starts to run. If a new table that matches the table selection pattern is added (to the source database) while the task is already running, Data Movement gateway will only capture changes from it if it was created with the DATA CAPTURE CHANGE attribute described above.
