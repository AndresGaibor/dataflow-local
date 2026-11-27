---
title: "Xero"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Xero.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Xero

Xero is an online accounting software for small businesses, automating invoicing, bank reconciliations, and reporting.

Xero integration replicates data using the [Xero Accounting API](https://developer.xero.com/documentation/api/api-overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To connect to the Xero integration, you need to have your client ID, client secret, user ID, and tenant ID. Follow the procedures below to copy each setting.

To obtain your client ID and secret:

1. Log into your [Xero](https://developer.xero.com/app/manage) account.
2. Create a new app.
3. Click Configuration on the left. The client ID and secret are displayed.
4. As the client secret is displayed only once, copy and paste it to a secured file. Otherwise, you have to create a new app.
5. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.

To obtain your user ID:

1. Log into your [Xero](https://go.xero.com/Settings/OrganisationSettings) account.
2. Select the organization in the drop-down list in the top-left corner.
3. Select User from the menu.
4. Select the user account you want to use.

   The user ID is part of the URL `https://go.xero.com/app/.../settings/users/edit?userId=%7BTHIS_IS_THE_USER_ID%7D)`.

To obtain your tenant ID:

1. Log into your [Xero](https://api-explorer.xero.com) account.
2. To display the tenant ID, select Show auto-generated headers.

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
| Include Archived Contacts | Select the check box to include archive contacts. |
| Client ID | Client ID. |
| Access Token | Access token. |
| Organization Name | Organization name. |
| Xero User ID | Xero user ID. |
| Tenant ID | Tenant ID. |

## Schema

Information note

**Schemas and versioning**

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

### accounts

The `accounts` table contains info about the various accounts (ex: banking) connected to your Xero account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | AccountID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/accounts "Opens in new tab: Xero API method") |

accounts table foreign keys

| Join accounts with | on |
| --- | --- |
| [bank\_transactions](#bank-transactions) | ``` accounts.AccountID = bank_transactions.BankAccount.AccountID ```  ``` accounts.CurrencyCode = bank_transactions.CurrencyCode ``` |
| [bank\_transfers](#bank-transfers) | ``` accounts.AccountID = bank_transfers.FromBankAccount.AccountID ```  ``` accounts.AccountID = bank_transfers.ToBankAccount.AccountID ``` |
| [journals](#journals) | ``` accounts.AccountID = journals.JournalLines.AccountID ``` |
| [payments](#payments) | ``` accounts.AccountID = payments.Account.AccountID ``` |
| [credit\_notes](#credit-notes) | ``` accounts.CurrencyCode = credit_notes.CurrencyCode ``` |
| [currencies](#currencies) | ``` accounts.CurrencyCode = currencies.Code ``` |
| [invoices](#invoices) | ``` accounts.CurrencyCode = invoices.CurrencyCode ``` |
| [prepayments](#prepayments) | ``` accounts.CurrencyCode = prepayments.CurrencyCode ``` |
| [purchase\_orders](#purchase-orders) | ``` accounts.CurrencyCode = purchase_orders.CurrencyCode ``` |
| [repeating\_invoices](#repeating-invoices) | ``` accounts.CurrencyCode = repeating_invoices.CurrencyCode ``` |

accounts table schema

|  |
| --- |
| **AccountID**  STRING |
| **BankAccountNumber**  STRING |
| **BankAccountType**  STRING |
| **Class**  STRING |
| **Code**  STRING |
| **CurrencyCode**  STRING |
| **Description**  STRING |
| **EnablePaymentsToAccount**  BOOLEAN |
| **HasAttachments**  BOOLEAN |
| **Name**  STRING |
| **ReportingCode**  STRING |
| **ReportingCodeName**  STRING |
| **ShowInExpenseClaims**  BOOLEAN |
| **Status**  STRING |
| **SystemAccount**  STRING |
| **TaxType**  STRING |
| **Type**  STRING |
| **UpdatedDateUTC**  DATE-TIME |

### bank\_transactions

The `bank_transactions` table contains info about the bank transactions in your Xero account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | BankTransactionID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/banktransactions "Opens in new tab: Xero API method") |

bank\_transactions table foreign keys

| Join bank\_transactions with | on |
| --- | --- |
| [accounts](#accounts) | ``` bank_transactions.BankAccount.AccountID = accounts.AccountID ```  ``` bank_transactions.CurrencyCode = accounts.CurrencyCode ``` |
| [bank\_transfers](#bank-transfers) | ``` bank_transactions.BankAccount.AccountID = bank_transfers.FromBankAccount.AccountID ```  ``` bank_transactions.BankAccount.AccountID = bank_transfers.ToBankAccount.AccountID ``` |
| [journals](#journals) | ``` bank_transactions.BankAccount.AccountID = journals.JournalLines.AccountID ``` |
| [payments](#payments) | ``` bank_transactions.BankAccount.AccountID = payments.Account.AccountID ```  ``` bank_transactions.OverpaymentID = payments.Overpayment.OverpaymentID ```  ``` bank_transactions.PrepaymentID = payments.Prepayments.PrepaymentID ``` |
| [linked\_transactions](#linked-transactions) | ``` bank_transactions.BankTransactionID = linked_transactions.SourceTransactionID ``` |
| [credit\_notes](#credit-notes) | ``` bank_transactions.CurrencyCode = credit_notes.CurrencyCode ``` |
| [currencies](#currencies) | ``` bank_transactions.CurrencyCode = currencies.Code ``` |
| [invoices](#invoices) | ``` bank_transactions.CurrencyCode = invoices.CurrencyCode ```  ``` bank_transactions.OverpaymentID = invoices.Overpayments.Overpayment.OverpaymentID ```  ``` bank_transactions.PrepaymentID = invoices.Prepayments.PrepaymentID ```  ``` bank_transactions.BankTransactionID = invoices.InvoiceID ``` |
| [prepayments](#prepayments) | ``` bank_transactions.CurrencyCode = prepayments.CurrencyCode ```  ``` bank_transactions.PrepaymentID = prepayments.PrepaymentID ``` |
| [purchase\_orders](#purchase-orders) | ``` bank_transactions.CurrencyCode = purchase_orders.CurrencyCode ``` |
| [repeating\_invoices](#repeating-invoices) | ``` bank_transactions.CurrencyCode = repeating_invoices.CurrencyCode ``` |
| [overpayments](#overpayments) | ``` bank_transactions.OverpaymentID = overpayments.OverpaymentID ``` |

bank\_transactions table schema

|  |
| --- |
| **BankAccount**  OBJECT This is a nested data structure:   - AccountID: STRING - BankAccountNumber: STRING - BankAccountType: STRING - Class: STRING - Code: STRING - CurrencyCode: STRING - Description: STRING - EnablePaymentsToAccount: BOOLEAN - HasAttachments: BOOLEAN - Name: STRING - ReportingCode: STRING - ReportingCodeName: STRING - ShowInExpenseClaims: BOOLEAN - Status: STRING - SystemAccount: STRING - TaxType: STRING - Type: STRING - UpdatedDateUTC: DATE-TIME |
| **BankTransactionID**  STRING |
| **Contact**  OBJECT This is a nested data structure:   - AccountNumber: STRING - AccountsPayableTaxType: STRING - AccountsReceivableTaxType: STRING - Addresses: ARRAY, which is also a nested data structure.   - AddressLine1: STRING   - AddressLine2: STRING   - AddressLine3: STRING   - AddressLine4: STRING   - AddressType: STRING   - AttentionTo: STRING   - City: STRING   - Country: STRING   - PostalCode: STRING   - Region: STRING - Attachments: ARRAY - Balances: OBJECT, which is also a nested data structure.   - AccountsPayable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER   - AccountsReceivable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER - BankAccountDetails: STRING - BatchPayments: OBJECT, which is also a nested data structure.   - BankAccountName: STRING   - BankAccountNumber: STRING   - Code: STRING   - Details: STRING   - Reference: STRING - BrandingTheme: OBJECT, which is also a nested data structure.   - BrandingThemeID: STRING   - CreatedDateUTC: DATE-TIME   - Name: STRING   - SortOrder: INTEGER - ContactGroups: ARRAY, which is also a nested data structure.   - ContactGroupID: STRING   - HasValidationErrors: BOOLEAN   - Name: STRING   - Status: STRING - ContactID: STRING - ContactNumber: STRING - ContactPersons: ARRAY, which is also a nested data structure.   - EmailAddress: STRING   - FirstName: STRING   - IncludeInEmails: BOOLEAN   - LastName: STRING - ContactStatus: STRING - DefaultCurrency: STRING - Discount: NUMBER - EmailAddress: STRING - FirstName: STRING - HasAttachments: BOOLEAN - HasValidationErrors: BOOLEAN - IsCustomer: BOOLEAN - IsSupplier: BOOLEAN - LastName: STRING - Name: STRING - PaymentTerms: OBJECT, which is also a nested data structure.   - Bills: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING   - Sales: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING - Phones: ARRAY, which is also a nested data structure.   - PhoneAreaCode: STRING   - PhoneCountryCode: STRING   - PhoneNumber: STRING   - PhoneType: STRING - PurchasesDefaultAccountCode: STRING - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SalesDefaultAccountCode: STRING - SalesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SkypeUserName: STRING - TaxNumber: STRING - TrackingCategoryName: STRING - TrackingCategoryOption: STRING - UpdatedDateUTC: DATE-TIME - ValidationErrors: ARRAY, which is also a nested data structure.   - Message: STRING - Website: STRING - XeroNetworkKey: STRING |
| **CurrencyCode**  STRING |
| **CurrencyRate**  NUMBER |
| **Date**  DATE-TIME |
| **DateString**  DATE-TIME |
| **ExternalLinkProviderName**  STRING |
| **HasAttachments**  BOOLEAN |
| **IsReconciled**  BOOLEAN |
| **LineAmountTypes**  STRING |
| **LineItems**  ARRAY This is a nested data structure:   - AccountCode: STRING - Description: STRING - DiscountRate: NUMBER - ItemCode: STRING - LineAmount: NUMBER - LineItemID: STRING - Quantity: NUMBER - TaxAmount: NUMBER - TaxType: STRING - Tracking: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - UnitAmount: NUMBER |
| **OverpaymentID**  STRING |
| **PrepaymentID**  STRING |
| **Reference**  STRING |
| **Status**  STRING |
| **SubTotal**  NUMBER |
| **Total**  NUMBER |
| **TotalTax**  NUMBER |
| **Type**  STRING |
| **UpdatedDateUTC**  DATE-TIME |
| **Url**  STRING |

### bank\_transfers

The `bank_transfers` table contains info about bank transfers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | BankTransferID |
| **Replication Key** | CreatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/bank-transfers "Opens in new tab: Xero API method") |

bank\_transfers table foreign keys

| Join bank\_transfers with | on |
| --- | --- |
| [accounts](#accounts) | ``` bank_transfers.FromBankAccount.AccountID = accounts.AccountID ```  ``` bank_transfers.ToBankAccount.AccountID = accounts.AccountID ``` |
| [bank\_transactions](#bank-transactions) | ``` bank_transfers.FromBankAccount.AccountID = bank_transactions.BankAccount.AccountID ```  ``` bank_transfers.ToBankAccount.AccountID = bank_transactions.BankAccount.AccountID ``` |
| [journals](#journals) | ``` bank_transfers.FromBankAccount.AccountID = journals.JournalLines.AccountID ```  ``` bank_transfers.ToBankAccount.AccountID = journals.JournalLines.AccountID ``` |
| [payments](#payments) | ``` bank_transfers.FromBankAccount.AccountID = payments.Account.AccountID ```  ``` bank_transfers.ToBankAccount.AccountID = payments.Account.AccountID ``` |

bank\_transfers table schema

|  |
| --- |
| **Amount**  NUMBER |
| **BankTransferID**  STRING |
| **CreatedDateUTC**  DATE-TIME |
| **CreatedDateUTCString**  DATE-TIME |
| **CurrencyRate**  NUMBER |
| **Date**  DATE-TIME |
| **DateString**  DATE-TIME |
| **FromBankAccount**  OBJECT This is a nested data structure:   - AccountID: STRING - BankAccountNumber: STRING - BankAccountType: STRING - Class: STRING - Code: STRING - CurrencyCode: STRING - Description: STRING - EnablePaymentsToAccount: BOOLEAN - HasAttachments: BOOLEAN - Name: STRING - ReportingCode: STRING - ReportingCodeName: STRING - ShowInExpenseClaims: BOOLEAN - Status: STRING - SystemAccount: STRING - TaxType: STRING - Type: STRING - UpdatedDateUTC: DATE-TIME |
| **FromBankTransactionID**  STRING |
| **HasAttachments**  BOOLEAN |
| **ToBankAccount**  OBJECT This is a nested data structure:   - AccountID: STRING - BankAccountNumber: STRING - BankAccountType: STRING - Class: STRING - Code: STRING - CurrencyCode: STRING - Description: STRING - EnablePaymentsToAccount: BOOLEAN - HasAttachments: BOOLEAN - Name: STRING - ReportingCode: STRING - ReportingCodeName: STRING - ShowInExpenseClaims: BOOLEAN - Status: STRING - SystemAccount: STRING - TaxType: STRING - Type: STRING - UpdatedDateUTC: DATE-TIME |
| **ToBankTransactionID**  STRING |

### branding\_themes

The `branding_themes` table contains info about your branding themes. A branding theme is customization you can apply to customer-facing documents such as invoices, statements, quotes, etc.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | BrandingThemeID |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/branding-themes "Opens in new tab: Xero API method") |

branding\_themes table foreign keys

| Join branding\_themes with | on |
| --- | --- |
| [contacts](#contacts) | ``` branding_themes.BrandingThemeID = contacts.BrandingTheme.BrandingThemeID ``` |
| [credit\_notes](#credit-notes) | ``` branding_themes.BrandingThemeID = credit_notes.BrandingThemeID ``` |
| [invoices](#invoices) | ``` branding_themes.BrandingThemeID = invoices.BrandingThemeID ``` |
| [purchase\_orders](#purchase-orders) | ``` branding_themes.BrandingThemeID = purchase_orders.BrandingThemeID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` branding_themes.BrandingThemeID = repeating_invoices.BrandingThemeID ``` |

branding\_themes table schema

|  |
| --- |
| **BrandingThemeID**  STRING |
| **CreatedDateUTC**  DATE-TIME |
| **Name**  STRING |
| **SortOrder**  INTEGER |

### contact\_groups

The `contact_groups` table contains info about your contact groups. A contact group is a group of contacts that have something in common.

**Note**: Due to the limits of Xero’s API, only active contact groups (`Status: ACTIVE`) may be retrieved.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | ContactGroupID |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/contactgroups "Opens in new tab: Xero API method") |

contact\_groups table foreign keys

| Join contact\_groups with | on |
| --- | --- |
| [contacts](#contacts) | ``` contact_groups.ContactGroupID = contacts.ContactGroups.ContactGroupID ``` |

contact\_groups table schema

|  |
| --- |
| **ContactGroupID**  STRING |
| **HasValidationErrors**  BOOLEAN |
| **Name**  STRING |
| **Status**  STRING |

### contacts

The `contacts` table contains info about the customers and suppliers you do business with.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ContactID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/contacts "Opens in new tab: Xero API method") |

contacts table foreign keys

| Join contacts with | on |
| --- | --- |
| [branding\_themes](#branding-themes) | ``` contacts.BrandingTheme.BrandingThemeID = branding_themes.BrandingThemeID ``` |
| [credit\_notes](#credit-notes) | ``` contacts.BrandingTheme.BrandingThemeID = credit_notes.BrandingThemeID ```  ``` contacts.ContactID = credit_notes.Contact.ContactID ```  ``` contacts.SalesTrackingCategories.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ```  ``` contacts.PurchasesTrackingCategories.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ``` |
| [invoices](#invoices) | ``` contacts.BrandingTheme.BrandingThemeID = invoices.BrandingThemeID ```  ``` contacts.ContactID = invoices.Contact.ContactID ```  ``` contacts.SalesTrackingCategories.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ```  ``` contacts.PurchasesTrackingCategories.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [purchase\_orders](#purchase-orders) | ``` contacts.BrandingTheme.BrandingThemeID = purchase_orders.BrandingThemeID ```  ``` contacts.SalesTrackingCategories.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ```  ``` contacts.PurchasesTrackingCategories.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` contacts.BrandingTheme.BrandingThemeID = repeating_invoices.BrandingThemeID ```  ``` contacts.ContactID = repeating_invoices.Contact.ContactID ```  ``` contacts.SalesTrackingCategories.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ```  ``` contacts.PurchasesTrackingCategories.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [contact\_groups](#contact-groups) | ``` contacts.ContactGroups.ContactGroupID = contact_groups.ContactGroupID ``` |
| [linked\_transactions](#linked-transactions) | ``` contacts.ContactID = linked_transactions.ContactID ``` |
| [overpayments](#overpayments) | ``` contacts.ContactID = overpayments.Contact.ContactID ```  ``` contacts.SalesTrackingCategories.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ```  ``` contacts.PurchasesTrackingCategories.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ``` |
| [prepayments](#prepayments) | ``` contacts.ContactID = prepayments.Contact.ContactID ```  ``` contacts.SalesTrackingCategories.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ```  ``` contacts.PurchasesTrackingCategories.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ``` |
| [receipts](#receipts) | ``` contacts.ContactID = receipts.Contact.ContactID ```  ``` contacts.SalesTrackingCategories.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ```  ``` contacts.PurchasesTrackingCategories.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ``` |
| [journals](#journals) | ``` contacts.SalesTrackingCategories.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ```  ``` contacts.PurchasesTrackingCategories.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ``` |
| [manual\_journals](#manual-journals) | ``` contacts.SalesTrackingCategories.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ```  ``` contacts.PurchasesTrackingCategories.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ``` |
| [tracking\_categories](#tracking-categories) | ``` contacts.SalesTrackingCategories.TrackingCategoryID = tracking_categories.TrackingCategoryID ```  ``` contacts.PurchasesTrackingCategories.TrackingCategoryID = tracking_categories.TrackingCategoryID ``` |

contacts table schema

|  |
| --- |
| **AccountNumber**  STRING |
| **AccountsPayableTaxType**  STRING |
| **AccountsReceivableTaxType**  STRING |
| **Addresses**  ARRAY This is a nested data structure:   - AddressLine1: STRING - AddressLine2: STRING - AddressLine3: STRING - AddressLine4: STRING - AddressType: STRING - AttentionTo: STRING - City: STRING - Country: STRING - PostalCode: STRING - Region: STRING |
| **Attachments**  ARRAY |
| **Balances**  OBJECT This is a nested data structure:   - AccountsPayable: OBJECT, which is also a nested data structure.   - Outstanding: NUMBER   - Overdue: NUMBER - AccountsReceivable: OBJECT, which is also a nested data structure.   - Outstanding: NUMBER   - Overdue: NUMBER |
| **BankAccountDetails**  STRING |
| **BatchPayments**  OBJECT This is a nested data structure:   - BankAccountName: STRING - BankAccountNumber: STRING - Code: STRING - Details: STRING - Reference: STRING |
| **BrandingTheme**  OBJECT This is a nested data structure:   - BrandingThemeID: STRING - CreatedDateUTC: DATE-TIME - Name: STRING - SortOrder: INTEGER |
| **ContactGroups**  ARRAY This is a nested data structure:   - ContactGroupID: STRING - HasValidationErrors: BOOLEAN - Name: STRING - Status: STRING |
| **ContactID**  STRING |
| **ContactNumber**  STRING |
| **ContactPersons**  ARRAY This is a nested data structure:   - EmailAddress: STRING - FirstName: STRING - IncludeInEmails: BOOLEAN - LastName: STRING |
| **ContactStatus**  STRING |
| **DefaultCurrency**  STRING |
| **Discount**  NUMBER |
| **EmailAddress**  STRING |
| **FirstName**  STRING |
| **HasAttachments**  BOOLEAN |
| **HasValidationErrors**  BOOLEAN |
| **IsCustomer**  BOOLEAN |
| **IsSupplier**  BOOLEAN |
| **LastName**  STRING |
| **Name**  STRING |
| **PaymentTerms**  OBJECT This is a nested data structure:   - Bills: OBJECT, which is also a nested data structure.   - Day: INTEGER   - Type: STRING - Sales: OBJECT, which is also a nested data structure.   - Day: INTEGER   - Type: STRING |
| **Phones**  ARRAY This is a nested data structure:   - PhoneAreaCode: STRING - PhoneCountryCode: STRING - PhoneNumber: STRING - PhoneType: STRING |
| **PurchasesDefaultAccountCode**  STRING |
| **PurchasesTrackingCategories**  ARRAY This is a nested data structure:   - Name: STRING - Option: STRING - Options: ARRAY, which is also a nested data structure.   - HasValidationErrors: BOOLEAN   - IsActive: BOOLEAN   - IsArchived: BOOLEAN   - IsDeleted: BOOLEAN   - Name: STRING   - Status: STRING   - TrackingOptionID: STRING - Status: STRING - TrackingCategoryID: STRING - TrackingCategoryName: STRING - TrackingOptionID: STRING - TrackingOptionName: STRING |
| **SalesDefaultAccountCode**  STRING |
| **SalesTrackingCategories**  ARRAY This is a nested data structure:   - Name: STRING - Option: STRING - Options: ARRAY, which is also a nested data structure.   - HasValidationErrors: BOOLEAN   - IsActive: BOOLEAN   - IsArchived: BOOLEAN   - IsDeleted: BOOLEAN   - Name: STRING   - Status: STRING   - TrackingOptionID: STRING - Status: STRING - TrackingCategoryID: STRING - TrackingCategoryName: STRING - TrackingOptionID: STRING - TrackingOptionName: STRING |
| **SkypeUserName**  STRING |
| **TaxNumber**  STRING |
| **TrackingCategoryName**  STRING |
| **TrackingCategoryOption**  STRING |
| **UpdatedDateUTC**  DATE-TIME |
| **ValidationErrors**  ARRAY This is a nested data structure:   - Message: STRING |
| **Website**  STRING |
| **XeroNetworkKey**  STRING |

### credit\_notes

The `credit_notes` table contains info about credit notes. A credit note is similar to an invoice, except it reduces the amount you owe a supplier or the amount a customer owes you.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | CreditNoteID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/credit-notes "Opens in new tab: Xero API method") |

credit\_notes table foreign keys

| Join credit\_notes with | on |
| --- | --- |
| [branding\_themes](#branding-themes) | ``` credit_notes.BrandingThemeID = branding_themes.BrandingThemeID ``` |
| [contacts](#contacts) | ``` credit_notes.BrandingThemeID = contacts.BrandingTheme.BrandingThemeID ```  ``` credit_notes.Contact.ContactID = contacts.ContactID ```  ``` credit_notes.LineItems.Tracking.TrackingCategoryID = contacts.SalesTrackingCategories.TrackingCategoryID ```  ``` credit_notes.LineItems.Tracking.TrackingCategoryID = contacts.PurchasesTrackingCategories.TrackingCategoryID ``` |
| [invoices](#invoices) | ``` credit_notes.BrandingThemeID = invoices.BrandingThemeID ```  ``` credit_notes.Contact.ContactID = invoices.Contact.ContactID ```  ``` credit_notes.CreditNoteID = invoices.CreditNotes.CreditNoteID ```  ``` credit_notes.CurrencyCode = invoices.CurrencyCode ```  ``` credit_notes.LineItems.Tracking.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [purchase\_orders](#purchase-orders) | ``` credit_notes.BrandingThemeID = purchase_orders.BrandingThemeID ```  ``` credit_notes.CurrencyCode = purchase_orders.CurrencyCode ```  ``` credit_notes.LineItems.Tracking.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` credit_notes.BrandingThemeID = repeating_invoices.BrandingThemeID ```  ``` credit_notes.Contact.ContactID = repeating_invoices.Contact.ContactID ```  ``` credit_notes.CurrencyCode = repeating_invoices.CurrencyCode ```  ``` credit_notes.LineItems.Tracking.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [linked\_transactions](#linked-transactions) | ``` credit_notes.Contact.ContactID = linked_transactions.ContactID ``` |
| [overpayments](#overpayments) | ``` credit_notes.Contact.ContactID = overpayments.Contact.ContactID ```  ``` credit_notes.LineItems.Tracking.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ``` |
| [prepayments](#prepayments) | ``` credit_notes.Contact.ContactID = prepayments.Contact.ContactID ```  ``` credit_notes.CurrencyCode = prepayments.CurrencyCode ```  ``` credit_notes.LineItems.Tracking.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ``` |
| [receipts](#receipts) | ``` credit_notes.Contact.ContactID = receipts.Contact.ContactID ```  ``` credit_notes.LineItems.Tracking.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ``` |
| [accounts](#accounts) | ``` credit_notes.CurrencyCode = accounts.CurrencyCode ``` |
| [bank\_transactions](#bank-transactions) | ``` credit_notes.CurrencyCode = bank_transactions.CurrencyCode ``` |
| [currencies](#currencies) | ``` credit_notes.CurrencyCode = currencies.Code ``` |
| [journals](#journals) | ``` credit_notes.LineItems.Tracking.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ``` |
| [manual\_journals](#manual-journals) | ``` credit_notes.LineItems.Tracking.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ``` |
| [tracking\_categories](#tracking-categories) | ``` credit_notes.LineItems.Tracking.TrackingCategoryID = tracking_categories.TrackingCategoryID ``` |

credit\_notes table schema

|  |
| --- |
| **Allocations**  ARRAY This is a nested data structure:   - Amount: NUMBER - Date: DATE-TIME - Invoice: OBJECT, which is also a nested data structure.   - AmountCredited: NUMBER   - AmountDue: NUMBER   - AmountPaid: NUMBER   - BrandingThemeID: STRING   - Contact: OBJECT, which is also a nested data structure.     - AccountNumber: STRING     - AccountsPayableTaxType: STRING     - AccountsReceivableTaxType: STRING     - Addresses: ARRAY, which is also a nested data structure.       - AddressLine1: STRING       - AddressLine2: STRING       - AddressLine3: STRING       - AddressLine4: STRING       - AddressType: STRING       - AttentionTo: STRING       - City: STRING       - Country: STRING       - PostalCode: STRING       - Region: STRING     - Attachments: ARRAY     - Balances: OBJECT, which is also a nested data structure.       - AccountsPayable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER       - AccountsReceivable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER     - BankAccountDetails: STRING     - BatchPayments: OBJECT, which is also a nested data structure.       - BankAccountName: STRING       - BankAccountNumber: STRING       - Code: STRING       - Details: STRING       - Reference: STRING     - BrandingTheme: OBJECT, which is also a nested data structure.       - BrandingThemeID: STRING       - CreatedDateUTC: DATE-TIME       - Name: STRING       - SortOrder: INTEGER     - ContactGroups: ARRAY, which is also a nested data structure.       - ContactGroupID: STRING       - HasValidationErrors: BOOLEAN       - Name: STRING       - Status: STRING     - ContactID: STRING     - ContactNumber: STRING     - ContactPersons: ARRAY, which is also a nested data structure.       - EmailAddress: STRING       - FirstName: STRING       - IncludeInEmails: BOOLEAN       - LastName: STRING     - ContactStatus: STRING     - DefaultCurrency: STRING     - Discount: NUMBER     - EmailAddress: STRING     - FirstName: STRING     - HasAttachments: BOOLEAN     - HasValidationErrors: BOOLEAN     - IsCustomer: BOOLEAN     - IsSupplier: BOOLEAN     - LastName: STRING     - Name: STRING     - PaymentTerms: OBJECT, which is also a nested data structure.       - Bills: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING       - Sales: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING     - Phones: ARRAY, which is also a nested data structure.       - PhoneAreaCode: STRING       - PhoneCountryCode: STRING       - PhoneNumber: STRING       - PhoneType: STRING     - PurchasesDefaultAccountCode: STRING     - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SalesDefaultAccountCode: STRING     - SalesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SkypeUserName: STRING     - TaxNumber: STRING     - TrackingCategoryName: STRING     - TrackingCategoryOption: STRING     - UpdatedDateUTC: DATE-TIME     - ValidationErrors: ARRAY, which is also a nested data structure.       - Message: STRING     - Website: STRING     - XeroNetworkKey: STRING   - CurrencyCode: STRING   - CurrencyRate: NUMBER   - Date: DATE-TIME   - DateString: DATE-TIME   - DueDate: DATE-TIME   - DueDateString: DATE-TIME   - ExpectedPaymentDate: DATE-TIME   - FullyPaidOnDate: DATE-TIME   - HasAttachments: BOOLEAN   - HasErrors: BOOLEAN   - InvoiceID: STRING   - InvoiceNumber: STRING   - IsDiscounted: BOOLEAN   - LineAmountTypes: STRING   - LineItems: ARRAY, which is also a nested data structure.     - AccountCode: STRING     - Description: STRING     - DiscountRate: NUMBER     - ItemCode: STRING     - LineAmount: NUMBER     - LineItemID: STRING     - Quantity: NUMBER     - TaxAmount: NUMBER     - TaxType: STRING     - Tracking: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - UnitAmount: NUMBER   - PlannedPaymentDate: DATE-TIME   - Reference: STRING   - SentToContact: BOOLEAN   - Status: STRING   - SubTotal: NUMBER   - Total: NUMBER   - TotalDiscount: NUMBER   - TotalTax: NUMBER   - Type: STRING   - UpdatedDateUTC: DATE-TIME   - Url: STRING |
| **AppliedAmount**  NUMBER |
| **BrandingThemeID**  STRING |
| **Contact**  OBJECT This is a nested data structure:   - AccountNumber: STRING - AccountsPayableTaxType: STRING - AccountsReceivableTaxType: STRING - Addresses: ARRAY, which is also a nested data structure.   - AddressLine1: STRING   - AddressLine2: STRING   - AddressLine3: STRING   - AddressLine4: STRING   - AddressType: STRING   - AttentionTo: STRING   - City: STRING   - Country: STRING   - PostalCode: STRING   - Region: STRING - Attachments: ARRAY - Balances: OBJECT, which is also a nested data structure.   - AccountsPayable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER   - AccountsReceivable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER - BankAccountDetails: STRING - BatchPayments: OBJECT, which is also a nested data structure.   - BankAccountName: STRING   - BankAccountNumber: STRING   - Code: STRING   - Details: STRING   - Reference: STRING - BrandingTheme: OBJECT, which is also a nested data structure.   - BrandingThemeID: STRING   - CreatedDateUTC: DATE-TIME   - Name: STRING   - SortOrder: INTEGER - ContactGroups: ARRAY, which is also a nested data structure.   - ContactGroupID: STRING   - HasValidationErrors: BOOLEAN   - Name: STRING   - Status: STRING - ContactID: STRING - ContactNumber: STRING - ContactPersons: ARRAY, which is also a nested data structure.   - EmailAddress: STRING   - FirstName: STRING   - IncludeInEmails: BOOLEAN   - LastName: STRING - ContactStatus: STRING - DefaultCurrency: STRING - Discount: NUMBER - EmailAddress: STRING - FirstName: STRING - HasAttachments: BOOLEAN - HasValidationErrors: BOOLEAN - IsCustomer: BOOLEAN - IsSupplier: BOOLEAN - LastName: STRING - Name: STRING - PaymentTerms: OBJECT, which is also a nested data structure.   - Bills: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING   - Sales: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING - Phones: ARRAY, which is also a nested data structure.   - PhoneAreaCode: STRING   - PhoneCountryCode: STRING   - PhoneNumber: STRING   - PhoneType: STRING - PurchasesDefaultAccountCode: STRING - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SalesDefaultAccountCode: STRING - SalesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SkypeUserName: STRING - TaxNumber: STRING - TrackingCategoryName: STRING - TrackingCategoryOption: STRING - UpdatedDateUTC: DATE-TIME - ValidationErrors: ARRAY, which is also a nested data structure.   - Message: STRING - Website: STRING - XeroNetworkKey: STRING |
| **CreditNoteID**  STRING |
| **CreditNoteNumber**  STRING |
| **CurrencyCode**  STRING |
| **CurrencyRate**  NUMBER |
| **Date**  DATE-TIME |
| **DateString**  DATE-TIME |
| **DueDate**  DATE-TIME |
| **DueDateString**  DATE-TIME |
| **FullyPaidOnDate**  DATE-TIME |
| **HasAttachments**  BOOLEAN |
| **ID**  STRING |
| **LineAmountTypes**  STRING |
| **LineItems**  ARRAY This is a nested data structure:   - AccountCode: STRING - Description: STRING - DiscountRate: NUMBER - ItemCode: STRING - LineAmount: NUMBER - LineItemID: STRING - Quantity: NUMBER - TaxAmount: NUMBER - TaxType: STRING - Tracking: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - UnitAmount: NUMBER |
| **Reference**  STRING |
| **RemainingCredit**  NUMBER |
| **SentToContact**  BOOLEAN |
| **Status**  STRING |
| **SubTotal**  NUMBER |
| **Total**  NUMBER |
| **TotalTax**  NUMBER |
| **Type**  STRING |
| **UpdatedDateUTC**  DATE-TIME |

### currencies

The `currencies` table contains info about the currencies available in your Xero account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | Code |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/currencies "Opens in new tab: Xero API method") |

currencies table foreign keys

| Join currencies with | on |
| --- | --- |
| [accounts](#accounts) | ``` currencies.Code = accounts.CurrencyCode ``` |
| [bank\_transactions](#bank-transactions) | ``` currencies.Code = bank_transactions.CurrencyCode ``` |
| [credit\_notes](#credit-notes) | ``` currencies.Code = credit_notes.CurrencyCode ``` |
| [invoices](#invoices) | ``` currencies.Code = invoices.CurrencyCode ``` |
| [prepayments](#prepayments) | ``` currencies.Code = prepayments.CurrencyCode ``` |
| [purchase\_orders](#purchase-orders) | ``` currencies.Code = purchase_orders.CurrencyCode ``` |
| [repeating\_invoices](#repeating-invoices) | ``` currencies.Code = repeating_invoices.CurrencyCode ``` |

currencies table schema

|  |
| --- |
| **Code**  STRING |
| **Description**  STRING |

### employees

The `employees` table contains info about employees.

**Note**: According to [Xero’s documentation](https://developer.xero.com/documentation/api/employees), the endpoint that produces this table is:

> Used for an [employee type](https://help.xero.com/int/Contacts_EmployeeAdd) used exclusively by the global Payrun functionality in Xero core accounting.

As a result, this table may not contain all employee data. Refer to the `contacts` table if you believe you are missing records.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | EmployeeID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/employees "Opens in new tab: Xero API method") |

employees table schema

|  |
| --- |
| **EmployeeID**  STRING |
| **ExternalLink**  STRING |
| **FirstName**  STRING |
| **LastName**  STRING |
| **Status**  STRING |
| **UpdatedDateUTC**  DATE-TIME |

### expense\_claims

The `expense_claims` table contains info about expense claims.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ExpenseClaimID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/expense-claims "Opens in new tab: Xero API method") |

expense\_claims table foreign keys

| Join expense\_claims with | on |
| --- | --- |
| [invoices](#invoices) | ``` expense_claims.Payments.PaymentID = invoices.Payments.PaymentID ``` |
| [overpayments](#overpayments) | ``` expense_claims.Payments.PaymentID = overpayments.Payments.PaymentID ``` |
| [payments](#payments) | ``` expense_claims.Payments.PaymentID = payments.PaymentID ``` |
| [receipts](#receipts) | ``` expense_claims.Receipts.ReceiptID = receipts.ReceiptID ```  ``` expense_claims.User.UserID = receipts.User.UserID ``` |

expense\_claims table schema

|  |
| --- |
| **AmountDue**  NUMBER |
| **AmountPaid**  NUMBER |
| **ExpenseClaimID**  STRING |
| **PaymentDueDate**  DATE-TIME |
| **Payments**  ARRAY This is a nested data structure:   - Account: OBJECT, which is also a nested data structure.   - AccountID: STRING   - BankAccountNumber: STRING   - BankAccountType: STRING   - Class: STRING   - Code: STRING   - CurrencyCode: STRING   - Description: STRING   - EnablePaymentsToAccount: BOOLEAN   - HasAttachments: BOOLEAN   - Name: STRING   - ReportingCode: STRING   - ReportingCodeName: STRING   - ShowInExpenseClaims: BOOLEAN   - Status: STRING   - SystemAccount: STRING   - TaxType: STRING   - Type: STRING   - UpdatedDateUTC: DATE-TIME - Amount: NUMBER - BankAmount: NUMBER - BatchPaymentID: STRING - CreditNote: OBJECT, which is also a nested data structure.   - CreditNoteNumber: STRING - CurrencyRate: NUMBER - Date: DATE-TIME - HasAccount: BOOLEAN - HasValidationErrors: BOOLEAN - Invoice: OBJECT, which is also a nested data structure.   - AmountCredited: NUMBER   - AmountDue: NUMBER   - AmountPaid: NUMBER   - BrandingThemeID: STRING   - Contact: OBJECT, which is also a nested data structure.     - AccountNumber: STRING     - AccountsPayableTaxType: STRING     - AccountsReceivableTaxType: STRING     - Addresses: ARRAY, which is also a nested data structure.       - AddressLine1: STRING       - AddressLine2: STRING       - AddressLine3: STRING       - AddressLine4: STRING       - AddressType: STRING       - AttentionTo: STRING       - City: STRING       - Country: STRING       - PostalCode: STRING       - Region: STRING     - Attachments: ARRAY     - Balances: OBJECT, which is also a nested data structure.       - AccountsPayable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER       - AccountsReceivable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER     - BankAccountDetails: STRING     - BatchPayments: OBJECT, which is also a nested data structure.       - BankAccountName: STRING       - BankAccountNumber: STRING       - Code: STRING       - Details: STRING       - Reference: STRING     - BrandingTheme: OBJECT, which is also a nested data structure.       - BrandingThemeID: STRING       - CreatedDateUTC: DATE-TIME       - Name: STRING       - SortOrder: INTEGER     - ContactGroups: ARRAY, which is also a nested data structure.       - ContactGroupID: STRING       - HasValidationErrors: BOOLEAN       - Name: STRING       - Status: STRING     - ContactID: STRING     - ContactNumber: STRING     - ContactPersons: ARRAY, which is also a nested data structure.       - EmailAddress: STRING       - FirstName: STRING       - IncludeInEmails: BOOLEAN       - LastName: STRING     - ContactStatus: STRING     - DefaultCurrency: STRING     - Discount: NUMBER     - EmailAddress: STRING     - FirstName: STRING     - HasAttachments: BOOLEAN     - HasValidationErrors: BOOLEAN     - IsCustomer: BOOLEAN     - IsSupplier: BOOLEAN     - LastName: STRING     - Name: STRING     - PaymentTerms: OBJECT, which is also a nested data structure.       - Bills: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING       - Sales: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING     - Phones: ARRAY, which is also a nested data structure.       - PhoneAreaCode: STRING       - PhoneCountryCode: STRING       - PhoneNumber: STRING       - PhoneType: STRING     - PurchasesDefaultAccountCode: STRING     - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SalesDefaultAccountCode: STRING     - SalesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SkypeUserName: STRING     - TaxNumber: STRING     - TrackingCategoryName: STRING     - TrackingCategoryOption: STRING     - UpdatedDateUTC: DATE-TIME     - ValidationErrors: ARRAY, which is also a nested data structure.       - Message: STRING     - Website: STRING     - XeroNetworkKey: STRING   - CurrencyCode: STRING   - CurrencyRate: NUMBER   - Date: DATE-TIME   - DateString: DATE-TIME   - DueDate: DATE-TIME   - DueDateString: DATE-TIME   - ExpectedPaymentDate: DATE-TIME   - FullyPaidOnDate: DATE-TIME   - HasAttachments: BOOLEAN   - HasErrors: BOOLEAN   - InvoiceID: STRING   - InvoiceNumber: STRING   - IsDiscounted: BOOLEAN   - LineAmountTypes: STRING   - LineItems: ARRAY, which is also a nested data structure.     - AccountCode: STRING     - Description: STRING     - DiscountRate: NUMBER     - ItemCode: STRING     - LineAmount: NUMBER     - LineItemID: STRING     - Quantity: NUMBER     - TaxAmount: NUMBER     - TaxType: STRING     - Tracking: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - UnitAmount: NUMBER   - PlannedPaymentDate: DATE-TIME   - Reference: STRING   - SentToContact: BOOLEAN   - Status: STRING   - SubTotal: NUMBER   - Total: NUMBER   - TotalDiscount: NUMBER   - TotalTax: NUMBER   - Type: STRING   - UpdatedDateUTC: DATE-TIME   - Url: STRING - IsReconciled: BOOLEAN - Overpayment: ARRAY, which is also a nested data structure.   - OverpaymentID: STRING - PaymentID: STRING - PaymentType: STRING - Prepayments: ARRAY, which is also a nested data structure.   - PrepaymentID: STRING - Reference: STRING - Status: STRING - UpdatedDateUTC: DATE-TIME |
| **Receipts**  ARRAY This is a nested data structure:   - Attachments: ARRAY - Contact: OBJECT, which is also a nested data structure.   - AccountNumber: STRING   - AccountsPayableTaxType: STRING   - AccountsReceivableTaxType: STRING   - Addresses: ARRAY, which is also a nested data structure.     - AddressLine1: STRING     - AddressLine2: STRING     - AddressLine3: STRING     - AddressLine4: STRING     - AddressType: STRING     - AttentionTo: STRING     - City: STRING     - Country: STRING     - PostalCode: STRING     - Region: STRING   - Attachments: ARRAY   - Balances: OBJECT, which is also a nested data structure.     - AccountsPayable: OBJECT, which is also a nested data structure.       - Outstanding: NUMBER       - Overdue: NUMBER     - AccountsReceivable: OBJECT, which is also a nested data structure.       - Outstanding: NUMBER       - Overdue: NUMBER   - BankAccountDetails: STRING   - BatchPayments: OBJECT, which is also a nested data structure.     - BankAccountName: STRING     - BankAccountNumber: STRING     - Code: STRING     - Details: STRING     - Reference: STRING   - BrandingTheme: OBJECT, which is also a nested data structure.     - BrandingThemeID: STRING     - CreatedDateUTC: DATE-TIME     - Name: STRING     - SortOrder: STRING   - ContactGroups: ARRAY, which is also a nested data structure.     - ContactGroupID: STRING     - HasValidationErrors: BOOLEAN     - Name: STRING     - Status: STRING   - ContactID: STRING   - ContactNumber: STRING   - ContactPersons: ARRAY, which is also a nested data structure.     - EmailAddress: STRING     - FirstName: STRING     - IncludeInEmails: BOOLEAN     - LastName: STRING   - ContactStatus: STRING   - DefaultCurrency: STRING   - Discount: NUMBER   - EmailAddress: STRING   - FirstName: STRING   - HasAttachments: BOOLEAN   - HasValidationErrors: BOOLEAN   - IsCustomer: BOOLEAN   - IsSupplier: BOOLEAN   - LastName: STRING   - Name: STRING   - PaymentTerms: OBJECT, which is also a nested data structure.     - Bills: OBJECT, which is also a nested data structure.       - Day: INTEGER       - Type: STRING     - Sales: OBJECT, which is also a nested data structure.       - Day: INTEGER       - Type: STRING   - Phones: ARRAY, which is also a nested data structure.     - PhoneAreaCode: STRING     - PhoneCountryCode: STRING     - PhoneNumber: STRING     - PhoneType: STRING   - PurchasesDefaultAccountCode: STRING   - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - SalesDefaultAccountCode: STRING   - SalesTrackingCategories: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - SkypeUserName: STRING   - TaxNumber: STRING   - TrackingCategoryName: STRING   - TrackingCategoryOption: STRING   - UpdatedDateUTC: DATE-TIME   - ValidationErrors: ARRAY, which is also a nested data structure.     - Message: STRING   - Website: STRING   - XeroNetworkKey: STRING - Date: DATE-TIME - HasAttachments: BOOLEAN - ID: STRING - LineAmountTypes: STRING - LineItems: ARRAY, which is also a nested data structure.   - AccountCode: STRING   - Description: STRING   - DiscountRate: NUMBER   - ItemCode: STRING   - LineAmount: NUMBER   - LineItemID: STRING   - Quantity: NUMBER   - TaxAmount: NUMBER   - TaxType: STRING   - Tracking: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - UnitAmount: NUMBER - ReceiptID: STRING - ReceiptNumber: INTEGER - Reference: STRING - Status: STRING - SubTotal: NUMBER - Total: NUMBER - TotalTax: NUMBER - UpdatedDateUTC: DATE-TIME - Url: STRING - User: OBJECT, which is also a nested data structure.   - EmailAddress: STRING   - FirstName: STRING   - IsSubscriber: BOOLEAN   - LastName: STRING   - OrganisationRole: STRING   - UpdatedDateUTC: DATE-TIME   - UserID: STRING   - ValidationErrors: ARRAY, which is also a nested data structure.     - Message: STRING - ValidationErrors: ARRAY, which is also a nested data structure.   - Message: STRING |
| **ReportingDate**  DATE-TIME |
| **Status**  STRING |
| **Total**  NUMBER |
| **UpdatedDateUTC**  DATE-TIME |
| **User**  OBJECT This is a nested data structure:   - EmailAddress: STRING - FirstName: STRING - IsSubscriber: BOOLEAN - LastName: STRING - OrganisationRole: STRING - UpdatedDateUTC: DATE-TIME - UserID: STRING - ValidationErrors: ARRAY, which is also a nested data structure.   - Message: STRING |

### invoices

The `invoices` table contains info about sales invoices, which are requests for payment for goods and services.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | InvoiceID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/invoices "Opens in new tab: Xero API method") |

invoices table foreign keys

| Join invoices with | on |
| --- | --- |
| [branding\_themes](#branding-themes) | ``` invoices.BrandingThemeID = branding_themes.BrandingThemeID ``` |
| [contacts](#contacts) | ``` invoices.BrandingThemeID = contacts.BrandingTheme.BrandingThemeID ```  ``` invoices.Contact.ContactID = contacts.ContactID ```  ``` invoices.LineItems.Tracking.TrackingCategoryID = contacts.SalesTrackingCategories.TrackingCategoryID ```  ``` invoices.LineItems.Tracking.TrackingCategoryID = contacts.PurchasesTrackingCategories.TrackingCategoryID ``` |
| [credit\_notes](#credit-notes) | ``` invoices.BrandingThemeID = credit_notes.BrandingThemeID ```  ``` invoices.Contact.ContactID = credit_notes.Contact.ContactID ```  ``` invoices.CreditNotes.CreditNoteID = credit_notes.CreditNoteID ```  ``` invoices.CurrencyCode = credit_notes.CurrencyCode ```  ``` invoices.LineItems.Tracking.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ``` |
| [purchase\_orders](#purchase-orders) | ``` invoices.BrandingThemeID = purchase_orders.BrandingThemeID ```  ``` invoices.CurrencyCode = purchase_orders.CurrencyCode ```  ``` invoices.LineItems.Tracking.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` invoices.BrandingThemeID = repeating_invoices.BrandingThemeID ```  ``` invoices.Contact.ContactID = repeating_invoices.Contact.ContactID ```  ``` invoices.CurrencyCode = repeating_invoices.CurrencyCode ```  ``` invoices.LineItems.Tracking.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [linked\_transactions](#linked-transactions) | ``` invoices.Contact.ContactID = linked_transactions.ContactID ```  ``` invoices.InvoiceID = linked_transactions.SourceTransactionID ```  ``` invoices.InvoiceID = linked_transactions.TargetTransactionID ``` |
| [overpayments](#overpayments) | ``` invoices.Contact.ContactID = overpayments.Contact.ContactID ```  ``` invoices.InvoiceID = overpayments.Allocations.Invoice.InvoiceID ```  ``` invoices.Overpayments.Overpayment.OverpaymentID = overpayments.OverpaymentID ```  ``` invoices.Payments.PaymentID = overpayments.Payments.PaymentID ```  ``` invoices.LineItems.Tracking.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ``` |
| [prepayments](#prepayments) | ``` invoices.Contact.ContactID = prepayments.Contact.ContactID ```  ``` invoices.CurrencyCode = prepayments.CurrencyCode ```  ``` invoices.InvoiceID = prepayments.Allocations.Invoice.InvoiceID ```  ``` invoices.Prepayments.PrepaymentID = prepayments.PrepaymentID ```  ``` invoices.LineItems.Tracking.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ``` |
| [receipts](#receipts) | ``` invoices.Contact.ContactID = receipts.Contact.ContactID ```  ``` invoices.LineItems.Tracking.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ``` |
| [accounts](#accounts) | ``` invoices.CurrencyCode = accounts.CurrencyCode ``` |
| [bank\_transactions](#bank-transactions) | ``` invoices.CurrencyCode = bank_transactions.CurrencyCode ```  ``` invoices.Overpayments.Overpayment.OverpaymentID = bank_transactions.OverpaymentID ```  ``` invoices.Prepayments.PrepaymentID = bank_transactions.PrepaymentID ```  ``` invoices.InvoiceID = bank_transactions.BankTransactionID ``` |
| [currencies](#currencies) | ``` invoices.CurrencyCode = currencies.Code ``` |
| [payments](#payments) | ``` invoices.InvoiceID = payments.Invoice.InvoiceID ```  ``` invoices.Overpayments.Overpayment.OverpaymentID = payments.Overpayment.OverpaymentID ```  ``` invoices.Payments.PaymentID = payments.PaymentID ```  ``` invoices.Prepayments.PrepaymentID = payments.Prepayments.PrepaymentID ``` |
| [expense\_claims](#expense-claims) | ``` invoices.Payments.PaymentID = expense_claims.Payments.PaymentID ``` |
| [journals](#journals) | ``` invoices.LineItems.Tracking.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ``` |
| [manual\_journals](#manual-journals) | ``` invoices.LineItems.Tracking.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ``` |
| [tracking\_categories](#tracking-categories) | ``` invoices.LineItems.Tracking.TrackingCategoryID = tracking_categories.TrackingCategoryID ``` |

invoices table schema

|  |
| --- |
| **AmountCredited**  NUMBER |
| **AmountDue**  NUMBER |
| **AmountPaid**  NUMBER |
| **BrandingThemeID**  STRING |
| **Contact**  OBJECT This is a nested data structure:   - AccountNumber: STRING - AccountsPayableTaxType: STRING - AccountsReceivableTaxType: STRING - Addresses: ARRAY, which is also a nested data structure.   - AddressLine1: STRING   - AddressLine2: STRING   - AddressLine3: STRING   - AddressLine4: STRING   - AddressType: STRING   - AttentionTo: STRING   - City: STRING   - Country: STRING   - PostalCode: STRING   - Region: STRING - Attachments: ARRAY - Balances: OBJECT, which is also a nested data structure.   - AccountsPayable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER   - AccountsReceivable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER - BankAccountDetails: STRING - BatchPayments: OBJECT, which is also a nested data structure.   - BankAccountName: STRING   - BankAccountNumber: STRING   - Code: STRING   - Details: STRING   - Reference: STRING - BrandingTheme: OBJECT, which is also a nested data structure.   - BrandingThemeID: STRING   - CreatedDateUTC: DATE-TIME   - Name: STRING   - SortOrder: INTEGER - ContactGroups: ARRAY, which is also a nested data structure.   - ContactGroupID: STRING   - HasValidationErrors: BOOLEAN   - Name: STRING   - Status: STRING - ContactID: STRING - ContactNumber: STRING - ContactPersons: ARRAY, which is also a nested data structure.   - EmailAddress: STRING   - FirstName: STRING   - IncludeInEmails: BOOLEAN   - LastName: STRING - ContactStatus: STRING - DefaultCurrency: STRING - Discount: NUMBER - EmailAddress: STRING - FirstName: STRING - HasAttachments: BOOLEAN - HasValidationErrors: BOOLEAN - IsCustomer: BOOLEAN - IsSupplier: BOOLEAN - LastName: STRING - Name: STRING - PaymentTerms: OBJECT, which is also a nested data structure.   - Bills: OBJECT, which is also a nested data structure.     - Day: NUMBER     - Type: NUMBER   - Sales: OBJECT, which is also a nested data structure.     - Day: NUMBER     - Type: NUMBER - Phones: ARRAY, which is also a nested data structure.   - PhoneAreaCode: STRING   - PhoneCountryCode: STRING   - PhoneNumber: STRING   - PhoneType: STRING - PurchasesDefaultAccountCode: STRING - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SalesDefaultAccountCode: STRING - SalesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SkypeUserName: STRING - TaxNumber: STRING - TrackingCategoryName: STRING - TrackingCategoryOption: STRING - UpdatedDateUTC: DATE-TIME - ValidationErrors: ARRAY, which is also a nested data structure.   - Message: STRING - Website: STRING - XeroNetworkKey: STRING |
| **CreditNotes**  ARRAY This is a nested data structure:   - Allocations: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - Date: DATE-TIME   - Invoice: OBJECT, which is also a nested data structure.     - AmountCredited: NUMBER     - AmountDue: NUMBER     - AmountPaid: NUMBER     - BrandingThemeID: STRING     - Contact: OBJECT, which is also a nested data structure.       - AccountNumber: STRING       - AccountsPayableTaxType: STRING       - AccountsReceivableTaxType: STRING       - Addresses: ARRAY, which is also a nested data structure.         - AddressLine1: STRING         - AddressLine2: STRING         - AddressLine3: STRING         - AddressLine4: STRING         - AddressType: STRING         - AttentionTo: STRING         - City: STRING         - Country: STRING         - PostalCode: STRING         - Region: STRING       - Attachments: ARRAY       - Balances: OBJECT, which is also a nested data structure.         - AccountsPayable: OBJECT, which is also a nested data structure.           - Outstanding: NUMBER           - Overdue: NUMBER         - AccountsReceivable: OBJECT, which is also a nested data structure.           - Outstanding: NUMBER           - Overdue: NUMBER       - BankAccountDetails: STRING       - BatchPayments: OBJECT, which is also a nested data structure.         - BankAccountName: STRING         - BankAccountNumber: STRING         - Code: STRING         - Details: STRING         - Reference: STRING       - BrandingTheme: OBJECT, which is also a nested data structure.         - BrandingThemeID: STRING         - CreatedDateUTC: DATE-TIME         - Name: STRING         - SortOrder: INTEGER       - ContactGroups: ARRAY, which is also a nested data structure.         - ContactGroupID: STRING         - HasValidationErrors: BOOLEAN         - Name: STRING         - Status: STRING       - ContactID: STRING       - ContactNumber: STRING       - ContactPersons: ARRAY, which is also a nested data structure.         - EmailAddress: STRING         - FirstName: STRING         - IncludeInEmails: BOOLEAN         - LastName: STRING       - ContactStatus: STRING       - DefaultCurrency: STRING       - Discount: NUMBER       - EmailAddress: STRING       - FirstName: STRING       - HasAttachments: BOOLEAN       - HasValidationErrors: BOOLEAN       - IsCustomer: BOOLEAN       - IsSupplier: BOOLEAN       - LastName: STRING       - Name: STRING       - PaymentTerms: OBJECT, which is also a nested data structure.         - Bills: OBJECT, which is also a nested data structure.           - Day: INTEGER           - Type: STRING         - Sales: OBJECT, which is also a nested data structure.           - Day: INTEGER           - Type: STRING       - Phones: ARRAY, which is also a nested data structure.         - PhoneAreaCode: STRING         - PhoneCountryCode: STRING         - PhoneNumber: STRING         - PhoneType: STRING       - PurchasesDefaultAccountCode: STRING       - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.         - Name: STRING         - Option: STRING         - Options: ARRAY, which is also a nested data structure.         - Status: STRING         - TrackingCategoryID: STRING         - TrackingCategoryName: STRING         - TrackingOptionID: STRING         - TrackingOptionName: STRING       - SalesDefaultAccountCode: STRING       - SalesTrackingCategories: ARRAY, which is also a nested data structure.         - Name: STRING         - Option: STRING         - Options: ARRAY, which is also a nested data structure.         - Status: STRING         - TrackingCategoryID: STRING         - TrackingCategoryName: STRING         - TrackingOptionID: STRING         - TrackingOptionName: STRING       - SkypeUserName: STRING       - TaxNumber: STRING       - TrackingCategoryName: STRING       - TrackingCategoryOption: STRING       - UpdatedDateUTC: DATE-TIME       - ValidationErrors: ARRAY, which is also a nested data structure.         - Message: STRING       - Website: STRING       - XeroNetworkKey: STRING     - CurrencyCode: STRING     - CurrencyRate: NUMBER     - Date: DATE-TIME     - DateString: DATE-TIME     - DueDate: DATE-TIME     - DueDateString: DATE-TIME     - ExpectedPaymentDate: DATE-TIME     - FullyPaidOnDate: DATE-TIME     - HasAttachments: BOOLEAN     - HasErrors: BOOLEAN     - InvoiceID: STRING     - InvoiceNumber: STRING     - IsDiscounted: BOOLEAN     - LineAmountTypes: STRING     - LineItems: ARRAY, which is also a nested data structure.       - AccountCode: STRING       - Description: STRING       - DiscountRate: NUMBER       - ItemCode: STRING       - LineAmount: NUMBER       - LineItemID: STRING       - Quantity: NUMBER       - TaxAmount: NUMBER       - TaxType: STRING       - Tracking: ARRAY, which is also a nested data structure.         - Name: STRING         - Option: STRING         - Options: ARRAY, which is also a nested data structure.           - HasValidationErrors: BOOLEAN           - IsActive: BOOLEAN           - IsArchived: BOOLEAN           - IsDeleted: BOOLEAN           - Name: STRING           - Status: STRING           - TrackingOptionID: STRING         - Status: STRING         - TrackingCategoryID: STRING         - TrackingCategoryName: STRING         - TrackingOptionID: STRING         - TrackingOptionName: STRING       - UnitAmount: NUMBER     - PlannedPaymentDate: DATE-TIME     - Reference: STRING     - SentToContact: BOOLEAN     - Status: STRING     - SubTotal: NUMBER     - Total: NUMBER     - TotalDiscount: NUMBER     - TotalTax: NUMBER     - Type: STRING     - UpdatedDateUTC: DATE-TIME     - Url: STRING - AppliedAmount: NUMBER - BrandingThemeID: STRING - Contact: OBJECT, which is also a nested data structure.   - AccountNumber: STRING   - AccountsPayableTaxType: STRING   - AccountsReceivableTaxType: STRING   - Addresses: ARRAY, which is also a nested data structure.     - AddressLine1: STRING     - AddressLine2: STRING     - AddressLine3: STRING     - AddressLine4: STRING     - AddressType: STRING     - AttentionTo: STRING     - City: STRING     - Country: STRING     - PostalCode: STRING     - Region: STRING   - Attachments: ARRAY   - Balances: OBJECT, which is also a nested data structure.     - AccountsPayable: OBJECT, which is also a nested data structure.       - Outstanding: NUMBER       - Overdue: NUMBER     - AccountsReceivable: OBJECT, which is also a nested data structure.       - Outstanding: NUMBER       - Overdue: NUMBER   - BankAccountDetails: STRING   - BatchPayments: OBJECT, which is also a nested data structure.     - BankAccountName: STRING     - BankAccountNumber: STRING     - Code: STRING     - Details: STRING     - Reference: STRING   - BrandingTheme: OBJECT, which is also a nested data structure.     - BrandingThemeID: STRING     - CreatedDateUTC: DATE-TIME     - Name: STRING     - SortOrder: INTEGER   - ContactGroups: ARRAY, which is also a nested data structure.     - ContactGroupID: STRING     - HasValidationErrors: BOOLEAN     - Name: STRING     - Status: STRING   - ContactID: STRING   - ContactNumber: STRING   - ContactPersons: ARRAY, which is also a nested data structure.     - EmailAddress: STRING     - FirstName: STRING     - IncludeInEmails: BOOLEAN     - LastName: STRING   - ContactStatus: STRING   - DefaultCurrency: STRING   - Discount: NUMBER   - EmailAddress: STRING   - FirstName: STRING   - HasAttachments: BOOLEAN   - HasValidationErrors: BOOLEAN   - IsCustomer: BOOLEAN   - IsSupplier: BOOLEAN   - LastName: STRING   - Name: STRING   - PaymentTerms: OBJECT, which is also a nested data structure.     - Bills: OBJECT, which is also a nested data structure.       - Day: INTEGER       - Type: STRING     - Sales: OBJECT, which is also a nested data structure.       - Day: INTEGER       - Type: STRING   - Phones: ARRAY, which is also a nested data structure.     - PhoneAreaCode: STRING     - PhoneCountryCode: STRING     - PhoneNumber: STRING     - PhoneType: STRING   - PurchasesDefaultAccountCode: STRING   - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - SalesDefaultAccountCode: STRING   - SalesTrackingCategories: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - SkypeUserName: STRING   - TaxNumber: STRING   - TrackingCategoryName: STRING   - TrackingCategoryOption: STRING   - UpdatedDateUTC: DATE-TIME   - ValidationErrors: ARRAY, which is also a nested data structure.     - Message: STRING   - Website: STRING   - XeroNetworkKey: STRING - CreditNoteID: STRING - CreditNoteNumber: STRING - CurrencyCode: STRING - CurrencyRate: NUMBER - Date: DATE-TIME - DateString: DATE-TIME - DueDateString: DATE-TIME - FullyPaidOnDate: DATE-TIME - HasAttachments: BOOLEAN - ID: STRING - LineAmountTypes: STRING - LineItems: ARRAY, which is also a nested data structure.   - AccountCode: STRING   - Description: STRING   - DiscountRate: NUMBER   - ItemCode: STRING   - LineAmount: NUMBER   - LineItemID: STRING   - Quantity: NUMBER   - TaxAmount: NUMBER   - TaxType: STRING   - Tracking: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - UnitAmount: NUMBER - Reference: STRING - RemainingCredit: NUMBER - SentToContact: BOOLEAN - Status: STRING - SubTotal: NUMBER - Total: NUMBER - TotalTax: NUMBER - Type: STRING - UpdatedDateUTC: DATE-TIME |
| **CurrencyCode**  STRING |
| **CurrencyRate**  NUMBER |
| **Date**  DATE-TIME |
| **DateString**  DATE-TIME |
| **DueDate**  DATE-TIME |
| **DueDateString**  DATE-TIME |
| **ExpectedPaymentDate**  DATE-TIME |
| **ExpectedPaymentDateString**  DATE-TIME |
| **FullyPaidOnDate**  DATE-TIME |
| **HasAttachments**  BOOLEAN |
| **HasErrors**  BOOLEAN |
| **InvoiceID**  STRING |
| **InvoiceNumber**  STRING |
| **IsDiscounted**  BOOLEAN |
| **LineAmountTypes**  STRING |
| **LineItems**  ARRAY This is a nested data structure:   - AccountCode: STRING - Description: STRING - DiscountRate: NUMBER - ItemCode: STRING - LineAmount: NUMBER - LineItemID: STRING - Quantity: NUMBER - TaxAmount: NUMBER - TaxType: STRING - Tracking: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - UnitAmount: NUMBER |
| **Overpayments**  ARRAY This is a nested data structure:   - Account: OBJECT, which is also a nested data structure.   - AccountID: STRING   - BankAccountNumber: STRING   - BankAccountType: STRING   - Class: STRING   - Code: STRING   - CurrencyCode: STRING   - Description: STRING   - EnablePaymentsToAccount: BOOLEAN   - HasAttachments: BOOLEAN   - Name: STRING   - ReportingCode: STRING   - ReportingCodeName: STRING   - ShowInExpenseClaims: BOOLEAN   - Status: STRING   - SystemAccount: STRING   - TaxType: STRING   - Type: STRING   - UpdatedDateUTC: DATE-TIME - Amount: NUMBER - BankAmount: NUMBER - BatchPaymentID: STRING - CreditNote: OBJECT, which is also a nested data structure.   - CreditNoteNumber: STRING - CurrencyRate: NUMBER - Date: DATE-TIME - HasAccount: BOOLEAN - HasValidationErrors: BOOLEAN - Invoice: OBJECT, which is also a nested data structure.   - AmountCredited: NUMBER   - AmountDue: NUMBER   - AmountPaid: NUMBER   - BrandingThemeID: STRING   - Contact: OBJECT, which is also a nested data structure.     - AccountNumber: STRING     - AccountsPayableTaxType: STRING     - AccountsReceivableTaxType: STRING     - Addresses: ARRAY, which is also a nested data structure.       - AddressLine1: STRING       - AddressLine2: STRING       - AddressLine3: STRING       - AddressLine4: STRING       - AddressType: STRING       - AttentionTo: STRING       - City: STRING       - Country: STRING       - PostalCode: STRING       - Region: STRING     - Attachments: ARRAY     - Balances: OBJECT, which is also a nested data structure.       - AccountsPayable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER       - AccountsReceivable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER     - BankAccountDetails: STRING     - BatchPayments: OBJECT, which is also a nested data structure.       - BankAccountName: STRING       - BankAccountNumber: STRING       - Code: STRING       - Details: STRING       - Reference: STRING     - BrandingTheme: OBJECT, which is also a nested data structure.       - BrandingThemeID: STRING       - CreatedDateUTC: DARE-TIME       - Name: STRING       - SortOrder: INTEGER     - ContactGroups: ARRAY, which is also a nested data structure.       - ContactGroupID: STRING       - HasValidationErrors: BOOLEAN       - Name: STRING       - Status: STRING     - ContactID: STRING     - ContactNumber: STRING     - ContactPersons: ARRAY, which is also a nested data structure.       - EmailAddress: STRING       - FirstName: STRING       - IncludeInEmails: BOOLEAN       - LastName: STRING     - ContactStatus: STRING     - DefaultCurrency: STRING     - Discount: NUMBER     - EmailAddress: STRING     - FirstName: STRING     - HasAttachments: BOOLEAN     - HasValidationErrors: BOOLEAN     - IsCustomer: BOOLEAN     - IsSupplier: BOOLEAN     - LastName: STRING     - Name: STRING     - PaymentTerms: OBJECT, which is also a nested data structure.       - Bills: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING       - Sales: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING     - Phones: ARRAY, which is also a nested data structure.       - PhoneAreaCode: STRING       - PhoneCountryCode: STRING       - PhoneNumber: STRING       - PhoneType: STRING     - PurchasesDefaultAccountCode: STRING     - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SalesDefaultAccountCode: STRING     - SalesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SkypeUserName: STRING     - TaxNumber: STRING     - TrackingCategoryName: STRING     - TrackingCategoryOption: STRING     - UpdatedDateUTC: DATE-TIME     - ValidationErrors: ARRAY, which is also a nested data structure.       - Message: STRING     - Website: STRING     - XeroNetworkKey: STRING   - CurrencyCode: STRING   - CurrencyRate: NUMBER   - Date: DATE-TIME   - DateString: DATE-TIME   - DueDate: DATE-TIME   - DueDateString: DATE-TIME   - ExpectedPaymentDate: DATE-TIME   - FullyPaidOnDate: DATE-TIME   - HasAttachments: BOOLEAN   - HasErrors: BOOLEAN   - InvoiceID: STRING   - InvoiceNumber: STRING   - IsDiscounted: BOOLEAN   - LineAmountTypes: STRING   - LineItems: ARRAY, which is also a nested data structure.     - AccountCode: STRING     - Description: STRING     - DiscountRate: NUMBER     - ItemCode: STRING     - LineAmount: NUMBER     - LineItemID: STRING     - Quantity: NUMBER     - TaxAmount: NUMBER     - TaxType: STRING     - Tracking: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - UnitAmount: NUMBER   - PlannedPaymentDate: DATE-TIME   - Reference: STRING   - SentToContact: BOOLEAN   - Status: STRING   - SubTotal: NUMBER   - Total: NUMBER   - TotalDiscount: NUMBER   - TotalTax: NUMBER   - Type: STRING   - UpdatedDateUTC: DATE-TIME   - Url: STRING - IsReconciled: BOOLEAN - Overpayment: ARRAY, which is also a nested data structure.   - OverpaymentID: STRING - PaymentID: STRING - PaymentType: STRING - Prepayments: ARRAY, which is also a nested data structure.   - PrepaymentID: STRING - Reference: STRING - Status: STRING - UpdatedDateUTC: DATE-TIME |
| **Payments**  ARRAY This is a nested data structure:   - Account: OBJECT, which is also a nested data structure.   - AccountID: STRING   - BankAccountNumber: STRING   - BankAccountType: STRING   - Class: STRING   - Code: STRING   - CurrencyCode: STRING   - Description: STRING   - EnablePaymentsToAccount: BOOLEAN   - HasAttachments: BOOLEAN   - Name: STRING   - ReportingCode: STRING   - ReportingCodeName: STRING   - ShowInExpenseClaims: BOOLEAN   - Status: STRING   - SystemAccount: STRING   - TaxType: STRING   - Type: STRING   - UpdatedDateUTC: DATE-TIME - Amount: NUMBER - BankAmount: NUMBER - BatchPaymentID: STRING - CreditNote: OBJECT, which is also a nested data structure.   - CreditNoteNumber: STRING - CurrencyRate: NUMBER - Date: DATE-TIME - HasAccount: BOOLEAN - HasValidationErrors: BOOLEAN - Invoice: OBJECT, which is also a nested data structure.   - AmountCredited: NUMBER   - AmountDue: NUMBER   - AmountPaid: NUMBER   - BrandingThemeID: STRING   - Contact: OBJECT, which is also a nested data structure.     - AccountNumber: STRING     - AccountsPayableTaxType: STRING     - AccountsReceivableTaxType: STRING     - Addresses: ARRAY, which is also a nested data structure.       - AddressLine1: STRING       - AddressLine2: STRING       - AddressLine3: STRING       - AddressLine4: STRING       - AddressType: STRING       - AttentionTo: STRING       - City: STRING       - Country: STRING       - PostalCode: STRING       - Region: STRING     - Attachments: ARRAY     - Balances: OBJECT, which is also a nested data structure.       - AccountsPayable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER       - AccountsReceivable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER     - BankAccountDetails: STRING     - BatchPayments: OBJECT, which is also a nested data structure.       - BankAccountName: STRING       - BankAccountNumber: STRING       - Code: STRING       - Details: STRING       - Reference: STRING     - BrandingTheme: OBJECT, which is also a nested data structure.       - BrandingThemeID: STRING       - CreatedDateUTC: DATE-TIME       - Name: STRING       - SortOrder: INTEGER     - ContactGroups: ARRAY, which is also a nested data structure.       - ContactGroupID: STRING       - HasValidationErrors: BOOLEAN       - Name: STRING       - Status: STRING     - ContactID: STRING     - ContactNumber: STRING     - ContactPersons: ARRAY, which is also a nested data structure.       - EmailAddress: STRING       - FirstName: STRING       - IncludeInEmails: BOOLEAN       - LastName: STRING     - ContactStatus: STRING     - DefaultCurrency: STRING     - Discount: NUMBER     - EmailAddress: STRING     - FirstName: STRING     - HasAttachments: BOOLEAN     - HasValidationErrors: BOOLEAN     - IsCustomer: BOOLEAN     - IsSupplier: BOOLEAN     - LastName: STRING     - Name: STRING     - PaymentTerms: OBJECT, which is also a nested data structure.       - Bills: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING       - Sales: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING     - Phones: ARRAY, which is also a nested data structure.       - PhoneAreaCode: STRING       - PhoneCountryCode: STRING       - PhoneNumber: STRING       - PhoneType: STRING     - PurchasesDefaultAccountCode: STRING     - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SalesDefaultAccountCode: STRING     - SalesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SkypeUserName: STRING     - TaxNumber: STRING     - TrackingCategoryName: STRING     - TrackingCategoryOption: STRING     - UpdatedDateUTC: DATE-TIME     - ValidationErrors: ARRAY, which is also a nested data structure.       - Message: STRING     - Website: STRING     - XeroNetworkKey: STRING   - CurrencyCode: STRING   - CurrencyRate: NUMBER   - Date: DATE-TIME   - DateString: DATE-TIME   - DueDate: DATE-TIME   - DueDateString: DATE-TIME   - ExpectedPaymentDate: DATE-TIME   - FullyPaidOnDate: DATE-TIME   - HasAttachments: BOOLEAN   - HasErrors: BOOLEAN   - InvoiceID: STRING   - InvoiceNumber: STRING   - IsDiscounted: BOOLEAN   - LineAmountTypes: STRING   - LineItems: ARRAY, which is also a nested data structure.     - AccountCode: STRING     - Description: STRING     - DiscountRate: NUMBER     - ItemCode: STRING     - LineAmount: NUMBER     - LineItemID: STRING     - Quantity: NUMBER     - TaxAmount: NUMBER     - TaxType: STRING     - Tracking: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - UnitAmount: NUMBER   - PlannedPaymentDate: DATE-TIME   - Reference: STRING   - SentToContact: BOOLEAN   - Status: STRING   - SubTotal: NUMBER   - Total: NUMBER   - TotalDiscount: NUMBER   - TotalTax: NUMBER   - Type: STRING   - UpdatedDateUTC: DATE-TIME   - Url: STRING - IsReconciled: BOOLEAN - Overpayment: ARRAY, which is also a nested data structure.   - OverpaymentID: STRING - PaymentID: STRING - PaymentType: STRING - Prepayments: ARRAY, which is also a nested data structure.   - PrepaymentID: STRING - Reference: STRING - Status: STRING - UpdatedDateUTC: DATE-TIME |
| **PlannedPaymentDate**  DATE-TIME |
| **PlannedPaymentDateString**  DATE-TIME |
| **Prepayments**  ARRAY This is a nested data structure:   - Allocations: ARRAY, which is also a nested data structure.   - Amount: NUMBER   - Date: DATE-TIME   - Invoice: OBJECT, which is also a nested data structure.     - AmountCredited: NUMBER     - AmountDue: NUMBER     - AmountPaid: NUMBER     - BrandingThemeID: STRING     - Contact: OBJECT, which is also a nested data structure.       - AccountNumber: STRING       - AccountsPayableTaxType: STRING       - AccountsReceivableTaxType: STRING       - Addresses: ARRAY, which is also a nested data structure.         - AddressLine1: STRING         - AddressLine2: STRING         - AddressLine3: STRING         - AddressLine4: STRING         - AddressType: STRING         - AttentionTo: STRING         - City: STRING         - Country: STRING         - PostalCode: STRING         - Region: STRING       - Attachments: ARRAY       - Balances: OBJECT, which is also a nested data structure.         - AccountsPayable: OBJECT, which is also a nested data structure.           - Outstanding: NUMBER           - Overdue: NUMBER         - AccountsReceivable: OBJECT, which is also a nested data structure.           - Outstanding: NUMBER           - Overdue: NUMBER       - BankAccountDetails: STRING       - BatchPayments: OBJECT, which is also a nested data structure.         - BankAccountName: STRING         - BankAccountNumber: STRING         - Code: STRING         - Details: STRING         - Reference: STRING       - BrandingTheme: OBJECT, which is also a nested data structure.         - BrandingThemeID: STRING         - CreatedDateUTC: DATE-TIME         - Name: STRING         - SortOrder: INTEGER       - ContactGroups: ARRAY, which is also a nested data structure.         - ContactGroupID: STRING         - HasValidationErrors: BOOLEAN         - Name: STRING         - Status: STRING       - ContactID: STRING       - ContactNumber: STRING       - ContactPersons: ARRAY, which is also a nested data structure.         - EmailAddress: STRING         - FirstName: STRING         - IncludeInEmails: BOOLEAN         - LastName: STRING       - ContactStatus: STRING       - DefaultCurrency: STRING       - Discount: NUMBER       - EmailAddress: STRING       - FirstName: STRING       - HasAttachments: BOOLEAN       - HasValidationErrors: BOOLEAN       - IsCustomer: BOOLEAN       - IsSupplier: BOOLEAN       - LastName: STRING       - Name: STRING       - PaymentTerms: OBJECT, which is also a nested data structure.         - Bills: OBJECT, which is also a nested data structure.           - Day: INTEGER           - Type: STRING         - Sales: OBJECT, which is also a nested data structure.           - Day: INTEGER           - Type: STRING       - Phones: ARRAY, which is also a nested data structure.         - PhoneAreaCode: STRING         - PhoneCountryCode: STRING         - PhoneNumber: STRING         - PhoneType: STRING       - PurchasesDefaultAccountCode: STRING       - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.         - Name: STRING         - Option: STRING         - Options: ARRAY, which is also a nested data structure.           - HasValidationErrors: BOOLEAN           - IsActive: BOOLEAN           - IsArchived: BOOLEAN           - IsDeleted: BOOLEAN           - Name: STRING           - Status: STRING           - TrackingOptionID: STRING         - Status: STRING         - TrackingCategoryID: STRING         - TrackingCategoryName: STRING         - TrackingOptionID: STRING         - TrackingOptionName: STRING       - SalesDefaultAccountCode: STRING       - SalesTrackingCategories: ARRAY, which is also a nested data structure.         - Name: STRING         - Option: STRING         - Options: ARRAY, which is also a nested data structure.           - HasValidationErrors: BOOLEAN           - IsActive: BOOLEAN           - IsArchived: BOOLEAN           - IsDeleted: BOOLEAN           - Name: STRING           - Status: STRING           - TrackingOptionID: STRING         - Status: STRING         - TrackingCategoryID: STRING         - TrackingCategoryName: STRING         - TrackingOptionID: STRING         - TrackingOptionName: STRING       - SkypeUserName: STRING       - TaxNumber: STRING       - TrackingCategoryName: STRING       - TrackingCategoryOption: STRING       - UpdatedDateUTC: DATE-TIME       - ValidationErrors: ARRAY, which is also a nested data structure.         - Message: STRING       - Website: STRING       - XeroNetworkKey: STRING     - CurrencyCode: STRING     - CurrencyRate: NUMBER     - Date: DATE-TIME     - DateString: DATE-TIME     - DueDate: DATE-TIME     - DueDateString: DATE-TIME     - ExpectedPaymentDate: DATE-TIME     - FullyPaidOnDate: DATE-TIME     - HasAttachments: BOOLEAN     - HasErrors: BOOLEAN     - InvoiceID: STRING     - InvoiceNumber: STRING     - IsDiscounted: BOOLEAN     - LineAmountTypes: STRING     - LineItems: ARRAY, which is also a nested data structure.       - AccountCode: STRING       - Description: STRING       - DiscountRate: NUMBER       - ItemCode: STRING       - LineAmount: NUMBER       - LineItemID: STRING       - Quantity: NUMBER       - TaxAmount: NUMBER       - TaxType: STRING       - Tracking: ARRAY, which is also a nested data structure.         - Name: STRING         - Option: STRING         - Options: ARRAY, which is also a nested data structure.           - HasValidationErrors: BOOLEAN           - IsActive: BOOLEAN           - IsArchived: BOOLEAN           - IsDeleted: BOOLEAN           - Name: STRING           - Status: STRING           - TrackingOptionID: STRING         - Status: STRING         - TrackingCategoryID: STRING         - TrackingCategoryName: STRING         - TrackingOptionID: STRING         - TrackingOptionName: STRING       - UnitAmount: NUMBER     - PlannedPaymentDate: DATE-TIME     - Reference: STRING     - SentToContact: BOOLEAN     - Status: STRING     - SubTotal: NUMBER     - Total: NUMBER     - TotalDiscount: NUMBER     - TotalTax: NUMBER     - Type: STRING     - UpdatedDateUTC: DATE-TIME     - Url: STRING - AppliedAmount: NUMBER - Contact: OBJECT, which is also a nested data structure.   - AccountNumber: STRING   - AccountsPayableTaxType: STRING   - AccountsReceivableTaxType: STRING   - Addresses: ARRAY, which is also a nested data structure.     - AddressLine1: STRING     - AddressLine2: STRING     - AddressLine3: STRING     - AddressLine4: STRING     - AddressType: STRING     - AttentionTo: STRING     - City: STRING     - Country: STRING     - PostalCode: STRING     - Region: STRING   - Attachments: ARRAY   - Balances: OBJECT, which is also a nested data structure.     - AccountsPayable: OBJECT, which is also a nested data structure.       - Outstanding: NUMBER       - Overdue: NUMBER     - AccountsReceivable: OBJECT, which is also a nested data structure.       - Outstanding: NUMBER       - Overdue: NUMBER   - BankAccountDetails: STRING   - BatchPayments: OBJECT, which is also a nested data structure.     - BankAccountName: STRING     - BankAccountNumber: STRING     - Code: STRING     - Details: STRING     - Reference: STRING   - BrandingTheme: OBJECT, which is also a nested data structure.     - BrandingThemeID: STRING     - CreatedDateUTC: DATE-TIME     - Name: STRING     - SortOrder: INTEGER   - ContactGroups: ARRAY, which is also a nested data structure.     - ContactGroupID: STRING     - HasValidationErrors: BOOLEAN     - Name: STRING     - Status: STRING   - ContactID: STRING   - ContactNumber: STRING   - ContactPersons: ARRAY, which is also a nested data structure.     - EmailAddress: STRING     - FirstName: STRING     - IncludeInEmails: BOOLEAN     - LastName: STRING   - ContactStatus: STRING   - DefaultCurrency: STRING   - Discount: NUMBER   - EmailAddress: STRING   - FirstName: STRING   - HasAttachments: BOOLEAN   - HasValidationErrors: BOOLEAN   - IsCustomer: BOOLEAN   - IsSupplier: BOOLEAN   - LastName: STRING   - Name: STRING   - PaymentTerms: OBJECT, which is also a nested data structure.     - Bills: OBJECT, which is also a nested data structure.       - Day: INTEGER       - Type: STRING     - Sales: OBJECT, which is also a nested data structure.       - Day: INTEGER       - Type: STRING   - Phones: ARRAY, which is also a nested data structure.     - PhoneAreaCode: STRING     - PhoneCountryCode: STRING     - PhoneNumber: STRING     - PhoneType: STRING   - PurchasesDefaultAccountCode: STRING   - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - SalesDefaultAccountCode: STRING   - SalesTrackingCategories: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - SkypeUserName: STRING   - TaxNumber: STRING   - TrackingCategoryName: STRING   - TrackingCategoryOption: STRING   - UpdatedDateUTC: DATE-TIME   - ValidationErrors: ARRAY, which is also a nested data structure.     - Message: STRING   - Website: STRING   - XeroNetworkKey: STRING - CurrencyCode: STRING - CurrencyRate: NUMBER - Date: DATE-TIME - DateString: DATE-TIME - HasAttachments: BOOLEAN - ID: STRING - LineAmountTypes: STRING - LineItems: ARRAY, which is also a nested data structure.   - AccountCode: STRING   - Description: STRING   - DiscountRate: NUMBER   - ItemCode: STRING   - LineAmount: NUMBER   - LineItemID: STRING   - Quantity: NUMBER   - TaxAmount: NUMBER   - TaxType: STRING   - Tracking: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - UnitAmount: NUMBER - Payments: ARRAY, which is also a nested data structure.   - Account: OBJECT, which is also a nested data structure.     - AccountID: STRING     - BankAccountNumber: STRING     - BankAccountType: STRING     - Class: STRING     - Code: STRING     - CurrencyCode: STRING     - Description: STRING     - EnablePaymentsToAccount: BOOLEAN     - HasAttachments: BOOLEAN     - Name: STRING     - ReportingCode: STRING     - ReportingCodeName: STRING     - ShowInExpenseClaims: BOOLEAN     - Status: STRING     - SystemAccount: STRING     - TaxType: STRING     - Type: STRING     - UpdatedDateUTC: DATE-TIME   - Amount: NUMBER   - BankAmount: NUMBER   - BatchPaymentID: STRING   - CreditNote: OBJECT, which is also a nested data structure.     - CreditNoteNumber: STRING   - CurrencyRate: NUMBER   - Date: DATE-TIME   - HasAccount: BOOLEAN   - HasValidationErrors: BOOLEAN   - Invoice: OBJECT, which is also a nested data structure.     - AmountCredited: NUMBER     - AmountDue: NUMBER     - AmountPaid: NUMBER     - BrandingThemeID: STRING     - Contact: OBJECT, which is also a nested data structure.       - AccountNumber: STRING       - AccountsPayableTaxType: STRING       - AccountsReceivableTaxType: STRING       - Addresses: ARRAY, which is also a nested data structure.         - AddressLine1: STRING         - AddressLine2: STRING         - AddressLine3: STRING         - AddressLine4: STRING         - AddressType: STRING         - AttentionTo: STRING         - City: STRING         - Country: STRING         - PostalCode: STRING         - Region: STRING       - Attachments: ARRAY       - Balances: OBJECT, which is also a nested data structure.         - AccountsPayable: OBJECT, which is also a nested data structure.           - Outstanding: NUMBER           - Overdue: NUMBER         - AccountsReceivable: OBJECT, which is also a nested data structure.           - Outstanding: NUMBER           - Overdue: NUMBER       - BankAccountDetails: STRING       - BatchPayments: OBJECT, which is also a nested data structure.         - BankAccountName: STRING         - BankAccountNumber: STRING         - Code: STRING         - Details: STRING         - Reference: STRING       - BrandingTheme: OBJECT, which is also a nested data structure.         - BrandingThemeID: STRING         - CreatedDateUTC: DATE-TIME         - Name: STRING         - SortOrder: INTEGER       - ContactGroups: ARRAY, which is also a nested data structure.         - ContactGroupID: STRING         - HasValidationErrors: BOOLEAN         - Name: STRING         - Status: STRING       - ContactID: STRING       - ContactNumber: STRING       - ContactPersons: ARRAY, which is also a nested data structure.         - EmailAddress: STRING         - FirstName: STRING         - IncludeInEmails: BOOLEAN         - LastName: STRING       - ContactStatus: STRING       - DefaultCurrency: STRING       - Discount: NUMBER       - EmailAddress: STRING       - FirstName: STRING       - HasAttachments: BOOLEAN       - HasValidationErrors: BOOLEAN       - IsCustomer: BOOLEAN       - IsSupplier: BOOLEAN       - LastName: STRING       - Name: STRING       - PaymentTerms: OBJECT, which is also a nested data structure.         - Bills: OBJECT, which is also a nested data structure.           - Day: INTEGER           - Type: STRING         - Sales: OBJECT, which is also a nested data structure.           - Day: INTEGER           - Type: STRING       - Phones: ARRAY, which is also a nested data structure.         - PhoneAreaCode: STRING         - PhoneCountryCode: STRING         - PhoneNumber: STRING         - PhoneType: STRING       - PurchasesDefaultAccountCode: STRING       - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.         - Name: STRING         - Option: STRING         - Options: ARRAY, which is also a nested data structure.           - HasValidationErrors: BOOLEAN           - IsActive: BOOLEAN           - IsArchived: BOOLEAN           - IsDeleted: BOOLEAN           - Name: STRING           - Status: STRING           - TrackingOptionID: STRING         - Status: STRING         - TrackingCategoryID: STRING         - TrackingCategoryName: STRING         - TrackingOptionID: STRING         - TrackingOptionName: STRING       - SalesDefaultAccountCode: STRING       - SalesTrackingCategories: ARRAY, which is also a nested data structure.         - Name: STRING         - Option: STRING         - Options: ARRAY, which is also a nested data structure.           - HasValidationErrors: BOOLEAN           - IsActive: BOOLEAN           - IsArchived: BOOLEAN           - IsDeleted: BOOLEAN           - Name: STRING           - Status: STRING           - TrackingOptionID: STRING         - Status: STRING         - TrackingCategoryID: STRING         - TrackingCategoryName: STRING         - TrackingOptionID: STRING         - TrackingOptionName: STRING       - SkypeUserName: STRING       - TaxNumber: STRING       - TrackingCategoryName: STRING       - TrackingCategoryOption: STRING       - UpdatedDateUTC: DATE-TIME       - ValidationErrors: ARRAY, which is also a nested data structure.         - Message: STRING       - Website: STRING       - XeroNetworkKey: STRING     - CurrencyCode: STRING     - CurrencyRate: NUMBER     - Date: DATE-TIME     - DateString: DATE-TIME     - DueDate: DATE-TIME     - DueDateString: DATE-TIME     - ExpectedPaymentDate: DATE-TIME     - FullyPaidOnDate: DATE-TIME     - HasAttachments: BOOLEAN     - HasErrors: BOOLEAN     - InvoiceID: STRING     - InvoiceNumber: STRING     - IsDiscounted: BOOLEAN     - LineAmountTypes: STRING     - LineItems: ARRAY, which is also a nested data structure.       - AccountCode: STRING       - Description: STRING       - DiscountRate: NUMBER       - ItemCode: STRING       - LineAmount: NUMBER       - LineItemID: STRING       - Quantity: NUMBER       - TaxAmount: NUMBER       - TaxType: STRING       - Tracking: ARRAY, which is also a nested data structure.         - Name: STRING         - Option: STRING         - Options: ARRAY, which is also a nested data structure.           - HasValidationErrors: BOOLEAN           - IsActive: BOOLEAN           - IsArchived: BOOLEAN           - IsDeleted: BOOLEAN           - Name: STRING           - Status: STRING           - TrackingOptionID: STRING         - Status: STRING         - TrackingCategoryID: STRING         - TrackingCategoryName: STRING         - TrackingOptionID: STRING         - TrackingOptionName: STRING       - UnitAmount: NUMBER     - PlannedPaymentDate: DATE-TIME     - Reference: STRING     - SentToContact: BOOLEAN     - Status: STRING     - SubTotal: NUMBER     - Total: NUMBER     - TotalDiscount: NUMBER     - TotalTax: NUMBER     - Type: STRING     - UpdatedDateUTC: DATE-TIME     - Url: STRING   - IsReconciled: BOOLEAN   - Overpayment: ARRAY, which is also a nested data structure.     - OverpaymentID: STRING   - PaymentID: STRING   - PaymentType: STRING   - Prepayments: ARRAY, which is also a nested data structure.     - PrepaymentID: STRING   - Reference: STRING   - Status: STRING   - UpdatedDateUTC: DATE-TIME - PrepaymentID: STRING - Reference: STRING - RemainingCredit: NUMBER - Status: STRING - SubTotal: NUMBER - Total: NUMBER - TotalTax: NUMBER - Type: STRING - UpdatedDateUTC: DATE-TIME |
| **Reference**  STRING |
| **SentToContact**  BOOLEAN |
| **Status**  STRING |
| **SubTotal**  NUMBER |
| **Total**  NUMBER |
| **TotalDiscount**  NUMBER |
| **TotalTax**  NUMBER |
| **Type**  STRING |
| **UpdatedDateUTC**  DATE-TIME |
| **Url**  STRING |

### items

The `items` table contains info about the [products and services you buy and sell](https://help.xero.com/us/Inventory).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ItemID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/items "Opens in new tab: Xero API method") |

items table schema

|  |
| --- |
| **Code**  STRING |
| **Description**  STRING |
| **InventoryAssetAccountCode**  STRING |
| **IsPurchased**  BOOLEAN |
| **IsSold**  BOOLEAN |
| **IsTrackedAsInventory**  BOOLEAN |
| **ItemID**  STRING |
| **Name**  STRING |
| **PurchaseDescription**  STRING |
| **PurchaseDetails**  OBJECT This is a nested data structure:   - AccountCode: STRING - COGSAccountCode: STRING - TaxType: STRING - UnitPrice: NUMBER |
| **QuantityOnHand**  NUMBER |
| **SalesDetails**  OBJECT This is a nested data structure:   - AccountCode: STRING - TaxType: STRING - UnitPrice: NUMBER |
| **TotalCostPool**  NUMBER |
| **UpdatedDateUTC**  DATE-TIME |

### journals

The `journals` table contains info about journal entries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | JournalID |
| **Replication Key** | JournalNumber |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/journals "Opens in new tab: Xero API method") |

journals table foreign keys

| Join journals with | on |
| --- | --- |
| [accounts](#accounts) | ``` journals.JournalLines.AccountID = accounts.AccountID ``` |
| [bank\_transactions](#bank-transactions) | ``` journals.JournalLines.AccountID = bank_transactions.BankAccount.AccountID ``` |
| [bank\_transfers](#bank-transfers) | ``` journals.JournalLines.AccountID = bank_transfers.FromBankAccount.AccountID ```  ``` journals.JournalLines.AccountID = bank_transfers.ToBankAccount.AccountID ``` |
| [payments](#payments) | ``` journals.JournalLines.AccountID = payments.Account.AccountID ``` |
| [tax\_rates](#tax-rates) | ``` journals.JournalLines.TaxName = tax_rates.Name ``` |
| [contacts](#contacts) | ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = contacts.SalesTrackingCategories.TrackingCategoryID ```  ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = contacts.PurchasesTrackingCategories.TrackingCategoryID ``` |
| [credit\_notes](#credit-notes) | ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ``` |
| [invoices](#invoices) | ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [manual\_journals](#manual-journals) | ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ``` |
| [overpayments](#overpayments) | ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ``` |
| [prepayments](#prepayments) | ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ``` |
| [purchase\_orders](#purchase-orders) | ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ``` |
| [receipts](#receipts) | ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [tracking\_categories](#tracking-categories) | ``` journals.JournalLines.TrackingCategories.TrackingCategoryID = tracking_categories.TrackingCategoryID ``` |

journals table schema

|  |
| --- |
| **CreatedDateUTC**  DATE-TIME |
| **JournalDate**  DATE-TIME |
| **JournalID**  STRING |
| **JournalLines**  ARRAY This is a nested data structure:   - AccountCode: STRING - AccountID: STRING - AccountName: STRING - AccountType: STRING - Description: STRING - GrossAmount: NUMBER - JournalLineID: STRING - NetAmount: NUMBER - TaxAmount: NUMBER - TaxName: STRING - TaxType: STRING - TrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING |
| **JournalNumber**  INTEGER |
| **Reference**  STRING |
| **SourceID**  STRING |
| **SourceType**  STRING |

### linked\_transactions

The `linked_transactions` table contains info about linked transactions. Linked transactions are transactions where line items from a purchase transaction to a customer are linked to a sales transaction.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | LinkedTransactionID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/linked-transactions "Opens in new tab: Xero API method") |

linked\_transactions table foreign keys

| Join linked\_transactions with | on |
| --- | --- |
| [bank\_transactions](#bank-transactions) | ``` linked_transactions.SourceTransactionID = bank_transactions.BankTransactionID ``` |
| [contacts](#contacts) | ``` linked_transactions.ContactID = contacts.ContactID ``` |
| [credit\_notes](#credit-notes) | ``` linked_transactions.ContactID = credit_notes.Contact.ContactID ``` |
| [invoices](#invoices) | ``` linked_transactions.ContactID = invoices.Contact.ContactID ```  ``` linked_transactions.SourceTransactionID = invoices.InvoiceID ```  ``` linked_transactions.TargetTransactionID = invoices.InvoiceID ``` |
| [overpayments](#overpayments) | ``` linked_transactions.ContactID = overpayments.Contact.ContactID ```  ``` linked_transactions.SourceTransactionID = overpayments.Allocations.Invoice.InvoiceID ```  ``` linked_transactions.TargetTransactionID = overpayments.Allocations.Invoice.InvoiceID ``` |
| [prepayments](#prepayments) | ``` linked_transactions.ContactID = prepayments.Contact.ContactID ```  ``` linked_transactions.SourceTransactionID = prepayments.Allocations.Invoice.InvoiceID ```  ``` linked_transactions.TargetTransactionID = prepayments.Allocations.Invoice.InvoiceID ``` |
| [receipts](#receipts) | ``` linked_transactions.ContactID = receipts.Contact.ContactID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` linked_transactions.ContactID = repeating_invoices.Contact.ContactID ``` |
| [payments](#payments) | ``` linked_transactions.SourceTransactionID = payments.Invoice.InvoiceID ```  ``` linked_transactions.TargetTransactionID = payments.Invoice.InvoiceID ``` |

linked\_transactions table schema

|  |
| --- |
| **ContactID**  STRING |
| **LinkedTransactionID**  STRING |
| **SourceLineItemID**  STRING |
| **SourceTransactionID**  STRING |
| **SourceTransactionTypeCode**  STRING |
| **Status**  STRING |
| **TargetLineItemID**  STRING |
| **TargetTransactionID**  STRING |
| **Type**  STRING |
| **UpdatedDateUTC**  DATE-TIME |

### manual\_journals

The `manual_journals` table contains info about manual journals, which are used by accountants or bookkeepers to work directly with a general ledger. For example: To record accrued expenses or completed work that wasn’t invoiced.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ManualJournalID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/manual-journals "Opens in new tab: Xero API method") |

manual\_journals table foreign keys

| Join manual\_journals with | on |
| --- | --- |
| [contacts](#contacts) | ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = contacts.SalesTrackingCategories.TrackingCategoryID ```  ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = contacts.PurchasesTrackingCategories.TrackingCategoryID ``` |
| [credit\_notes](#credit-notes) | ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ``` |
| [invoices](#invoices) | ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [journals](#journals) | ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ``` |
| [overpayments](#overpayments) | ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ``` |
| [prepayments](#prepayments) | ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ``` |
| [purchase\_orders](#purchase-orders) | ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ``` |
| [receipts](#receipts) | ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [tracking\_categories](#tracking-categories) | ``` manual_journals.JournalLines.Tracking.TrackingCategoryID = tracking_categories.TrackingCategoryID ``` |

manual\_journals table schema

|  |
| --- |
| **Date**  DATE-TIME |
| **HasAttachments**  BOOLEAN |
| **JournalLines**  ARRAY This is a nested data structure:   - AccountCode: STRING - AccountID: STRING - Description: STRING - IsBlank: BOOLEAN - LineAmount: NUMBER - TaxAmount: NUMBER - TaxType: STRING - Tracking: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING |
| **LineAmountTypes**  STRING |
| **ManualJournalID**  STRING |
| **Narration**  STRING |
| **ShowOnCashBasisReports**  BOOLEAN |
| **Status**  STRING |
| **UpdatedDateUTC**  DATE-TIME |
| **Url**  STRING |

### organisations

The `organisations` table contains info about the organisations in your Xero account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | OrganisationID |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/organisation "Opens in new tab: Xero API method") |

organisations table schema

|  |
| --- |
| **APIKey**  STRING |
| **Addresses**  ARRAY This is a nested data structure:   - AddressLine1: STRING - AddressLine2: STRING - AddressLine3: STRING - AddressLine4: STRING - AddressType: STRING - AttentionTo: STRING - City: STRING - Country: STRING - PostalCode: STRING - Region: STRING |
| **BaseCurrency**  STRING |
| **CountryCode**  STRING |
| **CreatedDateUTC**  DATE-TIME |
| **DefaultPurchasesTax**  STRING |
| **DefaultSalesTax**  STRING |
| **EndOfYearLockDate**  DATE-TIME |
| **ExternalLinks**  ARRAY This is a nested data structure:   - LinkType: STRING - Url: STRING |
| **FinancialYearEndDay**  INTEGER |
| **FinancialYearEndMonth**  INTEGER |
| **IsDemoCompany**  BOOLEAN |
| **LegalName**  STRING |
| **LineOfBusiness**  STRING |
| **Name**  STRING |
| **OrganisationEntityType**  STRING |
| **OrganisationID**  STRING |
| **OrganisationStatus**  STRING |
| **OrganisationType**  STRING |
| **PaymentTerms**  OBJECT  - Bills: OBJECT, which is also a nested data structure.   - Day: INTEGER   - Type: STRING - Sales: OBJECT, which is also a nested data structure.   - Day: INTEGER   - Type: STRING |
| **PaysTax**  BOOLEAN |
| **PeriodLockDate**  DATE-TIME |
| **Phones**  ARRAY This is a nested data structure:   - PhoneAreaCode: STRING - PhoneCountryCode: STRING - PhoneNumber: STRING - PhoneType: STRING |
| **RegistrationNumber**  STRING |
| **SalesTaxBasis**  STRING |
| **SalesTaxPeriod**  STRING |
| **ShortCode**  STRING |
| **TaxNumber**  STRING |
| **Timezone**  STRING |
| **Version**  STRING |

### overpayments

The `overpayments` table contains info about overpayments, which are transactions where a customer pays too much or you mistakenly overpay a supplier.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | OverpaymentID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/overpayments "Opens in new tab: Xero API method") |

overpayments table foreign keys

| Join overpayments with | on |
| --- | --- |
| [contacts](#contacts) | ``` overpayments.Contact.ContactID = contacts.ContactID ```  ``` overpayments.LineItems.Tracking.TrackingCategoryID = contacts.SalesTrackingCategories.TrackingCategoryID ```  ``` overpayments.LineItems.Tracking.TrackingCategoryID = contacts.PurchasesTrackingCategories.TrackingCategoryID ``` |
| [credit\_notes](#credit-notes) | ``` overpayments.Contact.ContactID = credit_notes.Contact.ContactID ```  ``` overpayments.LineItems.Tracking.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ``` |
| [invoices](#invoices) | ``` overpayments.Contact.ContactID = invoices.Contact.ContactID ```  ``` overpayments.Allocations.Invoice.InvoiceID = invoices.InvoiceID ```  ``` overpayments.OverpaymentID = invoices.Overpayments.Overpayment.OverpaymentID ```  ``` overpayments.Payments.PaymentID = invoices.Payments.PaymentID ```  ``` overpayments.LineItems.Tracking.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [linked\_transactions](#linked-transactions) | ``` overpayments.Contact.ContactID = linked_transactions.ContactID ```  ``` overpayments.Allocations.Invoice.InvoiceID = linked_transactions.SourceTransactionID ```  ``` overpayments.Allocations.Invoice.InvoiceID = linked_transactions.TargetTransactionID ``` |
| [prepayments](#prepayments) | ``` overpayments.Contact.ContactID = prepayments.Contact.ContactID ```  ``` overpayments.Allocations.Invoice.InvoiceID = prepayments.Allocations.Invoice.InvoiceID ```  ``` overpayments.LineItems.Tracking.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ``` |
| [receipts](#receipts) | ``` overpayments.Contact.ContactID = receipts.Contact.ContactID ```  ``` overpayments.LineItems.Tracking.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` overpayments.Contact.ContactID = repeating_invoices.Contact.ContactID ```  ``` overpayments.LineItems.Tracking.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [payments](#payments) | ``` overpayments.Allocations.Invoice.InvoiceID = payments.Invoice.InvoiceID ```  ``` overpayments.OverpaymentID = payments.Overpayment.OverpaymentID ```  ``` overpayments.Payments.PaymentID = payments.PaymentID ``` |
| [bank\_transactions](#bank-transactions) | ``` overpayments.OverpaymentID = bank_transactions.OverpaymentID ``` |
| [expense\_claims](#expense-claims) | ``` overpayments.Payments.PaymentID = expense_claims.Payments.PaymentID ``` |
| [journals](#journals) | ``` overpayments.LineItems.Tracking.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ``` |
| [manual\_journals](#manual-journals) | ``` overpayments.LineItems.Tracking.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ``` |
| [purchase\_orders](#purchase-orders) | ``` overpayments.LineItems.Tracking.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ``` |
| [tracking\_categories](#tracking-categories) | ``` overpayments.LineItems.Tracking.TrackingCategoryID = tracking_categories.TrackingCategoryID ``` |

overpayments table schema

|  |
| --- |
| **Allocations**  ARRAY This is a nested data structure:   - Amount: NUMBER - Date: DATE-TIME - Invoice: OBJECT, which is also a nested data structure.   - AmountCredited: NUMBER   - AmountDue: NUMBER   - AmountPaid: NUMBER   - BrandingThemeID: STRING   - Contact: OBJECT, which is also a nested data structure.     - AccountNumber: STRING     - AccountsPayableTaxType: STRING     - AccountsReceivableTaxType: STRING     - Addresses: ARRAY, which is also a nested data structure.       - AddressLine1: STRING       - AddressLine2: STRING       - AddressLine3: STRING       - AddressLine4: STRING       - AddressType: STRING       - AttentionTo: STRING       - City: STRING       - Country: STRING       - PostalCode: STRING       - Region: STRING     - Attachments: ARRAY     - Balances: OBJECT, which is also a nested data structure.       - AccountsPayable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER       - AccountsReceivable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER     - BankAccountDetails: STRING     - BatchPayments: OBJECT, which is also a nested data structure.       - BankAccountName: STRING       - BankAccountNumber: STRING       - Code: STRING       - Details: STRING       - Reference: STRING     - BrandingTheme: OBJECT, which is also a nested data structure.       - BrandingThemeID: STRING       - CreatedDateUTC: DARE-TIME       - Name: STRING       - SortOrder: INTEGER     - ContactGroups: ARRAY, which is also a nested data structure.       - ContactGroupID: STRING       - HasValidationErrors: BOOLEAN       - Name: STRING       - Status: STRING     - ContactID: STRING     - ContactNumber: STRING     - ContactPersons: ARRAY, which is also a nested data structure.       - EmailAddress: STRING       - FirstName: STRING       - IncludeInEmails: BOOLEAN       - LastName: STRING     - ContactStatus: STRING     - DefaultCurrency: STRING     - Discount: NUMBER     - EmailAddress: STRING     - FirstName: STRING     - HasAttachments: BOOLEAN     - HasValidationErrors: BOOLEAN     - IsCustomer: BOOLEAN     - IsSupplier: BOOLEAN     - LastName: STRING     - Name: STRING     - PaymentTerms: OBJECT, which is also a nested data structure.       - Bills: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING       - Sales: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING     - Phones: ARRAY, which is also a nested data structure.       - PhoneAreaCode: STRING       - PhoneCountryCode: STRING       - PhoneNumber: STRING       - PhoneType: STRING     - PurchasesDefaultAccountCode: STRING     - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SalesDefaultAccountCode: STRING     - SalesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SkypeUserName: STRING     - TaxNumber: STRING     - TrackingCategoryName: STRING     - TrackingCategoryOption: STRING     - UpdatedDateUTC: DATE-TIME     - ValidationErrors: ARRAY, which is also a nested data structure.       - Message: STRING     - Website: STRING     - XeroNetworkKey: STRING   - CurrencyCode: STRING   - CurrencyRate: NUMBER   - Date: DATE-TIME   - DateString: DATE-TIME   - DueDate: DATE-TIME   - DueDateString: DATE-TIME   - ExpectedPaymentDate: DATE-TIME   - FullyPaidOnDate: DATE-TIME   - HasAttachments: BOOLEAN   - HasErrors: BOOLEAN   - InvoiceID: STRING   - InvoiceNumber: STRING   - IsDiscounted: BOOLEAN   - LineAmountTypes: STRING   - LineItems: ARRAY, which is also a nested data structure.     - AccountCode: STRING     - Description: STRING     - DiscountRate: NUMBER     - ItemCode: STRING     - LineAmount: NUMBER     - LineItemID: STRING     - Quantity: NUMBER     - TaxAmount: NUMBER     - TaxType: STRING     - Tracking: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - UnitAmount: NUMBER   - PlannedPaymentDate: DATE-TIME   - Reference: STRING   - SentToContact: BOOLEAN   - Status: STRING   - SubTotal: NUMBER   - Total: NUMBER   - TotalDiscount: NUMBER   - TotalTax: NUMBER   - Type: STRING   - UpdatedDateUTC: DATE-TIME   - Url: STRING |
| **AppliedAmount**  NUMBER |
| **Contact**  OBJECT This is a nested data structure:   - AccountNumber: STRING - AccountsPayableTaxType: STRING - AccountsReceivableTaxType: STRING - Addresses: ARRAY, which is also a nested data structure.   - AddressLine1: STRING   - AddressLine2: STRING   - AddressLine3: STRING   - AddressLine4: STRING   - AddressType: STRING   - AttentionTo: STRING   - City: STRING   - Country: STRING   - PostalCode: STRING   - Region: STRING - Attachments: ARRAY - Balances: OBJECT, which is also a nested data structure.   - AccountsPayable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER   - AccountsReceivable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER - BankAccountDetails: STRING - BatchPayments: OBJECT, which is also a nested data structure.   - BankAccountName: STRING   - BankAccountNumber: STRING   - Code: STRING   - Details: STRING   - Reference: STRING - BrandingTheme: OBJECT, which is also a nested data structure.   - BrandingThemeID: STRING   - CreatedDateUTC: DARE-TIME   - Name: STRING   - SortOrder: INTEGER - ContactGroups: ARRAY, which is also a nested data structure.   - ContactGroupID: STRING   - HasValidationErrors: BOOLEAN   - Name: STRING   - Status: STRING - ContactID: STRING - ContactNumber: STRING - ContactPersons: ARRAY, which is also a nested data structure.   - EmailAddress: STRING   - FirstName: STRING   - IncludeInEmails: BOOLEAN   - LastName: STRING - ContactStatus: STRING - DefaultCurrency: STRING - Discount: NUMBER - EmailAddress: STRING - FirstName: STRING - HasAttachments: BOOLEAN - HasValidationErrors: BOOLEAN - IsCustomer: BOOLEAN - IsSupplier: BOOLEAN - LastName: STRING - Name: STRING - PaymentTerms: OBJECT, which is also a nested data structure.   - Bills: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING   - Sales: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING - Phones: ARRAY, which is also a nested data structure.   - PhoneAreaCode: STRING   - PhoneCountryCode: STRING   - PhoneNumber: STRING   - PhoneType: STRING - PurchasesDefaultAccountCode: STRING - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SalesDefaultAccountCode: STRING - SalesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SkypeUserName: STRING - TaxNumber: STRING - TrackingCategoryName: STRING - TrackingCategoryOption: STRING - UpdatedDateUTC: DATE-TIME - ValidationErrors: ARRAY, which is also a nested data structure.   - Message: STRING - Website: STRING - XeroNetworkKey: STRING |
| **CurrencyCode**  STRING |
| **CurrencyRate**  NUMBER |
| **Date**  DATE-TIME |
| **DateString**  DATE-TIME |
| **HasAttachments**  BOOLEAN |
| **ID**  STRING |
| **LineAmountTypes**  STRING |
| **LineItems**  ARRAY This is a nested data structure:   - AccountCode: STRING - Description: STRING - DiscountRate: NUMBER - ItemCode: STRING - LineAmount: NUMBER - LineItemID: STRING - Quantity: NUMBER - TaxAmount: NUMBER - TaxType: STRING - Tracking: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - UnitAmount: NUMBER |
| **OverpaymentID**  STRING |
| **Payments**  ARRAY This is a nested data structure:   - Account: OBJECT, which is also a nested data structure.   - AccountID: STRING   - BankAccountNumber: STRING   - BankAccountType: STRING   - Class: STRING   - Code: STRING   - CurrencyCode: STRING   - Description: STRING   - EnablePaymentsToAccount: BOOLEAN   - HasAttachments: BOOLEAN   - Name: STRING   - ReportingCode: STRING   - ReportingCodeName: STRING   - ShowInExpenseClaims: BOOLEAN   - Status: STRING   - SystemAccount: STRING   - TaxType: STRING   - Type: STRING   - UpdatedDateUTC: DATE-TIME - Amount: NUMBER - BankAmount: NUMBER - BatchPaymentID: STRING - CreditNote: OBJECT, which is also a nested data structure.   - CreditNoteNumber: STRING - CurrencyRate: NUMBER - Date: DATE-TIME - HasAccount: BOOLEAN - HasValidationErrors: BOOLEAN - Invoice: OBJECT, which is also a nested data structure.   - AmountCredited: NUMBER   - AmountDue: NUMBER   - AmountPaid: NUMBER   - BrandingThemeID: STRING   - Contact: OBJECT, which is also a nested data structure.     - AccountNumber: STRING     - AccountsPayableTaxType: STRING     - AccountsReceivableTaxType: STRING     - Addresses: ARRAY, which is also a nested data structure.       - AddressLine1: STRING       - AddressLine2: STRING       - AddressLine3: STRING       - AddressLine4: STRING       - AddressType: STRING       - AttentionTo: STRING       - City: STRING       - Country: STRING       - PostalCode: STRING       - Region: STRING     - Attachments: ARRAY     - Balances: OBJECT, which is also a nested data structure.       - AccountsPayable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER       - AccountsReceivable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER     - BankAccountDetails: STRING     - BatchPayments: OBJECT, which is also a nested data structure.       - BankAccountName: STRING       - BankAccountNumber: STRING       - Code: STRING       - Details: STRING       - Reference: STRING     - BrandingTheme: OBJECT, which is also a nested data structure.       - BrandingThemeID: STRING       - CreatedDateUTC: DARE-TIME       - Name: STRING       - SortOrder: INTEGER     - ContactGroups: ARRAY, which is also a nested data structure.       - ContactGroupID: STRING       - HasValidationErrors: BOOLEAN       - Name: STRING       - Status: STRING     - ContactID: STRING     - ContactNumber: STRING     - ContactPersons: ARRAY, which is also a nested data structure.       - EmailAddress: STRING       - FirstName: STRING       - IncludeInEmails: BOOLEAN       - LastName: STRING     - ContactStatus: STRING     - DefaultCurrency: STRING     - Discount: NUMBER     - EmailAddress: STRING     - FirstName: STRING     - HasAttachments: BOOLEAN     - HasValidationErrors: BOOLEAN     - IsCustomer: BOOLEAN     - IsSupplier: BOOLEAN     - LastName: STRING     - Name: STRING     - PaymentTerms: OBJECT, which is also a nested data structure.       - Bills: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING       - Sales: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING     - Phones: ARRAY, which is also a nested data structure.       - PhoneAreaCode: STRING       - PhoneCountryCode: STRING       - PhoneNumber: STRING       - PhoneType: STRING     - PurchasesDefaultAccountCode: STRING     - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SalesDefaultAccountCode: STRING     - SalesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SkypeUserName: STRING     - TaxNumber: STRING     - TrackingCategoryName: STRING     - TrackingCategoryOption: STRING     - UpdatedDateUTC: DATE-TIME     - ValidationErrors: ARRAY, which is also a nested data structure.       - Message: STRING     - Website: STRING     - XeroNetworkKey: STRING   - CurrencyCode: STRING   - CurrencyRate: NUMBER   - Date: DATE-TIME   - DateString: DATE-TIME   - DueDate: DATE-TIME   - DueDateString: DATE-TIME   - ExpectedPaymentDate: DATE-TIME   - FullyPaidOnDate: DATE-TIME   - HasAttachments: BOOLEAN   - HasErrors: BOOLEAN   - InvoiceID: STRING   - InvoiceNumber: STRING   - IsDiscounted: BOOLEAN   - LineAmountTypes: STRING   - LineItems: ARRAY, which is also a nested data structure.     - AccountCode: STRING     - Description: STRING     - DiscountRate: NUMBER     - ItemCode: STRING     - LineAmount: NUMBER     - LineItemID: STRING     - Quantity: NUMBER     - TaxAmount: NUMBER     - TaxType: STRING     - Tracking: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - UnitAmount: NUMBER   - PlannedPaymentDate: DATE-TIME   - Reference: STRING   - SentToContact: BOOLEAN   - Status: STRING   - SubTotal: NUMBER   - Total: NUMBER   - TotalDiscount: NUMBER   - TotalTax: NUMBER   - Type: STRING   - UpdatedDateUTC: DATE-TIME   - Url: STRING - IsReconciled: BOOLEAN - Overpayment: ARRAY, which is also a nested data structure.   - OverpaymentID: STRING - PaymentID: STRING - PaymentType: STRING - Prepayments: ARRAY, which is also a nested data structure.   - PrepaymentID: STRING - Reference: STRING - Status: STRING - UpdatedDateUTC: DATE-TIME |
| **Reference**  STRING |
| **RemainingCredit**  NUMBER |
| **Status**  STRING |
| **SubTotal**  NUMBER |
| **Total**  NUMBER |
| **TotalTax**  NUMBER |
| **Type**  STRING |
| **UpdatedDateUTC**  DATE-TIME |

### payments

The `payments` table contains info about the payments recorded in your Xero account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | PaymentID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/payments "Opens in new tab: Xero API method") |

payments table foreign keys

| Join payments with | on |
| --- | --- |
| [accounts](#accounts) | ``` payments.Account.AccountID = accounts.AccountID ``` |
| [bank\_transactions](#bank-transactions) | ``` payments.Account.AccountID = bank_transactions.BankAccount.AccountID ```  ``` payments.Overpayment.OverpaymentID = bank_transactions.OverpaymentID ```  ``` payments.Prepayments.PrepaymentID = bank_transactions.PrepaymentID ``` |
| [bank\_transfers](#bank-transfers) | ``` payments.Account.AccountID = bank_transfers.FromBankAccount.AccountID ```  ``` payments.Account.AccountID = bank_transfers.ToBankAccount.AccountID ``` |
| [journals](#journals) | ``` payments.Account.AccountID = journals.JournalLines.AccountID ``` |
| [invoices](#invoices) | ``` payments.Invoice.InvoiceID = invoices.InvoiceID ```  ``` payments.Overpayment.OverpaymentID = invoices.Overpayments.Overpayment.OverpaymentID ```  ``` payments.PaymentID = invoices.Payments.PaymentID ```  ``` payments.Prepayments.PrepaymentID = invoices.Prepayments.PrepaymentID ``` |
| [linked\_transactions](#linked-transactions) | ``` payments.Invoice.InvoiceID = linked_transactions.SourceTransactionID ```  ``` payments.Invoice.InvoiceID = linked_transactions.TargetTransactionID ``` |
| [overpayments](#overpayments) | ``` payments.Invoice.InvoiceID = overpayments.Allocations.Invoice.InvoiceID ```  ``` payments.Overpayment.OverpaymentID = overpayments.OverpaymentID ```  ``` payments.PaymentID = overpayments.Payments.PaymentID ``` |
| [prepayments](#prepayments) | ``` payments.Invoice.InvoiceID = prepayments.Allocations.Invoice.InvoiceID ```  ``` payments.Prepayments.PrepaymentID = prepayments.PrepaymentID ``` |
| [expense\_claims](#expense-claims) | ``` payments.PaymentID = expense_claims.Payments.PaymentID ``` |

payments table schema

|  |
| --- |
| **Account**  OBJECT This is a nested data structure:   - AccountID: STRING - BankAccountNumber: STRING - BankAccountType: STRING - Class: STRING - Code: STRING - CurrencyCode: STRING - Description: STRING - EnablePaymentsToAccount: BOOLEAN - HasAttachments: BOOLEAN - Name: STRING - ReportingCode: STRING - ReportingCodeName: STRING - ShowInExpenseClaims: BOOLEAN - Status: STRING - SystemAccount: STRING - TaxType: STRING - Type: STRING - UpdatedDateUTC: DATE-TIME |
| **Amount**  NUMBER |
| **BankAmount**  NUMBER |
| **BatchPaymentID**  STRING |
| **CreditNote**  OBJECT This is a nested data structure:   - CreditNoteNumber: STRING |
| **CurrencyRate**  NUMBER |
| **Date**  DATE-TIME |
| **HasAccount**  BOOLEAN |
| **HasValidationErrors**  BOOLEAN |
| **Invoice**  OBJECT This is a nested data structure:   - AmountCredited: NUMBER - AmountDue: NUMBER - AmountPaid: NUMBER - BrandingThemeID: STRING - Contact: OBJECT, which is also a nested data structure.   - AccountNumber: STRING   - AccountsPayableTaxType: STRING   - AccountsReceivableTaxType: STRING   - Addresses: ARRAY, which is also a nested data structure.     - AddressLine1: STRING     - AddressLine2: STRING     - AddressLine3: STRING     - AddressLine4: STRING     - AddressType: STRING     - AttentionTo: STRING     - City: STRING     - Country: STRING     - PostalCode: STRING     - Region: STRING   - Attachments: ARRAY   - Balances: OBJECT, which is also a nested data structure.     - AccountsPayable: OBJECT, which is also a nested data structure.       - Outstanding: NUMBER       - Overdue: NUMBER     - AccountsReceivable: OBJECT, which is also a nested data structure.       - Outstanding: NUMBER       - Overdue: NUMBER   - BankAccountDetails: STRING   - BatchPayments: OBJECT, which is also a nested data structure.     - BankAccountName: STRING     - BankAccountNumber: STRING     - Code: STRING     - Details: STRING     - Reference: STRING   - BrandingTheme: OBJECT, which is also a nested data structure.     - BrandingThemeID: STRING     - CreatedDateUTC: DARE-TIME     - Name: STRING     - SortOrder: INTEGER   - ContactGroups: ARRAY, which is also a nested data structure.     - ContactGroupID: STRING     - HasValidationErrors: BOOLEAN     - Name: STRING     - Status: STRING   - ContactID: STRING   - ContactNumber: STRING   - ContactPersons: ARRAY, which is also a nested data structure.     - EmailAddress: STRING     - FirstName: STRING     - IncludeInEmails: BOOLEAN     - LastName: STRING   - ContactStatus: STRING   - DefaultCurrency: STRING   - Discount: NUMBER   - EmailAddress: STRING   - FirstName: STRING   - HasAttachments: BOOLEAN   - HasValidationErrors: BOOLEAN   - IsCustomer: BOOLEAN   - IsSupplier: BOOLEAN   - LastName: STRING   - Name: STRING   - PaymentTerms: OBJECT, which is also a nested data structure.     - Bills: OBJECT, which is also a nested data structure.       - Day: INTEGER       - Type: STRING     - Sales: OBJECT, which is also a nested data structure.       - Day: INTEGER       - Type: STRING   - Phones: ARRAY, which is also a nested data structure.     - PhoneAreaCode: STRING     - PhoneCountryCode: STRING     - PhoneNumber: STRING     - PhoneType: STRING   - PurchasesDefaultAccountCode: STRING   - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - SalesDefaultAccountCode: STRING   - SalesTrackingCategories: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - SkypeUserName: STRING   - TaxNumber: STRING   - TrackingCategoryName: STRING   - TrackingCategoryOption: STRING   - UpdatedDateUTC: DATE-TIME   - ValidationErrors: ARRAY, which is also a nested data structure.     - Message: STRING   - Website: STRING   - XeroNetworkKey: STRING - CurrencyCode: STRING - CurrencyRate: NUMBER - Date: DATE-TIME - DateString: DATE-TIME - DueDate: DATE-TIME - DueDateString: DATE-TIME - ExpectedPaymentDate: DATE-TIME - FullyPaidOnDate: DATE-TIME - HasAttachments: BOOLEAN - HasErrors: BOOLEAN - InvoiceID: STRING - InvoiceNumber: STRING - IsDiscounted: BOOLEAN - LineAmountTypes: STRING - LineItems: ARRAY, which is also a nested data structure.   - AccountCode: STRING   - Description: STRING   - DiscountRate: NUMBER   - ItemCode: STRING   - LineAmount: NUMBER   - LineItemID: STRING   - Quantity: NUMBER   - TaxAmount: NUMBER   - TaxType: STRING   - Tracking: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - UnitAmount: NUMBER - PlannedPaymentDate: DATE-TIME - Reference: STRING - SentToContact: BOOLEAN - Status: STRING - SubTotal: NUMBER - Total: NUMBER - TotalDiscount: NUMBER - TotalTax: NUMBER - Type: STRING - UpdatedDateUTC: DATE-TIME - Url: STRING |
| **IsReconciled**  BOOLEAN |
| **Overpayment**  ARRAY This is a nested data structure:   - OverpaymentID: STRING |
| **PaymentID**  STRING |
| **PaymentType**  STRING |
| **Prepayments**  ARRAY This is a nested data structure:   - PrepaymentID: STRING |
| **Reference**  STRING |
| **Status**  STRING |
| **UpdatedDateUTC**  DATE-TIME |

### prepayments

The `prepayments` table contains info about prepayments, which are payments made in advance of an invoice being raised for a customer or a bill being received from a supplier.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | PrepaymentID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/prepayments "Opens in new tab: Xero API method") |

prepayments table foreign keys

| Join prepayments with | on |
| --- | --- |
| [contacts](#contacts) | ``` prepayments.Contact.ContactID = contacts.ContactID ```  ``` prepayments.LineItems.Tracking.TrackingCategoryID = contacts.SalesTrackingCategories.TrackingCategoryID ```  ``` prepayments.LineItems.Tracking.TrackingCategoryID = contacts.PurchasesTrackingCategories.TrackingCategoryID ``` |
| [credit\_notes](#credit-notes) | ``` prepayments.Contact.ContactID = credit_notes.Contact.ContactID ```  ``` prepayments.CurrencyCode = credit_notes.CurrencyCode ```  ``` prepayments.LineItems.Tracking.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ``` |
| [invoices](#invoices) | ``` prepayments.Contact.ContactID = invoices.Contact.ContactID ```  ``` prepayments.CurrencyCode = invoices.CurrencyCode ```  ``` prepayments.Allocations.Invoice.InvoiceID = invoices.InvoiceID ```  ``` prepayments.PrepaymentID = invoices.Prepayments.PrepaymentID ```  ``` prepayments.LineItems.Tracking.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [linked\_transactions](#linked-transactions) | ``` prepayments.Contact.ContactID = linked_transactions.ContactID ```  ``` prepayments.Allocations.Invoice.InvoiceID = linked_transactions.SourceTransactionID ```  ``` prepayments.Allocations.Invoice.InvoiceID = linked_transactions.TargetTransactionID ``` |
| [overpayments](#overpayments) | ``` prepayments.Contact.ContactID = overpayments.Contact.ContactID ```  ``` prepayments.Allocations.Invoice.InvoiceID = overpayments.Allocations.Invoice.InvoiceID ```  ``` prepayments.LineItems.Tracking.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ``` |
| [receipts](#receipts) | ``` prepayments.Contact.ContactID = receipts.Contact.ContactID ```  ``` prepayments.LineItems.Tracking.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` prepayments.Contact.ContactID = repeating_invoices.Contact.ContactID ```  ``` prepayments.CurrencyCode = repeating_invoices.CurrencyCode ```  ``` prepayments.LineItems.Tracking.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [accounts](#accounts) | ``` prepayments.CurrencyCode = accounts.CurrencyCode ``` |
| [bank\_transactions](#bank-transactions) | ``` prepayments.CurrencyCode = bank_transactions.CurrencyCode ```  ``` prepayments.PrepaymentID = bank_transactions.PrepaymentID ``` |
| [currencies](#currencies) | ``` prepayments.CurrencyCode = currencies.Code ``` |
| [purchase\_orders](#purchase-orders) | ``` prepayments.CurrencyCode = purchase_orders.CurrencyCode ```  ``` prepayments.LineItems.Tracking.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ``` |
| [payments](#payments) | ``` prepayments.Allocations.Invoice.InvoiceID = payments.Invoice.InvoiceID ```  ``` prepayments.PrepaymentID = payments.Prepayments.PrepaymentID ``` |
| [journals](#journals) | ``` prepayments.LineItems.Tracking.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ``` |
| [manual\_journals](#manual-journals) | ``` prepayments.LineItems.Tracking.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ``` |
| [tracking\_categories](#tracking-categories) | ``` prepayments.LineItems.Tracking.TrackingCategoryID = tracking_categories.TrackingCategoryID ``` |

prepayments table schema

|  |
| --- |
| **Allocations**  ARRAY This is a nested data structure:   - Amount: NUMBER - Date: DATE-TIME - Invoice: OBJECT, which is also a nested data structure.   - AmountCredited: NUMBER   - AmountDue: NUMBER   - AmountPaid: NUMBER   - BrandingThemeID: STRING   - Contact: OBJECT, which is also a nested data structure.     - AccountNumber: STRING     - AccountsPayableTaxType: STRING     - AccountsReceivableTaxType: STRING     - Addresses: ARRAY, which is also a nested data structure.       - AddressLine1: STRING       - AddressLine2: STRING       - AddressLine3: STRING       - AddressLine4: STRING       - AddressType: STRING       - AttentionTo: STRING       - City: STRING       - Country: STRING       - PostalCode: STRING       - Region: STRING     - Attachments: ARRAY     - Balances: OBJECT, which is also a nested data structure.       - AccountsPayable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER       - AccountsReceivable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER     - BankAccountDetails: STRING     - BatchPayments: OBJECT, which is also a nested data structure.       - BankAccountName: STRING       - BankAccountNumber: STRING       - Code: STRING       - Details: STRING       - Reference: STRING     - BrandingTheme: OBJECT, which is also a nested data structure.       - BrandingThemeID: STRING       - CreatedDateUTC: DARE-TIME       - Name: STRING       - SortOrder: INTEGER     - ContactGroups: ARRAY, which is also a nested data structure.       - ContactGroupID: STRING       - HasValidationErrors: BOOLEAN       - Name: STRING       - Status: STRING     - ContactID: STRING     - ContactNumber: STRING     - ContactPersons: ARRAY, which is also a nested data structure.       - EmailAddress: STRING       - FirstName: STRING       - IncludeInEmails: BOOLEAN       - LastName: STRING     - ContactStatus: STRING     - DefaultCurrency: STRING     - Discount: NUMBER     - EmailAddress: STRING     - FirstName: STRING     - HasAttachments: BOOLEAN     - HasValidationErrors: BOOLEAN     - IsCustomer: BOOLEAN     - IsSupplier: BOOLEAN     - LastName: STRING     - Name: STRING     - PaymentTerms: OBJECT, which is also a nested data structure.       - Bills: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING       - Sales: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING     - Phones: ARRAY, which is also a nested data structure.       - PhoneAreaCode: STRING       - PhoneCountryCode: STRING       - PhoneNumber: STRING       - PhoneType: STRING     - PurchasesDefaultAccountCode: STRING     - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SalesDefaultAccountCode: STRING     - SalesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SkypeUserName: STRING     - TaxNumber: STRING     - TrackingCategoryName: STRING     - TrackingCategoryOption: STRING     - UpdatedDateUTC: DATE-TIME     - ValidationErrors: ARRAY, which is also a nested data structure.       - Message: STRING     - Website: STRING     - XeroNetworkKey: STRING   - CurrencyCode: STRING   - CurrencyRate: NUMBER   - Date: DATE-TIME   - DateString: DATE-TIME   - DueDate: DATE-TIME   - DueDateString: DATE-TIME   - ExpectedPaymentDate: DATE-TIME   - FullyPaidOnDate: DATE-TIME   - HasAttachments: BOOLEAN   - HasErrors: BOOLEAN   - InvoiceID: STRING   - InvoiceNumber: STRING   - IsDiscounted: BOOLEAN   - LineAmountTypes: STRING   - LineItems: ARRAY, which is also a nested data structure.     - AccountCode: STRING     - Description: STRING     - DiscountRate: NUMBER     - ItemCode: STRING     - LineAmount: NUMBER     - LineItemID: STRING     - Quantity: NUMBER     - TaxAmount: NUMBER     - TaxType: STRING     - Tracking: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - UnitAmount: NUMBER   - PlannedPaymentDate: DATE-TIME   - Reference: STRING   - SentToContact: BOOLEAN   - Status: STRING   - SubTotal: NUMBER   - Total: NUMBER   - TotalDiscount: NUMBER   - TotalTax: NUMBER   - Type: STRING   - UpdatedDateUTC: DATE-TIME   - Url: STRING |
| **AppliedAmount**  NUMBER |
| **Contact**  OBJECT  - AccountNumber: STRING - AccountsPayableTaxType: STRING - AccountsReceivableTaxType: STRING - Addresses: ARRAY, which is also a nested data structure.   - AddressLine1: STRING   - AddressLine2: STRING   - AddressLine3: STRING   - AddressLine4: STRING   - AddressType: STRING   - AttentionTo: STRING   - City: STRING   - Country: STRING   - PostalCode: STRING   - Region: STRING - Attachments: ARRAY - Balances: OBJECT, which is also a nested data structure.   - AccountsPayable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER   - AccountsReceivable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER - BankAccountDetails: STRING - BatchPayments: OBJECT, which is also a nested data structure.   - BankAccountName: STRING   - BankAccountNumber: STRING   - Code: STRING   - Details: STRING   - Reference: STRING - BrandingTheme: OBJECT, which is also a nested data structure.   - BrandingThemeID: STRING   - CreatedDateUTC: DARE-TIME   - Name: STRING   - SortOrder: INTEGER - ContactGroups: ARRAY, which is also a nested data structure.   - ContactGroupID: STRING   - HasValidationErrors: BOOLEAN   - Name: STRING   - Status: STRING - ContactID: STRING - ContactNumber: STRING - ContactPersons: ARRAY, which is also a nested data structure.   - EmailAddress: STRING   - FirstName: STRING   - IncludeInEmails: BOOLEAN   - LastName: STRING - ContactStatus: STRING - DefaultCurrency: STRING - Discount: NUMBER - EmailAddress: STRING - FirstName: STRING - HasAttachments: BOOLEAN - HasValidationErrors: BOOLEAN - IsCustomer: BOOLEAN - IsSupplier: BOOLEAN - LastName: STRING - Name: STRING - PaymentTerms: OBJECT, which is also a nested data structure.   - Bills: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING   - Sales: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING - Phones: ARRAY, which is also a nested data structure.   - PhoneAreaCode: STRING   - PhoneCountryCode: STRING   - PhoneNumber: STRING   - PhoneType: STRING - PurchasesDefaultAccountCode: STRING - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SalesDefaultAccountCode: STRING - SalesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SkypeUserName: STRING - TaxNumber: STRING - TrackingCategoryName: STRING - TrackingCategoryOption: STRING - UpdatedDateUTC: DATE-TIME - ValidationErrors: ARRAY, which is also a nested data structure.   - Message: STRING - Website: STRING - XeroNetworkKey: STRING |
| **CurrencyCode**  STRING |
| **CurrencyRate**  NUMBER |
| **Date**  DATE-TIME |
| **DateString**  DATE-TIME |
| **HasAttachments**  BOOLEAN |
| **ID**  STRING |
| **LineAmountTypes**  STRING |
| **LineItems**  ARRAY This is a nested data structure:   - AccountCode: STRING - Description: STRING - DiscountRate: NUMBER - ItemCode: STRING - LineAmount: NUMBER - LineItemID: STRING - Quantity: NUMBER - TaxAmount: NUMBER - TaxType: STRING - Tracking: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - UnitAmount: NUMBER |
| **Payments**  ARRAY This is a nested data structure:   - Account: OBJECT, which is also a nested data structure.   - AccountID: STRING   - BankAccountNumber: STRING   - BankAccountType: STRING   - Class: STRING   - Code: STRING   - CurrencyCode: STRING   - Description: STRING   - EnablePaymentsToAccount: BOOLEAN   - HasAttachments: BOOLEAN   - Name: STRING   - ReportingCode: STRING   - ReportingCodeName: STRING   - ShowInExpenseClaims: BOOLEAN   - Status: STRING   - SystemAccount: STRING   - TaxType: STRING   - Type: STRING   - UpdatedDateUTC: DATE-TIME - Amount: NUMBER - BankAmount: NUMBER - BatchPaymentID: STRING - CreditNote: OBJECT, which is also a nested data structure.   - CreditNoteNumber: STRING - CurrencyRate: NUMBER - Date: DATE-TIME - HasAccount: BOOLEAN - HasValidationErrors: BOOLEAN - Invoice: OBJECT, which is also a nested data structure.   - AmountCredited: NUMBER   - AmountDue: NUMBER   - AmountPaid: NUMBER   - BrandingThemeID: STRING   - Contact: OBJECT, which is also a nested data structure.     - AccountNumber: STRING     - AccountsPayableTaxType: STRING     - AccountsReceivableTaxType: STRING     - Addresses: ARRAY, which is also a nested data structure.       - AddressLine1: STRING       - AddressLine2: STRING       - AddressLine3: STRING       - AddressLine4: STRING       - AddressType: STRING       - AttentionTo: STRING       - City: STRING       - Country: STRING       - PostalCode: STRING       - Region: STRING     - Attachments: ARRAY     - Balances: OBJECT, which is also a nested data structure.       - AccountsPayable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER       - AccountsReceivable: OBJECT, which is also a nested data structure.         - Outstanding: NUMBER         - Overdue: NUMBER     - BankAccountDetails: STRING     - BatchPayments: OBJECT, which is also a nested data structure.       - BankAccountName: STRING       - BankAccountNumber: STRING       - Code: STRING       - Details: STRING       - Reference: STRING     - BrandingTheme: OBJECT, which is also a nested data structure.       - BrandingThemeID: STRING       - CreatedDateUTC: DARE-TIME       - Name: STRING       - SortOrder: INTEGER     - ContactGroups: ARRAY, which is also a nested data structure.       - ContactGroupID: STRING       - HasValidationErrors: BOOLEAN       - Name: STRING       - Status: STRING     - ContactID: STRING     - ContactNumber: STRING     - ContactPersons: ARRAY, which is also a nested data structure.       - EmailAddress: STRING       - FirstName: STRING       - IncludeInEmails: BOOLEAN       - LastName: STRING     - ContactStatus: STRING     - DefaultCurrency: STRING     - Discount: NUMBER     - EmailAddress: STRING     - FirstName: STRING     - HasAttachments: BOOLEAN     - HasValidationErrors: BOOLEAN     - IsCustomer: BOOLEAN     - IsSupplier: BOOLEAN     - LastName: STRING     - Name: STRING     - PaymentTerms: OBJECT, which is also a nested data structure.       - Bills: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING       - Sales: OBJECT, which is also a nested data structure.         - Day: INTEGER         - Type: STRING     - Phones: ARRAY, which is also a nested data structure.       - PhoneAreaCode: STRING       - PhoneCountryCode: STRING       - PhoneNumber: STRING       - PhoneType: STRING     - PurchasesDefaultAccountCode: STRING     - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SalesDefaultAccountCode: STRING     - SalesTrackingCategories: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - SkypeUserName: STRING     - TaxNumber: STRING     - TrackingCategoryName: STRING     - TrackingCategoryOption: STRING     - UpdatedDateUTC: DATE-TIME     - ValidationErrors: ARRAY, which is also a nested data structure.       - Message: STRING     - Website: STRING     - XeroNetworkKey: STRING   - CurrencyCode: STRING   - CurrencyRate: NUMBER   - Date: DATE-TIME   - DateString: DATE-TIME   - DueDate: DATE-TIME   - DueDateString: DATE-TIME   - ExpectedPaymentDate: DATE-TIME   - FullyPaidOnDate: DATE-TIME   - HasAttachments: BOOLEAN   - HasErrors: BOOLEAN   - InvoiceID: STRING   - InvoiceNumber: STRING   - IsDiscounted: BOOLEAN   - LineAmountTypes: STRING   - LineItems: ARRAY, which is also a nested data structure.     - AccountCode: STRING     - Description: STRING     - DiscountRate: NUMBER     - ItemCode: STRING     - LineAmount: NUMBER     - LineItemID: STRING     - Quantity: NUMBER     - TaxAmount: NUMBER     - TaxType: STRING     - Tracking: ARRAY, which is also a nested data structure.       - Name: STRING       - Option: STRING       - Options: ARRAY, which is also a nested data structure.         - HasValidationErrors: BOOLEAN         - IsActive: BOOLEAN         - IsArchived: BOOLEAN         - IsDeleted: BOOLEAN         - Name: STRING         - Status: STRING         - TrackingOptionID: STRING       - Status: STRING       - TrackingCategoryID: STRING       - TrackingCategoryName: STRING       - TrackingOptionID: STRING       - TrackingOptionName: STRING     - UnitAmount: NUMBER   - PlannedPaymentDate: DATE-TIME   - Reference: STRING   - SentToContact: BOOLEAN   - Status: STRING   - SubTotal: NUMBER   - Total: NUMBER   - TotalDiscount: NUMBER   - TotalTax: NUMBER   - Type: STRING   - UpdatedDateUTC: DATE-TIME   - Url: STRING - IsReconciled: BOOLEAN - Overpayment: ARRAY, which is also a nested data structure.   - OverpaymentID: STRING - PaymentID: STRING - PaymentType: STRING - Prepayments: ARRAY, which is also a nested data structure.   - PrepaymentID: STRING - Reference: STRING - Status: STRING - UpdatedDateUTC: DATE-TIME |
| **PrepaymentID**  STRING |
| **Reference**  STRING |
| **RemainingCredit**  NUMBER |
| **Status**  STRING |
| **SubTotal**  NUMBER |
| **Total**  NUMBER |
| **TotalTax**  NUMBER |
| **Type**  STRING |
| **UpdatedDateUTC**  DATE-TIME |

### purchase\_orders

The `purchase_orders` table contains info about your purchase orders. Purchase orders are requests sent to suppliers for specific goods and services.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | PurchaseOrderID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/purchase-orders "Opens in new tab: Xero API method") |

purchase\_orders table foreign keys

| Join purchase\_orders with | on |
| --- | --- |
| [branding\_themes](#branding-themes) | ``` purchase_orders.BrandingThemeID = branding_themes.BrandingThemeID ``` |
| [contacts](#contacts) | ``` purchase_orders.BrandingThemeID = contacts.BrandingTheme.BrandingThemeID ```  ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = contacts.SalesTrackingCategories.TrackingCategoryID ```  ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = contacts.PurchasesTrackingCategories.TrackingCategoryID ``` |
| [credit\_notes](#credit-notes) | ``` purchase_orders.BrandingThemeID = credit_notes.BrandingThemeID ```  ``` purchase_orders.CurrencyCode = credit_notes.CurrencyCode ```  ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ``` |
| [invoices](#invoices) | ``` purchase_orders.BrandingThemeID = invoices.BrandingThemeID ```  ``` purchase_orders.CurrencyCode = invoices.CurrencyCode ```  ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` purchase_orders.BrandingThemeID = repeating_invoices.BrandingThemeID ```  ``` purchase_orders.CurrencyCode = repeating_invoices.CurrencyCode ```  ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [accounts](#accounts) | ``` purchase_orders.CurrencyCode = accounts.CurrencyCode ``` |
| [bank\_transactions](#bank-transactions) | ``` purchase_orders.CurrencyCode = bank_transactions.CurrencyCode ``` |
| [currencies](#currencies) | ``` purchase_orders.CurrencyCode = currencies.Code ``` |
| [prepayments](#prepayments) | ``` purchase_orders.CurrencyCode = prepayments.CurrencyCode ```  ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ``` |
| [journals](#journals) | ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ``` |
| [manual\_journals](#manual-journals) | ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ``` |
| [overpayments](#overpayments) | ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ``` |
| [receipts](#receipts) | ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ``` |
| [tracking\_categories](#tracking-categories) | ``` purchase_orders.LineItems.Tracking.TrackingCategoryID = tracking_categories.TrackingCategoryID ``` |

purchase\_orders table schema

|  |
| --- |
| **AttentionTo**  STRING |
| **BrandingThemeID**  STRING |
| **Contact**  OBJECT This is a nested data structure:   - AccountNumber: STRING - AccountsPayableTaxType: STRING - AccountsReceivableTaxType: STRING - Addresses: ARRAY, which is also a nested data structure.   - AddressLine1: STRING   - AddressLine2: STRING   - AddressLine3: STRING   - AddressLine4: STRING   - AddressType: STRING   - AttentionTo: STRING   - City: STRING   - Country: STRING   - PostalCode: STRING   - Region: STRING - Attachments: ARRAY - Balances: OBJECT, which is also a nested data structure.   - AccountsPayable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER   - AccountsReceivable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER - BankAccountDetails: STRING - BatchPayments: OBJECT, which is also a nested data structure.   - BankAccountName: STRING   - BankAccountNumber: STRING   - Code: STRING   - Details: STRING   - Reference: STRING - BrandingTheme: OBJECT, which is also a nested data structure.   - BrandingThemeID: STRING   - CreatedDateUTC: DARE-TIME   - Name: STRING   - SortOrder: INTEGER - ContactGroups: ARRAY, which is also a nested data structure.   - ContactGroupID: STRING   - HasValidationErrors: BOOLEAN   - Name: STRING   - Status: STRING - ContactID: STRING - ContactNumber: STRING - ContactPersons: ARRAY, which is also a nested data structure.   - EmailAddress: STRING   - FirstName: STRING   - IncludeInEmails: BOOLEAN   - LastName: STRING - ContactStatus: STRING - DefaultCurrency: STRING - Discount: NUMBER - EmailAddress: STRING - FirstName: STRING - HasAttachments: BOOLEAN - HasValidationErrors: BOOLEAN - IsCustomer: BOOLEAN - IsSupplier: BOOLEAN - LastName: STRING - Name: STRING - PaymentTerms: OBJECT, which is also a nested data structure.   - Bills: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING   - Sales: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING - Phones: ARRAY, which is also a nested data structure.   - PhoneAreaCode: STRING   - PhoneCountryCode: STRING   - PhoneNumber: STRING   - PhoneType: STRING - PurchasesDefaultAccountCode: STRING - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SalesDefaultAccountCode: STRING - SalesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SkypeUserName: STRING - TaxNumber: STRING - TrackingCategoryName: STRING - TrackingCategoryOption: STRING - UpdatedDateUTC: DATE-TIME - ValidationErrors: ARRAY, which is also a nested data structure.   - Message: STRING - Website: STRING - XeroNetworkKey: STRING |
| **CurrencyCode**  STRING |
| **CurrencyRate**  NUMBER |
| **Date**  DATE-TIME |
| **DateString**  DATE-TIME |
| **DeliveryAddress**  STRING |
| **DeliveryDate**  DATE-TIME |
| **DeliveryDateString**  DATE-TIME |
| **DeliveryInstructions**  STRING |
| **ExpectedArrivalDate**  DATE-TIME |
| **ExpectedArrivalDateString**  DATE-TIME |
| **HasAttachments**  BOOLEAN |
| **HasErrors**  BOOLEAN |
| **IsDiscounted**  BOOLEAN |
| **LineAmountTypes**  STRING |
| **LineItems**  ARRAY This is a nested data structure:   - AccountCode: STRING - Description: STRING - DiscountRate: NUMBER - ItemCode: STRING - LineAmount: NUMBER - LineItemID: STRING - Quantity: NUMBER - TaxAmount: NUMBER - TaxType: STRING - Tracking: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - UnitAmount: NUMBER |
| **PurchaseOrderID**  STRING |
| **PurchaseOrderNumber**  STRING |
| **Reference**  STRING |
| **SentToContact**  BOOLEAN |
| **Status**  STRING |
| **SubTotal**  NUMBER |
| **Telephone**  STRING |
| **Total**  NUMBER |
| **TotalDiscount**  NUMBER |
| **TotalTax**  NUMBER |
| **Type**  STRING |
| **UpdatedDateUTC**  DATE-TIME |

### receipts

The `receipts` table contains info about invoice receipts, which are receipts sent to customers after an invoice has been received.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ReceiptID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/receipts "Opens in new tab: Xero API method") |

receipts table foreign keys

| Join receipts with | on |
| --- | --- |
| [contacts](#contacts) | ``` receipts.Contact.ContactID = contacts.ContactID ```  ``` receipts.LineItems.Tracking.TrackingCategoryID = contacts.SalesTrackingCategories.TrackingCategoryID ```  ``` receipts.LineItems.Tracking.TrackingCategoryID = contacts.PurchasesTrackingCategories.TrackingCategoryID ``` |
| [credit\_notes](#credit-notes) | ``` receipts.Contact.ContactID = credit_notes.Contact.ContactID ```  ``` receipts.LineItems.Tracking.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ``` |
| [invoices](#invoices) | ``` receipts.Contact.ContactID = invoices.Contact.ContactID ```  ``` receipts.LineItems.Tracking.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [linked\_transactions](#linked-transactions) | ``` receipts.Contact.ContactID = linked_transactions.ContactID ``` |
| [overpayments](#overpayments) | ``` receipts.Contact.ContactID = overpayments.Contact.ContactID ```  ``` receipts.LineItems.Tracking.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ``` |
| [prepayments](#prepayments) | ``` receipts.Contact.ContactID = prepayments.Contact.ContactID ```  ``` receipts.LineItems.Tracking.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` receipts.Contact.ContactID = repeating_invoices.Contact.ContactID ```  ``` receipts.LineItems.Tracking.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [expense\_claims](#expense-claims) | ``` receipts.ReceiptID = expense_claims.Receipts.ReceiptID ```  ``` receipts.User.UserID = expense_claims.User.UserID ``` |
| [journals](#journals) | ``` receipts.LineItems.Tracking.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ``` |
| [manual\_journals](#manual-journals) | ``` receipts.LineItems.Tracking.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ``` |
| [purchase\_orders](#purchase-orders) | ``` receipts.LineItems.Tracking.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ``` |
| [tracking\_categories](#tracking-categories) | ``` receipts.LineItems.Tracking.TrackingCategoryID = tracking_categories.TrackingCategoryID ``` |

receipts table schema

|  |
| --- |
| **Attachments**  ARRAY |
| **Contact**  OBJECT This is a nested data structure:   - AccountNumber: STRING - AccountsPayableTaxType: STRING - AccountsReceivableTaxType: STRING - Addresses: ARRAY, which is also a nested data structure.   - AddressLine1: STRING   - AddressLine2: STRING   - AddressLine3: STRING   - AddressLine4: STRING   - AddressType: STRING   - AttentionTo: STRING   - City: STRING   - Country: STRING   - PostalCode: STRING   - Region: STRING - Attachments: ARRAY - Balances: OBJECT, which is also a nested data structure.   - AccountsPayable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER   - AccountsReceivable: OBJECT, which is also a nested data structure.     - Outstanding: NUMBER     - Overdue: NUMBER - BankAccountDetails: STRING - BatchPayments: OBJECT, which is also a nested data structure.   - BankAccountName: STRING   - BankAccountNumber: STRING   - Code: STRING   - Details: STRING   - Reference: STRING - BrandingTheme: OBJECT, which is also a nested data structure.   - BrandingThemeID: STRING   - CreatedDateUTC: DARE-TIME   - Name: STRING   - SortOrder: INTEGER - ContactGroups: ARRAY, which is also a nested data structure.   - ContactGroupID: STRING   - HasValidationErrors: BOOLEAN   - Name: STRING   - Status: STRING - ContactID: STRING - ContactNumber: STRING - ContactPersons: ARRAY, which is also a nested data structure.   - EmailAddress: STRING   - FirstName: STRING   - IncludeInEmails: BOOLEAN   - LastName: STRING - ContactStatus: STRING - DefaultCurrency: STRING - Discount: NUMBER - EmailAddress: STRING - FirstName: STRING - HasAttachments: BOOLEAN - HasValidationErrors: BOOLEAN - IsCustomer: BOOLEAN - IsSupplier: BOOLEAN - LastName: STRING - Name: STRING - PaymentTerms: OBJECT, which is also a nested data structure.   - Bills: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING   - Sales: OBJECT, which is also a nested data structure.     - Day: INTEGER     - Type: STRING - Phones: ARRAY, which is also a nested data structure.   - PhoneAreaCode: STRING   - PhoneCountryCode: STRING   - PhoneNumber: STRING   - PhoneType: STRING - PurchasesDefaultAccountCode: STRING - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SalesDefaultAccountCode: STRING - SalesTrackingCategories: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - SkypeUserName: STRING - TaxNumber: STRING - TrackingCategoryName: STRING - TrackingCategoryOption: STRING - UpdatedDateUTC: DATE-TIME - ValidationErrors: ARRAY, which is also a nested data structure.   - Message: STRING - Website: STRING - XeroNetworkKey: STRING |
| **Date**  DATE-TIME |
| **HasAttachments**  BOOLEAN |
| **ID**  STRING |
| **LineAmountTypes**  STRING |
| **LineItems**  ARRAY This is a nested data structure:   - AccountCode: STRING - Description: STRING - DiscountRate: NUMBER - ItemCode: STRING - LineAmount: NUMBER - LineItemID: STRING - Quantity: NUMBER - TaxAmount: NUMBER - TaxType: STRING - Tracking: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - UnitAmount: NUMBER |
| **ReceiptID**  STRING |
| **ReceiptNumber**  INTEGER |
| **Reference**  STRING |
| **Status**  STRING |
| **SubTotal**  NUMBER |
| **Total**  NUMBER |
| **TotalTax**  NUMBER |
| **UpdatedDateUTC**  DATE-TIME |
| **Url**  STRING |
| **User**  OBJECT This is a nested data structure:   - EmailAddress: STRING - FirstName: STRING - IsSubscriber: BOOLEAN - LastName: STRING - OrganisationRole: STRING - UpdatedDateUTC: DATE-TIME - UserID: STRING - ValidationErrors: ARRAY, which is also a nested data structure.   - Message: STRING |
| **ValidationErrors**  ARRAY This is a nested data structure:   - Message: STRING |

### repeating\_invoices

The `repeating_invoices` table contains info about invoices set up to repeat in your Xero account. A repeating invoice is a recurring transaction, or a transaction that occurs on a regular basis.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | RepeatingInvoiceID |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/repeating-invoices "Opens in new tab: Xero API method") |

repeating\_invoices table foreign keys

| Join repeating\_invoices with | on |
| --- | --- |
| [branding\_themes](#branding-themes) | ``` repeating_invoices.BrandingThemeID = branding_themes.BrandingThemeID ``` |
| [contacts](#contacts) | ``` repeating_invoices.BrandingThemeID = contacts.BrandingTheme.BrandingThemeID ```  ``` repeating_invoices.Contact.ContactID = contacts.ContactID ```  ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = contacts.SalesTrackingCategories.TrackingCategoryID ```  ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = contacts.PurchasesTrackingCategories.TrackingCategoryID ``` |
| [credit\_notes](#credit-notes) | ``` repeating_invoices.BrandingThemeID = credit_notes.BrandingThemeID ```  ``` repeating_invoices.Contact.ContactID = credit_notes.Contact.ContactID ```  ``` repeating_invoices.CurrencyCode = credit_notes.CurrencyCode ```  ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ``` |
| [invoices](#invoices) | ``` repeating_invoices.BrandingThemeID = invoices.BrandingThemeID ```  ``` repeating_invoices.Contact.ContactID = invoices.Contact.ContactID ```  ``` repeating_invoices.CurrencyCode = invoices.CurrencyCode ```  ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [purchase\_orders](#purchase-orders) | ``` repeating_invoices.BrandingThemeID = purchase_orders.BrandingThemeID ```  ``` repeating_invoices.CurrencyCode = purchase_orders.CurrencyCode ```  ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ``` |
| [linked\_transactions](#linked-transactions) | ``` repeating_invoices.Contact.ContactID = linked_transactions.ContactID ``` |
| [overpayments](#overpayments) | ``` repeating_invoices.Contact.ContactID = overpayments.Contact.ContactID ```  ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ``` |
| [prepayments](#prepayments) | ``` repeating_invoices.Contact.ContactID = prepayments.Contact.ContactID ```  ``` repeating_invoices.CurrencyCode = prepayments.CurrencyCode ```  ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ``` |
| [receipts](#receipts) | ``` repeating_invoices.Contact.ContactID = receipts.Contact.ContactID ```  ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ``` |
| [accounts](#accounts) | ``` repeating_invoices.CurrencyCode = accounts.CurrencyCode ``` |
| [bank\_transactions](#bank-transactions) | ``` repeating_invoices.CurrencyCode = bank_transactions.CurrencyCode ``` |
| [currencies](#currencies) | ``` repeating_invoices.CurrencyCode = currencies.Code ``` |
| [journals](#journals) | ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ``` |
| [manual\_journals](#manual-journals) | ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ``` |
| [tracking\_categories](#tracking-categories) | ``` repeating_invoices.LineItems.Tracking.TrackingCategoryID = tracking_categories.TrackingCategoryID ``` |

repeating\_invoices table schema

|  |
| --- |
| **BrandingThemeID**  STRING |
| **Contact**  OBJECT This is a nested data structure: - Contact: OBJECT, which is also a nested data structure.   - AccountNumber: STRING   - AccountsPayableTaxType: STRING   - AccountsReceivableTaxType: STRING   - Addresses: ARRAY, which is also a nested data structure.     - AddressLine1: STRING     - AddressLine2: STRING     - AddressLine3: STRING     - AddressLine4: STRING     - AddressType: STRING     - AttentionTo: STRING     - City: STRING     - Country: STRING     - PostalCode: STRING     - Region: STRING   - Attachments: ARRAY   - Balances: OBJECT, which is also a nested data structure.     - AccountsPayable: OBJECT, which is also a nested data structure.       - Outstanding: NUMBER       - Overdue: NUMBER     - AccountsReceivable: OBJECT, which is also a nested data structure.       - Outstanding: NUMBER       - Overdue: NUMBER   - BankAccountDetails: STRING   - BatchPayments: OBJECT, which is also a nested data structure.     - BankAccountName: STRING     - BankAccountNumber: STRING     - Code: STRING     - Details: STRING     - Reference: STRING   - BrandingTheme: OBJECT, which is also a nested data structure.     - BrandingThemeID: STRING     - CreatedDateUTC: DARE-TIME     - Name: STRING     - SortOrder: INTEGER   - ContactGroups: ARRAY, which is also a nested data structure.     - ContactGroupID: STRING     - HasValidationErrors: BOOLEAN     - Name: STRING     - Status: STRING   - ContactID: STRING   - ContactNumber: STRING   - ContactPersons: ARRAY, which is also a nested data structure.     - EmailAddress: STRING     - FirstName: STRING     - IncludeInEmails: BOOLEAN     - LastName: STRING   - ContactStatus: STRING   - DefaultCurrency: STRING   - Discount: NUMBER   - EmailAddress: STRING   - FirstName: STRING   - HasAttachments: BOOLEAN   - HasValidationErrors: BOOLEAN   - IsCustomer: BOOLEAN   - IsSupplier: BOOLEAN   - LastName: STRING   - Name: STRING   - PaymentTerms: OBJECT, which is also a nested data structure.     - Bills: OBJECT, which is also a nested data structure.       - Day: INTEGER       - Type: STRING     - Sales: OBJECT, which is also a nested data structure.       - Day: INTEGER       - Type: STRING   - Phones: ARRAY, which is also a nested data structure.     - PhoneAreaCode: STRING     - PhoneCountryCode: STRING     - PhoneNumber: STRING     - PhoneType: STRING   - PurchasesDefaultAccountCode: STRING   - PurchasesTrackingCategories: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - SalesDefaultAccountCode: STRING   - SalesTrackingCategories: ARRAY, which is also a nested data structure.     - Name: STRING     - Option: STRING     - Options: ARRAY, which is also a nested data structure.       - HasValidationErrors: BOOLEAN       - IsActive: BOOLEAN       - IsArchived: BOOLEAN       - IsDeleted: BOOLEAN       - Name: STRING       - Status: STRING       - TrackingOptionID: STRING     - Status: STRING     - TrackingCategoryID: STRING     - TrackingCategoryName: STRING     - TrackingOptionID: STRING     - TrackingOptionName: STRING   - SkypeUserName: STRING   - TaxNumber: STRING   - TrackingCategoryName: STRING   - TrackingCategoryOption: STRING   - UpdatedDateUTC: DATE-TIME   - ValidationErrors: ARRAY, which is also a nested data structure.     - Message: STRING   - Website: STRING   - XeroNetworkKey: STRING |
| **CurrencyCode**  STRING |
| **HasAttachments**  BOOLEAN |
| **ID**  STRING |
| **LineAmountTypes**  STRING |
| **LineItems**  ARRAY This is a nested data structure:   - AccountCode: STRING - Description: STRING - DiscountRate: NUMBER - ItemCode: STRING - LineAmount: NUMBER - LineItemID: STRING - Quantity: NUMBER - TaxAmount: NUMBER - TaxType: STRING - Tracking: ARRAY, which is also a nested data structure.   - Name: STRING   - Option: STRING   - Options: ARRAY, which is also a nested data structure.     - HasValidationErrors: BOOLEAN     - IsActive: BOOLEAN     - IsArchived: BOOLEAN     - IsDeleted: BOOLEAN     - Name: STRING     - Status: STRING     - TrackingOptionID: STRING   - Status: STRING   - TrackingCategoryID: STRING   - TrackingCategoryName: STRING   - TrackingOptionID: STRING   - TrackingOptionName: STRING - UnitAmount: NUMBER |
| **Reference**  STRING |
| **RepeatingInvoiceID**  STRING |
| **Schedule**  OBJECT This is a nested data structure:   - DueDate: INTEGER - DueDateType: STRING - EndDate: STRING - NextScheduledDate: DATE-TIME - Period: INTEGER - StartDate: DATE-TIME - Unit: STRING |
| **Status**  STRING |
| **SubTotal**  NUMBER |
| **Total**  NUMBER |
| **TotalDiscount**  NUMBER |
| **TotalTax**  NUMBER |
| **Type**  STRING |

### tax\_rates

The `tax_rates` table contains info about the tax rates set up in your Xero account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | Name |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/tax-rates "Opens in new tab: Xero API method") |

tax\_rates table foreign keys

| Join tax\_rates with | on |
| --- | --- |
| [journals](#journals) | ``` tax_rates.Name = journals.JournalLines.TaxName ``` |

tax\_rates table schema

|  |
| --- |
| **CanApplyToAssets**  BOOLEAN |
| **CanApplyToEquity**  BOOLEAN |
| **CanApplyToExpenses**  BOOLEAN |
| **CanApplyToLiabilities**  BOOLEAN |
| **CanApplyToRevenue**  BOOLEAN |
| **DisplayTaxRate**  NUMBER |
| **EffectiveRate**  NUMBER |
| **Name**  STRING |
| **ReportTaxType**  STRING |
| **Status**  STRING |
| **TaxComponents**  ARRAY This is a nested data structure:   - IsCompound: BOOLEAN - IsNonRecoverable: BOOLEAN - Name: STRING - Rate: NUMBER |
| **TaxType**  STRING |

### tracking\_categories

The `tracking_categories` table contains info about the tracking categories in your Xero account. Tracking categories are used to track the performance of different areas of a business.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | TrackingCategoryID |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/tracking-categories "Opens in new tab: Xero API method") |

tracking\_categories table foreign keys

| Join tracking\_categories with | on |
| --- | --- |
| [contacts](#contacts) | ``` tracking_categories.TrackingCategoryID = contacts.SalesTrackingCategories.TrackingCategoryID ```  ``` tracking_categories.TrackingCategoryID = contacts.PurchasesTrackingCategories.TrackingCategoryID ``` |
| [credit\_notes](#credit-notes) | ``` tracking_categories.TrackingCategoryID = credit_notes.LineItems.Tracking.TrackingCategoryID ``` |
| [invoices](#invoices) | ``` tracking_categories.TrackingCategoryID = invoices.LineItems.Tracking.TrackingCategoryID ``` |
| [journals](#journals) | ``` tracking_categories.TrackingCategoryID = journals.JournalLines.TrackingCategories.TrackingCategoryID ``` |
| [manual\_journals](#manual-journals) | ``` tracking_categories.TrackingCategoryID = manual_journals.JournalLines.Tracking.TrackingCategoryID ``` |
| [overpayments](#overpayments) | ``` tracking_categories.TrackingCategoryID = overpayments.LineItems.Tracking.TrackingCategoryID ``` |
| [prepayments](#prepayments) | ``` tracking_categories.TrackingCategoryID = prepayments.LineItems.Tracking.TrackingCategoryID ``` |
| [purchase\_orders](#purchase-orders) | ``` tracking_categories.TrackingCategoryID = purchase_orders.LineItems.Tracking.TrackingCategoryID ``` |
| [receipts](#receipts) | ``` tracking_categories.TrackingCategoryID = receipts.LineItems.Tracking.TrackingCategoryID ``` |
| [repeating\_invoices](#repeating-invoices) | ``` tracking_categories.TrackingCategoryID = repeating_invoices.LineItems.Tracking.TrackingCategoryID ``` |

tracking\_categories table schema

|  |
| --- |
| **Name**  STRING |
| **Option**  STRING |
| **Options**  ARRAY This is a nested data structure:   - HasValidationErrors: BOOLEAN - IsActive: BOOLEAN - IsArchived: BOOLEAN - IsDeleted: BOOLEAN - Name: STRING - Status: STRING - TrackingOptionID: STRING |
| **Status**  STRING |
| **TrackingCategoryID**  STRING |
| **TrackingCategoryName**  STRING |
| **TrackingOptionID**  STRING |
| **TrackingOptionName**  STRING |

### users

The `users` table contains info about the users in an organisation.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | UserID |
| **Replication Key** | UpdatedDateUTC |
| **Useful links** | [Xero API method](https://developer.xero.com/documentation/api/users "Opens in new tab: Xero API method") |

users table schema

|  |
| --- |
| **EmailAddress**  STRING |
| **FirstName**  STRING |
| **IsSubscriber**  BOOLEAN |
| **LastName**  STRING |
| **OrganisationRole**  STRING |
| **UpdatedDateUTC**  DATE-TIME |
| **UserID**  STRING |
| **ValidationErrors**  ARRAY This is a nested data structure:   - Message: STRING |
