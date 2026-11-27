---
title: "Using pagination with selected REST sources"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/Create-REST-connection/Pagination-scenarios.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "REST data sources", "Create a REST connection"]
---

# Using pagination with selected REST sources

The following procedures explain how to complete the properties associated with the pagination options in the Qlik REST Connector. Pagination is used when there is more data to load than the data source provides in a single load. You must specify how the connector is to page through the entire set of data you want to load. REST APIs have different mechanisms for pagination, and you must know which mechanism the selected data source uses before you can select a pagination option in the REST Connector and complete the required property fields.

The Qlik REST Connector supports the following paging options. Some data sources implement the REST API to support multiple types of pagination, but most sources support only one.

- None is used when no paging is supported. Some REST API implementations simply return records with a single call and do not allow subsequent calls. The None option can also be selected if you do not want to use a paging option. In that case, only the first set of records is returned.
- Offset uses a starting value from which to read additional records.
- Next page uses field names and values and page sizes to determine how to read additional records.
- Next token uses a token that is passed to the URL call for the next set of records.
- Next URL uses a value that contains the URL for the next set of records.
- Custom is a special option that can be used when none of the other paging options are implemented. It allows the user to write a customized query to return a set of records. The Custom option can also be used with data sources that support Offset, Next token, and Next URL. If you want to customize the load script in some way that is not handled by one of the other options, you can, in most cases, use the Custom option.

Warning noteWhen specifying field names in any of the pagination fields described below, you must use the name as returned by the data source, not the name displayed by the connector in the selection dialog. The connector renames some fields in some cases, such as when a field name is duplicated in different levels of a JSON or XML document. For example, the field name "total," used in Total field path, might be renamed "total\_u1" by the connector.

## Using Offset pagination with govtrack.us and ServiceNow

The site govtrack.us uses the Offset method to page through large data sets. In this use case, the query requests data on the terms held in office by current members of the US Congress, President, and Vice President. The URL to use is:

https://www.govtrack.us/api/v2/role?current=true

Do the following:

1. Set Timeout to 30.
2. Select GET from the Method drop-down menu.
3. Select 1.1 from the HTTP Protocol drop-down menu.
4. Select Auto detect response type to have the connector detect the format of the govtrack.us data set you are accessing.
5. Select Sequence ID as the Key generation strategy to use for creating primary and foreign keys in the data.

   The order of fields is the same in every record from govtrack.us, so Sequence ID can be used. It is the simplest and most efficient of the key generation options.
6. Use the Anonymous setting for Authentication Schema.

   The govtrack.us site does not require authentication, so credentials and certificates are not needed.
7. Select Offset as the Pagination Type.
8. Complete the Pagination fields as follows:

   Pagination Type: Offset

   'Start' parameter name: offset;

   'Start' initial value: 0

   'Count' parameter name: limit;

   'Count' initial value: 100

   'Total records' path: root/meta/total\_count

   The names for 'Start' parameter name, 'Count' parameter name, and 'Total records' path come from govtrack.us. You must use those names so the connector knows where to find the values for each successive page request.

   The 'Start' initial value must be 0 if you intend to start at the beginning of the data set because govtrack.us uses 0 as the base value.

   The'Count' initial value of 100 is the default. The maximum on govtrack.us is 600.

   Data indicator path is not required for govtrack.us because the total is contained in total\_count.
9. Skip the Query parameters and Query headers fields because no additional parameters or headers are required.
10. Enter a name for the connection to govtrack.us in the Name field.

    [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm)

ServiceNow is a commonly used IT management system. It also uses the offset method.

1. Set Timeout to 30.
2. Select GET from the Method drop-down menu.
3. Select 1.1 from the HTTP Protocol drop-down menu.
4. Select Auto detect response type to have the connector detect the format of the ServiceNow data set you are accessing.
5. Select Sequence ID as the Key generation strategy to use for creating primary and foreign keys in the data.

   The order of fields is the same in every record from govtrack.us, so Sequence ID can be used. It is the simplest and most efficient of the key generation options.
