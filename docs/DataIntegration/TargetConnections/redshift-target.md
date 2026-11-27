---
title: "Amazon Redshift"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/redshift-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to data warehouses"]
---

# Amazon Redshift

You can use Amazon Redshift as a target data platform in a data pipeline or in a replication task. In a data pipeline, various ELT operations can be performed on the target platform including storing data, transforming data, creating data marts, and registering data. A replication task, on the other hand, involves replication of data directly from a source system to a target system with basic transformation capabilities, but without support for ELT operations.

Setting up Amazon Redshift  as a target involves:

- [Fulfilling the prerequisites](#Prerequi2)
- Configuring a connection to the cloud staging area (Amazon S3). This is not required if you are [registering existing data](../Onboarding/Registering-data.htm).
- Configuring a connection to Amazon Redshift

## Setting up a cloud staging area

Information noteIf you are you are [registering existing data](../Onboarding/Registering-data.htm), you do not need to set up a cloud staging area.

Configuring a connection to Amazon Redshift also requires you to set up connectivity to an Amazon S3 cloud staging area, where data and changes are staged before being applied and stored.

For information on setting up a connection to Amazon S3, see [*Amazon S3*](aws-s3-target.htm#Using2).

## Configuring a connection to Amazon Redshift

Once you have provided the staging settings, do the following:

1. In Connections, click Create connection.
2. Select the Amazon Redshift target connector and then provide the following settings:

### Data target

#### Data gateway

Information noteThis field is not available with Qlik Talend Cloud Starter subscription as Data Movement gateway is not supported with this subscription tier.

A Data Movement gateway is only required if the target database is not accessible from Qlik Cloud and can only be accessed using a Private Link (for instance, if it's located on-premises behind a firewall or in a Virtual Private Cloud). If this is the case, select the Data Movement gateway through which you want to access the target database.

Depending on your use case, this will either be the same Data Movement gateway deployed to move data from the data source, or a different one.

For information about Data Movement gateway use cases, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top) and [*Common use cases*](../../Gateways/replication-gateway.htm#Common).

If the target database is directly accessible from Qlik Cloud, select None.

Information noteWhen accessing the target database via Data Movement gateway, you also need to install the appropriate driver on the Data Movement gateway machine. For details, see [*Driver setup*](#Driver) below.

### Connection properties

- Server: Host name of the Amazon Redshift database server.
- Port: The port through which to access your Amazon Redshift database. The default is 5439.

### Account properties

User Name and Password: The user name and password of a user authorized to access the Amazon Redshift database.

### Database properties

- Database name: There are two methods you can use to specify a database:

  - Method 1 - Select from a list: Click Load databases and then select a database.
  - Method 2 - Manually: Select Enter database name manually and then enter the database name.

### S3 properties

- IAM Role ARN (Only required when staging to S3 on EC2): The ARN associated with the role you created in the IAM Roles Anywhere console. A role is an IAM identity that you create in your account with specific permissions. For IAM Roles Anywhere to be able to assume a role and deliver temporary AWS credentials, the role must trust the IAM Roles Anywhere service principal.

  For more information about IAM Roles Anywhere, visit [Extend AWS IAM roles to workloads outside of AWS with IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the connection.

## Prerequisites

### Required permissions

Grant the following permissions on the Redshift database:

- Grant COPY
- Grant INSERT
- Grant UPDATE
- Grant DELETE
- Grant SELECT
- Create Schema (only required if schemas do not exist and you want Qlik Talend Data Integration to create them)
- Grant CREATE TABLE
- Grant ALTER TABLE
- Grant DROP TABLE

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

   ./install redshift

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will be displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the install redshift command again.

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

   ./update redshift

   If the driver cannot be downloaded (due to access restrictions or technical issues), a message will displayed instructing you where to download the driver and where to copy it on the Data Movement gateway machine. Once you have done that, run the update redshift command again.

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

   ./uninstall redshift

   The driver will be uninstalled.

#### Manually installing the driver

You should only attempt to install the driver manually if the automated driver installation did not complete successfully.

1. Stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Optionally, confirm that the service has stopped:

   sudo systemctl status repagent

The status should be as follows:

Active: inactive (dead) since <timestamp> ago

3. Download and install the [Linux SQL client tools](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-to-cluster.html) necessary to connect to the Amazon Redshift cluster. Qlik Data Gateway - Data Movement requires Amazon Redshift ODBC Driver (x64) 1.4.65.1000 only.

   Download the driver from:

   <https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.4.65.1000/AmazonRedshiftODBC-64-bit-1.4.65.1000-1.x86_64.rpm>

   After installing the ODBC driver, edit the /etc/odbcinst.ini file as follows:

   `[ODBC Drivers]`

   `Amazon Redshift (x64)=Installed`

   And:

   `[Amazon Redshift (x64)]`

   `Description=Amazon Redshift ODBC Driver (64-bit)`

   `Driver=/opt/amazon/redshiftodbc/lib/64/libamazonredshiftodbc64.so`
4. Start the Data Movement gateway service:

   sudo systemctl start repagent
5. Optionally, confirm that the service has started:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

For a list of drivers supported by Amazon Redshift, see <http://docs.aws.amazon.com/redshift/latest/mgmt/configure-odbc-connection.html>.

### Port

Port 5439 (Amazon Redshift Cluster) needs to be opened for outbound communication.

### CA certificate

Data Movement gateway connects to AWS using SSL. This requires an appropriate CA certificate to reside on the Data Movement gateway machine; otherwise, the connection will fail. The purpose of the CA certificate is to authenticate the ownership of the AWS server certificate.

Make sure that the required CA certificate exists in the following location on the Linux machine:

/etc/pki/tls/certs/ca-bundle.crt

If it does not exist, the simplest solution is to copy the certificates bundle from another Linux machine.

### General prerequisites and considerations

- If your data source has 4-byte emoji characters, use a transformation to convert the data type from WSTRING(n ) to WSTRING ( n\*2 ).
- Make sure the time and time zone settings on the Data Movement gateway machine are accurate. This is required in order to ensure:

  - Proper synchronization of Full Load and CDC tasks
  - Correlation of the transaction log time with the actual time
- You cannot read live views and history views into Qlik Cloud Analytics Services from datasets created in an Amazon Redshift target by Qlik Talend Data Integration.

## Limitations and considerations

- The Amazon Redshift connector supports standard authentication (user name and password) only.

## Data types

The following table shows the Amazon Redshift data types that are supported when using Qlik Cloud and the default mapping from Qlik Cloud data types.

Native data type information is preserved, and is displayed in the Native data type column in dataset views. If the column is not visible, you need to open the column picker of the data set view and select the Native data type column.

Information noteIn Qlik Cloud, string length is in characters, while in Redshift, varchar length is in bytes. The number of bytes per character may vary depending on the actual characters and the encoding. Qlik Cloud assumes the length is 3 bytes per character. This means that when you define wstring(10), the table will be created as varchar(30) in practice.

Supported data types

| Qlik Cloud data types | Amazon Redshift data types |
| --- | --- |
| BOOLEAN | BOOLEAN |
| BYTES | VARBINARY(length) |
| DATE | DATE |
| TIME | VARCHAR (20) |
| DATETIME | If scale is => 0 and =< 6, then:  TIMESTAMP  If scale is => 7 and =< 12, then:  VARCHAR (37) |
| INT1 | INT2 |
| INT2 | INT2 |
| INT4 | INT4 |
| INT8 | INT8 |
| NUMERIC | If scale is => 0 and =< 37, then:  NUMERIC (precision, scale)  If scale is => 38 and =< 127, then:  VARCHAR (length) |
| REAL4 | FLOAT4 |
| REAL8 | FLOAT8 |
| STRING | If length is => 1 and =< 65535, then:  VARCHAR (Length in Bytes)  If length is => 65535 and =< 2147483647, then:  VARCHAR (65535) |
| UINT1 | INT2 |
| UINT2 | INT4 |
| UINT4 | INT8 |
| UINT8 | NUMERIC (20,0) |
| WSTRING | If length is => 1 and =< 21845, then:  NVARCHAR (length in Bytes)  If length is => 21846and =< 2147483647, then:  NVARCHAR (65535) |
| BLOB | VARBYTE (16777216) |
| NCLOB | VARCHAR (65535) |
| CLOB | VARCHAR (65535) |
| JSON | SUPER |

The following SQL Server data types are not supported. Data will not be read.

- HLLSKETCH

The following data types are converted to VARCHAR (65535):

- GEOGRAPHY
- GEOMETRY
