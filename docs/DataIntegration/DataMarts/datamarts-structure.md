---
title: "Data mart view structure"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataMarts/datamarts-structure.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Creating and managing data marts"]
---

# Data mart view structure

This topic describes the internal header columns (identifiable by their hdr\_\_ prefix) of the data mart views. Data pipelines often culminate in data marts, which denormalize data into star schemas. Facts present a convenient structure for consumption by analysts using dimensional modeling. Therefore, understanding the role of the header columns will allow you to generate more focused reports for analytics and consumption by downstream applications.

## Fact view

View name format: <DATA\_ASSET\_SCHEMA>.[<PREFIX>]<FACT>

The following header columns are added to the view structure:

Table header fields

| Column | Type | Description |
| --- | --- | --- |
| hdr\_\_deleted | Boolean | Indicates whether or not the record was deleted from the fact table. |
| hdr\_{dimension-name}\_key\_id | int64 | Reference to Type 1 and Type 2 dimensions. The fact view will contain a separate column for each dimension in the fact.  Example:  hdr\_\_EMPLOYEES\_key\_id |

## Type 1 dimension view

View name format: <DATA\_ASSET\_SCHEMA>.[<PREFIX>]<DIMENSION>

The following header columns are added to the view structure:

Table header fields

| Column | Type | Description |
| --- | --- | --- |
| hdr\_{dimension-name}\_key\_id | int64 | Sequence incremented per record. |
| hdr\_\_deleted | Boolean | Indicates whether or not the record was deleted from the dimension table. |

## Type 2 dimension view

View name format: <INTERNAL\_SCHEMA>.[<PREFIX>]<DIMENSION>

The following header columns are added to the view structure:

Table header fields

| Column | Type | Description |
| --- | --- | --- |
| hdr\_{dimension-name}\_key\_id | int64 | Sequence incremented per record. |
| hdr\_\_from\_timestamp | timestamp | The UTC start timestamp for this version of the record. For example, the column might indicate the date a customer started living at a certain address.  This column allows you to:   - Analyze data based on historical information. For example, you could determine the length of time an order was in pending state or how a change in a customer's address impacts sales compared to last year's data. - Analyze data by date, but knowing what you know now. By contrast, the hdr\_\_was\_current\_from\_timestamp described below allows you to analyze data by a specific date, knowing only what you knew then.   For a Type 2 dimension with denormalized entities, this is the timestamp from the updated dataset in the Storage or Transform data asset. |
| hdr\_\_to\_timestamp | timestamp | The UTC end timestamp of the record version. The column is used to delimit the range of dates for a given record version. For example, the column could indicate the date a customer stopped living at a certain address.  See also the description of the hdr\_from\_timestamp column above. |
| hdr\_\_operation | varchar(1) | Full load operations:   - L: Inserted during full load   Change processing operations (using Change Tables):   - D: Deleted - U: Updated - I: inserted   Actions resulting from compare and apply operations:   - d: Deleted - u: Updated - i: Inserted |
| hdr\_\_was\_current\_from\_timestamp | timestamp | Shows the UTC timestamp of when the last update was applied to the record.  This column together with the hdr\_\_was\_current\_to\_timestamp column, allows you to analyze data by a specific date, knowing only what you knew then. For example, let's say that every day you calculate the total of the previous day's orders at 2:00 am. So on December 1st, the total sum of the previous day's orders is $1,000,000. However, on December 2nd, a record is inserted saying that on November 30th, an order totaling $500,000 was placed. So the order amount for November 30th was actually $1,500,000! However, if you generate a report for the total sum of orders on November 30th based on what was current on December 1st at 2:00 am, the result would still be $1,000,000. |
| hdr\_\_was\_current\_to\_timestamp | timestamp | This column is populated when a record is replaced with a newer record. It shows the UTC timestamp of when the record was processed, and therefore no longer the latest record.  See also the description of the hdr\_\_was\_current\_from\_timestamp column above. |
