---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA/prereq_saphana.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA (Database)"]
---

# Prerequisites

Before you can land or replicate data, make sure to complete the following prerequisites:

- Install the required driver on the Data Movement gateway server

  Information note

  This is only required if you opted to work with Data Movement gateway. For information on the benefits of Data Movement gateway and when it is required, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Grant the required permissions on the data source
- Configure the data source connector

## Driver setup

You can install the driver using the driver installation utility (recommended) or manually. Manual installation should only be attempted in the unlikely event that you encounter an issue with the driver installation utility.

### Using the driver installation utility to install the driver

This section describes how to install the required driver. The process involves downloading the driver, copying it to the required folder (see below), and running a script that will automatically install and configure it. You can also run scripts to update and uninstall the driver as needed.

### Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version
- Download SAP HANA ODBC 64-bit Driver 2.0.19 to 2.12 for Linux from the [SAP Software Download Center](https://support.sap.com/en/my-support/software-downloads.html)
  and copy the files IMDB\_CLIENT\_<version number>.SAR and SAPCAR\_<version number>.EXE to:

  /opt/qlik/gateway/movement/drivers/saphana

### Installing the driver

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

   ./install saphana

The driver will be installed.

5. Wait for the installation to complete (indicated by "Complete!") and then start the Data Movement gateway service:

   sudo systemctl start repagent
6. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Updating the driver

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

   ./update saphana

The old driver will be uninstalled and the new driver will be installed.

5. Wait for the installation to complete (indicated by "Complete!") and then start the Data Movement gateway service:

   sudo systemctl start repagent
6. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Uninstalling the driver

Run the uninstall command if you want to uninstall the driver.

To uninstall the driver:

1. Stop all tasks configured to use this connector.
2. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
3. Run the following command:

   Syntax:

   ./uninstall saphana

   The driver will be uninstalled.

### Installing the driver manually

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

Download SAP HANA ODBC 64-bit Driver 2.0.19-2.12 from the [SAP Software Download Center](https://support.sap.com/en/my-support/software-downloads.html).
You must have an account with SAP to download the software.

Information note

SAP HANA ODBC driver 2.13 and later are not supported.

Example driver name: HDBODBC

Then on the Data Movement gateway machine,
open a shell prompt and do the following:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
3. Install the driver on the Data Movement gateway machine.
4. Add the following section to the odbcinst.ini file located in directory /etc:

   [HDBODBC]

   Description=64-bit HANA ODBC Driver

   Driver=/opt/sap/hdbclient/libodbcHDB.so

   fileUsage=1
5. Start the Data Movement gateway service:

   sudo systemctl start repagent
6. Optionally confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Connecting using SSL

To connect to SAP HANA using SSL, the client must be configured to authenticate the SSL server certificate.

- For server authentication, follow the instructions in [Server Certificate Authentication.](https://help.sap.com/docs/SAP_HANA_CLIENT/f1b440ded6144a54ada97ff95dac7adf/a95754380f4c4c05b728524f9cd652e3.html)
- For mutual authentication, follow the instructions in [Implement Mutual Authentication](https://help.sap.com/docs/SAP_HANA_CLIENT/f1b440ded6144a54ada97ff95dac7adf/02f21560bbc1495483373d266f7e1fc7.html). When using OpenSSL as your crypto provider, you must complete the configuration by doing the extra steps for OpenSSL under Crypto Provider.

## Port

On the Data Movement gateway machine, open inbound port number 3xx15 to the SAP HANA server where xx is the instance number of the SAP HANA database that contains the source tables.

For example, the port for instance 90 would be 39015.

## Capturing data changes

When landing data using the SAP Hana (Database) connector, the following artifacts are automatically created in the source database:

- Three triggers for each of the source tables being landed: The triggers capture changes to the source tables (INSERTs, UPDATEs, and DELETEs) and write them to the attrep\_cdc\_changes\_cts table (described below). A separate trigger is created for each DML operation. The triggers are created in the source table schema.
- attrep\_cdc\_changes\_cts: This table contains changes captured by the triggers. The table will be created in the schema specified in the Create CDC table in schema field of the SAP HANA (Database) connector.

Information noteWhile there is no setup required from a user's perspective, the triggers are a prerequisite for capturing changes, which is why they are described in this topic.

See also: [*Permissions*](security_req_saphana.htm)
