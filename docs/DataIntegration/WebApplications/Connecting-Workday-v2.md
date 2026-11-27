---
title: "Workday"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Workday-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Workday

Workday is a cloud suite for human capital management, financial management, and planning. You can use Workday as a data source when landing or replicating data.

Workday integration replicates data using the [Workday Web Services (WWS) SOAP API](https://community-content.workday.com/en-us/public/products/platform-and-product-extensions/soap-api-reference.html?lang=en-us), version v45.0.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Worday account, you need:

- Permission to run the Register API Client task in Workday, or a Workday administrator who can run it for you.
- A Workday integration account to authorize the connection.
- Access through Workday domain security policies to the services and objects that you intend to replicate.

To register the Workday API client:

1. Log into your Workday account.
2. Search for and run the Register API Client task.

   Use the Register API Client task, not Register API Client for Integrations. Only the first task supports the redirection URI required by the Qlik sign-in flow.
3. Enter a Client Name, such as Qlik Talend Cloud.
4. Set Client Grant Type to Authorization Code Grant.
5. Set Access Token Type to Bearer.
6. Set Redirection URI to https://connector.qlik.com/auth/oauth/v3.htm.
7. Select the Scope (Functional Areas) that cover the data you intend to replicate. Select the functional areas corresponding to the Workday modules that you need. If you do not grant a scope, the matching tables are excluded from discovery.
8. Save the task. Workday displays the Client ID and Client Secret once. Copy and paste them into a secured file.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Click Authenticate when you have filled in the required connection settings.

   You may be asked to log in to the source application.

   A window is displayed with an authentication code.
2. Copy the code to the clipboard and return to the connection dialog.
3. Paste the code in Complete authentication with the code provided by the source and click Verify.

   Tip noteYou may need to scroll down to see this field.

   When status is Verified, the authentication is verified.
4. Provide a name for the connection in Connection name.
5. Select Open connection metadata to define metadata for the connection when it has been created.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. Select the date from which to begin historical replication in the date picker. The date is displayed in MM-DD-YYYY format and applies only to the first extraction of each incrementally replicated table. It does not apply to reload tables or later runs. |
| Tenant | Tenant name, such as company\_john1. |
| Hostname | API hostname, such as wd2-impl-services1.workday.com. Enter the host only. Do not enter https:// or a path. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Tables replicated

The connector replicates a fixed set of 30 tables across five Workday services. Tables that the Workday account cannot read through domain security are excluded from table discovery.

### Incrementally replicated tables

Seven tables replicate incrementally:

- On the first run, Workday returns records changed since the connection's Start date.
- On later runs, Workday returns records changed since the previous run finished. The Start date is not used again.
- A later run that returns zero rows is normal. It means that no records changed since the previous run.
- Workday filters these tables by its internal transaction log timestamp, which indicates when a change was entered or approved. It does not indicate when the change takes effect.

### Reload tables

The remaining 23 tables replicate in reload mode because the Workday operations behind them do not accept an update-date filter.

Information note

`financial_management_ledgers` can take longer than its row count suggests. Workday does not list ledgers directly, so the connector pages through all journal data to find distinct ledger identifiers and then calls Get\_Ledgers once for each ledger. The table returns no rows if the journals data is empty or the account cannot read it.

### Table contents

Workday tables, replication modes, and contents

| Table | Service | Replication mode | Contents |
| --- | --- | --- | --- |
| `absence_management_absence_inputs` | Absence Management | Reload | Employee absence input records including absence type, dates, and quantities. |
| `absence_management_override_balances` | Absence Management | Reload | Manual override balance adjustments for employee absence accrual plans. |
| `financial_management_cost_centers` | Financial Management | Incremental | Cost center definitions used for financial tracking and reporting. |
| `financial_management_customer_categories` | Financial Management | Reload | Categories used to classify customers in financial transactions. |
| `financial_management_fund_hierarchies` | Financial Management | Reload | Hierarchical groupings of funds for financial reporting. |
| `financial_management_fund_types` | Financial Management | Reload | Types used to classify financial funds. |
| `financial_management_funding_sources` | Financial Management | Reload | Sources of funding associated with financial transactions and grants. |
| `financial_management_funds` | Financial Management | Reload | Fund definitions used in financial and grant management. |
| `financial_management_journal_sources` | Financial Management | Reload | Source definitions that originate journal entries. |
| `financial_management_journals` | Financial Management | Incremental | Journal entries recording financial transactions and accounting events. |
| `financial_management_ledger_account_summaries` | Financial Management | Reload | Summary-level ledger accounts used for financial roll-up reporting. |
| `financial_management_ledgers` | Financial Management | Reload | Ledger definitions that organize financial accounts. |
| `financial_management_organizations` | Financial Management | Incremental | Financial management organizations such as companies and business units. |
| `financial_management_position_budgets` | Financial Management | Reload | Budget allocations associated with workforce positions. |
| `financial_management_program_hierarchies` | Financial Management | Reload | Hierarchical groupings of financial programs. |
| `financial_management_programs` | Financial Management | Reload | Financial programs used to track spending and funding by initiative. |
| `financial_management_revenue_categories` | Financial Management | Incremental | Categories used to classify revenue in financial transactions. |
| `financial_management_revenue_category_hierarchies` | Financial Management | Reload | Hierarchical groupings of revenue categories. |
| `financial_management_spend_category_hierarchies` | Financial Management | Reload | Hierarchical groupings of spend categories for expense classification. |
| `financial_management_supplier_categories` | Financial Management | Reload | Categories used to classify suppliers in procurement and payables. |
| `human_resources_job_categories` | Human Resources | Reload | Categories used to group and classify job profiles. |
| `human_resources_job_family_groups` | Human Resources | Reload | Top-level groupings of related job families. |
| `human_resources_job_profiles` | Human Resources | Incremental | Job profile definitions including title, level, and compensation details. |
| `human_resources_locations` | Human Resources | Reload | Physical and virtual work locations used across the organization. |
| `human_resources_organizations` | Human Resources | Incremental | HR organizations such as supervisory organizations and departments. |
| `performance_management_certification_issuers` | Performance Management | Reload | Organizations authorized to issue employee certifications. |
| `performance_management_competencies` | Performance Management | Reload | Skills and behaviors used to evaluate employee performance. |
| `performance_management_competency_categories` | Performance Management | Reload | Categories used to group related competencies. |
| `performance_management_degrees` | Performance Management | Reload | Academic degree types recognized in employee education records. |
| `staffing_organizations` | Staffing | Incremental | Staffing organizations used for headcount planning and position management. |

### Column structure

Each table has a small number of top-level columns and holds most of its content in nested structures that mirror the Workday SOAP response:

- `key_value`: The record's Workday ID (WID), used as the primary key.
- `<Entity>_Reference`: The record's reference object, containing an `ID` array of typed identifiers and a `Descriptor` label. For example, `Organization_Reference` occurs on `human_resources_organizations`.
- `<Entity>_Data`: A nested object holding the record's attributes, such as `Organization_Data`.
- `updated_through`: Incrementally replicated tables only. The connector adds a timestamp recording the point up to which the run collected changes. This is the table's replication key. It is not a Workday field and does not indicate when an individual record was modified.

Every field that ends in `_Reference`, at any depth, is normalized to the same `{ID: [...], Descriptor: ...}` shape so that related Workday objects can be resolved consistently. Dates and timestamps are emitted as ISO 8601 strings, and decimals are emitted as numbers.
