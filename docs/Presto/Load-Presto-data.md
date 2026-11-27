---
title: "Select and load data with a Presto connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Presto/Load-Presto-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Presto"]
---

# Select and load data with a Presto connection

Once you have created a Presto connection, you can select data and load it into a Qlik Sense application.
In Qlik Sense, you load data through the Add data dialog or the Data load editor.

Information noteThe SELECT statement does not include a WHERE clause, but one can be added in the Data load editor after the script built automatically in the script panel is inserted there. The SELECT statement for the PrestoDB Connector supports the addition of WHERE clause.

## Qlik Sense: Presto data selection properties

Database properties that can be configured

| Properties | Description |
| --- | --- |
| Database | Lists the databases configured for Presto. If a database was specified in the Catalog (Project) property of the connection dialog, it will be selected automatically when you open the selection dialog. You can select additional databases when you build the data selection script. After selecting tables and fields from one database, select another database and owner, and the tables and fields you select from that database will be added to the data selection script. |
| Owner | Lists the owners of data sets in the selected database. |
| Tables | Lists the tables associated with the selected owner.  Selecting a table will cause the table fields to be displayed in the Data preview tab. |
| Filter tables | Displays a field where you can enter filter criteria to search for specific tables. |
| Data preview | Displays a preview of the fields and data of the selected table.  You can select which data columns to include by checking the box beside the field name. You can also change the field name by clicking on the existing field name. The new name is then used as an alias for the name the field has in the database. |
| Metadata | Displays a table of the fields and whether they are primary keys. |
| Fields | Lists the fields in each selected table. If the table name check box is selected, all the fields in the table are automatically selected. If you click only the table name, fields are displayed but not selected. They can then be selected individually.  You can also change the field name by clicking on the existing field name. The new name is then used as an alias for the name the field has in the database. |
| Filter data | Displays a field in which you can enter filter criteria to select a subset of data in the fields you are loading. The Filter data property displays after tables have been selected.  [*Filter data from an ODBC database*](../Filter-ODBC-data.htm) |
| Filter fields | Displays a field where you can filter on field names |
| Hide script/Preview script | Shows or hides the load script that is automatically generated when table and field selections are made. |
| Include LOAD statement | Adds a LOAD statement before the SELECT statement.  [*Add a LOAD statement to an ODBC connection*](../How-to-add-LOAD-statement.htm) |
| Add data | Opens the Associations view of the Data manager. This option is available only when you use Add data.  Allows you add more data sources, fix any errors in your data, and create table associations. This option is available only when you use Add data.  [Managing data associations](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/LoadData/associating-data.htm) |
| Insert script | Inserts the script displayed in the Data preview panel into the script editor. This option is available only when you use the Data load editor. |
