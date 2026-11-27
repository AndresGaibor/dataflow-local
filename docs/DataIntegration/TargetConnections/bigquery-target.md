---
title: "Google BigQuery"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/bigquery-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to data warehouses"]
---

# Google BigQuery

You can use Google BigQuery as a target data platform in a data pipeline or in a replication task. In a data pipeline, various ELT operations can be performed on the target platform including storing data, transforming data, creating data marts, and registering data. A replication task, on the other hand, involves replication of data directly from a source system to a target system with basic transformation capabilities, but without support for ELT operations.

Setting up Google BigQuery as a target involves:

- [Fulfilling the prerequisites](#Prerequi2)
- Configuring a connection to Google BigQuery

## Configuring a connection to Google BigQuery

To configure the connector, do the following:

1. In Connections, click Create connection.
2. Select the Google BigQuery  target connector and then provide the following settings:

### Data target

#### Data gateway

Information noteThis field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.

A Data Movement gateway is only required if the target database is not accessible from Qlik Cloud and can only be accessed using a Private Link (for instance, if it's located in a Virtual Private Cloud). If this is the case, select the Data Movement gateway through which you want to access the target database.

Depending on your use case, this will either be the same Data Movement gateway deployed to move data from the data source, or a different one.

For information about Data Movement gateway use cases, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top) and [*Common use cases*](../../Gateways/replication-gateway.htm#Common).

If the target database is directly accessible from Qlik Cloud, select None.

Information noteWhen accessing the target database via Data Movement gateway, you also need to install the appropriate driver on the Data Movement gateway machine. For details, see [*Google BigQuery*](#Driver) below.

### Connection properties

Service account key: Upload the JSON file that was downloaded when you created your BigQuery service account key.

Location: Where to upload the dataset created by Qlik. If you select Other, enter the region name in the Region name field. For a list of supported region names, see [BigQuery locations](https://cloud.google.com/bigquery/docs/locations).

Information noteSelecting Other requires Data Movement gateway 2023.11.4 or later.

### Name

The display name for the connection.

## Prerequisites

### Permissions required for landing data

Permissions required to create the target dataset automatically:

If you want the dataset to be created automatically, the following permissions are required:

BigQuery > BigQuery Job User

BigQuery > BigQuery Data Editor

Permissions required when the target dataset already exists:

If the dataset already exists, you need to perform the following steps:

1. Create a service account with the following permission:

   BigQuery > BigQuery Job User
2. Navigate to the dataset that you want to use, and then:

   1. Add the service account you just created as a principal.
   2. Assign the BigQuery Data Editor role.

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

   ./install gbq

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will be displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the install gbq command again.

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

   ./update gbq

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the update gbq command again.

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

   ./uninstall gbq

   The driver will be uninstalled.

#### Installing the driver manually

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

You need to install both the ODBC driver and the JDBC driver.

Installing the ODBC driver

After Data Movement gateway is installed, download the SimbaODBCDriverforGoogleBigQuery\_<version>-Linux.tar.gz and google-cloud-sdk-<version>-linux-x86\_64.tar.gz files. You can find direct download links for these files under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/gbq.yaml. Once the download completes, copy the files to the Data Movement gateway machine.

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

The status should be as follows:

Active: inactive (dead) since <timestamp> ago

3. Extract:

   SimbaODBCDriverforGoogleBigQuery\_<version>.tar.gz

   to:

   /opt/SimbaODBCDriverforGoogleBigQuery\_<version>-Linux
4. Move the files GoogleBigQueryODBC.did and simba.googlebigqueryodbc.ini to the lib directory under the Simba ODBC driver directory.

   Example:

   Move the files from:

   /opt/SimbaODBCDriverforGoogleBigQuery\_<version>-Linux/setup

   to:

   /opt/SimbaODBCDriverforGoogleBigQuery\_<version>-Linux/SimbaODBCDriverforGoogleBigQuery64\_<version>/lib
5. Edit the simba.googlebigqueryodbc.ini file as follows:

   1. Change the `ErrorMessagesPath` to the path of the XML file containing the ODBC messages. The default location is:

      `ErrorMessagesPath=/opt/SimbaODBCDriverforGoogleBigQuery_<version>-Linux/SimbaODBCDriverforGoogleBigQuery64_<version>/ErrorMessages`
   2. Change the `DriverManagerEncoding` to `UTF-16`.
6. Add the following path to the site\_arep\_login.sh file located in the Data Movement gateway bin directory:

   export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/opt/SimbaODBCDriverforGoogleBigQuery\_<version>-Linux/SimbaODBCDriverforGoogleBigQuery64\_<version>/lib
7. Edit the /etc/odbcinst.ini file and add the driver path (i.e. the path where the driver is installed):

   `[ODBC Drivers]`

   `Simba= Installed`

   `Simba ODBC Driver for Google BigQuery = Installed`

   `[Simba ODBC Driver for Google BigQuery]`

   `Description=Simba ODBC Driver for Google BigQuery(64-bit)`

   `Driver=/opt/SimbaODBCDriverforGoogleBigQuery_<version>-Linux/SimbaODBCDriverforGoogleBigQuery64_<version>/lib/libgooglebigqueryodbc_sb64.so`
8. Install google-cloud-sdk-<version>-linux-x86\_64.tar.gz.
9. Start the Data Movement gateway service:

   sudo systemctl start repagent
10. Optionally, confirm that the service has started:

    sudo systemctl status repagent

    The status should be as follows:

    Active: active (running) since <timestamp> ago

Installing the JDBC driver and its dependencies

1. Download the following ZIP file and JAR files listed under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/gbq.yaml:

   - https://repo1.maven.org/maven2/com/google/cloud/google-cloud-bigquery/<version>/google-cloud-bigquery-<version>.jar
   - https://repo1.maven.org/maven2/com/google/cloud/google-cloud-storage/<version>/google-cloud-storage-<version>.jar
   - https://storage.googleapis.com/simba-bq-release/jdbc/SimbaJDBCDriverforGoogleBigQuery<version>.zip

   Copy the JAR files to the following folder on the Data Movement gateway machine and extract the JAR files in SimbaJDBCDriverforGoogleBigQuery<version>.zip to the same folder:

   /opt/qlik/gateway/movement/qcs\_agents/qdi-db-commands/lib
2. Restart the Data Movement gateway service by running the command described in [*Restarting the service*](../../Gateways/dm-gateway-managing.htm#Restarti2)

### Port

Firewall port 443 needs to be opened for outbound communication.

## Data types

Parametrized data type length will be set with default values:

- STRING: 8192 (length)
- BYTES: 8192 (length)
- NUMERIC: Precision: 38, Scale: 9
- BIGDECIMAL: Precision: 76, Scale: 38

The following table shows the Google BigQuery data types that are supported when using Qlik Cloud and the default mapping from Qlik Cloud data types.

Native data type information is preserved, and is displayed in the Native data type column in dataset views. If the column is not visible, you need to open the column picker of the data set view and select the Native data type column.

Supported data types

| Qlik Cloud data types | Google BigQuery data types |
| --- | --- |
| BOOLEAN | BOOL |
| BYTES | BYTES (length in Bytes) |
| DATE | DATE |
| TIME | TIME |
| DATETIME | TIMESTAMP  If scale > 7: STRING(37)  Otherwise, precision is always 6, even if the input column uses a precision lower than 6. |
| INT1 | TINYINT |
| INT2 | SMALLINT |
| INT4 | INTEGER |
| INT8 | BIGINT |
| NUMERIC | NUMERIC (precision, scale) |
| REAL4 | FLOAT64 |
| REAL8 | FLOAT64 |
| UINT1 | TINYINT |
| UINT2 | SMALLINT |
| UINT4 | INTEGER |
| UINT8 | BIGINT |
| STRING | STRING  If subtype is JSON, then:  JSON |
| WSTRING | STRING  If subtype is JSON, then:  JSON |
| BLOB | BYTES |
| NCLOB | STRING  If subtype is JSON, then:  JSON |
| CLOB | STRING  If subtype is JSON, then:  JSON |
| ARRAY | STRING |
| STRUCT | STRING |
| GEOGRAPHY | STRING |
| JSON | JSON |

## Limitations and considerations for all data tasks

- Capturing changes from source tables without a Primary Key or Unique Index is not supported. If you need to capture changes from such tables, you can add a Primary Key using a transformation. Additionally, Primary Key or Unique Index columns cannot contain NULLs. If you are aware that such columns will be populated with NULL values, define a transformation to change the NULLs to non-nullable values.
- JSON fields are not supported as primary keys.

## Limitations and considerations for replication tasks only

- The Transactional Apply changes mode is not supported.
- With the following task settings configuration, the replication task will perform a DELETE operation followed by an INSERT instead of an UPDATE:

  - Apply changes mode is set to Batch optimized.
  - The Apply changes using SQL MERGE option is not selected.
  - UPDATEs error handling for Apply Conflicts is set to: No record found for applying an UPDATE: INSERT the missing target record.

  As Google Cloud BigQuery does not support rollback, in the event that the replication task is unable to insert the updated row, the data will be deleted from the target.