6. Use the Basic setting for Authentication Schema and enter the user name and password for your ServiceNow account.
7. Select Offset as the Pagination Type.
8. Complete the Pagination fields as follows:

   Pagination Type: Offset

   'Start' parameter name: sysparm\_offset;

   'Start' initial value: 0

   'Count' parameter name: sysparm\_limit;

   'Count' initial value: 10000

   'Total records' path: X-Total-Count; ![ ](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/Icons/ic_tick.svg)Look in header

   The names for 'Start' parameter name, 'Count' parameter name, and 'Total records' path come from ServiceNow. You must use those names so the connector knows where to find the values for each successive page request.

   The 'Start' initial value must be 0 if you intend to start at the beginning of the data set because ServiceNow uses 0 as the base value.

   Data indicator path is not required for ServiceNow because the total is contained in X-Total-Count.
9. Skip the Query parameters and Query headers fields because no additional parameters or headers are required.
10. Enter a name for the connection to ServiceNow in the Name field.

    [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm)

## Using Next page pagination with Best Buy

The Best Buy electronics store chain uses the Next page method to page through large data sets. In this use case, the query requests all the Best Buy stores in Massachusetts. The URL to use is:

http://api.bestbuy.com/v1/stores%28region=ma%29?format=json&show=storeId,city,region

Do the following:

1. Set Timeout to 30.
2. Select GET from the Method drop-down menu.
3. Select 1.1 from the HTTP Protocol drop-down menu.
4. Select Auto detect response type to have the connector detect the format of the Best Buy data set you are accessing.
5. Select Sequence ID as the Key generation strategy to use for creating primary and foreign keys in the data.

   The order of fields is the same in every record from Best Buy, so Sequence ID can be used. It is the simplest and most efficient of the key generation options.
6. Use the Anonymous setting for Authentication Schema.

   Best Buy does not require authentication, so credentials are not needed. You do, however, need an apiKey, which is entered in Query parameters.You get an access token by signing into your Best Buy developers account.

   [*Setting up selected REST sources for data loading*](Connection-examples.htm).
7. Select Next page as the Pagination Type.
8. Complete the Pagination fields as follows:

   Pagination Type: Next page

   'Next page'
   parameter name: page

   'Next page'
   initial value: 1

   'Page size' parameter name: pageSize

   'Page size' value: 10

   'Total pages' path: root/totalPages

   The names 'Next page'parameter name, 'Page size' parameter name, and 'Total pages' path come from Best Buy. You must use those names so the connector knows where to find the values for each successive page request.

   The 'Next page'initial value must be 1 if you intend to start at the beginning of the data set because Best Buy uses 1 as the base value.

   The'Page size' value of 10 is the default. The maximum on Best Buy is 100.

   Data indicator path is not required for Best Buy because the total is contained in totalPages.
9. Enter the access token in Query parameters, as follows:

   Name: apiKey

   Value: CAACEdEose0CBAJgeyNljksdf2lou4qerqe8mv1BMYKMoPFeQj

   The access token shown for the Value parameter here is a sample to illustrate what the tokens look like. You must get your personal access token by signing into your Best Buy developers account.

   [*Setting up selected REST sources for data loading*](Connection-examples.htm).
10. Enter a name for the connection to Best Buy in the Name field.

    [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm)

## Using Next URL pagination with Facebook

Facebook uses the Next URL method to page through large data sets. In this use case, the query requests data on the Facebook account holder's friends. The configuration described here has been verified to return the intended results, but there are several issues to be aware of when constructing Facebook queries.

The REST Connector expects consistency in the data. In some cases, the format Facebook returns changes from one page to the next. When the page format is different, the REST Connector returns an error. To avoid this, you can create multiple queries instead of trying to return all the data in a single call. For example, you could create a query to return details of Facebook posts that have a 1-to-1 relationship with the post and create a separate query to return items with multiple values per post, such as comments.

Information note
'Next URL'
 value from the response always has the format .../{obj\_id}/{collection}. For example, .../me/posts?limit=5. If you use .../me?fields=posts.limit(5) as the initial URL, the response format will not be consistent with next data pages.

Do the following:

1. Enter the URL: https://graph.facebook.com/me/friends?access\_token=
2. Append your Facebook access token to the URL.

   You get an access token by signing into your Facebook developers account.

   [*Setting up selected REST sources for data loading*](Connection-examples.htm).
