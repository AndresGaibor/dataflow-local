---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/prereq-postgresql-source-dmgateway.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "PostgreSQL"]
---

# Prerequisites

Before you can land or replicate data, make sure to complete the following prerequisites:

- Install the required driver on the Data Movement gateway server

  Information note

  This is only required if you opted to work with Data Movement gateway. For information on the benefits of Data Movement gateway and when it is required, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).

  Note that Data Movement gateway is not available with the Qlik Talend Cloud Starter subscription.
- Grant the required permissions on the data source
- Configure the data source connector

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

### Updating the driver

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

### Uninstalling the driver

Run the uninstall command if you want to uninstall the driver.

To uninstall the driver:

1. Stop all tasks configured to use this connector.
2. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
3. Run the following command:

   Syntax:

   ./uninstall postgres

   The driver will be uninstalled.

### Installing the driver manually

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

## Port

By default, port 5432 needs to be opened for outbound communication on the Data Movement gateway server. You can change this in the connector settings.

## Capturing changes from a customer-installed PostgreSQL database

- The IP address of the Data Movement gateway machine must be added to the pg\_hba.conf
  configuration file with the "replication" keyword in the database field.

  Example:

  host replication all 176.123.1.212/32 trust
- Make sure that the test\_decoding output plugin (found in the postgresql12-contrib package) is installed.
- The user specified in the connection settings must be granted read-write permissions to the source database to allow the creation of "slots" on the database. The slots are required in order to read the changes.
- The following parameters and values must be set in the postgresql.conf configuration file.

  wal\_level = logical

  max\_replication\_slots = number of replication slots

  Where number of replication slots must be greater than one and should be set according to the number of tasks that you want to run. For example, to run five tasks you need to set max\_replication\_slots = 5. Slots open automatically as soon as a task starts and remain open, even when task is no longer running. Note that open slots need to be manually deleted.

  max\_wal\_senders = number of concurrent tasks

  Where number of concurrent tasks must be greater than one and should be set according to the number of tasks that you are running concurrently. For example, to run three tasks concurrently you need to set max\_wal\_senders = 3.
- The wal\_sender\_timeout parameter terminates connections that are inactive longer than the specified number of milliseconds. The default timeout is 60 seconds. To disable the timeout mechanism (optional), set this parameter to zero.

  Information note

  By default, the value of the wal\_sender\_timeout parameter is interpreted by the server as milliseconds. To explicitly specify seconds, append an "s" to the value as in the following example:

  wal\_sender\_timeout=60s

For more information on the configuration parameters, see the Replication section under Server Configuration in the [PostgreSQL online help](https://www.postgresql.org/docs/).

## Capturing changes from Amazon RDS for PostgreSQL

You can use the AWS master user account for the PostgreSQL database instance as the user for the Amazon RDS for PostgreSQL source endpoint. The master user account has the required roles that allow it to set up Change Data Capture (CDC).

If you prefer not to use the master user account, the account you wish to use must have the rds\_superuser role and the rds\_replication role. The rds\_replication role grants permissions to manage logical slots and to stream data using logical slots.

To enable logical replication for an Amazon RDS PostgreSQL database instance:

1. Create a new parameter group with the following configuration:
   1. Set the rds.logical\_replication parameter in the database parameter group to 1.
   2. max\_wal\_senders – The number of tasks that can run in parallel.
   3. max\_replication\_slots – Every connection (i.e. task) creates a new slot; this parameter configures the amount of simultaneous connections that can be established to the database.
2. Link the Amazon RDS instance to the parameter group.

## Capturing changes from Microsoft Azure for PostgreSQL

To be able to capture changes from Microsoft Azure for PostgreSQL, you need to set the "replication" property to "logical", as described in the steps below.

1. Open the Azure CLI and run the following command:

   Information note

   You can download the CLI or connect via a shell command on Azure portal.

   Syntax:

   az postgres server configuration set --resource-group resource-group --server-name server-name --name azure.replication\_support --value logical

   Example:

   az postgres server configuration set --resource-group azuredb --server-name qlik-azure-pg --name azure.replication\_support --value logical
2. Restart the database (using the command line or via the portal).

## Capturing changes from Google Cloud SQL for PostgreSQL

Information noteThis functionality requires Data Movement gateway 2022.11.42 or later.

To be able to capture changes from the database, you need to set up logical replication.

To set up logical replication:

1. On Google Cloud platform, set the following flags in the PostgreSQL settings:

   - cloudsql.logical\_decoding=on
   - max\_replication\_slots: Every connection (that is, task) creates a new slot; this parameter configures the amount of simultaneous connections that can be established to the database. If you encounter performance issues, increasing this value might help.
   - max\_wal\_senders: The number of tasks that can run in parallel. If you encounter performance issues, increasing this value might help.

   For more information on these parameters, see <https://www.postgresql.org/docs/current/runtime-config-replication.html>
2. On the database, alter the user specified in the connector settings (*username*) to support replication:

   ALTER USER username WITH REPLICATION;
