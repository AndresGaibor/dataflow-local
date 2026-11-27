---
title: "Using the SAP SQL Connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Clients/Using-SAP-SQL-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connector clients"]
---

# Using the SAP SQL Connector

Connections to the Qlik SAP SQL Connector are made from the list of connectors in Qlik Sense.

## Supported objects

The SAP SQL connector supports the following SAP objects only:

- Transparent table
- CDS DDIC-based views (to be continued)

Information noteNew CDS view entities are not supported since there is no DDIC included. See the following SAP Community blog for more information: [CDS view entities - The new CDS views](https://community.sap.com/t5/technology-blogs-by-sap/cds-view-entities-the-new-cds-views/ba-p/13484596).

## Create an SAP SQL connection

### Before you start

To access SAP SQL data, you need to know the type of server you want to connect to, and have access credentials. When using Qlik Cloud you must also have a valid license, one that supports Qlik connector for use with SAP NetWeaver.

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

### Creating the connection

Do the following:

1. Open a new or existing Qlik Sense application, or add the connection as a data source in a space.
2. Select the SAP SQL from the list of connectors.

   A create connection dialog opens.
3. From the Direct Gateway drop-down list, select the data gateway through which you need to connect to your data source.

   Information noteThis field will only appear if you selected the "via Direct Access gateway" data connection. Users that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space with which the gateway is associated.

### Connection fields

Connection fields available to be configured

| Connection field | Description |
| --- | --- |
| Server Type | Application Server or Message Server Information noteDo not change the Server Type once you start to edit the remaining fields as a connection error may result. If this is the case close the Connect… dialog and restart the script editor. |
| Host | Address of the Application Server or Message Server. |
| Client | The client number of the SAP system. If empty, the default is the SAP system's default client. |
| System Nr | The system number of the SAP Application Server system. If empty, the default is 0. |
| System ID / Port | The system ID of the SAP Message Server system.If passing through a message server, an entry may have to be added in the C:\WINDOWS\system32\drivers\etc\services file. Add sapmsxxx 36nn/tcp, where xxx is the system ID and nn is the system number. If it is the last line in the file, add a new line break after the entry. You can also enter the Port number directly, instead of the System ID. The Port number is of the form 36nn where nn is the system number. |
| Group | The Message Server group |
| Logon Language | The language to use when logging into the SAP system. The default is to use the language that is set on the SAP system. The logon language is used to get the BEx names and descriptions that will populate the selection dialog. If the language is not specified, the user's default language in SAP is used. If the user's default language in SAP is not set, the system language of the SAP system is used. The language can be specified with either the SAP one-character or ISO two-character format (such as EN for English and SV for Swedish). You can also use the complete name of a language, such as English and Deutsch. |
| Username | A user name authorized to access the SAP system.  Information noteRemember that different users can get different results due to row based access control. [*Access control*](../Configuration/Access-authorization.htm#AccessControl) |
| Password | The authorized user's password. |
| Secure Network Settings | Select Secure Network Connection if Secure Network Communication is installed.  [*Secure network communication*](../Secure-network-communication.htm) |
| Connection String Properties | Additional properties to use for the connection. In Qlik Sense, the properties can be added by selecting the properties in the connection dialog.  [*Connection string properties*](#Connection-string-properties) |

### Passing through a SAP Router

Do the following:

1. When you are creating the connection, go to the Application Server Host/Message Server Host field.
2. Input the following string: /H/<Host name or IP number of SAP Router>/S/3299/H/<Fully Qualified Domain Name of target system>

   The port which the SAP Router is listening to is always 3299.
3. (Optional) Fill in the following connection string properties: SAPRouter, GatewayHost, and GatewayService. These are described below under "Connection string properties".

   This step is not mandatory, but is useful if the connection needs to be made through a firewall via SAP router.
4. If passing through a Message server, please read that section below. Note that the services file must also be updated on the SAP Router server. In that case, the SAP Router needs to be restarted.

### Passing through a Message server

If passing through a Message server, you may need an entry for the Message server port in the services file.

Do the following:

1. Locate the services file in: C:\Windows\System32\drivers\etc
2. Add sapmsxxx 36nn/tcp, where:

   1. xxx is the system ID
   2. nn is the system number (of the Message server).

   If it is the last line in the file, add a new line break after the entry.

There is an alternative to updating the services file. When you create the connector connection, you can enter the Message server port number directly, instead of the System ID.

The port number is of the form 36nn, where nn is the system number.

### Connection string properties

There are a number of properties that can be added to the connection string in either the Qlik Sense Data load editor if needed. Normally, the default values for these properties are sufficient. The following can be added as advanced properties in the connection dialog:

Connection string properties

| Properties | Values | Descriptions |
| --- | --- | --- |
| ConvRoutine | 0/1 (default = 0, on = 1) | Indicates that output conversion routines are used. This is commonly used for fields like Material Number (MATNR). |
| CheckSeparator | 0/1 (default/off = 0): | A specific combination of characters is used as field separator in the connector. This combination may occur in a field in the database and cause an error. If that happens, turn on this property to make the connector try alternative character combinations. Since this slows down the performance, it is only to be used when necessary. |
| Nulldate | 0/1 (default/on = 1) | Nulldate=1, date type fields with the value ‘00000000’ are returned as NULL to Qlik Sense.  Nulldate=0, date type fields with the value ‘00000000’ are returned as 12/30/1899 to Qlik Sense.  Corresponding SAP transports send all data to the connector without using any of the conversion functions applied to the SAP system. Any data that is not valid for the datatype is interpreted in Qlik Sense as NULL.  It is possible to display a NULL value as a selectable value by using the Qlik Sense variable NullDisplay.  [Qlik Sense: NullDisplay](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/Scripting/ValueHandlingVariables/NullDisplay.htm?q=NullDisplay) |
| RemoveAllBlanks | 0/1 (default/off = 0) | If on, provides the possibility to get the behavior where all blanks in fields in SAP containing only blank characters are trimmed. The default behavior leaves one blank character in order to differentiate from NULL fields. |
| ReplaceNullvalue | 0/1 (default/on = 1) | If on, replaces all ’null’ values in the data with ‘ ‘ (SPACE) before sending it to Qlik Sense. |
| Trace | 0/1 (default/off = 0, on = 1) | Turns on/off the trace functionality in SAP programs. The trace information is written in the table /QTQVC/TRACE. |
| MixedMode | 0/1 (default/off = 0 or false, on = 1 or true) | When MixedMode is enabled, the NUMC and CHAR data types are sent as UNKNOWN instead of ASCII, and it is up to Qlik to decide what their content is. A numeric string with a maximum length of 14 characters will be interpreted as numeric in Qlik (the same behavior as in the legacy connector). |
| NulldateLegacy | 0/1 (default/off = 0 or false, on = 1 or true) | When NulldateLegacy is enabled, the property Nulldate behaves as it did in the legacy connector, returning an empty value when Nulldate is enabled and returning "0000-00-00" when Nulldate is disabled. When NulldateLegacy is disabled, null is returned when Nulldate is enabled and 0 (displays as 1899-12-30) is returned when Nulldate is disabled.  It is recommended that you not use NulldateLegacy for new development. |
| FLTPLegacy | 0/1 (default/off = 0 or false, on = 1 or true) | When FLTPLegacy is enabled, FLTP (floating point) data is transferred to Qlik Sense as string values with scientific notation. When FLTPLegacy is disabled (the default setting), floating point data is transferred in decimal format. |
| TIMSLegacy | 0/1 (default/off = 0 or false, on = 1 or true) | When TIMSLegacy is enabled, TIMS data is transferred to as DUAL. When TIMSLegacy is disabled (the default setting), TIMS data is transferred to QVDs as a numeric value. |
| PacketSize | n (default = 20000) | The maximum number of rows in a packet that the connector downloads with each fetch operation. This is re-calculated by the connector and might be reduced automatically, depending of the actual amount of shared memory in the SAP system. |
| FetchBuffers | n (default = 99999999) | Defines how many buffers of data to fetch from SAP. It can be combined with the property PacketSize which decides how many rows there should be in each buffer.  To fetch one buffer with 100 rows, set the properties as follows:  FetchBuffers=1  PacketSize=100 |
| BufferPercentage | nn (default = 10) | Defines the amount of the free shared memory buffer that can be used by the job. A higher value increases the speed, but also increases the risk for conflicts with other jobs.  Special value 999 can now be used to force the connector to use 10% of the available shared memory, not only a percentage of free shared memory. This should be used if the Connector starts to show deteriorating performance. |
| TimeOutBatch | n (default = 600 seconds) | The number of seconds that the background job waits for the client side to fetch data. |
| TimeOutFetch | n (default = 1200 seconds) | The number of seconds spent trying to fetch from SAP without getting any records back. |
| TimeOutStartBatch | n (default = 2400 seconds) | The number of seconds that the client side waits for the background job to start. |
| TimeOutCheckJob | n (default = 60 seconds) | The number of seconds that the Windows side of the SAP SQL connector waits before checking to see if the background task in SAP has aborted. This property can be set in the connection string. It cannot be set in the connection dialog.  Warning noteSetting this property to less than the default value can noticeably affect performance. |
| BatchJobName | XXX (default = /QTQVC/READ\_DATA) | BatchJobName is the name of the data extraction batch job and can contain up to 32 characters.  BatchJobName can be found in Job Overview (transaction SM37). |
| TargetServer | xxxxxxx | If specified, forces the background job to be executed on the specified application server. The correct name can be found in transaction SM51. The name is case-sensitive. |
| JobClass | A/B/C (default = C) | Sets the priority for the background job, which can be useful for small jobs that need to be reloaded often. |
| SocketBufferSize | n (default = 32768) | Sets the socket buffer size (in bytes) for the Network Interface (TCP/IP). |
| SAPRouter | Possible value is a string of host name and service name/ port in the following format: /H/hostname/S/portnumber | Use this field to specify the SAP Router parameters if the connection needs to be made through a firewall via a SAP Router. |
| GatewayHost | Not applicable | The hostname of the Gateway at which you want to register. It must be the same as defined in SAP transaction SM59 (if the RFC destination defines an explicit gateway). |
| GatewayService | Possible values are sapgw00 - sapgw99, 3300 - 3399 | The Service name (as defined in etc/services) or the port number under which the gateway is listening. |

## Select and load data from an SAP SQL connection

Once a connection to SAP has been established, you can select data and load it into a a Qlik Sense application.

### Qlik Sense: Selection properties

Database properties that can be configured

| Properties | Description |
| --- | --- |
| Tables | Shows the tables associated with the selected owner.  Selecting a table will cause the table fields to be displayed in the Data preview tab. |
| Data preview | Shows a preview of the fields and data of the selected table.  You can select which data columns to include by checking the box beside the field name. You can also change the field name by clicking on the existing field name. The new name is then used as an alias for the name the field has in the database. |
| Metadata | Shows a table of the fields and whether they are primary keys. Primary-key fields are also labeled with a key icon Primary key beside the field name. |
| Show descriptions | Displays descriptions of the fields beside the field names. |
| Include LOAD statement | Adds a LOAD statement before the SELECT statement. This property is available in the Data load editor.  The LOAD statement before the SELECT statement allows the LOAD statement to use the SELECT statements as input. Basically, it is a LOAD statement that loads from the LOAD or SELECT statement below, without specifying a source qualifier, such as From or Resident, as you would normally. You can stack any number of LOAD statements this way. The statement at the bottom will be evaluated first, then the statement above, and so on until the top statement has been evaluated. Another advantage of the LOAD preceding SELECT is that you can keep a calculation in one place and reuse it in LOAD statements placed above. For example, when you load data from a database using a SELECT statement, you cannot use Qlik Sense functions to interpret data in the SELECT statement. The solution is to add a LOAD statement and perform data transformations above the SELECT statement. |
| Add data | Opens the Associations view of the Data manager.  Allows you add more data sources, fix any errors in your data, and create table associations. This option is available only when you use Add data.  [Managing data associations](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/LoadData/associating-data.htm) |
| Insert script | Inserts the script displayed in the Data preview panel into the script editor. This option is available only when you use the Data load editor. |

## Data types in SAP

A field in an SAP database table is assigned to a Data Type. Fields assigned to the following Data Types cannot be downloaded by the SQL Connector:

- LCHR (Long character string, requires preceding INT2 field)
- LRAW (Long byte string, requires preceding INT2 field)
- RAWSTRING (Byte String of Variable Length)

## Changing the field names

While the SELECT and LOAD statements are built automatically in Qlik Sense when you select tables and fields, you can make certain changes to those statements.

Field names can be changed in the Fields panel by clicking on the existing name and editing the name text.

![Field name editing dialog](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_SAP-SQL-select-data-change.png)

The changed name is then used as an alias for the original name when the field is loaded into Qlik Sense.

## STORE and DROP TABLE

STORE and DROP TABLE statements are automatically added to the generated script. However they are commented out as it is necessary to manually add a folder data connection that will be used in the STORE statement.

Example:

LIB CONNECT TO 'H6Q';

[VBAK]:

LOAD MANDT,

NETWR,

VDATU;

SELECT MANDT, // Client

NETWR, // Net value

VDATU // Req.dlv.dt

FROM VBAK;

// STORE \* FROM [VBAK] INTO LIB://[FolderConnection]/VBAK.qvd;

// DROP TABLE [VBAK];

If the statements were not commented out a script execution error would be raised, as there is no folder data connection named [FolderConnection]. A folder data connection must be manually created before running the script.

If you want to use the STORE and DROP TABLE statements, then once the folder data connection has been added to the application, the statements can be uncommented.

## ScriptBuilder

ScriptBuilder is a QlikView application, ScriptBuilder.qvw, that is used to find tables to download from the SAP system and to generate the script code. We recommend you copy the complete folder to be able to use this application for several SAP systems.

C:\ProgramData\QlikTech\Custom Data\QvSAPConnector\ScriptBuilder\.

Start with the ReLoadSAPDD.qvw application, which downloads data from the data dictionary of the SAP system. Since the content of the dictionary differs for different variants and versions of SAP, this is a necessary first step.

ReLoadSAPDD.qvw creates .qvd files that can be loaded to the ScriptBuilder application.

Change the script regarding the connection and language in this application prior to doing a reload.

The Popular Tables and Data Models sheets may refer to tables that do not exist in the version of SAP used.

Detailed usage instructions can be found in the application.

## SQL SUBSELECT syntax

An addition to the standard SAP OPENSQL syntax in the SQL Connector is SUBSELECT. This addition has been developed since JOIN or SUBSELECT cannot be done with cluster tables. Quite often this is required for tables like BSEG or KONV in order to do delta loads.

Information noteThe SUBSELECT method cannot be used if the row-based access control concept of the SAP SQL Connector is activated.

The result of the select from the main table is temporarily stored in the ABAP program in an internal table. There is a size limitation to internal tables, so try to avoid SELECT \*. Only select the fields necessary.

When using the SUBSELECT method against big database tables, always try to limit the selection with a WHERE condition which is using KEY fields or INDEXED fields. Before using the SUBSELECT statement in a production system, monitor it in a test system to make sure it does not consume too much memory or affect the system performance.

The syntax of SUBSELECT in the script is as follows:

SQL SUBSELECT BUKRS BELNR GJAHR BUZEI BUZID AUGDT FROM BSEG WHERE BUKRS BELNR GJAHR IN ( SELECT BUKRS BELNR GJAHR FROM BKPF WHERE BLDAT GE '20070101' );

- Only one SUBSELECT is allowed (within the parenthesis).
- The SUBSELECT can have condition(s).
- One or many comparison fields can be passed.
- If the SELECT of the sub-table returns duplicates, they are removed before selecting from the main table. So, there is no need (and it does not work) to use the DISTINCT addition to the SUBSELECT.
- The comparison field or fields has to match between main and SUBSELECT. The field names of the comparison fields do not have to be the same in the main and SUBSELECT, but the corresponding fields (of main and SUBSELECT) must have the same data types.
- To achieve good performance, it is important to provide as many of the key fields in the main table as possible. Try to select them from the sub-table. The most important item to provide is the first key field (after client).
- If the SUBSELECT fails, the reason can often be found in the log for the job /QTQVC/READ\_DATA in transaction SM37.

Other examples of SUBSELECT statements:

Example 1:

SQL SUBSELECT KDATU KAWRT KBETR WAERS FROM KONV WHERE KNUMV IN ( SELECT KNUMV FROM VBRK );

Example 2:

SQL SUBSELECT CHANGENR TABNAME TABKEY FNAME CHNGIND VALUE\_NEW VALUE\_OLD FROM CDPOS WHERE OBJECTCLAS OBJECTID CHANGENR IN ( SELECT OBJECTCLAS OBJECTID CHANGENR FROM CDHDR WHERE CHANGENR BETWEEN '0000100000' AND '0000300000' );

## SQL WIDESELECT syntax

Another addition to the standard SAP OPENSQL syntax in the SQL Connector is WIDESELECT.

SAP database fields with a column width exceeding 800 characters cannot be extracted by the ordinary SQL Connector.

With the Wideselect functionality there is no limitation on column width. It is possible to extract one wide field at a time together with a number of associated key fields.

- The key fields are optional.
- A key field can be any field in the database table with a fixed column width.
- The sum total of the column widths of the key fields cannot exceed 255 characters.
- The WIDE field must be of the datatype CHAR (character) or STRG (string).

Information noteThe WIDESELECT method cannot be used if the row-based access control concept of the SAP SQL Connector is activated

Two parameters are applicable for the key fields in the Wideselect connection string:

Key field parameters

| Parameters | Values | Descriptions |
| --- | --- | --- |
| ConvRoutine | 0/1 (default = 0, on = 1) | Indicates that output conversion routines are used. This is commonly used for fields like Material Number (MATNR). |
| Nulldate | 0/1 (default/on = 1) | Nulldate=1, date type fields with the value ‘00000000’ are returned as NULL to Qlik Sense and QlikView.  Nulldate=0, date type fields with the value ‘00000000’ are returned as 12/30/1899 to Qlik Sense and QlikView.  Corresponding SAP transports send all data to the connector without using any of the conversion functions applied to the SAP system. Any data that is not valid for the datatype is interpreted in Qlik Sense and QlikView as NULL.  It is possible to display a NULL value as a selectable value by using the Qlik Sense or QlikView variable NullDisplay.  [Qlik Sense: NullDisplay](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/Scripting/ValueHandlingVariables/NullDisplay.htm) |

The syntax of WIDESELECT in the script is as follows:

SQL WIDESELECT keyfield1 keyfield2 keyfieldn WIDE(widefield) FROM table WHERE <condition>

Example:

SQL WIDESELECT object joining\_date WIDE(test\_string) FROM zhrgtest WHERE connector = ‘WIDE12000’;

Information noteThere is no UI syntax support for the Wideselect functionality.

## SQL CDSSELECT syntax

Another addition to the standard SAP OPEN SQL syntax in the SAP SQL Connector is CDSSELECT. An SAP HANA system with SAP BASIS 740 SP08 or higher is required to use the functionality.

It is possible to select CDS views with parameters.

A CDS view has a name in the ABAP Dictionary. It also has a DDL (Data Definition Language) Source name. For CDSSELECT, the DDL Source name should be used.

The syntax of CDSSELECT in the script is as follows:

SQL CDSSELECT [\*] [fieldname\_1, fieldname\_2, fieldname\_n]

FROM 'CDS view name'(

parameter\_1 = 'X',

parameter\_2 = 'X',

parameter\_n = 'X' )

WHERE [condition];

- If there are parameters, the left parenthesis must be placed on the same row, immediately after the CDS view name, with no white space. Following the left parenthesis, there must be at least one white space before the first parameter. After the last parameter, there must be one white space before the right parenthesis.
- The field names and parameters are comma-separated.

Example:

CDS view with parameters:

SQL CDSSELECT \* FROM demo\_cds\_parameters(

p\_distance\_l = 1,

p\_distance\_o = 7000,

p\_unit = 'KM' );

CDS view without parameters:

SQL CDSSELECT \*

FROM demo\_cds\_select\_t100;

The CDSSELECT method cannot be used if the row-based access control concept of the SQL Connector is activated.

The available Connection String Properties are the same as for the ordinary SQL connector.

Information noteThere is no UI syntax support for the CDSSELECT functionality.