3. Set Timeout to 30.
4. Select GET from the Method drop-down menu.
5. Select 1.1 from the HTTP Protocol drop-down menu.
6. Select Auto detect response type to have the connector detect the format of the Facebook data set you are accessing.
7. Select Sequence ID as the Key generation strategy to use for creating primary and foreign keys in the data.

   The order of fields is the same in every record from Facebook, so Sequence ID can be used. It is the simplest and most efficient of the key generation options.
8. Use the Anonymous setting for Authentication Schema..

   Facebook does not require authentication, so credentials are not needed.
9. Select Next URL as the Pagination Type.
10. Complete the Pagination fields as follows:

    Pagination Type: Next URL

    'Next URL'
    path: root/paging/next

    The path for 'Next URL'path comes from Facebook. You must use that path so the connector knows where to find the values for each successive page request.
11. Enter a name for the connection to Facebook in the Name field.

    [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm)

## Using Next token pagination with Google Analytics

Google uses the Next token method to page through large data sets, though you can also use the Custom method. That is covered in the next section below.

In this use case, the query requests an account summary. The URL to use is:

https://www.googleapis.com/analytics/v3/management/accountSummaries

Do the following:

1. Set Timeout to 30.
2. Select GET from the Method drop-down menu.
3. Select 1.1 from the HTTP Protocol drop-down menu.
4. Select Auto detect response type to have the connector detect the format of the Facebook data set you are accessing.
5. Select Sequence ID as the Key generation strategy to use for creating primary and foreign keys in the data.

   The order of fields is the same in every record from Google, so Sequence ID can be used. It is the simplest and most efficient of the key generation options.
6. Use the Anonymous setting for Authentication Schema.

   Google authenticates with an authentication token, which is entered in Query headers.You get an authentication token when you execute the method you have selected.

   [*Setting up selected REST sources for data loading*](Connection-examples.htm).
7. Select Next token as the Pagination Type.

   Complete the Pagination fields as follows:

   Pagination Type: Next token

   'Next token'
   parameter name: pageToken; ![ ](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/Icons/ic_tick.svg) Pass via header

   'Next token'
   path: root/nextPageToken; ![ ](../_images/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Resources/Images/Icons/ic_tick.svg) Look in header

   The path for 'Next token'path comes from Google. You must use that path so the connector knows where to find the values for each successive page request.
8. Enter the authentication token in Query headers, as follows.

   Name: Authorization

   Value: Bearer ya29.IwIyP6RQeRL-g2MS4p0CBAJge

   The authentication token is generated when you execute the method you have selected.

   [*Setting up selected REST sources for data loading*](Connection-examples.htm).
9. Enter a name for the connection to Google Analytics in the Name field.

   [*Select and load data from a REST data source*](../Load-REST-data/Load-data.htm)

## Using Custom pagination with Google Analytics

When the Custom option is selected, no additional fields are displayed. The Custom option inserts a script template in the Data load editor or Edit script dialog.

Information noteThe Custom option is available in Add data, but if you select it, you must go to the Data load editor to customize the script.

In this use case, the query requests an account summary. The URL to use is:

https://www.googleapis.com/analytics/v3/management/accountSummaries?max-results=100&start-index=1&fields=items%2CstartIndex%2CtotalResults%2Cusername

After the script template has been inserted n the Data load editor or Edit script dialog, you must adapt the script for the source from which you are retrieving data in order to retrieve all of the intended records.

The following script is the generated template before it has been adapted. As it is, the template script would retrieve only the first page of data.

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
	"__KEY_root",
	(SELECT
		"__FK_items",
		"__KEY_items",
		(SELECT
			"email",
			"displayName",
			"self",
			"__FK_creator"
		FROM "creator" FK "__FK_creator")
	FROM "items" PK "__KEY_items" FK "__FK_items")
FROM JSON (wrap on) "root" PK "__KEY_root"
WITH CONNECTION(Url "https://content.googleapis.com/calendar/v3/calendars/primary/events?key=AIzaS...");
// Action required: change URL included in 'WITH CONNECTION' as
// needed to support pagination for the REST source.
// Please see the documentation for "Loading paged data."

NEXT startAt;

[creator]:
LOAD	[email] AS [email],
	[displayName] AS [displayName],
	[self] AS [self],
	[__FK_creator] AS [__KEY_items]
