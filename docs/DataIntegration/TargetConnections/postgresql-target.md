---
title: "PostgreSQL"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/postgresql-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to databases"]
---

# PostgreSQL

This section explains how to configure connectivity to a PostgreSQL target using the PostgreSQL target connector. PostgreSQL can be used as a target in a replication task only. Before you can connect to a PostgreSQL target you need to configure the [*Required permissions*](#Permissi) on the database. If you are connecting to PostgreSQL via Data Movement gateway, you also need to install the driver as described in [*Driver setup*](#Driver).

For information about the limitations and considerations when using the PostgreSQL connector, see [*Limitations and considerations*](#Limitati).

## Setting connection properties

To configure the connector, do the following:

1. In Connections, click Create connection.
2. Select the PostgreSQL target connector and then provide the following settings:

### Data target

- Data gateway: When working with Data Movement gateway, select the data gateway that will be used to test the connection to the PostgreSQL target. This should be the same gateway that was used to access the data source.

  Information note
  - This field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.
  - You also need to install the appropriate driver on the Data Movement gateway machine. For details, see [*Driver setup*](#Driver) below.
- Cloud provider: Choose one of the following as appropriate:

  - None - Select when working with:

    - PostgreSQL on-premises
    - Amazon Aurora
    - Azure Database for PostgreSQL - Flexible Server
    - No Data Movement gateway
  - Amazon RDS

    For Amazon RDS for PostgreSQL.
  - Google Cloud - Select when working with:

    - Google Cloud SQL for PostgreSQL
    - Google Cloud AlloyDB for PostgreSQL
  - Microsoft Azure

    For Microsoft Azure Database for PostgreSQL.
- Host: The host name or IP address of the computer on which the PostgreSQL database is installed.
- Port: The port to use when connecting to the database. The default is 5432.

### Account properties

User Name and Password: The user name and password of a user authorized to access the PostgreSQL Server database.

### Database properties

- Database name: There are two methods you can use to specify a database:

  - Method 1 - Select from a list: Click Load databases and then select a database.
  - Method 2 - Manually: Select Enter database name manually and then enter the database name.
- SSL Mode:
  Select one of the following:
  - disable - Connect with a surname and password only.
  - allow - Establish an encrypted connection if requested by the server.
  - prefer
    - This is the default. Establishes an encrypted connection if the server supports encrypted connections, falling back to an unencrypted connection if an encrypted connection cannot be established.
  - require - Establishes an encrypted connection if the server supports encrypted connections. The connection attempt fails if an encrypted connection cannot be established.
  - verify-ca - Similar to Required, but also verifies the server Certificate Authority (CA) certificate against the configured CA certificates. The connection attempt fails if no valid matching CA certificates are found.
  - verify-full - Similar to Verify CA, but also performs host name identity verification by checking the host name the client (i.e. Qlik Talend Data Integration) uses for connecting to the server against the identity in the certificate that the server sends to the client. The client checks whether the host name that it uses for connecting matches the Common Name value in the server certificate.
    The connection fails if there is a mismatch.
- Trusted certificate: The Certificate Authority (CA) that issued the client certificate file in PEM format.
- Client certificate: Upload the client certificate requested by the server.
- Client certificate key: The client private key file in PEM format.
- CRL: The CRL certificate. This file contains certificates revoked by certificate authorities. If the server certificate appears in this list, the connection will fail.
- SSL compression: Select this option to compress the data before it is encrypted.
- Max file size (KB): Select or type the maximum size (in KB) of a CSV file before it is loaded into the PostgreSQL target database. The default value is 32000 KB.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the connection.

## Prerequisites

### Required permissions

The user specified in the connector settings must be a registered user in the PostgreSQL database.

In addition, the following privileges must be granted:

- Can login
- Create databases

  Information noteIf the target schema already exists in the database, the "Create databases" privilege is not required.

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

   ./install postgres

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will be displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the install postgres command again.

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

   ./update postgres

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the update postgres command again.

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

   ./uninstall postgres

   The driver will be uninstalled.

#### Installing the drivers and libraries manually

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

After Data Movement gateway is installed, download the following RPM files. You can find direct download links for the files under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/postgres.yaml. Once the download completes, copy the files to the Data Movement gateway machine.

When Data Movement gateway is installed on Red Hat 9.x:

- postgresql<version>-libs-<version>PGDG.rhel9.x86\_64.rpm
- postgresql<version>-<version>PGDG.rhel9.x86\_64.rpm
- postgresql<version>-odbc-<version>PGDG.rhel9.x86\_64.

When Data Movement gateway is installed on Red Hat 8.x:

- postgresql<version>-libs-<version>PGDG.rhel8.x86\_64.rpm
- postgresql<version>-<version>PGDG.rhel8.x86\_64.rpm
- postgresql<version>-odbc-<version>PGDG.rhel8.x86\_64.rpm

On the Data Movement gateway server,
open a shell prompt and do the following:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
3. Install the RPM files.
4. Change the working directory to <Data Movement gateway-Install-Dir>/bin.
5. Copy the driver location to the site\_arep\_login.sh file, as follows:

   echo "export LD\_LIBRARY\_PATH=\$LD\_LIBRARY\_PATH:/usr/lib:/usr/lib64:/usr/pgsql-<version>/lib" >> site\_arep\_login.sh

   This will add the driver to "LD\_LIBRARY\_PATH" and update the driver location in the site\_arep\_login.sh file.
6. Optionally, confirm that the driver location was copied:

   `cat site_arep_login.sh`
7. Makes sure that the /etc/odbcinst.ini file contains an entry for PostgreSQL, as in the following example:

   [PostgreSQL]

   Description = PostgreSQL ODBC driver

   Driver = /usr/pgsql-13/lib/psqlodbc.so

   Setup = /usr/pgsql-13/lib/psqlodbcw.so

   UsageCount = 1
8. Start the Data Movement gateway service:

   sudo systemctl start repagent
9. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

## Limitations and considerations

The following limitations apply when using PostgreSQL as a replication target:

- UPDATE and DELETE operations on tables without a Primary Key/Unique Index that contain duplicate records is not supported. Any changes to these tables will affect all the records in the target.
- Tables with a LOB column in the key are not supported in Batch Optimized Apply mode. When a VARBINARY column is used as a source table key, a BYTEA column will be created in the target. This causes unpredictable behavior in Batch Optimized Apply mode. As a workaround, we suggest using the SQLite HEX function to convert VARBINARY to VARCHAR.

## Data types

Native data type information is preserved, and is displayed in the Native data type column in dataset views. If the column is not visible, you need to open the column picker of the data set view and select the Native data type column.

Warning noteWhen moving from a source table with columns that map to BYTEA on the PostgreSQL target, make sure the Replicate LOB columns option is enabled [in the task settings](../Replicating/replicating-settings.htm#LOB) (the default).

Data types

| Qlik Cloud Data Types | PostgreSQL data types |
| --- | --- |
| BOOL | BOOL |
| BYTES | BYTEA |
| DATE | DATE |
| TIME | TIME |
| DATETIME | If scale is => 0 and =< 6, then:  TIMESTAMP  If scale is => 7 and =< 12, then:  VARCHAR (37) |
| INT1 | SMALLINT |
| INT2 | SMALLINT |
| INT4 | INTEGER |
| INT8 | BIGINT |
| NUMERIC | DECIMAL (P, S) |
| REAL4 | FLOAT4 |
| REAL8 | FLOAT8 |
| STRING | If length is 1 - 21845, then:  VARCHAR (Length in Bytes = The STRING value multiplied by three)  If length is 21846 - 2147483647, then:  VARCHAR (65535) |
| UINT1 | SMALLINT |
| UINT2 | INTEGER |
| UINT4 | BIGINT |
| UINT8 | BIGINT |
| WSTRING | If length is 1 - 21845, then:  VARCHAR (Length in Bytes = The WSTRING value multiplied by three)  If length is 21846 - 2147483647, then:  VARCHAR (65535) |
| BLOB | BYTEA |
| NCLOB | TEXT |
| CLOB | TEXT |

### Data types when replicating from a PostgreSQL source

When replicating from a PostgreSQL source, the target table will be created with the same data types for all columns, apart from columns with user-defined or PostGIS data types. In such cases, the data type will be created as "character varying" in the target.
