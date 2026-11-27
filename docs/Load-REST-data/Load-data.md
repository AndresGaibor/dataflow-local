---
title: "Select and load data from a REST data source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/Load-REST-data/Load-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "REST data sources"]
---

# Select and load data from a REST data source

Information noteIf you use the Data load editor, do not modify the generated script. Specifically, modifying or removing the generated LOAD statements can result in \_\_extra\_ fields in your data.

Once a connection to a REST data source has been established, you can select data and load it into a Qlik Sense application. You select data by selecting REST tables and fields in the data selection dialog. You can load data using either Add data or the Data load editor. If you are using the Data load editor, you can also select data by entering script manually.

## Qlik Sense: Selection properties

Selection properties that can be configured

| Properties | Description |
| --- | --- |
| Response type | The format of the data to be loaded: XML, JSON, or CSV. |
| Auto detect | Detect the data format automatically when loading the data. |
| Preload symbols count | Specifies the amount of character data that is preloaded to display the data selection structure. The default is 50K. If the preload symbol count is not large enough to load all the branches in the data hierarchy, then any branches that are not loaded cannot be selected and are be included in the data load. No limit can be selected so that all the data is preloaded, but in that case, the preload could take a long time. |
| Tables | The hierarchy of tables available. |
| Filter tables | Displays a field for entering filter criteria. |
| Fields | The fields available in each selected table. [*Changing the field names in Qlik Sense*](#ChangingFieldName) |
| Data preview | Shows a preview of the fields and data of the selected table. |
| Metadata | Shows a table of the fields in the selected branch. |
| Filter fields | Displays a field for entering filter criteria. |

### Changing the field names in Qlik Sense

While the SELECT and LOAD statements are built automatically when you select tables and fields, you can make certain changes to those statements when using Qlik Sense.

Field names can be changed in the Fields panel by clicking on the existing name and editing the name text.

![Field name editing example](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/ui_Field-change-name1.png)

The changed name is then used as an alias for the original name when the field is loaded into Qlik Sense.

## Select statement syntax with the REST Connector

REST Connector load scripts consist of one SELECT statement and one or more LOAD statements. SELECT statements use the same structure as the source data. For example, data about stores from a JSON data source might be selected as follows:

![Example selection displaying that with the stores data selected in the structure it will select all the data in the tables](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/ui_gen_Select-statement-data.png)

The SELECT statement generated for this selection would be:

```
SQL SELECT
	"__KEY_root",
    (SELECT
    	"storedId",
        "city",
        "region",
        "__FK_stores"
     FROM "stores" FK "__FK_stores")
FROM JSON (wrap on) "root" PK "__KEY_root";

[stores]:
LOAD [storedId] AS [storeId],
	[city] AS [city],
    [__FK_stores] AS [__KEY_root]
RESIDENT RestConnectorMasterTable
WHERE NOT IsNull([__FK_stores]);
```

## SELECT statement syntax

The SELECT statement uses Extended Backus-Naur Form (EBNF). The syntax for the SELECT statement:

SQL <select\_stmt>;

select\_stmt=SELECT[<field>{,<field>}] FROM [<response\_type>][<options>] <table\_name> ['PK' <pk\_field\_name>] ['FK' <fk\_field\_name>] ['ContentFieldAlias' <content\_field\_name>] ['ArrayValueAlias' <array\_item\_field\_name>]

### SELECT statement parameters

- field = <simple\_field>|<select\_stmt>
- simple\_field = <field\_full\_name> [AS <field\_alias>]
- response\_type = CSV|XML|JSON. Only for top-level <select\_stmt>.
- options = (wrap on|off) for JSON, (header on|off, delimiter ",", quote "tab") for CSV. Only for top-level <select\_stmt>.
- pk\_field\_name - primary key field name for current table. Should be specified if there is any sub-select for current table.
- fk\_field\_name - primary key field name for current table. Should be specified if current table is sub-select.
- content\_field\_name - field name for data from XML element content (look at @Content in Metadata part).
- array\_item\_field\_name - field name for data from simple array items of JSON (look at @Value in Metadata part).
- table\_name - table name on the current hierarchical level (for XML and JSON). For CSV it is always CSV\_Source.
- field\_name - string describing data field location in the data source.
- field\_alias - this name will be used as field name in QvxTable.

All field aliases must be unique. If conflicts exist with alias names, the connector adds auto-incremented suffixes to the aliases until they are unique. For example, Employee\_u0, Employee\_u1. Aliases are used as field names in Qlik Sense tables.

For the XML response type, the connector adds a subselect without fields for descendant nodes, even if they are not selected in the select dialog. This is required to calculate key values for the Key generation strategy when Current record or Full qualified record is selected.

### WITH CONNECTION keyword

The REST Connector supports the WITH CONNECTION keyword, which can be used to override URLs, query parameters and query headers in a connection. The POST body can also be overridden when the POST method has been selected for the connection. WITH CONNECTION allows you to alter some parts of a connection rather than create a separate connection.

Four parameters can be used with the WITH CONNECTION keyword:

- URL
- QUERY
- HTTPHEADER
- BODY

The syntax for each parameter is:

- URL "new url"
- QUERY "parameter name" "parameter value"
- HTTPHEADER "header name" "header value"
- BODY "request body text"

Examples:

WITH CONNECTION (

Url "https://localhost:81/northwind2.xml",

QUERY "type" "XML",

QUERY "size" "",

HTTPHEADER "auth\_type" "token",

HTTPHEADER "token" "1234123123123",

BODY "Post this");

WITH CONNECTION can be used with any of the pagination types. When Custom pagination is specified, a WITH CONNECTION statement is included automatically in the load script. In the following example, the WITH CONNECTION statement is inserted using the URL generated for the Select data to load dialog. The load script must be modified, however, to perform the desired pagination. As it is generated, the statement would simply return the same page with each call because the startAt variable is always set to 0. An example of how the load script can be modified to get a sequence of pages is shown below:

```
LIB CONNECT TO 'REST-Google-custom (abc_admin)';

// Action required: Implement the logic to retrieve the total records
// from the REST source and assign to the 'total' local variable.
Let total = 0;

Let totalfetched = 0;
Let startAt = 0;
Let pageSize = 100;

for startAt = 0 to total step pageSize
RestConnectorMasterTable:
SQL SELECT
	.
	.
	.
	.
FROM JSON (wrap on) "root" PK "__KEY_root"
WITH CONNECTION(Url "https://content.googleapis.com/calendar/v3/calendars/primary/events?key=AIzaS...");
// Action required: change URL included in 'WITH CONNECTION' as
// needed to support pagination for the REST source.
// Please see the documentation for "Loading paged data."

NEXT startAt;
```

When any of the other pagination types are used, the WITH CONNECTION statement must be added manually.

[*Using WITH CONNECTION for pagination*](#WITH-CONNECTION-pagination)

## Using pagination

The following script illustrates how the automatically generated template for Custom pagination can be adapted to retrieve the desired number of pages in a Google Analytics data source. The query parameter startAt is incremented by the script so each call to the Google Analytics REST API begins to retrieve data at a different point in the source. Without the adaptation, the script would retrieve only the first page of data.

```
LIB CONNECT TO 'REST-Google-custom (abc_admin)';

// Action required: Implement the logic to retrieve the total records
// from the REST source and assign to the 'total' local variable.
Let total = 0;

Let totalfetched = 0;
Let startAt = 0;
Let pageSize = 100;

for startAt = 0 to total step pageSize
RestConnectorMasterTable:
SQL SELECT
	.
	.
	.
	.
FROM JSON (wrap on) "root" PK "__KEY_root"
WITH CONNECTION(QUERY "startAt" "$(startAt)");
// Action required: change URL included in 'WITH CONNECTION' as
// needed to support pagination for the REST source.
// Please see the documentation for "Loading paged data."

NEXT startAt;

LOAD

	.
	.
	.
	.

DROP TABLE RestConnectorMasterTable;
```

[*WITH CONNECTION keyword*](#WITH-CONNECTION-keyword)

## Using WITH CONNECTION for pagination

The WITH CONNECTION keyword can be used with all of the pagination options. Unlike with Custom pagination, which inserts WITH CONNECTION in the load script automatically, the WITH CONNECTION statement must be inserted manually after the SELECT statement.

When the Select data to load dialog opens, the tables and fields displayed are loaded by the URL and parameters specified in the URL field in the Create new connection (REST) dialog. Any entries in the Query parameters and Query headers fields in the dialog are also used. But when data is loaded, the WITH CONNECTION statement takes precedence over the Query parameters and Query headers fields. If the Add missing query parameters to final request option is selected, then any parameters from the Query parameters fields that are not in the WITH CONNECTION statement are added to the URL.

If the WITH CONNECTION statement contains a URL, that URL is used when data is loaded rather than the URL specified in the URL field in the Create new connection (REST) dialog.

If a WITH CONNECTION statement contains a URL, it must point to a data source that contains fields that match any of the selections made in the Select data to load dialog. Usually, the base URL used in the WITH CONNECTION statement is the same as the URL specified in the connection dialog. In that case, the tables and fields are likely to match.

[*WITH CONNECTION keyword*](#WITH-CONNECTION-keyword)

Several points are important to keep in mind when using WITH CONNECTION:

- Query parameters and headers can be added to the WITH CONNECTION statement, even if they are not specified in the Create new connection (REST) dialog.
- If the WITH CONNECTION statement includes a URL, then that URL is used when data is loaded. All paging iterations are then derived from that URL. In that case, the URL specified in the URL field in the Create new connection (REST) dialog is not used when data is loaded.

  In the case of Next URL pagination, each subsequent page request uses the URL returned by the data source.

  [*Using Next URL pagination and WITH CONNECTION*](#NextURL)
- If the WITH CONNECTION statement includes only query parameters and headers and does not include a URL, then the URL is taken from the URL field in the Create new connection (REST) dialog.

  In the case of Next URL pagination, each subsequent page request uses the URL returned by the data source.

  [*Using Next URL pagination and WITH CONNECTION*](#NextURL)
- Query parameters and headers included in the WITH CONNECTION statement cannot conflict with any query parameters or headers returned by the data source for pagination.

  Warning noteAn error results if the query parameters or headers from the WITH CONNECTION statement conflict with the query parameters or headers returned by the data source. However, if Add missing query parameters to final request is selected, the query parameters specified in the Create new connection (REST) dialog and those returned from the data source are added and the query parameters specified in the WITH CONNECTION statement are ignored. In that case, there is no error for conflicting query parameters.
- If the URL from the URL field of Create new connection (REST) dialog is used, query parameters and headers specified in the connection dialog's Query parameters and Query headers fields are added to the URL when it is used to open the Select data to load dialog. Those query parameters headers overwrite any entries with the same name that were added manually to the URL. If the WITH CONNECTION statement contains query parameters or headers, they are added to the URL at the time it is used to open the Select data to load dialog, and they overwrite any parameters or headers with the same name.

  Warning noteAn error results if the query parameters or headers from the WITH CONNECTION statement or from the connection dialog's Query parameters and Query headers fields conflict with the query parameters or headers returned by the data source. If there are no conflicts, the query parameters and headers returned by the data source are simply added to the other parameters and headers.
- Query parameters specified in the Create new connection (REST) dialog are added to the WITH CONNECTION statement if the Add missing query parameters to final request option is selected in the Create new connection (REST) dialog.
- Query parameters and headers added manually in the URL field of Create new connection (REST) dialog are not used in the WITH CONNECTION statement unless they are added the WITH CONNECTION statement manually as well.
- If the POST method is used, the body of text is taken from the WITH CONNECTION statement. If the WITH CONNECTION statement does not contain a Body property, the text is taken from the text specified in the Request body field in the Create new connection (REST) dialog.

## Using Next URL pagination and WITH CONNECTION

There are additional points to keep in mind when using WITH CONNECTION and the Next URL pagination option:

- If the WITH CONNECTION statement includes a URL, that URL is used for the first page of data.
- Query parameters and headers from the WITH CONNECTION statement are added to the URL returned from the data source and that returned URL is used for the next page request.

  Warning noteAn error results if the query parameters or headers from the WITH CONNECTION statement conflict with the query parameters or headers returned by Next URL pagination. However, if Add missing query parameters to final request is selected, the query parameters specified in the Create new connection (REST) dialog are added to the URL returned from the data source, and the query parameters specified in the WITH CONNECTION statement are ignored. In that case, there is no error for conflicting query parameters.

  If parameters or headers from the Create new connection (REST) dialog conflict with parameters or headers returned by Next URL pagination, the Next URL parameters and headers are used and the others are ignored. Any parameters or headers from the connection dialog that do not conflict are added to the URL returned by Next URL pagination.
- Query parameters and headers included in the WITH CONNECTION statement take precedence over parameters and headers in the Create new connection (REST) dialog.

  When the Add missing query parameters to final request option is selected in the Create new connection (REST) dialog, the parameters in the Query parameters fields are added to the URL returned from the data source, but if any of the parameters in the WITH CONNECTION statement are the same, the values from the WITH CONNECTION statement take precedence.

[*WITH CONNECTION keyword*](#WITH-CONNECTION-keyword)
