---
title: "Access authorization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Configuration/Access-authorization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connector configuration"]
---

# Access authorization

The Qlik SAP Connectors are intended to be used as back-end components. They are not intended for end users. The authorization for end users should be setup using the normal QlikView and Qlik Sense procedures.

Connector-specific SAP Users should be created and these should not be used for other purposes. This will ensure traceability and better control. The connector package includes roles and profiles, but these should be seen as suggestions to be used in development environments. Part of the development process of the QlikView and Qlik Sense applications will be to create the necessary authorization in production roles. When changes to the QlikView or Qlik Sense-supplied roles are made in new versions of the SAP Connector software, the changes have to be manually added to the production roles.

## Authorization concept

An authorization is a permission to perform a certain action in the SAP system. The action is defined by the values of individual fields in an authorization object. When a user logs on to a client in an SAP system, the user’s authorizations are loaded in the user context. The user context is located in the user buffer (in the main memory) of the application server.

![Illustrated authorization concept with separate object class, authorization objects, authorization information, profile information, and user information](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/dr_authorization-concept.svg)

Several authorizations may be needed to perform an operation in the SAP system. The resulting contexts can be complex. The SAP authorization concept, based on authorization objects, has been introduced to provide an understandable and simple procedure.

The programmer of a function decides whether, where, and how authorizations are to be checked. The program determines whether the user is authorized to perform an activity by comparing the specified authorization object field values in the program to the authorization values in the user master record.

Authorizations can be collected in authorization profiles in order to reduce the maintenance effort that would be required to enter individual authorizations in the user master record. Access authorization changes affect all users with the profile in their master record.

## Authorization

The user profile transports from the Qlik SAP Connector installation package contain several predefined roles. These roles are only a proposal and should be adjusted to fit the specific purpose and needs. When you add authorization objects or change values, you should do so in a new custom role to avoid the changes being lost when you import new versions of the connector transports. The Qlik-supplied roles and their intended usage are as follows.

- QTQVCADMIN

There are a number of QlikView and Qlik Sense transactions in the SAP GUI. Most of them require that this role is assigned to the user.

- QTQVCACCESS

To be used by an SQL Back-end user when doing extraction jobs from QlikView or Qlik Sense.

[*Access control*](#AccessControl)

- QTQVCBWACCESS

To be used by OLAP, DSO/ODS and BEx Connectors Back-end users when doing extraction jobs from an SAP BI/BW system with QlikView.

- QTQVCEXTRACTOR

To be used by an Extractor Connector Back-end user when doing extraction jobs from QlikView.

- QTQVCEXTRADM

This role can only be used to activate and generate the extractors in an SAP system. The role is very restricted and can only be used to activate the extractors for later use by the Extractor Connector in QlikView.

- QTQVCEXTRSETUP

This role can only be used to create, delete, and verify the setup of the number logical system in an SAP system for later use by the Extractor Connector in QlikView.

## Access control

The role QTQVCACCESS should be used by the newly created SAP/QlikView or Qlik Sense user. This role, included in the user profile transport, provides access to all tables in the SAP system.

### Table-based access control

The QTQVCACCESS role is only intended to be used in a development environment. A copy of this role can be used in a production environment, where you have restricted access to only the tables that need to be downloaded.

Do the following:

1. In SAP, go to transaction PFCG and enter the role QTQVCACCESS.
2. Click ![Edit](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ic_gen_SAP-edit_20x20.png).

![Role Maintenance dialog with QTQVACCESS](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_role-maintenance.png)

1. Select the Authorizations tab.

![Change Roles dialog with Authorizations tab open](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_Change-roles.png)

1. Click the Change Authorization Data icon.
2. Expand the tree until the QlikTechDisplay>Table name row is visible.

![Authorization data tree](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_table-name-row.png)

1. Click the Edit icon ![Edit](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ic_gen_SAP-edit_20x20.png) to change the values.

   By default, it has the value \*, which means all tables are accessible. Single values or ranges of tables can be entered.

![Field values table dialog with * visible in first entry](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_Field-values.png)

### Row-based access control

In most cases, table-based access restriction is sufficient, but there can be situations where you may also want to restrict which rows in a table can be downloaded.

Use the /n/QTQVC/USERCONTROL transaction to define row-based access to specific tables for a user. This transaction is only to be used when download restrictions are needed at the row level. If the tables are empty, the table-based access restriction is used instead. If there is at least one row in this row-based restriction, it takes precedence over the table-based restriction.

You can use the position-based wildcard "+" when defining table scope. A "+" character represents any character in that position as follows:

- ZAP+++++++++++++++++++++++++ (would give access to all tables starting with ZAP).
- Z+++ (would give access to all tables starting with Z and having 1-4 characters in the name.
- +++A (would give access to all tables with 4 characters ending with A.
- ++++ (would give access to all tables with 4 characters or less).

If wildcards are used in the Table Name, it is not possible to have any value conditions on the field level in the effected tables. Thus the field name always has to contain an asterisk (\*) in connection with a wildcard in Table Name.

To use this functionality, create an additional Admin user that is allowed to use this transaction. Create the user in the same manner as above, but assign the role QTQVCADMIN instead. The Download users must not have this role assigned.

![Maintenance of Authorizations dialog](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_Authorization_maintenance.png)

In the left-hand table, Restriction tables, define the table to download data from:

- If restriction at the row-level is not needed, enter \* as FieldName and ALL as Domain.
- Any user assigned to a domain with an asterisk (\*) in the TableName column has access to all tables.
- To restrict at the row-level, enter the FieldName for which a value-based restriction is required. The Domain field is a free text field. Several field names in different tables can be linked to the same domain (to ease the maintenance of values).

In the right-hand table, Restriction users, define the allowed values, by user and by domain:

- If all values are allowed, enter an asterisk (\*) in the Value field and ALL in the Domain field.
- To restrict, enter one or more values in the Value field.

  Multiple values must be separated by commas followed by whitespace (101, 103).

  Non-numeric values must be enclosed within single quotation marks ('xxx').

  Ranges can be specified as BT(‘a’-‘d’). BT must be in capital letters.
- To apply restrictions to more than one field in a table, create more lines in each table.
- To create OR conditions, use the Group field to link the values together in pairs (or triplets).

Example:

(VKORG = 1000 AND SPART = 10) OR (VKORG =2000 AND SPART =20) 

VKORG value=1000 group=1

SPART value=10 group=1

VKORG value=2000 group=2

SPART value=20 group=2

### Copy user

To simplify maintenance, there is a Copy User function. Click the Copy User icon to open the Maintainance of Authorizations Copy dialog. If the Copy to user already exists, the lines of the Copy from user are appended to any existing lines.

![Maintenance of Authorizations copy dialog](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_Copy-user.png)

### Overview

To get an overview of what has been entered for a specific table or user, click Overview. This screen is only used to display the defined access.

The left-hand and right-hand tables are joined together using the Domain field.

Filtering can be done on the table and/or the user.

![Table overview dialog](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_overview.png)
