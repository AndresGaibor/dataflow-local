---
title: "Infor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Infor-Data-Fabric-Lake.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Infor

Infor Data Fabric is Infor's cloud-native data management platform. It provides capabilities for big data storage, real-time data delivery, querying, and advanced data management tooling. It supports an ecosystem of more than 30 Infor applications and services.

Infor Data Lake is a component of Infor Data Fabric. It provides high-volume, scalable object storage for real-time data from CloudSuite applications, third-party systems, and other data producers. Data Fabric is the management and connectivity layer, and Data Lake is the underlying storage layer.

Infor Data Fabric / Data Lake integration replicates data using the [Compass SQL API v2](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/default.html?helpcontent=uan1631199548644.html). The [Compass API documentation](https://docs.infor.com/inforos/2026.11/en-us/useradminlib_cloud/datafabrug/ufj4977568588442.html) recommends this API for most Data Lake query and extraction scenarios, including large result sets, long-running queries, scheduled integrations, and data pipelines. For other scenarios, review the Infor documentation for API guidance.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Infor account, you need:

- An active Infor CloudSuite subscription with Data Fabric / Data Lake enabled.
- Access to Infor OS with ION API Gateway Administrator rights (`IONAPI-Administrator` role), or the ability to request that an authorized app is created for you.
- A Backend Service authorized application registered in ION API Gateway, with a service account and a downloaded `.ionapi` credential file.
- A service account user with read access to the Data Lake tables that you want to replicate.

The `.ionapi` credential file is generated in Infor OS and contains the OAuth client credentials and service account keys required for authentication.

You can download these credentials only once. Store the file securely.

To obtain the `.ionapi` credential file:

1. Log into your Infor account.
2. In Infor OS, navigate to API Gateway > Authorized Apps.
3. Click +.
4. Enter the following information for your application:
   - Name: Enter a name.
   - Type: Select Backend Service.
   - Description: Enter a description.
5. Click Save.
6. Click Download Credentials.
7. Enable Create Service Account.
8. Select a user to associate with the service account.

   The selected user defines the data that the connector can access.

   Optionally, select one or more scopes that the service account can access.
9. Click DOWNLOAD to save the `.ionapi` credential file.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| ION API File Content | The JSON content of the `.ionapi` credential file. Open the file in a text editor and paste the full content into this field. |
| Variation Handling | Controls which record versions are included in replication. Default: Latest. |
| Date Window Size | Number of days per query window for incremental replication. Date windowing keeps queries on large tables within Compass execution limits. Default: 180. Fractional values are supported (for example, 0.5 = 12 hours). |

### Variation handling options

Infor Data Lake tracks multiple versions of each record, including deletions and archival states. For more information, see the [Infor Data Lake documentation](https://docs.infor.com/inforos/2024.x/en-us/useradminlib_cloud/datafabrug/gve1631199565990.html).

Variation handling settings

| Display Name | Config Value | Description |
| --- | --- | --- |
| Latest | `latest` | Replicates only the current, live version of each record (excludes deleted and archived). |
| Include Deleted | `include_deleted` | Replicates current records and those soft-deleted at the source. |
| Include Deleted and Archived | `include_deleted_and_archived` | Replicates current, deleted, and archived records. |
| All Variations | `all_variations` | Replicates every historical version of each record (excludes archived). |
| All Variations Including Archived | `all_variations_include_archived` | Replicates all historical versions of each record, including archived ones. |

### Replicated tables

All tables available in your organization's Infor Data Lake can be selected for replication in Qlik Talend Cloud. The specific tables you see depend on which data objects your CloudSuite applications and any third-party sources have published to your Data Lake.

To explore available data objects, use the Atlas tool within Infor Data Fabric.

Each table is incrementally replicated based on the `last_modified` timestamp, which is populated by Infor's `infor.lastModified()` system function. Primary keys for each table are automatically determined from Infor's Data Catalog API.

## Limitations and considerations

- Compass queries are processed asynchronously. Each query is submitted as a job, monitored for status, and results are retrieved when the job completes. Large datasets may require additional processing time.
- A rate limit of 100 query submissions per minute applies to the Compass SQL API. Qlik Talend Cloud handles rate limiting and retries automatically.
- Query results remain accessible for approximately 20 hours after the job completes.
- The connector waits up to 10 minutes for each Compass query to complete. If a query does not finish within that time, the task stops with an error. Reduce Date Window Size to keep queries on large tables within this limit.
- The connector supports Data Lake objects in newline-delimited JSON and delimiter-separated values (DSV) formats.
