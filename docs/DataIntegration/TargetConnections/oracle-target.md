---
title: "Oracle"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/oracle-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to databases"]
---

# Oracle

This section explains how to configure connectivity to a Oracle target using the Oracle target connector. Oracle can be used as a target in a replication task only. Before you can connect to a Oracle target you need to configure the [*Required permissions*](#Permissi) on the database. If you are connecting to Oracle via Data Movement gateway, you also need to install the driver as described in [*Driver setup*](#Driver).

For information about the limitations and considerations when using the Oracle connector, see [*Limitations and considerations*](#Limitati).

## Setting connection properties

To configure the connector, do the following:

1. In Connections, click Create connection.
2. Select the Oracle target connector and then provide the following settings:

### Data target

- Data gateway: When working with Data Movement gateway, select the data gateway that will be used to test the connection to the Oracle target. This should be the same gateway that was used to access the data source.

  Information note
  - This field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.
  - You also need to install the appropriate driver on the Data Movement gateway machine. For details, see [*Driver setup*](#Driver) below.
- Connection string: The Oracle Connection String for the Oracle database you want to work with.

  Information note
  - When replicating to an Oracle Autonomous Data Warehouse, you first need to perform the procedure described in [*Connecting to an Oracle autonomous data warehouse*](#Connecti) .
  - This information is case sensitive.

### Account properties

User Name and Password: The user name and password of a user authorized to access the Oracle Server database.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the connection.

## Prerequisites

### Required permissions

The user specified in the connection string must be granted the following privileges granted in the Oracle database:

- CREATE ANY TABLE
- CREATE ANY INDEXES
- ALTER ANY TABLE
- DROP ANY TABLE
- INSERT ANY TABLE
- UPDATE ANY TABLE
- DELETE ANY TABLE
- SELECT ANY TABLE
- SELECT all\_indexes
- SELECT all\_ind\_columns
- SELECT all\_constraints
- SELECT all\_cons\_columns
- LOCK ANY TABLE

### Driver setup

You can install the driver using the driver installation utility (recommended) or manually. Manual installation should only be attempted in the unlikely event that you encounter an issue with the driver installation utility.

#### Using the driver installation utility to install the driver

This section describes how to install the required driver. The process involves running a script that will automatically download, install and configure the required driver. You can also run scripts to update and uninstall the driver as needed.

Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version

Installing the driver

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

Updating the driver

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

Uninstalling the driver

Run the uninstall command if you want to uninstall the driver.

To uninstall the driver:

1. Stop all tasks configured to use this connector.
2. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
3. Run the following command:

   Syntax:

   ./uninstall oracle

   The driver will be uninstalled.

#### Installing the driver manually

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

### Connecting to an Oracle autonomous data warehouse

The following procedure should be performed when replicating to an Oracle Autonomous Data Warehouse.

To set up connectivity to Oracle Autonomous Data Warehouse (ADW), you need the Client Credentials (Wallet) ZIP file that you downloaded when you set up your Oracle Autonomous Data Warehouse environment.

To enable Qlik Talend Data Integration to connect to Oracle Autonomous Data Warehouse:

1. Extract the contents of the Client Credentials ZIP file to a folder of your choice.

   This can be any folder, but for the purpose of this procedure, /home/adw\_credentials will be the Linux folder containing the extracted files.
2. In the folder containing the extracted files, edit the sqlnet.ora file, replacing ?/network/admin with the path of the folder containing the extracted files:

   `WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY="/home/adw_credentials")))`

   `SSL_SERVER_DN_MATCH=yes`
3. Create the TNS\_ADMIN environment variable and set it to the location of the credentials file.

   Run the following commands:

   `export TNS_ADMIN=/home/adw_credentials`

   `export PATH=$TNS_ADMIN:$PATH`
4. In the Oracle Target connector's Connection string field, enter one of the names from the tnsnames.ora file.

For more information on setting up connectivity to Oracle ADW, see:

[Connect Autonomous Transaction Processing Using a Client Application](https://docs.oracle.com/en/cloud/paas/atp-cloud/atpug/connect-preparing.html#GUID-EFAFA00E-54CC-47C7-8C71-E7868279EF3B)

## Limitations and considerations

The following limitations apply when using Oracle as a replication target:

- It is not possible to create new schemas in the Oracle database. To replicate to a new schema, the new schema name must already exist in the target database. You should then specify the new schema name in the task settings’ [*Metadata*](../Replicating/replicating-settings-metadata.htm) tab.
- When working in [Batch optimized apply](../Replicating/replicating-settings-replication.htm) mode, empty LOB columns might be replicated as NULL values.
- After Full Load completes, if the Limit LOB size to option is enabled and a table contains NCLOB data, the NCLOB size on the target will be truncated to half the size specified in the [Limit LOB size to](../Replicating/replicating-settings-metadata.htm) field. CDC will still truncate it according to the limit.

## Data types

Native data type information is preserved, and is displayed in the Native data type column in dataset views. If the column is not visible, you need to open the column picker of the data set view and select the Native data type column.

Data types

| Qlik Cloud Data Types | Oracle Data Types |
| --- | --- |
| BOOLEAN | NUMBER (1) |
| BYTES | RAW (length) |
| DATE | DATETIME |
| TIME | TIMESTAMP (0) |
| DATETIME | If scale <= 9, then TIMESTAMP (scale)  Otherwise, VARCHAR2 (37) |
| INT1 | NUMBER (3) |
| INT2 | NUMBER (5) |
| INT4 | NUMBER (10) |
| INT8 | NUMBER (19) |
| NUMERIC | NUMBER (p,s) |
| REAL4 | BINARY\_FLOAT |
| REAL8 | BINARY\_DOUBLE |
| STRING | With date indication: DATE  With time indication: TIMESTAMP  With timestamp indication: TIMESTAMP  With timestamp\_with\_timezone indication: TIMESTAMP WITH TIMEZONE  With timestamp\_with\_local\_timezone indication: TIMESTAMP WITH LOCAL TIMEZONE  With interval\_year\_to\_month indication: INTERVAL YEAR TO MONTH  With interval\_day\_to\_second indication: INTERVAL DAY TO SECOND  If Length > 4000: CLOB  In all other cases: VARCHAR2 (Length) |
| UINT1 | NUMBER (3) |
| UINT2 | NUMBER (5) |
| UINT4 | NUMBER (10) |
| UINT8 | NUMBER (19) |
| WSTRING | NVARCHAR2 (length)  Note that when length is greater than 2000, the column data type will be NCLOB. |
| BLOB | BLOB    Information note  - To use this data type in a replication task, you must enable the use of BLOBs for a specific task. - During CDC or during Full Load when the Allow unlimited LOB size option is enabled, LOB data types are supported only in tables with a primary key or unique index. |
| CLOB | CLOB  Information note  - To use this data type in a replication task, you must enable the use of CLOBs for a specific task. - During CDC or during Full Load when the Allow unlimited LOB size option is enabled, LOB data types are supported only in tables with a primary key or unique index. |
| NCLOB | NCLOB  Information note  - To use this data type in a replication task, you must enable the use of NCLOBs for a specific task. - During CDC or during Full Load when the Allow unlimited LOB size option is enabled, LOB data types are supported only in tables with a primary key or unique index. |
| The XMLTYPE target data type is only relevant in Oracle-to-Oracle replication tasks. See the note below. | XMLTYPE |
