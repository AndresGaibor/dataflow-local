---
title: "Select and load data from a MySQL Enterprise Edition database"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/MySQL/Load-MySQL-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "MySQL Enterprise Edition"]
---

# Select and load data from a MySQL Enterprise Edition database

Once you have created a connection to a MySQL Enterprise Edition database, you can select data and load it into a Qlik Sense application or a QlikView document.
In Qlik Sense, you load data through the Add data dialog or the Data load editor.

Information noteThe SELECT statement does not include a WHERE clause, but one can be added in the Data load editor after the script built automatically in the script panel is inserted there. The SELECT statement for the MySQL Enterprise Edition Connector supports the addition of WHERE clause.

## Qlik Sense: MySQL Enterprise Edition database properties

Database properties that can be configured

| Properties | Description |
| --- | --- |
| Tables | Shows the tables associated with the selected owner.  Selecting a table will cause the table fields to be displayed in the Data preview tab. |
| Data preview | Shows a preview of the fields and data of the selected table.  You can select which data columns to include by checking the box beside the field name. You can also change the field name by clicking on the existing field name. The new name is then used as an alias for the name the field has in the database. |
| Metadata | Shows a table of the fields and whether they are primary keys. Primary-key fields are also labeled with a key icon Primary key beside the field name. |
| Filter data | Shows a field where you can enter filter criteria.  [*Filter data from an ODBC database*](../Filter-ODBC-data.htm) |
| Include LOAD statement | Adds a LOAD statement before the SELECT statement.  [*Add a LOAD statement to an ODBC connection*](../How-to-add-LOAD-statement.htm) |
| Add data | Opens the Associations view of the Data manager.  Allows you add more data sources, fix any errors in your data, and create table associations. This option is available only when you use Add data.  [Managing data associations](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/LoadData/associating-data.htm) |
| Insert script | Inserts the script displayed in the Data preview panel into the script editor. This option is available only when you use the Data load editor. |
