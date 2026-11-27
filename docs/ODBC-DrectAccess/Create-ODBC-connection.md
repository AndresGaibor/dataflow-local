---
title: "Create a connection to an ODBC database"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ODBC-DrectAccess/Create-ODBC-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "ODBC (via Direct Access gateway)"]
---

# Create a connection to an ODBC database

Connections to an ODBC database are made by selecting ODBC (via Direct Access gateway) from the list of connectors in the Add data connection or Data load editor dialogs.

Information noteIndustry-accepted best practices must be followed when using or allowing access through the ODBC Connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Data gateway

Source properties

| Database properties | Description | Required |
| --- | --- | --- |
| Direct Access gateway | Select the Direct Access gateway through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space with which the gateway is associated. | Yes |

## Database properties

Database properties

| Database properties | Description | Required |
| --- | --- | --- |
| System DSN  ODBC driver | Choose one of the following:   - System DSN: This option requires you to define a System DSN for your data source. For more information, see [*Creating a System DSN*](ODBC.htm#Creating). - ODBC driver: If you choose this option, after you select your driver from the ODBC source drop-down list, you will need to configure the connection properties in the Connection string field. | Yes |
| ODBC source | Click the Load button. The drop-down list will be populated with either of the following:   - If you selected System DSN, the list will show all System DSNs defined on the Direct Access gateway machine. - If you selected ODBC driver, the list will show all drivers installed on the Direct Access gateway machine.   Choose the driver or System DSN for your data source. | Yes |
| Connection string | Do one of the following:   - If you selected ODBC driver, enter a connection string. - If you selected System DSN, optionally append parameters to the existing DSN parameters.  Information noteAs the existing DSN parameters are not exposed in the UI, be careful not to enter parameters that might override existing DSN parameters. As each driver type handles duplicate parameters differently (some use the first instance while others use the last), best practice is to check the DSN parameters on the Direct Access gateway machine before entering any additional parameters.   Information noteAlthough the connection string usually starts with Driver= (for drivers) or DSN= (for System DSNs), these parameters should be omitted as they are automatically added when establishing a connection to the data source.  Example of an ODBC driver connection string - MariaDB syntax:  SERVER=mydatabase.mydomain.com;USER=odbc\_user;PASSWORD=odbc\_pw;DATABASE=odbc\_test;PORT=3306  Warning noteDo not include sensitive parameters such as user, password, tokens, and so on, in the connection string, as such parameters might be exposed as plain text when establishing the connection. Instead, use the Encrypted Properties option (see below) to store sensitive connection string parameters. | Yes |
| Encrypted properties | You can securely store encrypted connection string properties. For each encrypted property, you have to provide a Name and a Value. Use the Add icon and Bin icon buttons to the right of the Value field to add and remove properties. The connection string will be completed with the specified property names and their unencrypted values when connecting to the data source. | No |
| Attached file properties | For each attached file property, specify a property Name and a File name. Use the Add icon and Bin icon buttons to the right of the File button to add and remove properties. A connection string will be completed with specified property names and temporary path to uploaded the file when connecting to the data source. | No |

## Database specific options

Database specific options

| Database properties | Description | Required |
| --- | --- | --- |
| SQL syntax | Select your data source syntax or select Custom SQL syntax to specify a custom syntax. Out-of-the-box syntax is provided for the following data sources:   - DB2 - MariaDB - Sybase ASE - SAP HANA - Greenplum | Yes |
| Delimit column names | Some data sources require column names with upper case letters or special characters to be delimited in the load script. When this option is selected, the delimiter specified in the Identifier start delimiter and Identifier end delimiter fields will be used to delimit these column names. If the option is not selected and one or more column names needs to be delimited, an error will occur when you try to load or preview the data.  Information noteThis option requires Direct Access gateway 1.7.10 or later. | Only if required by the data source. |
| Delimit table names | Some data sources require table names with upper case letters or special characters to be delimited in the load script. When this option is selected, the delimiter specified in the Identifier start delimiter and Identifier end delimiter fields will be used to delimit these table names. If the option is not selected and one or more table names needs to be delimited, an error will occur when you try to load or preview the data.  Information noteThis option requires Direct Access gateway 1.7.11 or later. | Only if required by the data source. |
| Identifier start delimiter | The character string that is used as the starting delimiter of a quoted (delimited) identifier in SQL statements. This field is read-only unless you selected Custom syntax. | A value needs to be provided if Custom SQL syntax is selected. |
| Identifier end delimiter | The character string that is used as the ending delimiter of a quoted (delimited) identifier in SQL statements. This field is read-only unless you selected Custom syntax. | A value needs to be provided if Custom SQL syntax is selected. |
| SELECT statement template for Data Preview | This field is read-only unless you selected Custom syntax. The template supports the use of the following variables:   - ${QO}: Corresponds to the Identifier start delimiter value. The character string that is used as the starting delimiter of a quoted (delimited) identifier in SQL statements. - ${QC}: Corresponds to the Identifier end delimiter value. The character string that is used as the ending delimiter of a quoted (delimited) identifier in SQL statements. - ${COLUMN\_LIST}: List of columns used in result set. - ${TABLE\_NAME}: The table name. - ${TABLE\_OWNER}: The table owner. - ${SCHEMA\_NAME}: The schema name. - ${FILTER} LIMIT 50: When an SQL statement is generated for Data Preview, ${FILTER} will be replaced by the values defined in the “Filter data” text box. For example, if a selected table has Category and Product columns, and the following values are defined in the “Filter data” text box:  Category=“beverages” and Product=“Coke”  Then the configured filter will be applied to the SELECT statement when the data is previewed.   Warning noteDo not omit "LIMIT" keywords from the SELECT statement template for Data Preview. "LIMIT" keywords differ according to the SQL syntax supported by the data source. For example, MariaDB uses "LIMIT" while SAP Sybase ASE uses TOP. Even if "LIMIT" keywords are omitted, the connector will always truncate the data preview result set to a maximum of 50 records. However, in some cases, performing just SELECT xxx FROM yyy without limiting the result-set could take a long time to complete on the database server, impacting Select dialog performance.  See also:  [*Filter data from an ODBC database*](../Filter-ODBC-data.htm)  [*Select and load data from an ODBC data source*](Load-ODBC-data.htm) | Values need to be provided if Custom SQL syntax is selected. |

## Miscellaneous

Miscellaneous properties

| Database properties | Description | Required |
| --- | --- | --- |
| Allow non-select queries | You can execute load scripts that do not start with an SQL SELECT statement, for example UPDATE, INSERT, EXEC, and WITH ... AS.  For more information, see [*Executing non-SELECT statements*](../How-to-load-without-SELECT.htm) | No |
| Load primary key metadata | Turn on this option to load primary key metadata.  Information noteThe Load primary key metadata option is not supported with all drivers. If this option is turned on for an unsupported data source, a message will be shown in the Select dialog (when retrieving a table) that an error occurred while trying to retrieve the primary key metadata. In such a case, you need to turn off the Load primary key metadata option before retrying the operation. |  |
| Query timeout | Amount of time before the query times out. This can be set from 30 seconds to 65535 seconds. Default is 150. | No |

## Reload optimization

If you have large datasets, the Bulk Reader will automatically load larger portions of data in the iterations within a load, instead of loading data row by row.

Load optimization properties

| Property | Description | Required |
| --- | --- | --- |
| Number of rows to fetch per bulk  Information noteRequires Direct Access gateway 1.7.13 or later. | The default value is optimal for most scenarios and drivers. However, if you encounter significant performance issues, adjusting this value might help.  Information noteThe number of rows that are actually fetched might be less than the specified value. If the sum of multiplying the specified value by the total size of all fetched rows (per bulk) does not exceed 20 MB (the maximum fetch buffer threshold), the number of rows fetched will match the specified value. However, if the sum exceeds 20 MB, the number of rows fetched will be reduced until it falls within the maximum buffer threshold (20 MB). | No |
| Maximum string length | Maximum length of string fields. This can be set from 256 to 16384 characters. The default value is 4096. Setting this value close to the maximum length may improve load times, as it limits the need to allocate unnecessary resources. If a string is longer than the set value, it will be truncated, and the exceeding characters will not be loaded. | No |
