---
title: "MySQL"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/mysql-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to databases"]
---

# MySQL

This topic explains how to configure connectivity to a MySQL target using the MySQL target connector. MySQL can be used as a target database in a replication task only. Before you can connect to a MySQL target you need to configure the [*Required permissions*](#Permissi) on the database. If you are connecting to MySQL via Data Movement gateway, you also need to install the driver as described in [*Driver setup*](#Driver).

For information about the limitations and considerations when using the MySQL connector, see [*Limitations and considerations*](#Limitati).

## Setting connection properties

To configure the connector, do the following:

1. In Connections, click Create connection.
2. Select the MySQL target connector and then provide the following settings:

### Data target

- Data gateway: When working with Data Movement gateway, select the data gateway that will be used to test the connection to the MySQL target. This should be the same gateway that was used to access the data source.

  Information note
  - This field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.
  - You also need to install the appropriate driver on the Data Movement gateway machine. For details, see [*Driver setup*](#Driver) below.
- Cloud provider: Choose one of the following as appropriate:

  - None

    - For MySQL on-premises, MariaDB, Amazon Aurora, or Microsoft Azure Database for MySQL - Flexible Server.
    - When working without Data Movement gateway
  - Amazon RDS

    For Amazon RDS for MariaDB or Amazon RDS for MySQL.
  - Google Cloud

    For Google Cloud SQL for MySQL.
  - Microsoft Azure

    For Microsoft Azure Database for MySQL.
- Server: The host name or IP address of the computer on which the MySQL database is installed.
- Port: The port to use when connecting to the database. The default is 3306.

### Account properties

User Name and Password: The user name and password of a user authorized to access the MySQL Server database.

### Database properties

- Target Database Type: Choose one of the following:
  - Specific database: When this option is selected, all source schemas will be loaded into the specified Database.
  - Multiple databases: When this option is selected, each of the source schemas will be loaded into its corresponding database. Additionally, by default, all Control Tables will be replicated to a new schema called attrep\_control. For more information about Control Tables, see [*Control tables*](../Replicating/control_tables.htm).
- Max file size (KB): Select or type the maximum size (in KB) of a CSV file before it is loaded into the MySQL target database. The default value is 32000 KB.
- Parallel load threads: Increasing the number of threads might improve performance when loading data into the MySQL target database. Note that setting a large number of threads may have an adverse effect on database performance since a separate connection is required for each thread.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the connection.

## Prerequisites

### Required permissions

The user specified in the connector settings must be granted:

- MySQL account access
- Read/write privileges in the MySQL database
- The following permissions
  for each target schema involved in the replication:
  - ALTER
  - CREATE
  - CREATE TEMPORARY TABLES
  - DELETE
  - DROP
  - INSERT
  - SELECT
  - UPDATE

### Driver setup

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

   ./install mysql

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will be displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the install mysql command again.

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

   ./update mysql

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the update mysql command again.

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

   ./uninstall mysql

   The driver will be uninstalled.

### Installing the driver manually

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

After Data Movement gateway is installed, download the mysql-connector-odbc-<version>.x86\_64.rpm driver. You can find a direct download link to the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/mysql.yaml. Once the download completes, copy the RPM to the Data Movement gateway machine.

On the Data Movement gateway server,
open a shell prompt and do the following:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
3. Install the driver on the Data Movement gateway machine.
4. Change the working directory to <Data Movement gateway-Install-Dir>/bin.
5. Copy the driver location to the site\_arep\_login.sh file:

   echo "export LD\_LIBRARY\_PATH=\$LD\_LIBRARY\_PATH:/usr/lib64" >> site\_arep\_login.sh

   This will add the driver to "LD\_LIBRARY\_PATH" and update the driver location in the site\_arep\_login.sh file.
6. Optionally, confirm that the driver location was copied:

   `cat site_arep_login.sh`
7. Make sure that the /etc/odbcinst.ini file contains an entry for MySQL, as in the following example:

   `[MySQL ODBC 8.0 Unicode Driver]`

   `Driver = /usr/lib64/libmyodbc8w.so`

   `UsageCount = 1`
8. Start the Data Movement gateway service:

   sudo systemctl start repagent
9. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

## Limitations and considerations

The following limitations apply when using MySQL as a replication target:

- When replicating to the MariaDB target database, if the DATETIME value is set to zero, you need to define a transformation that replaces the DATETIME with valid values. For example:

  replace($datetime\_column,'9999-12-31 23:59:59','2000-01-01 22:00:00')

  Information noteThis limitation does not apply to Microsoft Azure Database for MySQL.
- Due to the way MySQL operates, when loading data to a MySQL target during a Full Load task, duplicate key errors will not be reported to the logs.
- When updating a column's value to its existing value, a zero rows affected is returned from MySQL (unlike Oracle and Microsoft SQL Server that perform an update of one row).

  This generates an entry in the [attrep\_apply\_exceptions Control Table](../Replicating/apply_exceptions.htm) and the following warning:

  Some changes from the source database had no impact when applied to the target database. See attrep\_apply\_exceptions table for details.
- If you need to replicate 4-byte emoji characters, the target schema character set must be set to utf8mb4.
- When a source table contains a large number of columns, MySQL might return a Row size too large (> 8126) error as 8126 bytes is the default maximum row size in MySQL. When using SaaS application sources, this error occurs during runtime. When using other source types such as databases, the error occurs during task preparation. To address this limitation, use either of the following approaches:

  - **Recommended approach:** After the data is ingested. remove the columns you do not need on the target. For information on how to do this, see [*Removing columns*](../Introduction/Managing-datasets.htm#Removing). If you still encounter the error, remove more columns.
  - **Alternative mitigation:** If you need all the source columns to be included in the target table, there are certain MySQL database configurations that will allow this. One of these is increasing the MySQL page size to be large enough to accommodate the row size.

    Information noteFor sources with row sizes exceeding the 65,535-byte limit, you must convert the source field to a data type that supports larger row sizes. This is due to a known limitation on maximum row record size. For more information, see the [MySQL documentation on row size limits](https://dev.mysql.com/doc/refman/8.4/en/column-count-limit.html).

## Data types

Native data type information is preserved, and is displayed in the Native data type column in dataset views. If the column is not visible, you need to open the column picker of the data set view and select the Native data type column.

Supported data types

| Qlik Cloud data types | MySQL data types |
| --- | --- |
| BOOL | BOOL |
| BYTES | If length is => 1 and =< 8095, then:  VARBINARY (Length)  If length is => 8096 and =< 65535, then:  BLOB  If length is => 65536 and =< 16777215, then:  MEDIUMBLOB  If length is => 16777216 and =< 2147483647, then:  LONGBLOB |
| DATE | DATE |
| TIME | TIME |
| DATETIME | If scale is => 0 and =< 6, then:  DECIMAL (p,s)  If scale is => 7 and =< 12, then:  VARCHAR (37) |
| INT1 | TINYINT |
| INT2 | SMALLINT |
| INT4 | INTEGER |
| INT8 | BIGINT |
| NUMERIC | If scale is => 0 and =< 30, then:  DECIMAL (p,s)  If scale is => 31 and =< 100, then:  VARCHAR (45) |
| REAL4 | FLOAT |
| REAL8 | DOUBLE |
| STRING | If length is => 1 and =< 8095, then:  VARCHAR (Length)  If length is => 8096 and =< 65535, then:  TEXT  If length is => 65536 and =< 16777215, then:  MEDIUMTEXT  If length is => 16777216 and =< 2147483647, then:  LONGTEXT |
| UINT1 | UNSIGNED TINYINT |
| UINT2 | UNSIGNED SMALLINT |
| UINT4 | UNSIGNED INTEGER |
| UINT8 | UNSIGNED BIGINT |
| WSTRING | If length is => 1 and =< 8095, then:  VARCHAR (Length)  If length is => 8096 and =< 65535, then:  TEXT  If length is => 65536 and =< 16777215, then:  MEDIUMTEXT  If length is => 16777216 and =< 2147483647, then:  LONGTEXT |
| BLOB | When the Allow unlimited LOB size option is enabled:   - LONGBLOB   When the Limit LOB size to option is enabled:   - If the specified value i is 63 KB or smaller, then:  BLOB  - If the specified value is 64 KB or larger, then:  LONGBLOB   For information on limiting LOB size, see [*Metadata*](../Replicating/replicating-settings-metadata.htm#ar_tasks_custom_1624443382_1693100). |
| NCLOB | When the Allow unlimited LOB size option is enabled:   - TEXT   When the Limit LOB size to option is enabled:   - If the specified value is 63 KB or smaller, then:  TEXT  - If the specified value is 64 KB or larger, then:  LONGTEXT   For information on limiting LOB size, see [*Metadata*](../Replicating/replicating-settings-metadata.htm#ar_tasks_custom_1624443382_1693100). |
| CLOB | When the Allow unlimited LOB size option is enabled:   - TEXT CHARACTER SET UTF-16   When the Limit LOB size to option is enabled:   - If the specified value is 63 KB or smaller, then:  TEXT CHARACTER SET UTF-16  - If the specified value is 64 KB or larger, then:  LONGTEXT CHARACTER SET UTF-16   For information on limiting LOB size, see [*Metadata*](../Replicating/replicating-settings-metadata.htm#ar_tasks_custom_1624443382_1693100). |
