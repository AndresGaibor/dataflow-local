---
title: "Loading paged data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/Create-REST-connection/Loading-paged-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "REST data sources", "Create a REST connection"]
---

# Loading paged data

Many REST API implementations enforce a limit on the maximum number of records that can be returned in a single REST call. This applies mainly to JSON and XML data. When there are more records than can be returned by a single call, additional record pages can be returned by subsequent calls. How those additional pages are returned depends on the REST pagination type implemented by the data source.

Information noteCSV data sources usually do not provide paging values. When no paging is provided, the None paging option should be selected.

The Qlik REST Connector supports the following paging options. To select a paging option, you must know what option the REST data source supports. Some data sources implement the REST API to support multiple types of pagination, but most sources support only one.

- None is used when no paging is supported. Some REST API implementations simply return records with a single call and do not allow subsequent calls.
- Offset uses a starting value from which to read additional records.
- Next page uses field names and values and page sizes to determine how to read additional records.
- Next token uses a token that is passed to the URL call for the next set of records.
- Next URL uses a value that contains the URL for the next set of records.
- Custom is a special option that can be used when none of the other paging options are implemented. It requires the user to write a customized query using a WITH CONNECTION statement to return a set of records.

The WITH CONNECTION statement can also be used with data sources that support Offset, Next page, Next token, and Next URL. This is valuable when you need to customize the load script in some way that is not handled automatically by one of those options. See [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm) for more information.

The Qlik REST Connector enables the selection of Pagination Type when creating a connection.

Warning noteWhen specifying field names in any of the pagination fields described below, you must use the name as returned by the data source, not the name displayed by the connector in the selection dialog. The connector renames some fields in some cases, such as when a field name is duplicated in different levels of a JSON or XML document. For example, the field name "total," used in Total field path, might be renamed "total\_u1" by the connector.

The None option is selected when the REST API implemented by the data source does not support paging. The None option can also be selected if you do not want to use a paging option. In that case, only the first set of records is returned.

When the Offset option is selected, the following fields display in the connection dialog:

- 'Start' parameter name: The name of the parameter in the URL or request header that contains the starting point for the next page of data. When a data source such as LinkedIn uses Offset for pagination, it must specify which field is considered the first field in a record. For example, JIRA uses the field name "startAt" to hold the index value of the first item of the results requested, and LinkedIn uses the field name "\_start" to hold that index value.
- Pass via header: Specifies how the 'Start' parameter name and 'Start' initial value are transmitted by the connector. When Pass via header is selected, the connector transmits the parameter name and value in the header. If Pass via header is not selected, the parameter name and value are transmitted in the URL.
- 'Start' initial value: The number of the record from which to start reading records.
- 'Count' parameter name: The name of the count field used by the data source. The count field indicates the amount of data to return with each page. For example, JIRA uses the field name "maxresults" to hold the value for the number of records to return with each call, and LinkedIn uses the field name "\_count" to hold that value.
- Pass via header: Specifies how the 'Count' parameter name and 'Count' initial value are transmitted by the connector. When Pass via header is selected, the connector transmits the parameter name and value in the header. If Pass via header is not selected, the parameter name and value are transmitted in the URL.
- 'Count' initial value: The number of records to return with each call. The maximum allowed depends on the data source. Value must be a positive integer.
- 'Total records' path: The path to where the field that contains the total number of pages in the current source. For example, JIRA returns the value in the root element, root/total. The connector can use this value to understand when all the data has been loaded.
- Look in header: Specifies where to find the 'Total records' path. When Look in header is selected, the connector gets the path from the header. If Look in header is not selected, the connector gets the path from the URL.
- Data indicator path: The path to a field that contains values indicating whether or not data has been returned with the most recent request for the next page of data. This field can be used when the data source does not provide a total-number-of-pages value that the connector can use to determine when all the pages have been returned.

  The path to the data field begins with the table root. For example, root/meta/Total.

  The connector must be able to determine when the end of data has been reached, so either 'Total records' path or Data indicator path must be specified.

When the Next page option is selected, the following fields display:

- 'Next page'
   parameter name: The name of the parameter in the URL or request header that contains the starting point for the next page of data.
- Pass via header: Specifies how the 'Next page' parameter name an 'Next page'initial value are transmitted by the connector. When Pass via header is selected, the connector transmits the parameter name and value in the header. If Pass via header is not selected, the parameter name and value are transmitted in the URL.
- 'Next page'
   initial value: The number of the first page to be read from the current source.
- 'Page size' parameter name: The name of the parameter that holds the page size to use when reading from the current source.
- Pass via header: Specifies how the 'Page size' parameter name value is transmitted by the connector. When Pass via header is selected, the connector transmits the parameter name and value in the header. If Is header field is not selected, the parameter name and value are transmitted in the URL.
- 'Page size' value: The number of records to be returned with each page.
- 'Total pages' path: The path to the field that contains the total number of pages in the current source. The connector can use this value to determine when all the data has been loaded.

  Some data sources return the number of pages when the connection is made and some do not. If the data source does not provide a parameter with the total number of pages, then you must specify a Data indicator path to use for determining when all the data has been read.

  The path to the total page count begins with the table root. For example, root/totalPages.

  The total pages value can also be returned in a response header.
- Look in header: Specifies where to find the 'Total pages' path value.When Look in header is selected, the connector gets the path from the header. If Look in header is not selected, the connector gets the path from the URL.
- Data indicator path: The path to a field that contains values indicating whether or not data has been returned with the most recent request for the next page of data. This field can be used when the data source does not provide a total-number-of-pages value that the connector can use to determine when all the pages have been returned.

  The path to the data field begins with the table root. For example, root/stores/storeId.

  The connector must be able to determine when the end of data has been reached, so either 'Total pages' path or Data indicator path must be specified.

When the Next token option is selected, the following fields display:

- 'Next token'
   parameter name: The name of the parameter in the URL or request header that is used to send the token of the next page with each request. For example, YouTube uses Next token for pagination, and it uses the parameter "nextPageToken" to hold the token value that designates the next page of data.
- Pass via header: Specifies how the 'Next token' parameter name is transmitted by the connector. When Pass via header is selected, the connector transmits the parameter name and value in the header. If Pass via header is not selected, the parameter name and value are transmitted in the URL.
- 'Next token'
   path: The path to where the token field is stored. The token field stores the token value for the next page.
- Look in header: Specifies where to find the 'Next token' path value. When Look in header is selected, the connector gets the path from the header. If Look in header is not selected, the connector gets the path from the URL.

When the Next URL option is selected, the following fields display:

- 'Next URL' path: The path to the field in the response that contains the URL for the next page. When a data source has more pages, it returns the URL for the next page in the response to the previous request.

  All data pages must have the same data structure.
- Look in header: Specifies where to find the 'Next URL' path value. When Look in header is selected, the connector gets the path from the header. If Look in header is not selected, the connector gets the path from the URL.

When the Custom option is selected, no additional fields are displayed. The Custom option inserts a script template in the Data load editorEdit script dialog.

Information noteThe Custom option is available in Add data, but if you select it, you must go to the Data load editor to customize the script.

After the script template has been inserted in the, you must adapt the script for the source from which you are retrieving data in order to retrieve all of the intended records. [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm)
