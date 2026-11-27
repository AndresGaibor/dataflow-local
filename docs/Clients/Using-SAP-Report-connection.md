---
title: "Using the SAP Report Connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Clients/Using-SAP-Report-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connector clients"]
---

# Using the SAP Report Connector

Connections to the Qlik SAP Report Connector are made from the list of connectors in Qlik Cloud.

You must have a valid Enterprise license that supports Qlik connectors for use with SAP NetWeaver. To access data, you need to have access credentials.

For information on how to use this connector with QlikView, see Using the SAP Report Connector with QlikView.

## Supported objects

The SAP Report connector supports the following SAP objects:

- ALV GRID Tables

## Create an SAP Report connection

### Before you start

To access SAP Report data, you need to know the type of server you want to connect to, and have access credentials. When using Qlik Cloud you must also have a valid license, one that supports Qlik connector for use with SAP NetWeaver.

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

### Creating the connection

Do the following:

1. Open a new or existing Qlik Cloud application, or add the connection as a data source in a space.
2. Select the SAP Report from the list of connectors.

   A create connection dialog opens with the following connection fields.

Connection fields available to be configured

| Connection field | Description |
| --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway through which you need to connect to your data source.  Information note Requires Direct Access gateway 1.7.7 or later.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space with which the gateway is associated. |
| Server Type | Application Server or Message Server Information noteDo not change the Server Type once you start to edit the remaining fields as a connection error may result. If this is the case close the Connect… dialog and restart the script editor. |
| Host | Address of the Application Server or Message Server. |
| Client | The client number of the SAP system. If empty, the default is the SAP system's default client. |
| System Nr | The system number of the SAP Application Server system. If empty, the default is 0. |
| System ID / Port | The system ID of the SAP Message Server system.If passing through a message server, an entry may have to be added in the C:\WINDOWS\system32\drivers\etc\services file. Add sapmsxxx 36nn/tcp, where xxx is the system ID and nn is the system number. If it is the last line in the file, add a new line break after the entry. You can also enter the Port number directly, instead of the System ID. The Port number is of the form 36nn where nn is the system number. |
| Group | The Message Server group |
| Username | A user name authorized to access the SAP system.  Information noteRemember that different users can get different results due to row based access control. [*Access control*](../Configuration/Access-authorization.htm#AccessControl) |
| Password | The authorized user's password. |
| Logon Language | The language to use when logging into the SAP system. The default is to use the language that is set on the SAP system. If the language is not specified, the user's default language in SAP is used. If the user's default language in SAP is not set, the system language of the SAP system is used. The language can be specified with either the SAP one-character or ISO two-character format (such as EN for English and SV for Swedish). You can also use the complete name of a language, such as English and Deutsch. |
| Trace | Use this option to turn on/off the trace functionality in SAP programs. The trace information is written in the /QTQVC/TRACE table |
| SAP router | If the connection needs to be made through a firewall via a SAProuter, specify the SAProuter parameters here. |
| Gateway Host | The hostname of the gateway where you want to register. |
| Gateway Service | The service name (as defined in etc/service) or the port number under which the gateway is listening. |

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

## Select and load data from an SAP Report connection

Once a connection to SAP has been established, you can select data and load it into a a Qlik Sense application.

## Select and load data

Do the following:

1. Open the Select dialog
2. Select a report from the available Reports
3. Select a variant from the Report variant list
4. Preview the data in the Data Preview tab
5. Select Fields in the Metadata tab
6. Select Preview script or Insert script

### If a report is missing from the Reports list

If a report does not appear in the Reports list in the Select dialog, add and scan the report in SAP, and then try again.

Use transaction /QTQVC/ALV\_MAINT when the automatic scan misses a report, when you need to correct or lock report details manually, or when you need to re-scan one or more reports.

Do the following:

1. In SAP GUI, open transaction /QTQVC/ALV\_MAINT.
2. Enter the report program name. For SAP Query reports, use the generated program name (AQ.../SAPQUERY/...), not the query transaction name.
3. Click Scan to detect ALV metadata.
4. If the source scan cannot determine the structure, confirm runtime scan by choosing Run when prompted.
5. Optional: select Manual to protect curated entries from automatic re-scanning.
6. Click Save.
7. Return to Qlik and open the Select dialog again.

Information note

Report metadata is stored in /QTQVC/TRDIR\_ALV.

Automatic discovery uses /QTQVC/GET\_ALV\_REPORTS and includes reports added and scanned manually.

Entries marked Manual are protected and are not overwritten by automatic scans.

Runtime scan submits the report and can execute report business logic.

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
