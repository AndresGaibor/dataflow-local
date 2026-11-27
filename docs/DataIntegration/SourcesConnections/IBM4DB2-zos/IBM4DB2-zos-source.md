---
title: "IBM DB2 for z/OS"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-zos/IBM4DB2-zos-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# IBM DB2 for z/OS

This section explains how to set up an IBM DB2 for z/OS source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](prerequisites-zos.htm), and familiarized yourself with the [*Limitations and considerations*](zos-limitations.htm).

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the IBM DB2 for z/OS source connector and then provide the following settings:

### Data source

- Data gateway

Select a Data Movement gateway to use for moving your data.

For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).

- Server: The IP address or host name of the IBM DB2 for z/OS server.
- Port: The port through which to access the IBM DB2 for z/OS server.

  Information noteIf the Server is a parallel SysPlex and data sharing members reside on multiple LPARs, the host address may specify a DVIPA - a Dynamic Virtual IP Address (to utilize the system redundancy and load-balancing in Data Movement gateway processing). In this case, the port numbers must be identical for all members.

### Account properties

- User name: The user name required to access the IBM DB2 for z/OS server.
- Password: The password required to access the IBM DB2 for z/OS server.

### Database properties

The Location should be the DB2 location name defined during the installation. This should be a relational database management system under z/OS, which can be either a subsystem or a group connection. This is the logical name which serves applications in order to designate resources managed by this system, either using the SQL CONNECT instruction, or placing it as a qualifier of a table (preceding the schema name).

To see the location name, use the “-DIS DDF” DB2 command (option 7 under the DB2I panel in ISPF), or look in message DSNL004I in the job log of the <ssid>MSTR address space.

### CDC properties

- To enable data capture from IBM DB2 for z/OS, the source tables need to be created as follows:

  CREATE / ALTER TABLE table-name …. DATA CAPTURE CHANGES [INCLUDE LONGVAR COLUMNS];

  You can either configure Data Movement gateway to perform this operation by selecting Automatically enable DATA CAPTURE CHANGES (requires admin privilege) in the connector settings or you can do this manually.

- Check for changes every (sec): How often to check the source database for changes.
- CDC reader UDTF name: The name of the Qlik-supplied User-Defined Table Function, which is used for CDC. Specify the two-part name using the values you have chosen for schema name, &R4ZSCNM, and the function name, &R4ZIFITF.
- UDTF result set size (MB): Specify the maximum size to be accumulated by result rows returned by the Qlik-supplied User-Defined Table Function, through CDC landing tasks using this connector. A larger result set will cause less overhead time establishing the IFI session, but will result in greater memory consumption by DB2. Specifically, because the result set is a LOB, you might need to increase the LOBVALA limit in the DB2 configuration (DSNZPARM), specifying the maximum LOB size allowed per user. Assuming all CDC tasks are configured with the same ODBC user-ID, to accommodate for all tasks running concurrently, set LOBVALA to 2 × 1024 × the following size:`SUM[(i=all endpoints) : resultset size in endpoint(i) × #_tasks using endpoint(i)]`(Resultset size is in Mbytes, so it needs to be multiplied by 1024 to reflect LOBVALA size, which is in Kbytes).Another DSNZPARM limit, LOBVALS, specifies the total size when across all user-IDs; so, if there are multiple user IDs, you need to monitor this value as well. Note, however, that LOBVALS is specified in Mbytes, unlike LOBVALA.

### SSL options

- Enable SSL: Select to enable SSL
- Keystore database file: (Optional) The keystore database file (containing your private key) on the Data Movement gateway machine. The file must be in CMS format (<filename>.kdb), which is usually the default.
- Stash file: (Optional) A file with an encrypted version of the keystore database password.
- Keystore database password: (Optional) The Keystore database file can be access using either the password that is set here or the stash file that is specified in the Stash file field.

Warning note

KDB and stash files need to be generated using a GSKit version that is compatible with the DB2 driver supported by Data Movement gateway.

For information on which GSKit version is shipped with a particular driver version, see [GSKit Versions Shipped with DB2](https://www.ibm.com/support/pages/node/484539)

### Override CCSID mapping to code page

In the CCSID to character set mapping field enter the CCSID(s) and code page(s) in the following format (separated by commas with no spaces):

CCSID1,codepage1,CCSID2,codepage2,...

The Character set (code page) must be specified in the proper format (e.g. ibm-1148\_P100-1997). For a list of valid formats, see [the ICU Converter Explorer](http://demo.icu-project.org/icu-bin/convexp).

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

#### Supported internal properties

The following table provides a list of internal parameters that can be used as required.

Internal parameters

| Parameter name | Values | Default; Max; Min. |
| --- | --- | --- |
| ifi306MessageLevel | 0 – No DEBUG traces;  1 – include DEBUG traces;  9 – full DEBUG | 0; 0; 9. |
| ifi306BufferSize | Size (in bytes) of Log data buffer used for IFI reading | 65536; 65536; 1048576. |
| additionalConnectionProperties | <keyword>=<value>;…  Example:  `cursorhold=1;patch2=15` | (empty string) |

### Name

The display name for the source connection.

## R4Z configuration dependency on host

This table in this section provides a list of R4Z configuration values, which can be set during installation or as part of the CDC service setup, or as part of the endpoint definition.

R4Z configuration values

| R4Z Topic | Depends upon Property | Defined at/Inquired by | Resolution |
| --- | --- | --- | --- |
| Total Size of R4Z ECSA structures | Available ECSA size | /DNET,CSM,…  OWNERID=ALL | Make sure ECSA size is not exceeded. |
| MAXRESULTSETSECS parameter in the CDC service | Maximum time DB2 thread waits for a locked resource | DSNZPARM IRLMRWT param. in SDSNSAMP(DSNTIJUZ) | Set at least two seconds below the SSID spec. |
| MAXRESULSETSIZEparameter in the CDC service | Maximum LOB size available per user-ID | DSNZPARM LOBVALA param. in SDSNSAMP(DSNTIJUZ) | 2 \* (resultset size \* max. session) |
| Decimal point: period or comma | Designates the decimal editing separator | DSNHDECM DECIMAL= param. In DSNTIJUZ | If the decimal separator is a comma, set the additionalConnectionProperties internal property to patch2=15. |
