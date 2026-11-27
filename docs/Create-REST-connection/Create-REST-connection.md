---
title: "Create a REST connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/Create-REST-connection/Create-REST-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "REST data sources"]
---

# Create a REST connection

Use the REST Connector to retrieve data from web APIs and integrate external data sources into your Qlik Sense or QlikView applications. This guide explains how to set up a REST connection, configure authentication and security, and optimize data retrieval for your analytics needs.

## Before you begin

- Confirm which Qlik product and environment you are using (Qlik Sense, QlikView, Cloud, Windows, etc.).
- Identify your target REST API endpoint and review its documentation for authentication, data format, and pagination requirements.
- Ensure you have permission to access the API and any required credentials.
- To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Overview: How REST connections work in Qlik

The REST Connector lets you connect to any web service or API that supports HTTP requests. You can specify endpoints, configure authentication, set request parameters, and control how data is retrieved and loaded. The connector supports GET and POST methods, custom headers, pagination, and advanced security options.

## Step 1: Allow access to URLs (Direct Access Gateway only)

Complete this step only if you use the "REST (via Direct Access gateway)" option in your data connection.

For instructions, see [Limiting the list of URLs that Direct Access gateway can access using the REST (via Direct Access gateway) connector](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-troubleshooting.htm#Limiting2).

## Step 2: Create and configure the REST connection

1. Open your Qlik application.

   - In Qlik Sense: Use Add data or Data load editor.
   - In QlikView: Use Edit Script.
   - In Qlik Cloud: Use Add data or add a data source in a space.
2. Select REST from the list of connectors.
3. If available, select a Data gateway from the drop-down (only appears for gateway-enabled connections).
4. Enter the API endpoint URL. Example:
   https://maps.googleapis.com/maps/api/geocode/xml?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=false
5. Set Connection Timeout (in seconds). This sets how long Qlik waits for a connection before erroring.
6. Set Read/Write Timeout (in seconds). This controls how long Qlik waits for data after connecting.
7. Choose HTTP method:
   - GET: Retrieves data without changing the server.
   - POST: Sends data to the server, such as submitting a form or creating a resource.
8. If using POST, enter the request body data as required by your API.
9. Select HTTP Protocol version (1.1 is default and recommended).
10. If your API supports Expect: 100-Continue for POST requests, enable the corresponding header.
11. Enable Auto detect response type to let Qlik determine the data format automatically.
12. Optionally, enable Check response type during 'Test connection' for additional validation.
13. Choose a Key generation strategy for JSON/XML data if you need parent/child relationships:
    - Sequence ID: Simple, maintains order.
    - Current record or Fully qualified record: Uses hash keys for complex relationships.
    - No keys: No explicit keys in loaded data.
14. If loading XML with DTD, select the appropriate XML DTD support option.

## Step 3: Optionally allow connections to localhost

Information note

Requires Direct Access gateway 1.7.6 or later.

You can allow the REST (via Direct Access gateway) connector to connect to localhost. This is required for the following operations:

- Metrics collection

  For more information on metrics collection, see [Metrics collector](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-troubleshooting.htm#Metrics).

  Information note

  Supported from Direct Access gateway 1.7.9.
- The use of local (to the gateway server) REST endpoints such as the connector-agent/status endpoint to determine the active number of reloads on an agent.

  Information note

  Supported from Direct Access gateway 1.7.6.

To allow the REST (via Direct Access gateway) connector to connect to localhost, select Allow working with localhost connection.

## Step 4: Configure authentication

1. Select Authentication Schema:

   Authentication schema options

   | Schema | Description |
   | --- | --- |
   | Anonymous | No authentication required. All users can access the resource. |
   | Basic | Requires username and password (sent as Base64, not encrypted). |
   | Digest | Challenge-response using Windows domain accounts. Requires domain configuration on the server. |
   | Windows NTLM | Challenge-response using Windows credentials. More secure than Digest. |
   | Current Windows User (NTLM) | Uses the Windows user running the connector. |
2. If required, enter your username and password for the REST account. These fields do not appear for Anonymous or Current Windows User (NTLM).
3. Choose Certificate validation:
   - Skip server certificate validation: Use only for non-production/test APIs.
   - Use System Trust Store: Validate server certificates against system root certificates.
   - Custom Root CA Certificate: Upload a PEM certificate if your API uses a custom CA.
4. For mutual SSL/TLS, enable Enable mutual SSL/TLS and specify certificate details.
5. Specify Trusted locations to restrict where credentials can be sent.
6. Click Test Connection to verify configuration before saving.

## Step 5: Define request parameters and headers

1. Add query parameters:
   - Enter a unique Name and Value for each parameter.
   - For duplicate parameter names, add them directly into the URL.
2. Enable Add missing query parameters to final request to include all specified parameters.
3. Add query headers:
   - Enter Name and Value for each header.
   - Enable Encrypt for sensitive headers (e.g., authorization).
4. Enable Allow "WITH CONNECTION" for advanced scripting in load statements.
5. Enable Retry failed requests to handle transient errors (e.g., 429, 503).

   Warning noteIf you use Date as a query header, format it as: yyyy-MM-dd-HH:mm:ssZ (for example, 2014-09-28 16:25:09Z).

## Step 6: Configure pagination (if needed)

1. Select the appropriate Pagination Type based on the API’s requirements.
2. Refer to your API documentation for pagination details.

For more guidance, see [*Loading paged data*](Loading-paged-data.htm)

## Step 7: Set security options

1. Enable Allow response headers to retrieve header fields in responses if your data source requires it.
2. Select Allow HTTPS only to enforce secure connections.
3. Add an allowlist of URLs for redirects during pagination.
4. Enable Use cookie container when redirect if your API requires cookies for redirected requests.

## Step 8: Configure proxy settings (Windows/Multi-Cloud only)

Information noteProxy settings are only available for Qlik Sense Enterprise for Windows or QlikView.

1. Enable Use proxy to route requests through a proxy server.
2. Enter the proxy IP address and port.
3. Enable Bypass on Local to allow local addresses through without proxy.
4. Specify any external addresses that should bypass the proxy.
5. Enable Use current user credentials to use your Windows credentials, or provide alternate credentials if needed.

## Step 9: Save and complete the connection

1. Enter a meaningful name for your connection in the Name field.
2. Click Create (or OK in QlikView) to save the connection.

After creating the connection, proceed to select and load data from your REST source. In Add data, this step follows immediately. In Data load editor, initiate the data load manually.

For advanced loading options, see [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm).

To insert the connection string in a script, use:

LIB CONNECT TO 'YourConnectionName';

## Troubleshooting and tips

- If you receive timeout errors, try increasing the Connection or Read/Write Timeout values, and review your proxy settings if applicable.
- If data fails to load, verify the API endpoint, authentication settings, and required headers.
- Consult your API documentation for required request parameters, headers, and pagination approaches.

## Related resources

- [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm)
- [*Loading paged data*](Loading-paged-data.htm)

# Create a REST connection

Access to the Qlik REST Connector is provided by Qlik Sense. Qlik Sense connects to data sources through Add data and the Data load editor.

The difference between Add data and the Data load editor is mainly in how you manage data. Add data provides assistance with creating data associations in your data model. The Data load editor enables you to build a data model with ETL (Extract, Transform & Load) processes using the Qlik data load script language. The script language enables you to perform complex transformations and create a scalable data model.

## Preparing a list of URLs that Direct Access gateway can access

Information noteThis procedure is only relevant if you selected the REST (via Direct Access gateway) data connection.

To allow access to URLs, you need to edit the restconnector\_allowed\_urls.txt file on the Direct Access gateway machine.

To do this:

1. On the Direct Access gateway machine, open C:\ProgramData\Qlik\Gateway\restconnector\_allowed\_urls.txt as admin.
2. To allow all URLs, simply add \* to the file.
3. To allow specific URLs only, add each URL to a separate row, as in the following example:

   https://myprivaterestservice.com/restricted
   https://mypublicrestservice.com/all
4. To allow any path under a specified URL, add the URL to a separate row and append it with a \*, as in the following example:

   https://myprivaterestservice.com/restricted\*

   In the above example, the URL, https://myprivaterestservice.com/restricted/admin will also be accessible.
5. Save the file and restart the Direct Access gateway service.

## Specifying the data retrieval method

Do the following:

1. In Qlik Cloud you can select Add data from an application or add as a data source in a space. You can also use the Data load editor.
2. From Add data, select REST from the list of connectors.

   From Data load editor, select Create a new connection in the Data connections column to get a list of connectors.
3. From the Data gateway drop-down list, select the data gateway that you need to use to connect to your data source.

   Information note
   - This field will only appear if you selected the "via Direct Access gateway" data connection.
   - Users that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides.
4. Enter the URL of the resource being requested from the REST service.

   The URL syntax must include http://. In addition to the location, the URL can include query parameters and other information about the data being retrieved. The parameters allowed or required are specified by the particular implementation of REST used for the data source. For example, a URL to Google Maps can be:

   http://maps.googleapis.com/maps/api/geocode/xml?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=false
5. Enter the Connection Timeout value in seconds.

   This is the time limit for the connection to be completed. If the connection request takes longer than the timeout value, an error message is displayed. The maximum is 10,000 seconds.
6. Enter Read/Write Timeout value in seconds.

   This is the time limit for how long it should take for data to be loaded after a successful connection. If a data reload request takes longer than the timeout value, an error message is displayed. The maximum is 10,000 seconds.
7. Select GET or POST from the Method list.

   The GET method retrieves information from the resource and does not change the state of the server. It is considered a *safe* method with regard to the server.

   The POST method creates a new entry in the resource. The entry is specified in the Request body field, which appears when the POST method is selected. The request or data sent with the POST method can be, for example, a message to a bulletin board or newsgroup.

   Information noteThe REST Connector sends the POST body without any transformation, even if a transformation is specified in the request header. If you want to encode the POST body, such as with the x-www-form-urlencoded format, you must do it manually. For example, to encode with the x-www-form-urlencoded format, the POST body would be written similar to following:

   format=json&start\_date=2018-10-30&finish\_date=2018-10-31&store=all&username=MarasSam&password=MarasSam0517
8. Enter the data to be posted to the resource with the POST method in the Request body field.

   If you use the GET method, this field is not displayed.
9. Select the HTTP Protocol version.
   Version 1.1 is the default selection because it is the newest version, and provides an automatic persistent HTTP connection. You can select 1.0 if your target web server requires that version, which also requires you to manually select whether to send keep-alive messages.
10. Select Add 'Expect: 100-continue' header if you have selected the POST method and the server you are posting to uses the 100 (Continue) initial response.

    When communicating with servers that respond with 100 (Continue), the initial request must include Expect: 100-Continue instead of sending the entire content of Request body. The content to be posted is then sent in the second request after the server responds with 100 (Continue).
11. Select Auto detect response type to detect the data format in the REST data source when the connection is made.

    If the data format is detected during connection, the Select data to load screen displays the fields required for selecting data in the source’s format when it opens. If Auto detect response type is not selected, you can use Auto detect on the Select data to load screen, or you can select the format manually if you know what it is.
12. Select Check response type during 'Test connection' to include verification that correct data format is returned.

    The Test Connection button at the bottom of the connection dialog in both the Qlik Sense Data load editor dialog verifies that the connection to the data source can be made and that the credentials are valid. When Check response type during 'Test connection' is selected, Test Connection also validates that the correct data format (JSON, CSV, or XML) is returned.

    In Qlik Sense Add data, the connection is tested automatically before proceeding to data selection. The test connection step is described below. [Test Connection](#Test_Connection).
13. Select Key generation strategy to use for creating primary and foreign keys in JSON and XML data.

    To associate parent and child fields appropriately, the connector generates ID fields to serve as primary and foreign keys. The key generation strategy determines how the keys are generated.

    - Sequence ID: Generates an ID for each child of a parent record. This strategy is simple and efficient, but it requires that the order of fields is the same in every record.
    - Current record: Generates a hash key based on all the values of the current record and uses that as the primary key. It also generates a hash key based on all the values of the direct parent and uses that as the foreign key.
    - Fully qualified record: Generates a hash key based on all the parent values.
    - No keys: Keys for parent-child relationships will not be shown in the Select data to load step, but they will be used in the SELECT statements.
14. Select XML DTD support to load an XML file with a DTD header.

    - Prohibited: A DTD header is prohibited and XML files with a DTD header will cause an unexpected DTD header error.
    - Internal Document: This option is for a DTD header that includes the entire definition in the XML.
    - Document in URL: This option is for a DTD header that includes a URL in the XML to link to the web available definition.

      Information noteThe REST Connector will not process or parse the DTD header of the XML document.

## Specifying credentials for the REST service on Qlik Cloud

Information noteTo connect to a REST API, you might need to update the TLS Cipher Suite.
[Updating the TLS Cipher Suite](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikDataTransfer/install-Qlik-DataTransfer.htm#SSL-config-settings)

Do the following:

1. Select an authentication mode from the Authentication Schema list.

   Authentication schema options

   | Schema | Description |
   | --- | --- |
   | Anonymous | Does not provide any authentication. Everyone using the connection has access to the resource. |
   | Basic | Sends a Base64-encoded string with a user name and password for the client. Base64 is not a form of encryption. It is the same as sending the user name and password in clear text. |
   | Digest | Provides a challenge-response. The server sends a string of random data called a nonce, and the server responds with a hash that includes the user name, password, and nonce along with additional information. The complexity of the response makes it difficult to steal and reuse the credentials.  The Digest schema requires the use of Windows domain accounts. The digest realm is the Windows domain name. A server cannot use Digest authentication unless it is running an operating system that supports Windows domains. In the case of a client that does not run an operating system with Windows domain support, the domain account must be explicitly specified during the authentication. |
2. Enter the user name and password for the REST account.

   These two fields do not appear if you have selected Anonymous or Current Windows User (NTLM) because they are not needed.
3. Use the Certificate validation list to select one of three options:

   - Select Skip server certificate validation if you do not need to verify that the web site server's public certificate is valid. The server certificate is checked even if you select Skip server certificate validation, but in that case, the connection will be made even if the certificate is invalid.
   - Select Use System Trust Store if you need the web site server’s certificate to be validated using root certificates installed in a system’s trust store.
   - Select Custom Root CA Certificate if you would like to upload and use a PEM file which contains root certificate(s). Use File button to select a file.
4. Select Enable mutual SSL/TLS to enable mutual verification. This is useful when the client also needs to be verified by the server using a client certificate. In this scenario the uploaded PFX file will be sent to the server and the check will be performed on the server side. The PFX file property allows you to upload a certificate that can verify the client to the server. The PFX file password is the password required to access the certificate data.
5. Specify Trusted locations by adding a URL with a port number to the Value field and an alias for the host identified by the URL to the Name field. If you specify multiple trusted locations, the alias names must be unique.

   The list of hosts specified as Trusted locations are the only hosts to which the user credentials can be sent. If a request is sent to a host that is not a trusted location, the user credentials will not be given to that host.
6. If you are using the Data load editor you can click Test Connection to verify that a connection can be made with the REST service properties entered.

   In both Data load editor and Add data, the connection is tested before it is created. Clicking Test Connection in the Data load editor enables you to test the connection before you attempt to create it.

## Specifying additional request parameters

Do the following:

1. For additional query parameters:

   1. Enter the Name and Value for each additional query parameter you want to include in the URL. Use the ![Create new](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove parameters as needed.

      Query parameters are specific to the REST service to which you are connecting. They can specify information to return. For example, a parameter named “filter” could be used to specify a value such as “salary>10000.” Query parameters can also be used to provide security keys.

      Names used in the Query parameters section must be unique. To specify multiple query parameters with the same name, you must place the names and values in the URL or use the WITH CONNECTION keyword in the load script.

      The WITH CONNECTION keyword can be added to the script in the Data load editor.

      [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm)

      To place identically named query parameters in the URL, add them consecutively as in the following simple example:

      http://localhost:9999/echo?q=3&q=4
   2. Select Add missing query parameters to final request to add any parameters specified in the Query parameters fields to any URL that does not automatically get the parameters.

      Any parameters in the Query parameters fields are automatically added to the URL in the URL field at the top of the Create new connection (REST) dialog when the Select data to load dialog is opened or data is loaded. However, in the case of Next URL pagination, the URLs returned by the data source after the first page of data is requested do not have the query parameters specified in the Query parameters fields. If Add missing query parameters to final request is selected, those query parameters are added to each of the URLs used to get subsequent pages.

      Add missing query parameters to final request also affects the URLs used in WITH CONNECTION statements. If a query parameter is not explicitly included in the WITH CONNECTION statement, it will be added if Add missing query parameters to final request is selected.

      [*Using WITH CONNECTION for pagination*](../Load-REST-data/Load-data.htm#WITH-CONNECTION-pagination)
2. For additional query headers:

   1. Enter the Name and Value for each additional query header you want to include in the *http* request header. “Accept-Language” is an example of a query header. To specify English as the language, you would use the value “en.” Use the ![Create new](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove parameters as needed.
   2. Optionally, select the Encrypt check box. This is best practice If you enter sensitive information such as an authorization request header.
   3. Select Allow "WITH CONNECTION" to use the “WITH CONNECTION” keyword in load statements. If your load statement includes “WITH CONNECTION” and this option is not selected, an error will occur.

      For information about using the "WITH CONNECTION" keyword in load statements, see [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm).
   4. Select Retry failed requests to retry failed REST calls. This will enable retry for error codes 429 and 503 if there is a Retry-After header. Optionally, enter a comma-separated list of HTTP code errors to retry in the Retry codes field. This list works only with 5xx server error codes.

   Warning noteIf you use Date as a query header, it must have the format: yyyy-MM-dd-HH:mm:ssZ. For example, 2014-09-28 16:25:09Z. Any other format produces an error.

## Specifying the type of pagination

Do the following:

1. Select the type of paging to use from the Pagination Type menu.

   To select the appropriate type of paging, you must know how the data source to which you are connecting implements the REST API. The REST API allows for Offset, Next page, Next token, Next URL, and Custom pagination. You can also choose None from the list of Pagination Type selections.

   [*Loading paged data*](Loading-paged-data.htm)

## Specifying security

Do the following:

1. Select Allow response headers to permit responses from the data source to return header fields in responses.

   By default, headers are not allowed in responses.

   Warning noteThe Qlik REST Connector supports the ability to include HTTP headers in the response object. Starting with version 1.2, loading of the headers does not happen by default. It must be explicitly allowed. Existing connections that load the response headers must be reconfigured with the Allow response headers parameter.
2. Select Allow HTTPS only to require that all URLs use the HTTP security protocol (HTTPS).

   If Allow HTTPS only is selected, all URLs must use HTTPS. That includes the URL used for the initial REST connection and all the URLs in the allowlist.
3. Add an allowlist of URLs that can be used when queries are redirected.

   The URLs in the allowlist are the only URLs to which responses can redirect for paged data.

   Specify a URL in the Value field and create an alias for the host identified by the URL in the Name field. If you specify multiple URLs, the alias names must be unique. If Allow HTTPS only has been selected, then all URLs on the allowlist must use HTTPS.
4. Check Use cookie container when redirect option if a query is redirected to another URL and authentication cookie obtained from original URL needs to be set in a redirected request.

## Completing the connection

Do the following:

1. In Qlik Sense, enter a name for the connection in the Name field.

   The Name field contains a default name for the connection. You can use that name or replace it with another name.
2. In Add data, click Create to create the connection and move to the data selection step.

   In Data load editor, click Create to create the connection that will be used when loading data from the REST resource.

In Add data, the data selection step follows immediately when the connection is created, but in Data load editor, you must initiate data selection.

[*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm)
