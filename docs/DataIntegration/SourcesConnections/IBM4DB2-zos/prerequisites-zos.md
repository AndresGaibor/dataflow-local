---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-zos/prerequisites-zos.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for z/OS"]
---

# Prerequisites

Before you can land or replicate data, make sure to complete the following prerequisites:

- Install the required driver on the Data Movement gateway server

  Information note

  This is only required if you opted to work with Data Movement gateway. For information on the benefits of Data Movement gateway and when it is required, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Grant the required permissions on the data source
- Configure the data source connector

## Install the R4Z product on z/OS

Before you can work with an IBM DB2 for z/OS source, you must first install and configure the R4Z product on z/OS.

1. Go to [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).
2. Select Qlik Data Integration.
3. In the Product list, select Qlik Replicate.
4. In the Release list, select the Qlik Replicate version that corresponds to the release date (year and month) of your Data Movement gateway version. For example, if your Data Movement gateway version is 2024.5.54 (Year.Month.Build), select May 2024.
5. In the Release Number list, select Initial Release.
6. In the Download Link column, click the QlikReplicate\_<version>\_r4z.zip link to start your download.
7. Once downloaded, install it on your z/OS data source.

For installation and configuration instructions, see [*Installing and configuring R4Z*](../../../../Global_Common/Content/SharedReplicateHDD/R4Z_Install_Config/concept-design.htm).

## Installing and setting up the driver

You can install the driver using the driver installation utility (recommended) or manually. Manual installation should only be attempted in the unlikely event that you encounter an issue with the driver installation utility.

### Using the driver installation utility to install the driver

This section describes how to install the required driver. The process involves downloading the driver, copying it to the required folder (see below), and running a script that will automatically install and configure it. You can also run scripts to update and uninstall the driver as needed.

### Preparing the installation

- Make sure that Python 3.6 or later is installed on the Data Movement gateway server.

  Python comes preinstalled on most Linux distributions. You can check which Python version is installed on your system, by running the following command:

  python3 --version
- Download the IBM Data Server Client "<version>\_linuxx64\_client.tar.gz" from the IBM web site. You can find the supported version under binary-artifacts in /opt/qlik/gateway/movement/drivers/manifests/db2.yaml. Once the download completes, copy the file to:

  /opt/qlik/gateway/movement/drivers/db2

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

   ./install db2

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

   ./update db2

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

### Uninstalling the driver

Run the uninstall command if you want to uninstall the driver.

To uninstall the driver:

1. Stop all tasks configured to use this connector.
2. On the Data Movement gateway machine, change the working directory to:

   opt/qlik/gateway/movement/drivers/bin
3. Run the following command:

   Syntax:

   ./uninstall db2

   The driver will be uninstalled.

### Installing the driver manually

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

#### Linux ODBC client package

