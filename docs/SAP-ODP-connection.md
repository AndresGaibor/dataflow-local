---
title: "Using the SAP ODP Connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_ODP_Connectors_Help/Content/Connectors_SAP_ODP/SAP-ODP-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP ODP"]
---

# Using the SAP ODP Connector

## Creating a SAP ODP connection

Qlik Sense applications connect to the SAP ODP Connector through the Data manager or the Data load editor.

Do the following:

1. Open a new or existing Qlik Sense application.
2. Select SAP ODP from the list of connectors.

   The SAP ODP connection dialog opens with the following fields:

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
   | Username | A user name authorized to access the SAP system.  Information noteRemember that different users can get different results due to row based access control. [*Access control*](../Connectors_SAP/Configuration/Access-authorization.htm#AccessControl) |
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

SAP ODP properties available in connection dialog

| Properties | Values | Descriptions |
| --- | --- | --- |
| Max PackageSize | 0 - 52428800 (default = 52428800 ) | The maximum number of rows in a packet that the connector downloads with each fetch operation. |
| Subscriber Type | XXX (default = SAP\_BW) | The ODP API requires the type of receiver of the extracted data. The selected Subscriber Type doesn't affect the API responses used within the connector. |
| Subscriber Name | XXX (default = QLIK\_CONNECTOR) | The name of the receiver of data. Used as part of the key for registered ODP subscriptions (delta processes). |
| Subscriber Process | XXX (default = QLIK\_\*) |  |
| SAPRouter | Possible value is a string of host name and service name / port in the following format: /H/hostname/S/portnumber | Use this field to specify the SAP Router parameters if the connection needs to be made through a firewall via a SAP Router. |
| GatewayHost | Not applicable | The hostname of the Gateway at which you want to register. It must be the same as defined in SAP transaction SM59 (if the RFC destination defines an explicit gateway). |
| GatewayService | Possible values are sapgw00 - sapgw99, 3300 - 3399 | The Service name (as defined in etc/services) or the port number under which the gateway is listening. |

If the properties are added manually to the connection string, separate the properties with a semicolon in the connection string.

## Select and load data

Do the following:

1. Open the Select dialog
2. Select Context
3. Select and object from the Object list
4. Select Fields in the Metadata tab
5. Set conditions in the Conditions tab
6. Preview the data in the Data Preview tab
