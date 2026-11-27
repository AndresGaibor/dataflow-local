---
title: "Creating an on-demand selection application"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/creating-OnDemand-selection-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Managing big data with on-demand applications"]
---

# Creating an on-demand selection application

An on-demand selection application provides the means for selecting subsets of large data sets so that the Qlik associative engine can make associations efficiently and effectively. In very large data volume environments, we recommend that you have the selection application load only a modest level of [dimension](#glossary-0 "Glossary term") granularity. For example, a selection application whose data is based on sales data aggregated by quarter, region, and product category could use an SQL SELECT statement such as the following:

```
SELECT 	SUM(S.UNIT_COST) AS TOTAL_UNIT_COST,
	SUM(S.QUANTITY) AS TOTAL_QUANTITY,
	SUM(S.UNIT_PRICE * S.QUANTITY) AS TOTAL_SALE,
	SUM( (S.UNIT_PRICE - S.UNIT_COST) * QUANTITY) AS TOTAL_PROFIT,
	SUM(1) AS TOTAL_LINE_ITEMS,
	S.REGION,
	S.YEARQUARTER,
	S.PRODCAT,
FROM SALE_DETAIL S
GROUP BY S.REGION, S.YEARQUARTER, S.PRODCAT
```

The on-demand [measure](#glossary-1 "Glossary term") expression property is typically based on a computed aggregate result from an SQL GROUP BY query used to load the data. Because the selection application uses a GROUP BY query to aggregate the SALE\_DETAIL records, an [aggregation](#glossary-2 "Glossary term") function--in this case SUM--must be used on the measure fields of UNIT\_COST, QUANTITY and the computed values for TOTAL\_SALE and TOTAL\_PROFIT.

The SUM(1) AS TOTAL\_LINE\_ITEMS provides a way to precisely measure the total number of sale line items for every distinct combination of region, quarter, and product category. When creating a link used to produce on-demand applications, a measure expression must be supplied as way to control the number of records loaded into the on-demand applications. In the SALE\_DETAIL example, when a user selects multiple product categories, regions, and/or quarters, a sum can be computed for TOTAL\_LINE\_ITEMS to determine whether or not the selection exceeds the record limit for the on-demand application.

Record limits are specified when the selection application is linked to a template application to create an application navigation link. Each application navigation link has a record limit. Multiple navigation links can be created from the selection application. Multiple application navigation links are commonly made linking a selection application to different template applications in order to produce multiple views of data.

Individual on-demand application navigation links can be included in a selection application for publication. Once included in the selection application, an application navigation link is used to create one or more application navigation points that make it possible for users of specific [sheets](#glossary-4 "Glossary term") to create on-demand applications based on that link’s template application.

For information about how to create an on-demand application, see [*Building an on-demand application*](creating-OnDemand-app.htm).

Information note

Once an on-demand selection application is published to a managed space, you cannot edit the navigation link in the selection application or published application. If you need to update the navigation link, delete the published application. Next, edit the link in the selection application, and publish the application again to the managed space.