You can choose between installing the full ODBC client package or installing just the data server client, as described in [*Linux data server client*](#Linux) below.

Information note

The "enableWLB" driver option is not supported. To force the connection to automatically switch to another LPAR in a parallel sysplex (i.e. “failover”), set “enableACR” to “true” and “enableWLB” to “false” in the driver configuration.

On the Data Movement gateway machine, open a shell prompt and do the following:

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
3. Install v11.5.8\_linuxx64\_server\_dec.tar.gz and choose the “CLIENT” option.
4. If the Data Movement gateway machine does not have a DB2 instance, create a DB2 instance by running the following commands:

   adduser <db2\_instance\_name>

   /opt/ibm/db2/V11.5/instance/db2icrt <db2\_instance\_name>
5. Change the working directory to <Data Movement gateway\_Install\_Dir>/bin.
6. Add the DB2 driver location to the Linux library path.

   To do this, add the following line to the **site\_ arep\_login.sh** file as follows:

   export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/path/lib

   where path is the CLIENT path to the driver.

   **Example (with db2clnt1 as the instance name):**

   export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/home/db2clnt1/sqllib/lib:/home/db2clnt1/sqllib/lib64/gskit

   export DB2INSTANCE=db2clnt1
7. Optionally, confirm that the driver location was copied:

   `cat site_arep_login.sh`
8. Add the following entry to the odbcinst.ini file under /etc:

   [IBM DB2 ODBC DRIVER]

   Driver = /home/db2clnt1/sqllib/lib/libdb2o.so

   fileusage=1

   dontdlclose=1
9. Start the Data Movement gateway service:

   sudo systemctl start repagent
10. Optionally confirm that the service has started:

    sudo systemctl status repagent

    The status should be as follows:

    Active: active (running) since <timestamp> ago

#### Linux data server client

1. Download 12.1.4 (v12.1.4\_linuxx64\_client.tar.gz) from [IBM Fix Central](https://www.ibm.com/support/fixcentral/) and extract the files.
2. Stop the Data Movement gateway service:

   `sudo service repagent stop`
3. Optionally, confirm that the service has stopped:

   `sudo service repagent status`

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
4. Change the working directory to /opt/client and run db2\_install.
5. Create an RSP file (see Sample RSP file below) and then run the following command (from /opt/client):

   ./db2setup -r /file-path/client.rsp
6. Add the following entry to the odbcinst.ini file under /etc:

   [IBM DB2 ODBC DRIVER]

   Driver = /opt/ibm/db2/V12.1.4/lib64/libdb2o.so

   fileusage=1

   dontdlclose=1
7. Start the Data Movement gateway service:

   `sudo service repagent start`
8. Optionally confirm that the service has started:

   `sudo service repagent status`

   The status should be as follows:

   Active: active (running) since <timestamp> ago

Sample RSP file

```
*-----------------------------------------------------
* Generated response file used by the DB2 Setup wizard
* generation time: 2/18/22 4:10 PM
*-----------------------------------------------------
*  Product Installation
LIC_AGREEMENT       = ACCEPT
PROD       = CLIENT
FILE       = /opt/ibm/db2/V12.1.4
INSTALL_TYPE       = TYPICAL
* ----------------------------------------------
*  Instance properties
* ----------------------------------------------
INSTANCE       = inst1
inst1.TYPE       = client
*  Instance-owning user
inst1.NAME       = qlik
inst1.UID       = 1000
inst1.GROUP_NAME       = qlik
inst1.HOME_DIRECTORY       = /home/qlik
inst1.AUTOSTART       = NO
*-----------------------------------------------
*  Installed Languages
*-----------------------------------------------
LANG       = EN

```

### Server side ODBC setup

Bind the plan to be used for ODBC, as specified in the PLANNAME= value in the ODBC initialization file. The default name is DSNACLI.
The BIND job can be found in member DSNTIJCL, which is in the SDSNSAMP library of the source DB2 installation.

Use the DB2CLI bind command to bind the ODBC-supplied packages to your intended source z/OS DB2 subsystem. This action is described in [Configuring your developer and runtime environment](https://www.ibm.com/support/knowledgecenter/en/SSEPGG_11.1.0/com.ibm.db2.luw.apdv.cli.doc/doc/r0007866.html) on the IBM website. For information about the DB2CLI utility, including an example for the bind utility, see [db2cli - DB2 interactive CLI command](https://www.ibm.com/support/knowledgecenter/en/SSEPGG_11.1.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0002045.html) on the IBM website.

## Required permissions

To enable Data Movement gateway to extract data from the source tables (Full Load and Change Data Capture), the user specified in the IBM DB2 for z/OS connector settings must be granted the following permissions:

- EXECUTE on the IFI reading the UDTF (only required for Change Data Capture)
- SELECT on the source tables and on the following system catalog tables:
  - SYSIBM.SYSDUMMY1
  - SYSIBM.SYSTABLES
  - SYSIBM.SYSTABLESPACE
  - SYSIBM.SYSPARMS
  - SYSIBM.SYSROUTINES
  - SYSIBM.SYSCOLUMNS
  - SYSIBM.SYSLGRNX
  - SYSIBM.SYSTABLEPART
- MONITOR2 to be able to start IFI sessions
  (only required for Change Data Capture)

## Capturing data changes

To capture changes from IBM DB2 for z/OS, Data Movement gateway uses a special program - invoked as an external routine - which is a user-defined table function (UDTF). This program (a load module) as well as the UDTF need to be installed and configured on the z/OS system before changes can be captured. The installation procedure, which should be performed by the DBA, is described in [*Installing and configuring R4Z*](../../../../Global_Common/Content/SharedReplicateHDD/R4Z_Install_Config/concept-design.htm).

Additionally, the DATA CAPTURE CHANGES attribute must be set for every table whose changes you want to capture. You can either do this manually or allow Data Movement gateway to do this by leaving the Automatically enable DATA CAPTURE CHANGES (requires admin privilege) option enabled (the default) in the connector settings.
