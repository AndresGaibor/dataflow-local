---
title: "Sample connection strings and syntax"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ODBC-DrectAccess/sample-connection-strings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "ODBC (via Direct Access gateway)"]
---

# Sample connection strings and syntax

This topic provides sample connection strings and syntax for common drivers. Note that although the examples include sensitive information in the connection strings, due to a known issue with sensitive information being exposed as plain text, such information (for example, passwords, tokens, and so on) should not be included in the connection string. Instead, it should be specified in the Encrypted Properties fields, as in the following example:

![Image of the connection string and encrypted properties.](../_images/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Resources/Images/example-odbc-encryption.png)

Information noteIn future, this content will be available in Qlik Community only.

Connection string and syntax examples

| Name | Version | Connection String | Database required | Schema required | Delimiter Start | Delimiter End | Syntax | Example |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MariaDB | 3.01.17 | SERVER=<SERVER>; PORT=3306; DATABASE=<DBNAME>;uid=<username>;pwd=<password>; |  | No | ` | ` | SELECT ${COLUMN\_LIST}  FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 | LIB CONNECT TO 'Vera''s GODBC:Maria\_db\_ODBC\_(via\_Direct\_Access\_gateway)';  LOAD id,  numericcol,  numericPrecisionOverflowcol,  numericScaleOverflowcol,  numericp34s0col,  numericp34s20col;  [datatype\_numeric\_table]:[datatype\_numeric\_table]:  SELECT id,  numericcol, numericPrecisionOverflowcol, numericScaleOverflowcol, numericp34s0col, numericp34s20col  FROM `datatype\_numeric\_table`; |
| DB2 | 11.05.8000.317 | Server=<servername>;Port=50000;DATABASE=<DBNAME>;uid=<username>;pwd=<password>; |  | Yes | " | " | SELECT ${COLUMN\_LIST}  FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 |  |
| Pivotal Greenplum | 7.10.06.455 | Server=<servername>;Port=5432;DATABASE=<DBNAME>;uid=<username>;pwd=<password>; |  | Yes | " | " | SELECT ${COLUMN\_LIST}  FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 | LIB CONNECT TO 'Vera''s GODBC:Green\_ODBC\_(via\_Direct\_Access\_gateway)';  LOAD a,   b;  [bool]: [bool]:  SELECT a,  b  FROM "datatypes\_automation".bool; |
| Sybase ASE | 22.00.8389 | Server=<servername>;Port=5000;DATABASE=<DBNAME>;uid=<username>;pwd=<password>; |  |  | [ | ] | SELECT TOP ${COLUMN\_LIST}  FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 | LIB CONNECT TO 'Enterprise Connectors:Sybase\_ODBC\_(via\_Direct\_Access\_gateway)';  LOAD A,   B,   C;  [test\_table]:  [test\_table]:  SELECT A,  B,  C  FROM [test\_table]; |
| SAP HANA | 2.15.22.29501 | uid=<username>;pwd=<password>;SERVERNODE=<server>:30015; |  | Yes | " | " | SELECT TOP ${COLUMN\_LIST}  FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 | LIB CONNECT TO 'Vera''s GODBC:Saphana\_ODBC\_(via\_Direct\_Access\_gateway)';  LOAD ID,   DATECOL,   TIMECOL,  SECONDDATECOL,  TIMESTAMPCOL;  [Piggie\_Table\_4\_DateTime]:[Piggie\_Table\_4\_DateTime]:  SELECT ID,  DATECOL,  TIMECOL,  SECONDDATECOL, TIMESTAMPCOL  FROM "Z\_QLIK\_RnD"."Piggie\_Table\_4\_DateTime"; |
| MSSQL 17 (Custom) |  | Server=<servername>;Port=1433;DATABASE=<DBNAME>;uid=<username>;pwd=<password>; | Yes | Yes | " | " | SELECT TOP ${COLUMN\_LIST} FROM ${TABLE\_NAME} ${FILTER} | LIB CONNECT TO 'Vera''s GODBC:MSSQLODBC\_(via\_Direct\_Access\_gateway)';  LOAD id,   bitcol,   textcol,   ntextcol;  [datatype\_text]: [datatype\_text]:  SELECT id,  bitcol,  textcol,  ntextcol  FROM Northwind.dbo."datatype\_text"; |
| Vertica (Custom) |  | Server=<servername>;Port=5433;DATABASE=<DBNAME>;uid=<username>;pwd=<password>; | No | Yes | " | " | SELECT ${COLUMN\_LIST} FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 | LIB CONNECT TO 'vertica\_ODBC\_(via\_Direct\_Access\_gateway)';  LOAD A,   B,   C,   D,   WHATT;  [new\_table]: [new\_table]:  SELECT A,  B,  C,  D,  WHATT  FROM vmart."public"."new\_table"; |
| IBM Netezza (Custom) |  | DSN | Yes | Yes | " | " | SELECT ${COLUMN\_LIST} FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 | LIB CONNECT TO 'Vera''s GODBC:Neteza\_ODBC\_(via\_Direct\_Access\_gateway)';  LOAD A,   B;  [TEST]: [TEST]:  SELECT A,  B  FROM TEST.TEST; |
| PostgreSQL (Custom) |  | Server=<servername>;Port=5432;DATABASE=<DBNAME>;uid=<username>;pwd=<password>;schema=<schemaname>; | Depends on the database configuration. | Depends on the database configuration. | " | " | SELECT ${COLUMN\_LIST} FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 | LIB CONNECT TO 'Vera''s GODBC:1postgreODBC\_(via\_Direct\_Access\_gateway)';  LOAD id,   boolcol;  [datatypes\_bool]: [datatypes\_bool]:  SELECT id,  boolcol  FROM "public"."datatypes\_bool"; |
| MySQL |  | Server=<servername>;Port=3306;DATABASE=<DBNAME>;uid=<username>;pwd=<password>; | Depends on the database configuration. | Not supported. | ` | ` | SELECT ${COLUMN\_LIST} FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 | LIB CONNECT TO 'mysql\_ODBC\_(via\_Direct\_Access\_gateway)';  LOAD id,   charcol,   charExtcol,   ncharcol,   ncharUnicol,   varcharcol,   varcharExtcol,   nvarcharcol,   nvarcharUnicol;  [datatype\_char\_table]: [datatype\_char\_table]:  SELECT id,  charcol,  charExtcol,  ncharcol,  ncharUnicol,  varcharcol,  varcharExtcol,  nvarcharcol, nvarcharUnicol  FROM `datatype\_char\_table`; |
| Oracle (Custom) |  | DSN  connection string: pwd=ecPrivate123; |  | Yes | " | " | SELECT ${COLUMN\_LIST} FROM ${TABLE\_NAME} where ROWNUM <= 50 |  |
| IBM Informix (Custom) |  | DSN  connection string: Delimident=Y; |  | Yes | " | " | SELECT ${COLUMN\_LIST} FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 |  |
| IBM DB2 for iSeries |  | System=<servername>;Port=3306;DBQ=<DBQ>;uid=<username>;pwd=<password>; |  | Yes | " | " | SELECT ${COLUMN\_LIST} FROM ${TABLE\_NAME} ${FILTER} LIMIT 50 | LIB CONNECT TO 'Enterprise Connectors:DBi\_ODBC\_(via\_Direct\_Access\_gateway)';  LOAD A,   B;  [TEST]:  [TEST]:  SELECT A,  B  FROM  DAN.TEST; |
