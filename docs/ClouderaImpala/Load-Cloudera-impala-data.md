---
title: "Select and load data from a Cloudera Impala database"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ClouderaImpala/Load-Cloudera-impala-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Cloudera Impala"]
---

# Select and load data from a Cloudera Impala database

Once you have created a connection to an Cloudera Impala database, you can select data and load it into a Qlik Sense application.
In Qlik Sense, you load data through the Add data dialog or the Data load editor.

Information noteThe SELECT statement does not include a WHERE clause, but one can be added in the Data load editor after the script built automatically in the script panel is inserted there. The SELECT statement for the Cloudera Impala Connector supports the addition of WHERE clause.

## Qlik Sense: Cloudera Impala database properties

Database properties that can be configured

| Properties | Description |
| --- | --- |
| Database | Shows the databases (catalogs) on the server if the corresponding option is turned on in the connection dialog. |
| Owner | Shows the owners of tables in the database if the corresponding option is turned on in the connection dialog. |
| Tables | Shows the tables associated with the selected owner.  Selecting a table will cause the table fields to be displayed in the Data preview tab.  Overriding the default number of tables retrieved  Information noteRequires Direct Access gateway 1.7.1 or later.  By default, a maximum of 10,000 tables are retrieved from the database. You can override the default when your database has more than 10,0000 tables.  To do this, on the Direct Access gateway machine:   1. Using a text editor, open C:\ProgramData\Qlik\Gateway\configuration.properties as admin. If you are doing this via Windows Explorer, make sure that Show > Hidden items is selected. 2. Locate the ODBC\_TABLES\_LIMIT\_FOR\_GENERICODBC property and set it to the directory of your choice.  Example:  ODBC\_TABLES\_LIMIT\_FOR\_GENERICODBC=15000 3. Save the configuration.properties file and restart the Qlik Data Gateway - Direct Access service. |
| Data preview | Shows a preview of the fields and data of the selected table. |
| Metadata | Shows a table of the fields and whether they are primary keys. Primary key fields are also labeled with a key icon Primary key beside the field name.  Information noteWhen using the ODBC (via Direct Access gateway) connector, primary key fields will only be shown if the Load PK metadata connector option is turned on. For more information, see [*Create a connection to an ODBC database*](../ODBC-DrectAccess/Create-ODBC-connection.htm).  Information noteOccasionally, due to a bug with the vendor driver's handling of data types, the target data might be incorrect or an error might occur during reload. If you encounter such issues, see [Overriding the Qlik Cloud data type when working with the ODBC (via ) Direct Access gateway connector](../../../Sense_Hub/Gateways/direct-access-gateway-troubleshooting.htm#Overridi) |
| Fields | Lists the fields in each selected table. If the table name check box is selected, all the fields in the table are automatically selected. If you click only the table name, fields are displayed but not selected. They can then be selected individually.  You can also change the field name by clicking on the existing field name. The new name is then used as an alias for the name the field has in the database. |
| Filter data | Shows a field where you can enter filter criteria.  [*Filter data from an ODBC database*](../Filter-ODBC-data.htm) |
| Filter fields | Displays a field where you can filter on field names |
| Hide script/Preview script | Shows or hides the load script that is automatically generated when table and field selections are made. |
| Include LOAD statement | Adds a LOAD statement before the SELECT statement.  [*Add a LOAD statement to an ODBC connection*](../How-to-add-LOAD-statement.htm) |
| Add data | Opens the Associations view of the Data manager.  Allows you add more data sources, fix any errors in your data, and create table associations. This option is available only when you use Add data.  [Managing data associations](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/LoadData/associating-data.htm) |
| Insert script | Inserts the script displayed in the Data preview panel into the script editor. This option is available only when you use the Data load editor. |
