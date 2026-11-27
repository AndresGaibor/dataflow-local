---
title: "QuickBooks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-QuickBooks-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# QuickBooks

QuickBooks is an online accounting software package. You can use a QuickBooks private app as a data source when landing or replicating data.

See the [Schema](#Schema) section for a list of objects available for replication.

Currently, replicating data f
rom QuickBooks desktop apps isn’t supported.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To create an OAuth 2.0 app for QuickBooks:

1. Log into [Intuit Developer Portal](https://developer.intuit.com/app/developer/homepage).
2. From the dashboard, click + Create an App.
3. Under Platforms, choose QuickBooks Online.
4. Name your app and choose the accounting scopes: com.intuit.quickbooks.accounting.

To obtain your client ID and secret:

1. In your app settings, go to Keys & OAuth section.
2. Copy your client ID and secret.
3. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.

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
| Realm ID | QuickBooks company ID. You can find it under your Account Settings > Billing and Subscription of your QuickBooks account. |
| Connect to a sandbox environment | Select this option if you are connecting to a sandbox environment. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### accounts

The `accounts` table contains info about the various account types in you QuickBooks instance. This table includes all account types: asset, liability, revenue (income), expenses, and equity.

**Note**: Both active and inactive accounts are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/most-commonly-used/account)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/most-commonly-used/account#query-an-account "Opens in new tab: QuickBooks API method") |

accounts table foreign keys

| Join accounts with | on |
| --- | --- |
| [bill\_payments](#bill-payments) | ``` accounts.Id = bill_payments.APAccountRef.value ```  ``` accounts.ParentRef.value = bill_payments.APAccountRef.value ```  ``` accounts.Id = bill_payments.CheckPayment.BankAccountRef.value ```  ``` accounts.ParentRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` accounts.Id = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` accounts.ParentRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` accounts.CurrencyRef.value = bill_payments.CurrencyRef.value ``` |
| [bills](#bills) | ``` accounts.Id = bills.APAccountRef.value ```  ``` accounts.ParentRef.value = bills.APAccountRef.value ```  ``` accounts.Id = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` accounts.ParentRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` accounts.CurrencyRef.value = bills.CurrencyRef.value ``` |
| [budgets](#budgets) | ``` accounts.Id = budgets.BudgetDetail.AccountRef.value ```  ``` accounts.ParentRef.value = budgets.BudgetDetail.AccountRef.value ``` |
| [deposits](#deposits) | ``` accounts.Id = deposits.CashBack.AccountRef.value ```  ``` accounts.ParentRef.value = deposits.CashBack.AccountRef.value ```  ``` accounts.Id = deposits.DepositToAccountRef.value ```  ``` accounts.ParentRef.value = deposits.DepositToAccountRef.value ```  ``` accounts.Id = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` accounts.ParentRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` accounts.CurrencyRef.value = deposits.CurrencyRef.value ``` |
| [invoices](#invoices) | ``` accounts.Id = invoices.DepositToAccountRef.value ```  ``` accounts.ParentRef.value = invoices.DepositToAccountRef.value ```  ``` accounts.Id = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` accounts.ParentRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` accounts.CurrencyRef.value = invoices.CurrencyRef.value ``` |
| [items](#items) | ``` accounts.Id = items.AssetAccountRef.value ```  ``` accounts.ParentRef.value = items.AssetAccountRef.value ```  ``` accounts.Id = items.ExpenseAccountRef.value ```  ``` accounts.ParentRef.value = items.ExpenseAccountRef.value ```  ``` accounts.Id = items.IncomeAccountRef.value ```  ``` accounts.ParentRef.value = items.IncomeAccountRef.value ``` |
| [journal\_entries](#journal-entries) | ``` accounts.Id = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` accounts.ParentRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` accounts.CurrencyRef.value = journal_entries.CurrencyRef.value ``` |
| [payments](#payments) | ``` accounts.Id = payments.DepositToAccountRef.value ```  ``` accounts.ParentRef.value = payments.DepositToAccountRef.value ```  ``` accounts.CurrencyRef.value = payments.CurrencyRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` accounts.Id = purchase_orders.APAccountRef.value ```  ``` accounts.ParentRef.value = purchase_orders.APAccountRef.value ```  ``` accounts.CurrencyRef.value = purchase_orders.CurrencyRef.value ``` |
| [purchases](#purchases) | ``` accounts.Id = purchases.AccountRef.value ```  ``` accounts.ParentRef.value = purchases.AccountRef.value ```  ``` accounts.Id = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` accounts.ParentRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` accounts.CurrencyRef.value = purchases.CurrencyRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` accounts.Id = refund_receipts.DepositToAccountRef.value ```  ``` accounts.ParentRef.value = refund_receipts.DepositToAccountRef.value ```  ``` accounts.CurrencyRef.value = refund_receipts.CurrencyRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` accounts.Id = sales_receipts.DepositToAccountRef.value ```  ``` accounts.ParentRef.value = sales_receipts.DepositToAccountRef.value ```  ``` accounts.Id = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` accounts.ParentRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` accounts.CurrencyRef.value = sales_receipts.CurrencyRef.value ``` |
| [transfers](#transfers) | ``` accounts.Id = transfers.FromAccountRef.value ```  ``` accounts.ParentRef.value = transfers.FromAccountRef.value ```  ``` accounts.Id = transfers.ToAccountRef.value ```  ``` accounts.ParentRef.value = transfers.ToAccountRef.value ```  ``` accounts.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` accounts.Id = vendor_credits.APAccountRef.value ```  ``` accounts.ParentRef.value = vendor_credits.APAccountRef.value ```  ``` accounts.Id = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` accounts.ParentRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` accounts.CurrencyRef.value = vendor_credits.CurrencyRef.value ``` |
| [credit\_memos](#credit-memos) | ``` accounts.CurrencyRef.value = credit_memos.CurrencyRef.value ``` |
| [customers](#customers) | ``` accounts.CurrencyRef.value = customers.CurrencyRef.value ``` |
| [estimates](#estimates) | ``` accounts.CurrencyRef.value = estimates.CurrencyRef.value ``` |
| [vendors](#vendors) | ``` accounts.CurrencyRef.value = vendors.CurrencyRef.value ``` |

accounts table schema

|  |
| --- |
| **AccountAlias**  STRING |
| **AccountSubType**  STRING |
| **AccountType**  STRING |
| **AcctNum**  STRING |
| **Active**  BOOLEAN |
| **Classification**  STRING |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CurrentBalance**  NUMBER |
| **CurrentBalanceWithSubAccounts**  NUMBER |
| **Description**  STRING |
| **FullyQualifiedName**  STRING |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Name**  STRING |
| **ParentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SubAccount**  BOOLEAN |
| **SyncToken**  STRING |
| **TaxCodeRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **TxnLocationType**  STRING |
| **domain**  STRING |

### bill\_payments

The `bill_payments` table contains info about payments made on bills received from vendors for goods or services.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/billpayment)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/billpayment#query-a-billpayment "Opens in new tab: QuickBooks API method") |

bill\_payments table foreign keys

| Join bill\_payments with | on |
| --- | --- |
| [accounts](#accounts) | ``` bill_payments.APAccountRef.value = accounts.Id ```  ``` bill_payments.CheckPayment.BankAccountRef.value = accounts.Id ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = accounts.Id ```  ``` bill_payments.APAccountRef.value = accounts.ParentRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = accounts.ParentRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = accounts.ParentRef.value ```  ``` bill_payments.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bills](#bills) | ``` bill_payments.APAccountRef.value = bills.APAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = bills.APAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = bills.APAccountRef.value ```  ``` bill_payments.APAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bill_payments.Id = bills.LinkedTxn.TxnId ```  ``` bill_payments.Line.LinkedTxn.TxnId = bills.Id ```  ``` bill_payments.CurrencyRef.value = bills.CurrencyRef.value ```  ``` bill_payments.DepartmentRef.value = bills.DepartmentRef.value ```  ``` bill_payments.VendorRef.value = bills.VendorRef.value ``` |
| [budgets](#budgets) | ``` bill_payments.APAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` bill_payments.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [deposits](#deposits) | ``` bill_payments.APAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` bill_payments.APAccountRef.value = deposits.DepositToAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = deposits.DepositToAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = deposits.DepositToAccountRef.value ```  ``` bill_payments.APAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` bill_payments.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` bill_payments.DepartmentRef.value = deposits.DepartmentRef.value ```  ``` bill_payments.Line.LinkedTxn.TxnId = deposits.Line.LinkedTxn.TxnId ``` |
| [invoices](#invoices) | ``` bill_payments.APAccountRef.value = invoices.DepositToAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = invoices.DepositToAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = invoices.DepositToAccountRef.value ```  ``` bill_payments.APAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` bill_payments.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` bill_payments.DepartmentRef.value = invoices.DepartmentRef.value ``` |
| [items](#items) | ``` bill_payments.APAccountRef.value = items.AssetAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = items.AssetAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = items.AssetAccountRef.value ```  ``` bill_payments.APAccountRef.value = items.ExpenseAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = items.ExpenseAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = items.ExpenseAccountRef.value ```  ``` bill_payments.APAccountRef.value = items.IncomeAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = items.IncomeAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = items.IncomeAccountRef.value ```  ``` bill_payments.VendorRef.value = items.PrefVendorRef.value ``` |
| [journal\_entries](#journal-entries) | ``` bill_payments.APAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` bill_payments.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` bill_payments.Line.LinkedTxn.TxnId = journal_entries.Id ``` |
| [payments](#payments) | ``` bill_payments.APAccountRef.value = payments.DepositToAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = payments.DepositToAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = payments.DepositToAccountRef.value ```  ``` bill_payments.CurrencyRef.value = payments.CurrencyRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` bill_payments.APAccountRef.value = purchase_orders.APAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = purchase_orders.APAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = purchase_orders.APAccountRef.value ```  ``` bill_payments.Line.LinkedTxn.TxnId = purchase_orders.LinkedTxn.TxnId ```  ``` bill_payments.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` bill_payments.DepartmentRef.value = purchase_orders.DepartmentRef.value ```  ``` bill_payments.Id = purchase_orders.Id ```  ``` bill_payments.VendorRef.value = purchase_orders.VendorRef.value ``` |
| [purchases](#purchases) | ``` bill_payments.APAccountRef.value = purchases.AccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = purchases.AccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = purchases.AccountRef.value ```  ``` bill_payments.APAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bill_payments.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` bill_payments.DepartmentRef.value = purchases.DepartmentRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` bill_payments.APAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` bill_payments.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` bill_payments.DepartmentRef.value = refund_receipts.DepartmentRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` bill_payments.APAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` bill_payments.APAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` bill_payments.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` bill_payments.DepartmentRef.value = sales_receipts.DepartmentRef.value ``` |
| [transfers](#transfers) | ``` bill_payments.APAccountRef.value = transfers.FromAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = transfers.FromAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = transfers.FromAccountRef.value ```  ``` bill_payments.APAccountRef.value = transfers.ToAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = transfers.ToAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = transfers.ToAccountRef.value ```  ``` bill_payments.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` bill_payments.APAccountRef.value = vendor_credits.APAccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = vendor_credits.APAccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = vendor_credits.APAccountRef.value ```  ``` bill_payments.APAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bill_payments.CheckPayment.BankAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bill_payments.CreditCardPayment.CCAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bill_payments.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` bill_payments.DepartmentRef.value = vendor_credits.DepartmentRef.value ```  ``` bill_payments.Line.LinkedTxn.TxnId = vendor_credits.Id ```  ``` bill_payments.VendorRef.value = vendor_credits.VendorRef.value ``` |
| [credit\_memos](#credit-memos) | ``` bill_payments.CurrencyRef.value = credit_memos.CurrencyRef.value ``` |
| [customers](#customers) | ``` bill_payments.CurrencyRef.value = customers.CurrencyRef.value ``` |
| [estimates](#estimates) | ``` bill_payments.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` bill_payments.DepartmentRef.value = estimates.DepartmentRef.value ``` |
| [vendors](#vendors) | ``` bill_payments.CurrencyRef.value = vendors.CurrencyRef.value ```  ``` bill_payments.VendorRef.value = vendors.Id ``` |
| [departments](#departments) | ``` bill_payments.DepartmentRef.value = departments.ParentRef.value ```  ``` bill_payments.DepartmentRef.value = departments.Id ``` |
| [time\_activities](#time-activities) | ``` bill_payments.DepartmentRef.value = time_activities.DepartmentRef.value ```  ``` bill_payments.VendorRef.value = time_activities.VendorRef.value ``` |

bill\_payments table schema

|  |
| --- |
| **APAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CheckPayment**  OBJECT This is a nested data structure:   - BankAccountRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING - PrintStatus: STRING |
| **CreditCardPayment**  OBJECT This is a nested data structure:   - CCAccountRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **ExchangeRate**  NUMBER |
| **Id**  STRING |
| **Line**  ARRAY This is a nested data structure:   - Amount: NUMBER - LinkedTxn: ARRAY, which is also a nested data structure.   - TxnId: STRING   - TxnLineId: STRING   - TxnType: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PayType**  STRING |
| **PrivateNote**  STRING |
| **ProcessBillPayment**  BOOLEAN |
| **SyncToken**  STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **VendorRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **domain**  STRING |

### bills

The `bills` table contains info about the bills, or requests for payment from third parties, in your QuickBooks instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/bill)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/bill#query-a-bill "Opens in new tab: QuickBooks API method") |

bills table foreign keys

| Join bills with | on |
| --- | --- |
| [accounts](#accounts) | ``` bills.APAccountRef.value = accounts.Id ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = accounts.Id ```  ``` bills.APAccountRef.value = accounts.ParentRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = accounts.ParentRef.value ```  ``` bills.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` bills.APAccountRef.value = bill_payments.APAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = bill_payments.APAccountRef.value ```  ``` bills.APAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` bills.APAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` bills.LinkedTxn.TxnId = bill_payments.Id ```  ``` bills.Id = bill_payments.Line.LinkedTxn.TxnId ```  ``` bills.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` bills.DepartmentRef.value = bill_payments.DepartmentRef.value ```  ``` bills.VendorRef.value = bill_payments.VendorRef.value ``` |
| [budgets](#budgets) | ``` bills.APAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = budgets.BudgetDetail.CustomerRef.value ```  ``` bills.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [deposits](#deposits) | ``` bills.APAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = deposits.CashBack.AccountRef.value ```  ``` bills.APAccountRef.value = deposits.DepositToAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = deposits.DepositToAccountRef.value ```  ``` bills.APAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` bills.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` bills.DepartmentRef.value = deposits.DepartmentRef.value ``` |
| [invoices](#invoices) | ``` bills.APAccountRef.value = invoices.DepositToAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = invoices.DepositToAccountRef.value ```  ``` bills.APAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` bills.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = invoices.CustomerRef.value ```  ``` bills.DepartmentRef.value = invoices.DepartmentRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.ItemRef.value = invoices.Line.SalesItemLineDetail.ItemRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` bills.SalesTermRef.value = invoices.SalesTermRef.value ``` |
| [items](#items) | ``` bills.APAccountRef.value = items.AssetAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = items.AssetAccountRef.value ```  ``` bills.APAccountRef.value = items.ExpenseAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = items.ExpenseAccountRef.value ```  ``` bills.APAccountRef.value = items.IncomeAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = items.IncomeAccountRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.ItemRef.value = items.Id ```  ``` bills.Line.ItemBasedExpenseLineDetail.ItemRef.value = items.ParentRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ```  ``` bills.VendorRef.value = items.PrefVendorRef.value ``` |
| [journal\_entries](#journal-entries) | ``` bills.APAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` bills.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` bills.Id = journal_entries.Id ``` |
| [payments](#payments) | ``` bills.APAccountRef.value = payments.DepositToAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = payments.DepositToAccountRef.value ```  ``` bills.CurrencyRef.value = payments.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = payments.CustomerRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` bills.APAccountRef.value = purchase_orders.APAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = purchase_orders.APAccountRef.value ```  ``` bills.Id = purchase_orders.LinkedTxn.TxnId ```  ``` bills.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ```  ``` bills.DepartmentRef.value = purchase_orders.DepartmentRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.ItemRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` bills.LinkedTxn.TxnId = purchase_orders.Id ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` bills.SalesTermRef.value = purchase_orders.SalesTermRef.value ```  ``` bills.VendorRef.value = purchase_orders.VendorRef.value ``` |
| [purchases](#purchases) | ``` bills.APAccountRef.value = purchases.AccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = purchases.AccountRef.value ```  ``` bills.APAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bills.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` bills.DepartmentRef.value = purchases.DepartmentRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.ItemRef.value = purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` bills.APAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` bills.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = refund_receipts.CustomerRef.value ```  ``` bills.DepartmentRef.value = refund_receipts.DepartmentRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.ItemRef.value = refund_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` bills.APAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` bills.APAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` bills.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = sales_receipts.CustomerRef.value ```  ``` bills.DepartmentRef.value = sales_receipts.DepartmentRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.ItemRef.value = sales_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [transfers](#transfers) | ``` bills.APAccountRef.value = transfers.FromAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = transfers.FromAccountRef.value ```  ``` bills.APAccountRef.value = transfers.ToAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = transfers.ToAccountRef.value ```  ``` bills.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` bills.APAccountRef.value = vendor_credits.APAccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = vendor_credits.APAccountRef.value ```  ``` bills.APAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.AccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` bills.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` bills.DepartmentRef.value = vendor_credits.DepartmentRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` bills.Id = vendor_credits.Id ```  ``` bills.VendorRef.value = vendor_credits.VendorRef.value ``` |
| [credit\_memos](#credit-memos) | ``` bills.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = credit_memos.CustomerRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.ItemRef.value = credit_memos.Line.SalesItemLineDetail.ItemRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` bills.SalesTermRef.value = credit_memos.SalesTermRef.value ``` |
| [customers](#customers) | ``` bills.CurrencyRef.value = customers.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = customers.Id ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ```  ``` bills.SalesTermRef.value = customers.SalesTermRef.value ``` |
| [estimates](#estimates) | ``` bills.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value = estimates.CustomerRef.value ```  ``` bills.DepartmentRef.value = estimates.DepartmentRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.ItemRef.value = estimates.Line.SalesItemLineDetail.ItemRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` bills.SalesTermRef.value = estimates.SalesTermRef.value ``` |
| [vendors](#vendors) | ``` bills.CurrencyRef.value = vendors.CurrencyRef.value ```  ``` bills.VendorRef.value = vendors.Id ``` |
| [departments](#departments) | ``` bills.DepartmentRef.value = departments.ParentRef.value ```  ``` bills.DepartmentRef.value = departments.Id ``` |
| [time\_activities](#time-activities) | ``` bills.DepartmentRef.value = time_activities.DepartmentRef.value ```  ``` bills.Line.ItemBasedExpenseLineDetail.ItemRef.value = time_activities.ItemRef.value ```  ``` bills.VendorRef.value = time_activities.VendorRef.value ``` |
| [terms](#terms) | ``` bills.SalesTermRef.value = terms.Id ``` |

bills table schema

|  |
| --- |
| **APAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Balance**  NUMBER |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **DueDate**  DATE-TIME |
| **ExchangeRate**  NUMBER |
| **GlobalTaxCalculation**  STRING |
| **HomeBalance**  NUMBER |
| **Id**  STRING |
| **IncludeInAnnualTPAR**  BOOLEAN |
| **Line**  ARRAY This is a nested data structure:   - AccountBasedExpenseLineDetail: OBJECT, which is also a nested data structure.   - AccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - BillableStatus: STRING   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - CustomerRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - TaxAmount: NUMBER   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER - Amount: NUMBER - Description: STRING - DetailType: STRING - Id: STRING - ItemBasedExpenseLineDetail: OBJECT, which is also a nested data structure.   - BillableStatus: STRING   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - CustomerRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - PriceLevelRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Qty: INTEGER   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER   - UnitPrice: NUMBER - LineNum: INTEGER - LinkedTxn: ARRAY, which is also a nested data structure.   - TxnId: STRING   - TxnLineId: STRING   - TxnType: STRING |
| **LinkedTxn**  ARRAY This is a nested data structure:   - TxnId: STRING - TxnLineId: STRING - TxnType: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SalesTermRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SyncToken**  STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnTaxDetail**  OBJECT This is a nested data structure:   - TaxLine: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - DetailType: STRING   - TaxLineDetail: OBJECT, which is also a nested data structure.     - NetAmountTaxable: NUMBER     - OverrideDeltaAmount: NUMBER     - PercentBased: BOOLEAN     - TaxInclusiveAmount: NUMBER     - TaxPercent: NUMBER     - TaxRateRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - TotalTax: NUMBER - TxnTaxCodeRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **VendorRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **domain**  STRING |

### budgets

The `budgets` table contains info about the current state of budgets in your QuickBooks instance. **Note**: Both active and inactive budgets are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/budget)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/budget#query-the-budget "Opens in new tab: QuickBooks API method") |

budgets table foreign keys

| Join budgets with | on |
| --- | --- |
| [accounts](#accounts) | ``` budgets.BudgetDetail.AccountRef.value = accounts.Id ```  ``` budgets.BudgetDetail.AccountRef.value = accounts.ParentRef.value ``` |
| [bill\_payments](#bill-payments) | ``` budgets.BudgetDetail.AccountRef.value = bill_payments.APAccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = bill_payments.DepartmentRef.value ``` |
| [bills](#bills) | ``` budgets.BudgetDetail.AccountRef.value = bills.APAccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` budgets.BudgetDetail.CustomerRef.value = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = bills.DepartmentRef.value ``` |
| [deposits](#deposits) | ``` budgets.BudgetDetail.AccountRef.value = deposits.CashBack.AccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = deposits.DepositToAccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = deposits.DepartmentRef.value ``` |
| [invoices](#invoices) | ``` budgets.BudgetDetail.AccountRef.value = invoices.DepositToAccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` budgets.BudgetDetail.ClassRef.value = invoices.ClassRef.value ```  ``` budgets.BudgetDetail.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` budgets.BudgetDetail.CustomerRef.value = invoices.CustomerRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = invoices.DepartmentRef.value ``` |
| [items](#items) | ``` budgets.BudgetDetail.AccountRef.value = items.AssetAccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = items.ExpenseAccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = items.IncomeAccountRef.value ```  ``` budgets.BudgetDetail.ClassRef.value = items.ClassRef.value ``` |
| [journal\_entries](#journal-entries) | ``` budgets.BudgetDetail.AccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ``` |
| [payments](#payments) | ``` budgets.BudgetDetail.AccountRef.value = payments.DepositToAccountRef.value ```  ``` budgets.BudgetDetail.CustomerRef.value = payments.CustomerRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` budgets.BudgetDetail.AccountRef.value = purchase_orders.APAccountRef.value ```  ``` budgets.BudgetDetail.ClassRef.value = purchase_orders.ClassRef.value ```  ``` budgets.BudgetDetail.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` budgets.BudgetDetail.CustomerRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = purchase_orders.DepartmentRef.value ``` |
| [purchases](#purchases) | ``` budgets.BudgetDetail.AccountRef.value = purchases.AccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` budgets.BudgetDetail.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` budgets.BudgetDetail.CustomerRef.value = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = purchases.DepartmentRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` budgets.BudgetDetail.AccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` budgets.BudgetDetail.ClassRef.value = refund_receipts.ClassRef.value ```  ``` budgets.BudgetDetail.CustomerRef.value = refund_receipts.CustomerRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = refund_receipts.DepartmentRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` budgets.BudgetDetail.AccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` budgets.BudgetDetail.ClassRef.value = sales_receipts.ClassRef.value ```  ``` budgets.BudgetDetail.CustomerRef.value = sales_receipts.CustomerRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = sales_receipts.DepartmentRef.value ``` |
| [transfers](#transfers) | ``` budgets.BudgetDetail.AccountRef.value = transfers.FromAccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = transfers.ToAccountRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` budgets.BudgetDetail.AccountRef.value = vendor_credits.APAccountRef.value ```  ``` budgets.BudgetDetail.AccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` budgets.BudgetDetail.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` budgets.BudgetDetail.CustomerRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = vendor_credits.DepartmentRef.value ``` |
| [classes](#classes) | ``` budgets.BudgetDetail.ClassRef.value = classes.Id ```  ``` budgets.BudgetDetail.ClassRef.value = classes.ParentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` budgets.BudgetDetail.ClassRef.value = credit_memos.ClassRef.value ```  ``` budgets.BudgetDetail.CustomerRef.value = credit_memos.CustomerRef.value ``` |
| [estimates](#estimates) | ``` budgets.BudgetDetail.ClassRef.value = estimates.ClassRef.value ```  ``` budgets.BudgetDetail.CustomerRef.value = estimates.CustomerRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = estimates.DepartmentRef.value ``` |
| [time\_activities](#time-activities) | ``` budgets.BudgetDetail.ClassRef.value = time_activities.ClassRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = time_activities.DepartmentRef.value ``` |
| [customers](#customers) | ``` budgets.BudgetDetail.CustomerRef.value = customers.Id ``` |
| [departments](#departments) | ``` budgets.BudgetDetail.DepartmentRef.value = departments.ParentRef.value ```  ``` budgets.BudgetDetail.DepartmentRef.value = departments.Id ``` |

budgets table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **BudgetDetail**  ARRAY This is a nested data structure:   - AccountRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING - Amount: NUMBER - BudgetDate: DATE-TIME - ClassRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING - CustomerRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING - DepartmentRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **BudgetEntryType**  STRING |
| **BudgetType**  STRING |
| **EndDate**  DATE-TIME |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Name**  STRING |
| **StartDate**  DATE-TIME |
| **SyncToken**  STRING |
| **domain**  STRING |

### classes

The `classes` table contains info about the classes set up in your QuickBooks instance. **Note**: Both active and inactive classes are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/class)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/class#query-a-class "Opens in new tab: QuickBooks API method") |

classes table foreign keys

| Join classes with | on |
| --- | --- |
| [budgets](#budgets) | ``` classes.Id = budgets.BudgetDetail.ClassRef.value ```  ``` classes.ParentRef.value = budgets.BudgetDetail.ClassRef.value ``` |
| [credit\_memos](#credit-memos) | ``` classes.Id = credit_memos.ClassRef.value ```  ``` classes.ParentRef.value = credit_memos.ClassRef.value ``` |
| [estimates](#estimates) | ``` classes.Id = estimates.ClassRef.value ```  ``` classes.ParentRef.value = estimates.ClassRef.value ``` |
| [invoices](#invoices) | ``` classes.Id = invoices.ClassRef.value ```  ``` classes.ParentRef.value = invoices.ClassRef.value ```  ``` classes.Id = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` classes.ParentRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ``` |
| [items](#items) | ``` classes.Id = items.ClassRef.value ```  ``` classes.ParentRef.value = items.ClassRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` classes.Id = purchase_orders.ClassRef.value ```  ``` classes.ParentRef.value = purchase_orders.ClassRef.value ```  ``` classes.Id = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` classes.ParentRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ``` |
| [purchases](#purchases) | ``` classes.Id = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` classes.ParentRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` classes.Id = refund_receipts.ClassRef.value ```  ``` classes.ParentRef.value = refund_receipts.ClassRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` classes.Id = sales_receipts.ClassRef.value ```  ``` classes.ParentRef.value = sales_receipts.ClassRef.value ``` |
| [time\_activities](#time-activities) | ``` classes.Id = time_activities.ClassRef.value ```  ``` classes.ParentRef.value = time_activities.ClassRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` classes.Id = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` classes.ParentRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ``` |

classes table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **FullyQualifiedName**  STRING |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Name**  STRING |
| **ParentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SubClass**  BOOLEAN |
| **SyncToken**  STRING |
| **domain**  STRING |

### credit\_memos

The `credit_memos` table contains info about the credit memos in your QuickBooks instance. A credit memo is a transaction representing a refund or credit of payment for goods or services that have been sold.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/creditmemo)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/creditmemo#query-a-credit-memo "Opens in new tab: QuickBooks API method") |

credit\_memos table foreign keys

| Join credit\_memos with | on |
| --- | --- |
| [budgets](#budgets) | ``` credit_memos.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` credit_memos.CustomerRef.value = budgets.BudgetDetail.CustomerRef.value ``` |
| [classes](#classes) | ``` credit_memos.ClassRef.value = classes.Id ```  ``` credit_memos.ClassRef.value = classes.ParentRef.value ``` |
| [estimates](#estimates) | ``` credit_memos.ClassRef.value = estimates.ClassRef.value ```  ``` credit_memos.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` credit_memos.CustomerRef.value = estimates.CustomerRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.ItemRef.value = estimates.Line.SalesItemLineDetail.ItemRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` credit_memos.SalesTermRef.value = estimates.SalesTermRef.value ``` |
| [invoices](#invoices) | ``` credit_memos.ClassRef.value = invoices.ClassRef.value ```  ``` credit_memos.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` credit_memos.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` credit_memos.CustomerRef.value = invoices.CustomerRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.ItemRef.value = invoices.Line.SalesItemLineDetail.ItemRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` credit_memos.SalesTermRef.value = invoices.SalesTermRef.value ```  ``` credit_memos.Id = invoices.Id ``` |
| [items](#items) | ``` credit_memos.ClassRef.value = items.ClassRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.ItemRef.value = items.Id ```  ``` credit_memos.Line.SalesItemLineDetail.ItemRef.value = items.ParentRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` credit_memos.ClassRef.value = purchase_orders.ClassRef.value ```  ``` credit_memos.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` credit_memos.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` credit_memos.CustomerRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.ItemRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` credit_memos.SalesTermRef.value = purchase_orders.SalesTermRef.value ``` |
| [purchases](#purchases) | ``` credit_memos.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` credit_memos.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` credit_memos.CustomerRef.value = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.ItemRef.value = purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` credit_memos.Id = purchases.Id ``` |
| [refund\_receipts](#refund-receipts) | ``` credit_memos.ClassRef.value = refund_receipts.ClassRef.value ```  ``` credit_memos.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` credit_memos.CustomerRef.value = refund_receipts.CustomerRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.ItemRef.value = refund_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` credit_memos.ClassRef.value = sales_receipts.ClassRef.value ```  ``` credit_memos.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` credit_memos.CustomerRef.value = sales_receipts.CustomerRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.ItemRef.value = sales_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [time\_activities](#time-activities) | ``` credit_memos.ClassRef.value = time_activities.ClassRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.ItemRef.value = time_activities.ItemRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` credit_memos.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` credit_memos.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` credit_memos.CustomerRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [payments](#payments) | ``` credit_memos.Id = payments.Line.LinkedTxn.TxnId ```  ``` credit_memos.CurrencyRef.value = payments.CurrencyRef.value ```  ``` credit_memos.CustomerRef.value = payments.CustomerRef.value ``` |
| [accounts](#accounts) | ``` credit_memos.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` credit_memos.CurrencyRef.value = bill_payments.CurrencyRef.value ``` |
| [bills](#bills) | ``` credit_memos.CurrencyRef.value = bills.CurrencyRef.value ```  ``` credit_memos.CustomerRef.value = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.ItemRef.value = bills.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` credit_memos.SalesTermRef.value = bills.SalesTermRef.value ``` |
| [customers](#customers) | ``` credit_memos.CurrencyRef.value = customers.CurrencyRef.value ```  ``` credit_memos.CustomerRef.value = customers.Id ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ```  ``` credit_memos.SalesTermRef.value = customers.SalesTermRef.value ``` |
| [deposits](#deposits) | ``` credit_memos.CurrencyRef.value = deposits.CurrencyRef.value ``` |
| [journal\_entries](#journal-entries) | ``` credit_memos.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [transfers](#transfers) | ``` credit_memos.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [vendors](#vendors) | ``` credit_memos.CurrencyRef.value = vendors.CurrencyRef.value ``` |
| [terms](#terms) | ``` credit_memos.SalesTermRef.value = terms.Id ``` |

credit\_memos table schema

|  |
| --- |
| **ApplyTaxAfterDiscount**  BOOLEAN |
| **Balance**  NUMBER |
| **BillAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **BillEmail**  OBJECT This is a nested data structure:   - Address: STRING |
| **ClassRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CustomField**  ARRAY |
| **CustomerMemo**  OBJECT This is a nested data structure:   - value: STRING |
| **CustomerRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **EmailStatus**  STRING |
| **ExchangeRate**  NUMBER |
| **GlobalTaxCalculation**  STRING |
| **HomeBalance**  NUMBER |
| **HomeTotalAmt**  NUMBER |
| **Id**  STRING |
| **InvoiceRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Line**  ARRAY This is a nested data structure:   - Amount: NUMBER - Description: STRING - DescriptionLineDetail: OBJECT, which is also a nested data structure.   - ServiceDate: DATE-TIME   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - DetailType: STRING - DiscountLineDetail: OBJECT, which is also a nested data structure.   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountAccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountPercent: NUMBER   - PercentBased: BOOLEAN   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - GroupLineDetail: OBJECT, which is also a nested data structure.   - GroupItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Line: ARRAY, which is also a nested data structure.     - Amount: NUMBER     - Description: STRING     - DetailType: STRING     - Id: STRING     - LineNum: NUMBER     - SalesItemLineDetail: OBJECT, which is also a nested data structure.       - ClassRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - DiscountAmt: NUMBER       - DiscountRate: NUMBER       - ItemAccountRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - ItemRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - MarkupInfo: OBJECT, which is also a nested data structure.         - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING         - Percent: NUMBER         - PriceLevelRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING       - Qty: INTEGER       - ServiceDate: DATE-TIME       - TaxClassificationRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - TaxCodeRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - TaxInclusiveAmt: NUMBER       - UnitPrice: NUMBER   - Quantity: NUMBER - Id: STRING - LineNum: INTEGER - SalesItemLineDetail: OBJECT, which is also a nested data structure.   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountAmt: NUMBER   - DiscountRate: NUMBER   - ItemAccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - Qty: INTEGER   - ServiceDate: DATE-TIME   - TaxClassificationRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER   - UnitPrice: NUMBER - SubtotalLineDetail: OBJECT, which is also a nested data structure.   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PaymentMethodRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **PrintStatus**  STRING |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **RemainingCredit**  INTEGER |
| **SalesTermRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ShipAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **SyncToken**  STRING |
| **TaxExemptionRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnTaxDetail**  OBJECT This is a nested data structure:   - TaxLine: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - DetailType: STRING   - TaxLineDetail: OBJECT, which is also a nested data structure.     - NetAmountTaxable: NUMBER     - OverrideDeltaAmount: NUMBER     - PercentBased: BOOLEAN     - TaxInclusiveAmount: NUMBER     - TaxPercent: NUMBER     - TaxRateRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - TotalTax: NUMBER - TxnTaxCodeRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **domain**  STRING |
| **patternProperties**  OBJECT  Click to expand patternProperties |

### customer\_types

The `customer_types` table contains info about types of customers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/changedatacapture#the-changedatacapture-object)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/customertype#query-a-customertype "Opens in new tab: QuickBooks API method") |

customer\_types table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Name**  STRING |
| **SyncToken**  STRING |
| **domain**  STRING |
| **sparse**  STRING |

### customers

The `customers` table contains info about the consumers of your business’s goods and services. **Note**: Both active and inactive customers are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/customer)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/customer#query-a-customer "Opens in new tab: QuickBooks API method") |

customers table foreign keys

| Join customers with | on |
| --- | --- |
| [accounts](#accounts) | ``` customers.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` customers.CurrencyRef.value = bill_payments.CurrencyRef.value ``` |
| [bills](#bills) | ``` customers.CurrencyRef.value = bills.CurrencyRef.value ```  ``` customers.Id = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` customers.DefaultTaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` customers.DefaultTaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` customers.SalesTermRef.value = bills.SalesTermRef.value ``` |
| [credit\_memos](#credit-memos) | ``` customers.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` customers.Id = credit_memos.CustomerRef.value ```  ``` customers.DefaultTaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` customers.SalesTermRef.value = credit_memos.SalesTermRef.value ``` |
| [deposits](#deposits) | ``` customers.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` customers.PaymentMethodRef.value = deposits.Line.DepositLineDetail.PaymentMethodRef.value ``` |
| [estimates](#estimates) | ``` customers.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` customers.Id = estimates.CustomerRef.value ```  ``` customers.DefaultTaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` customers.DefaultTaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` customers.SalesTermRef.value = estimates.SalesTermRef.value ``` |
| [invoices](#invoices) | ``` customers.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` customers.Id = invoices.CustomerRef.value ```  ``` customers.DefaultTaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` customers.DefaultTaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` customers.SalesTermRef.value = invoices.SalesTermRef.value ``` |
| [journal\_entries](#journal-entries) | ``` customers.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` customers.DefaultTaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [payments](#payments) | ``` customers.CurrencyRef.value = payments.CurrencyRef.value ```  ``` customers.Id = payments.CustomerRef.value ```  ``` customers.PaymentMethodRef.value = payments.PaymentMethodRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` customers.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` customers.Id = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ```  ``` customers.DefaultTaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` customers.SalesTermRef.value = purchase_orders.SalesTermRef.value ``` |
| [purchases](#purchases) | ``` customers.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` customers.Id = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` customers.PaymentMethodRef.value = purchases.PaymentMethodRef.value ```  ``` customers.DefaultTaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` customers.DefaultTaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` customers.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` customers.Id = refund_receipts.CustomerRef.value ```  ``` customers.PaymentMethodRef.value = refund_receipts.PaymentMethodRef.value ```  ``` customers.DefaultTaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` customers.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` customers.Id = sales_receipts.CustomerRef.value ```  ``` customers.PaymentMethodRef.value = sales_receipts.PaymentMethodRef.value ```  ``` customers.DefaultTaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [transfers](#transfers) | ``` customers.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` customers.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` customers.Id = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` customers.DefaultTaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [vendors](#vendors) | ``` customers.CurrencyRef.value = vendors.CurrencyRef.value ``` |
| [budgets](#budgets) | ``` customers.Id = budgets.BudgetDetail.CustomerRef.value ``` |
| [payment\_methods](#payment-methods) | ``` customers.PaymentMethodRef.value = payment_methods.Id ``` |
| [items](#items) | ``` customers.DefaultTaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` customers.DefaultTaxCodeRef.value = items.SalesTaxCodeRef.value ``` |
| [terms](#terms) | ``` customers.SalesTermRef.value = terms.Id ``` |

customers table schema

|  |
| --- |
| **ARAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Active**  BOOLEAN |
| **AlternatePhone**  OBJECT This is a nested data structure:   - FreeFormNumber: STRING |
| **Balance**  NUMBER |
| **BalanceWithJobs**  NUMBER |
| **BillAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **BillWithParent**  BOOLEAN |
| **BusinessNumber**  STRING |
| **CompanyName**  STRING |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CustomerTypeRef**  OBJECT This is a nested data structure:   - value: STRING |
| **DefaultTaxCodeRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DisplayName**  STRING |
| **FamilyName**  STRING |
| **Fax**  OBJECT This is a nested data structure:   - FreeFormNumber: STRING |
| **FullyQualifiedName**  STRING |
| **GSTIN**  STRING |
| **GSTRegistrationType**  STRING |
| **GivenName**  STRING |
| **Id**  STRING |
| **IsProject**  BOOLEAN |
| **Job**  BOOLEAN |
| **Level**  INTEGER |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **MiddleName**  STRING |
| **Mobile**  OBJECT This is a nested data structure:   - FreeFormNumber: STRING |
| **Notes**  STRING |
| **OpenBalanceDate**  DATE-TIME |
| **ParentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **PaymentMethodRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **PreferredDeliveryMethod**  STRING |
| **PrimaryEmailAddr**  OBJECT This is a nested data structure:   - Address: STRING |
| **PrimaryPhone**  OBJECT This is a nested data structure:   - FreeFormNumber: STRING |
| **PrimaryTaxIdentifier**  STRING |
| **PrintOnCheckName**  STRING |
| **ResaleNum**  STRING |
| **SalesTermRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SecondaryTaxIdentifier**  STRING |
| **ShipAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **Source**  STRING |
| **Suffix**  STRING |
| **SyncToken**  STRING |
| **TaxExemptionReasonId**  INTEGER |
| **Taxable**  BOOLEAN |
| **Title**  STRING |
| **WebAddr**  OBJECT This is a nested data structure:   - URI: STRING |
| **domain**  STRING |

### deleted\_objects

The `deleted_objects` table contains info about objects deleted from QuickBooks.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/changedatacapture#the-changedatacapture-object)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/changedatacapture#get-a-list-of-changed-entities "Opens in new tab: QuickBooks API method") |

deleted\_objects table schema

|  |
| --- |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - LastUpdatedTime: DATE-TIME |
| **Type**  STRING |
| **domain**  STRING |

### departments

The `departments` table contains info about the departments in your QuickBooks instance. **Note**: Both active and inactive departments are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/department)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/department#query-a-department "Opens in new tab: QuickBooks API method") |

departments table foreign keys

| Join departments with | on |
| --- | --- |
| [bills](#bills) | ``` departments.ParentRef.value = bills.DepartmentRef.value ```  ``` departments.Id = bills.DepartmentRef.value ``` |
| [bill\_payments](#bill-payments) | ``` departments.ParentRef.value = bill_payments.DepartmentRef.value ```  ``` departments.Id = bill_payments.DepartmentRef.value ``` |
| [budgets](#budgets) | ``` departments.ParentRef.value = budgets.BudgetDetail.DepartmentRef.value ```  ``` departments.Id = budgets.BudgetDetail.DepartmentRef.value ``` |
| [deposits](#deposits) | ``` departments.ParentRef.value = deposits.DepartmentRef.value ```  ``` departments.Id = deposits.DepartmentRef.value ``` |
| [estimates](#estimates) | ``` departments.ParentRef.value = estimates.DepartmentRef.value ```  ``` departments.Id = estimates.DepartmentRef.value ``` |
| [invoices](#invoices) | ``` departments.ParentRef.value = invoices.DepartmentRef.value ```  ``` departments.Id = invoices.DepartmentRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` departments.ParentRef.value = purchase_orders.DepartmentRef.value ```  ``` departments.Id = purchase_orders.DepartmentRef.value ``` |
| [purchases](#purchases) | ``` departments.ParentRef.value = purchases.DepartmentRef.value ```  ``` departments.Id = purchases.DepartmentRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` departments.ParentRef.value = refund_receipts.DepartmentRef.value ```  ``` departments.Id = refund_receipts.DepartmentRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` departments.ParentRef.value = sales_receipts.DepartmentRef.value ```  ``` departments.Id = sales_receipts.DepartmentRef.value ``` |
| [time\_activities](#time-activities) | ``` departments.ParentRef.value = time_activities.DepartmentRef.value ```  ``` departments.Id = time_activities.DepartmentRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` departments.ParentRef.value = vendor_credits.DepartmentRef.value ```  ``` departments.Id = vendor_credits.DepartmentRef.value ``` |

departments table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **FullyQualifiedName**  STRING |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Name**  STRING |
| **ParentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SubDepartment**  BOOLEAN |
| **SyncToken**  STRING |
| **domain**  STRING |

### deposits

The `deposits` table contains info about deposits in your QuickBooks instance. These can be customer payments or new direct deposits.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/deposit)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/deposit#query-a-deposit "Opens in new tab: QuickBooks API method") |

deposits table foreign keys

| Join deposits with | on |
| --- | --- |
| [accounts](#accounts) | ``` deposits.CashBack.AccountRef.value = accounts.Id ```  ``` deposits.DepositToAccountRef.value = accounts.Id ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = accounts.Id ```  ``` deposits.CashBack.AccountRef.value = accounts.ParentRef.value ```  ``` deposits.DepositToAccountRef.value = accounts.ParentRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = accounts.ParentRef.value ```  ``` deposits.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` deposits.CashBack.AccountRef.value = bill_payments.APAccountRef.value ```  ``` deposits.DepositToAccountRef.value = bill_payments.APAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = bill_payments.APAccountRef.value ```  ``` deposits.CashBack.AccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` deposits.DepositToAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` deposits.CashBack.AccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` deposits.DepositToAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` deposits.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` deposits.DepartmentRef.value = bill_payments.DepartmentRef.value ```  ``` deposits.Line.LinkedTxn.TxnId = bill_payments.Line.LinkedTxn.TxnId ``` |
| [bills](#bills) | ``` deposits.CashBack.AccountRef.value = bills.APAccountRef.value ```  ``` deposits.DepositToAccountRef.value = bills.APAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = bills.APAccountRef.value ```  ``` deposits.CashBack.AccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` deposits.DepositToAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` deposits.CurrencyRef.value = bills.CurrencyRef.value ```  ``` deposits.DepartmentRef.value = bills.DepartmentRef.value ``` |
| [budgets](#budgets) | ``` deposits.CashBack.AccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` deposits.DepositToAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` deposits.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [invoices](#invoices) | ``` deposits.CashBack.AccountRef.value = invoices.DepositToAccountRef.value ```  ``` deposits.DepositToAccountRef.value = invoices.DepositToAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = invoices.DepositToAccountRef.value ```  ``` deposits.CashBack.AccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` deposits.DepositToAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` deposits.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` deposits.DepartmentRef.value = invoices.DepartmentRef.value ```  ``` deposits.Line.LinkedTxn.TxnId = invoices.LinkedTxn.TxnId ``` |
| [items](#items) | ``` deposits.CashBack.AccountRef.value = items.AssetAccountRef.value ```  ``` deposits.DepositToAccountRef.value = items.AssetAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = items.AssetAccountRef.value ```  ``` deposits.CashBack.AccountRef.value = items.ExpenseAccountRef.value ```  ``` deposits.DepositToAccountRef.value = items.ExpenseAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = items.ExpenseAccountRef.value ```  ``` deposits.CashBack.AccountRef.value = items.IncomeAccountRef.value ```  ``` deposits.DepositToAccountRef.value = items.IncomeAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = items.IncomeAccountRef.value ``` |
| [journal\_entries](#journal-entries) | ``` deposits.CashBack.AccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` deposits.DepositToAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` deposits.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` deposits.Line.LinkedTxn.TxnId = journal_entries.Id ``` |
| [payments](#payments) | ``` deposits.CashBack.AccountRef.value = payments.DepositToAccountRef.value ```  ``` deposits.DepositToAccountRef.value = payments.DepositToAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = payments.DepositToAccountRef.value ```  ``` deposits.CurrencyRef.value = payments.CurrencyRef.value ```  ``` deposits.Line.LinkedTxn.TxnId = payments.Id ```  ``` deposits.Line.DepositLineDetail.PaymentMethodRef.value = payments.PaymentMethodRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` deposits.CashBack.AccountRef.value = purchase_orders.APAccountRef.value ```  ``` deposits.DepositToAccountRef.value = purchase_orders.APAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = purchase_orders.APAccountRef.value ```  ``` deposits.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` deposits.DepartmentRef.value = purchase_orders.DepartmentRef.value ``` |
| [purchases](#purchases) | ``` deposits.CashBack.AccountRef.value = purchases.AccountRef.value ```  ``` deposits.DepositToAccountRef.value = purchases.AccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = purchases.AccountRef.value ```  ``` deposits.CashBack.AccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` deposits.DepositToAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` deposits.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` deposits.DepartmentRef.value = purchases.DepartmentRef.value ```  ``` deposits.Line.DepositLineDetail.PaymentMethodRef.value = purchases.PaymentMethodRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` deposits.CashBack.AccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` deposits.DepositToAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` deposits.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` deposits.DepartmentRef.value = refund_receipts.DepartmentRef.value ```  ``` deposits.Line.DepositLineDetail.PaymentMethodRef.value = refund_receipts.PaymentMethodRef.value ```  ``` deposits.Line.LinkedTxn.TxnId = refund_receipts.Id ``` |
| [sales\_receipts](#sales-receipts) | ``` deposits.CashBack.AccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` deposits.DepositToAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` deposits.CashBack.AccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` deposits.DepositToAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` deposits.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` deposits.DepartmentRef.value = sales_receipts.DepartmentRef.value ```  ``` deposits.Line.DepositLineDetail.PaymentMethodRef.value = sales_receipts.PaymentMethodRef.value ```  ``` deposits.Line.LinkedTxn.TxnId = sales_receipts.Id ``` |
| [transfers](#transfers) | ``` deposits.CashBack.AccountRef.value = transfers.FromAccountRef.value ```  ``` deposits.DepositToAccountRef.value = transfers.FromAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = transfers.FromAccountRef.value ```  ``` deposits.CashBack.AccountRef.value = transfers.ToAccountRef.value ```  ``` deposits.DepositToAccountRef.value = transfers.ToAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = transfers.ToAccountRef.value ```  ``` deposits.CurrencyRef.value = transfers.CurrencyRef.value ```  ``` deposits.Line.LinkedTxn.TxnId = transfers.Id ``` |
| [vendor\_credits](#vendor-credits) | ``` deposits.CashBack.AccountRef.value = vendor_credits.APAccountRef.value ```  ``` deposits.DepositToAccountRef.value = vendor_credits.APAccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = vendor_credits.APAccountRef.value ```  ``` deposits.CashBack.AccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` deposits.DepositToAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` deposits.Line.DepositLineDetail.AccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` deposits.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` deposits.DepartmentRef.value = vendor_credits.DepartmentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` deposits.CurrencyRef.value = credit_memos.CurrencyRef.value ``` |
| [customers](#customers) | ``` deposits.CurrencyRef.value = customers.CurrencyRef.value ```  ``` deposits.Line.DepositLineDetail.PaymentMethodRef.value = customers.PaymentMethodRef.value ``` |
| [estimates](#estimates) | ``` deposits.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` deposits.DepartmentRef.value = estimates.DepartmentRef.value ``` |
| [vendors](#vendors) | ``` deposits.CurrencyRef.value = vendors.CurrencyRef.value ``` |
| [departments](#departments) | ``` deposits.DepartmentRef.value = departments.ParentRef.value ```  ``` deposits.DepartmentRef.value = departments.Id ``` |
| [time\_activities](#time-activities) | ``` deposits.DepartmentRef.value = time_activities.DepartmentRef.value ``` |
| [payment\_methods](#payment-methods) | ``` deposits.Line.DepositLineDetail.PaymentMethodRef.value = payment_methods.Id ``` |

deposits table schema

|  |
| --- |
| **CashBack**  OBJECT This is a nested data structure:   - AccountRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING - Amount: NUMBER - Memo: STRING |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepositToAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ExchangeRate**  NUMBER |
| **GlobalTaxCalculation**  STRING |
| **HomeTotalAmt**  NUMBER |
| **Id**  STRING |
| **Line**  ARRAY This is a nested data structure:   - Amount: NUMBER - CustomField: OBJECT, which is also a nested data structure.   - DefinitionId: STRING   - Name: STRING   - StringValue: STRING   - Type: STRING - DepositLineDetail: OBJECT, which is also a nested data structure.   - AccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - CheckNum: STRING   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Entity: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - PaymentMethodRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxApplicableOn: STRING   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TxnType: STRING - Description: STRING - DetailType: STRING - Id: STRING - LineNum: INTEGER - LinkedTxn: ARRAY, which is also a nested data structure.   - TxnId: STRING   - TxnLineId: STRING   - TxnType: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SyncToken**  STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnSource**  STRING |
| **TxnTaxDetail**  OBJECT This is a nested data structure:   - TaxLine: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - DetailType: STRING   - TaxLineDetail: OBJECT, which is also a nested data structure.     - NetAmountTaxable: NUMBER     - OverrideDeltaAmount: NUMBER     - PercentBased: BOOLEAN     - TaxInclusiveAmount: NUMBER     - TaxPercent: NUMBER     - TaxRateRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - TotalTax: NUMBER - TxnTaxCodeRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **domain**  STRING |

### employees

The `employees` table contains info about the people working for your company. **Note**: Both active and inactive employees are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/employee)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/employee#query-an-employee "Opens in new tab: QuickBooks API method") |

employees table foreign keys

| Join employees with | on |
| --- | --- |
| [purchases](#purchases) | ``` employees.Id = purchases.EntityRef.value ``` |
| [time\_activities](#time-activities) | ``` employees.Id = time_activities.EmployeeRef.value ``` |

employees table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **BillRate**  NUMBER |
| **BillableTime**  BOOLEAN |
| **BirthDate**  DATE-TIME |
| **CostRate**  NUMBER |
| **DisplayName**  STRING |
| **EmployeeNumber**  STRING |
| **FamilyName**  STRING |
| **Gender**  STRING |
| **GivenName**  STRING |
| **HiredDate**  DATE-TIME |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **MiddleName**  STRING |
| **Mobile**  OBJECT This is a nested data structure:   - FreeFormNumber: STRING |
| **Organization**  BOOLEAN |
| **PrimaryAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **PrimaryEmailAddr**  OBJECT This is a nested data structure:   - Address: STRING |
| **PrimaryPhone**  OBJECT This is a nested data structure:   - FreeFormNumber: STRING |
| **PrintOnCheckName**  STRING |
| **ReleasedDate**  DATE-TIME |
| **SSN**  STRING |
| **Suffix**  STRING |
| **SyncToken**  STRING |
| **Title**  STRING |
| **V4IDPseudonym**  STRING |
| **domain**  STRING |

### estimates

The `estimates` table contains info about the estimates in your QuickBooks instance. An estimate is a financial proposal from a business to a [customer](#customers) for goods or services.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/estimate)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/estimate#read-an-estimate "Opens in new tab: QuickBooks API method") |

estimates table foreign keys

| Join estimates with | on |
| --- | --- |
| [budgets](#budgets) | ``` estimates.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` estimates.CustomerRef.value = budgets.BudgetDetail.CustomerRef.value ```  ``` estimates.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [classes](#classes) | ``` estimates.ClassRef.value = classes.Id ```  ``` estimates.ClassRef.value = classes.ParentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` estimates.ClassRef.value = credit_memos.ClassRef.value ```  ``` estimates.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` estimates.CustomerRef.value = credit_memos.CustomerRef.value ```  ``` estimates.Line.SalesItemLineDetail.ItemRef.value = credit_memos.Line.SalesItemLineDetail.ItemRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` estimates.SalesTermRef.value = credit_memos.SalesTermRef.value ``` |
| [invoices](#invoices) | ``` estimates.ClassRef.value = invoices.ClassRef.value ```  ``` estimates.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` estimates.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` estimates.CustomerRef.value = invoices.CustomerRef.value ```  ``` estimates.DepartmentRef.value = invoices.DepartmentRef.value ```  ``` estimates.Id = invoices.LinkedTxn.TxnId ```  ``` estimates.LinkedTxn.TxnId = invoices.Id ```  ``` estimates.Line.SalesItemLineDetail.ItemRef.value = invoices.Line.SalesItemLineDetail.ItemRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value = invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ```  ``` estimates.SalesTermRef.value = invoices.SalesTermRef.value ``` |
| [items](#items) | ``` estimates.ClassRef.value = items.ClassRef.value ```  ``` estimates.Line.SalesItemLineDetail.ItemRef.value = items.Id ```  ``` estimates.Line.SalesItemLineDetail.ItemRef.value = items.ParentRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = items.SalesTaxCodeRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` estimates.ClassRef.value = purchase_orders.ClassRef.value ```  ``` estimates.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` estimates.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` estimates.CustomerRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ```  ``` estimates.DepartmentRef.value = purchase_orders.DepartmentRef.value ```  ``` estimates.Line.SalesItemLineDetail.ItemRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.SalesTermRef.value = purchase_orders.SalesTermRef.value ``` |
| [purchases](#purchases) | ``` estimates.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` estimates.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` estimates.CustomerRef.value = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` estimates.DepartmentRef.value = purchases.DepartmentRef.value ```  ``` estimates.Line.SalesItemLineDetail.ItemRef.value = purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.Id = purchases.Id ``` |
| [refund\_receipts](#refund-receipts) | ``` estimates.ClassRef.value = refund_receipts.ClassRef.value ```  ``` estimates.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` estimates.CustomerRef.value = refund_receipts.CustomerRef.value ```  ``` estimates.DepartmentRef.value = refund_receipts.DepartmentRef.value ```  ``` estimates.Line.SalesItemLineDetail.ItemRef.value = refund_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` estimates.ClassRef.value = sales_receipts.ClassRef.value ```  ``` estimates.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` estimates.CustomerRef.value = sales_receipts.CustomerRef.value ```  ``` estimates.DepartmentRef.value = sales_receipts.DepartmentRef.value ```  ``` estimates.Line.SalesItemLineDetail.ItemRef.value = sales_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [time\_activities](#time-activities) | ``` estimates.ClassRef.value = time_activities.ClassRef.value ```  ``` estimates.DepartmentRef.value = time_activities.DepartmentRef.value ```  ``` estimates.Line.SalesItemLineDetail.ItemRef.value = time_activities.ItemRef.value ```  ``` estimates.Id = time_activities.Id ``` |
| [vendor\_credits](#vendor-credits) | ``` estimates.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` estimates.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` estimates.CustomerRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` estimates.DepartmentRef.value = vendor_credits.DepartmentRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [accounts](#accounts) | ``` estimates.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` estimates.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` estimates.DepartmentRef.value = bill_payments.DepartmentRef.value ``` |
| [bills](#bills) | ``` estimates.CurrencyRef.value = bills.CurrencyRef.value ```  ``` estimates.CustomerRef.value = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` estimates.DepartmentRef.value = bills.DepartmentRef.value ```  ``` estimates.Line.SalesItemLineDetail.ItemRef.value = bills.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` estimates.SalesTermRef.value = bills.SalesTermRef.value ``` |
| [customers](#customers) | ``` estimates.CurrencyRef.value = customers.CurrencyRef.value ```  ``` estimates.CustomerRef.value = customers.Id ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = customers.DefaultTaxCodeRef.value ```  ``` estimates.SalesTermRef.value = customers.SalesTermRef.value ``` |
| [deposits](#deposits) | ``` estimates.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` estimates.DepartmentRef.value = deposits.DepartmentRef.value ``` |
| [journal\_entries](#journal-entries) | ``` estimates.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` estimates.Line.SalesItemLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TxnTaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value = journal_entries.TaxRateRef.value ```  ``` estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value = journal_entries.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ``` |
| [payments](#payments) | ``` estimates.CurrencyRef.value = payments.CurrencyRef.value ```  ``` estimates.CustomerRef.value = payments.CustomerRef.value ```  ``` estimates.LinkedTxn.TxnId = payments.Line.LinkedTxn.TxnId ```  ``` estimates.Id = payments.Id ``` |
| [transfers](#transfers) | ``` estimates.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [vendors](#vendors) | ``` estimates.CurrencyRef.value = vendors.CurrencyRef.value ``` |
| [departments](#departments) | ``` estimates.DepartmentRef.value = departments.ParentRef.value ```  ``` estimates.DepartmentRef.value = departments.Id ``` |
| [tax\_codes](#tax-codes) | ``` estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value = tax_codes.PurchaseTaxRateList.TaxRateDetail.TaxRateRef.value ```  ``` estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value = tax_codes.SalesTaxRateList.TaxRateDetail.TaxRateRef.value ``` |
| [tax\_rates](#tax-rates) | ``` estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value = tax_rates.Id ``` |
| [terms](#terms) | ``` estimates.SalesTermRef.value = terms.Id ``` |

estimates table schema

|  |
| --- |
| **AcceptedBy**  STRING |
| **AcceptedDate**  DATE-TIME |
| **ApplyTaxAfterDiscount**  BOOLEAN |
| **BillAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **BillEmail**  OBJECT This is a nested data structure:   - Address: STRING |
| **ClassRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CustomField**  ARRAY |
| **CustomerMemo**  OBJECT This is a nested data structure:   - value: STRING |
| **CustomerRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DeliveryInfo**  OBJECT This is a nested data structure:   - DeliveryTime: DATE-TIME - DeliveryType: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **DueDate**  DATE-TIME |
| **EmailStatus**  STRING |
| **ExchangeRate**  NUMBER |
| **ExpirationDate**  DATE-TIME |
| **FreeFormAddress**  BOOLEAN |
| **GlobalTaxCalculation**  STRING |
| **HomeTotalAmt**  NUMBER |
| **Id**  STRING |
| **Line**  ARRAY This is a nested data structure:   - Amount: NUMBER - Description: STRING - DescriptionLineDetail: OBJECT, which is also a nested data structure.   - ServiceDate: DATE-TIME   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - DetailType: STRING - DiscountLineDetail: OBJECT, which is also a nested data structure.   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountAccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountPercent: NUMBER   - PercentBased: BOOLEAN   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - GroupLineDetail: OBJECT, which is also a nested data structure.   - GroupItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Line: ARRAY, which is also a nested data structure.     - Amount: NUMBER     - Description: STRING     - DetailType: STRING     - Id: STRING     - LineNum: NUMBER     - SalesItemLineDetail: OBJECT, which is also a nested data structure.       - ClassRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - DiscountAmt: NUMBER       - DiscountRate: NUMBER       - ItemAccountRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - ItemRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - MarkupInfo: OBJECT, which is also a nested data structure.         - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING         - Percent: NUMBER         - PriceLevelRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING       - Qty: INTEGER       - ServiceDate: DATE-TIME       - TaxClassificationRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - TaxCodeRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - TaxInclusiveAmt: NUMBER       - UnitPrice: NUMBER   - Quantity: NUMBER - Id: STRING - LineNum: INTEGER - SalesItemLineDetail: OBJECT, which is also a nested data structure.   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountAmt: NUMBER   - DiscountRate: NUMBER   - ItemAccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - Qty: INTEGER   - ServiceDate: DATE-TIME   - TaxClassificationRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER   - UnitPrice: NUMBER - SubtotalLineDetail: OBJECT, which is also a nested data structure.   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING |
| **LinkedTxn**  ARRAY This is a nested data structure:   - TxnId: STRING - TxnLineId: STRING - TxnType: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PrintStatus**  STRING |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SalesTermRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ShipAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **ShipDate**  DATE-TIME |
| **ShipFromAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **ShipMethodRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SyncToken**  STRING |
| **TaxExemptionRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnStatus**  STRING |
| **TxnTaxDetail**  OBJECT This is a nested data structure:   - TaxLine: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - DetailType: STRING   - TaxLineDetail: OBJECT, which is also a nested data structure.     - TaxLine: ARRAY, which is also a nested data structure.       - Amount: NUMBER       - DetailType: STRING       - TaxLineDetail: OBJECT, which is also a nested data structure.         - NetAmountTaxable: NUMBER         - OverrideDeltaAmount: NUMBER         - PercentBased: BOOLEAN         - TaxInclusiveAmount: NUMBER         - TaxPercent: NUMBER         - TaxRateRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING     - TotalTax: NUMBER     - TxnTaxCodeRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - TotalTax: NUMBER - TxnTaxCodeRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **domain**  STRING |
| **patternProperties**  OBJECT  Click to expand patternProperties |

### invoices

The `invoices` table contains info about the invoices in your QuickBooks account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/invoice)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/invoice#query-an-invoice "Opens in new tab: QuickBooks API method") |

invoices table foreign keys

| Join invoices with | on |
| --- | --- |
| [accounts](#accounts) | ``` invoices.DepositToAccountRef.value = accounts.Id ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = accounts.Id ```  ``` invoices.DepositToAccountRef.value = accounts.ParentRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = accounts.ParentRef.value ```  ``` invoices.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` invoices.DepositToAccountRef.value = bill_payments.APAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = bill_payments.APAccountRef.value ```  ``` invoices.DepositToAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` invoices.DepositToAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` invoices.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` invoices.DepartmentRef.value = bill_payments.DepartmentRef.value ``` |
| [bills](#bills) | ``` invoices.DepositToAccountRef.value = bills.APAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = bills.APAccountRef.value ```  ``` invoices.DepositToAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` invoices.CurrencyRef.value = bills.CurrencyRef.value ```  ``` invoices.CustomerRef.value = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` invoices.DepartmentRef.value = bills.DepartmentRef.value ```  ``` invoices.Line.SalesItemLineDetail.ItemRef.value = bills.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.SalesTermRef.value = bills.SalesTermRef.value ``` |
| [budgets](#budgets) | ``` invoices.DepositToAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` invoices.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` invoices.CustomerRef.value = budgets.BudgetDetail.CustomerRef.value ```  ``` invoices.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [deposits](#deposits) | ``` invoices.DepositToAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` invoices.DepositToAccountRef.value = deposits.DepositToAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = deposits.DepositToAccountRef.value ```  ``` invoices.DepositToAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` invoices.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` invoices.DepartmentRef.value = deposits.DepartmentRef.value ```  ``` invoices.LinkedTxn.TxnId = deposits.Line.LinkedTxn.TxnId ``` |
| [items](#items) | ``` invoices.DepositToAccountRef.value = items.AssetAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = items.AssetAccountRef.value ```  ``` invoices.DepositToAccountRef.value = items.ExpenseAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = items.ExpenseAccountRef.value ```  ``` invoices.DepositToAccountRef.value = items.IncomeAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = items.IncomeAccountRef.value ```  ``` invoices.ClassRef.value = items.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = items.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ItemRef.value = items.Id ```  ``` invoices.Line.SalesItemLineDetail.ItemRef.value = items.ParentRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = items.SalesTaxCodeRef.value ``` |
| [journal\_entries](#journal-entries) | ``` invoices.DepositToAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` invoices.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = journal_entries.TaxRateRef.value ```  ``` invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = journal_entries.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ``` |
| [payments](#payments) | ``` invoices.DepositToAccountRef.value = payments.DepositToAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = payments.DepositToAccountRef.value ```  ``` invoices.CurrencyRef.value = payments.CurrencyRef.value ```  ``` invoices.CustomerRef.value = payments.CustomerRef.value ```  ``` invoices.Id = payments.Line.LinkedTxn.TxnId ```  ``` invoices.LinkedTxn.TxnId = payments.Id ```  ``` invoices.LinkedTxn.TxnId = payments.Line.LinkedTxn.TxnId ``` |
| [purchase\_orders](#purchase-orders) | ``` invoices.DepositToAccountRef.value = purchase_orders.APAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = purchase_orders.APAccountRef.value ```  ``` invoices.ClassRef.value = purchase_orders.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = purchase_orders.ClassRef.value ```  ``` invoices.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` invoices.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` invoices.CustomerRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ```  ``` invoices.DepartmentRef.value = purchase_orders.DepartmentRef.value ```  ``` invoices.Line.SalesItemLineDetail.ItemRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.SalesTermRef.value = purchase_orders.SalesTermRef.value ``` |
| [purchases](#purchases) | ``` invoices.DepositToAccountRef.value = purchases.AccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = purchases.AccountRef.value ```  ``` invoices.DepositToAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` invoices.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` invoices.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` invoices.CustomerRef.value = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` invoices.DepartmentRef.value = purchases.DepartmentRef.value ```  ``` invoices.Line.SalesItemLineDetail.ItemRef.value = purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` invoices.LinkedTxn.TxnId = purchases.Id ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.Id = purchases.Id ``` |
| [refund\_receipts](#refund-receipts) | ``` invoices.DepositToAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` invoices.ClassRef.value = refund_receipts.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = refund_receipts.ClassRef.value ```  ``` invoices.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` invoices.CustomerRef.value = refund_receipts.CustomerRef.value ```  ``` invoices.DepartmentRef.value = refund_receipts.DepartmentRef.value ```  ``` invoices.Line.SalesItemLineDetail.ItemRef.value = refund_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` invoices.DepositToAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` invoices.DepositToAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` invoices.ClassRef.value = sales_receipts.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = sales_receipts.ClassRef.value ```  ``` invoices.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` invoices.CustomerRef.value = sales_receipts.CustomerRef.value ```  ``` invoices.DepartmentRef.value = sales_receipts.DepartmentRef.value ```  ``` invoices.Line.SalesItemLineDetail.ItemRef.value = sales_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [transfers](#transfers) | ``` invoices.DepositToAccountRef.value = transfers.FromAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = transfers.FromAccountRef.value ```  ``` invoices.DepositToAccountRef.value = transfers.ToAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = transfers.ToAccountRef.value ```  ``` invoices.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` invoices.DepositToAccountRef.value = vendor_credits.APAccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = vendor_credits.APAccountRef.value ```  ``` invoices.DepositToAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` invoices.Line.DiscountLineDetail.DiscountAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` invoices.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` invoices.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` invoices.CustomerRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` invoices.DepartmentRef.value = vendor_credits.DepartmentRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [classes](#classes) | ``` invoices.ClassRef.value = classes.Id ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = classes.Id ```  ``` invoices.ClassRef.value = classes.ParentRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = classes.ParentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` invoices.ClassRef.value = credit_memos.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = credit_memos.ClassRef.value ```  ``` invoices.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` invoices.CustomerRef.value = credit_memos.CustomerRef.value ```  ``` invoices.Line.SalesItemLineDetail.ItemRef.value = credit_memos.Line.SalesItemLineDetail.ItemRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` invoices.SalesTermRef.value = credit_memos.SalesTermRef.value ```  ``` invoices.Id = credit_memos.Id ``` |
| [estimates](#estimates) | ``` invoices.ClassRef.value = estimates.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = estimates.ClassRef.value ```  ``` invoices.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` invoices.CustomerRef.value = estimates.CustomerRef.value ```  ``` invoices.DepartmentRef.value = estimates.DepartmentRef.value ```  ``` invoices.LinkedTxn.TxnId = estimates.Id ```  ``` invoices.Id = estimates.LinkedTxn.TxnId ```  ``` invoices.Line.SalesItemLineDetail.ItemRef.value = estimates.Line.SalesItemLineDetail.ItemRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value ```  ``` invoices.SalesTermRef.value = estimates.SalesTermRef.value ``` |
| [time\_activities](#time-activities) | ``` invoices.ClassRef.value = time_activities.ClassRef.value ```  ``` invoices.Line.SalesItemLineDetail.ClassRef.value = time_activities.ClassRef.value ```  ``` invoices.DepartmentRef.value = time_activities.DepartmentRef.value ```  ``` invoices.Line.SalesItemLineDetail.ItemRef.value = time_activities.ItemRef.value ```  ``` invoices.LinkedTxn.TxnId = time_activities.Id ``` |
| [customers](#customers) | ``` invoices.CurrencyRef.value = customers.CurrencyRef.value ```  ``` invoices.CustomerRef.value = customers.Id ```  ``` invoices.Line.SalesItemLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ```  ``` invoices.TxnTaxDetail.TxnTaxCodeRef.value = customers.DefaultTaxCodeRef.value ```  ``` invoices.SalesTermRef.value = customers.SalesTermRef.value ``` |
| [vendors](#vendors) | ``` invoices.CurrencyRef.value = vendors.CurrencyRef.value ``` |
| [departments](#departments) | ``` invoices.DepartmentRef.value = departments.ParentRef.value ```  ``` invoices.DepartmentRef.value = departments.Id ``` |
| [tax\_codes](#tax-codes) | ``` invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = tax_codes.PurchaseTaxRateList.TaxRateDetail.TaxRateRef.value ```  ``` invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = tax_codes.SalesTaxRateList.TaxRateDetail.TaxRateRef.value ``` |
| [tax\_rates](#tax-rates) | ``` invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = tax_rates.Id ``` |
| [terms](#terms) | ``` invoices.SalesTermRef.value = terms.Id ``` |

invoices table schema

|  |
| --- |
| **AllowIPNPayment**  BOOLEAN |
| **AllowOnlineACHPayment**  BOOLEAN |
| **AllowOnlineCreditCardPayment**  BOOLEAN |
| **AllowOnlinePayment**  BOOLEAN |
| **ApplyTaxAfterDiscount**  BOOLEAN |
| **Balance**  NUMBER |
| **BillAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **BillEmail**  OBJECT This is a nested data structure:   - Address: STRING |
| **BillEmailBcc**  OBJECT This is a nested data structure:   - Address: STRING |
| **BillEmailCc**  OBJECT This is a nested data structure:   - Address: STRING |
| **ClassRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CustomField**  ARRAY |
| **CustomerMemo**  OBJECT This is a nested data structure:   - value: STRING |
| **CustomerRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DeliveryInfo**  OBJECT This is a nested data structure:   - DeliveryTime: DATE-TIME - DeliveryType: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Deposit**  NUMBER |
| **DepositToAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **DueDate**  DATE-TIME |
| **EmailStatus**  STRING |
| **ExchangeRate**  NUMBER |
| **FreeFormAddress**  BOOLEAN |
| **GlobalTaxCalculation**  STRING |
| **HomeBalance**  NUMBER |
| **HomeTotalAmt**  NUMBER |
| **Id**  STRING |
| **InvoiceLink**  STRING |
| **Line**  ARRAY This is a nested data structure:   - Amount: NUMBER - Description: STRING - DescriptionLineDetail: OBJECT, which is also a nested data structure.   - ServiceDate: DATE-TIME   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - DetailType: STRING - DiscountLineDetail: OBJECT, which is also a nested data structure.   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountAccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountPercent: NUMBER   - PercentBased: BOOLEAN   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - GroupLineDetail: OBJECT, which is also a nested data structure.   - GroupItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Line: ARRAY, which is also a nested data structure.     - Amount: NUMBER     - Description: STRING     - DetailType: STRING     - Id: STRING     - LineNum: NUMBER     - SalesItemLineDetail: OBJECT, which is also a nested data structure.       - ClassRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - DiscountAmt: NUMBER       - DiscountRate: NUMBER       - ItemAccountRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - ItemRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - MarkupInfo: OBJECT, which is also a nested data structure.         - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING         - Percent: NUMBER         - PriceLevelRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING       - Qty: INTEGER       - ServiceDate: DATE-TIME       - TaxClassificationRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - TaxCodeRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - TaxInclusiveAmt: NUMBER       - UnitPrice: NUMBER   - Quantity: NUMBER - Id: STRING - LineNum: INTEGER - LinkedTxn: ARRAY, which is also a nested data structure.   - TxnId: STRING   - TxnLineId: STRING   - TxnType: STRING - SalesItemLineDetail: OBJECT, which is also a nested data structure.   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountAmt: NUMBER   - DiscountRate: NUMBER   - ItemAccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - Qty: INTEGER   - ServiceDate: DATE-TIME   - TaxClassificationRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER   - UnitPrice: NUMBER - SubtotalLineDetail: OBJECT, which is also a nested data structure.   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING |
| **LinkedTxn**  ARRAY This is a nested data structure:   - TxnId: STRING - TxnLineId: STRING - TxnType: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PrintStatus**  STRING |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SalesTermRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ShipAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **ShipDate**  DATE-TIME |
| **ShipFromAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **ShipMethodRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SyncToken**  STRING |
| **TaxExemptionRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **TotalAmt**  NUMBER |
| **TrackingNum**  STRING |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnSource**  STRING |
| **TxnTaxDetail**  OBJECT This is a nested data structure:   - TaxLine: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - DetailType: STRING   - TaxLineDetail: OBJECT, which is also a nested data structure.     - NetAmountTaxable: NUMBER     - OverrideDeltaAmount: NUMBER     - PercentBased: BOOLEAN     - TaxInclusiveAmount: NUMBER     - TaxPercent: NUMBER     - TaxRateRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - TotalTax: NUMBER - TxnTaxCodeRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **domain**  STRING |
| **patternProperties**  OBJECT  Click to expand patternProperties |

### items

The `items` table contains info about the items your company buys, sells, or re-sells. This includes all item types in QuickBooks, such as `Inventory`, `Group`, `Service` and `Noninventory`.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/item)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/item/#query-an-item "Opens in new tab: QuickBooks API method") |

items table foreign keys

| Join items with | on |
| --- | --- |
| [accounts](#accounts) | ``` items.AssetAccountRef.value = accounts.Id ```  ``` items.ExpenseAccountRef.value = accounts.Id ```  ``` items.IncomeAccountRef.value = accounts.Id ```  ``` items.AssetAccountRef.value = accounts.ParentRef.value ```  ``` items.ExpenseAccountRef.value = accounts.ParentRef.value ```  ``` items.IncomeAccountRef.value = accounts.ParentRef.value ``` |
| [bill\_payments](#bill-payments) | ``` items.AssetAccountRef.value = bill_payments.APAccountRef.value ```  ``` items.ExpenseAccountRef.value = bill_payments.APAccountRef.value ```  ``` items.IncomeAccountRef.value = bill_payments.APAccountRef.value ```  ``` items.AssetAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` items.ExpenseAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` items.IncomeAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` items.AssetAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` items.ExpenseAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` items.IncomeAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` items.PrefVendorRef.value = bill_payments.VendorRef.value ``` |
| [bills](#bills) | ``` items.AssetAccountRef.value = bills.APAccountRef.value ```  ``` items.ExpenseAccountRef.value = bills.APAccountRef.value ```  ``` items.IncomeAccountRef.value = bills.APAccountRef.value ```  ``` items.AssetAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` items.ExpenseAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` items.IncomeAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` items.Id = bills.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` items.ParentRef.value = bills.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` items.PurchaseTaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.PurchaseTaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.PrefVendorRef.value = bills.VendorRef.value ``` |
| [budgets](#budgets) | ``` items.AssetAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` items.ExpenseAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` items.IncomeAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` items.ClassRef.value = budgets.BudgetDetail.ClassRef.value ``` |
| [deposits](#deposits) | ``` items.AssetAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` items.ExpenseAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` items.IncomeAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` items.AssetAccountRef.value = deposits.DepositToAccountRef.value ```  ``` items.ExpenseAccountRef.value = deposits.DepositToAccountRef.value ```  ``` items.IncomeAccountRef.value = deposits.DepositToAccountRef.value ```  ``` items.AssetAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` items.ExpenseAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` items.IncomeAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ``` |
| [invoices](#invoices) | ``` items.AssetAccountRef.value = invoices.DepositToAccountRef.value ```  ``` items.ExpenseAccountRef.value = invoices.DepositToAccountRef.value ```  ``` items.IncomeAccountRef.value = invoices.DepositToAccountRef.value ```  ``` items.AssetAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` items.ExpenseAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` items.IncomeAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` items.ClassRef.value = invoices.ClassRef.value ```  ``` items.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` items.Id = invoices.Line.SalesItemLineDetail.ItemRef.value ```  ``` items.ParentRef.value = invoices.Line.SalesItemLineDetail.ItemRef.value ```  ``` items.PurchaseTaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` items.PurchaseTaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [journal\_entries](#journal-entries) | ``` items.AssetAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` items.ExpenseAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` items.IncomeAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` items.PurchaseTaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [payments](#payments) | ``` items.AssetAccountRef.value = payments.DepositToAccountRef.value ```  ``` items.ExpenseAccountRef.value = payments.DepositToAccountRef.value ```  ``` items.IncomeAccountRef.value = payments.DepositToAccountRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` items.AssetAccountRef.value = purchase_orders.APAccountRef.value ```  ``` items.ExpenseAccountRef.value = purchase_orders.APAccountRef.value ```  ``` items.IncomeAccountRef.value = purchase_orders.APAccountRef.value ```  ``` items.ClassRef.value = purchase_orders.ClassRef.value ```  ``` items.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` items.Id = purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` items.ParentRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` items.PurchaseTaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.PrefVendorRef.value = purchase_orders.VendorRef.value ``` |
| [purchases](#purchases) | ``` items.AssetAccountRef.value = purchases.AccountRef.value ```  ``` items.ExpenseAccountRef.value = purchases.AccountRef.value ```  ``` items.IncomeAccountRef.value = purchases.AccountRef.value ```  ``` items.AssetAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` items.ExpenseAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` items.IncomeAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` items.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` items.Id = purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` items.ParentRef.value = purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` items.PurchaseTaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.PurchaseTaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` items.AssetAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` items.ExpenseAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` items.IncomeAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` items.ClassRef.value = refund_receipts.ClassRef.value ```  ``` items.Id = refund_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` items.ParentRef.value = refund_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` items.PurchaseTaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` items.AssetAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` items.ExpenseAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` items.IncomeAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` items.AssetAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` items.ExpenseAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` items.IncomeAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` items.ClassRef.value = sales_receipts.ClassRef.value ```  ``` items.Id = sales_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` items.ParentRef.value = sales_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` items.PurchaseTaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [transfers](#transfers) | ``` items.AssetAccountRef.value = transfers.FromAccountRef.value ```  ``` items.ExpenseAccountRef.value = transfers.FromAccountRef.value ```  ``` items.IncomeAccountRef.value = transfers.FromAccountRef.value ```  ``` items.AssetAccountRef.value = transfers.ToAccountRef.value ```  ``` items.ExpenseAccountRef.value = transfers.ToAccountRef.value ```  ``` items.IncomeAccountRef.value = transfers.ToAccountRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` items.AssetAccountRef.value = vendor_credits.APAccountRef.value ```  ``` items.ExpenseAccountRef.value = vendor_credits.APAccountRef.value ```  ``` items.IncomeAccountRef.value = vendor_credits.APAccountRef.value ```  ``` items.AssetAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` items.ExpenseAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` items.IncomeAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` items.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` items.PurchaseTaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` items.PrefVendorRef.value = vendor_credits.VendorRef.value ``` |
| [classes](#classes) | ``` items.ClassRef.value = classes.Id ```  ``` items.ClassRef.value = classes.ParentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` items.ClassRef.value = credit_memos.ClassRef.value ```  ``` items.Id = credit_memos.Line.SalesItemLineDetail.ItemRef.value ```  ``` items.ParentRef.value = credit_memos.Line.SalesItemLineDetail.ItemRef.value ```  ``` items.PurchaseTaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [estimates](#estimates) | ``` items.ClassRef.value = estimates.ClassRef.value ```  ``` items.Id = estimates.Line.SalesItemLineDetail.ItemRef.value ```  ``` items.ParentRef.value = estimates.Line.SalesItemLineDetail.ItemRef.value ```  ``` items.PurchaseTaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` items.PurchaseTaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [time\_activities](#time-activities) | ``` items.ClassRef.value = time_activities.ClassRef.value ```  ``` items.Id = time_activities.ItemRef.value ```  ``` items.ParentRef.value = time_activities.ItemRef.value ```  ``` items.PrefVendorRef.value = time_activities.VendorRef.value ``` |
| [customers](#customers) | ``` items.PurchaseTaxCodeRef.value = customers.DefaultTaxCodeRef.value ```  ``` items.SalesTaxCodeRef.value = customers.DefaultTaxCodeRef.value ``` |
| [vendors](#vendors) | ``` items.PrefVendorRef.value = vendors.Id ``` |

items table schema

|  |
| --- |
| **AbatementRate**  NUMBER |
| **Active**  BOOLEAN |
| **AssetAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ClassRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Description**  STRING |
| **ExpenseAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **FullyQualifiedName**  STRING |
| **Id**  STRING |
| **IncomeAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **InvStartDate**  DATE-TIME |
| **ItemCategoryType**  STRING |
| **Level**  INTEGER |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Name**  STRING |
| **ParentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **PrefVendorRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **PurchaseCost**  INTEGER, NUMBER |
| **PurchaseDesc**  STRING |
| **PurchaseTaxCodeRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **PurchaseTaxIncluded**  BOOLEAN |
| **QtyOnHand**  INTEGER |
| **ReorderPoint**  NUMBER |
| **ReverseChargeRate**  NUMBER |
| **SalesTaxCodeRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SalesTaxIncluded**  BOOLEAN |
| **ServiceType**  STRING |
| **Sku**  STRING |
| **Source**  STRING |
| **SubItem**  BOOLEAN |
| **SyncToken**  STRING |
| **TaxClassificationRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Taxable**  BOOLEAN |
| **TrackQtyOnHand**  BOOLEAN |
| **Type**  STRING |
| **UQCDisplayText**  STRING |
| **UQCId**  STRING |
| **UnitPrice**  NUMBER |
| **domain**  STRING |
| **patternProperties**  OBJECT  Click to expand patternProperties |

### journal\_entries

The `journal_entries` table contains info about the journal entries in your QuickBooks instance. A journal entry is a transaction that:

- Contains a pair of distribution lines, including a debit and a credit
- Each distribution line has an account from the Chart of Accounts
- The total of the debit column equals the total of the credit column

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/journalentry)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/journalentry/#query-a-journalentry "Opens in new tab: QuickBooks API method") |

journal\_entries table foreign keys

| Join journal\_entries with | on |
| --- | --- |
| [accounts](#accounts) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = accounts.Id ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = accounts.ParentRef.value ```  ``` journal_entries.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = bill_payments.APAccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` journal_entries.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` journal_entries.Id = bill_payments.Line.LinkedTxn.TxnId ``` |
| [bills](#bills) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = bills.APAccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` journal_entries.CurrencyRef.value = bills.CurrencyRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` journal_entries.Id = bills.Id ``` |
| [budgets](#budgets) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = budgets.BudgetDetail.AccountRef.value ``` |
| [deposits](#deposits) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = deposits.CashBack.AccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = deposits.DepositToAccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` journal_entries.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` journal_entries.Id = deposits.Line.LinkedTxn.TxnId ``` |
| [invoices](#invoices) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = invoices.DepositToAccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` journal_entries.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` journal_entries.TaxRateRef.value = invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ```  ``` journal_entries.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ``` |
| [items](#items) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = items.AssetAccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = items.ExpenseAccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = items.IncomeAccountRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = items.SalesTaxCodeRef.value ``` |
| [payments](#payments) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = payments.DepositToAccountRef.value ```  ``` journal_entries.CurrencyRef.value = payments.CurrencyRef.value ```  ``` journal_entries.Id = payments.Id ``` |
| [purchase\_orders](#purchase-orders) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = purchase_orders.APAccountRef.value ```  ``` journal_entries.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [purchases](#purchases) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = purchases.AccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` journal_entries.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` journal_entries.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` journal_entries.Id = refund_receipts.Id ``` |
| [sales\_receipts](#sales-receipts) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` journal_entries.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` journal_entries.Id = sales_receipts.Id ``` |
| [transfers](#transfers) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = transfers.FromAccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = transfers.ToAccountRef.value ```  ``` journal_entries.CurrencyRef.value = transfers.CurrencyRef.value ```  ``` journal_entries.Id = transfers.Id ``` |
| [vendor\_credits](#vendor-credits) | ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = vendor_credits.APAccountRef.value ```  ``` journal_entries.Line.JournalEntryLineDetail.AccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` journal_entries.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` journal_entries.Id = vendor_credits.Id ``` |
| [credit\_memos](#credit-memos) | ``` journal_entries.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [customers](#customers) | ``` journal_entries.CurrencyRef.value = customers.CurrencyRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = customers.DefaultTaxCodeRef.value ``` |
| [estimates](#estimates) | ``` journal_entries.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` journal_entries.TxnTaxDetail.TxnTaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` journal_entries.TaxRateRef.value = estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value ```  ``` journal_entries.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value ``` |
| [vendors](#vendors) | ``` journal_entries.CurrencyRef.value = vendors.CurrencyRef.value ``` |
| [tax\_codes](#tax-codes) | ``` journal_entries.TaxRateRef.value = tax_codes.PurchaseTaxRateList.TaxRateDetail.TaxRateRef.value ```  ``` journal_entries.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = tax_codes.PurchaseTaxRateList.TaxRateDetail.TaxRateRef.value ```  ``` journal_entries.TaxRateRef.value = tax_codes.SalesTaxRateList.TaxRateDetail.TaxRateRef.value ```  ``` journal_entries.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = tax_codes.SalesTaxRateList.TaxRateDetail.TaxRateRef.value ``` |
| [tax\_rates](#tax-rates) | ``` journal_entries.TaxRateRef.value = tax_rates.Id ```  ``` journal_entries.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value = tax_rates.Id ``` |

journal\_entries table schema

|  |
| --- |
| **Adjustment**  BOOLEAN |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **ExchangeRate**  NUMBER |
| **GlobalTaxCalculation**  STRING |
| **HomeTotalAmt**  NUMBER |
| **Id**  STRING |
| **JournalCodeRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Line**  ARRAY This is a nested data structure:   - Amount: NUMBER - Description: STRING - DescriptionLineDetail: OBJECT, which is also a nested data structure.   - ServiceDate: DATE-TIME   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - DetailType: STRING - Id: STRING - JournalEntryLineDetail: OBJECT, which is also a nested data structure.   - AccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - BillableStatus: STRING   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DepartmentRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Entity: OBJECT, which is also a nested data structure.     - EntityRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Type: STRING   - JournalCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - PostingType: STRING   - TaxAmount: NUMBER   - TaxApplicableOn: STRING   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER - LineNum: NUMBER |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SyncToken**  STRING |
| **TaxRateRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnTaxDetail**  OBJECT This is a nested data structure:   - TaxLine: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - DetailType: STRING   - TaxLineDetail: OBJECT, which is also a nested data structure.     - NetAmountTaxable: NUMBER     - OverrideDeltaAmount: NUMBER     - PercentBased: BOOLEAN     - TaxInclusiveAmount: NUMBER     - TaxPercent: NUMBER     - TaxRateRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - TotalTax: NUMBER - TxnTaxCodeRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **domain**  STRING |

### payment\_methods

The `payment_methods` table contains info about the methods of payment your company receives for goods. **Note**: Both active and inactive payment methods are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/paymentmethod)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/paymentmethod/#query-a-paymentmethod "Opens in new tab: QuickBooks API method") |

payment\_methods table foreign keys

| Join payment\_methods with | on |
| --- | --- |
| [customers](#customers) | ``` payment_methods.Id = customers.PaymentMethodRef.value ``` |
| [deposits](#deposits) | ``` payment_methods.Id = deposits.Line.DepositLineDetail.PaymentMethodRef.value ``` |
| [payments](#payments) | ``` payment_methods.Id = payments.PaymentMethodRef.value ``` |
| [purchases](#purchases) | ``` payment_methods.Id = purchases.PaymentMethodRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` payment_methods.Id = refund_receipts.PaymentMethodRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` payment_methods.Id = sales_receipts.PaymentMethodRef.value ``` |

payment\_methods table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Name**  STRING |
| **SyncToken**  STRING |
| **Type**  STRING |
| **domain**  STRING |

### payments

The `payments` table contains info about the payments recorded in your QuickBooks instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/payment)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/payment/#query-a-payment "Opens in new tab: QuickBooks API method") |

payments table foreign keys

| Join payments with | on |
| --- | --- |
| [accounts](#accounts) | ``` payments.DepositToAccountRef.value = accounts.Id ```  ``` payments.DepositToAccountRef.value = accounts.ParentRef.value ```  ``` payments.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` payments.DepositToAccountRef.value = bill_payments.APAccountRef.value ```  ``` payments.DepositToAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` payments.DepositToAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` payments.CurrencyRef.value = bill_payments.CurrencyRef.value ``` |
| [bills](#bills) | ``` payments.DepositToAccountRef.value = bills.APAccountRef.value ```  ``` payments.DepositToAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` payments.CurrencyRef.value = bills.CurrencyRef.value ```  ``` payments.CustomerRef.value = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ``` |
| [budgets](#budgets) | ``` payments.DepositToAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` payments.CustomerRef.value = budgets.BudgetDetail.CustomerRef.value ``` |
| [deposits](#deposits) | ``` payments.DepositToAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` payments.DepositToAccountRef.value = deposits.DepositToAccountRef.value ```  ``` payments.DepositToAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` payments.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` payments.Id = deposits.Line.LinkedTxn.TxnId ```  ``` payments.PaymentMethodRef.value = deposits.Line.DepositLineDetail.PaymentMethodRef.value ``` |
| [invoices](#invoices) | ``` payments.DepositToAccountRef.value = invoices.DepositToAccountRef.value ```  ``` payments.DepositToAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` payments.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` payments.CustomerRef.value = invoices.CustomerRef.value ```  ``` payments.Line.LinkedTxn.TxnId = invoices.Id ```  ``` payments.Id = invoices.LinkedTxn.TxnId ```  ``` payments.Line.LinkedTxn.TxnId = invoices.LinkedTxn.TxnId ``` |
| [items](#items) | ``` payments.DepositToAccountRef.value = items.AssetAccountRef.value ```  ``` payments.DepositToAccountRef.value = items.ExpenseAccountRef.value ```  ``` payments.DepositToAccountRef.value = items.IncomeAccountRef.value ``` |
| [journal\_entries](#journal-entries) | ``` payments.DepositToAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` payments.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` payments.Id = journal_entries.Id ``` |
| [purchase\_orders](#purchase-orders) | ``` payments.DepositToAccountRef.value = purchase_orders.APAccountRef.value ```  ``` payments.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` payments.CustomerRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ``` |
| [purchases](#purchases) | ``` payments.DepositToAccountRef.value = purchases.AccountRef.value ```  ``` payments.DepositToAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` payments.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` payments.CustomerRef.value = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` payments.PaymentMethodRef.value = purchases.PaymentMethodRef.value ```  ``` payments.Line.LinkedTxn.TxnId = purchases.Id ```  ``` payments.Id = purchases.Id ``` |
| [refund\_receipts](#refund-receipts) | ``` payments.DepositToAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` payments.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` payments.CustomerRef.value = refund_receipts.CustomerRef.value ```  ``` payments.PaymentMethodRef.value = refund_receipts.PaymentMethodRef.value ```  ``` payments.Id = refund_receipts.Id ``` |
| [sales\_receipts](#sales-receipts) | ``` payments.DepositToAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` payments.DepositToAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` payments.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` payments.CustomerRef.value = sales_receipts.CustomerRef.value ```  ``` payments.PaymentMethodRef.value = sales_receipts.PaymentMethodRef.value ```  ``` payments.Id = sales_receipts.Id ``` |
| [transfers](#transfers) | ``` payments.DepositToAccountRef.value = transfers.FromAccountRef.value ```  ``` payments.DepositToAccountRef.value = transfers.ToAccountRef.value ```  ``` payments.CurrencyRef.value = transfers.CurrencyRef.value ```  ``` payments.Id = transfers.Id ``` |
| [vendor\_credits](#vendor-credits) | ``` payments.DepositToAccountRef.value = vendor_credits.APAccountRef.value ```  ``` payments.DepositToAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` payments.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` payments.CustomerRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ``` |
| [credit\_memos](#credit-memos) | ``` payments.Line.LinkedTxn.TxnId = credit_memos.Id ```  ``` payments.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` payments.CustomerRef.value = credit_memos.CustomerRef.value ``` |
| [customers](#customers) | ``` payments.CurrencyRef.value = customers.CurrencyRef.value ```  ``` payments.CustomerRef.value = customers.Id ```  ``` payments.PaymentMethodRef.value = customers.PaymentMethodRef.value ``` |
| [estimates](#estimates) | ``` payments.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` payments.CustomerRef.value = estimates.CustomerRef.value ```  ``` payments.Line.LinkedTxn.TxnId = estimates.LinkedTxn.TxnId ```  ``` payments.Id = estimates.Id ``` |
| [vendors](#vendors) | ``` payments.CurrencyRef.value = vendors.CurrencyRef.value ``` |
| [payment\_methods](#payment-methods) | ``` payments.PaymentMethodRef.value = payment_methods.Id ``` |
| [time\_activities](#time-activities) | ``` payments.Id = time_activities.Id ``` |

payments table schema

|  |
| --- |
| **ARAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CreditCardPayment**  OBJECT This is a nested data structure:   - CreditChargeInfo: OBJECT, which is also a nested data structure.   - Amount: NUMBER   - BillAddrStreet: STRING   - CcExpiryMonth: INTEGER   - CcExpiryYear: INTEGER   - NameOnAcct: STRING   - PostalCode: STRING   - ProcessPayment: BOOLEAN   - Type: STRING - CreditChargeResponse: OBJECT, which is also a nested data structure.   - AuthCode: STRING   - CCTransId: STRING   - Status: STRING   - TxnAuthorizationTime: DATE-TIME |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CustomerRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepositToAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ExchangeRate**  NUMBER |
| **Id**  STRING |
| **Line**  ARRAY This is a nested data structure:   - Amount: NUMBER - LineEx: OBJECT, which is also a nested data structure.   - any: ARRAY, which is also a nested data structure.     - declaredType: STRING     - globalScope: BOOLEAN     - name: STRING     - nil: BOOLEAN     - scope: STRING     - typeSubstituted: BOOLEAN     - value: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - LinkedTxn: ARRAY, which is also a nested data structure.   - TxnId: STRING   - TxnLineId: STRING   - TxnType: STRING |
| **LinkedTxn**  ARRAY This is a nested data structure:   - TxnId: STRING - TxnLineId: STRING - TxnType: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PaymentMethodRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **PaymentRefNum**  STRING |
| **PrivateNote**  STRING |
| **ProcessPayment**  BOOLEAN |
| **SyncToken**  STRING |
| **TaxExemptionRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnSource**  STRING |
| **UnappliedAmt**  NUMBER |
| **domain**  STRING |

### profit\_loss\_report

The `profit_loss_report` table contains reports about profit and loss recorded in your QuickBooks instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ReportDate |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/most-commonly-used/profitandloss)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/most-commonly-used/profitandloss#query-a-report "Opens in new tab: QuickBooks API method") |

profit\_loss\_report table schema

|  |
| --- |
| **AccountingMethod**  STRING |
| **Details**  OBJECT |
| **ReportDate**  DATE-TIME |

### purchase\_orders

The `purchase_orders` table contains info about purchase orders in your QuickBooks instance. A purchase order is a request to purchase goods or services from a third party.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/purchaseorder)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/purchaseorder/#query-a-purchaseorder "Opens in new tab: QuickBooks API method") |

purchase\_orders table foreign keys

| Join purchase\_orders with | on |
| --- | --- |
| [accounts](#accounts) | ``` purchase_orders.APAccountRef.value = accounts.Id ```  ``` purchase_orders.APAccountRef.value = accounts.ParentRef.value ```  ``` purchase_orders.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` purchase_orders.APAccountRef.value = bill_payments.APAccountRef.value ```  ``` purchase_orders.APAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` purchase_orders.APAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` purchase_orders.LinkedTxn.TxnId = bill_payments.Line.LinkedTxn.TxnId ```  ``` purchase_orders.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` purchase_orders.DepartmentRef.value = bill_payments.DepartmentRef.value ```  ``` purchase_orders.Id = bill_payments.Id ```  ``` purchase_orders.VendorRef.value = bill_payments.VendorRef.value ``` |
| [bills](#bills) | ``` purchase_orders.APAccountRef.value = bills.APAccountRef.value ```  ``` purchase_orders.APAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` purchase_orders.LinkedTxn.TxnId = bills.Id ```  ``` purchase_orders.CurrencyRef.value = bills.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` purchase_orders.DepartmentRef.value = bills.DepartmentRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value = bills.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` purchase_orders.Id = bills.LinkedTxn.TxnId ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` purchase_orders.SalesTermRef.value = bills.SalesTermRef.value ```  ``` purchase_orders.VendorRef.value = bills.VendorRef.value ``` |
| [budgets](#budgets) | ``` purchase_orders.APAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` purchase_orders.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = budgets.BudgetDetail.CustomerRef.value ```  ``` purchase_orders.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [deposits](#deposits) | ``` purchase_orders.APAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` purchase_orders.APAccountRef.value = deposits.DepositToAccountRef.value ```  ``` purchase_orders.APAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` purchase_orders.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` purchase_orders.DepartmentRef.value = deposits.DepartmentRef.value ``` |
| [invoices](#invoices) | ``` purchase_orders.APAccountRef.value = invoices.DepositToAccountRef.value ```  ``` purchase_orders.APAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` purchase_orders.ClassRef.value = invoices.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = invoices.ClassRef.value ```  ``` purchase_orders.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` purchase_orders.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = invoices.CustomerRef.value ```  ``` purchase_orders.DepartmentRef.value = invoices.DepartmentRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value = invoices.Line.SalesItemLineDetail.ItemRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` purchase_orders.SalesTermRef.value = invoices.SalesTermRef.value ``` |
| [items](#items) | ``` purchase_orders.APAccountRef.value = items.AssetAccountRef.value ```  ``` purchase_orders.APAccountRef.value = items.ExpenseAccountRef.value ```  ``` purchase_orders.APAccountRef.value = items.IncomeAccountRef.value ```  ``` purchase_orders.ClassRef.value = items.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = items.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value = items.Id ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value = items.ParentRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ```  ``` purchase_orders.VendorRef.value = items.PrefVendorRef.value ``` |
| [journal\_entries](#journal-entries) | ``` purchase_orders.APAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` purchase_orders.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [payments](#payments) | ``` purchase_orders.APAccountRef.value = payments.DepositToAccountRef.value ```  ``` purchase_orders.CurrencyRef.value = payments.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = payments.CustomerRef.value ``` |
| [purchases](#purchases) | ``` purchase_orders.APAccountRef.value = purchases.AccountRef.value ```  ``` purchase_orders.APAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` purchase_orders.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` purchase_orders.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` purchase_orders.DepartmentRef.value = purchases.DepartmentRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value = purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` purchase_orders.APAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` purchase_orders.ClassRef.value = refund_receipts.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = refund_receipts.ClassRef.value ```  ``` purchase_orders.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = refund_receipts.CustomerRef.value ```  ``` purchase_orders.DepartmentRef.value = refund_receipts.DepartmentRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value = refund_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` purchase_orders.APAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` purchase_orders.APAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` purchase_orders.ClassRef.value = sales_receipts.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = sales_receipts.ClassRef.value ```  ``` purchase_orders.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = sales_receipts.CustomerRef.value ```  ``` purchase_orders.DepartmentRef.value = sales_receipts.DepartmentRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value = sales_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [transfers](#transfers) | ``` purchase_orders.APAccountRef.value = transfers.FromAccountRef.value ```  ``` purchase_orders.APAccountRef.value = transfers.ToAccountRef.value ```  ``` purchase_orders.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` purchase_orders.APAccountRef.value = vendor_credits.APAccountRef.value ```  ``` purchase_orders.APAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` purchase_orders.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` purchase_orders.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` purchase_orders.DepartmentRef.value = vendor_credits.DepartmentRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` purchase_orders.VendorRef.value = vendor_credits.VendorRef.value ``` |
| [classes](#classes) | ``` purchase_orders.ClassRef.value = classes.Id ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = classes.Id ```  ``` purchase_orders.ClassRef.value = classes.ParentRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = classes.ParentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` purchase_orders.ClassRef.value = credit_memos.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = credit_memos.ClassRef.value ```  ``` purchase_orders.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = credit_memos.CustomerRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value = credit_memos.Line.SalesItemLineDetail.ItemRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchase_orders.SalesTermRef.value = credit_memos.SalesTermRef.value ``` |
| [estimates](#estimates) | ``` purchase_orders.ClassRef.value = estimates.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = estimates.ClassRef.value ```  ``` purchase_orders.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = estimates.CustomerRef.value ```  ``` purchase_orders.DepartmentRef.value = estimates.DepartmentRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value = estimates.Line.SalesItemLineDetail.ItemRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` purchase_orders.SalesTermRef.value = estimates.SalesTermRef.value ``` |
| [time\_activities](#time-activities) | ``` purchase_orders.ClassRef.value = time_activities.ClassRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value = time_activities.ClassRef.value ```  ``` purchase_orders.DepartmentRef.value = time_activities.DepartmentRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value = time_activities.ItemRef.value ```  ``` purchase_orders.VendorRef.value = time_activities.VendorRef.value ``` |
| [customers](#customers) | ``` purchase_orders.CurrencyRef.value = customers.CurrencyRef.value ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value = customers.Id ```  ``` purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ```  ``` purchase_orders.SalesTermRef.value = customers.SalesTermRef.value ``` |
| [vendors](#vendors) | ``` purchase_orders.CurrencyRef.value = vendors.CurrencyRef.value ```  ``` purchase_orders.VendorRef.value = vendors.Id ``` |
| [departments](#departments) | ``` purchase_orders.DepartmentRef.value = departments.ParentRef.value ```  ``` purchase_orders.DepartmentRef.value = departments.Id ``` |
| [terms](#terms) | ``` purchase_orders.SalesTermRef.value = terms.Id ``` |

purchase\_orders table schema

|  |
| --- |
| **APAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ClassRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CustomField**  ARRAY |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **DueDate**  DATE-TIME |
| **EmailStatus**  STRING |
| **ExchangeRate**  NUMBER |
| **GlobalTaxCalculation**  STRING |
| **Id**  STRING |
| **Line**  ARRAY This is a nested data structure:   - AccountBasedExpenseLineDetail: OBJECT, which is also a nested data structure.   - AccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - BillableStatus: STRING   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - CustomerRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - TaxAmount: NUMBER   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER - Amount: NUMBER - Description: STRING - DetailType: STRING - Id: STRING - ItemBasedExpenseLineDetail: OBJECT, which is also a nested data structure.   - BillableStatus: STRING   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - CustomerRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - PriceLevelRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Qty: INTEGER   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER   - UnitPrice: NUMBER - LineNum: INTEGER - LinkedTxn: ARRAY, which is also a nested data structure.   - TxnId: STRING   - TxnLineId: STRING   - TxnType: STRING |
| **LinkedTxn**  ARRAY This is a nested data structure:   - TxnId: STRING - TxnLineId: STRING - TxnType: STRING |
| **Memo**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **POEmail**  OBJECT This is a nested data structure:   - Address: STRING |
| **POStatus**  STRING |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SalesTermRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ShipAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **ShipMethodRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ShipTo**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SyncToken**  STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnTaxDetail**  OBJECT This is a nested data structure:   - TaxLine: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - DetailType: STRING   - TaxLineDetail: OBJECT, which is also a nested data structure.     - NetAmountTaxable: NUMBER     - OverrideDeltaAmount: NUMBER     - PercentBased: BOOLEAN     - TaxInclusiveAmount: NUMBER     - TaxPercent: NUMBER     - TaxRateRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - TotalTax: NUMBER - TxnTaxCodeRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **VendorAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **VendorRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **domain**  STRING |

### purchases

The `purchases` table contains info about the purchases recorded in your QuickBooks instance. This table includes all purchase types: `Cash`, `Check`, and `CreditCard`.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/purchase)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/purchase/#query-a-purchase "Opens in new tab: QuickBooks API method") |

purchases table foreign keys

| Join purchases with | on |
| --- | --- |
| [accounts](#accounts) | ``` purchases.AccountRef.value = accounts.Id ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = accounts.Id ```  ``` purchases.AccountRef.value = accounts.ParentRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = accounts.ParentRef.value ```  ``` purchases.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` purchases.AccountRef.value = bill_payments.APAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = bill_payments.APAccountRef.value ```  ``` purchases.AccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` purchases.AccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` purchases.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` purchases.DepartmentRef.value = bill_payments.DepartmentRef.value ``` |
| [bills](#bills) | ``` purchases.AccountRef.value = bills.APAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = bills.APAccountRef.value ```  ``` purchases.AccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` purchases.CurrencyRef.value = bills.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` purchases.DepartmentRef.value = bills.DepartmentRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value = bills.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [budgets](#budgets) | ``` purchases.AccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = budgets.BudgetDetail.CustomerRef.value ```  ``` purchases.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [deposits](#deposits) | ``` purchases.AccountRef.value = deposits.CashBack.AccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = deposits.CashBack.AccountRef.value ```  ``` purchases.AccountRef.value = deposits.DepositToAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = deposits.DepositToAccountRef.value ```  ``` purchases.AccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` purchases.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` purchases.DepartmentRef.value = deposits.DepartmentRef.value ```  ``` purchases.PaymentMethodRef.value = deposits.Line.DepositLineDetail.PaymentMethodRef.value ``` |
| [invoices](#invoices) | ``` purchases.AccountRef.value = invoices.DepositToAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = invoices.DepositToAccountRef.value ```  ``` purchases.AccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = invoices.ClassRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` purchases.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = invoices.CustomerRef.value ```  ``` purchases.DepartmentRef.value = invoices.DepartmentRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value = invoices.Line.SalesItemLineDetail.ItemRef.value ```  ``` purchases.Id = invoices.LinkedTxn.TxnId ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` purchases.Id = invoices.Id ``` |
| [items](#items) | ``` purchases.AccountRef.value = items.AssetAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = items.AssetAccountRef.value ```  ``` purchases.AccountRef.value = items.ExpenseAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = items.ExpenseAccountRef.value ```  ``` purchases.AccountRef.value = items.IncomeAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = items.IncomeAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = items.ClassRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value = items.Id ```  ``` purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value = items.ParentRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ``` |
| [journal\_entries](#journal-entries) | ``` purchases.AccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` purchases.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [payments](#payments) | ``` purchases.AccountRef.value = payments.DepositToAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = payments.DepositToAccountRef.value ```  ``` purchases.CurrencyRef.value = payments.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = payments.CustomerRef.value ```  ``` purchases.PaymentMethodRef.value = payments.PaymentMethodRef.value ```  ``` purchases.Id = payments.Line.LinkedTxn.TxnId ```  ``` purchases.Id = payments.Id ``` |
| [purchase\_orders](#purchase-orders) | ``` purchases.AccountRef.value = purchase_orders.APAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = purchase_orders.APAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = purchase_orders.ClassRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` purchases.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ```  ``` purchases.DepartmentRef.value = purchase_orders.DepartmentRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` purchases.AccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = refund_receipts.ClassRef.value ```  ``` purchases.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = refund_receipts.CustomerRef.value ```  ``` purchases.DepartmentRef.value = refund_receipts.DepartmentRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value = refund_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` purchases.PaymentMethodRef.value = refund_receipts.PaymentMethodRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` purchases.AccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` purchases.AccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = sales_receipts.ClassRef.value ```  ``` purchases.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = sales_receipts.CustomerRef.value ```  ``` purchases.DepartmentRef.value = sales_receipts.DepartmentRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value = sales_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` purchases.PaymentMethodRef.value = sales_receipts.PaymentMethodRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [transfers](#transfers) | ``` purchases.AccountRef.value = transfers.FromAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = transfers.FromAccountRef.value ```  ``` purchases.AccountRef.value = transfers.ToAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = transfers.ToAccountRef.value ```  ``` purchases.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` purchases.AccountRef.value = vendor_credits.APAccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = vendor_credits.APAccountRef.value ```  ``` purchases.AccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` purchases.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` purchases.DepartmentRef.value = vendor_credits.DepartmentRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [classes](#classes) | ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = classes.Id ```  ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = classes.ParentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = credit_memos.ClassRef.value ```  ``` purchases.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = credit_memos.CustomerRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value = credit_memos.Line.SalesItemLineDetail.ItemRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchases.Id = credit_memos.Id ``` |
| [estimates](#estimates) | ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = estimates.ClassRef.value ```  ``` purchases.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = estimates.CustomerRef.value ```  ``` purchases.DepartmentRef.value = estimates.DepartmentRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value = estimates.Line.SalesItemLineDetail.ItemRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` purchases.Id = estimates.Id ``` |
| [time\_activities](#time-activities) | ``` purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value = time_activities.ClassRef.value ```  ``` purchases.DepartmentRef.value = time_activities.DepartmentRef.value ```  ``` purchases.EntityRef.value = time_activities.EmployeeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value = time_activities.ItemRef.value ```  ``` purchases.Id = time_activities.Id ``` |
| [customers](#customers) | ``` purchases.CurrencyRef.value = customers.CurrencyRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value = customers.Id ```  ``` purchases.PaymentMethodRef.value = customers.PaymentMethodRef.value ```  ``` purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ```  ``` purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ``` |
| [vendors](#vendors) | ``` purchases.CurrencyRef.value = vendors.CurrencyRef.value ``` |
| [departments](#departments) | ``` purchases.DepartmentRef.value = departments.ParentRef.value ```  ``` purchases.DepartmentRef.value = departments.Id ``` |
| [employees](#employees) | ``` purchases.EntityRef.value = employees.Id ``` |
| [payment\_methods](#payment-methods) | ``` purchases.PaymentMethodRef.value = payment_methods.Id ``` |

purchases table schema

|  |
| --- |
| **AccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Credit**  BOOLEAN |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **EntityRef**  OBJECT This is a nested data structure:   - name: STRING - type: STRING - value: STRING |
| **ExchangeRate**  NUMBER |
| **GlobalTaxCalculation**  STRING |
| **Id**  STRING |
| **IncludeInAnnualTPAR**  BOOLEAN |
| **Line**  ARRAY This is a nested data structure:   - AccountBasedExpenseLineDetail: OBJECT, which is also a nested data structure.   - AccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - BillableStatus: STRING   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - CustomerRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - TaxAmount: NUMBER   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER - Amount: NUMBER - Description: STRING - DetailType: STRING - Id: STRING - ItemBasedExpenseLineDetail: OBJECT, which is also a nested data structure.   - BillableStatus: STRING   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - CustomerRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - PriceLevelRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Qty: INTEGER   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER   - UnitPrice: NUMBER - LineNum: INTEGER - LinkedTxn: ARRAY, which is also a nested data structure.   - TxnId: STRING   - TxnLineId: STRING   - TxnType: STRING |
| **LinkedTxn**  ARRAY This is a nested data structure:   - TxnId: STRING - TxnLineId: STRING - TxnType: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PaymentMethodRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **PaymentType**  STRING |
| **PrintStatus**  STRING |
| **PrivateNote**  STRING |
| **PurchaseEx**  OBJECT This is a nested data structure:   - any: ARRAY, which is also a nested data structure.   - declaredType: STRING   - globalScope: BOOLEAN   - name: STRING   - nil: BOOLEAN   - scope: STRING   - typeSubstituted: BOOLEAN   - value: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **RemitToAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **SyncToken**  STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnSource**  STRING |
| **TxnTaxDetail**  OBJECT This is a nested data structure:   - TaxLine: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - DetailType: STRING   - TaxLineDetail: OBJECT, which is also a nested data structure.     - NetAmountTaxable: NUMBER     - OverrideDeltaAmount: NUMBER     - PercentBased: BOOLEAN     - TaxInclusiveAmount: NUMBER     - TaxPercent: NUMBER     - TaxRateRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - TotalTax: NUMBER - TxnTaxCodeRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **domain**  STRING |
| **patternProperties**  OBJECT  Click to expand patternProperties |

### refund\_receipts

The `refund_receipts` table contains info about customer refunds recorded in your QuickBooks instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/refundreceipt)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/refundreceipt/#query-a-refundreceipt "Opens in new tab: QuickBooks API method") |

refund\_receipts table foreign keys

| Join refund\_receipts with | on |
| --- | --- |
| [accounts](#accounts) | ``` refund_receipts.DepositToAccountRef.value = accounts.Id ```  ``` refund_receipts.DepositToAccountRef.value = accounts.ParentRef.value ```  ``` refund_receipts.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` refund_receipts.DepositToAccountRef.value = bill_payments.APAccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` refund_receipts.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` refund_receipts.DepartmentRef.value = bill_payments.DepartmentRef.value ``` |
| [bills](#bills) | ``` refund_receipts.DepositToAccountRef.value = bills.APAccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` refund_receipts.CurrencyRef.value = bills.CurrencyRef.value ```  ``` refund_receipts.CustomerRef.value = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` refund_receipts.DepartmentRef.value = bills.DepartmentRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.ItemRef.value = bills.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [budgets](#budgets) | ``` refund_receipts.DepositToAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` refund_receipts.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` refund_receipts.CustomerRef.value = budgets.BudgetDetail.CustomerRef.value ```  ``` refund_receipts.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [deposits](#deposits) | ``` refund_receipts.DepositToAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = deposits.DepositToAccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` refund_receipts.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` refund_receipts.DepartmentRef.value = deposits.DepartmentRef.value ```  ``` refund_receipts.PaymentMethodRef.value = deposits.Line.DepositLineDetail.PaymentMethodRef.value ```  ``` refund_receipts.Id = deposits.Line.LinkedTxn.TxnId ``` |
| [invoices](#invoices) | ``` refund_receipts.DepositToAccountRef.value = invoices.DepositToAccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` refund_receipts.ClassRef.value = invoices.ClassRef.value ```  ``` refund_receipts.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` refund_receipts.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` refund_receipts.CustomerRef.value = invoices.CustomerRef.value ```  ``` refund_receipts.DepartmentRef.value = invoices.DepartmentRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.ItemRef.value = invoices.Line.SalesItemLineDetail.ItemRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [items](#items) | ``` refund_receipts.DepositToAccountRef.value = items.AssetAccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = items.ExpenseAccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = items.IncomeAccountRef.value ```  ``` refund_receipts.ClassRef.value = items.ClassRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.ItemRef.value = items.Id ```  ``` refund_receipts.Line.SalesItemLineDetail.ItemRef.value = items.ParentRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ``` |
| [journal\_entries](#journal-entries) | ``` refund_receipts.DepositToAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` refund_receipts.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` refund_receipts.Id = journal_entries.Id ``` |
| [payments](#payments) | ``` refund_receipts.DepositToAccountRef.value = payments.DepositToAccountRef.value ```  ``` refund_receipts.CurrencyRef.value = payments.CurrencyRef.value ```  ``` refund_receipts.CustomerRef.value = payments.CustomerRef.value ```  ``` refund_receipts.PaymentMethodRef.value = payments.PaymentMethodRef.value ```  ``` refund_receipts.Id = payments.Id ``` |
| [purchase\_orders](#purchase-orders) | ``` refund_receipts.DepositToAccountRef.value = purchase_orders.APAccountRef.value ```  ``` refund_receipts.ClassRef.value = purchase_orders.ClassRef.value ```  ``` refund_receipts.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` refund_receipts.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` refund_receipts.CustomerRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ```  ``` refund_receipts.DepartmentRef.value = purchase_orders.DepartmentRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.ItemRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [purchases](#purchases) | ``` refund_receipts.DepositToAccountRef.value = purchases.AccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` refund_receipts.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` refund_receipts.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` refund_receipts.CustomerRef.value = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` refund_receipts.DepartmentRef.value = purchases.DepartmentRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.ItemRef.value = purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` refund_receipts.PaymentMethodRef.value = purchases.PaymentMethodRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` refund_receipts.DepositToAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` refund_receipts.ClassRef.value = sales_receipts.ClassRef.value ```  ``` refund_receipts.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` refund_receipts.CustomerRef.value = sales_receipts.CustomerRef.value ```  ``` refund_receipts.DepartmentRef.value = sales_receipts.DepartmentRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.ItemRef.value = sales_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` refund_receipts.PaymentMethodRef.value = sales_receipts.PaymentMethodRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` refund_receipts.Id = sales_receipts.Id ``` |
| [transfers](#transfers) | ``` refund_receipts.DepositToAccountRef.value = transfers.FromAccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = transfers.ToAccountRef.value ```  ``` refund_receipts.CurrencyRef.value = transfers.CurrencyRef.value ```  ``` refund_receipts.Id = transfers.Id ``` |
| [vendor\_credits](#vendor-credits) | ``` refund_receipts.DepositToAccountRef.value = vendor_credits.APAccountRef.value ```  ``` refund_receipts.DepositToAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` refund_receipts.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` refund_receipts.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` refund_receipts.CustomerRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` refund_receipts.DepartmentRef.value = vendor_credits.DepartmentRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [classes](#classes) | ``` refund_receipts.ClassRef.value = classes.Id ```  ``` refund_receipts.ClassRef.value = classes.ParentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` refund_receipts.ClassRef.value = credit_memos.ClassRef.value ```  ``` refund_receipts.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` refund_receipts.CustomerRef.value = credit_memos.CustomerRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.ItemRef.value = credit_memos.Line.SalesItemLineDetail.ItemRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [estimates](#estimates) | ``` refund_receipts.ClassRef.value = estimates.ClassRef.value ```  ``` refund_receipts.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` refund_receipts.CustomerRef.value = estimates.CustomerRef.value ```  ``` refund_receipts.DepartmentRef.value = estimates.DepartmentRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.ItemRef.value = estimates.Line.SalesItemLineDetail.ItemRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [time\_activities](#time-activities) | ``` refund_receipts.ClassRef.value = time_activities.ClassRef.value ```  ``` refund_receipts.DepartmentRef.value = time_activities.DepartmentRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.ItemRef.value = time_activities.ItemRef.value ``` |
| [customers](#customers) | ``` refund_receipts.CurrencyRef.value = customers.CurrencyRef.value ```  ``` refund_receipts.CustomerRef.value = customers.Id ```  ``` refund_receipts.PaymentMethodRef.value = customers.PaymentMethodRef.value ```  ``` refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ``` |
| [vendors](#vendors) | ``` refund_receipts.CurrencyRef.value = vendors.CurrencyRef.value ``` |
| [departments](#departments) | ``` refund_receipts.DepartmentRef.value = departments.ParentRef.value ```  ``` refund_receipts.DepartmentRef.value = departments.Id ``` |
| [payment\_methods](#payment-methods) | ``` refund_receipts.PaymentMethodRef.value = payment_methods.Id ``` |

refund\_receipts table schema

|  |
| --- |
| **ApplyTaxAfterDiscount**  BOOLEAN |
| **Balance**  NUMBER |
| **BillAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **BillEmail**  OBJECT This is a nested data structure:   - Address: STRING |
| **CheckPayment**  OBJECT This is a nested data structure:   - AcctNum: STRING - BankName: STRING - CheckNum: STRING - NameOnAcct: STRING - Status: STRING |
| **ClassRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CreditCardPayment**  OBJECT This is a nested data structure:   - CreditChargeInfo: OBJECT, which is also a nested data structure.   - Amount: NUMBER   - BillAddrStreet: STRING   - CcExpiryMonth: INTEGER   - CcExpiryYear: INTEGER   - NameOnAcct: STRING   - PostalCode: STRING   - ProcessPayment: BOOLEAN   - Type: STRING - CreditChargeResponse: OBJECT, which is also a nested data structure.   - AuthCode: STRING   - CCTransId: STRING   - Status: STRING   - TxnAuthorizationTime: DATE-TIME |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CustomField**  ARRAY |
| **CustomerMemo**  OBJECT This is a nested data structure:   - value: STRING |
| **CustomerRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepositToAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **ExchangeRate**  NUMBER |
| **FreeFormAddress**  BOOLEAN |
| **GlobalTaxCalculation**  STRING |
| **HomeBalance**  NUMBER |
| **HomeTotalAmt**  NUMBER |
| **Id**  STRING |
| **Line**  ARRAY This is a nested data structure:   - Amount: NUMBER - Description: STRING - DescriptionLineDetail: OBJECT, which is also a nested data structure.   - ServiceDate: DATE-TIME   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - DetailType: STRING - DiscountLineDetail: OBJECT, which is also a nested data structure.   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountAccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountPercent: NUMBER   - PercentBased: BOOLEAN   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - GroupLineDetail: OBJECT, which is also a nested data structure.   - GroupItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Line: ARRAY, which is also a nested data structure.     - Amount: NUMBER     - Description: STRING     - DetailType: STRING     - Id: STRING     - LineNum: NUMBER     - SalesItemLineDetail: OBJECT, which is also a nested data structure.       - ClassRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - DiscountAmt: NUMBER       - DiscountRate: NUMBER       - ItemAccountRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - ItemRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - MarkupInfo: OBJECT, which is also a nested data structure.         - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING         - Percent: NUMBER         - PriceLevelRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING       - Qty: INTEGER       - ServiceDate: DATE-TIME       - TaxClassificationRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - TaxCodeRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - TaxInclusiveAmt: NUMBER       - UnitPrice: NUMBER   - Quantity: NUMBER - Id: STRING - LineNum: INTEGER - SalesItemLineDetail: OBJECT, which is also a nested data structure.   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountAmt: NUMBER   - DiscountRate: NUMBER   - ItemAccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - Qty: INTEGER   - ServiceDate: DATE-TIME   - TaxClassificationRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER   - UnitPrice: NUMBER - SubtotalLineDetail: OBJECT, which is also a nested data structure.   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PaymentMethodRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **PaymentRefNum**  STRING |
| **PaymentType**  STRING |
| **PrintStatus**  STRING |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ShipAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **SyncToken**  STRING |
| **TaxExemptionRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnSource**  STRING |
| **TxnTaxDetail**  OBJECT This is a nested data structure:   - TaxLine: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - DetailType: STRING   - TaxLineDetail: OBJECT, which is also a nested data structure.     - NetAmountTaxable: NUMBER     - OverrideDeltaAmount: NUMBER     - PercentBased: BOOLEAN     - TaxInclusiveAmount: NUMBER     - TaxPercent: NUMBER     - TaxRateRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - TotalTax: NUMBER - TxnTaxCodeRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **domain**  STRING |
| **patternProperties**  OBJECT  Click to expand patternProperties |

### sales\_receipts

The `sales_receipts` table contains info about the sales receipts recorded in your QuickBooks instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/salesreceipt)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/salesreceipt/#query-a-salesreceipt "Opens in new tab: QuickBooks API method") |

sales\_receipts table foreign keys

| Join sales\_receipts with | on |
| --- | --- |
| [accounts](#accounts) | ``` sales_receipts.DepositToAccountRef.value = accounts.Id ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = accounts.Id ```  ``` sales_receipts.DepositToAccountRef.value = accounts.ParentRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = accounts.ParentRef.value ```  ``` sales_receipts.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` sales_receipts.DepositToAccountRef.value = bill_payments.APAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = bill_payments.APAccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` sales_receipts.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` sales_receipts.DepartmentRef.value = bill_payments.DepartmentRef.value ``` |
| [bills](#bills) | ``` sales_receipts.DepositToAccountRef.value = bills.APAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = bills.APAccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` sales_receipts.CurrencyRef.value = bills.CurrencyRef.value ```  ``` sales_receipts.CustomerRef.value = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` sales_receipts.DepartmentRef.value = bills.DepartmentRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.ItemRef.value = bills.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [budgets](#budgets) | ``` sales_receipts.DepositToAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` sales_receipts.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` sales_receipts.CustomerRef.value = budgets.BudgetDetail.CustomerRef.value ```  ``` sales_receipts.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [deposits](#deposits) | ``` sales_receipts.DepositToAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = deposits.DepositToAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = deposits.DepositToAccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` sales_receipts.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` sales_receipts.DepartmentRef.value = deposits.DepartmentRef.value ```  ``` sales_receipts.PaymentMethodRef.value = deposits.Line.DepositLineDetail.PaymentMethodRef.value ```  ``` sales_receipts.Id = deposits.Line.LinkedTxn.TxnId ``` |
| [invoices](#invoices) | ``` sales_receipts.DepositToAccountRef.value = invoices.DepositToAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = invoices.DepositToAccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` sales_receipts.ClassRef.value = invoices.ClassRef.value ```  ``` sales_receipts.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` sales_receipts.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` sales_receipts.CustomerRef.value = invoices.CustomerRef.value ```  ``` sales_receipts.DepartmentRef.value = invoices.DepartmentRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.ItemRef.value = invoices.Line.SalesItemLineDetail.ItemRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [items](#items) | ``` sales_receipts.DepositToAccountRef.value = items.AssetAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = items.AssetAccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = items.ExpenseAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = items.ExpenseAccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = items.IncomeAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = items.IncomeAccountRef.value ```  ``` sales_receipts.ClassRef.value = items.ClassRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.ItemRef.value = items.Id ```  ``` sales_receipts.Line.SalesItemLineDetail.ItemRef.value = items.ParentRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ``` |
| [journal\_entries](#journal-entries) | ``` sales_receipts.DepositToAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` sales_receipts.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` sales_receipts.Id = journal_entries.Id ``` |
| [payments](#payments) | ``` sales_receipts.DepositToAccountRef.value = payments.DepositToAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = payments.DepositToAccountRef.value ```  ``` sales_receipts.CurrencyRef.value = payments.CurrencyRef.value ```  ``` sales_receipts.CustomerRef.value = payments.CustomerRef.value ```  ``` sales_receipts.PaymentMethodRef.value = payments.PaymentMethodRef.value ```  ``` sales_receipts.Id = payments.Id ``` |
| [purchase\_orders](#purchase-orders) | ``` sales_receipts.DepositToAccountRef.value = purchase_orders.APAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = purchase_orders.APAccountRef.value ```  ``` sales_receipts.ClassRef.value = purchase_orders.ClassRef.value ```  ``` sales_receipts.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` sales_receipts.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` sales_receipts.CustomerRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ```  ``` sales_receipts.DepartmentRef.value = purchase_orders.DepartmentRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.ItemRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [purchases](#purchases) | ``` sales_receipts.DepositToAccountRef.value = purchases.AccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = purchases.AccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` sales_receipts.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` sales_receipts.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` sales_receipts.CustomerRef.value = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` sales_receipts.DepartmentRef.value = purchases.DepartmentRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.ItemRef.value = purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` sales_receipts.PaymentMethodRef.value = purchases.PaymentMethodRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` sales_receipts.DepositToAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` sales_receipts.ClassRef.value = refund_receipts.ClassRef.value ```  ``` sales_receipts.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` sales_receipts.CustomerRef.value = refund_receipts.CustomerRef.value ```  ``` sales_receipts.DepartmentRef.value = refund_receipts.DepartmentRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.ItemRef.value = refund_receipts.Line.SalesItemLineDetail.ItemRef.value ```  ``` sales_receipts.PaymentMethodRef.value = refund_receipts.PaymentMethodRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` sales_receipts.Id = refund_receipts.Id ``` |
| [transfers](#transfers) | ``` sales_receipts.DepositToAccountRef.value = transfers.FromAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = transfers.FromAccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = transfers.ToAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = transfers.ToAccountRef.value ```  ``` sales_receipts.CurrencyRef.value = transfers.CurrencyRef.value ```  ``` sales_receipts.Id = transfers.Id ``` |
| [vendor\_credits](#vendor-credits) | ``` sales_receipts.DepositToAccountRef.value = vendor_credits.APAccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = vendor_credits.APAccountRef.value ```  ``` sales_receipts.DepositToAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` sales_receipts.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` sales_receipts.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` sales_receipts.CustomerRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` sales_receipts.DepartmentRef.value = vendor_credits.DepartmentRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [classes](#classes) | ``` sales_receipts.ClassRef.value = classes.Id ```  ``` sales_receipts.ClassRef.value = classes.ParentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` sales_receipts.ClassRef.value = credit_memos.ClassRef.value ```  ``` sales_receipts.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` sales_receipts.CustomerRef.value = credit_memos.CustomerRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.ItemRef.value = credit_memos.Line.SalesItemLineDetail.ItemRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [estimates](#estimates) | ``` sales_receipts.ClassRef.value = estimates.ClassRef.value ```  ``` sales_receipts.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` sales_receipts.CustomerRef.value = estimates.CustomerRef.value ```  ``` sales_receipts.DepartmentRef.value = estimates.DepartmentRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.ItemRef.value = estimates.Line.SalesItemLineDetail.ItemRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [time\_activities](#time-activities) | ``` sales_receipts.ClassRef.value = time_activities.ClassRef.value ```  ``` sales_receipts.DepartmentRef.value = time_activities.DepartmentRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.ItemRef.value = time_activities.ItemRef.value ``` |
| [customers](#customers) | ``` sales_receipts.CurrencyRef.value = customers.CurrencyRef.value ```  ``` sales_receipts.CustomerRef.value = customers.Id ```  ``` sales_receipts.PaymentMethodRef.value = customers.PaymentMethodRef.value ```  ``` sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ``` |
| [vendors](#vendors) | ``` sales_receipts.CurrencyRef.value = vendors.CurrencyRef.value ``` |
| [departments](#departments) | ``` sales_receipts.DepartmentRef.value = departments.ParentRef.value ```  ``` sales_receipts.DepartmentRef.value = departments.Id ``` |
| [payment\_methods](#payment-methods) | ``` sales_receipts.PaymentMethodRef.value = payment_methods.Id ``` |

sales\_receipts table schema

|  |
| --- |
| **ApplyTaxAfterDiscount**  BOOLEAN |
| **Balance**  NUMBER |
| **BillAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **BillEmail**  OBJECT This is a nested data structure:   - Address: STRING |
| **ClassRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CreditCardPayment**  OBJECT This is a nested data structure:   - CreditChargeInfo: OBJECT, which is also a nested data structure.   - Amount: NUMBER   - BillAddrStreet: STRING   - CcExpiryMonth: INTEGER   - CcExpiryYear: INTEGER   - NameOnAcct: STRING   - PostalCode: STRING   - ProcessPayment: BOOLEAN   - Type: STRING - CreditChargeResponse: OBJECT, which is also a nested data structure.   - AuthCode: STRING   - CCTransId: STRING   - Status: STRING   - TxnAuthorizationTime: DATE-TIME |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CustomField**  ARRAY |
| **CustomerMemo**  OBJECT This is a nested data structure:   - value: STRING |
| **CustomerRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DeliveryInfo**  OBJECT This is a nested data structure:   - DeliveryTime: DATE-TIME - DeliveryType: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepositToAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **EmailStatus**  STRING |
| **ExchangeRate**  NUMBER |
| **FreeFormAddress**  BOOLEAN |
| **GlobalTaxCalculation**  STRING |
| **HomeBalance**  NUMBER |
| **HomeTotalAmt**  NUMBER |
| **Id**  STRING |
| **Line**  ARRAY This is a nested data structure:   - Amount: NUMBER - Description: STRING - DescriptionLineDetail: OBJECT, which is also a nested data structure.   - ServiceDate: DATE-TIME   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - DetailType: STRING - DiscountLineDetail: OBJECT, which is also a nested data structure.   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountAccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountPercent: NUMBER   - PercentBased: BOOLEAN   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING - GroupLineDetail: OBJECT, which is also a nested data structure.   - GroupItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Line: ARRAY, which is also a nested data structure.     - Amount: NUMBER     - Description: STRING     - DetailType: STRING     - Id: STRING     - LineNum: NUMBER     - SalesItemLineDetail: OBJECT, which is also a nested data structure.       - ClassRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - DiscountAmt: NUMBER       - DiscountRate: NUMBER       - ItemAccountRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - ItemRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - MarkupInfo: OBJECT, which is also a nested data structure.         - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING         - Percent: NUMBER         - PriceLevelRef: OBJECT, which is also a nested data structure.           - name: STRING           - value: STRING       - Qty: INTEGER       - ServiceDate: DATE-TIME       - TaxClassificationRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - TaxCodeRef: OBJECT, which is also a nested data structure.         - name: STRING         - value: STRING       - TaxInclusiveAmt: NUMBER       - UnitPrice: NUMBER   - Quantity: NUMBER - Id: STRING - LineNum: INTEGER - SalesItemLineDetail: OBJECT, which is also a nested data structure.   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - DiscountAmt: NUMBER   - DiscountRate: NUMBER   - ItemAccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - Qty: INTEGER   - ServiceDate: DATE-TIME   - TaxClassificationRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER   - UnitPrice: NUMBER - SubtotalLineDetail: OBJECT, which is also a nested data structure.   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING |
| **LinkedTxn**  ARRAY This is a nested data structure:   - TxnId: STRING - TxnLineId: STRING - TxnType: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PaymentMethodRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **PaymentRefNum**  STRING |
| **PrintStatus**  STRING |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ShipAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **ShipDate**  DATE-TIME |
| **ShipFromAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **ShipMethodRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SyncToken**  STRING |
| **TotalAmt**  NUMBER |
| **TrackingNum**  STRING |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **TxnSource**  STRING |
| **TxnTaxDetail**  OBJECT This is a nested data structure:   - TaxLine: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - DetailType: STRING   - TaxLineDetail: OBJECT, which is also a nested data structure.     - NetAmountTaxable: NUMBER     - OverrideDeltaAmount: NUMBER     - PercentBased: BOOLEAN     - TaxInclusiveAmount: NUMBER     - TaxPercent: NUMBER     - TaxRateRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING - TotalTax: NUMBER - TxnTaxCodeRef: OBJECT, which is also a nested data structure.   - name: STRING   - value: STRING |
| **domain**  STRING |
| **patternProperties**  OBJECT  Click to expand patternProperties |

### tax\_agencies

The `tax_agencies` table contains info about the tax-collecting entites defined in your QuickBooks instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/taxagency)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/taxagency/#query-a-taxagency "Opens in new tab: QuickBooks API method") |

tax\_agencies table foreign keys

| Join tax\_agencies with | on |
| --- | --- |
| [tax\_rates](#tax-rates) | ``` tax_agencies.Id = tax_rates.AgencyRef.value ``` |

tax\_agencies table schema

|  |
| --- |
| **DisplayName**  STRING |
| **Id**  STRING |
| **LastFileDate**  DATE-TIME |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **SyncToken**  STRING |
| **TaxAgencyConfig**  STRING |
| **TaxRegistrationNumber**  STRING |
| **TaxTrackedOnPurchases**  BOOLEAN |
| **TaxTrackedOnSales**  BOOLEAN |
| **domain**  STRING |

### tax\_codes

The `tax_codes` table contains info about the tax codes defined in your QuickBooks instance. **Note**: Both active and inactive tax codes are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/taxcode "Opens in new tab: QuickBooks API method") |

tax\_codes table foreign keys

| Join tax\_codes with | on |
| --- | --- |
| [estimates](#estimates) | ``` tax_codes.PurchaseTaxRateList.TaxRateDetail.TaxRateRef.value = estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value ```  ``` tax_codes.SalesTaxRateList.TaxRateDetail.TaxRateRef.value = estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value ``` |
| [invoices](#invoices) | ``` tax_codes.PurchaseTaxRateList.TaxRateDetail.TaxRateRef.value = invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ```  ``` tax_codes.SalesTaxRateList.TaxRateDetail.TaxRateRef.value = invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ``` |
| [journal\_entries](#journal-entries) | ``` tax_codes.PurchaseTaxRateList.TaxRateDetail.TaxRateRef.value = journal_entries.TaxRateRef.value ```  ``` tax_codes.SalesTaxRateList.TaxRateDetail.TaxRateRef.value = journal_entries.TaxRateRef.value ```  ``` tax_codes.PurchaseTaxRateList.TaxRateDetail.TaxRateRef.value = journal_entries.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ```  ``` tax_codes.SalesTaxRateList.TaxRateDetail.TaxRateRef.value = journal_entries.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ``` |
| [tax\_rates](#tax-rates) | ``` tax_codes.PurchaseTaxRateList.TaxRateDetail.TaxRateRef.value = tax_rates.Id ```  ``` tax_codes.SalesTaxRateList.TaxRateDetail.TaxRateRef.value = tax_rates.Id ``` |

tax\_codes table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **Description**  STRING |
| **Hidden**  BOOLEAN |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Name**  STRING |
| **PurchaseTaxRateList**  OBJECT This is a nested data structure:   - TaxRateDetail: ARRAY, which is also a nested data structure.   - TaxOrder: INTEGER   - TaxRateRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxTypeApplicable: STRING |
| **SalesTaxRateList**  OBJECT This is a nested data structure:   - TaxRateDetail: ARRAY, which is also a nested data structure.   - TaxOrder: INTEGER   - TaxRateRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxTypeApplicable: STRING |
| **SyncToken**  STRING |
| **TaxCodeConfigType**  STRING |
| **TaxGroup**  BOOLEAN |
| **Taxable**  BOOLEAN |
| **domain**  STRING |

### tax\_rates

The `tax_rates` table contains info about the tax rates defined in your QuickBooks instance. **Note**: Both active and inactive tax rates are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/taxrate)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/taxrate#query-a-taxrate "Opens in new tab: QuickBooks API method") |

tax\_rates table foreign keys

| Join tax\_rates with | on |
| --- | --- |
| [tax\_agencies](#tax-agencies) | ``` tax_rates.AgencyRef.value = tax_agencies.Id ``` |
| [estimates](#estimates) | ``` tax_rates.Id = estimates.TxnTaxDetail.TaxLine.TaxLineDetail.TaxLine.TaxLineDetail.TaxRateRef.value ``` |
| [invoices](#invoices) | ``` tax_rates.Id = invoices.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ``` |
| [journal\_entries](#journal-entries) | ``` tax_rates.Id = journal_entries.TaxRateRef.value ```  ``` tax_rates.Id = journal_entries.TxnTaxDetail.TaxLine.TaxLineDetail.TaxRateRef.value ``` |
| [tax\_codes](#tax-codes) | ``` tax_rates.Id = tax_codes.PurchaseTaxRateList.TaxRateDetail.TaxRateRef.value ```  ``` tax_rates.Id = tax_codes.SalesTaxRateList.TaxRateDetail.TaxRateRef.value ``` |

tax\_rates table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **AgencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Description**  STRING |
| **DisplayType**  STRING |
| **EffectiveTaxRate**    OBJECT  Click to expand EffectiveTaxRate  ARRAY This is a nested data structure:   - EffectiveDate: DATE-TIME - EndDate: DATE-TIME - RateValue: NUMBER |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Name**  STRING |
| **OriginalTaxRate**  STRING |
| **RateValue**  NUMBER |
| **SpecialTaxType**  STRING |
| **SyncToken**  STRING |
| **TaxReturnLineRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **domain**  STRING |

### terms

The `terms` table contains info about the sale terms defined in your QuickBooks instance. **Note**: Both active and inactive terms are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/term)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/term#query-a-term "Opens in new tab: QuickBooks API method") |

terms table foreign keys

| Join terms with | on |
| --- | --- |
| [bills](#bills) | ``` terms.Id = bills.SalesTermRef.value ``` |
| [credit\_memos](#credit-memos) | ``` terms.Id = credit_memos.SalesTermRef.value ``` |
| [customers](#customers) | ``` terms.Id = customers.SalesTermRef.value ``` |
| [estimates](#estimates) | ``` terms.Id = estimates.SalesTermRef.value ``` |
| [invoices](#invoices) | ``` terms.Id = invoices.SalesTermRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` terms.Id = purchase_orders.SalesTermRef.value ``` |

terms table schema

|  |
| --- |
| **Active**  BOOLEAN |
| **DayOfMonthDue**  INTEGER |
| **DiscountDayOfMonth**  INTEGER |
| **DiscountDays**  INTEGER |
| **DiscountPercent**  NUMBER |
| **DueDays**  INTEGER |
| **DueNextMonthDays**  INTEGER |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Name**  STRING |
| **SyncToken**  STRING |
| **Type**  STRING |
| **domain**  STRING |

### time\_activities

The `time_activities` table contains info about vendor and employee time records in your QuickBooks instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/timeactivity)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/timeactivity#query-a-timeactivity "Opens in new tab: QuickBooks API method") |

time\_activities table foreign keys

| Join time\_activities with | on |
| --- | --- |
| [budgets](#budgets) | ``` time_activities.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` time_activities.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [classes](#classes) | ``` time_activities.ClassRef.value = classes.Id ```  ``` time_activities.ClassRef.value = classes.ParentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` time_activities.ClassRef.value = credit_memos.ClassRef.value ```  ``` time_activities.ItemRef.value = credit_memos.Line.SalesItemLineDetail.ItemRef.value ``` |
| [estimates](#estimates) | ``` time_activities.ClassRef.value = estimates.ClassRef.value ```  ``` time_activities.DepartmentRef.value = estimates.DepartmentRef.value ```  ``` time_activities.ItemRef.value = estimates.Line.SalesItemLineDetail.ItemRef.value ```  ``` time_activities.Id = estimates.Id ``` |
| [invoices](#invoices) | ``` time_activities.ClassRef.value = invoices.ClassRef.value ```  ``` time_activities.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` time_activities.DepartmentRef.value = invoices.DepartmentRef.value ```  ``` time_activities.ItemRef.value = invoices.Line.SalesItemLineDetail.ItemRef.value ```  ``` time_activities.Id = invoices.LinkedTxn.TxnId ``` |
| [items](#items) | ``` time_activities.ClassRef.value = items.ClassRef.value ```  ``` time_activities.ItemRef.value = items.Id ```  ``` time_activities.ItemRef.value = items.ParentRef.value ```  ``` time_activities.VendorRef.value = items.PrefVendorRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` time_activities.ClassRef.value = purchase_orders.ClassRef.value ```  ``` time_activities.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` time_activities.DepartmentRef.value = purchase_orders.DepartmentRef.value ```  ``` time_activities.ItemRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` time_activities.VendorRef.value = purchase_orders.VendorRef.value ``` |
| [purchases](#purchases) | ``` time_activities.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` time_activities.DepartmentRef.value = purchases.DepartmentRef.value ```  ``` time_activities.EmployeeRef.value = purchases.EntityRef.value ```  ``` time_activities.ItemRef.value = purchases.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` time_activities.Id = purchases.Id ``` |
| [refund\_receipts](#refund-receipts) | ``` time_activities.ClassRef.value = refund_receipts.ClassRef.value ```  ``` time_activities.DepartmentRef.value = refund_receipts.DepartmentRef.value ```  ``` time_activities.ItemRef.value = refund_receipts.Line.SalesItemLineDetail.ItemRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` time_activities.ClassRef.value = sales_receipts.ClassRef.value ```  ``` time_activities.DepartmentRef.value = sales_receipts.DepartmentRef.value ```  ``` time_activities.ItemRef.value = sales_receipts.Line.SalesItemLineDetail.ItemRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` time_activities.ClassRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` time_activities.DepartmentRef.value = vendor_credits.DepartmentRef.value ```  ``` time_activities.VendorRef.value = vendor_credits.VendorRef.value ``` |
| [bills](#bills) | ``` time_activities.DepartmentRef.value = bills.DepartmentRef.value ```  ``` time_activities.ItemRef.value = bills.Line.ItemBasedExpenseLineDetail.ItemRef.value ```  ``` time_activities.VendorRef.value = bills.VendorRef.value ``` |
| [bill\_payments](#bill-payments) | ``` time_activities.DepartmentRef.value = bill_payments.DepartmentRef.value ```  ``` time_activities.VendorRef.value = bill_payments.VendorRef.value ``` |
| [departments](#departments) | ``` time_activities.DepartmentRef.value = departments.ParentRef.value ```  ``` time_activities.DepartmentRef.value = departments.Id ``` |
| [deposits](#deposits) | ``` time_activities.DepartmentRef.value = deposits.DepartmentRef.value ``` |
| [employees](#employees) | ``` time_activities.EmployeeRef.value = employees.Id ``` |
| [payments](#payments) | ``` time_activities.Id = payments.Id ``` |
| [vendors](#vendors) | ``` time_activities.VendorRef.value = vendors.Id ``` |

time\_activities table schema

|  |
| --- |
| **BillableStatus**  STRING |
| **BreakHours**  INTEGER |
| **BreakMinutes**  INTEGER |
| **ClassRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **CostRate**  NUMBER |
| **CustomerRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Description**  STRING |
| **EmployeeRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **EndTime**  DATE-TIME |
| **HourlyRate**  INTEGER |
| **Hours**  INTEGER |
| **Id**  STRING |
| **ItemRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **Minutes**  INTEGER |
| **NameOf**  STRING |
| **PayrollItemRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **StartTime**  DATE-TIME |
| **SyncToken**  STRING |
| **Taxable**  BOOLEAN |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **VendorRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **domain**  STRING |
| **patternProperties**  OBJECT  Click to expand patternProperties |

### transfers

The `transfers` table contains info about account transfers from your company’s QuickBooks chart of accounts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/transfer)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/transfer#query-a-transfer "Opens in new tab: QuickBooks API method") |

transfers table foreign keys

| Join transfers with | on |
| --- | --- |
| [accounts](#accounts) | ``` transfers.FromAccountRef.value = accounts.Id ```  ``` transfers.ToAccountRef.value = accounts.Id ```  ``` transfers.FromAccountRef.value = accounts.ParentRef.value ```  ``` transfers.ToAccountRef.value = accounts.ParentRef.value ```  ``` transfers.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` transfers.FromAccountRef.value = bill_payments.APAccountRef.value ```  ``` transfers.ToAccountRef.value = bill_payments.APAccountRef.value ```  ``` transfers.FromAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` transfers.ToAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` transfers.FromAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` transfers.ToAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` transfers.CurrencyRef.value = bill_payments.CurrencyRef.value ``` |
| [bills](#bills) | ``` transfers.FromAccountRef.value = bills.APAccountRef.value ```  ``` transfers.ToAccountRef.value = bills.APAccountRef.value ```  ``` transfers.FromAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` transfers.ToAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` transfers.CurrencyRef.value = bills.CurrencyRef.value ``` |
| [budgets](#budgets) | ``` transfers.FromAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` transfers.ToAccountRef.value = budgets.BudgetDetail.AccountRef.value ``` |
| [deposits](#deposits) | ``` transfers.FromAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` transfers.ToAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` transfers.FromAccountRef.value = deposits.DepositToAccountRef.value ```  ``` transfers.ToAccountRef.value = deposits.DepositToAccountRef.value ```  ``` transfers.FromAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` transfers.ToAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` transfers.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` transfers.Id = deposits.Line.LinkedTxn.TxnId ``` |
| [invoices](#invoices) | ``` transfers.FromAccountRef.value = invoices.DepositToAccountRef.value ```  ``` transfers.ToAccountRef.value = invoices.DepositToAccountRef.value ```  ``` transfers.FromAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` transfers.ToAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` transfers.CurrencyRef.value = invoices.CurrencyRef.value ``` |
| [items](#items) | ``` transfers.FromAccountRef.value = items.AssetAccountRef.value ```  ``` transfers.ToAccountRef.value = items.AssetAccountRef.value ```  ``` transfers.FromAccountRef.value = items.ExpenseAccountRef.value ```  ``` transfers.ToAccountRef.value = items.ExpenseAccountRef.value ```  ``` transfers.FromAccountRef.value = items.IncomeAccountRef.value ```  ``` transfers.ToAccountRef.value = items.IncomeAccountRef.value ``` |
| [journal\_entries](#journal-entries) | ``` transfers.FromAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` transfers.ToAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` transfers.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` transfers.Id = journal_entries.Id ``` |
| [payments](#payments) | ``` transfers.FromAccountRef.value = payments.DepositToAccountRef.value ```  ``` transfers.ToAccountRef.value = payments.DepositToAccountRef.value ```  ``` transfers.CurrencyRef.value = payments.CurrencyRef.value ```  ``` transfers.Id = payments.Id ``` |
| [purchase\_orders](#purchase-orders) | ``` transfers.FromAccountRef.value = purchase_orders.APAccountRef.value ```  ``` transfers.ToAccountRef.value = purchase_orders.APAccountRef.value ```  ``` transfers.CurrencyRef.value = purchase_orders.CurrencyRef.value ``` |
| [purchases](#purchases) | ``` transfers.FromAccountRef.value = purchases.AccountRef.value ```  ``` transfers.ToAccountRef.value = purchases.AccountRef.value ```  ``` transfers.FromAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` transfers.ToAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` transfers.CurrencyRef.value = purchases.CurrencyRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` transfers.FromAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` transfers.ToAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` transfers.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` transfers.Id = refund_receipts.Id ``` |
| [sales\_receipts](#sales-receipts) | ``` transfers.FromAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` transfers.ToAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` transfers.FromAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` transfers.ToAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` transfers.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` transfers.Id = sales_receipts.Id ``` |
| [vendor\_credits](#vendor-credits) | ``` transfers.FromAccountRef.value = vendor_credits.APAccountRef.value ```  ``` transfers.ToAccountRef.value = vendor_credits.APAccountRef.value ```  ``` transfers.FromAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` transfers.ToAccountRef.value = vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` transfers.CurrencyRef.value = vendor_credits.CurrencyRef.value ``` |
| [credit\_memos](#credit-memos) | ``` transfers.CurrencyRef.value = credit_memos.CurrencyRef.value ``` |
| [customers](#customers) | ``` transfers.CurrencyRef.value = customers.CurrencyRef.value ``` |
| [estimates](#estimates) | ``` transfers.CurrencyRef.value = estimates.CurrencyRef.value ``` |
| [vendors](#vendors) | ``` transfers.CurrencyRef.value = vendors.CurrencyRef.value ``` |

transfers table schema

|  |
| --- |
| **Amount**  NUMBER |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **ExchangeRate**  NUMBER |
| **FromAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SyncToken**  STRING |
| **ToAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **domain**  STRING |

### vendor\_credits

The `vendor_credits` table contains info about credits that a vendor owes your company.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/vendorcredit)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/vendorcredit#query-a-vendorcredit "Opens in new tab: QuickBooks API method") |

vendor\_credits table foreign keys

| Join vendor\_credits with | on |
| --- | --- |
| [accounts](#accounts) | ``` vendor_credits.APAccountRef.value = accounts.Id ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = accounts.Id ```  ``` vendor_credits.APAccountRef.value = accounts.ParentRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = accounts.ParentRef.value ```  ``` vendor_credits.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` vendor_credits.APAccountRef.value = bill_payments.APAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = bill_payments.APAccountRef.value ```  ``` vendor_credits.APAccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = bill_payments.CheckPayment.BankAccountRef.value ```  ``` vendor_credits.APAccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = bill_payments.CreditCardPayment.CCAccountRef.value ```  ``` vendor_credits.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` vendor_credits.DepartmentRef.value = bill_payments.DepartmentRef.value ```  ``` vendor_credits.Id = bill_payments.Line.LinkedTxn.TxnId ```  ``` vendor_credits.VendorRef.value = bill_payments.VendorRef.value ``` |
| [bills](#bills) | ``` vendor_credits.APAccountRef.value = bills.APAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = bills.APAccountRef.value ```  ``` vendor_credits.APAccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = bills.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` vendor_credits.CurrencyRef.value = bills.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = bills.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` vendor_credits.DepartmentRef.value = bills.DepartmentRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = bills.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = bills.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` vendor_credits.Id = bills.Id ```  ``` vendor_credits.VendorRef.value = bills.VendorRef.value ``` |
| [budgets](#budgets) | ``` vendor_credits.APAccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = budgets.BudgetDetail.AccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = budgets.BudgetDetail.ClassRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = budgets.BudgetDetail.CustomerRef.value ```  ``` vendor_credits.DepartmentRef.value = budgets.BudgetDetail.DepartmentRef.value ``` |
| [deposits](#deposits) | ``` vendor_credits.APAccountRef.value = deposits.CashBack.AccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = deposits.CashBack.AccountRef.value ```  ``` vendor_credits.APAccountRef.value = deposits.DepositToAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = deposits.DepositToAccountRef.value ```  ``` vendor_credits.APAccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = deposits.Line.DepositLineDetail.AccountRef.value ```  ``` vendor_credits.CurrencyRef.value = deposits.CurrencyRef.value ```  ``` vendor_credits.DepartmentRef.value = deposits.DepartmentRef.value ``` |
| [invoices](#invoices) | ``` vendor_credits.APAccountRef.value = invoices.DepositToAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = invoices.DepositToAccountRef.value ```  ``` vendor_credits.APAccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = invoices.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = invoices.ClassRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = invoices.Line.SalesItemLineDetail.ClassRef.value ```  ``` vendor_credits.CurrencyRef.value = invoices.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = invoices.CustomerRef.value ```  ``` vendor_credits.DepartmentRef.value = invoices.DepartmentRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = invoices.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = invoices.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [items](#items) | ``` vendor_credits.APAccountRef.value = items.AssetAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = items.AssetAccountRef.value ```  ``` vendor_credits.APAccountRef.value = items.ExpenseAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = items.ExpenseAccountRef.value ```  ``` vendor_credits.APAccountRef.value = items.IncomeAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = items.IncomeAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = items.ClassRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = items.PurchaseTaxCodeRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = items.SalesTaxCodeRef.value ```  ``` vendor_credits.VendorRef.value = items.PrefVendorRef.value ``` |
| [journal\_entries](#journal-entries) | ``` vendor_credits.APAccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = journal_entries.Line.JournalEntryLineDetail.AccountRef.value ```  ``` vendor_credits.CurrencyRef.value = journal_entries.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = journal_entries.TxnTaxDetail.TxnTaxCodeRef.value ```  ``` vendor_credits.Id = journal_entries.Id ``` |
| [payments](#payments) | ``` vendor_credits.APAccountRef.value = payments.DepositToAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = payments.DepositToAccountRef.value ```  ``` vendor_credits.CurrencyRef.value = payments.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = payments.CustomerRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` vendor_credits.APAccountRef.value = purchase_orders.APAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = purchase_orders.APAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = purchase_orders.ClassRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.ClassRef.value ```  ``` vendor_credits.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.CustomerRef.value ```  ``` vendor_credits.DepartmentRef.value = purchase_orders.DepartmentRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = purchase_orders.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ```  ``` vendor_credits.VendorRef.value = purchase_orders.VendorRef.value ``` |
| [purchases](#purchases) | ``` vendor_credits.APAccountRef.value = purchases.AccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = purchases.AccountRef.value ```  ``` vendor_credits.APAccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = purchases.Line.AccountBasedExpenseLineDetail.AccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = purchases.Line.AccountBasedExpenseLineDetail.ClassRef.value ```  ``` vendor_credits.CurrencyRef.value = purchases.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = purchases.Line.AccountBasedExpenseLineDetail.CustomerRef.value ```  ``` vendor_credits.DepartmentRef.value = purchases.DepartmentRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = purchases.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = purchases.Line.ItemBasedExpenseLineDetail.TaxCodeRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` vendor_credits.APAccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = refund_receipts.DepositToAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = refund_receipts.ClassRef.value ```  ``` vendor_credits.CurrencyRef.value = refund_receipts.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = refund_receipts.CustomerRef.value ```  ``` vendor_credits.DepartmentRef.value = refund_receipts.DepartmentRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = refund_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` vendor_credits.APAccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = sales_receipts.DepositToAccountRef.value ```  ``` vendor_credits.APAccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = sales_receipts.Line.DiscountLineDetail.DiscountAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = sales_receipts.ClassRef.value ```  ``` vendor_credits.CurrencyRef.value = sales_receipts.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = sales_receipts.CustomerRef.value ```  ``` vendor_credits.DepartmentRef.value = sales_receipts.DepartmentRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = sales_receipts.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [transfers](#transfers) | ``` vendor_credits.APAccountRef.value = transfers.FromAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = transfers.FromAccountRef.value ```  ``` vendor_credits.APAccountRef.value = transfers.ToAccountRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.AccountRef.value = transfers.ToAccountRef.value ```  ``` vendor_credits.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [classes](#classes) | ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = classes.Id ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = classes.ParentRef.value ``` |
| [credit\_memos](#credit-memos) | ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = credit_memos.ClassRef.value ```  ``` vendor_credits.CurrencyRef.value = credit_memos.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = credit_memos.CustomerRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = credit_memos.Line.SalesItemLineDetail.TaxCodeRef.value ``` |
| [estimates](#estimates) | ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = estimates.ClassRef.value ```  ``` vendor_credits.CurrencyRef.value = estimates.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = estimates.CustomerRef.value ```  ``` vendor_credits.DepartmentRef.value = estimates.DepartmentRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = estimates.Line.SalesItemLineDetail.TaxCodeRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = estimates.TxnTaxDetail.TxnTaxCodeRef.value ``` |
| [time\_activities](#time-activities) | ``` vendor_credits.Line.AccountBasedExpenseLineDetail.ClassRef.value = time_activities.ClassRef.value ```  ``` vendor_credits.DepartmentRef.value = time_activities.DepartmentRef.value ```  ``` vendor_credits.VendorRef.value = time_activities.VendorRef.value ``` |
| [customers](#customers) | ``` vendor_credits.CurrencyRef.value = customers.CurrencyRef.value ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.CustomerRef.value = customers.Id ```  ``` vendor_credits.Line.AccountBasedExpenseLineDetail.TaxCodeRef.value = customers.DefaultTaxCodeRef.value ``` |
| [vendors](#vendors) | ``` vendor_credits.CurrencyRef.value = vendors.CurrencyRef.value ```  ``` vendor_credits.VendorRef.value = vendors.Id ``` |
| [departments](#departments) | ``` vendor_credits.DepartmentRef.value = departments.ParentRef.value ```  ``` vendor_credits.DepartmentRef.value = departments.Id ``` |

vendor\_credits table schema

|  |
| --- |
| **APAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Balance**  NUMBER |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DepartmentRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DocNumber**  STRING |
| **ExchangeRate**  NUMBER |
| **GlobalTaxCalculation**  STRING |
| **Id**  STRING |
| **IncludeInAnnualTPAR**  BOOLEAN |
| **Line**  ARRAY This is a nested data structure:   - AccountBasedExpenseLineDetail: OBJECT, which is also a nested data structure.   - AccountRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - BillableStatus: STRING   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - CustomerRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - TaxAmount: NUMBER   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER - Amount: NUMBER - Description: STRING - DetailType: STRING - Id: STRING - ItemBasedExpenseLineDetail: OBJECT, which is also a nested data structure.   - BillableStatus: STRING   - ClassRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - CustomerRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - ItemRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - MarkupInfo: OBJECT, which is also a nested data structure.     - MarkUpIncomeAccountRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING     - Percent: NUMBER     - PriceLevelRef: OBJECT, which is also a nested data structure.       - name: STRING       - value: STRING   - PriceLevelRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - Qty: INTEGER   - TaxCodeRef: OBJECT, which is also a nested data structure.     - name: STRING     - value: STRING   - TaxInclusiveAmt: NUMBER   - UnitPrice: NUMBER - LineNum: INTEGER - LinkedTxn: ARRAY, which is also a nested data structure.   - TxnId: STRING   - TxnLineId: STRING   - TxnType: STRING |
| **LinkedTxn**  ARRAY This is a nested data structure:   - TxnId: STRING - TxnLineId: STRING - TxnType: STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME  Click to expand MetaData |  | | --- | | **CreateTime**  DATE-TIME | | **LastUpdatedTime**  DATE-TIME | |
| **PrivateNote**  STRING |
| **RecurDataRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **SyncToken**  STRING |
| **TotalAmt**  NUMBER |
| **TransactionLocationType**  STRING |
| **TxnDate**  DATE-TIME |
| **VendorRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **domain**  STRING |

### vendors

The `vendors` table contains info about the sellers your company purchases products from. **Note**: Both active and inactive vendors are included in the data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Useful links** | [QuickBooks documentation](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/vendor)  [QuickBooks API method](https://developer.intuit.com/app/developer/qbo/Content/api/accounting/all-entities/vendor#query-a-vendor "Opens in new tab: QuickBooks API method") |

vendors table foreign keys

| Join vendors with | on |
| --- | --- |
| [accounts](#accounts) | ``` vendors.CurrencyRef.value = accounts.CurrencyRef.value ``` |
| [bill\_payments](#bill-payments) | ``` vendors.CurrencyRef.value = bill_payments.CurrencyRef.value ```  ``` vendors.Id = bill_payments.VendorRef.value ``` |
| [bills](#bills) | ``` vendors.CurrencyRef.value = bills.CurrencyRef.value ```  ``` vendors.Id = bills.VendorRef.value ``` |
| [credit\_memos](#credit-memos) | ``` vendors.CurrencyRef.value = credit_memos.CurrencyRef.value ``` |
| [customers](#customers) | ``` vendors.CurrencyRef.value = customers.CurrencyRef.value ``` |
| [deposits](#deposits) | ``` vendors.CurrencyRef.value = deposits.CurrencyRef.value ``` |
| [estimates](#estimates) | ``` vendors.CurrencyRef.value = estimates.CurrencyRef.value ``` |
| [invoices](#invoices) | ``` vendors.CurrencyRef.value = invoices.CurrencyRef.value ``` |
| [journal\_entries](#journal-entries) | ``` vendors.CurrencyRef.value = journal_entries.CurrencyRef.value ``` |
| [payments](#payments) | ``` vendors.CurrencyRef.value = payments.CurrencyRef.value ``` |
| [purchase\_orders](#purchase-orders) | ``` vendors.CurrencyRef.value = purchase_orders.CurrencyRef.value ```  ``` vendors.Id = purchase_orders.VendorRef.value ``` |
| [purchases](#purchases) | ``` vendors.CurrencyRef.value = purchases.CurrencyRef.value ``` |
| [refund\_receipts](#refund-receipts) | ``` vendors.CurrencyRef.value = refund_receipts.CurrencyRef.value ``` |
| [sales\_receipts](#sales-receipts) | ``` vendors.CurrencyRef.value = sales_receipts.CurrencyRef.value ``` |
| [transfers](#transfers) | ``` vendors.CurrencyRef.value = transfers.CurrencyRef.value ``` |
| [vendor\_credits](#vendor-credits) | ``` vendors.CurrencyRef.value = vendor_credits.CurrencyRef.value ```  ``` vendors.Id = vendor_credits.VendorRef.value ``` |
| [items](#items) | ``` vendors.Id = items.PrefVendorRef.value ``` |
| [time\_activities](#time-activities) | ``` vendors.Id = time_activities.VendorRef.value ``` |

vendors table schema

|  |
| --- |
| **APAccountRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **AcctNum**  STRING |
| **Active**  BOOLEAN |
| **AlternatePhone**  OBJECT This is a nested data structure:   - FreeFormNumber: STRING |
| **Balance**  NUMBER |
| **BillAddr**  OBJECT This is a nested data structure:   - City: STRING - Country: STRING - CountrySubDivisionCode: STRING - Id: STRING - Lat: STRING - Line1: STRING - Line2: STRING - Line3: STRING - Line4: STRING - Line5: STRING - Long: STRING - PostalCode: STRING |
| **BillRate**  NUMBER |
| **BusinessNumber**  STRING |
| **CompanyName**  STRING |
| **CostRate**  NUMBER |
| **CurrencyRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **DisplayName**  STRING |
| **FamilyName**  STRING |
| **Fax**  OBJECT This is a nested data structure:   - FreeFormNumber: STRING |
| **GSTIN**  STRING |
| **GSTRegistrationType**  STRING |
| **GivenName**  STRING |
| **HasTPAR**  BOOLEAN |
| **Id**  STRING |
| **MetaData**  OBJECT This is a nested data structure:   - CreateTime: DATE-TIME - LastUpdatedTime: DATE-TIME |
| **MiddleName**  STRING |
| **Mobile**  OBJECT This is a nested data structure:   - FreeFormNumber: STRING |
| **OtherContactInfo**  OBJECT This is a nested data structure:   - Type: STRING |
| **PrimaryEmailAddr**  OBJECT This is a nested data structure:   - Address: STRING |
| **PrimaryPhone**  OBJECT This is a nested data structure:   - FreeFormNumber: STRING |
| **PrintOnCheckName**  STRING |
| **Source**  STRING |
| **Suffix**  STRING |
| **SyncToken**  STRING |
| **T4AEligible**  BOOLEAN |
| **T5018Eligible**  BOOLEAN |
| **TaxIdentifier**  STRING |
| **TaxReportingBasis**  STRING |
| **TermRef**  OBJECT This is a nested data structure:   - name: STRING - value: STRING |
| **Title**  STRING |
| **Vendor1099**  BOOLEAN |
| **VendorPaymentBankDetail**  OBJECT This is a nested data structure:   - BankAccountName: STRING - BankAccountNumber: STRING - BankBranchIdentifier: STRING - StatementText: STRING |
| **WebAddr**  OBJECT This is a nested data structure:   - URI: STRING |
| **domain**  STRING |
| **patternProperties**  OBJECT  Click to expand patternProperties |
