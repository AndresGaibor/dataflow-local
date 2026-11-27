---
title: "Snowflake"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/snowflake-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to data warehouses"]
---

# Snowflake

You can use Snowflake as a target data platform in a data pipeline or in a replication task. In a data pipeline, various ELT operations can be performed on the target platform including storing data, transforming data, creating data marts, and registering data. A replication task, on the other hand, involves replication of data directly from a source system to a target system with basic transformation capabilities, but without support for ELT operations.

Setting up Snowflake as a target involves:

- Configuring the [*Required permissions*](#Permissi) on the database.
- Installing the [required driver](#Driver). Note that this is only required if you are connecting to Snowflake via Data Movement gateway.
- Configuring a connection to Snowflake

## Setting connection properties

To configure the connector, do the following:

1. In Connections, click Create connection.
2. Select the Snowflake  target connector and then provide the following settings:

### Data target

#### Data gateway

Information noteThis field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.

A Data Movement gateway is only required if the target database is not accessible from Qlik Cloud and can only be accessed using a Private Link (for instance, if it's located in a Virtual Private Cloud). If this is the case, select the Data Movement gateway through which you want to access the target database.

Depending on your use case, this will either be the same Data Movement gateway deployed to move data from the data source, or a different one.

For information about Data Movement gateway use cases, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top) and [*Common use cases*](../../Gateways/replication-gateway.htm#Common).

If the target database is directly accessible from Qlik Cloud, select None.

Information noteWhen accessing the target database via Data Movement gateway, you also need to install the appropriate driver on the Data Movement gateway machine. For details, see [*Driver setup*](#Driver) below.

### Connection properties

- Server: Your URL for accessing Snowflake. For example, myaccount.snowflakecomputing.com.
- Port: The port through which you want to access your Snowflake database. The default is 443.

### Authentication

Choose an authentication method:

- Username and password

  Information noteWhen this method is selected, the Snowpipe Streaming loading method in the task settings' General tab is not supported.
- Key Pair

  Your Snowflake database must be configured to use key pair authentication. The process is described in [Configuring Key Pair Authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth.html#configuring-key-pair-authentication).

  Information noteIf you use Data Movement gateway, version 2024.5.14 or higher is required to use key pair authentication.

### Account properties

#### Username and password

User Name and Password: The user name and password of a user authorized to access the Snowflake database.

#### Key Pair

Key pair properties

| Account property | Description |
| --- | --- |
| User | User in Snowflake. |
| Private Key File | Click Browse to select your private key file. |
| Private Key File Password | The password to decrypt your private key if it is encrypted. |

### Database properties

- Default Warehouse: The name of your Snowflake warehouse. You can override this in your project settings.
- Database name: There are two methods you can use to specify a database:

  - Method 1 - Select from a list: Click Load databases and then select a database.
  - Method 2 - Manually: Select Enter database name manually and then enter the database name.

### Additional connection properties

You can specify additional ODBC and JDBC connection properties as required. Properties that are relevant for both ODBC and JDBC connections - for example, "Role" - should be added to both.

Information note

- If you are using Data Movement gateway, Additional connection properties are supported from version 2024.5.54.
- Secure properties (for example, encryption keys) are not supported.
- Do not add properties that have dedicated fields in the connection settings.

#### ODBC properties

You can specify additional connection properties that will be used by data movement tasks (Landing, Replication, and Landing in a data lake) when connecting via an ODBC driver.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

#### JDBC properties

You can specify additional connection properties that will be used by ELT tasks (Register, Storage, Transform, and Data marts) when connecting via a JDBC driver.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the connection.

## Prerequisites

### Required permissions

The following permissions are required:

Permissions required if you want schemas that do not exist to be created automatically

- USAGE ON DATABASE
- CREATE SCHEMA ON DATABASE

Permissions required if the schema already exists

- USAGE ON DATABASE
- USAGE ON SCHEMA
- CREATE FILE FORMAT ON SCHEMA
- CREATE STAGE ON SCHEMA
- CREATE TABLE ON SCHEMA

### Driver setup

A driver is only required if you are accessing the database via Data Movement gateway.

You can install the driver using the driver installation utility (recommended) or manually. Manual installation should only be attempted in the unlikely event that you encounter an issue with the driver installation utility.

#### Using the driver installation utility to install the driver

This section describes how to install the required driver. The process involves downloading the driver, copying it to the required folder (see below), and running a script that will automatically install and configure it. You can also run scripts to update and uninstall the driver as needed.

Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version
- Download the Snowflake ODBC driver "snowflake-odbc-<version>.x86\_64.rpm". You can find a direct download link for the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/snowflake.yaml. Once the download completes, copy the file to:

  /opt/qlik/gateway/movement/drivers/snowflake

Installing the driver

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

   ./install snowflake

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

   ./update snowflake

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

   ./uninstall snowflake

   The driver will be uninstalled.

#### Manually installing the driver

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

You need to install both an ODBC driver and a JDBC driver.

Installing the ODBC driver

1. After Data Movement gateway is installed, download the snowflake-odbc-<version>x86\_64.rpm driver file listed under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/snowflake.yaml, and copy it to the Data Movement gateway machine.
2. Install the driver on the Data Movement gateway machine.

Installing the JDBC driver

1. Download the snowflake-jdbc-<version>.jar file listed under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/snowflake.yaml, and copy it to the following folder on the Data Movement gateway machine:

   /opt/qlik/gateway/movement/qcs\_agents/qdi-db-commands/lib
2. Restart the Data Movement gateway service and check that it has started by running the commands described in [*Data Movement gateway service commands*](../../Gateways/dm-gateway-managing.htm#Restarti)

### Port

Firewall port 443 needs to be opened for outbound communication.

## Limitations and considerations

The following limitations apply when moving data to a Snowflake target:

- Replication of tables with backslashes in their names (e.g. SPECIAL\\TABLE\N) is not supported.

### Limitations and considerations when using the Snowpipe Streaming loading method

- When using Snowpipe Streaming as the loading method, the following limitations apply:
  - For landing tasks only:

    - As Snowpipe only supports INSERT operations, the Reload and compare update method is not supported.
  - For replications tasks only:

    - As Snowpipe only supports INSERT operations, the Apply changes replication mode is not supported.
    - Stopping Store Changes replication during a transaction and resuming it after 30 days or more might cause duplicate records on target. Snowflake automatically deletes channels after 30 days.
  - For both landing and replications tasks:

    - Username and password authentication is not supported.
    - The XML subtype is not supported.

## Data types

The following table shows the Snowflake data types that are supported when using Qlik Cloud and the default mapping from Qlik Cloud data types.

Native data type information is preserved, and is displayed in the Native data type column in dataset views. If the column is not visible, you need to open the column picker of the data set view and select the Native data type column.

Supported data types

| Qlik Cloud data types | Snowflake data types |
| --- | --- |
| BOOLEAN | BOOLEAN |
| BYTES | BINARY (length in Bytes) |
| DATE | DATE |
| TIME | TIME (precision) |
| DATETIME | Snowflake:   - TIMESTAMP   For Snowflake Iceberg :   - TIMESTAMP - If scale > 7: STRING(37) |
| INT1 | BYTEINT |
| INT2 | SMALLINT |
| INT4 | INTEGER |
| INT8 | BIGINT |
| NUMERIC | NUMBER (precision, scale) |
| REAL4 | FLOAT4 |
| REAL8 | FLOAT8 |
| UINT1 | BYTEINT |
| UINT2 | INTEGER |
| UINT4 | INTEGER |
| UINT8 | BIGINT |
| STRING | VARCHAR (length in Bytes) |
| WSTRING | NVARCHAR (length in Bytes) |
| BLOB | BINARY (8388608) |
| NCLOB | NVARCHAR (8388608) |
| CLOB | VARCHAR (8388608) |
| JSON | VARIANT |

In Snowflake, all VARCHAR columns store UTF-8 characters. If the data loaded into a VARCHAR column exceeds its maximum length of 128 MB, the following error will occur:

```
        RetCode: SQL_ERROR  SqlState: 22000 NativeError: 100078 Message: String '{"col1": null, "col2": null, "col3": null, "col4' is too long and would be truncated
```

When working with array, object, or TIMESTAMP\_TZ data types in Snowflake, you must convert them to BINARY if:

- You have a registered data task with one of these types, and then a task that stores tables in Iceberg format.
- You have an Iceberg task with one of these types, and then a task without Iceberg.
