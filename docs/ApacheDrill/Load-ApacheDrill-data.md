---
title: "Select and load data from an Apache Drill database"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ApacheDrill/Load-ApacheDrill-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Apache Drill"]
---

# Select and load data from an Apache Drill database

Once you have created a connection to an Apache Drill database, you can select data and load it into a Qlik Sense application.
In Qlik Sense, you load data through the Add data dialog or the Data load editor.

Information noteThe SELECT statement does not include a WHERE clause, but one can be added in the Data load editor after the script built automatically in the script panel is inserted there. The SELECT statement for the Apache SPARK Connector supports the addition of WHERE clause.

## Qlik Sense: Apache Drill database properties

Database properties that can be configured

| Properties | Description |
| --- | --- |
| Owner | Lists the owners of tables in the data store. |
| Tables | Lists the tables associated with the selected owner.  Selecting a table will cause the table fields to be displayed in the Data preview tab. |
| Filter tables | Displays a field where you can enter filter criteria to search for specific tables. |
| Data preview | Displays a preview of the fields and data of the selected table. |
| Metadata | Displays a table of the fields and whether they are primary keys. Primary-key fields are also labeled with a key icon Primary key beside the field name. |
| Fields | Lists the fields in each selected table. If the table name check box is selected, all the fields in the table are automatically selected. If you click only the table name, fields are displayed but not selected. They can then be selected individually. You can also change the field name by clicking on the existing field name. The new name is then used as an alias for the name the field has in the database. |
| Filter data | Displays a field in which you can enter filter criteria.  [*Filter data from an ODBC database*](../Filter-ODBC-data.htm) |
| Filter fields | Displays a field where you can filter on field names |
| Hide script/Preview script | Shows or hides the load script that is automatically generated when table and field selections are made. |
| Include LOAD statement | Adds a LOAD statement before the SELECT statement.  [*Add a LOAD statement to an ODBC connection*](../How-to-add-LOAD-statement.htm) |
| Add data | Opens the Associations view of the Data manager.  Allows you add more data sources, fix any errors in your data, and create table associations. This option is available only when you use Add data.  [Managing data associations](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/LoadData/associating-data.htm) |
| Insert script | Inserts the script displayed in the Data preview panel into the script editor. This option is available only when you use the Data load editor. |
