---
title: "ServiceNow"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-ServiceNow.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# ServiceNow

ServiceNow is a cloud platform for IT service management (ITSM), IT operations management, HR service delivery, security operations, and customer service workflows. You can use ServiceNow as a data source when landing or replicating data.

ServiceNow integration replicates data using the [ServiceNow Table API](https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/c_TableAPI.html) at the `/api/now/table` endpoint.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Grant the integration user read access through ACLs to the tables you intend to replicate and to the `sys_db_object` and `sys_dictionary` system tables, which the connector uses to discover available tables and their column definitions.

You need administrator permissions in your ServiceNow account to create the integration user.

To create a ServiceNow integration user:

1. Log into your ServiceNow instance, for example https://instance.service-now.com.
2. Navigate to All > User Administration > Users and click New.
3. Enter a User ID and set a password.
4. Clear Password needs reset to avoid requiring a password change at the user's next login.
5. Click Save.
6. Assign a role that grants read access to the tables you intend to replicate. A read-only role scoped to the required tables is preferred over a broadly privileged role such as admin.

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
| Instance | The instance subdomain of your ServiceNow account.  Example: For https://dev12345.service-now.com, enter dev12345. |
| Username | User ID. |
| Password | Password. |

## Schema

The set of available tables is instance-specific and determined at discovery time. The connector enumerates all tables from `sys_db_object`, resolves each table's inherited columns by walking its `super_class` chain, and reads column data types from `sys_dictionary`. You then select which discovered tables and fields to replicate. Commonly replicated tables include `incident`, `problem`, `change_request`, `task`, `sys_user`, and `cmdb_ci`, but the exact catalog depends on your instance and the integration user's permissions.

Every table uses `sys_id` as its primary key.

The replication method used for each table depends on whether the table has a `sys_updated_on` column:

- **Incremental replication** is used when a table has a `sys_updated_on` column. New and changed records are picked up on each sync using `sys_updated_on` as the replication key.
- **Full-table replication** is used when a table has no `sys_updated_on` column.

Information note

If you use server-side scripts that include `autoSysFields(false)`, the `sys_updated_on` field will not be updated automatically. In this case, add custom code to update the `sys_updated_on` field when records change.

### Tables excluded by default

To protect sync performance, the following high-volume system and log tables are excluded from discovery by default: `sys_audit`, `sys_audit_delete`, `syslog`, `syslog_transaction`, `sys_email_log`, `sys_history_line`, `sys_history_set`, `ha_log`, `sys_cache_flush`, `sys_cluster_state`. These exclusions cannot be changed from the connection settings in this release.

## Limitations and considerations

- **HTTP Basic authentication only.** This connector authenticates with a username and password. OAuth 2.0 is not supported in this release.
- **Discovery scope follows the account's permissions.** Tables the account cannot read are skipped during discovery and reported in the run log. If the account cannot read any table, discovery fails with a permissions error.
- **Large catalogs.** A broadly privileged account can surface thousands of tables. Scope the integration user's permissions and select only the tables you need.
- **Incremental replication re-reads the boundary record.** The most recent record from the previous sync may be re-read on the next sync. Records upsert on `sys_id`, so duplicate reads are safe.
- **Full-table replication re-reads the entire table on every sync.** Tables without `sys_updated_on` are re-read in full on each sync. Sync time does not decrease as data accumulates.
- **Start Date applies to the initial sync only.** Once a table has a stored bookmark, later syncs resume from it. Changing Start Date does not re-replicate historical data.
- **Empty records are skipped.** Empty (`{}`) rows returned by ServiceNow are skipped and counted in the run log.
- **Retries.** Rate-limit responses (HTTP 429) and transient connection errors are retried automatically with exponential backoff (up to 5 attempts), honoring ServiceNow's `Retry-After` header.
- **Pagination.** The connector uses keyset pagination based on `sys_id` with a page size of 1,000 records and a default request timeout of 300 seconds.
