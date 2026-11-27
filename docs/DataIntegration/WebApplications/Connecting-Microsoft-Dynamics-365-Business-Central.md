---
title: "Microsoft Dynamics 365 Business Central"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Microsoft-Dynamics-365-Business-Central.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Microsoft Dynamics 365 Business Central

Microsoft Dynamics 365 Business Central is a cloud ERP platform for finance, operations, and business management. You can use Microsoft Dynamics 365 Business Central as a data source when landing or replicating data.

Business Central integration replicates data using the [Business Central API v2.0](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access data, authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Microsoft Dynamics 365 Business Central account, you need:

- Enable Business Central APIs. For more information, see [Enabling APIs for Dynamics 365 Business Central](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/enabling-apis-for-dynamics-nav).
- The connection is authenticated by a person signing in, and the connector accesses Business Central as that person. The authenticating user must be a licensed Business Central user with a permission set that covers the tables to be replicated. Tables that this user cannot read in Business Central will not be replicated.
- Admin permission to register an application or grant admin consent to API permissions in Microsoft Entra ID.
- Admin permission in Business Central to create a Microsoft Entra application and grant consent.

To register an Azure application:

1. Log into your organization's [Azure portal](https://portal.azure.com).
2. Navigate to Microsoft Entra ID > App registrations > New registration, then complete the registration form:
   1. Enter an application name.
   2. Under Supported account types, select Accounts in this organizational directory only (Single tenant).
   3. Under Redirect URI, select Web and enter https://connector.qlik.com/auth/oauth/v3.htm.
3. Click Register.
4. From the application's Overview page, copy the Application (client) ID and the Directory (tenant) ID.
5. Navigate to API permissions > Add a permission > Microsoft APIs > Dynamics 365 Business Central, and add:
   - Under Delegated permissions: `user_impersonation` and `Financials.ReadWrite.All`.
   - Under Application permissions: `API.ReadWrite.All`.
6. A Global Administrator must click Grant admin consent on the API permissions page. Admin consent is required because `API.ReadWrite.All` is an application permission.
7. Navigate to Certificates & secrets > Client secrets > New client secret.
8. Choose an expiry, and note that replication stops when the secret expires.
9. Copy and paste your secret Value into a secured file.

To create required roles and permissions in Business Central:

1. Open Business Central, search for Entra App, and open Microsoft Entra applications.
2. Click New to create a Microsoft Entra application, then complete the application details:
   1. Enter the Client ID of the registered app.
   2. Enter a meaningful description for the app.
   3. Set State to Enabled.
3. Under User Permission Sets, click New line and add D365 BUS FULL ACCESS.

   The user ID, user name, and user telemetry ID are created automatically after the Microsoft Entra application card is created.
4. After the Microsoft Entra application card is created, ask a Global Administrator to grant consent for the application.

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
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Client ID | Client ID. |
| Client Secret | Client secret. |
| Environment Name | Name of the Business Central environment to replicate from, for example Production or Sandbox. For a list of environments, see [Get environments in Business Central](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/api-get-environments). |
| Tenant ID | Directory (tenant) ID of the Microsoft Entra ID tenant where the app is registered. This is the value copied from the application's Overview page. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

The connector does not use a fixed table list. At discovery time, it reads the `$metadata` document of the connected Business Central environment and builds the stream catalog from it.

- Each entity set in `$metadata` becomes a stream. Names are converted from camelCase to snake\_case.
- A stream replicates as `CDC` if the entity exposes `lastModifiedDateTime`, and as `Full Table` if it does not.
- The primary key is the entity key declared in `$metadata`.
- When a replication key applies, it is always `lastModifiedDateTime`.

### `accounting_periods`

The `accounting_periods` table contains data for accounting periods.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `accounts`

The `accounts` table contains data for accounts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `aged_accounts_payables`

The `aged_accounts_payables` table contains data for aged accounts payables.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | vendorId |

### `aged_accounts_receivables`

The `aged_accounts_receivables` table contains data for aged accounts receivables.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | customerId |

### `apply_vendor_entries`

The `apply_vendor_entries` table contains data for apply vendor entries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `approval_entries`

The `approval_entries` table contains data for approval entries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `approval_user_setups`

The `approval_user_setups` table contains data for approval user setups.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `assembly_order_lines`

The `assembly_order_lines` table contains data for assembly order lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `assembly_orders`

The `assembly_orders` table contains data for assembly orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `balance_sheets`

The `balance_sheets` table contains data for balance sheets.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `bank_accounts`

The `bank_accounts` table contains data for bank accounts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `blanket_purchase_order_lines`

The `blanket_purchase_order_lines` table contains data for blanket purchase order lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `blanket_purchase_orders`

The `blanket_purchase_orders` table contains data for blanket purchase orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `blanket_sales_order_lines`

The `blanket_sales_order_lines` table contains data for blanket sales order lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `blanket_sales_orders`

The `blanket_sales_orders` table contains data for blanket sales orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `cash_flow_statements`

The `cash_flow_statements` table contains data for cash flow statements.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `companies`

The `companies` table contains data for companies.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `company_information`

The `company_information` table contains data for company information.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `contacts`

The `contacts` table contains data for contacts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `contacts_information`

The `contacts_information` table contains data for contacts information.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | contactId |

### `countries_regions`

The `countries_regions` table contains data for countries regions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `currencies`

The `currencies` table contains data for currencies.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `currency_exchange_rates`

The `currency_exchange_rates` table contains data for currency exchange rates.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `customer_contacts`

The `customer_contacts` table contains data for customer contacts.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `customer_financial_details`

The `customer_financial_details` table contains data for customer financial details.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `customer_payment_journals`

The `customer_payment_journals` table contains data for customer payment journals.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `customer_payments`

The `customer_payments` table contains data for customer payments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `customer_return_reasons`

The `customer_return_reasons` table contains data for customer return reasons.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `customer_sales`

The `customer_sales` table contains data for customer sales.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | customerId  customerNumber  name |

### `customers`

The `customers` table contains data for customers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `default_dimensions`

The `default_dimensions` table contains data for default dimensions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `dimension_values`

The `dimension_values` table contains data for dimension values.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `dimensions`

The `dimensions` table contains data for dimensions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `dispute_status`

The `dispute_status` table contains data for dispute status.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `document_attachments`

The `document_attachments` table contains data for document attachments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `employees`

The `employees` table contains data for employees.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `fixed_asset_locations`

The `fixed_asset_locations` table contains data for fixed asset locations.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `fixed_assets`

The `fixed_assets` table contains data for fixed assets.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `general_ledger_entries`

The `general_ledger_entries` table contains data for general ledger entries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `general_ledger_setup`

The `general_ledger_setup` table contains data for general ledger setup.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `general_product_posting_groups`

The `general_product_posting_groups` table contains data for general product posting groups.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `income_statements`

The `income_statements` table contains data for income statements.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `inventory_posting_groups`

The `inventory_posting_groups` table contains data for inventory posting groups.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `inventory_receipt_lines`

The `inventory_receipt_lines` table contains data for inventory receipt lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `inventory_receipts`

The `inventory_receipts` table contains data for inventory receipts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `inventory_shipment_lines`

The `inventory_shipment_lines` table contains data for inventory shipment lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `inventory_shipments`

The `inventory_shipments` table contains data for inventory shipments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `item_categories`

The `item_categories` table contains data for item categories.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `item_ledger_entries`

The `item_ledger_entries` table contains data for item ledger entries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `item_variants`

The `item_variants` table contains data for item variants.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `items`

The `items` table contains data for items.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `job_queue_entries`

The `job_queue_entries` table contains data for job queue entries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `job_queue_log_entries`

The `job_queue_log_entries` table contains data for job queue log entries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `journal_lines`

The `journal_lines` table contains data for journal lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `journals`

The `journals` table contains data for journals.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `locations`

The `locations` table contains data for locations.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `opportunities`

The `opportunities` table contains data for opportunities.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `payment_methods`

The `payment_methods` table contains data for payment methods.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `payment_terms`

The `payment_terms` table contains data for payment terms.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `physical_inventory_order_lines`

The `physical_inventory_order_lines` table contains data for physical inventory order lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `physical_inventory_orders`

The `physical_inventory_orders` table contains data for physical inventory orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `physical_inventory_recording_lines`

The `physical_inventory_recording_lines` table contains data for physical inventory recording lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `physical_inventory_recordings`

The `physical_inventory_recordings` table contains data for physical inventory recordings.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_approval_entries`

The `posted_approval_entries` table contains data for posted approval entries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_assembly_order_lines`

The `posted_assembly_order_lines` table contains data for posted assembly order lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_assembly_orders`

The `posted_assembly_orders` table contains data for posted assembly orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_direct_transfer_lines`

The `posted_direct_transfer_lines` table contains data for posted direct transfer lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_direct_transfers`

The `posted_direct_transfers` table contains data for posted direct transfers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_inventory_receipt_lines`

The `posted_inventory_receipt_lines` table contains data for posted inventory receipt lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_inventory_receipts`

The `posted_inventory_receipts` table contains data for posted inventory receipts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_inventory_shipment_lines`

The `posted_inventory_shipment_lines` table contains data for posted inventory shipment lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_inventory_shipments`

The `posted_inventory_shipments` table contains data for posted inventory shipments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_physical_inventory_order_lines`

The `posted_physical_inventory_order_lines` table contains data for posted physical inventory order lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_physical_inventory_orders`

The `posted_physical_inventory_orders` table contains data for posted physical inventory orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_physical_inventory_recording_lines`

The `posted_physical_inventory_recording_lines` table contains data for posted physical inventory recording lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `posted_physical_inventory_recordings`

The `posted_physical_inventory_recordings` table contains data for posted physical inventory recordings.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `projects`

The `projects` table contains data for projects.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_blanket_order_archive_lines`

The `purchase_blanket_order_archive_lines` table contains data for purchase blanket order archive lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_blanket_order_archives`

The `purchase_blanket_order_archives` table contains data for purchase blanket order archives.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_credit_memo_lines`

The `purchase_credit_memo_lines` table contains data for purchase credit memo lines.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `purchase_credit_memos`

The `purchase_credit_memos` table contains data for purchase credit memos.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_invoice_lines`

The `purchase_invoice_lines` table contains data for purchase invoice lines.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `purchase_invoices`

The `purchase_invoices` table contains data for purchase invoices.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_order_archive_lines`

The `purchase_order_archive_lines` table contains data for purchase order archive lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_order_archives`

The `purchase_order_archives` table contains data for purchase order archives.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_order_lines`

The `purchase_order_lines` table contains data for purchase order lines.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `purchase_orders`

The `purchase_orders` table contains data for purchase orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_quote_archive_lines`

The `purchase_quote_archive_lines` table contains data for purchase quote archive lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_quote_archives`

The `purchase_quote_archives` table contains data for purchase quote archives.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_quote_lines`

The `purchase_quote_lines` table contains data for purchase quote lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_quotes`

The `purchase_quotes` table contains data for purchase quotes.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_receipt_lines`

The `purchase_receipt_lines` table contains data for purchase receipt lines.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `purchase_receipts`

The `purchase_receipts` table contains data for purchase receipts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_return_order_archive_lines`

The `purchase_return_order_archive_lines` table contains data for purchase return order archive lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_return_order_archives`

The `purchase_return_order_archives` table contains data for purchase return order archives.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_return_order_lines`

The `purchase_return_order_lines` table contains data for purchase return order lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_return_orders`

The `purchase_return_orders` table contains data for purchase return orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `purchase_return_shipments`

The `purchase_return_shipments` table contains data for purchase return shipments.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `retained_earnings_statements`

The `retained_earnings_statements` table contains data for retained earnings statements.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `return_receipts`

The `return_receipts` table contains data for return receipts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_blanket_order_archive_lines`

The `sales_blanket_order_archive_lines` table contains data for sales blanket order archive lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_blanket_order_archives`

The `sales_blanket_order_archives` table contains data for sales blanket order archives.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_credit_memo_lines`

The `sales_credit_memo_lines` table contains data for sales credit memo lines.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `sales_credit_memos`

The `sales_credit_memos` table contains data for sales credit memos.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_invoice_lines`

The `sales_invoice_lines` table contains data for sales invoice lines.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `sales_invoices`

The `sales_invoices` table contains data for sales invoices.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_order_archive_lines`

The `sales_order_archive_lines` table contains data for sales order archive lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_order_archives`

The `sales_order_archives` table contains data for sales order archives.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_order_lines`

The `sales_order_lines` table contains data for sales order lines.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `sales_orders`

The `sales_orders` table contains data for sales orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_quote_archive_lines`

The `sales_quote_archive_lines` table contains data for sales quote archive lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_quote_archives`

The `sales_quote_archives` table contains data for sales quote archives.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_quote_lines`

The `sales_quote_lines` table contains data for sales quote lines.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `sales_quotes`

The `sales_quotes` table contains data for sales quotes.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_return_order_archive_lines`

The `sales_return_order_archive_lines` table contains data for sales return order archive lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_return_order_archives`

The `sales_return_order_archives` table contains data for sales return order archives.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_return_order_lines`

The `sales_return_order_lines` table contains data for sales return order lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_return_orders`

The `sales_return_orders` table contains data for sales return orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `sales_shipment_lines`

The `sales_shipment_lines` table contains data for sales shipment lines.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `sales_shipments`

The `sales_shipments` table contains data for sales shipments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `salespeople_purchasers`

The `salespeople_purchasers` table contains data for salespeople purchasers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `shipment_methods`

The `shipment_methods` table contains data for shipment methods.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `tax_areas`

The `tax_areas` table contains data for tax areas.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `tax_groups`

The `tax_groups` table contains data for tax groups.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `time_registration_entries`

The `time_registration_entries` table contains data for time registration entries.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

### `transfer_order_lines`

The `transfer_order_lines` table contains data for transfer order lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `transfer_orders`

The `transfer_orders` table contains data for transfer orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `transfer_receipt_lines`

The `transfer_receipt_lines` table contains data for transfer receipt lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `transfer_receipts`

The `transfer_receipts` table contains data for transfer receipts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `transfer_shipment_lines`

The `transfer_shipment_lines` table contains data for transfer shipment lines.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `transfer_shipments`

The `transfer_shipments` table contains data for transfer shipments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `trial_balances`

The `trial_balances` table contains data for trial balances.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | accountId |

### `units_of_measure`

The `units_of_measure` table contains data for units of measure.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `vendor_payment_journals`

The `vendor_payment_journals` table contains data for vendor payment journals.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `vendor_payments`

The `vendor_payments` table contains data for vendor payments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `vendor_purchases`

The `vendor_purchases` table contains data for vendor purchases.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | vendorId  vendorNumber  name |

### `vendors`

The `vendors` table contains data for vendors.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `workflow_approvers`

The `workflow_approvers` table contains data for workflow approvers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |

### `workflow_response_options`

The `workflow_response_options` table contains data for workflow response options.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | systemId |
| **Replication Key** | lastModifiedDateTime |

### `workflow_steps`

The `workflow_steps` table contains data for workflow steps.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | systemId |
| **Replication Key** | lastModifiedDateTime |

### `workflows`

The `workflows` table contains data for workflows.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | lastModifiedDateTime |
