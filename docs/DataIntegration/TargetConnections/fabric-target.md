---
title: "Microsoft Fabric"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/fabric-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to data warehouses"]
---

# Microsoft Fabric

You can use Microsoft Fabric as a target data platform in a data pipeline or in a replication task. In a data pipeline, various ELT operations can be performed on the target platform including storing data, transforming data, creating data marts, and registering data. A replication task, on the other hand, involves replication of data directly from a source system to a target system with basic transformation capabilities, but without support for ELT operations.

Information noteRequires Data Movement gateway 2023.5.15 or later.

Setting up Microsoft Fabric as a target involves:

- [Fulfilling the prerequisites](#Prerequi2)
- Configuring a connection to a cloud staging area (Azure Data Lake Storage). This is not required if you are [registering existing data](../Onboarding/Registering-data.htm).
- Configuring a connection to Microsoft Fabric

## Setting up a cloud staging area

Information noteIf you are you are [registering existing data](../Onboarding/Registering-data.htm), you do not need to set up a cloud staging area.

You also need an Azure Data Lake Storage cloud staging area where data and changes are staged, before being applied and stored. For information on setting up a connection to Azure Data Lake Storage, see [*Azure Data Lake Storage*](adls-target.htm).

## Setting Microsoft Fabric connection properties

Once you have provided the Azure Data Lake Storage Target settings, do the following:

1. In Connections, click Create connection.
2. Select the Microsoft Fabric  target connector and then provide the following settings:

### Data target

#### Data gateway

Information noteThis field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.

A Data Movement gateway is only required if the target database is not accessible from Qlik Cloud and can only be accessed using a Private Link (for instance, if it's located in a Virtual Private Cloud). If this is the case, select the Data Movement gateway through which you want to access the target database.

Depending on your use case, this will either be the same Data Movement gateway deployed to move data from the data source, or a different one.

For information about Data Movement gateway use cases, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top) and [*Common use cases*](../../Gateways/replication-gateway.htm#Common).

If the target database is directly accessible from Qlik Cloud, select None.

Information noteWhen accessing the target database via Data Movement gateway, you also need to install the appropriate driver on the Data Movement gateway machine. For details, see [*Microsoft Fabric*](#Driver) below.

### Connection properties

- Server: The name of the Microsoft Fabric Data Warehouse server you are using.

### Account properties

Authentication method: Select one of the following:

- Azure Active Directory Service Principal

  Then provide your Client ID and Client Secret in the designated fields.
- Azure Active Directory User Principal

  Then provide a User name and Password in the designated fields.

### Database properties

- Database name: There are two methods you can use to specify a database:

  - Method 1 - Select from a list: Click Load databases and then select a database.
  - Method 2 - Manually: Select Enter database name manually and then enter the database name.

### Data loading

- SAS token: The SAS token that will be used by Microsoft Fabric to access the ADLS storage account. This is not required if you are [registering existing data](../Onboarding/Registering-data.htm).

### Name

The display name for the connection.

## Prerequisites

### Database permissions

The Azure Active Directory User/Service Principal specified in the ODBC Access section of the Microsoft Fabric connector settings must be granted the Contributor role.

### Driver setup

A driver is only required if you are accessing the database via Data Movement gateway. In such a case, you need to install the driver on the Data Movement gateway machine.

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

   ./install fabric

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will be displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the install fabric command again.

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

   ./update fabric

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the update fabric command again.

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

   ./uninstall fabric

   The driver will be uninstalled.

#### Manually installing the driver

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

You need to install both an ODBC driver and a JDBC driver.

Installing the ODBC driver

After Data Movement gateway is installed, download the msodbcsql<version>.x86\_64.rpm driver. You can find a direct download link to the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/fabric.yaml. Once the download completes, copy the RPM to the Data Movement gateway machine.

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

The status should be as follows:

Active: inactive (dead) since <timestamp> ago

3. Install the driver on the Data Movement gateway machine.
4. Copy the driver location to the `site_arep_login.sh` file as follows:

   `echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/opt/microsoft/msodbcsql<version>/lib64/" >> site_arep_login.sh`

   Example:

   `echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/opt/microsoft/msodbcsql17/lib64/" >> site_arep_login.sh`

   This will add the driver to "LD\_LIBRARY\_PATH" and update the driver location in the **site\_arep\_login.sh** file.
5. Optionally, confirm that the driver location was copied:

   `cat site_arep_login.sh`
6. Start the Data Movement gateway service:

   sudo systemctl start repagent
7. Optionally, confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

Installing the JDBC driver

1. Download the JAR files listed under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/fabric.yaml. Then copy the files to the following folder on the Data Movement gateway machine:

   /opt/qlik/gateway/movement/qcs\_agents/qdi-db-commands/lib
2. Restart the Data Movement gateway service by running the command described in [*Restarting the service*](../../Gateways/dm-gateway-managing.htm#Restarti2)

Warning noteIf you are using a Microsoft SQL Server data source (CDC-based or log-based), uninstalling the Fabric driver will break connectivity to SQL Server as well, as they share the same driver.

### Ports

Open port 1433 for outbound communication.

## Limitations and considerations

- The following operations are not supported and will not be applied to the target:

  - RENAME column
  - DROP/ALTER column
- Newly added columns (ADD COLUMN) must be nullable.

Information note

From Data Movement gatewayy 2026.5.1, target data types are mapped to `MAX` length instead of `8000`. To apply the mapping to existing columns in registered data, storage, transform, data mart, and knowledge mart tasks, run `ALTER TABLE` to change the column data type or recreate the tables. For other task types, recreate the tables.

## Data types

The following table shows the Microsoft Fabric data types that are supported when using Qlik Cloud and the default mapping from Qlik Cloud data types.

Native data type information is preserved, and is displayed in the Native data type column in dataset views. If the column is not visible, you need to open the column picker of the data set view and select the Native data type column.

Supported data types

| Qlik Talend Data Integration data types | Microsoft Fabric data types |
| --- | --- |
| BOOL | BIT |
| BYTES | If length is 1-8000, then:  VARBINARY (Length in Bytes)  BYTES are mapped to VARBINARY (MAX) if length exceeds 8000 bytes. |
| DATE | DATE |
| TIME | If scale is 0-6, then:  TIME (Scale)  If scale exceeds 6, then:  TIME (6) |
| TIMESTAMP | If scale is 0-6, then:  DATETIME2 (Scale)  If scale exceeds 6, then:  DATETIME2 (6) |
| INT1 | SMALLINT |
| INT2 | SMALLINT |
| INT4 | INT |
| INT8 | BIGINT |
| NUMERIC | DECIMAL (p,s) |
| REAL4 | FLOAT(24) |
| REAL8 | FLOAT(53) |
| STRING | If length in bytes is 1-8000, then:  VARCHAR (Length in Bytes)  STRING is mapped to VARCHAR (MAX) if length in bytes exceeds 8000. |
| UINT1 | SMALLINT |
| UINT2 | INT |
| UINT4 | BIGINT |
| UINT8 | DECIMAL (20,0) |
| WSTRING | If length in bytes is 1-8000, then:  VARCHAR (Length in Bytes)  WSTRING is mapped to VARCHAR (MAX) if length in bytes exceeds 8000. |
| BLOB | VARBINARY (MAX) |
| NCLOB | VARCHAR (MAX) |
| CLOB | VARCHAR (MAX) |
| JSON | VARCHAR (MAX) |

Information noteFull LOB data types are not supported. For information on including Limited-size LOB data types in the moving, see [*Landing data from data sources*](../Landing/Landing-data-data-sources.htm#Runtime).
