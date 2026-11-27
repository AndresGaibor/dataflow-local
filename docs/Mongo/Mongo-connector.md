---
title: "MongoDB"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Mongo/Mongo-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# MongoDB

Connections to a MongoDB database are made by selecting MongoDB from the list of drivers in the list of connectors in the Qlik Sense Add data or Data load editor dialogs.

MongoDB is a NoSQL database program. It uses JSON-like documents with schemas.

Information noteIndustry-accepted best practices must be followed when using or allowing access through the ODBC Connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.

## Supported MongoDB versions

The followings database versions are supported:

- 6.0
- 7.0
- 8.0

## Supported MongoDB data types

The following MongoDB data types are supported by the MongoDB Connector.

- Date
- DBPointer
- Decimal
- JavaScript
- JavaScript (with scope) -- Not supported as string. Converts to SQL\_VARCHAR.
- LongVarbinary
- MaxKey
- MinKey
- NumberDouble
- NumberInt
- NumberLong
- ObjectID
- Regular Expression
- String
- Symbol
- Timestamp
- Undefined
- Varbinary
