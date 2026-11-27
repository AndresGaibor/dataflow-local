---
title: "SAP Sales and Service Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SAP-Sales-and-Service-Cloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# SAP Sales and Service Cloud

SAP Sales and Service Cloud is a cloud CRM suite for sales, service, and marketing. You can use it as a data source when landing or replicating data.

The suite includes accounts and contacts, leads and opportunities, quotes and orders, activities, service requests and contracts, visits and field operations, and business partner and product master data.

SAP Sales and Service Cloud integration replicates data using the [SAP Cloud for Customer OData API](https://help.sap.com/docs/sap-cloud-for-customer/odata-services/sap-cloud-for-customer-odata-api).

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

The connector uses HTTP Basic authentication through the SAP Cloud for Customer OData API. Use a dedicated SAP business user and its password.

The API endpoint has the following format: `https://<tenant>.crm.ondemand.com/sap/c4c/odata/v1/c4codataapi`. This business-user path does not require a communication system or communication arrangement.

To set up your SAP Sales and Service Cloud connection, you need:

- An SAP Sales and Service Cloud tenant on the supported original tenant domain.
- Administrator access to create and configure the integration user and business role.
- A dedicated business user whose initial password has been changed at first sign-in.
- The required work center views and business-object permissions.

OData API external consumption is enabled by default. Confirm that it remains enabled for external access.

To create a business user:

1. Log into your [SAP](https://account.sap.com/sam/landing) account.
2. Navigate to Administrator > Users > Employees.
3. Create an employee. SAP automatically creates the corresponding business user.
4. Navigate to Administrator > Users > Business Users.
5. Select the business user, click Edit > Attributes, and set the initial password.
6. Copy and paste your user ID into a secured file.
7. Sign in once as the business user and complete the password change required by SAP.

Do not use the unchanged initial password in the connection. SAP can return an opaque connection failure until the business user completes the required password change.

To create and assign a business role:

1. Navigate to Administrator > General Settings > Business Roles.
2. Click New > Business Role.
3. Enter the role ID, name, and description.
4. Assign the work centers and views required for the business objects that you want to access.
5. Click Actions > Activate.
6. Assign the role to the business user through Business Users > Edit Access Rights > Business Role Assignment.

Role assignment runs as a background job. Wait for it to finish before creating the connection.

In SAP OData v2 metadata, each entity references the authorization information, which identifies the work center view that controls access. For example, `CorporateAccountCollection` references `CODACCOUNTWCV`. Code lists follow the authorization of their related object. Grant only the work center views that are required.

OData does not apply field-level restrictions, action restrictions, Key User Tool adaptations, or UI switches. It does apply instance-level restrictions.

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
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target.  For this connector, use `YYYY-MM-DDT00:00:00Z` rather than the generic format above. You can use the date picker. The time is midnight UTC and is used on the first run for incremental tables. |
| API Server URL | Enter only the base tenant URL, such as https://<tenant>.crm.ondemand.com. The connector appends /sap/c4c/odata/v1/c4codataapi. Do not include the service path. |
| Username | The system-generated SAP business-user User ID, not an email address or name. |
| Password | Password. |

## Tables replicated

The connector discovers tables dynamically. When you create a connection, it reads the tenant's OData metadata, creates candidates for entity sets, and sends a single-record test query to each candidate. It removes candidates that return errors and dependent tables that cannot be used.

The tests run in parallel. A transient SAP error can cause a table to be omitted. Refresh the connection metadata to retry discovery.

The catalog is specific to the tenant. Activated scenarios, configuration, custom fields, and work-center permissions determine its contents. A fully configured tenant can have more than 1,000 tables; roughly three quarters can be code lists and other reference data rather than business data.

### Table names and columns

The connector converts entity set names to snake\_case. The `Collection` suffix becomes `_collection`.

Entity set name conversion

| Entity set | Table name |
| --- | --- |
| `CorporateAccountCollection` | `corporate_account_collection` |
| `IndividualCustomerCollection` | `individual_customer_collection` |
| `OpportunityCollection` | `opportunity_collection` |
| `EMailCcRecipientsCollection` | `e_mail_cc_recipients_collection` |
| `CompetitorPOBoxDeviatingCountryCodeCollection` | `competitor_po_box_deviating_country_code_collection` |

Columns come from OData metadata. Custom and extension fields appear after they are enabled in OData and the connection metadata is read again. SAP supplies the primary keys. Business objects generally use `ObjectID`; code lists are an exception.

### Incremental replication

For each table, the connector checks the following properties in this fixed order and uses the first usable date or timestamp:

1. `EntityLastChangedOn`
2. `LastChangeDateTime`
3. `LastUpdatedOn`
4. `ChangedOn`
5. `ChangeDateTime`
6. `LastModifiedOn`
7. `UpdatedOn`
8. `ModifiedOn`
9. `LastChangedOn`

If the connector finds a property, it uses incremental replication. Otherwise, it reads the full table on every run. Code lists always use full replication because they have no change timestamp. Fewer than half of business-object tables can have a usable timestamp, so schedule and select tables with this limitation in mind.

### Parent and child tables

The connector detects relationships from metadata. To replicate a child, it iterates through the parent and filters on the parent key because some child entities reject direct queries. The child table includes `__parent_<parent table>_ObjectID` for joins.

Select the parent together with its child tables. Child tables require requests for each parent and can take longer to replicate.

### Data types

OData type conversion

| OData type | Connector type | Notes |
| --- | --- | --- |
| `Edm.String`, `Guid`, `Binary` | string | No additional conversion. |
| `Byte`, `SByte`, `Int16`, `Int32`, `Int64` | integer | No additional conversion. |
| `Single`, `Double`, `Decimal` | number | No additional conversion. |
| `Boolean` | boolean | No additional conversion. |
| `DateTime`, `DateTimeOffset` | nullable string date-time | SAP `/Date(...)/` values become standard timestamps. |
| `Time` | string | The value remains text. |
| Other types | string | Structured amount, quantity, and language values remain one text column containing the whole structure. |

Columns are nullable. All-zero and out-of-range dates become null. SAP placeholder dates such as 1900 and 9999 remain dates.

## Limitations and considerations

- **Missing table:** Refresh connection metadata and verify the required work-center view and OData custom-field permissions.
- **Authentication failure:** Verify that the business user completed SAP's required initial password change.
- **403 or permission error:** Verify the business role, its activated work centers and views, the assignment to the business user, and that the background role-assignment job has finished.
- **Throttling or timeout:** Reduce the selected tables, allow more time for large or parent-child tables, and retry after transient SAP errors.
- **Invalid URL:** Check the API Server URL value. SAP Sales Cloud Version 2 tenants are not supported.
