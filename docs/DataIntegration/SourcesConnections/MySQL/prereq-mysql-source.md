---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/prereq-mysql-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "MySQL"]
---

# Prerequisites

Before you can land or replicate data, make sure to complete the following prerequisites:

- Install the required driver on the Data Movement gateway server

  Information note

  This is only required if you opted to work with Data Movement gateway. For information on the benefits of Data Movement gateway and when it is required, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).

  Note that Data Movement gateway is not available with the Qlik Talend Cloud Starter subscription.
- Grant the required permissions on the data source
- Configure the data source connector

## Supported editions

The following MySQL editions are supported:

- MySQL Community Edition
- MySQL Standard Edition
- MySQL Enterprise Edition
- MySQL Cluster Carrier Grade Edition

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

### Updating the driver

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

### Uninstalling the driver

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

## Port

By default, port 3306 needs to be opened for outbound communication on the Data Movement gateway server. You can change this in the connector settings.

## General prerequisites

Make sure the following prerequisites have been met:

- A MySQL account with the [*Required permissions*](security-req-mysql-source.htm).
- MySQL 8: Standard authentication for capturing changes
- Certified MySQL versions support the fractional value for temporal data types (introduced in MySQL 5.6). Consequently, moving of the old temporal data type format is no longer supported.

  Information noteNote that upgrading to MySQL versions that support the fractional value for temporal data types *does not* upgrade the temporal data type format automatically. This needs to be done separately. This also applies when upgrading from MariaDB 10.1. For instructions on upgrading the temporal data type format, see the vendor's online help.

## Capturing changes from a customer-installed MySQL database

The following section describes the requirements for capturing changes from an on-premises MySQL database.

### Enable binary logging

To enable binary logging (required for CDC moving), the following parameters must be configured in MySQL’s my.ini (Windows) or my.cnf (UNIX) files.

Binary logging parameters

| Parameter | Value |
| --- | --- |
| server\_id | Any value from 1.  Example:  server\_id=1 |
| log-bin=<path> | Path to the binary log file (without an extension).  Example:  log-bin=E:\MySql\_Logs\BinLog |
| binlog\_format | Must be:  binlog\_format=row |
| binlog\_expire\_logs\_seconds | To prevent disk space issues, it is strongly recommended not to use the default value (2592000).  Example (for 5 days):  binlog\_expire\_logs\_seconds=432000 |
| binlog\_row\_image | Must be:  binlog\_row\_image=full |

### Cluster prerequisites

To be able to Move clustered (NDB) tables (by connecting to any of the cluster nodes), the following parameters must be configured in MySQL’s my.ini (Windows) or my.cnf (UNIX) files.

Information note

When using Percona as a source, there is no need to perform the procedures described in this section.

Cluster parameters

| Parameter | Value |
| --- | --- |
| ndb\_log\_bin | Must be:  ndb\_log\_bin=on  Ensures that changes in clustered tables will be logged to the binary log. |
| ndb\_log\_update\_as\_write | Must be:  ndb\_log\_update\_as\_write=OFF  Prevents UPDATEs being written as INSERTs in the binary log. |
| ndb\_log\_updated\_only | Must be:  ndb\_log\_updated\_only=OFF  Ensures that the binary log will contain the entire row and not just the changed columns. |

## Capturing changes from Google Cloud for MySQL

#### Binary logging

Binary logging is required for capturing changes. To check that binary logging is enabled (the default), make sure that the database's `binlog_row_image` parameter is set to `full`.

#### Replication

Replication enables data from the primary database server to be copied to one or more secondary servers.

Data can be landed from either a primary server or a secondary server.

To capture changes from a secondary server, the binary logging parameter `log_slave_updates` needs to be set to `true` (`1`).

Further reading: <https://cloud.google.com/sql/docs/mysql/replication>

## Capturing changes from Amazon RDS for MySQL and Amazon Aurora for MySQL

#### Binary logging

To set up Amazon RDS for MySQL or Amazon Aurora for MySQL for CDC:

1. Follow the instructions in the AWS Help for creating a new Parameter Group (see the Binary Logging Format section).
2. When creating the new Parameter Group, set: `binlog_format=row`
3. Save the new Parameter Group.
4. If you have an existing instance of Amazon RDS for MySQL, edit the instance to use the parameter specified in Step 2 above. If you are provisioning a new instance of Amazon RDS for MySQL, reference the new Parameter Group created in Step 1 above.
5. Finally, make sure that automated backup is enabled (the default).

Further reading: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.BinaryFormat.html>

#### Replication

Replication enables data from the primary database server to be copied to one or more secondary servers.

Data can be landed from either a primary server or a secondary server.

To capture changes from a secondary server, the binary logging parameter `log_slave_updates` needs to be set to `true` (`1`).

Further reading: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.html>

## Capturing changes from Microsoft Azure database for MySQL

Binary logging is required for capturing changes. To check that binary logging is enabled (the default), make sure that the database's `binlog_row_image` parameter is set to `full`.
