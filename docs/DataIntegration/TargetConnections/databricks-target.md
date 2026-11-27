---
title: "Databricks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/databricks-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to data warehouses"]
---

# Databricks

You can use Databricks as a target data platform in a data pipeline or in a replication task. In a data pipeline, various ELT operations can be performed on the target platform including storing data, transforming data, creating data marts, and registering data. A replication task, on the other hand, involves replication of data directly from a source system to a target system with basic transformation capabilities, but without support for ELT operations.

Setting up Databricks as a target involves:

- [Fulfilling the prerequisites](#Prerequi2)
- Configuring a connection to a cloud staging area. This is not required if you are [registering existing data](../Onboarding/Registering-data.htm).
- Configuring a connection to Databricks

Information noteSupported with SQL Warehouse clusters only

## Setting up a cloud staging area

When using the Databricks Target connector, you also need to define a cloud staging area where data and changes are staged there before being applied and stored. The following storage platforms are supported:

- [Amazon S3](aws-s3-target.htm)
- [Azure Data Lake Storage](adls-target.htm)
- [Google Cloud Storage](google-storage-target.htm)

Information noteIf you are you are [registering existing data](../Onboarding/Registering-data.htm), you do not need to set up a cloud staging area.

## Configuring a connection to Databricks

Once you have provided the staging settings, do the following:

1. In Connections, click Create connection.
2. Select the Databricks target connector and then provide the following settings:

### Data target

#### Data gateway

Information noteThis field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.

A Data Movement gateway is only required if the target database is not accessible from Qlik Cloud and can only be accessed using a Private Link (for instance, if it's located in a Virtual Private Cloud). If this is the case, select the Data Movement gateway through which you want to access the target database.

Depending on your use case, this will either be the same Data Movement gateway deployed to move data from the data source, or a different one.

For information about Data Movement gateway use cases, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top) and [*Common use cases*](../../Gateways/replication-gateway.htm#Common).

If the target database is directly accessible from Qlik Cloud, select None.

Information noteWhen accessing the target database via Data Movement gateway, you also need to install the appropriate driver on the Data Movement gateway machine. For details, see [*Driver setup*](#Driver) below.

### Connection properties

- Host: the host name of the Databricks workspace.
- Port: the port via which to access the workspace.
- HTTP Path: the path to the cluster being used.

### Authentication

- Authentication Method - Select one of the following:

  - OAuth: Provide the following information:

    Information note

    OAuth authentication prerequisites:

    - Make sure your Databricks  database is configured to use OAuth. For instructions, see the vendor's online help.
    - If you are using Data Movement gateway to access the database, Data Movement gateway 2024.11.30 or later is required.

    - Client ID: The client ID of your application.
    - Client Secret: The client secret of your application. Note that if you edit the connection, the client secret will be removed as a safeguard, and you will need to re-enter it.
  - Personal Access Token: In the Token field, enter your personal token for accessing the workspace.

### Catalog properties

Click Load catalogs to load the available catalogs and then select a Catalog. If your environment is not configured with any catalogs, select hive\_metastore, which is the default catalog.

Information note

You need to allow the data task to access external (unmanaged) tables by defining an external location in Databricks. For guidelines, see:

<https://docs.databricks.com/data-governance/unity-catalog/manage-external-locations-and-credentials.html#manage-permissions-for-an-external-location>

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the connection.

## Prerequisites

### General permissions

- The time on the Qlik Talend Data Integration Server machine must be accurate.
- Databricks table permissions: Qlik Talend Data Integration requires permissions to perform the following operations on Databricks tables: CREATE, DROP, TRUNCATE, DESCRIBE, and ALTER table.
- In the Access Control (IAM) settings for the ADLS Gen2 file system, assign the “Storage Blob Data Contributor” role to Qlik Talend Data Integration (AD App ID). It may take a few minutes for the role to take effect.
- In order for Qlik Talend Data Integration to connect to a Databricks cluster via ODBC, users must be granted "Can Attach To" permission in their Databricks account.
- A valid security token is required to access Databricks. The token should be specified when configuring the Databricks ODBC Access fields in the endpoint settings.
- When configuring a new cluster with Microsoft Azure Data Lake Storage (ADLS) Gen2, the following line must be added to the "Spark Config" section.

  `spark.hadoop.hive.server2.enable.doAs false`
- To be able to access the storage directories from the Databricks cluster, users need to add a configuration (in Spark Config) for that Storage Account and its key.

  Example:

  fs.azure.account.key.<storage-account-name>.dfs.core.windows.net <storage-account-access-key>

  For details, refer to the Databricks online help at: <https://docs.databricks.com/clusters/configure.html#spark-configuration>
- Best practice is *not* to use the root location (/Usr/Hive/Warehouse/) for the Databricks database as doing so may impact performance.

### Storage access permission

Databricks SQL compute must be configured to access cloud storage. For instructions, see the vendor’s online help.

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

   ./install databricks

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will be displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the install databricks command again.

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

   ./update databricks

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the update databricks command again.

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

   ./uninstall databricks

   The driver will be uninstalled.

#### Manually installing the driver

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

Installing the ODBC driver

After Data Movement gateway is installed, download the SimbaSparkODBC-<version>-LinuxRPM-64bit.zip file. You can find a direct download link to the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/databricks.yaml. Once the download completes, copy the file to the Data Movement gateway machine.

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

The status should be as follows:

Active: inactive (dead) since <timestamp> ago

3. Install the driver on the Data Movement gateway machine.
4. Once installed, make sure the following section appears in the /etc/odbcinst.ini file:

```
[Databricks ODBC Driver]
Driver=/opt/databricks/databricksodbc/lib/64/libdatabricksodbc64.so
```

5. Start the Data Movement gateway service:

   sudo systemctl start repagent
6. Optionally, confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

Installing the JDBC driver

1. Download the databricks-jdbc-<version>.jar file. You can find a direct download link to the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/databricks.yaml. Once the download completes, copy the JAR file to the following folder on the Data Movement gateway machine:

   /opt/qlik/gateway/movement/qcs\_agents/qdi-db-commands/lib
2. Restart the Data Movement gateway service and check that it has started by running the commands described in [*Data Movement gateway service commands*](../../Gateways/dm-gateway-managing.htm#Restarti)

### Port

Firewall port 443 needs to be opened for outbound communication.

## Data types

The following table shows the Databricks data types that are supported when using Qlik Cloud and the default mapping from Qlik Cloud data types.

Native data type information is preserved, and is displayed in the Native data type column in dataset views. If the column is not visible, you need to open the column picker of the data set view and select the Native data type column.

Supported data types

| Qlik Cloud data types | Databricks data types |
| --- | --- |
| BOOLEAN | BOOLEAN |
| BYTES | VARCHAR (Length in Bytes) |
| DATE | DATE |
| TIME | STRING |
| DATETIME | TIMESTAMP  Precision is always 6, even if the input column uses a precision lower than 6.  If the input column uses a precision higher than 6, you can preserve the full precision, consider converting the column to another supported type, such as STRING. |
| INT1 | TINYINT |
| INT2 | SMALLINT |
| INT4 | INT |
| INT8 | BIGINT |
| NUMERIC | DECIMAL (precision, scale) |
| REAL4 | FLOAT |
| REAL8 | DOUBLE |
| UINT1 | SMALLINT |
| UINT2 | INT |
| UINT4 | BIGINT |
| UINT8 | DECIMAL (20, 0) |
| STRING | VARCHAR (length in Bytes)  When the column has a JSON subtype and the Databricks Runtime version is 15.4 LTS or later, then: VARIANT |
| WSTRING | VARCHAR (length in Bytes)  When the column has a JSON subtype and the Databricks Runtime version is 15.4 LTS or later, then: VARIANT |
| NCLOB | STRING  When the column has a JSON subtype and the Databricks Runtime version is 15.4 LTS or later, then: VARIANT |
| CLOB | STRING  When the column has a JSON subtype and the Databricks Runtime version is 15.4 LTS or later, then: VARIANT |
| BLOB | STRING |
| JSON | VARIANT  Information noteThe VARIANT data type is supported as Public Preview in Databricks. |

The following data types are converted to STRING(255):

- MAP
- ARRAY
- STRUCT

## Limitations and considerations

- When using Databricks on AWS with tables without a primary key, reloading the tables in the landing will fail in the Storage app. To resolve this you can either

  - Define a primary key in the tables.
  - Set spark.databricks.delta.alterTable.rename.enabledOnAWS to True in Databricks.
  - When creating a SQL-based transformation, all VARCHAR fields are returned as STRING(255).
- If a primary key is based on a nullable column, it will not be created in Databricks.
