---
title: "Using the SAP BW Connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Clients/SAP-BW-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connector clients"]
---

# Using the SAP BW Connector

The BW Connector lets you extract data from  InfoProviders and BEx/BW queries in SAP BW.

For details about extraction for different BW objects, see:

- [*Working with BEx and BW queries using a SAP BW connection*](Working-with-BEx.htm)
- [*Working with InfoProviders using a SAP BW connection*](Working-with-InfoProviders.htm)

## Supported objects

The SAP BW connector supports the following SAP objects only:

- InfoObject

  Information noteText and attribute tables for InfoObjects included in InfoProviders are loaded with the SQL connector. Individual InfoObjects cannot be selected in the Select dialog.
- Cube
- MultiProvider
- ADSO
- CompositeProvider
- Open ODS view
- BEx query

## Creating an SAP BW connection

Qlik Sense applications connect to the SAP BW Connector through the Data manager or the Data load editor.

### Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

### Creating the connection

Do the following:

1. Open a new or existing Qlik Sense application.
2. Select SAP BW from the list of connectors.

   The SAP BW connection dialog opens with the following fields:

   Connection fields available to be configured

   | Connection field | Description |
   | --- | --- |
   | Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. |
   | Server Type | Application Server or Message Server Information noteDo not change the Server Type once you start to edit the remaining fields as a connection error may result. If this is the case close the Connect… dialog and restart the script editor. |
   | Host | Address of the Application Server or Message Server. |
   | Client | The client number of the SAP system. |
   | System Nr | The system number of the SAP Application Server system. |
   | System ID / Port | The system ID of the SAP Message Server system.If passing through a message server, an entry may have to be added in the C:\WINDOWS\system32\drivers\etc\services file. Add sapmsxxx 36nn/tcp, where xxx is the system ID and nn is the system number. If it is the last line in the file, add a new line break after the entry. You can also enter the Port number directly, instead of the System ID. The Port number is of the form 36nn where nn is the system number. |
   | Group | The Message Server group |
   | Username | A user name authorized to access the SAP system.  Information noteRemember that different users can get different results due to row based access control. [*Access control*](../Configuration/Access-authorization.htm#AccessControl) |
   | Password | The authorized user's password. |
   | Logon Language | The language to use when logging into the SAP system. The default is to use the language that is set on the SAP system. The logon language is used to get the InfoProvider names and descriptions that will populate the selection dialog. If the language is not specified, the user's default language in SAP is used. If the user's default language in SAP is not set, the system language of the SAP system is used. The language can be specified with either the SAP one-character or ISO two-character format (such as EN for English and SV for Swedish). You can also use the complete name of a language, such as English and Deutsch. |
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

There are a number of properties that can be added to the connection string. Normally, the default values for these properties are sufficient. The following can be added as advanced properties in the connection dialog:

BEx properties available in connection dialog

| Properties | Values | Descriptions |
| --- | --- | --- |
| BEx Legacy Mode (datatypes) | 0/1 (default/off = 0, on = 1) | Handles the data sent from SAP without data type mapping in the client. This should be turned on if you are using an old BEx script.  Information noteWe strongly recommend that you use the BW Connector instead of the BEx and InfoProvider Connectors when creating new scripts. |
| BEx Legacy Mode (script) | 0/1 (default/off = 0, on = 1) | Interprets the load script as an old BEx script. This should be turned on if you are using an old BEx script |

InfoProvider properties available in connection dialog

| Properties | Values | Descriptions |
| --- | --- | --- |
| DB Aggregation | 0/1 (default/on = 0, on = 1) | When turned off, the field RowNum, which is added by the connector, guarantees that the extracted rows are unique. When turned on, SAP aggregates the selected measure values in relation to the selected characteristics. |
| Use\_Aggregates | 0/1 (default/on = 1, 0 = off) | When on, data is read from aggregates if the InfoProvider is a cube. |
| Currency\_Conv | 0/1 (default/on = 1, 0 = off) | Currency key figures are stored in the database with two decimal places. For output, these amounts have to be converted to a format according to the decimal places definition in table TCURX. Because the converted currency is written to a field that only has two decimal places, conversion of currencies with more than two decimal places causes rounding errors. |
| ConvRoutine | 0/1 (default/off = 0, on = 1) | Indicates that output conversion routines are used. This is commonly used for fields like Material Number (MATNR). |
| CheckSeparator | 0/1 (default/off = 0, on = 1): | A specific combination of characters is used as field separator in the connector. This combination may occur in a field in the database and cause an error. If that happens, turn on this property to make the connector try alternative character combinations. Since this slows down the performance, it is only to be used when necessary. |
| ReplaceNullvalue | 0/1 (default/on = 1, 0 = off) | If on, replaces all ’null’ values in the data with ‘ ‘ (SPACE) before sending it to Qlik Sense. |
| Trace | 0/1 (default/off = 0, on = 1) | Turns on/off the trace functionality in SAP programs. The trace information is written in the table /QTQVC/TRACE. |
| PacketSize | n (default = 20000) | The maximum number of rows in a packet that the connector downloads with each fetch operation. This is re-calculated by the connector and might be reduced automatically, depending of the actual amount of shared memory in the SAP system. The PacketSize setting can be further limited by MaxRows. |
| MaxRows | n (default = 0, where 0 means no limit) | The maximum number of rows the connector downloads. MaxRows works independently from PacketSize and sets a limit on the total number of rows to download.  For example, if PacketSize is set to 100 and the query returns 1000 rows, the data will be downloaded in 10 packets of 100 rows each. But if MaxRows is set to 500, only 5 packets of 100 rows each will be downloaded. |
| BufferPercentage | nn (default = 10) | Defines the amount of the free shared memory buffer that can be used by the job. A higher value increases the speed, but also increases the risk for conflicts with other jobs.  Special value 999 can now be used to force the connector to use 10% of the available shared memory, not only a percentage of free shared memory. This should be used if the Connector starts to show deteriorating performance. |
| TimeOutBatch | n (default = 600 seconds) | The number of seconds that the background job waits for the client side to fetch data. |
| TimeOutFetch | n (default = 1200 seconds) | The number of seconds spent trying to fetch from SAP without getting any records back. |
| TimeOutStartBatch | n (default = 2400 seconds) | The number of seconds that the client side waits for the background job to start. |
| BatchJobName | XXX (default = /QTQVC/READ\_MPDATA) | BatchJobName is the name of the data extraction batch job and can contain up to 32 characters.  BatchJobName can be found in Job Overview (transaction SM37). |
| TargetServer | xxxxxxx | If specified, forces the background job to be executed on the specified application server. The correct name can be found in transaction SM51. The name is case-sensitive. |
| JobClass | A/B/C (default = C) | Sets the priority for the background job, which can be useful for small jobs that need to be reloaded often. |
| SAPRouter | Possible value is a string of host name and service name/ port in the following format: /H/hostname/S/portnumber | Use this field to specify the SAP Router parameters if the connection needs to be made through a firewall via a SAP Router. |
| GatewayHost | Not applicable | The hostname of the Gateway at which you want to register. It must be the same as defined in SAP transaction SM59 (if the RFC destination defines an explicit gateway). |
| GatewayService | Possible values are sapgw00 - sapgw99, 3300 - 3399 | The Service name (as defined in etc/services) or the port number under which the gateway is listening. |

If the properties are added manually to the connection string, separate the properties with a semicolon in the connection string.
