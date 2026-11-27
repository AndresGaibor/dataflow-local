---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/AzureSQLMSCDC/Prereqs-sql-server-cdc.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Microsoft SQL Server (Microsoft CDC based)"]
---

# Prerequisites

Before you can land or replicate data, make sure to complete the following prerequisites:

- Install the required driver on the Data Movement gateway server

  Information note

  This is only required if you opted to work with Data Movement gateway. For information on the benefits of Data Movement gateway and when it is required, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).

  Note that Data Movement gateway is not available with the Qlik Talend Cloud Starter subscription.
- Grant the required permissions on the data source
- Configure the data source connector

## Driver setup

You can install the driver using the driver installation utility (recommended) or manually. Manual installation should only be attempted in the unlikely event that you encounter an issue with the driver installation utility.

### Using the driver installation utility to install the driver

This section describes how to install the required driver. The process involves running a script that will automatically download, install and configure the required driver. You can also run scripts to update and uninstall the driver as needed.

### Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version

### Installing the driver

To download and install the driver:

1. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
2. Run the following command:

   Syntax:

   ./install sqlserver

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will be displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the install sqlserver command again.

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

To download and update the driver:

1. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
2. Run the following command:

   Syntax:

   ./update sqlserver

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the update sqlserver command again.

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

   ./uninstall sqlserver

   The driver will be uninstalled.

### Installing the driver manually

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

After Data Movement gateway is installed, download the msodbcsql<version>.x86\_64.rpm driver. You can find a direct download link to the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/sqlserver.yaml. Once the download completes, copy the RPM to the Data Movement gateway machine.

On the Data Movement gateway server,
open a shell prompt and do the following:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

The status should be as follows:

Active: inactive (dead) since <timestamp> ago

3. Install the driver (RPM).
4. Change the working directory to <product\_dir>/bin.
5. Copy the driver location to the `site_arep_login.sh` file as follows:

   `echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/opt/microsoft/``msodbcsql<version>``/lib64/" >> site_arep_login.sh`

   This will add the driver to "LD\_LIBRARY\_PATH" and update the driver location in the **site\_arep\_login.sh** file.
6. Optionally, confirm that the driver location was copied:

   `cat site_arep_login.sh`
7. Start the Data Movement gateway service:

   sudo systemctl start repagent
8. Optionally, confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago
9. Data Movement gateway requires the following ODBC library: msodbcsql-18.1.so.1.1

   To check which library version is currently installed Issue the following command:

   `ls /opt/microsoft/msodbcsql<version>/lib64/`

   If the existing library has a different version number (for example, libmsodbcsql-18.0.so.1.1), you need to create a symbolic link between the existing library and the required library.

   To do this, issue the following commands:

   `cd /opt/microsoft/msodbcsql<version>/lib64/`

   `ln -s existing_library_name` msodbcsql-18.1.so.1.1

   where `existing_library_name` is the name of the currently installed library (for example, libmsodbcsql-18.0.so.1.1).

Warning noteIf you are using a Microsoft Fabric target, uninstalling the Microsoft ODBC Driver for SQL Server driver will break connectivity to Microsoft Fabric as well, as they share the same driver.

## Database selection

To be able to select a database (by clicking Load databases in the connector dialog), the user specified in the connector settings needs to be created on the master database.

## Port

By default, port 1434 needs to be opened for outbound communication on the Data Movement gateway server. You can change this in the connector settings.

## Preparing the database for CDC

The following section explains how to set up the database for CDC.

To set up the database for CDC:

1. Set up the database for MS-CDC by executing the following:

   exec *source\_db\_name*.dbo.sp\_cdc\_enable\_db

   where source\_db\_name is the name of the source database.
2. The landing task automatically enables MS-CDC for all the source tables. However, if you prefer to enable MS-CDC manually, execute the following script (for each of the intended source tables):

   exec sys.sp\_cdc\_enable\_table

   @source\_schema = N'*schema\_name*',

   @source\_name = N'*table\_name*',

   @role\_name = NULL

   where *schema\_name* and *table\_name* are the names of the source schema and the source table respectively.

   Information note
   - The CT table names must use the default naming format: <SchemaName>\_<TableName>\_CT
   - The CT table must include the following columns: [\_\_$start\_lsn], [\_\_$end\_lsn], [\_\_$seqval], [\_\_$operation], [\_\_$update\_mask], <all the data columns>, [\_\_$command\_id]
3. Make sure the MS-CDC capture and cleanup jobs are running.

   Information note
   - You can control the jobs using sys.sp\_cdc\_change\_job. For additional information, see the Microsoft Help.
   - To reduce latency, you might want to set the @pollinginterval parameter to a small value.
