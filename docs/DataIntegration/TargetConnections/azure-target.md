---
title: "Azure Synapse Analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/azure-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to data warehouses"]
---

# Azure Synapse Analytics

You can use Azure Synapse Analytics as a target data platform in a data pipeline. In a data pipeline, various ELT operations can be performed on the target platform including storing data, transforming data, creating data marts, and registering data.

Setting up Azure Synapse Analytics as a target involves:

- [Fulfilling the prerequisites](#Prerequi2)
- Configuring a connection to a cloud staging area (Azure Data Lake Storage). This is not required if you are [registering existing data](../Onboarding/Registering-data.htm).
- Configuring a connection to Azure Synapse Analytics

## Setting up a cloud staging area

Information noteIf you are you are [registering existing data](../Onboarding/Registering-data.htm), you do not need to set up a cloud staging area.

You also need an Azure Data Lake Storage cloud staging area where data and changes are staged, before being applied and stored. For information on setting up a connection to Azure Data Lake Storage, see [*Azure Data Lake Storage*](adls-target.htm).

## Setting Azure Synapse Analytics connection properties

Once you have provided the Azure Data Lake Storage Target settings, do the following:

1. In Connections, click Create connection.
2. Select the Azure Synapse Analytics target connector and then provide the following settings:

### Data target

#### Data gateway

Information noteThis field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.

A Data Movement gateway is only required if the target database is not accessible from Qlik Cloud and can only be accessed using a Private Link (for instance, if it's located in a Virtual Private Cloud). If this is the case, select the Data Movement gateway through which you want to access the target database.

Depending on your use case, this will either be the same Data Movement gateway deployed to move data from the data source, or a different one.

For information about Data Movement gateway use cases, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top) and [*Common use cases*](../../Gateways/replication-gateway.htm#Common).

If the target database is directly accessible from Qlik Cloud, select None.

Information noteWhen accessing the target database via Data Movement gateway, you also need to install the appropriate driver on the Data Movement gateway machine. For details, see [*Azure Synapse Analytics*](#Driver) below.

### Connection properties

- Server: Host name to identify the location of the Azure Synapse Analytics database.
- Port: The port through which to access your Azure Synapse Analytics database. The default is 1433.

### Account properties

User Name and Password: The user name and password of a user authorized to access the Azure Synapse Analytics database.

### Database properties

- Database name: There are two methods you can use to specify a database:

  - Method 1 - Select from a list: This method requires the user to be [created on the master database](#Database). Click Load databases and then select a database.
  - Method 2 - Manually: Select Enter database name manually and then enter the database name.

### Data loading properties

Information noteIf you are just [registering data](../Onboarding/Registering-data.htm) (i.e. not landing data), these fields are not required.

The SQL Server credential can be created automatically during runtime (the default) or you can use an existing credential. Do one of the following as appropriate:

- When the Create SQL Server credential check box is selected (the default) the SQL Server credential will be created automatically during runtime. Specify your access key in the Access key field.
- To use an existing credential, clear the Create SQL Server credential check box and specify your SQL Server credential name in the Credential name field.

### Name

The display name for the connection.

## Prerequisites

### Permissions

You need to grant both storage permissions and database permissions, as describe below.

#### Storage permissions

The user specified in the Azure Synapse Analytics connector must be granted the following storage permissions.

- On the ADLS Gen2 Storage container: LIST
- On the ADLS Gen2 Storage folder: READ, WRITE and DELETE
- In the Access Control (IAM) settings for the ADLS Gen2 file system, assign the “Storage Blob Data Contributor” role to Data Movement gateway (AD App ID). It may take a few minutes for the role to take effect.

#### Database permissions

The user specified in the Azure Synapse Analytics connector must be granted the following permissions on the database:

- **General permissions:**

  - db\_owner role
- **Table permissions:**

  - SELECT, INSERT, UPDATE and DELETE
  - Bulk Load
  - CREATE, ALTER, DROP (if required by the task's definition)

### Database selection

To be able to select a database (by clicking Load databases in the connector dialog), the user specified in the connector settings needs to be created on the master database.

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

#### Manually installing the driver

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

You need to install both an ODBC driver and a JDBC driver.

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

### Ports

- When Data Movement gateway runs on a machine outside Azure
  - Open port 1433 for outbound communication.
- When Data Movement gateway runs on an AzureVM - Open the following ports for outbound communication:
  - 1433
  - 11000-11999
  - 14000-14999

## Limitations and considerations

When using Azure Synapse Analytics as a target, you need to take into account the following limitations and considerations:

Information noteIn data pipeline projects, SaaS connectors are not supported as sources for Azure Synapse Analytics.

- Source columns with CHAR/VARCHAR data types and a non-Latin collation (e.g. "Chinese\_PRC\_CI\_AS") need to be mapped to NVARCHAR.
- Empty source column handling:

  - When moving a source binary column (for example, VARBINARY or BLOB) with an empty value, Qlik Talend Data Integration inserts a NULL into the corresponding target column.

  Information noteEmpty values are not NULL, but data with zero length.
- Moving of records exceeding 1 MB is not supported.
- Moving of data with 4-byte emoji characters requires the data type to be a wide string (for example, NCHAR/NVARCHAR/NCLOB) on the target.

## Data types

The following table shows the Azure Synapse Analytics data types that are supported when using Qlik Cloud and the default mapping from Qlik Cloud data types.

Native data type information is preserved, and is displayed in the Native data type column in dataset views. If the column is not visible, you need to open the column picker of the data set view and select the Native data type column.

Supported data types

| Qlik Cloud data types | Azure Synapse Analytics data types |
| --- | --- |
| BOOLEAN | BIT |
| BYTES | VARBINARY (length in Bytes) |
| DATE | DATE |
| TIME | TIME |
| DATETIME | If scale is => 0 and =< 7, then:  DATETIME2 (s)  If scale is => 8 and =< 9, then:  VARCHAR (37) |
| INT1 | BYTEINT |
| INT2 | SMALLINT |
| INT4 | INTEGER |
| INT8 | BIGINT |
| NUMERIC | NUMERIC (precision, scale) |
| REAL4 | REAL |
| REAL8 | FLOAT |
| UINT1 | BYTEINT |
| UINT2 | INTEGER |
| UINT4 | INTEGER |
| UINT8 | BIGINT |
| STRING | VARCHAR (length in Bytes) |
| WSTRING | NVARCHAR (length in Bytes) |
| BLOB | VARBINARY (length in Bytes) |
| NCLOB | NVARCHAR (length in Bytes) |
| CLOB | VARCHAR (length in Bytes) |
| JSON | VARCHAR (max) |
