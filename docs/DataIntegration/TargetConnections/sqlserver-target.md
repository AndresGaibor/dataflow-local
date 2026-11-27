---
title: "Microsoft SQL Server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/sqlserver-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to databases"]
---

# Microsoft SQL Server

This topic explains how to configure connectivity to a Microsoft SQL Server target using the Microsoft SQL Server target connector.

Microsoft SQL Server target can either be used in a data pipeline or in a replication task. In a data pipeline, various ELT operations can be performed on the target platform including storing data, transforming data, creating data marts, and registering data. A replication task, on the other hand, involves replication of data directly from a source system to a target system with basic transformation capabilities, but without support for ELT operations. Before you can connect to a Microsoft SQL Server target you need to configure the [*User prerequisites*](#Permissi) on the database. If you are connecting to Microsoft SQL Server via Data Movement gateway, you also need to install the driver as described in [*Driver setup*](#Driver).

For information about the limitations and considerations when using the Microsoft SQL Server Target connector, see [*Limitations and considerations*](#Limitati).

## Setting connection properties

To configure the connector, do the following:

1. In Connections, click Create connection.
2. Select the Microsoft SQL Server target connector and then provide the following settings:

### Data Movement gateway

Information noteIf you have a Qlik Talend Cloud Standard subscription, the Data gateway field will not be available as Data Movement gateway is not supported with this subscription tier.

Microsoft SQL Server can either be used as a target in a data pipeline or in a replication task. While Data Movement gateway might be required to access Microsoft SQL Server target in a pipeline (depending on whether the database is directly accessible from Qlik Cloud), it is always required when using a Microsoft SQL Server target in a replication task.

Information noteWhen accessing the target database via Data Movement gateway, you also need to install the appropriate driver on the Data Movement gateway machine. For details, see [*Driver setup*](#Driver) below.

#### Using a Microsoft SQL Server target in a data pipeline

Information noteThis field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.

A Data Movement gateway is only required if the target database is not accessible from Qlik Cloud and can only be accessed using a Private Link (for instance, if it's located on-premises behind a firewall or in a Virtual Private Cloud). If this is the case, select the Data Movement gateway through which you want to access the target database.

Depending on your use case, this will either be the same Data Movement gateway deployed to move data from the data source, or a different one.

For information about Data Movement gateway use cases, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top) and [*Common use cases*](../../Gateways/replication-gateway.htm#Common).

Information noteRequires Data Movement gateway 2022.11.70 or later.

If the target database is directly accessible from Qlik Cloud, select None.

#### Using a Microsoft SQL Server target in a replication task

Data gateway: Select the Data Movement gateway that will be used to test the connection to the Microsoft SQL Server target. This should be the same gateway that was used to access the data source.

Information note

Requires Data Movement gateway 2023.5.10 or later.

### Data target

- Cloud provider: Choose one of the following as appropriate:

  - None (for on-premises)
  - Amazon RDS
  - Google Cloud
  - Microsoft Azure (Supports both Microsoft Azure Managed Instance and Microsoft Azure Database)
- Server: The host name or IP address of the computer on which the Microsoft SQL Server database is installed.

  Information note

  To override the default port, add the port to the server name, separated by a comma. For example, if the server name is `myserver.company.local` and the port is `3333`, then the server name should be:

  `myserver.company.local,3333`

### Account properties

User Name and Password: The user name and password of a user authorized to access the Microsoft SQL Server database.

### Database properties

- Database name: There are two methods you can use to specify a database:

  - Method 1 - Select from a list: This method requires the user to be [created on the master database](#Permissi). Click Load databases and then select a database.
  - Method 2 - Manually: Select Enter database name manually and then enter the database name.
- Encrypt (Trust server certificate): Select to encrypt the communication between the database server and Data Movement gateway or between the database server and Qlik Cloud when Data gateway is set to None. When selected, the server certificate will be automatically trusted.
  - Host name in certificate: To only trust the sever certificate if its host name matches the value specified in this field, enter the server certificate's host name.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the connection.

## Prerequisites

### User prerequisites

- The user specified in the connector settings must have at least the `db_owner` user role on the target Microsoft SQL Server database.
- To be able to select a database (by clicking Load databases in the connector dialog), the user specified in the connector settings needs to be created on the master database.

### Driver setup

A driver is only required if you are accessing the database via Data Movement gateway. See Data Movement gateway above for more information about use cases when a Data Movement gateway is required.

You can install the driver using the driver installation utility (recommended) or manually. Manual installation should only be attempted in the unlikely event that you encounter an issue with the driver installation utility.

#### Using the driver installation utility to install the driver

This section describes how to install the required driver. The process involves running a script that will automatically download, install and configure the required driver. You can also run scripts to update and uninstall the driver as needed.

Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version

Installing the driver

To download and install the driver:

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

   ./install sqlserver

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will be displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the install sqlserver command again.

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

Updating the driver

Run the update command if you want to uninstall previous versions of the driver before installing the provided driver.

To download and update the driver:

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

   ./update sqlserver

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the update sqlserver command again.

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

Uninstalling the driver

Run the uninstall command if you want to uninstall the driver.

To uninstall the driver:

1. Stop all tasks configured to use this connector.
2. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
3. Run the following command:

   Syntax:

   ./uninstall sqlserver

   The driver will be uninstalled.

#### Installing the drivers manually

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

When using Microsoft SQL Server as a target, you need to install both the ODBC driver and the JDBC driver.

Installing the ODBC driver

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

Installing the JDBC driver

1. Download the mssql-jdbc-<version>.jar file. You can find a direct download link to the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/sqlserver.yaml. Once the download completes, copy the JAR file to the following folder on the Data Movement gateway machine:

   /opt/qlik/gateway/movement/qcs\_agents/qdi-db-commands/lib
2. Restart the Data Movement gateway service by running the command described in [*Restarting the service*](../../Gateways/dm-gateway-managing.htm#Restarti2)

## Limitations and considerations

### Limitations and considerations when used in a data pipeline

- When landing data to Microsoft SQL Server in a data pipeline, live views are nor supported. For more information on live views, see [*Storing datasets*](../Storage/generating-datasets.htm).

### Limitations and considerations for all data tasks

If following large object types are empty in the source database (0 bytes), they will not be empty after Full Load:

- BLOB will be written as 0x0000 (2 bytes)
- TEXT (VARCHAR(max)) will be written as 0X00 (1 byte)
- NTEXT (NVARCHAR(max)) will be written as 0x0000 (2 bytes)

Information noteIf these types are empty during Change Processing, they will be correctly written to the target as empty (0 bytes).

### Limitations and considerations for replication tasks only

- Full-sized LOB columns are not supported in Batch optimized apply mode. You can work around this limitation by limiting LOB column size [in the task settings](../Replicating/replicating-settings-metadata.htm) or switching to [Transactional apply mode](../Replicating/replicating-settings-replication.htm#Apply).
- When both [Batch optimized](../Replicating/replicating-settings-replication.htm#Apply) apply and [Replicate limited LOB columns (KB)](../Replicating/replicating-settings-metadata.htm) options are enabled, BLOB columns on the target will be truncated to a quarter of the size specified in the Limit LOB column size to field, while CLOB columns will be truncated to half the specified size.
- If you need to replicate 4-byte emoji characters, use a transformation to convert the data type from WSTRING(n ) to WSTRING ( n\*2 ).

## Data types

Native data type information is preserved, and is displayed in the Native data type column in dataset views. If the column is not visible, you need to open the column picker of the data set view and select the Native data type column.

Supported target data types

| Qlik Cloud data types | Microsoft SQL Server data types |
| --- | --- |
| BOOLEAN | TINYINT |
| BYTES | **VARBINARY(length)** |
| DATE | DATE |
| TIME | TIME(0) |
| DATETIME | If scale is 0-7, then:  DATETIME2 (Scale)  If scale exceeds 7, then:  DATETIME2 (7) |
| INT1 | **SMALLINT** |
| INT2 | **SMALLINT** |
| INT4 | **INT** |
| INT8 | **BIGINT** |
| NUMERIC | **NUMERIC(p,s)** |
| REAL4 | **REAL** |
| REAL8 | **FLOAT** |
| UINT1 | **INT2** |
| UINT2 | **INT4** |
| UINT4 | **INT8** |
| UINT8 | **NUMERIC(20)** |
| STRING | If column is date or time then:  DATETIME2  If the column is *not* a date or time:  **VARCHAR(length)**  Information noteIf subtype is JSON, and the Data Movement gateway, Microsoft SQL Server version, and Map compatible source JSON columns to JSON columns on the target task setting requirements described below are met, then JSON. Otherwise, VARCHAR(length). |
| WSTRING | **NVARCHAR(length)**  Information noteIf subtype is JSON, and the Data Movement gateway, Microsoft SQL Server version, and Map compatible source JSON columns to JSON columns on the target task setting requirements described below are met, then JSON. Otherwise, NVARCHAR(length). |
| CLOB | **VARCHAR(max)**  **TEXT**  Information noteIf subtype is JSON, and the Data Movement gateway, Microsoft SQL Server version, and Map compatible source JSON columns to JSON columns on the target task setting requirements described below are met, then JSON. Otherwise, VARCHAR(max). |
| NCLOB | **NVARCHAR(max)**  **NTEXT**  Information noteIf subtype is JSON, and the Data Movement gateway, Microsoft SQL Server version, and Map compatible source JSON columns to JSON columns on the target task setting requirements described below are met, then JSON. Otherwise, NVARCHAR(max). |
| BLOB | **VARBINARY(max)**  **IMAGE** |
| JSON | VARCHAR(max) Information noteNative JSON on the target requires Data Movement gateway May 2026 (2026.5) or later, Microsoft SQL Server 2025 as the target, and the Map compatible source JSON columns to JSON columns on the target task setting enabled. Otherwise, JSON is mapped to VARCHAR(max), as today. |

The following SQL Server data types are not supported. Data will not be read.

- CURSOR
- SQL\_VARIANT
- TABLE

The following data types are converted to VARCHAR (MAX):

- XML
- GEOGRAPHY
- GEOMETRY
