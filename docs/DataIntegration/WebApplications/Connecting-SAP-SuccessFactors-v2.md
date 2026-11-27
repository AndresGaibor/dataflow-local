---
title: "SAP SuccessFactors"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SAP-SuccessFactors-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# SAP SuccessFactors

SAP SuccessFactors is SAP's cloud human experience management (HXM) suite. You can use SAP SuccessFactors as a data source when landing or replicating data.

SAP SuccessFactors integration replicates data using the [SuccessFactors HXM Suite OData V2 API](https://help.sap.com/docs/successfactors-platform/sap-successfactors-api-reference-guide-odata-v2). You can authenticate with Basic Auth or SAML Bearer OAuth. SAP's [deprecation of Basic Authentication](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/fcc05a902b4140e585d968c2fe4a96bc.html) is the motivation for using SAML Bearer OAuth as an alternative.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To find your API server URL:

The hostname depends on which SAP data center hosts your instance. It is not the same as the URL you use to sign in.

1. Log into your [SAP SuccessFactors](https://performancemanager.successfactors.eu/login#/companyEntry) account.
2. Click your profile picture and select Show version information.
3. Note the Data Center and Company ID values shown.
4. Look up the API server for that data center in SAP's [list of API servers](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/af2b8d5437494b12be88fe374eba75b6.html). For example, data center DC4 uses https://api4.successfactors.com.

To create an integration user and grant permissions:

1. Log into your [SAP SuccessFactors](https://performancemanager.successfactors.eu/login#/companyEntry) account as an administrator.
2. Navigate to Admin Center > Manage Permission Roles and either create a new role for the integration user or edit an existing one.
3. For Basic Auth, under Manage Integration Tools, grant Allow Admin to Access OData API through Basic Authentication. This permission applies only to Basic Auth.
4. Grant the integration user read access to the entities you intend to replicate. Permissions are per module — grant only what you need. Use Company Settings > OData API Data Dictionary to identify the required entities. Common permission choices include Employee Central API, Employee Export, and Admin access to MDF OData API.
5. Navigate to Admin Center > Manage Permission Groups, add the integration user to a group, and assign the role from the previous step to that group.

To register an OAuth client for SAML Bearer OAuth:

1. Log into your [SAP SuccessFactors](https://performancemanager.successfactors.eu/login#/companyEntry) account as an administrator.
2. Navigate to Admin Center > API Center > OAuth Configuration for OData, then click Register Client Application.
3. Enter the application name, description, and Application URL. SAP requires this URL for identification, but does not use it to connect to the API. For details, see [Registering your OAuth2 client application](https://help.sap.com/docs/successfactors-platform/sap-successfactors-api-reference-guide-odata-v2/registering-your-oauth2-client-application).
4. Select Bind to Users and enter the User ID of the integration user you prepared.
5. Click Generate X.509 Certificate, enter a Common Name, and click Generate. SuccessFactors generates the key pair in this flow; you do not need to generate a certificate externally.
6. Download the generated certificate file.
   1. Extract only the encrypted private-key text between `-----BEGIN ENCRYPTED PRIVATE KEY-----` and `-----END ENCRYPTED PRIVATE KEY-----`. Do not include either marker line.
   2. When you create the connection, enter the extracted text in the Private Key field.
   3. Treat the private key as a secret. Do not share the downloaded file.
   4. Remove the downloaded file from your device after extracting the key.
7. Register the application. To retrieve its API Key, return to the registered applications list and click View for the application. Copy the API Key into the connection's Client ID field.

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
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Authentication Method | Select Basic Auth or SAML Bearer OAuth. Basic Auth is selected by default and remains supported. |
| Username | For Basic Auth, enter the integration user's username suffixed with the Company ID in the form username@companyId, for example qlik\_integration@ACME01. |
| Password | For Basic Auth, enter the integration user's password. |
| Client ID | For SAML Bearer OAuth, enter the API Key for the registered OAuth client. |
| User ID | For SAML Bearer OAuth, enter the User ID of the integration user bound to the OAuth client. |
| Company ID | Enter the Company ID for your SAP SuccessFactors instance. |
| API Server URL | Required for both authentication methods. Enter the API server URL for your tenant's data center, for example https://api4.successfactors.com. The connector requires HTTPS and a host under successfactors.com, successfactors.eu, sapsf.com, sapsf.eu, sapsf.cn, or hr.cloud.sap. You can include port 443 and a trailing slash. Do not include the /odata/v2 path. |
| Private Key | Required for SAML Bearer OAuth. The connector uses this private key to sign the SAML assertion locally; it does not send the key to SAP. SuccessFactors resolves the certificate registered for the Client ID, so you do not enter a certificate in the connection. |

## Tables replicated

This connector uses dynamic discovery. It does not ship a fixed schema, and there is no fixed list of tables. Discovery runs in two phases:

1. The connector reads your tenant's OData metadata document at /odata/v2/$metadata and creates one candidate table for every entity set the tenant exposes.
2. It then sends a single-record test query to each candidate entity set and drops any that return an error. This removes entities belonging to modules you have not licensed or provisioned, entities the integration user cannot read, and a small number of SAP entities that cannot be queried directly.

The result is that the tables you see are specific to your instance: your licensed modules, your configuration, your custom fields and your integration user's permissions all shape the catalog. Two customers will not see the same list, and a fully provisioned instance can expose several hundred tables.

**Table names** are the SAP entity set name converted to snake case. `PerPerson` becomes `per_person`, `EmpJob` becomes `emp_job`. Where the SAP entity name already contains an underscore the result carries a double underscore, so `Background_Awards` becomes `background__awards`.

**Columns** are discovered per table from the same metadata document, so customer-configured custom fields on a standard entity are picked up automatically on the next discovery.

**Primary keys** are taken from the entity's key definition in SAP's metadata. They are frequently composite, and more than half of all tables have a key spanning two or more columns. Where a key column is inherited from a parent entity, SAP names it `<ParentEntity>_<keyName>`, for example `AutoDelegateConfig_delegator`.

Replication strategy is decided per table:

- If the table has a `lastModifiedDateTime`, `lastModifiedOn` or `lastModifiedDate` column, and SAP reports that column as filterable, the table replicates incrementally using the first such column found as the replication key.
- If it does not, the table replicates as full table.

Most tables replicate incrementally, and most of those use `lastModifiedDateTime` as the replication key. A smaller set, mainly the `background__*` employee profile tables, use `lastModifiedDate`.

### Parent/child stream relationships

Some SAP entities cannot be queried on their own and are only reachable through a parent entity. The connector detects these relationships from the associations declared in your tenant's metadata and replicates the child table by iterating the parent and filtering on the parent's key. A substantial minority of the tables in a typical instance are child tables.

Each child record carries an injected column named `__parent_<parent_table>_<parent_key_column>` holding the parent value it was fetched under.

Parent/child relationship examples

| Parent table | Example child tables |
| --- | --- |
| `per_person` | `per_email`, `per_personal`, `per_phone`, `per_national_id`, `emp_employment` |
| `emp_employment` | `emp_job`, `emp_compensation`, `emp_work_permit`, `emp_employment_termination` |
| `user` | `attachment`, `photo`, `competency_rating`, `employee_time`, `work_schedule` |
| `time_account_type` | `time_account`, `time_account_payout`, `time_account_snapshot` |

If you select a child table, select its parent table as well. A replication task that includes a child without its parent is rejected when the task is prepared.

## Limitations and considerations

- **Deletes are not captured.** The connector replicates inserts and updates only. A record deleted in SAP SuccessFactors remains in the destination. Use a periodic full reload if you need deletes reflected.
- **The catalog is instance-specific.** Tables belonging to modules you have not licensed, or that your integration user cannot read, do not appear. If an expected table is missing, check the module provisioning and the RBP permissions on the integration user rather than assuming the connector does not support it.
- **Discovery is slow on large instances.** The connector sends one test query per candidate entity set, twenty at a time. On an instance exposing several hundred entity sets the first discovery takes on the order of a minute, and the connection form can appear to hang while it runs.
- **Effective-dated tables return only currently effective records.** Employee Central entities such as `emp_job` and `emp_compensation` are effective-dated. The connector does not pass SAP's `fromDate`, `toDate` or `asOfDate` parameters, so these tables return the records effective as of the time of the sync rather than full history. Incremental results on these tables should not be treated as a complete change history.
- **Incremental runs can re-deliver boundary records.** Each incremental run filters on `<replication key> ge <last bookmark>`, so records whose timestamp exactly equals the previous run's high-water mark are replicated again. Records are keyed on the table's primary key, so this resolves to an upsert in the destination rather than a duplicate.
- **Start Date applies to the initial sync only.** Once a table has a stored bookmark, later syncs resume from it. Changing Start Date does not retroactively re-replicate data, and it has no effect on full-table tables.
- **Records are read using SAP's server-side pagination.** The connector follows the `__next` link SAP returns on each page until there are no more pages, at a server-controlled page size of 1000 records. This is not configurable from the connection form.
- **Rate limits are handled automatically.** SAP applies per-instance API limits and returns `HTTP 429 Too Many Requests` when they are exceeded. The connector honors the `Retry-After` header, falling back to 60 seconds when the header is absent, across a maximum of 5 attempts. Connection errors, timeouts and 5xx responses are retried separately with exponential backoff, also across a maximum of 5 attempts. The per-request timeout is 300 seconds.
- **Password expiry ends replication.** SuccessFactors password policies apply to the integration user. When the password expires or is reset, all tasks on the connection fail until the new password is saved to the connection. Configure the integration user so its password does not expire, if your policy allows it.
- **The certificate registered with SuccessFactors can expire and interrupt replication.** If you leave SAP's Validity(Days) field blank, SAP sets the certificate validity to 365 days. If Enable validity check is selected, the connection stops when the certificate expires. To resume replication, regenerate the certificate and enter the new private key and API Key in the connection. See [SAP KBA 2511864](https://userapps.support.sap.com/sap/support/knowledge/en/2511864) for details about certificate validity.
