---
title: "Understanding the subscription value meters"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/subscription-value-meters.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Planning your Qlik Cloud deployment"]
---

# Understanding the subscription value meters

Value meters determine pricing and billing for Qlik Cloud subscriptions by measuring resource usage. Capacity-based subscriptions primarily use data volume, but the specific value meters depend on your subscription type.

## Subscription value meters by subscription type

The following table shows the primary value meters for each subscription type:

Subscription value meters

| Subscription option | Value meters |
| --- | --- |
| Qlik Cloud Analytics Starter | Users |
| Qlik Cloud Analytics Standard | Data for Analysis |
| Qlik Cloud Analytics Premium | Data for Analysis |
| Qlik Cloud Enterprise | Data for Analysis, Data Moved |
| Qlik Talend Cloud Starter | Data Moved |
| Qlik Talend Cloud Standard | Data Moved, Open Lakehouse compute |
| Qlik Talend Cloud Premium | Data Moved, Third-party data transformations ($/GB), Job execution, Job duration, Open Lakehouse compute |
| Qlik Talend Cloud Enterprise | Data Moved, Third-party data transformations ($/GB), Job execution, Job duration, Open Lakehouse compute |
| Qlik Anonymous Access | Anonymous Capacity, Anonymous Concurrent Sessions |

## Monitoring resource usage

Administrators can track usage of Data for Analysis, Data Moved, and other resources in the Administration activity center and the Data Capacity Reporting App.

For more information, see:

- [*Monitoring resource consumption*](mc-monitor-consumption.htm)
- [*Monitoring detailed consumption for capacity-based subscriptions*](usage-metrics-app.htm)

For more information about the license metrics, see the [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) product description.

## Data for Analysis

Qlik Cloud Analytics is measured on Data for Analysis volume. This value meter counts the total volume of data loaded into and analyzed in Qlik Cloud. Your monthly peak usage is compared against your purchased capacity. Exceeding your capacity may incur overages.

For detailed information on what data is included, how usage is calculated, and best practices for managing your data, see [*Data for Analysis*](subscription-value-meters-data-for-analysis.htm).

## Data Moved

The Data Moved metric is the sum of all data moved to a target. You can move data to any type of target. The type of sources you can move data from depends on your subscription. There is no limit on the number of targets or sources.

### How data moved is calculated

Data Moved is measured from the beginning of the month. It is counted as it is landed on the target. This means that the same data replicated to two different targets is counted twice. The initial full load of new tables or files is free and is not counted.

The Data Moved volume is calculated as the number of rows in the dataset multiplied by the estimated row size. The estimated row size is calculated as the total size of all the columns in a row, based on the data type of each column. For details on how the internal representation of the data types maps to your target schema, see [Connecting to cloud data platforms in your data projects](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/data-project-connections.htm) and go to the Data types section in the topic for your cloud data platform.

Information note

The row count used in the calculation of the Data Moved volume might differ slightly from the expected value. These small differences are expected and caused by technical artifacts that cannot be controlled by Qlik.

For example, when loading a big table, the database might send the same row twice (phantom reads) or count a row both as reload and as a change row. Differences might also arise in change counts when a change causes a trigger execution, which makes additional unexpected changes, and the change counts are read from a transaction log or a change source.

The Data Moved calculation is based on the landing dataset as it appears in Qlik Cloud. Changes to this dataset will be taken into account, such as adding new columns. If you are trying to reproduce the Data Moved volume calculations, make sure that you are using the right data types as they appear in Qlik Cloud and not the source, as this affects the column size in the calculation. For example, using varchar(20) instead of varchar(10) doubles the column contribution to the estimated row size.

### Data types and sizes used in the calculation

The following table lists the size of each data type. The min() function used for bytes, string, and wstring returns the smallest of the two values, either length/2 or 200.

Sizes for Qlik Cloud data types

| Data type | Size (in bytes) |
| --- | --- |
| Unspecified | 1 |
| BOOLEAN | 1 |
| BYTES(length) | min(length/2, 200) |
| DATE | 4 |
| TIME | 4 |
| DATETIME | 8 |
| INT1 | 1 |
| INT2 | 2 |
| INT4 | 4 |
| INT8 | 8 |
| REAL4 | 2 |
| REAL8 | 4 |
| UINT1 | 1 |
| UINT2 | 2 |
| UINT4 | 4 |
| UINT8 | 8 |
| NUMERIC | 2 |
| STRING(length) | min(length/2, 200) |
| WSTRING(length) | min(length/2, 200) |
| BLOB | 200 |
| CLOB | 200 |
| NCLOB | 200 |
| JSON | 200 |

