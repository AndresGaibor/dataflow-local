---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Oracle/oracle-prerequisites-server.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
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

   ./install oracle

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will be displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the install oracle command again.

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

   ./update oracle

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the update oracle command again.

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

   ./uninstall oracle

   The driver will be uninstalled.

### Installing the driver manually

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

After Data Movement gateway is installed, download the oracle-instantclient-basiclite-<version>.x86\_64.rpm driver. You can find a direct download link to the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/oracle.yaml. Once the download completes, copy the RPM to the Data Movement gateway machine.

Then, on the Data Movement gateway server,
open a shell prompt and do the following:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

The status should be as follows:

Active: inactive (dead) since <timestamp> ago

3. Install the driver (RPM).
4. In addition, if not already included in your system, create a symbolic link in the $Oracle\_Home\lib directory. Name the link libclntsh.so, and point it to a specific version of this file.

   Example:

   lrwxrwxrwx 1 oracle oracle 63 Oct 2 14:16 libclntsh.so -> /u01/app/oracle/home/lib/libclntsh.so.21.1
5. Change the working directory to <Data Movement gateway-Install-Dir>/bin and append the LD\_LIBRARY\_PATH environment variable to the Oracle instant client directory and to the Data Movement gatewaylib directory by copying the driver location to the site\_arep\_login.sh file:

   echo "export LD\_LIBRARY\_PATH=\$LD\_LIBRARY\_PATH:/opt/oracle/instantclient\_<version>:/opt/qlik/gateway/movement/lib/" >> site\_arep\_login.sh
6. Optionally, confirm that the driver location was copied:

   `cat site_arep_login.sh`
7. Start the Data Movement gateway service:

   sudo systemctl start repagent
8. Optionally, confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

## Provide Oracle account access

You must provide Oracle account access to the Data Movement gateway user. This user must have read/write privileges on the Oracle database. For information on setting up access to the Oracle account, see [*Required permissions*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/OracleDBSource_Security.htm).

## Ensure that ARCHIVELOG mode is on

Oracle can be run in two different modes: the ARCHIVELOG mode and the NOARCHIVELOG mode. To use the Oracle logs with Data Movement gateway, run the database in ARCHIVELOG mode. If the log is not set to ARCHIVELOG mode, then execute the following query:

ALTER database ARCHIVELOG

Note that if your Oracle database instance is on Amazon RDS, a different command needs to be executed. For more information, see [*Enabling automatic backups*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/oracle_rds_prerequisites.htm#Enabling) and [*Setting up archiving*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/oracle_rds_prerequisites.htm#ar_oracleds_385117211_chdddeji)

## Set up supplemental logging

Supplemental logging must be enabled for the Oracle database, both at the database level and at the table level.

Information note

When moving from an Oracle standby environment, supplemental logging must be set up in the primary Oracle instance (as described below), not in the standby instance.

### Checking and enabling supplemental logging at database level

1. Run the following query:

   SELECT name, value, description FROM v$parameter WHERE name = 'compatible';

   The returned result should be from GE to n.n.n where n.n.n is the Oracle database version (e.g. 10.0.0).

   Warning note

   The parameter value must match the real version of the database.
2. Run the following query:

   SELECT supplemental\_log\_data\_min FROM v$database;

   The returned result should be YES or IMPLICIT.

   Enable supplemental logging by executing the following query:

   ALTER DATABASE ADD SUPPLEMENTAL LOG DATA

   Information note

   If your Oracle database instance is on Amazon RDS, a different command needs to be executed. For more information, see [*Working with Amazon RDS for Oracle*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/oracle_rds_prerequisites.htm).

### Checking and enabling supplemental logging at table level

1. To check whether supplemental logging is enabled at table level, run the following query:

   Syntax:

   select count(\*) from ALL\_LOG\_GROUPS where LOG\_GROUP\_TYPE='ALL COLUMN LOGGING' and OWNER= 'OWNER' and TABLE\_NAME='TABLE-NAME';

   Example:

   select count(\*) from ALL\_LOG\_GROUPS where LOG\_GROUP\_TYPE='ALL COLUMN LOGGING' and OWNER= 'HR' and TABLE\_NAME='EMPLOYEES';
2. To enable supplemental logging at table level, run the following query:

   Syntax:

   ALTER TABLE TABLE-NAME ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

   Example:

   ALTER TABLE HR.EMPLOYEES ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

See also: [*Required permissions*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/OracleDBSource_Security.htm)
