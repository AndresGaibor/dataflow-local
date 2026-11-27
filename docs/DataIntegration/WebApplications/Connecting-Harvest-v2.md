---
title: "Harvest"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Harvest-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Harvest

Harvest is a time tracking and management software with reporting and streamlined online invoicing.

Harvest integration replicates data using the [Harvest REST API V2](https://help.getharvest.com/api-v2/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate the client ID and client secret:

1. Log into your [Harvest Developers](https://id.getharvest.com/sessions/new?go_back=%2Fdevelopers) account.
2. Select the OAuth app you want to use, or create a new one.
3. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.
4. Click Save.
5. As the client ID and client secret are displayed only once, copy and paste them to a secured file.

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
| Account Name | Account name. For example: the account name of qlik.harvestapp.com would be qlik. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### clients

The `clients` table contains info about the clients in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/clients-api/clients/clients/)  [Harvest API method](https://help.getharvest.com/api-v2/clients-api/clients/clients/#list-all-clients "Opens in new tab: Harvest API method") |

clients table foreign keys

| Join clients with | on |
| --- | --- |
| [contacts](#contacts) | ``` clients.id = contacts.client_id ``` |
| [estimates](#estimates) | ``` clients.id = estimates.client_id ``` |
| [expenses](#expenses) | ``` clients.id = expenses.client_id ``` |
| [invoices](#invoices) | ``` clients.id = invoices.client_id ``` |
| [projects](#projects) | ``` clients.id = projects.client_id ``` |
| [time\_entries](#time-entries) | ``` clients.id = time_entries.client_id ``` |
| [user\_projects](#user-projects) | ``` clients.id = user_projects.client_id ``` |

clients table schema

|  |
| --- |
| **address**  STRING |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **id**  INTEGER |
| **is\_active**  BOOLEAN |
| **name**  STRING |
| **updated\_at**  DATE-TIME |

### contacts

The `contacts` table contains info about the client contacts in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/clients-api/clients/contacts/)  [Harvest API method](https://help.getharvest.com/api-v2/clients-api/clients/contacts/#list-all-contacts "Opens in new tab: Harvest API method") |

contacts table foreign keys

| Join contacts with | on |
| --- | --- |
| [clients](#clients) | ``` contacts.client_id = clients.id ``` |
| [estimates](#estimates) | ``` contacts.client_id = estimates.client_id ``` |
| [expenses](#expenses) | ``` contacts.client_id = expenses.client_id ``` |
| [invoices](#invoices) | ``` contacts.client_id = invoices.client_id ``` |
| [projects](#projects) | ``` contacts.client_id = projects.client_id ``` |
| [time\_entries](#time-entries) | ``` contacts.client_id = time_entries.client_id ``` |
| [user\_projects](#user-projects) | ``` contacts.client_id = user_projects.client_id ``` |

contacts table schema

|  |
| --- |
| **client\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **email**  STRING |
| **fax**  STRING |
| **first\_name**  STRING |
| **id**  INTEGER |
| **last\_name**  STRING |
| **phone\_mobile**  STRING |
| **phone\_office**  STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |

### estimate\_item\_categories

The `estimate_item_categories` table contains info about the estimate item categories in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/estimates-api/estimates/estimate-item-categories/)  [Harvest API method](https://help.getharvest.com/api-v2/estimates-api/estimates/estimate-item-categories/#list-all-estimate-item-categories "Opens in new tab: Harvest API method") |

estimate\_item\_categories table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **name**  STRING |
| **updated\_at**  DATE-TIME |

### estimate\_line\_items

The `estimate_line_items` table contains info about the line items contained in estimates.

**Note**: This table is updated based on new and updated `estimates`. This means that when an estimate is updated, this table will also be updated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/estimates-api/estimates/estimates/#the-estimate-line-item-object)  [Harvest API method](https://help.getharvest.com/api-v2/estimates-api/estimates/estimates/#get-all-estimates "Opens in new tab: Harvest API method") |

estimate\_line\_items table foreign keys

| Join estimate\_line\_items with | on |
| --- | --- |
| [estimate\_messages](#estimate-messages) | ``` estimate_line_items.estimate_id = estimate_messages.estimate_id ``` |
| [estimates](#estimates) | ``` estimate_line_items.estimate_id = estimates.id ``` |
| [invoices](#invoices) | ``` estimate_line_items.estimate_id = invoices.estimate_id ``` |

estimate\_line\_items table schema

|  |
| --- |
| **amount**  NUMBER |
| **description**  STRING |
| **estimate\_id**  INTEGER |
| **id**  INTEGER |
| **kind**  STRING |
| **quantity**  INTEGER |
| **taxed**  BOOLEAN |
| **taxed2**  BOOLEAN |
| **unit\_price**  NUMBER |

### estimate\_messages

The `estimate_messages` table contains info about the messages associated with estimates.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/estimates-api/estimates/estimate-messages/)  [Harvest API method](https://help.getharvest.com/api-v2/estimates-api/estimates/estimate-messages/#list-all-messages-for-an-estimate "Opens in new tab: Harvest API method") |

estimate\_messages table foreign keys

| Join estimate\_messages with | on |
| --- | --- |
| [estimate\_line\_items](#estimate-line-items) | ``` estimate_messages.estimate_id = estimate_line_items.estimate_id ``` |
| [estimates](#estimates) | ``` estimate_messages.estimate_id = estimates.id ``` |
| [invoices](#invoices) | ``` estimate_messages.estimate_id = invoices.estimate_id ``` |

estimate\_messages table schema

|  |
| --- |
| **body**  STRING |
| **created\_at**  DATE-TIME |
| **estimate\_id**  INTEGER |
| **event\_type**  STRING |
| **id**  INTEGER |
| **recipients**  ARRAY This is a nested data structure:   - email: STRING - name: STRING |
| **send\_me\_a\_copy**  BOOLEAN |
| **sent\_by**  STRING |
| **sent\_by\_email**  STRING |
| **sent\_from**  STRING |
| **sent\_from\_email**  STRING |
| **subject**  STRING |
| **updated\_at**  DATE-TIME |

### estimates

The `estimates` table contains info about the estimates in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/estimates-api/estimates/estimates/)  [Harvest API method](https://help.getharvest.com/api-v2/estimates-api/estimates/estimate-messages/#list-all-messages-for-an-estimate "Opens in new tab: Harvest API method") |

estimates table foreign keys

| Join estimates with | on |
| --- | --- |
| [clients](#clients) | ``` estimates.client_id = clients.id ``` |
| [contacts](#contacts) | ``` estimates.client_id = contacts.client_id ``` |
| [expenses](#expenses) | ``` estimates.client_id = expenses.client_id ``` |
| [invoices](#invoices) | ``` estimates.client_id = invoices.client_id ```  ``` estimates.id = invoices.estimate_id ```  ``` estimates.creator_id = invoices.creator_id ``` |
| [projects](#projects) | ``` estimates.client_id = projects.client_id ``` |
| [time\_entries](#time-entries) | ``` estimates.client_id = time_entries.client_id ```  ``` estimates.creator_id = time_entries.user_id ``` |
| [user\_projects](#user-projects) | ``` estimates.client_id = user_projects.client_id ```  ``` estimates.creator_id = user_projects.user_id ``` |
| [estimate\_line\_items](#estimate-line-items) | ``` estimates.id = estimate_line_items.estimate_id ``` |
| [estimate\_messages](#estimate-messages) | ``` estimates.id = estimate_messages.estimate_id ``` |
| [users](#users) | ``` estimates.creator_id = users.id ``` |
| [user\_project\_tasks](#user-project-tasks) | ``` estimates.creator_id = user_project_tasks.user_id ``` |
| [user\_roles](#user-roles) | ``` estimates.creator_id = user_roles.user_id ``` |

estimates table schema

|  |
| --- |
| **accepted\_at**  DATE-TIME |
| **amount**  NUMBER |
| **client\_id**  INTEGER |
| **client\_key**  STRING |
| **created\_at**  DATE-TIME |
| **creator\_id**  INTEGER |
| **currency**  STRING |
| **declined\_at**  DATE-TIME |
| **discount**  STRING, NUMBER |
| **discount\_amount**  NUMBER |
| **id**  INTEGER |
| **issue\_date**  DATE-TIME |
| **notes**  STRING |
| **number**  STRING |
| **purchase\_order**  STRING |
| **sent\_at**  DATE-TIME |
| **state**  STRING |
| **subject**  STRING |
| **tax**  STRING, NUMBER |
| **tax2**  STRING, NUMBER |
| **tax2\_amount**  NUMBER |
| **tax\_amount**  NUMBER |
| **updated\_at**  DATE-TIME |

### expense\_categories

The `expense_categories` table contains info about the expense categories in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/expenses-api/expenses/expense-categories/)  [Harvest API method](https://help.getharvest.com/api-v2/expenses-api/expenses/expense-categories/#list-all-expense-categories "Opens in new tab: Harvest API method") |

expense\_categories table foreign keys

| Join expense\_categories with | on |
| --- | --- |
| [expenses](#expenses) | ``` expense_categories.id = expenses.expense_category_id ``` |

expense\_categories table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **is\_active**  BOOLEAN |
| **name**  STRING |
| **unit\_name**  STRING |
| **unit\_price**  NUMBER |
| **updated\_at**  DATE-TIME |

### expenses

The `expenses` table contains info about the expenses recorded in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/expenses-api/expenses/expenses/)  [Harvest API method](https://help.getharvest.com/api-v2/expenses-api/expenses/expenses#list-all-expenses "Opens in new tab: Harvest API method") |

expenses table foreign keys

| Join expenses with | on |
| --- | --- |
| [clients](#clients) | ``` expenses.client_id = clients.id ``` |
| [contacts](#contacts) | ``` expenses.client_id = contacts.client_id ``` |
| [estimates](#estimates) | ``` expenses.client_id = estimates.client_id ``` |
| [invoices](#invoices) | ``` expenses.client_id = invoices.client_id ```  ``` expenses.invoice_id = invoices.id ``` |
| [projects](#projects) | ``` expenses.client_id = projects.client_id ```  ``` expenses.project_id = projects.id ``` |
| [time\_entries](#time-entries) | ``` expenses.client_id = time_entries.client_id ```  ``` expenses.id = time_entries.external_reference_id ```  ``` expenses.invoice_id = time_entries.invoice_id ```  ``` expenses.project_id = time_entries.project_id ``` |
| [user\_projects](#user-projects) | ``` expenses.client_id = user_projects.client_id ```  ``` expenses.project_id = user_projects.project_id ``` |
| [expense\_categories](#expense-categories) | ``` expenses.expense_category_id = expense_categories.id ``` |
| [time\_entry\_external\_reference](#time-entry-external-reference) | ``` expenses.id = time_entry_external_reference.external_reference_id ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` expenses.invoice_id = invoice_line_items.invoice_id ```  ``` expenses.project_id = invoice_line_items.project_id ``` |
| [invoice\_messages](#invoice-messages) | ``` expenses.invoice_id = invoice_messages.invoice_id ``` |
| [invoice\_payments](#invoice-payments) | ``` expenses.invoice_id = invoice_payments.invoice_id ``` |
| [project\_tasks](#project-tasks) | ``` expenses.project_id = project_tasks.project_id ``` |
| [project\_users](#project-users) | ``` expenses.project_id = project_users.project_id ``` |

expenses table schema

|  |
| --- |
| **billable**  BOOLEAN |
| **client\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **expense\_category\_id**  INTEGER |
| **id**  INTEGER |
| **invoice\_id**  INTEGER |
| **is\_billed**  BOOLEAN |
| **is\_closed**  BOOLEAN |
| **is\_locked**  BOOLEAN |
| **locked\_reason**  STRING |
| **notes**  STRING |
| **project\_id**  INTEGER |
| **receipt\_content\_type**  STRING |
| **receipt\_file\_name**  STRING |
| **receipt\_file\_size**  INTEGER |
| **receipt\_url**  STRING |
| **spent\_date**  DATE-TIME |
| **total\_cost**  NUMBER |
| **units**  NUMBER |
| **updated\_at**  DATE-TIME |
| **user\_assignment\_id**  INTEGER |
| **user\_id**  INTEGER |

### invoice\_item\_categories

The `invoice_item_categories` table contains info about the various categories that can be applied to invoice line items.

**Note**: Harvest includes two non-removable categories by default for the hours and expenses you bill.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-item-categories/)  [Harvest API method](http://help.getharvest.com/api-v1/invoices-api/invoices/invoice-messages-payments/#show-all-categories "Opens in new tab: Harvest API method") |

invoice\_item\_categories table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **name**  STRING |
| **updated\_at**  DATE-TIME |
| **use\_as\_expense**  BOOLEAN |
| **use\_as\_service**  BOOLEAN |

### invoice\_line\_items

The `invoice_line_items` table contains info about the line items contained in invoices.

**Note**: This table is updated based on new and updated `invoices`. This means that when an invoice is updated, this table will also be updated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/invoices-api/invoices/invoices#the-invoice-line-item-object)  [Harvest API method](https://help.getharvest.com/api-v2/invoices-api/invoices/invoices#list-all-invoices "Opens in new tab: Harvest API method") |

invoice\_line\_items table foreign keys

| Join invoice\_line\_items with | on |
| --- | --- |
| [expenses](#expenses) | ``` invoice_line_items.invoice_id = expenses.invoice_id ```  ``` invoice_line_items.project_id = expenses.project_id ``` |
| [invoice\_messages](#invoice-messages) | ``` invoice_line_items.invoice_id = invoice_messages.invoice_id ``` |
| [invoice\_payments](#invoice-payments) | ``` invoice_line_items.invoice_id = invoice_payments.invoice_id ``` |
| [invoices](#invoices) | ``` invoice_line_items.invoice_id = invoices.id ``` |
| [time\_entries](#time-entries) | ``` invoice_line_items.invoice_id = time_entries.invoice_id ```  ``` invoice_line_items.project_id = time_entries.project_id ``` |
| [project\_tasks](#project-tasks) | ``` invoice_line_items.project_id = project_tasks.project_id ``` |
| [project\_users](#project-users) | ``` invoice_line_items.project_id = project_users.project_id ``` |
| [projects](#projects) | ``` invoice_line_items.project_id = projects.id ``` |
| [user\_projects](#user-projects) | ``` invoice_line_items.project_id = user_projects.project_id ``` |

invoice\_line\_items table schema

|  |
| --- |
| **amount**  NUMBER |
| **description**  STRING |
| **id**  INTEGER |
| **invoice\_id**  INTEGER |
| **kind**  STRING |
| **project\_id**  INTEGER |
| **quantity**  INTEGER |
| **taxed**  BOOLEAN |
| **taxed2**  BOOLEAN |
| **unit\_price**  NUMBER |

### invoice\_messages

The `invoice_messages` table contains info about invoice messages, or emails sent to clients about invoices.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest API method](https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-messages/ "Opens in new tab: Harvest API method") |

invoice\_messages table foreign keys

| Join invoice\_messages with | on |
| --- | --- |
| [expenses](#expenses) | ``` invoice_messages.invoice_id = expenses.invoice_id ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` invoice_messages.invoice_id = invoice_line_items.invoice_id ``` |
| [invoice\_payments](#invoice-payments) | ``` invoice_messages.invoice_id = invoice_payments.invoice_id ``` |
| [invoices](#invoices) | ``` invoice_messages.invoice_id = invoices.id ``` |
| [time\_entries](#time-entries) | ``` invoice_messages.invoice_id = time_entries.invoice_id ``` |

invoice\_messages table schema

|  |
| --- |
| **attach\_pdf**  BOOLEAN |
| **body**  STRING |
| **created\_at**  DATE-TIME |
| **event\_type**  STRING |
| **id**  INTEGER |
| **include\_link\_to\_client\_invoice**  BOOLEAN |
| **invoice\_id**  INTEGER |
| **recipients**  ARRAY This is a nested data structure:   - email: STRING - name: STRING |
| **reminder**  BOOLEAN |
| **send\_me\_a\_copy**  BOOLEAN |
| **send\_reminder\_on**  DATE-TIME |
| **sent\_by**  STRING |
| **sent\_by\_email**  STRING |
| **sent\_from**  STRING |
| **sent\_from\_email**  STRING |
| **subject**  STRING |
| **thank\_you**  BOOLEAN |
| **updated\_at**  DATE-TIME |

### invoice\_payments

The `invoice_payments` table contains info about the payments applied to invoices in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-payments/)  [Harvest API method](https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-payments#list-all-payments-for-an-invoice "Opens in new tab: Harvest API method") |

invoice\_payments table foreign keys

| Join invoice\_payments with | on |
| --- | --- |
| [expenses](#expenses) | ``` invoice_payments.invoice_id = expenses.invoice_id ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` invoice_payments.invoice_id = invoice_line_items.invoice_id ``` |
| [invoice\_messages](#invoice-messages) | ``` invoice_payments.invoice_id = invoice_messages.invoice_id ``` |
| [invoices](#invoices) | ``` invoice_payments.invoice_id = invoices.id ``` |
| [time\_entries](#time-entries) | ``` invoice_payments.invoice_id = time_entries.invoice_id ``` |

invoice\_payments table schema

|  |
| --- |
| **amount**  NUMBER |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **invoice\_id**  INTEGER |
| **notes**  STRING |
| **paid\_at**  DATE-TIME |
| **paid\_date**  DATE-TIME |
| **payment\_gateway\_id**  INTEGER |
| **payment\_gateway\_name**  INTEGER |
| **recorded\_by**  STRING |
| **recorded\_by\_email**  STRING |
| **transaction\_id**  STRING |
| **updated\_at**  DATE-TIME |

### invoices

The `invoices` table contains info about the invoices in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/invoices-api/invoices/invoices/)  [Harvest API method](https://help.getharvest.com/api-v2/invoices-api/invoices/invoices#list-all-invoices "Opens in new tab: Harvest API method") |

invoices table foreign keys

| Join invoices with | on |
| --- | --- |
| [clients](#clients) | ``` invoices.client_id = clients.id ``` |
| [contacts](#contacts) | ``` invoices.client_id = contacts.client_id ``` |
| [estimates](#estimates) | ``` invoices.client_id = estimates.client_id ```  ``` invoices.estimate_id = estimates.id ```  ``` invoices.creator_id = estimates.creator_id ``` |
| [expenses](#expenses) | ``` invoices.client_id = expenses.client_id ```  ``` invoices.id = expenses.invoice_id ``` |
| [projects](#projects) | ``` invoices.client_id = projects.client_id ``` |
| [time\_entries](#time-entries) | ``` invoices.client_id = time_entries.client_id ```  ``` invoices.id = time_entries.invoice_id ```  ``` invoices.creator_id = time_entries.user_id ``` |
| [user\_projects](#user-projects) | ``` invoices.client_id = user_projects.client_id ```  ``` invoices.creator_id = user_projects.user_id ``` |
| [estimate\_line\_items](#estimate-line-items) | ``` invoices.estimate_id = estimate_line_items.estimate_id ``` |
| [estimate\_messages](#estimate-messages) | ``` invoices.estimate_id = estimate_messages.estimate_id ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` invoices.id = invoice_line_items.invoice_id ``` |
| [invoice\_messages](#invoice-messages) | ``` invoices.id = invoice_messages.invoice_id ``` |
| [invoice\_payments](#invoice-payments) | ``` invoices.id = invoice_payments.invoice_id ``` |
| [users](#users) | ``` invoices.creator_id = users.id ``` |
| [user\_project\_tasks](#user-project-tasks) | ``` invoices.creator_id = user_project_tasks.user_id ``` |
| [user\_roles](#user-roles) | ``` invoices.creator_id = user_roles.user_id ``` |

invoices table schema

|  |
| --- |
| **amount**  NUMBER |
| **client\_id**  INTEGER |
| **client\_key**  STRING |
| **closed\_at**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **creator\_id**  INTEGER |
| **currency**  STRING |
| **discount**  STRING, NUMBER |
| **discount\_amount**  NUMBER |
| **due\_amount**  NUMBER |
| **due\_date**  DATE-TIME |
| **estimate\_id**  INTEGER |
| **id**  INTEGER |
| **issue\_date**  DATE-TIME |
| **notes**  STRING |
| **number**  STRING |
| **paid\_at**  DATE-TIME |
| **paid\_date**  DATE-TIME |
| **payment\_term**  STRING |
| **period\_end**  DATE-TIME |
| **period\_start**  DATE-TIME |
| **purchase\_order**  STRING |
| **retainer\_id**  INTEGER |
| **sent\_at**  DATE-TIME |
| **state**  STRING |
| **subject**  STRING |
| **tax**  STRING, NUMBER |
| **tax2**  STRING, NUMBER |
| **tax2\_amount**  NUMBER |
| **tax\_amount**  NUMBER |
| **updated\_at**  DATE-TIME |

### project\_tasks

The `project_tasks` table contains info about the tasks assigned to projects.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/projects-api/projects/task-assignments/)  [Harvest API method](https://help.getharvest.com/api-v2/projects-api/projects/task-assignments#list-all-task-assignments "Opens in new tab: Harvest API method") |

project\_tasks table foreign keys

| Join project\_tasks with | on |
| --- | --- |
| [expenses](#expenses) | ``` project_tasks.project_id = expenses.project_id ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` project_tasks.project_id = invoice_line_items.project_id ``` |
| [project\_users](#project-users) | ``` project_tasks.project_id = project_users.project_id ``` |
| [projects](#projects) | ``` project_tasks.project_id = projects.id ``` |
| [time\_entries](#time-entries) | ``` project_tasks.project_id = time_entries.project_id ``` |
| [user\_projects](#user-projects) | ``` project_tasks.project_id = user_projects.project_id ``` |
| [user\_project\_tasks](#user-project-tasks) | ``` project_tasks.id = user_project_tasks.project_task_id ``` |

project\_tasks table schema

|  |
| --- |
| **billable**  BOOLEAN |
| **budget**  NUMBER |
| **created\_at**  DATE-TIME |
| **hourly\_rate**  NUMBER |
| **id**  INTEGER |
| **is\_active**  BOOLEAN |
| **project\_id**  INTEGER |
| **task\_id**  INTEGER |
| **updated\_at**  DATE-TIME |

### project\_users

The `project_users` table contains info about the users assigned to projects.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest API method](https://help.getharvest.com/api-v2/projects-api/projects/user-assignments/ "Opens in new tab: Harvest API method") |

project\_users table foreign keys

| Join project\_users with | on |
| --- | --- |
| [expenses](#expenses) | ``` project_users.project_id = expenses.project_id ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` project_users.project_id = invoice_line_items.project_id ``` |
| [project\_tasks](#project-tasks) | ``` project_users.project_id = project_tasks.project_id ``` |
| [projects](#projects) | ``` project_users.project_id = projects.id ``` |
| [time\_entries](#time-entries) | ``` project_users.project_id = time_entries.project_id ``` |
| [user\_projects](#user-projects) | ``` project_users.project_id = user_projects.project_id ``` |

project\_users table schema

|  |
| --- |
| **budget**  NUMBER |
| **created\_at**  DATE-TIME |
| **hourly\_rate**  NUMBER |
| **id**  INTEGER |
| **is\_active**  BOOLEAN |
| **is\_project\_manager**  BOOLEAN |
| **project\_id**  INTEGER |
| **updated\_at**  DATE-TIME |
| **user\_id**  INTEGER |

### projects

The `projects` table contains info about the projects in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/projects-api/projects/projects/)  [Harvest API method](https://help.getharvest.com/api-v2/projects-api/projects/projects#list-all-projects "Opens in new tab: Harvest API method") |

projects table foreign keys

| Join projects with | on |
| --- | --- |
| [clients](#clients) | ``` projects.client_id = clients.id ``` |
| [contacts](#contacts) | ``` projects.client_id = contacts.client_id ``` |
| [estimates](#estimates) | ``` projects.client_id = estimates.client_id ``` |
| [expenses](#expenses) | ``` projects.client_id = expenses.client_id ```  ``` projects.id = expenses.project_id ``` |
| [invoices](#invoices) | ``` projects.client_id = invoices.client_id ``` |
| [time\_entries](#time-entries) | ``` projects.client_id = time_entries.client_id ```  ``` projects.id = time_entries.project_id ``` |
| [user\_projects](#user-projects) | ``` projects.client_id = user_projects.client_id ```  ``` projects.id = user_projects.project_id ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` projects.id = invoice_line_items.project_id ``` |
| [project\_tasks](#project-tasks) | ``` projects.id = project_tasks.project_id ``` |
| [project\_users](#project-users) | ``` projects.id = project_users.project_id ``` |

projects table schema

|  |
| --- |
| **bill\_by**  STRING |
| **budget**  NUMBER |
| **budget\_by**  STRING |
| **budget\_is\_monthly**  BOOLEAN |
| **client\_id**  INTEGER |
| **code**  STRING |
| **cost\_budget**  NUMBER |
| **cost\_budget\_include\_expenses**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **ends\_on**  STRING |
| **fee**  NUMBER |
| **hourly\_rate**  NUMBER |
| **id**  INTEGER |
| **is\_active**  BOOLEAN |
| **is\_billable**  BOOLEAN |
| **is\_fixed\_fee**  BOOLEAN |
| **name**  STRING |
| **notes**  STRING |
| **notify\_when\_over\_budget**  BOOLEAN |
| **over\_budget\_notification\_date**  DATE-TIME |
| **over\_budget\_notification\_percentage**  INTEGER |
| **show\_budget\_to\_all**  BOOLEAN |
| **starts\_on**  STRING |
| **updated\_at**  DATE-TIME |

### roles

The `roles` table contains info about the roles in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/roles-api/roles/roles/)  [Harvest API method](https://help.getharvest.com/api-v2/roles-api/roles/roles#list-all-roles "Opens in new tab: Harvest API method") |

roles table foreign keys

| Join roles with | on |
| --- | --- |
| [user\_roles](#user-roles) | ``` roles.id = user_roles.role_id ``` |

roles table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **name**  STRING |
| **updated\_at**  DATE-TIME |

### tasks

The `tasks` table contains info about the tasks in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/tasks-api/tasks/tasks/)  [Harvest API method](https://help.getharvest.com/api-v2/tasks-api/tasks/tasks#list-all-tasks "Opens in new tab: Harvest API method") |

tasks table foreign keys

| Join tasks with | on |
| --- | --- |
| [time\_entries](#time-entries) | ``` tasks.id = time_entries.task_id ``` |

tasks table schema

|  |
| --- |
| **billable\_by\_default**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **default\_hourly\_rate**  NUMBER |
| **id**  INTEGER |
| **is\_active**  BOOLEAN |
| **is\_default**  BOOLEAN |
| **name**  STRING |
| **updated\_at**  DATE-TIME |

### time\_entries

The `time_entries` table contains info about the time entries in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/)  [Harvest API method](https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries#list-all-time-entries "Opens in new tab: Harvest API method") |

time\_entries table foreign keys

| Join time\_entries with | on |
| --- | --- |
| [clients](#clients) | ``` time_entries.client_id = clients.id ``` |
| [contacts](#contacts) | ``` time_entries.client_id = contacts.client_id ``` |
| [estimates](#estimates) | ``` time_entries.client_id = estimates.client_id ```  ``` time_entries.user_id = estimates.creator_id ``` |
| [expenses](#expenses) | ``` time_entries.client_id = expenses.client_id ```  ``` time_entries.external_reference_id = expenses.id ```  ``` time_entries.invoice_id = expenses.invoice_id ```  ``` time_entries.project_id = expenses.project_id ``` |
| [invoices](#invoices) | ``` time_entries.client_id = invoices.client_id ```  ``` time_entries.invoice_id = invoices.id ```  ``` time_entries.user_id = invoices.creator_id ``` |
| [projects](#projects) | ``` time_entries.client_id = projects.client_id ```  ``` time_entries.project_id = projects.id ``` |
| [user\_projects](#user-projects) | ``` time_entries.client_id = user_projects.client_id ```  ``` time_entries.project_id = user_projects.project_id ```  ``` time_entries.user_id = user_projects.user_id ``` |
| [time\_entry\_external\_reference](#time-entry-external-reference) | ``` time_entries.external_reference_id = time_entry_external_reference.external_reference_id ```  ``` time_entries.id = time_entry_external_reference.time_entry_id ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` time_entries.invoice_id = invoice_line_items.invoice_id ```  ``` time_entries.project_id = invoice_line_items.project_id ``` |
| [invoice\_messages](#invoice-messages) | ``` time_entries.invoice_id = invoice_messages.invoice_id ``` |
| [invoice\_payments](#invoice-payments) | ``` time_entries.invoice_id = invoice_payments.invoice_id ``` |
| [project\_tasks](#project-tasks) | ``` time_entries.project_id = project_tasks.project_id ``` |
| [project\_users](#project-users) | ``` time_entries.project_id = project_users.project_id ``` |
| [tasks](#tasks) | ``` time_entries.task_id = tasks.id ``` |
| [users](#users) | ``` time_entries.user_id = users.id ``` |
| [user\_project\_tasks](#user-project-tasks) | ``` time_entries.user_id = user_project_tasks.user_id ``` |
| [user\_roles](#user-roles) | ``` time_entries.user_id = user_roles.user_id ``` |

time\_entries table schema

|  |
| --- |
| **billable**  BOOLEAN |
| **billable\_rate**  NUMBER |
| **budgeted**  NUMBER |
| **client\_id**  INTEGER |
| **cost\_rate**  NUMBER |
| **created\_at**  DATE-TIME |
| **ended\_time**  TIME |
| **external\_reference\_id**  STRING |
| **hours**  NUMBER |
| **id**  INTEGER |
| **invoice\_id**  INTEGER |
| **is\_billed**  BOOLEAN |
| **is\_closed**  BOOLEAN |
| **is\_locked**  BOOLEAN |
| **is\_running**  BOOLEAN |
| **locked\_reason**  STRING |
| **notes**  STRING |
| **project\_id**  INTEGER |
| **spent\_date**  DATE-TIME |
| **started\_time**  TIME |
| **task\_assignment\_id**  INTEGER |
| **task\_id**  INTEGER |
| **timer\_started\_at**  DATE-TIME |
| **updated\_at**  DATE-TIME |
| **user\_assignment\_id**  INTEGER |
| **user\_id**  INTEGER |

### time\_entry\_external\_reference

The `time_entry_external_reference` table contains pairs of time entry IDs and external reference IDs. This data can be used to tie time entries tracked in external services (such as Trello) to your other Harvest data.

**Note**: This table is updated based on new and updated `time_entries`. This means that when a time entry is updated, this table will also be updated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | time\_entry\_id  external\_reference\_id |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/)  [Harvest API method](https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries#list-all-time-entries "Opens in new tab: Harvest API method") |

time\_entry\_external\_reference table foreign keys

| Join time\_entry\_external\_reference with | on |
| --- | --- |
| [expenses](#expenses) | ``` time_entry_external_reference.external_reference_id = expenses.id ``` |
| [time\_entries](#time-entries) | ``` time_entry_external_reference.external_reference_id = time_entries.external_reference_id ```  ``` time_entry_external_reference.time_entry_id = time_entries.id ``` |

time\_entry\_external\_reference table schema

|  |
| --- |
| **external\_reference\_id**  STRING |
| **time\_entry\_id**  INTEGER |

### user\_project\_tasks

The `user_project_tasks` table contains pairs of user IDs and project task IDs.

This data can be used to see lists of all the project tasks associated with a user, and join tables together to get a comprehensive look at the user’s projects.

**Note**: This table is updated based on new and updated `users`. This means that when a user is updated, this table will also be updated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | user\_id  project\_task\_id |
| **Useful links** | Harvest documentation |

user\_project\_tasks table foreign keys

| Join user\_project\_tasks with | on |
| --- | --- |
| [project\_tasks](#project-tasks) | ``` user_project_tasks.project_task_id = project_tasks.id ``` |
| [estimates](#estimates) | ``` user_project_tasks.user_id = estimates.creator_id ``` |
| [invoices](#invoices) | ``` user_project_tasks.user_id = invoices.creator_id ``` |
| [time\_entries](#time-entries) | ``` user_project_tasks.user_id = time_entries.user_id ``` |
| [users](#users) | ``` user_project_tasks.user_id = users.id ``` |
| [user\_projects](#user-projects) | ``` user_project_tasks.user_id = user_projects.user_id ``` |
| [user\_roles](#user-roles) | ``` user_project_tasks.user_id = user_roles.user_id ``` |

user\_project\_tasks table schema

|  |
| --- |
| **project\_task\_id**  INTEGER |
| **user\_id**  INTEGER |

### user\_projects

The `user_projects` table contains info about the project assignments users are assigned to.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest API method](https://help.getharvest.com/api-v2/users-api/users/project-assignments/ "Opens in new tab: Harvest API method") |

user\_projects table foreign keys

| Join user\_projects with | on |
| --- | --- |
| [clients](#clients) | ``` user_projects.client_id = clients.id ``` |
| [contacts](#contacts) | ``` user_projects.client_id = contacts.client_id ``` |
| [estimates](#estimates) | ``` user_projects.client_id = estimates.client_id ```  ``` user_projects.user_id = estimates.creator_id ``` |
| [expenses](#expenses) | ``` user_projects.client_id = expenses.client_id ```  ``` user_projects.project_id = expenses.project_id ``` |
| [invoices](#invoices) | ``` user_projects.client_id = invoices.client_id ```  ``` user_projects.user_id = invoices.creator_id ``` |
| [projects](#projects) | ``` user_projects.client_id = projects.client_id ```  ``` user_projects.project_id = projects.id ``` |
| [time\_entries](#time-entries) | ``` user_projects.client_id = time_entries.client_id ```  ``` user_projects.project_id = time_entries.project_id ```  ``` user_projects.user_id = time_entries.user_id ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` user_projects.project_id = invoice_line_items.project_id ``` |
| [project\_tasks](#project-tasks) | ``` user_projects.project_id = project_tasks.project_id ``` |
| [project\_users](#project-users) | ``` user_projects.project_id = project_users.project_id ``` |
| [users](#users) | ``` user_projects.user_id = users.id ``` |
| [user\_project\_tasks](#user-project-tasks) | ``` user_projects.user_id = user_project_tasks.user_id ``` |
| [user\_roles](#user-roles) | ``` user_projects.user_id = user_roles.user_id ``` |

user\_projects table schema

|  |
| --- |
| **budget**  NUMBER |
| **client\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **hourly\_rate**  NUMBER |
| **id**  INTEGER |
| **is\_active**  BOOLEAN |
| **is\_project\_manager**  BOOLEAN |
| **project\_id**  INTEGER |
| **updated\_at**  DATE-TIME |
| **user\_id**  INTEGER |

### user\_roles

The `user_roles` table contains a list of user ID and role ID pairs, enabling you to see the roles users are associated with.

**Note**: This table is updated based on new and updated `users`. This means that when a user is updated, this table will also be updated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | user\_id  role\_id |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/users-api/users/users/) |

user\_roles table foreign keys

| Join user\_roles with | on |
| --- | --- |
| [roles](#roles) | ``` user_roles.role_id = roles.id ``` |
| [estimates](#estimates) | ``` user_roles.user_id = estimates.creator_id ``` |
| [invoices](#invoices) | ``` user_roles.user_id = invoices.creator_id ``` |
| [time\_entries](#time-entries) | ``` user_roles.user_id = time_entries.user_id ``` |
| [users](#users) | ``` user_roles.user_id = users.id ``` |
| [user\_project\_tasks](#user-project-tasks) | ``` user_roles.user_id = user_project_tasks.user_id ``` |
| [user\_projects](#user-projects) | ``` user_roles.user_id = user_projects.user_id ``` |

user\_roles table schema

|  |
| --- |
| **role\_id**  INTEGER |
| **user\_id**  INTEGER |

### users

The `users` table contains info about the users in your Harvest account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Harvest documentation](https://help.getharvest.com/api-v2/users-api/users/users/)  [Harvest API method](https://help.getharvest.com/api-v2/users-api/users/users#list-all-users "Opens in new tab: Harvest API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [estimates](#estimates) | ``` users.id = estimates.creator_id ``` |
| [invoices](#invoices) | ``` users.id = invoices.creator_id ``` |
| [time\_entries](#time-entries) | ``` users.id = time_entries.user_id ``` |
| [user\_project\_tasks](#user-project-tasks) | ``` users.id = user_project_tasks.user_id ``` |
| [user\_projects](#user-projects) | ``` users.id = user_projects.user_id ``` |
| [user\_roles](#user-roles) | ``` users.id = user_roles.user_id ``` |

users table schema

|  |
| --- |
| **avatar\_url**  STRING |
| **can\_create\_invoices**  BOOLEAN |
| **can\_create\_projects**  BOOLEAN |
| **can\_see\_rates**  BOOLEAN |
| **cost\_rate**  NUMBER |
| **created\_at**  DATE-TIME |
| **default\_hourly\_rate**  NUMBER |
| **email**  STRING |
| **first\_name**  STRING |
| **has\_access\_to\_all\_future\_projects**  BOOLEAN |
| **id**  INTEGER |
| **is\_active**  BOOLEAN |
| **is\_admin**  BOOLEAN |
| **is\_contractor**  BOOLEAN |
| **is\_project\_manager**  BOOLEAN |
| **last\_name**  STRING |
| **telephone**  STRING |
| **timezone**  STRING |
| **updated\_at**  DATE-TIME |
| **weekly\_capacity**  INTEGER |
