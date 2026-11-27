---
title: "Codat"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Codat.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Codat

Codat is a data sharing and AI insights platform that helps financial institutions build deeper connections with their business customers.

Codat integration replicates data using the [Codat API](https://docs.codat.io/using-the-api/overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

API keys can only be managed by Administrator or Developer users.

To retrieve your API key:

1. Log into your [Codat](https://authentication.codat.io/u/login/identifier?state=hKFo2SBaZUtqdGh0V0x6c3REejByWnRtRVVBVXFBSFBDSTliZaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEJkUTNYQmFrcGphMHFCUFlEVHNpTS1kR3VzVlhyMVM0o2NpZNkgWmxlMUdZMzNCN0djeFlYU3hQZWw0cEl2Q3l5eGZ3eXo) account.
2. Go to Developers > API keys.
3. Copy and paste your API key into a secured file.

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
| API Key | API key. |
| Use Codat UAT environment | Select this check box to connect your UAT environment. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### accounts

The `accounts` table contains info about the accounts in your Codat instance. In Codat, an account is a category used to record accounting transactions for a business.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  companyId |
| **Replication Key** | modifiedDate |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/accounts-1)  [Codat API method](https://docs.codat.io/reference/accounts#accounts_list "Opens in new tab: Codat API method") |

accounts table foreign keys

| Join accounts with | on |
| --- | --- |
| [bank\_accounts](#bank-accounts) | ``` accounts.name = bank_accounts.accountName ``` |
| [balance\_sheets](#balance-sheets) | ``` accounts.id = balance_sheets.reports.assets.accountId ```  ``` accounts.id = balance_sheets.reports.equity.accountId ```  ``` accounts.id = balance_sheets.reports.liabilities.accountId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` accounts.id = profit_and_loss.reports.costOfSales.accountId ```  ``` accounts.id = profit_and_loss.reports.expenses.accountId ```  ``` accounts.id = profit_and_loss.reports.income.accountId ```  ``` accounts.id = profit_and_loss.reports.otherExpenses.accountId ```  ``` accounts.id = profit_and_loss.reports.otherIncome.accountId ``` |
| [bills](#bills) | ``` accounts.id = bills.lineItems.accountRef.id ``` |
| [items](#items) | ``` accounts.id = items.billItem.accountRef.id ```  ``` accounts.id = items.invoiceItem.accountRef.id ``` |
| [journal\_entries](#journal-entries) | ``` accounts.id = journal_entries.journalLines.accountRef.id ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` accounts.name = bank_statement_lines.accountName ``` |

accounts table schema

|  |
| --- |
| **companyId**  STRING |
| **currency**  STRING |
| **currentBalance**  NUMBER |
| **description**  STRING |
| **fullyQualifiedCategory**  STRING |
| **fullyQualifiedName**  STRING |
| **id**  STRING |
| **isBankAccount**  BOOLEAN |
| **modifiedDate**  STRING |
| **name**  STRING |
| **nominalCode**  STRING |
| **sourceModifiedDate**  STRING |
| **status**  STRING |
| **type**  STRING |

### balance\_sheets

The `balance_sheets` table contains info about the balance sheets in your Codat instance. A balance sheet is a snapshot at a point in time of a company’s accounts.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | companyId |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/balance-sheet-2)  [Codat API method](https://docs.codat.io/reference/financials#financials_balancesheet "Opens in new tab: Codat API method") |

balance\_sheets table foreign keys

| Join balance\_sheets with | on |
| --- | --- |
| [accounts](#accounts) | ``` balance_sheets.reports.assets.accountId = accounts.id ```  ``` balance_sheets.reports.equity.accountId = accounts.id ```  ``` balance_sheets.reports.liabilities.accountId = accounts.id ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` balance_sheets.reports.assets.accountId = profit_and_loss.reports.costOfSales.accountId ```  ``` balance_sheets.reports.equity.accountId = profit_and_loss.reports.costOfSales.accountId ```  ``` balance_sheets.reports.liabilities.accountId = profit_and_loss.reports.costOfSales.accountId ```  ``` balance_sheets.reports.assets.accountId = profit_and_loss.reports.expenses.accountId ```  ``` balance_sheets.reports.equity.accountId = profit_and_loss.reports.expenses.accountId ```  ``` balance_sheets.reports.liabilities.accountId = profit_and_loss.reports.expenses.accountId ```  ``` balance_sheets.reports.assets.accountId = profit_and_loss.reports.income.accountId ```  ``` balance_sheets.reports.equity.accountId = profit_and_loss.reports.income.accountId ```  ``` balance_sheets.reports.liabilities.accountId = profit_and_loss.reports.income.accountId ```  ``` balance_sheets.reports.assets.accountId = profit_and_loss.reports.otherExpenses.accountId ```  ``` balance_sheets.reports.equity.accountId = profit_and_loss.reports.otherExpenses.accountId ```  ``` balance_sheets.reports.liabilities.accountId = profit_and_loss.reports.otherExpenses.accountId ```  ``` balance_sheets.reports.assets.accountId = profit_and_loss.reports.otherIncome.accountId ```  ``` balance_sheets.reports.equity.accountId = profit_and_loss.reports.otherIncome.accountId ```  ``` balance_sheets.reports.liabilities.accountId = profit_and_loss.reports.otherIncome.accountId ```  ``` balance_sheets.companyId = profit_and_loss.companyId ``` |
| [bills](#bills) | ``` balance_sheets.reports.assets.accountId = bills.lineItems.accountRef.id ```  ``` balance_sheets.reports.equity.accountId = bills.lineItems.accountRef.id ```  ``` balance_sheets.reports.liabilities.accountId = bills.lineItems.accountRef.id ```  ``` balance_sheets.companyId = bills.companyId ``` |
| [items](#items) | ``` balance_sheets.reports.assets.accountId = items.billItem.accountRef.id ```  ``` balance_sheets.reports.equity.accountId = items.billItem.accountRef.id ```  ``` balance_sheets.reports.liabilities.accountId = items.billItem.accountRef.id ```  ``` balance_sheets.reports.assets.accountId = items.invoiceItem.accountRef.id ```  ``` balance_sheets.reports.equity.accountId = items.invoiceItem.accountRef.id ```  ``` balance_sheets.reports.liabilities.accountId = items.invoiceItem.accountRef.id ```  ``` balance_sheets.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` balance_sheets.reports.assets.accountId = journal_entries.journalLines.accountRef.id ```  ``` balance_sheets.reports.equity.accountId = journal_entries.journalLines.accountRef.id ```  ``` balance_sheets.reports.liabilities.accountId = journal_entries.journalLines.accountRef.id ```  ``` balance_sheets.companyId = journal_entries.companyId ``` |
| [companies](#companies) | ``` balance_sheets.companyId = companies.id ``` |
| [bank\_statements](#bank-statements) | ``` balance_sheets.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` balance_sheets.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` balance_sheets.companyId = bill_payments.supplierRef.companyId ```  ``` balance_sheets.companyId = bill_payments.companyId ``` |
| [company\_info](#company-info) | ``` balance_sheets.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` balance_sheets.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` balance_sheets.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` balance_sheets.companyId = payments.companyId ``` |
| [suppliers](#suppliers) | ``` balance_sheets.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` balance_sheets.companyId = connections.companyId ``` |
| [events](#events) | ``` balance_sheets.companyId = events.companyId ``` |
| [tax\_rates](#tax-rates) | ``` balance_sheets.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` balance_sheets.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` balance_sheets.companyId = bank_accounts.companyId ``` |

balance\_sheets table schema

|  |
| --- |
| **companyId**  STRING |
| **currency**  STRING |
| **mostRecentAvailableMonth**  STRING |
| **reports**  ARRAY This is a nested data structure:   - assets: ARRAY, which is also a nested data structure.   - accountId: STRING   - name: STRING   - value: NUMBER - date: DATE-TIME - equity: ARRAY, which is also a nested data structure.   - accountId: STRING   - name: STRING   - value: NUMBER - liabilities: ARRAY, which is also a nested data structure.   - accountId: STRING   - name: STRING   - value: NUMBER - netAssets: NUMBER |
| **status**  OBJECT, STRING This is a nested data structure. |

### bank\_account\_transactions

The bank\_account\_transactions table contains information about transactions for a specified company and bank account in your Codat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | \_transactionIndex  bankAccountId  companyId |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/bank-transactions)  [Codat API method](https://docs.codat.io/reference/bankaccounts#bankaccounts_getaccounttransactions "Opens in new tab: Codat API method") |

bank\_account\_transactions table foreign keys

| Join bank\_account\_transactions with | on |
| --- | --- |
| [bank\_accounts](#bank-accounts) | ``` bank_account_transactions.bankAccountId = bank_accounts.id ```  ``` bank_account_transactions.companyId = bank_accounts.companyId ``` |
| [companies](#companies) | ``` bank_account_transactions.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` bank_account_transactions.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` bank_account_transactions.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` bank_account_transactions.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` bank_account_transactions.companyId = bill_payments.supplierRef.companyId ```  ``` bank_account_transactions.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` bank_account_transactions.companyId = bills.companyId ``` |
| [company\_info](#company-info) | ``` bank_account_transactions.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` bank_account_transactions.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` bank_account_transactions.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` bank_account_transactions.companyId = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` bank_account_transactions.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` bank_account_transactions.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` bank_account_transactions.companyId = connections.companyId ``` |
| [events](#events) | ``` bank_account_transactions.companyId = events.companyId ``` |
| [items](#items) | ``` bank_account_transactions.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` bank_account_transactions.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` bank_account_transactions.companyId = tax_rates.companyId ``` |

bank\_account\_transactions table schema

|  |
| --- |
| **\_transactionIndex**  INTEGER |
| **amount**  NUMBER |
| **balance**  NUMBER |
| **bankAccountId**  STRING |
| **companyId**  STRING |
| **date**  STRING |
| **description**  STRING |
| **modifiedDate**  STRING |
| **reconciled**  BOOLEAN |
| **sourceModifiedDate**  STRING |
| **transactionType**  STRING |

### bank\_accounts

The `bank_accounts` table contains informaiton about bank accounts for a given company in your Codat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | accountName  companyId  connectionId |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/bank-accounts)  [Codat API method](https://docs.codat.io/reference/bankaccounts#bankaccounts_listaccountspaged "Opens in new tab: Codat API method") |

bank\_accounts table foreign keys

| Join bank\_accounts with | on |
| --- | --- |
| [accounts](#accounts) | ``` bank_accounts.accountName = accounts.name ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` bank_accounts.accountName = bank_statement_lines.accountName ```  ``` bank_accounts.companyId = bank_statement_lines.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` bank_accounts.id = bank_account_transactions.bankAccountId ```  ``` bank_accounts.companyId = bank_account_transactions.companyId ``` |
| [companies](#companies) | ``` bank_accounts.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` bank_accounts.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` bank_accounts.companyId = bank_statements.companyId ``` |
| [bill\_payments](#bill-payments) | ``` bank_accounts.companyId = bill_payments.supplierRef.companyId ```  ``` bank_accounts.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` bank_accounts.companyId = bills.companyId ``` |
| [company\_info](#company-info) | ``` bank_accounts.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` bank_accounts.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` bank_accounts.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` bank_accounts.companyId = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` bank_accounts.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` bank_accounts.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` bank_accounts.companyId = connections.companyId ```  ``` bank_accounts.connectionId = connections.id ``` |
| [events](#events) | ``` bank_accounts.companyId = events.companyId ``` |
| [items](#items) | ``` bank_accounts.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` bank_accounts.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` bank_accounts.companyId = tax_rates.companyId ``` |

bank\_accounts table schema

|  |
| --- |
| **accountName**  STRING |
| **accountNumber**  STRING |
| **availableBalance**  NUMBER |
| **balance**  NUMBER |
| **companyId**  STRING |
| **connectionId**  STRING |
| **currency**  STRING |
| **fromDate**  STRING |
| **iban**  STRING |
| **id**  STRING |
| **modifiedDate**  STRING |
| **overdraftLimit**  NUMBER |
| **sortCode**  STRING |
| **sourceModifiedDate**  STRING |
| **toDate**  STRING |

### bank\_statement\_lines

The `bank_statement_lines` table contains info about lines included in bank statements.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | accountName  companyId  \_lineIndex |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/bank-transactions)  [Codat API method](https://docs.codat.io/reference/bankstatements#bankstatements_listpaged "Opens in new tab: Codat API method") |

bank\_statement\_lines table foreign keys

| Join bank\_statement\_lines with | on |
| --- | --- |
| [accounts](#accounts) | ``` bank_statement_lines.accountName = accounts.name ``` |
| [bank\_accounts](#bank-accounts) | ``` bank_statement_lines.accountName = bank_accounts.accountName ```  ``` bank_statement_lines.companyId = bank_accounts.companyId ``` |
| [companies](#companies) | ``` bank_statement_lines.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` bank_statement_lines.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` bank_statement_lines.companyId = bank_statements.companyId ``` |
| [bill\_payments](#bill-payments) | ``` bank_statement_lines.companyId = bill_payments.supplierRef.companyId ```  ``` bank_statement_lines.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` bank_statement_lines.companyId = bills.companyId ``` |
| [company\_info](#company-info) | ``` bank_statement_lines.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` bank_statement_lines.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` bank_statement_lines.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` bank_statement_lines.companyId = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` bank_statement_lines.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` bank_statement_lines.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` bank_statement_lines.companyId = connections.companyId ``` |
| [events](#events) | ``` bank_statement_lines.companyId = events.companyId ``` |
| [items](#items) | ``` bank_statement_lines.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` bank_statement_lines.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` bank_statement_lines.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` bank_statement_lines.companyId = bank_account_transactions.companyId ``` |

bank\_statement\_lines table schema

|  |
| --- |
| **\_lineIndex**  INTEGER |
| **accountName**  STRING |
| **amount**  NUMBER |
| **balance**  NUMBER |
| **companyId**  STRING |
| **date**  DATE-TIME |
| **description**  STRING |
| **id**  STRING |
| **reconciled**  BOOLEAN |

### bank\_statements

The `bank_statements` table contains info about bank statement report data for a company over a time period.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  companyId |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/bank-accounts)  [Codat API method](https://docs.codat.io/reference/bankstatements#bankstatements_listpaged "Opens in new tab: Codat API method") |

bank\_statements table foreign keys

| Join bank\_statements with | on |
| --- | --- |
| [companies](#companies) | ``` bank_statements.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` bank_statements.companyId = balance_sheets.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` bank_statements.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` bank_statements.companyId = bill_payments.supplierRef.companyId ```  ``` bank_statements.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` bank_statements.companyId = bills.companyId ``` |
| [company\_info](#company-info) | ``` bank_statements.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` bank_statements.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` bank_statements.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` bank_statements.companyId = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` bank_statements.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` bank_statements.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` bank_statements.companyId = connections.companyId ``` |
| [events](#events) | ``` bank_statements.companyId = events.companyId ``` |
| [items](#items) | ``` bank_statements.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` bank_statements.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` bank_statements.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` bank_statements.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` bank_statements.companyId = bank_accounts.companyId ``` |

bank\_statements table schema

|  |
| --- |
| **accountName**  STRING |
| **accountNumber**  STRING |
| **availableBalance**  STRING, NUMBER |
| **balance**  STRING, NUMBER |
| **companyId**  STRING |
| **currency**  STRING |
| **fromDate**  DATE-TIME |
| **iban**  STRING |
| **id**  STRING |
| **sortCode**  STRING |
| **toDate**  DATE-TIME |

### bill\_payments

The bill\_payments table contains information about company bill payments in your Codat account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | companyId  id |
| **Replication Key** | modifiedDate |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/billpayments-1)  [Codat API method](https://docs.codat.io/reference/billpayments#billpayments_listpaged "Opens in new tab: Codat API method") |

bill\_payments table foreign keys

| Join bill\_payments with | on |
| --- | --- |
| [companies](#companies) | ``` bill_payments.supplierRef.companyId = companies.id ```  ``` bill_payments.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` bill_payments.supplierRef.companyId = balance_sheets.companyId ```  ``` bill_payments.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` bill_payments.supplierRef.companyId = bank_statements.companyId ```  ``` bill_payments.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` bill_payments.supplierRef.companyId = bank_statement_lines.companyId ```  ``` bill_payments.companyId = bank_statement_lines.companyId ``` |
| [bills](#bills) | ``` bill_payments.supplierRef.companyId = bills.companyId ```  ``` bill_payments.companyId = bills.companyId ```  ``` bill_payments.supplierRef.id = bills.supplierRef ``` |
| [company\_info](#company-info) | ``` bill_payments.supplierRef.companyId = company_info.companyId ```  ``` bill_payments.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` bill_payments.supplierRef.companyId = customers.companyId ```  ``` bill_payments.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` bill_payments.supplierRef.companyId = invoices.companyId ```  ``` bill_payments.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` bill_payments.supplierRef.companyId = payments.companyId ```  ``` bill_payments.companyId = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` bill_payments.supplierRef.companyId = profit_and_loss.companyId ```  ``` bill_payments.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` bill_payments.supplierRef.companyId = suppliers.companyId ```  ``` bill_payments.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` bill_payments.supplierRef.companyId = connections.companyId ```  ``` bill_payments.companyId = connections.companyId ``` |
| [events](#events) | ``` bill_payments.supplierRef.companyId = events.companyId ```  ``` bill_payments.companyId = events.companyId ``` |
| [items](#items) | ``` bill_payments.supplierRef.companyId = items.companyId ```  ``` bill_payments.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` bill_payments.supplierRef.companyId = journal_entries.companyId ```  ``` bill_payments.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` bill_payments.supplierRef.companyId = tax_rates.companyId ```  ``` bill_payments.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` bill_payments.supplierRef.companyId = bank_account_transactions.companyId ```  ``` bill_payments.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` bill_payments.supplierRef.companyId = bank_accounts.companyId ```  ``` bill_payments.companyId = bank_accounts.companyId ``` |

bill\_payments table schema

|  |
| --- |
| **companyId**  STRING |
| **currency**  STRING |
| **currencyRate**  NUMBER |
| **date**  STRING |
| **id**  STRING |
| **lines**  ARRAY This is a nested data structure:   - amount: NUMBER - links: ARRAY, which is also a nested data structure.   - id: STRING   - type: STRING |
| **modifiedDate**  STRING |
| **note**  STRING |
| **sourceModifiedDate**  STRING |
| **supplierRef**  OBJECT This is a nested data structure:   - addresses: ARRAY, which is also a nested data structure.   - city: STRING   - country: STRING   - line1: STRING   - line2: STRING   - postalCode: STRING   - region: STRING   - type: STRING - companyId: STRING - contactName: STRING - emailAddress: STRING - id: STRING - phone: STRING - registrationNumber: STRING - status: STRING - supplierName: STRING - taxNumber: STRING |
| **totalAmount**  NUMBER |

### bills

The `bills` table contains info about the bills in your Codat account. A bill is an itemized record of goods or services purchased from a [supplier](#suppliers).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | companyId  id |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/bills-1)  [Codat API method](https://docs.codat.io/reference/bills#bills_listpaged "Opens in new tab: Codat API method") |

bills table foreign keys

| Join bills with | on |
| --- | --- |
| [accounts](#accounts) | ``` bills.lineItems.accountRef.id = accounts.id ``` |
| [balance\_sheets](#balance-sheets) | ``` bills.lineItems.accountRef.id = balance_sheets.reports.assets.accountId ```  ``` bills.lineItems.accountRef.id = balance_sheets.reports.equity.accountId ```  ``` bills.lineItems.accountRef.id = balance_sheets.reports.liabilities.accountId ```  ``` bills.companyId = balance_sheets.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` bills.lineItems.accountRef.id = profit_and_loss.reports.costOfSales.accountId ```  ``` bills.lineItems.accountRef.id = profit_and_loss.reports.expenses.accountId ```  ``` bills.lineItems.accountRef.id = profit_and_loss.reports.income.accountId ```  ``` bills.lineItems.accountRef.id = profit_and_loss.reports.otherExpenses.accountId ```  ``` bills.lineItems.accountRef.id = profit_and_loss.reports.otherIncome.accountId ```  ``` bills.companyId = profit_and_loss.companyId ``` |
| [items](#items) | ``` bills.lineItems.accountRef.id = items.billItem.accountRef.id ```  ``` bills.lineItems.accountRef.id = items.invoiceItem.accountRef.id ```  ``` bills.companyId = items.companyId ```  ``` bills.lineItems.itemRef.id = items.id ```  ``` bills.lineItems.taxRateRef.id = items.billItem.taxRateRef.id ```  ``` bills.lineItems.taxRateRef.id = items.invoiceItem.taxRateRef.id ``` |
| [journal\_entries](#journal-entries) | ``` bills.lineItems.accountRef.id = journal_entries.journalLines.accountRef.id ```  ``` bills.companyId = journal_entries.companyId ``` |
| [companies](#companies) | ``` bills.companyId = companies.id ``` |
| [bank\_statements](#bank-statements) | ``` bills.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` bills.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` bills.companyId = bill_payments.supplierRef.companyId ```  ``` bills.companyId = bill_payments.companyId ```  ``` bills.supplierRef = bill_payments.supplierRef.id ``` |
| [company\_info](#company-info) | ``` bills.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` bills.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` bills.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` bills.companyId = payments.companyId ``` |
| [suppliers](#suppliers) | ``` bills.companyId = suppliers.companyId ```  ``` bills.supplierRef = suppliers.id ``` |
| [connections](#connections) | ``` bills.companyId = connections.companyId ``` |
| [events](#events) | ``` bills.companyId = events.companyId ``` |
| [tax\_rates](#tax-rates) | ``` bills.companyId = tax_rates.companyId ```  ``` bills.lineItems.taxRateRef.id = tax_rates.id ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` bills.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` bills.companyId = bank_accounts.companyId ``` |

bills table schema

|  |
| --- |
| **amountDue**  NUMBER |
| **companyId**  STRING |
| **currency**  STRING |
| **dueDate**  DATE-TIME |
| **id**  STRING |
| **issueDate**  DATE-TIME |
| **lineItems**  ARRAY This is a nested data structure:   - accountRef: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING - description: STRING - discountAmount: NUMBER - discountPercentage: NUMBER - itemRef: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING - quantity: NUMBER - subTotal: NUMBER - taxAmount: NUMBER - taxRateRef: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING - totalAmount: NUMBER - unitAmount: NUMBER |
| **reference**  STRING |
| **status**  STRING |
| **subTotal**  NUMBER |
| **supplierRef**  OBJECT This is a nested data structure:   - addresses: ARRAY, which is also a nested data structure.   - city: STRING   - country: STRING   - line1: STRING   - line2: STRING   - postalCode: STRING   - region: STRING   - type: STRING - companyId: STRING - contactName: STRING - emailAddress: STRING - id: STRING - phone: STRING - registrationNumber: STRING - status: STRING - supplierName: STRING - taxNumber |
| **taxAmount**  NUMBER |
| **totalAmount**  NUMBER |

### companies

The `companies` table contains info about the companies in your Codat instance. A company represents a business who can share the connection to their financial data sources.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Codat documentation](https://docs.codat.io/reference/companies)  [Codat API method](https://docs.codat.io/reference/companies#companies_listpaged "Opens in new tab: Codat API method") |

companies table foreign keys

| Join companies with | on |
| --- | --- |
| [balance\_sheets](#balance-sheets) | ``` companies.id = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` companies.id = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` companies.id = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` companies.id = bill_payments.supplierRef.companyId ```  ``` companies.id = bill_payments.companyId ``` |
| [bills](#bills) | ``` companies.id = bills.companyId ``` |
| [company\_info](#company-info) | ``` companies.id = company_info.companyId ``` |
| [customers](#customers) | ``` companies.id = customers.companyId ``` |
| [invoices](#invoices) | ``` companies.id = invoices.companyId ``` |
| [payments](#payments) | ``` companies.id = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` companies.id = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` companies.id = suppliers.companyId ``` |
| [connections](#connections) | ``` companies.id = connections.companyId ``` |
| [events](#events) | ``` companies.id = events.companyId ``` |
| [items](#items) | ``` companies.id = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` companies.id = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` companies.id = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` companies.id = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` companies.id = bank_accounts.companyId ``` |

companies table schema

|  |
| --- |
| **id**  STRING |
| **lastSync**  DATE-TIME |
| **name**  STRING |
| **platform**  STRING |
| **redirect**  STRING |
| **status**  STRING |

### company\_info

The `company_info` table contains company info. In Codat, company info includes information about a linked company such as address, phone number and company registration.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | companyId |
| **Useful links** | [Codat documentation](https://docs.codat.io/reference/info)  [Codat API method](https://docs.codat.io/reference/info#info_list "Opens in new tab: Codat API method") |

company\_info table foreign keys

| Join company\_info with | on |
| --- | --- |
| [companies](#companies) | ``` company_info.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` company_info.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` company_info.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` company_info.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` company_info.companyId = bill_payments.supplierRef.companyId ```  ``` company_info.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` company_info.companyId = bills.companyId ``` |
| [customers](#customers) | ``` company_info.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` company_info.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` company_info.companyId = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` company_info.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` company_info.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` company_info.companyId = connections.companyId ``` |
| [events](#events) | ``` company_info.companyId = events.companyId ``` |
| [items](#items) | ``` company_info.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` company_info.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` company_info.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` company_info.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` company_info.companyId = bank_accounts.companyId ``` |

company\_info table schema

|  |
| --- |
| **accountingPlatformRef**  STRING |
| **addresses**  ARRAY This is a nested data structure:   - city: STRING - country: STRING - line1: STRING - line2: STRING - postalCode: STRING - region: STRING - type: STRING |
| **baseCurrency**  STRING |
| **companyId**  STRING |
| **companyLegalName**  STRING |
| **companyName**  STRING |
| **createdDate**  STRING |
| **financialYearStartDate**  DATE-TIME |
| **phoneNumbers**  ARRAY This is a nested data structure:   - number: STRING - type: STRING |
| **registrationNumber**  STRING |
| **taxNumber**  STRING |
| **webLinks**  ARRAY This is a nested data structure:   - type: STRING - url: STRING |

### connections

The connections table contains information about company connections in your Codat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | companyId  id |
| **Useful links** | [Codat API method](https://docs.codat.io/reference/connection#connection_getconnection "Opens in new tab: Codat API method") |

connections table foreign keys

| Join connections with | on |
| --- | --- |
| [companies](#companies) | ``` connections.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` connections.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` connections.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` connections.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` connections.companyId = bill_payments.supplierRef.companyId ```  ``` connections.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` connections.companyId = bills.companyId ``` |
| [company\_info](#company-info) | ``` connections.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` connections.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` connections.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` connections.companyId = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` connections.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` connections.companyId = suppliers.companyId ``` |
| [events](#events) | ``` connections.companyId = events.companyId ``` |
| [items](#items) | ``` connections.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` connections.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` connections.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` connections.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` connections.companyId = bank_accounts.companyId ```  ``` connections.id = bank_accounts.connectionId ``` |

connections table schema

|  |
| --- |
| **companyId**  STRING |
| **id**  STRING |
| **integrationId**  STRING |
| **linkUrl**  STRING |
| **platformName**  STRING |
| **sourceId**  STRING |
| **status**  STRING |

### credit\_notes

The `credit_notes` table contains info about the credit notes in your Codat instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  companyId |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/credit-notes)  [Codat API method](https://docs.codat.io/reference/creditnotes#creditnotes_listpaged "Opens in new tab: Codat API method") |

credit\_notes table foreign keys

| Join credit\_notes with | on |
| --- | --- |
| [payments](#payments) | ``` credit_notes.id = payments.lines.links.id ```  ``` credit_notes.customerRef.id = payments.customerRef.id ``` |
| [customers](#customers) | ``` credit_notes.customerRef.id = customers.id ``` |

credit\_notes table schema

|  |
| --- |
| **companyId**  STRING |
| **creditNoteNumber**  STRING |
| **currency**  STRING |
| **customerRef**  OBJECT This is a nested data structure:   - companyName: STRING - id: STRING |
| **id**  STRING |
| **issueDate**  DATE-TIME |
| **paymentAllocations**  ARRAY This is a nested data structure. |
| **remainingCredit**  NUMBER |
| **status**  STRING |
| **totalAmount**  NUMBER |

### customers

The `customers` table contains info about the customers in your Codat instance. A customer is a person or organisation that buys goods or services.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | companyId  id |
| **Replication Key** | modifiedDate |
| **Useful links** | [Codat documentation](https://docs.codat.io/reference/customers)  [Codat API method](https://docs.codat.io/reference/customers#customers_listpaged "Opens in new tab: Codat API method") |

customers table foreign keys

| Join customers with | on |
| --- | --- |
| [companies](#companies) | ``` customers.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` customers.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` customers.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` customers.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` customers.companyId = bill_payments.supplierRef.companyId ```  ``` customers.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` customers.companyId = bills.companyId ``` |
| [company\_info](#company-info) | ``` customers.companyId = company_info.companyId ``` |
| [invoices](#invoices) | ``` customers.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` customers.companyId = payments.companyId ```  ``` customers.id = payments.customerRef.id ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` customers.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` customers.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` customers.companyId = connections.companyId ``` |
| [events](#events) | ``` customers.companyId = events.companyId ``` |
| [items](#items) | ``` customers.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` customers.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` customers.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` customers.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` customers.companyId = bank_accounts.companyId ``` |
| [credit\_notes](#credit-notes) | ``` customers.id = credit_notes.customerRef.id ``` |

customers table schema

|  |
| --- |
| **addresses**  ARRAY This is a nested data structure:   - city: STRING - country: STRING - line1: STRING - line2: STRING - postalCode: STRING - region: STRING - type: STRING |
| **companyId**  STRING |
| **contactName**  STRING |
| **contacts**  ARRAY This is a nested data structure:   - address: OBJECT, which is also a nested data structure.   - city: STRING   - country: STRING   - line1: STRING   - line2: STRING   - postalCode: STRING   - region: STRING   - type: STRING - email: STRING - modifiedDate: DATE-TIME - name: STRING - phone: ARRAY, which is also a nested data structure.   - number: STRING   - type: STRING - status: STRING |
| **customerName**  STRING |
| **defaultCurrency**  STRING |
| **emailAddress**  STRING |
| **id**  STRING |
| **modifiedDate**  DATE-TIME |
| **phone**  STRING |
| **registrationNumber**  STRING |
| **status**  STRING |
| **taxNumber**  STRING |

### events

The `events` table contains information about a given company’s events in your Codat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | companyId  eventTimeUtc |
| **Useful links** | [Codat API method](https://docs.codat.io/reference/reports#reports_companyevents "Opens in new tab: Codat API method") |

events table foreign keys

| Join events with | on |
| --- | --- |
| [companies](#companies) | ``` events.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` events.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` events.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` events.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` events.companyId = bill_payments.supplierRef.companyId ```  ``` events.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` events.companyId = bills.companyId ``` |
| [company\_info](#company-info) | ``` events.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` events.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` events.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` events.companyId = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` events.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` events.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` events.companyId = connections.companyId ``` |
| [items](#items) | ``` events.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` events.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` events.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` events.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` events.companyId = bank_accounts.companyId ``` |

events table schema

|  |
| --- |
| **companyId**  STRING |
| **description**  STRING |
| **eventTimeUtc**  STRING |
| **type**  STRING |

### invoices

The `invoices` table contains info about the invoices in your Codat instance. An invoice is an itemized record of goods or services sold to a [customer](#customers).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | companyId  id |
| **Replication Key** | modifiedDate |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/invoices-1)  [Codat API method](https://docs.codat.io/reference/invoices#invoices_listpaged "Opens in new tab: Codat API method") |

invoices table foreign keys

| Join invoices with | on |
| --- | --- |
| [companies](#companies) | ``` invoices.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` invoices.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` invoices.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` invoices.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` invoices.companyId = bill_payments.supplierRef.companyId ```  ``` invoices.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` invoices.companyId = bills.companyId ``` |
| [company\_info](#company-info) | ``` invoices.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` invoices.companyId = customers.companyId ``` |
| [payments](#payments) | ``` invoices.companyId = payments.companyId ```  ``` invoices.id = payments.lines.links.id ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` invoices.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` invoices.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` invoices.companyId = connections.companyId ``` |
| [events](#events) | ``` invoices.companyId = events.companyId ``` |
| [items](#items) | ``` invoices.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` invoices.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` invoices.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` invoices.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` invoices.companyId = bank_accounts.companyId ``` |

invoices table schema

|  |
| --- |
| **amountDue**  NUMBER |
| **companyId**  STRING |
| **currency**  STRING |
| **customerRef**  OBJECT This is a nested data structure:   - companyName: STRING - id: STRING |
| **dueDate**  DATE-TIME |
| **id**  STRING |
| **invoiceNumber**  STRING |
| **issueDate**  DATE-TIME |
| **lineItems**  ARRAY This is a nested data structure:   - description: STRING - discountAmount: NUMBER - quantity: NUMBER - subTotal: NUMBER - taxAmount: NUMBER - totalAmount: NUMBER - unitAmount: NUMBER |
| **modifiedDate**  DATE-TIME |
| **paidOnDate**  DATE-TIME |
| **paymentAllocations**  ARRAY This is a nested data structure. |
| **status**  STRING |
| **subTotal**  NUMBER |
| **totalAmount**  NUMBER |
| **totalDiscount**  NUMBER |
| **totalTaxAmount**  NUMBER |

### items

The items table contains information about items for a given company in your Codat account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | companyId  id |
| **Replication Key** | modifiedDate |
| **Useful links** | [Codat documentation](https://docs.codat.io/reference/items)  [Codat API method](https://docs.codat.io/reference/items#items_listpaged "Opens in new tab: Codat API method") |

items table foreign keys

| Join items with | on |
| --- | --- |
| [accounts](#accounts) | ``` items.billItem.accountRef.id = accounts.id ```  ``` items.invoiceItem.accountRef.id = accounts.id ``` |
| [balance\_sheets](#balance-sheets) | ``` items.billItem.accountRef.id = balance_sheets.reports.assets.accountId ```  ``` items.invoiceItem.accountRef.id = balance_sheets.reports.assets.accountId ```  ``` items.billItem.accountRef.id = balance_sheets.reports.equity.accountId ```  ``` items.invoiceItem.accountRef.id = balance_sheets.reports.equity.accountId ```  ``` items.billItem.accountRef.id = balance_sheets.reports.liabilities.accountId ```  ``` items.invoiceItem.accountRef.id = balance_sheets.reports.liabilities.accountId ```  ``` items.companyId = balance_sheets.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` items.billItem.accountRef.id = profit_and_loss.reports.costOfSales.accountId ```  ``` items.invoiceItem.accountRef.id = profit_and_loss.reports.costOfSales.accountId ```  ``` items.billItem.accountRef.id = profit_and_loss.reports.expenses.accountId ```  ``` items.invoiceItem.accountRef.id = profit_and_loss.reports.expenses.accountId ```  ``` items.billItem.accountRef.id = profit_and_loss.reports.income.accountId ```  ``` items.invoiceItem.accountRef.id = profit_and_loss.reports.income.accountId ```  ``` items.billItem.accountRef.id = profit_and_loss.reports.otherExpenses.accountId ```  ``` items.invoiceItem.accountRef.id = profit_and_loss.reports.otherExpenses.accountId ```  ``` items.billItem.accountRef.id = profit_and_loss.reports.otherIncome.accountId ```  ``` items.invoiceItem.accountRef.id = profit_and_loss.reports.otherIncome.accountId ```  ``` items.companyId = profit_and_loss.companyId ``` |
| [bills](#bills) | ``` items.billItem.accountRef.id = bills.lineItems.accountRef.id ```  ``` items.invoiceItem.accountRef.id = bills.lineItems.accountRef.id ```  ``` items.companyId = bills.companyId ```  ``` items.id = bills.lineItems.itemRef.id ```  ``` items.billItem.taxRateRef.id = bills.lineItems.taxRateRef.id ```  ``` items.invoiceItem.taxRateRef.id = bills.lineItems.taxRateRef.id ``` |
| [journal\_entries](#journal-entries) | ``` items.billItem.accountRef.id = journal_entries.journalLines.accountRef.id ```  ``` items.invoiceItem.accountRef.id = journal_entries.journalLines.accountRef.id ```  ``` items.companyId = journal_entries.companyId ``` |
| [companies](#companies) | ``` items.companyId = companies.id ``` |
| [bank\_statements](#bank-statements) | ``` items.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` items.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` items.companyId = bill_payments.supplierRef.companyId ```  ``` items.companyId = bill_payments.companyId ``` |
| [company\_info](#company-info) | ``` items.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` items.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` items.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` items.companyId = payments.companyId ``` |
| [suppliers](#suppliers) | ``` items.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` items.companyId = connections.companyId ``` |
| [events](#events) | ``` items.companyId = events.companyId ``` |
| [tax\_rates](#tax-rates) | ``` items.companyId = tax_rates.companyId ```  ``` items.billItem.taxRateRef.id = tax_rates.id ```  ``` items.invoiceItem.taxRateRef.id = tax_rates.id ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` items.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` items.companyId = bank_accounts.companyId ``` |

items table schema

|  |
| --- |
| **billItem**  OBJECT This is a nested data structure:   - accountRef: OBJECT, which is also a nested data structure.   - id: STRING - description: STRING - taxRateRef: OBJECT, which is also a nested data structure.   - id: STRING - unitPrice: NUMBER |
| **code**  STRING |
| **companyId**  STRING |
| **id**  STRING |
| **invoiceItem**  OBJECT This is a nested data structure:   - accountRef: OBJECT, which is also a nested data structure.   - id: STRING - description: STRING - taxRateRef: OBJECT, which is also a nested data structure.   - id: STRING - unitPrice: NUMBER |
| **isBillItem**  BOOLEAN |
| **isInvoiceItem**  BOOLEAN |
| **itemStatus**  STRING |
| **modifiedDate**  STRING |
| **name**  STRING |
| **sourceModifiedDate**  STRING |

### journal\_entries

The journal\_entries table contains information about journal entries for a given company in your Codat account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | companyId  id |
| **Replication Key** | modifiedDate |
| **Useful links** | [Codat documentation](https://docs.codat.io/reference/journals)  [Codat API method](https://docs.codat.io/reference/journals#journals_listpaged "Opens in new tab: Codat API method") |

journal\_entries table foreign keys

| Join journal\_entries with | on |
| --- | --- |
| [accounts](#accounts) | ``` journal_entries.journalLines.accountRef.id = accounts.id ``` |
| [balance\_sheets](#balance-sheets) | ``` journal_entries.journalLines.accountRef.id = balance_sheets.reports.assets.accountId ```  ``` journal_entries.journalLines.accountRef.id = balance_sheets.reports.equity.accountId ```  ``` journal_entries.journalLines.accountRef.id = balance_sheets.reports.liabilities.accountId ```  ``` journal_entries.companyId = balance_sheets.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` journal_entries.journalLines.accountRef.id = profit_and_loss.reports.costOfSales.accountId ```  ``` journal_entries.journalLines.accountRef.id = profit_and_loss.reports.expenses.accountId ```  ``` journal_entries.journalLines.accountRef.id = profit_and_loss.reports.income.accountId ```  ``` journal_entries.journalLines.accountRef.id = profit_and_loss.reports.otherExpenses.accountId ```  ``` journal_entries.journalLines.accountRef.id = profit_and_loss.reports.otherIncome.accountId ```  ``` journal_entries.companyId = profit_and_loss.companyId ``` |
| [bills](#bills) | ``` journal_entries.journalLines.accountRef.id = bills.lineItems.accountRef.id ```  ``` journal_entries.companyId = bills.companyId ``` |
| [items](#items) | ``` journal_entries.journalLines.accountRef.id = items.billItem.accountRef.id ```  ``` journal_entries.journalLines.accountRef.id = items.invoiceItem.accountRef.id ```  ``` journal_entries.companyId = items.companyId ``` |
| [companies](#companies) | ``` journal_entries.companyId = companies.id ``` |
| [bank\_statements](#bank-statements) | ``` journal_entries.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` journal_entries.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` journal_entries.companyId = bill_payments.supplierRef.companyId ```  ``` journal_entries.companyId = bill_payments.companyId ``` |
| [company\_info](#company-info) | ``` journal_entries.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` journal_entries.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` journal_entries.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` journal_entries.companyId = payments.companyId ``` |
| [suppliers](#suppliers) | ``` journal_entries.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` journal_entries.companyId = connections.companyId ``` |
| [events](#events) | ``` journal_entries.companyId = events.companyId ``` |
| [tax\_rates](#tax-rates) | ``` journal_entries.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` journal_entries.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` journal_entries.companyId = bank_accounts.companyId ``` |

journal\_entries table schema

|  |
| --- |
| **companyId**  STRING |
| **createdOn**  STRING |
| **id**  STRING |
| **journalLines**  ARRAY This is a nested data structure:   - accountRef: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING - currency: STRING - description: STRING - grossAmount: NUMBER - id: STRING - netAmount: NUMBER - taxAmount: NUMBER |
| **modifiedDate**  STRING |
| **postedOn**  STRING |
| **sourceModifiedDate**  STRING |

### payments

The `payments` table contains info about the payments, or Accounts Receivable transactions, in your Codat instance. This includes details about invoices and credit notes.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | companyId  id |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/payments-1)  [Codat API method](https://docs.codat.io/reference/payments#payments_listpaged "Opens in new tab: Codat API method") |

payments table foreign keys

| Join payments with | on |
| --- | --- |
| [companies](#companies) | ``` payments.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` payments.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` payments.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` payments.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` payments.companyId = bill_payments.supplierRef.companyId ```  ``` payments.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` payments.companyId = bills.companyId ``` |
| [company\_info](#company-info) | ``` payments.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` payments.companyId = customers.companyId ```  ``` payments.customerRef.id = customers.id ``` |
| [invoices](#invoices) | ``` payments.companyId = invoices.companyId ```  ``` payments.lines.links.id = invoices.id ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` payments.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` payments.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` payments.companyId = connections.companyId ``` |
| [events](#events) | ``` payments.companyId = events.companyId ``` |
| [items](#items) | ``` payments.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` payments.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` payments.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` payments.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` payments.companyId = bank_accounts.companyId ``` |
| [credit\_notes](#credit-notes) | ``` payments.lines.links.id = credit_notes.id ```  ``` payments.customerRef.id = credit_notes.customerRef.id ``` |

payments table schema

|  |
| --- |
| **companyId**  STRING |
| **currency**  STRING |
| **customerRef**  OBJECT This is a nested data structure:   - companyName: STRING - id: STRING |
| **date**  DATE-TIME |
| **id**  STRING |
| **lines**  ARRAY This is a nested data structure:   - amount: NUMBER - links: ARRAY, which is also a nested data structure.   - id: STRING   - type: STRING |
| **note**  STRING |
| **totalAmount**  NUMBER |

### profit\_and\_loss

The `profit_and_loss` table contains profit and loss report data for a company over a time period.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | companyId |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/profit-and-loss-2)  [Codat API method](https://docs.codat.io/reference/financials#financials_profitandloss "Opens in new tab: Codat API method") |

profit\_and\_loss table foreign keys

| Join profit\_and\_loss with | on |
| --- | --- |
| [accounts](#accounts) | ``` profit_and_loss.reports.costOfSales.accountId = accounts.id ```  ``` profit_and_loss.reports.expenses.accountId = accounts.id ```  ``` profit_and_loss.reports.income.accountId = accounts.id ```  ``` profit_and_loss.reports.otherExpenses.accountId = accounts.id ```  ``` profit_and_loss.reports.otherIncome.accountId = accounts.id ``` |
| [balance\_sheets](#balance-sheets) | ``` profit_and_loss.reports.costOfSales.accountId = balance_sheets.reports.assets.accountId ```  ``` profit_and_loss.reports.expenses.accountId = balance_sheets.reports.assets.accountId ```  ``` profit_and_loss.reports.income.accountId = balance_sheets.reports.assets.accountId ```  ``` profit_and_loss.reports.otherExpenses.accountId = balance_sheets.reports.assets.accountId ```  ``` profit_and_loss.reports.otherIncome.accountId = balance_sheets.reports.assets.accountId ```  ``` profit_and_loss.reports.costOfSales.accountId = balance_sheets.reports.equity.accountId ```  ``` profit_and_loss.reports.expenses.accountId = balance_sheets.reports.equity.accountId ```  ``` profit_and_loss.reports.income.accountId = balance_sheets.reports.equity.accountId ```  ``` profit_and_loss.reports.otherExpenses.accountId = balance_sheets.reports.equity.accountId ```  ``` profit_and_loss.reports.otherIncome.accountId = balance_sheets.reports.equity.accountId ```  ``` profit_and_loss.reports.costOfSales.accountId = balance_sheets.reports.liabilities.accountId ```  ``` profit_and_loss.reports.expenses.accountId = balance_sheets.reports.liabilities.accountId ```  ``` profit_and_loss.reports.income.accountId = balance_sheets.reports.liabilities.accountId ```  ``` profit_and_loss.reports.otherExpenses.accountId = balance_sheets.reports.liabilities.accountId ```  ``` profit_and_loss.reports.otherIncome.accountId = balance_sheets.reports.liabilities.accountId ```  ``` profit_and_loss.companyId = balance_sheets.companyId ``` |
| [bills](#bills) | ``` profit_and_loss.reports.costOfSales.accountId = bills.lineItems.accountRef.id ```  ``` profit_and_loss.reports.expenses.accountId = bills.lineItems.accountRef.id ```  ``` profit_and_loss.reports.income.accountId = bills.lineItems.accountRef.id ```  ``` profit_and_loss.reports.otherExpenses.accountId = bills.lineItems.accountRef.id ```  ``` profit_and_loss.reports.otherIncome.accountId = bills.lineItems.accountRef.id ```  ``` profit_and_loss.companyId = bills.companyId ``` |
| [items](#items) | ``` profit_and_loss.reports.costOfSales.accountId = items.billItem.accountRef.id ```  ``` profit_and_loss.reports.expenses.accountId = items.billItem.accountRef.id ```  ``` profit_and_loss.reports.income.accountId = items.billItem.accountRef.id ```  ``` profit_and_loss.reports.otherExpenses.accountId = items.billItem.accountRef.id ```  ``` profit_and_loss.reports.otherIncome.accountId = items.billItem.accountRef.id ```  ``` profit_and_loss.reports.costOfSales.accountId = items.invoiceItem.accountRef.id ```  ``` profit_and_loss.reports.expenses.accountId = items.invoiceItem.accountRef.id ```  ``` profit_and_loss.reports.income.accountId = items.invoiceItem.accountRef.id ```  ``` profit_and_loss.reports.otherExpenses.accountId = items.invoiceItem.accountRef.id ```  ``` profit_and_loss.reports.otherIncome.accountId = items.invoiceItem.accountRef.id ```  ``` profit_and_loss.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` profit_and_loss.reports.costOfSales.accountId = journal_entries.journalLines.accountRef.id ```  ``` profit_and_loss.reports.expenses.accountId = journal_entries.journalLines.accountRef.id ```  ``` profit_and_loss.reports.income.accountId = journal_entries.journalLines.accountRef.id ```  ``` profit_and_loss.reports.otherExpenses.accountId = journal_entries.journalLines.accountRef.id ```  ``` profit_and_loss.reports.otherIncome.accountId = journal_entries.journalLines.accountRef.id ```  ``` profit_and_loss.companyId = journal_entries.companyId ``` |
| [companies](#companies) | ``` profit_and_loss.companyId = companies.id ``` |
| [bank\_statements](#bank-statements) | ``` profit_and_loss.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` profit_and_loss.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` profit_and_loss.companyId = bill_payments.supplierRef.companyId ```  ``` profit_and_loss.companyId = bill_payments.companyId ``` |
| [company\_info](#company-info) | ``` profit_and_loss.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` profit_and_loss.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` profit_and_loss.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` profit_and_loss.companyId = payments.companyId ``` |
| [suppliers](#suppliers) | ``` profit_and_loss.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` profit_and_loss.companyId = connections.companyId ``` |
| [events](#events) | ``` profit_and_loss.companyId = events.companyId ``` |
| [tax\_rates](#tax-rates) | ``` profit_and_loss.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` profit_and_loss.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` profit_and_loss.companyId = bank_accounts.companyId ``` |

profit\_and\_loss table schema

|  |
| --- |
| **companyId**  STRING |
| **currency**  STRING |
| **mostRecentAvailableMonth**  STRING |
| **reportBasis**  STRING |
| **reports**  ARRAY This is a nested data structure:   - costOfSales: ARRAY, which is also a nested data structure.   - accountId: STRING   - name: STRING   - value: NUMBER - expenses: ARRAY, which is also a nested data structure.   - accountId: STRING   - name: STRING   - value: NUMBER - fromDate: STRING - grossProfit: NUMBER - income: ARRAY, which is also a nested data structure.   - accountId: STRING   - name: STRING   - value: NUMBER - netOperatingProfit: NUMBER - netOtherIncome: NUMBER - netProfit: NUMBER - otherExpenses: ARRAY, which is also a nested data structure.   - accountId: STRING   - name: STRING   - value: NUMBER - otherIncome: ARRAY, which is also a nested data structure.   - accountId: STRING   - name: STRING   - value: NUMBER - toDate: STRING |

### suppliers

The `suppliers` table contains info about the suppliers in your Codat instance. A supplier is a person or organization that provides a product or service.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | companyId  id |
| **Useful links** | [Codat documentation](https://docs.codat.io/Content/suppliers-2)  [Codat API method](https://docs.codat.io/reference/suppliers#suppliers_listpaged "Opens in new tab: Codat API method") |

suppliers table foreign keys

| Join suppliers with | on |
| --- | --- |
| [companies](#companies) | ``` suppliers.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` suppliers.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` suppliers.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` suppliers.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` suppliers.companyId = bill_payments.supplierRef.companyId ```  ``` suppliers.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` suppliers.companyId = bills.companyId ```  ``` suppliers.id = bills.supplierRef ``` |
| [company\_info](#company-info) | ``` suppliers.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` suppliers.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` suppliers.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` suppliers.companyId = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` suppliers.companyId = profit_and_loss.companyId ``` |
| [connections](#connections) | ``` suppliers.companyId = connections.companyId ``` |
| [events](#events) | ``` suppliers.companyId = events.companyId ``` |
| [items](#items) | ``` suppliers.companyId = items.companyId ``` |
| [journal\_entries](#journal-entries) | ``` suppliers.companyId = journal_entries.companyId ``` |
| [tax\_rates](#tax-rates) | ``` suppliers.companyId = tax_rates.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` suppliers.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` suppliers.companyId = bank_accounts.companyId ``` |

suppliers table schema

|  |
| --- |
| **addresses**  ARRAY This is a nested data structure:   - city: STRING - country: STRING - line1: STRING - line2: STRING - postalCode: STRING - region: STRING - type: STRING |
| **companyId**  STRING |
| **contactName**  STRING |
| **emailAddress**  STRING |
| **id**  STRING |
| **phone**  STRING |
| **registrationNumber**  STRING |
| **status**  STRING |
| **supplierName**  STRING |
| **taxNumber**  STRING |

### tax\_rates

The tax\_rates table contains information about tax rates for a given company in your Codat account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | companyId  id |
| **Replication Key** | modifiedDate |
| **Useful links** | [Codat documentation](https://docs.codat.io/reference/taxrates)  [Codat API method](https://docs.codat.io/reference/taxrates#taxrates_listpaged "Opens in new tab: Codat API method") |

tax\_rates table foreign keys

| Join tax\_rates with | on |
| --- | --- |
| [companies](#companies) | ``` tax_rates.companyId = companies.id ``` |
| [balance\_sheets](#balance-sheets) | ``` tax_rates.companyId = balance_sheets.companyId ``` |
| [bank\_statements](#bank-statements) | ``` tax_rates.companyId = bank_statements.companyId ``` |
| [bank\_statement\_lines](#bank-statement-lines) | ``` tax_rates.companyId = bank_statement_lines.companyId ``` |
| [bill\_payments](#bill-payments) | ``` tax_rates.companyId = bill_payments.supplierRef.companyId ```  ``` tax_rates.companyId = bill_payments.companyId ``` |
| [bills](#bills) | ``` tax_rates.companyId = bills.companyId ```  ``` tax_rates.id = bills.lineItems.taxRateRef.id ``` |
| [company\_info](#company-info) | ``` tax_rates.companyId = company_info.companyId ``` |
| [customers](#customers) | ``` tax_rates.companyId = customers.companyId ``` |
| [invoices](#invoices) | ``` tax_rates.companyId = invoices.companyId ``` |
| [payments](#payments) | ``` tax_rates.companyId = payments.companyId ``` |
| [profit\_and\_loss](#profit-and-loss) | ``` tax_rates.companyId = profit_and_loss.companyId ``` |
| [suppliers](#suppliers) | ``` tax_rates.companyId = suppliers.companyId ``` |
| [connections](#connections) | ``` tax_rates.companyId = connections.companyId ``` |
| [events](#events) | ``` tax_rates.companyId = events.companyId ``` |
| [items](#items) | ``` tax_rates.companyId = items.companyId ```  ``` tax_rates.id = items.billItem.taxRateRef.id ```  ``` tax_rates.id = items.invoiceItem.taxRateRef.id ``` |
| [journal\_entries](#journal-entries) | ``` tax_rates.companyId = journal_entries.companyId ``` |
| [bank\_account\_transactions](#bank-account-transactions) | ``` tax_rates.companyId = bank_account_transactions.companyId ``` |
| [bank\_accounts](#bank-accounts) | ``` tax_rates.companyId = bank_accounts.companyId ``` |

tax\_rates table schema

|  |
| --- |
| **code**  STRING |
| **companyId**  STRING |
| **components**  ARRAY This is a nested data structure:   - isCompound: BOOLEAN - name: STRING - rate: NUMBER |
| **effectiveTaxRate**  NUMBER |
| **id**  STRING |
| **modifiedDate**  STRING |
| **name**  STRING |
| **sourceModifiedDate**  STRING |
| **totalTaxRate**  NUMBER |