RESIDENT RestConnectorMasterTable
WHERE NOT IsNull([__FK_creator]);

DROP TABLE RestConnectorMasterTable;
```

The following script illustrates how the template can be adapted to retrieve the desired number of pages in the Google Analytics data source. Without the adaptation, the script would retrieve only the first page of data.

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
	"__KEY_root",
	(SELECT
		"kind",
		"etag",
		"id",
		"status",
		"htmlLink",
		"created",
		"updated",
		"summary",
		"description",
		"location",
		"iCalUID",
		"sequence",
		"guestsCanInviteOthers",
		"privateCopy",
		"__KEY_items",
		"__FK_items",
		(SELECT
			"email",
			"displayName",
			"self",
			"__FK_creator"
		FROM "creator" FK "__FK_creator"),
		(SELECT
			"email" AS "email_u0",
			"displayName" AS "displayName_u0",
			"self" AS "self_u0",
			"__FK_organizer"
		FROM "organizer" FK "__FK_organizer"),
		(SELECT
			"dateTime",
			"__FK_start"
		FROM "start" FK "__FK_start"),
		(SELECT
			"dateTime" AS "dateTime_u0",
			"__FK_end"
		FROM "end" FK "__FK_end"),
		(SELECT
			"email" AS "email_u1",
			"displayName" AS "displayName_u1",
			"self" AS "self_u1",
			"responseStatus",
			"__FK_attendees"
		FROM "attendees" FK "__FK_attendees"),
		(SELECT
			"useDefault",
			"__FK_reminders"
		FROM "reminders" FK "__FK_reminders")
	FROM "items" PK "__KEY_items" FK "__FK_items")
FROM JSON (wrap on) "root" PK "__KEY_root"
WITH CONNECTION(QUERY "startAt" "$(startAt)");
// Action required: change URL included in 'WITH CONNECTION' as
// needed to support pagination for the REST source.
// Please see the documentation for "Loading paged data."

NEXT startAt;

[creator]:
LOAD	[email] AS [email],
	[displayName] AS [displayName],
	[self] AS [self],
	[__FK_creator] AS [__KEY_items]
RESIDENT RestConnectorMasterTable
WHERE NOT IsNull([__FK_creator]);

[organizer]:
LOAD	[email_u0] AS [email_u0],
	[displayName_u0] AS [displayName_u0],
	[self_u0] AS [self_u0],
	[__FK_organizer] AS [__KEY_items]
RESIDENT RestConnectorMasterTable
WHERE NOT IsNull([__FK_organizer]);

[start]:
LOAD	[dateTime] AS [dateTime],
	[__FK_start] AS [__KEY_items]
RESIDENT RestConnectorMasterTable
WHERE NOT IsNull([__FK_start]);

[end]:
LOAD	[dateTime_u0] AS [dateTime_u0],
	[__FK_end] AS [__KEY_items]
RESIDENT RestConnectorMasterTable
WHERE NOT IsNull([__FK_end]);

[attendees]:
LOAD	[email_u1] AS [email_u1],
	[displayName_u1] AS [displayName_u1],
	[self_u1] AS [self_u1],
	[responseStatus] AS [responseStatus],
	[__FK_attendees] AS [__KEY_items]
RESIDENT RestConnectorMasterTable
WHERE NOT IsNull([__FK_attendees]);

[reminders]:
LOAD	[useDefault] AS [useDefault],
	[__FK_reminders] AS [__KEY_items]
RESIDENT RestConnectorMasterTable
WHERE NOT IsNull([__FK_reminders]);

[items]:
LOAD	[kind] AS [kind],
	[etag] AS [etag],
	[id] AS [id],
	[status] AS [status],
	[htmlLink] AS [htmlLink],
	[created] AS [created],
	[updated] AS [updated],
	[summary] AS [summary],
	[description] AS [description],
	[location] AS [location],
	[iCalUID] AS [iCalUID],
	[sequence] AS [sequence],
	[guestsCanInviteOthers] AS [guestsCanInviteOthers],
	[privateCopy] AS [privateCopy],
	[__KEY_items] AS [__KEY_items],
	[__FK_items] AS [__KEY_root]
RESIDENT RestConnectorMasterTable
WHERE NOT IsNull([__FK_items]);

DROP TABLE RestConnectorMasterTable;
```