Example: Calculating Data Moved volume

In this example we have a dataset for product categories. The dataset has 100 rows and the following columns:

| Column name | Data type |
| --- | --- |
| CategoryID | INT4 |
| CategoryName | WSTRING(15) |
| Description | NCLOB |
| Picture | BLOB |

There is a fixed size for each data type:

| Data type | Size (in bytes) |
| --- | --- |
| INT4 | 4 |
| WSTRING(15) | min(15/2, 200) = 7.5 |
| NCLOB | 200 |
| BLOB | 200 |

We can now calculate the estimated row size as the sum of the column sizes: 4 + 7.5 + 200 + 200 = 411.5 bytes. Multiplied by 100 rows, this gives us a total data volume of 41,150 bytes.

## Third-party data transformations

This metric applies to all datasets that are registered using the data task for Registered data. Third-party transformations are measured in $/GB from the beginning of the month.

GB for third-party data transformations is calculated with the same logic as Data Moved: the number of rows in the dataset multiplied by the estimated row size. For more information about estimating row size, see [*Data Moved*](#Data2).

When processing data through the Registered data task, full or initial load processing is counted toward the capacity. Subsequent executions will detect changed rows, and will only count changed records.

## Open Lakehouse compute

Open Lakehouse compute is a usage metric measured in core-hours. It applies to streaming workloads that run on streaming-enabled Qlik Open Lakehouse clusters.

Streaming workloads are supported by these task types:

- Streaming landing
- Streaming transform

Streaming workloads can only run on streaming-enabled clusters. For details, see [*Managing lakehouse clusters*](../DataIntegration/Lakehouse/manage-clusters.htm).

Information noteCDC and other non-streaming workloads that run on CDC-enabled lakehouse clusters are measured by the Data Moved metric.

### How core-hours are calculated

Open Lakehouse compute shows the total core-hours used for streaming workloads on Qlik Open Lakehouse clusters during the billing month.

Core-hours are counted only while a streaming task (or an associated maintenance task) is running on the cluster. If the cluster is running but no streaming tasks are executing, core-hours are not counted.

Clusters with more CPU cores consume core-hours faster. For example:

- An 8-core system running for 1 hour uses 8 core-hours.
- A 16-core system running for 1 hour uses 16 core-hours.

Example: Calculating core-hours

A streaming-enabled lakehouse cluster with two 8-core instances, running 24 hours a day for 31 days (no autoscaling), uses:

2 × 8 × 24 × 31 = 11,904 core-hours

### Progressive conversion scale for large workloads

For large-scale workloads, the following conversion scale is applied to Open Lakehouse compute:

- 0–48,000 core-hours: 100% of the hours are counted.
- 48,001–186,000 core-hours: 50% of the hours are counted.
- Above 186,000 core-hours: 10% of the hours are counted.

## Job execution and Job duration

Job execution and Job duration are the main metrics for Talend Data Fabric capabilities that are included in Qlik Talend Cloud subscriptions.

### How job execution is counted

Job executions are the total number of job runs executed and concluded in a given month. A job is identified as a distinct Artifact ID, as reported in the Talend Management Console. Always-On Jobs are counted once in each month the job is running.

### How job duration is calculated

Job duration is the total duration in minutes, measured from the time a job starts until it stops. For batch jobs, the duration is counted in the month the job successfully ends. For Always-On Jobs, duration is measured from the start execution time in each month the job is running.

The actual duration is converted to a chargeable metric using a progressive conversion scale:

- 0–24,000 hours: 5% of the hours are counted.
- Above 24,000 hours: 1% of the hours are counted.

## Anonymous Capacity

Anonymous Capacity is only applicable to Qlik Anonymous Access subscriptions.
This value meter refers to the total RAM usage that all applications loaded into memory can consume at a given time. This includes tenant user sessions (sessions opened by users and administrators within the tenant) and anonymous user sessions (sessions opened by users who are not logged into the Qlik Cloud tenant).

The Anonymous Capacity of a tenant is defined by the purchased amount purchased within the subscription.

## Anonymous Concurrent Sessions

Anonymous Concurrent Sessions is only applicable to Qlik Anonymous Access subscriptions.
This value meter defines the maximum number of application sessions that can be run concurrently by anonymous users (users who are not logged into the Qlik Cloud tenant).

The Anonymous Concurrent Sessions of a tenant is defined by the purchased amount purchased within the subscription. You can purchase up to 1000 sessions. For more information, see [*Qlik Anonymous Access specifications and capacity limits*](../Introduction/qcs-specs-capacity-anonymous-access.htm).
