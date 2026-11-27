---
title: "Netsuite"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Netsuite-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Netsuite

Netsuite is an enterprise resource planning (ERP) system. Use the Netsuite connector to replicate data from your Netsuite account into your data warehouse.

Netsuite integration replicates data using the [Netsuite SOAP API](https://docs.oracle.com/en/cloud/saas/Netsuite/ns-online-help/chapter_N3477815.html).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need administrator permissions in your Netsuite account. Log into your [Netsuite](https://system.Netsuite.com/pages/customerlogin.jsp?country=US) account before completing the following procedures.

To enable the Connect Service feature:

1. Navigate to Setup > Company > Enable Features.
2. Click the SuiteCloud subtab.
3. Locate the SuiteTalk Web Services section.
4. Select the SOAP Web Services checkbox.
5. Click Save.

To retrieve your service host, service port and account ID:

1. On the homepage, locate the Settings module and click Set Up SuiteAnalytics Connect.
2. Copy and paste your service host, service port and account ID into a secured file.

To enable token-based authentication:

1. Navigate to Setup > Company > Enable Features.
2. Click the SuiteCloud subtab.
3. In the Manage Authentication section, select the Token-based Authentication checkbox.
4. Click Save.

To create an integration record for an application:

1. Navigate to Setup > Integration > Manage Integrations > New.
2. Enter a Name and a Description for your application.
3. Set State to Enabled.
4. On the Authentication subtab, select the Token-based Authentication checkbox and clear the Authorization Code Grant checkbox.
5. Click Save.
6. Copy and paste your consumer key and secret into a secured file.

To create a role:

1. Navigate to Setup > Users/Roles > Manage Roles > New Role.
2. In the General subtab, enter the role details.
3. In the Authentication subtab, select Web Service only role. Click Save.
4. In the Permissions subtab, under Setup, add the following permissions:

   | Permissions | Level |
   | --- | --- |
   | Custom Body Field | View |
   | Custom Fields | View |
   | Custom Record Types | View |
   | Deleted Records | Full |
   | SOAP Web Services | Full |
   | User Access Token | Full |
5. Click Save.

The permissions listed above are the minimum required to create a successful connection between Qlik Talend Cloud and your Netsuite instance. Qlik Talend Cloud may not be able to replicate every Netsuite object. To access additional objects or tables, you may need to grant extra permissions for specific use cases.

To assign a role to a user:

1. Navigate to Setup > Users/Roles > Manage User.
2. Click Edit next to the user.
3. Click the Access subtab.
4. On the Roles subtab, select the role you previously created.
5. Click Save.

To create your token ID and token secret:

1. Navigate to Setup > Users/Roles > Access Tokens > New.
2. Enter the following information:
   - In Application Name, select the application you created.
   - In User, select the integration user.
   - In Role, select the role you created.
3. Click Save.
4. Copy and paste your token ID and token secret into a secured file.

To retrieve the internal ID of the role you created:

1. Navigate to Setup > Users/Roles > Manage Roles.
2. Locate the internal ID next to the role you created.

   In Netsuite, the list view does not display the internal ID of roles by default. To view the internal ID, customize the list view to include this column.

To authorize the Qlik Talend Cloud IP address:

This step is only required if IP Address rules are enabled in your Netsuite account.

1. Find your Qlik Talend Cloud IP address: [Qlik Cloud IP addresses](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qlik-cloud-dns-ip.htm).
2. Log into your [Netsuite](https://system.Netsuite.com/pages/customerlogin.jsp?country=US) account.
3. Navigate to Setup > Company > Company Information.
4. In the Allowed IP Addresses field, enter the Qlik Talend Cloud IP addresses.

   For more details, see the [Netsuite help documentation](https://docs.oracle.com/en/cloud/saas/Netsuite/ns-online-help/section_1535041652.html#procedure_N250842).

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
| Account ID | Account ID. |
| Role ID | Internal role ID. |
| Host | Service host name. |
| Port | Service port number. |
| Consumer Key | Consumer key. |
| Consumer Secret | Consumer secret. |
| Token ID | Token ID. |
| Token Secret | Token secret. |

## Supported Netsuite transaction types

Qlik Talend Cloud supports replicating the following transaction types. Data for these records is available in the `Transaction` table:

- AssemblyBuild
- AssemblyUnbuild
- BinTransfer
- BinWorksheet
- CashRefund
- CashSale
- Check
- CreditMemo
- CustomerDeposit
- CustomerPayment
- CustomerRefund
- Deposit
- DepositApplication
- Estimate
- ExpenseReport
- InventoryTransfer
- InterCompanyJournalEntry
- InventoryAdjustment
- InventoryCostRevaluation
- Invoice
- ItemFulfillment
- ItemReceipt
- JournalEntry
- PaycheckJournal
- PurchaseOrder
- ReturnAuthorization
- SalesOrder
- StatisticalJournalEntry
- TransferOrder
- VendorBill
- VendorCredit
- VendorPayment
- VendorReturnAuthorization
- WorkOrder
- WorkOrderClose
- WorkOrderCompletion
- WorkOrderIssue

## Supported Netsuite item types

Qlik Talend Cloud supports replicating the following item types. Data for these records is available in the `Item` table:

- AssemblyItem
- DescriptionItem
- DiscountItem
- DownloadItem
- GiftCertificateItem
- InventoryItem
- ItemGroup
- KitItem
- LotNumberedAssemblyItem
- LotNumberedInventoryItem
- MarkupItem
- NonInventoryPurchaseItem
- NonInventoryResaleItem
- NonInventorySaleItem
- OtherChargePurchaseItem
- OtherChargeResaleItem
- OtherChargeSaleItem
- PaymentItem
- SerializedAssemblyItem
- SerializedInventoryItem
- ServicePurchaseItem
- ServiceResaleItem
- ServiceSaleItem
- SubtotalItem

## Unsupported Netsuite record types

Qlik Talend Cloud supports replicating all record types from Netsuite’s 2017.2 WSDL, except for the following:

- AccountingTransaction
- AssemblyItemBom
- Entity
- InventoryDetail
- InventoryNumberbin
- ItemBinNumber
- MseSubsidary
- OriginatingLead
- Pricing
- ProjectTaskAssignment
- TaxDetail

## Custom records

Custom record tables are named `custrecord_[custom_record_name]`, where `[custom_record_name]` is the value of the ID field in the Custom Record Setup page in Netsuite.

**Example:** If a custom record is named `promo discount` in Netsuite, the corresponding table would be `custrecord_promo_discount`.

If the ID field is left blank, Netsuite auto-assigns a numerical ID, such as `custrecord_123`, where `123` is the generated ID.

The replication method that Qlik Talend Cloud uses for each custom record type depends on whether the Show Last Modified setting is enabled in Netsuite. This setting controls if the Netsuite SuiteTalk API provides a timestamp column for use as a replication key.

- If Show Last Modified is enabled, Qlik Talend Cloud uses Key-based Incremental Replication. Only new and updated records are replicated for each job.
- If Show Last Modified is not enabled, Qlik Talend Cloud uses Full Table Replication. All records are replicated in full during each job.

To check the configuration of this setting for a custom record type in Netsuite:

1. Type page: record types into the global search and select the Page: Record Types result.
2. Find and click the custom record type in the list to open its Custom Record Type page.
3. Locate the Show Last Modified setting.

Information note

If you do not see datasets available for selection, verify that the integration user is using the custom role described above and that the role has access to the required tables.

To review role permissions in Netsuite, navigate to Setup > Users/Roles > Manage Roles, search for the role, click Edit, and then open the Permissions tab and the Lists section. For details, see [Netsuite role permissions](https://docs.oracle.com/en/cloud/saas/Netsuite/ns-online-help/section_N326341.html).

When selecting datasets for replication, Qlik Talend Cloud recommends replicating the `oa_fkeys` table to help build analytics across explicit and custom foreign keys. For reference, see [Netsuite foreign keys documentation](https://docs.oracle.com/en/cloud/saas/Netsuite/ns-online-help/section_4410184091.html). The foreign key information in that table may be inaccurate and is provided for reference only.

## Deleted records

To track deleted records in Netsuite, Qlik Talend Cloud’s Netsuite integration provides a table named `Deleted`. When replication for this table is enabled, it serves as a log for records deleted in Netsuite.

According to Netsuite documentation, only certain record types support the `getDeleted` API operation used by Qlik Talend Cloud to retrieve deleted record data through the SuiteTalk API.

The table below lists record types that support deletes and shows the corresponding table or dataset name for each type. If a record type appears in this list, deleted records of that type will be logged in the `Deleted` table.

**Note:** If a record type is not in this list, it does not support deletes. Records not listed will not be included in the `Deleted` table, even if deleted in Netsuite.

| Netsuite Record Type | Dataset/Table Name |
| --- | --- |
| AdvInterCompanyJournalEntry | Transaction |
| AssemblyBuild | Transaction |
| AssemblyItem | Item |
| AssemblyUnbuild | Transaction |
| BillingSchedule | BillingSchedule |
| Bin | Bin |
| BinTransfer | Transaction |
| BinWorksheet | Transaction |
| Bom | Bom |
| BomRevision | BomRevision |
| CalendarEvent | CalendarEvent |
| Campaign | Campaign |
| CashRefund | Transaction |
| CashSale | Transaction |
| Charge | Charge |
| Check | Transaction |
| Contact | Contact |
| ContactCategory | ContactCategory |
| CostCategory | CostCategory |
| CouponCode | CouponCode |
| CreditMemo | Transaction |
| CurrencyRate | CurrencyRate |
| customRecord | customrecord\_[custom\_record\_name] |
| CustomTransaction | Transaction |
| Customer | Customer |
| CustomerCategory | CustomerCategory |
| CustomerMessage | CustomerMessage |
| CustomerDeposit | Transaction |
| CustomerPayment | Transaction |
| CustomerRefund | Transaction |
| CustomerStatus | CustomerStatus |
| CustomerSubsidiaryRelationship | CustomerSubsidiaryRelationship |
| Deposit | Transaction |
| DepositApplication | Transaction |
| DescriptionItem | Item |
| DiscountItem | Item |
| DownloadItem | Item |
| Employee | Employee |
| Estimate | Transaction |
| ExpenseReport | Transaction |
| File | File |
| Folder | Folder |
| GiftCertificateItem | Item |
| GlobalAccountMapping | GlobalAccountMapping |
| InterCompanyJournalEntry | Transaction |
| InterCompanyTransferOrder | Transaction |
| InventoryAdjustment | Transaction |
| InventoryCostRevaluation | Transaction |
| InventoryItem | Item |
| InventoryNumber | InventoryNumber |
| InventoryTransfer | Transaction |
| Invoice | Transaction |
| Issue | Issue |
| ItemAccountMapping | ItemAccountMapping |
| ItemDemandPlan | ItemDemandPlan |
| ItemFulfillment | Transaction |
| ItemSupplyPlan | ItemSupplyPlan |
| ItemGroup | Item |
| ItemRevision | ItemRevision |
| Job | Job |
| JobStatus | JobStatus |
| JournalEntry | Transaction |
| KitItem | Item |
| LotNumberedAssemblyItem | Item |
| LotNumberedInventoryItem | Item |
| MarkupItem | Item |
| Message | Message |
| ManufacturingCostTemplate | ManufacturingCostTemplate |
| ManufacturingOperationTask | ManufacturingOperationTask |
| ManufacturingRouting | ManufacturingRouting |
| MerchandiseHierarchyNode | MerchandiseHierarchyNode |
| Nexus | Nexus |
| NonInventoryPurchaseItem | Item |
| NonInventoryResaleItem | Item |
| NonInventorySaleItem | Item |
| Note | Note |
| NoteType | NoteType |
| Opportunity | Opportunity |
| OtherChargePurchaseItem | Item |
| OtherChargeResaleItem | Item |
| OtherChargeSaleItem | Item |
| OtherNameCategory | OtherNameCategory |
| Partner | Partner |
| Paycheck | Transaction |
| PaymentItem | Item |
| PaymentMethod | PaymentMethod |
| PayrollItem | PayrollItem |
| PhoneCall | PhoneCall |
| PriceLevel | PriceLevel |
| PricingGroup | PricingGroup |
| ProjectTask | ProjectTask |
| PromotionCode | PromotionCode |
| PurchaseOrder | Transaction |
| ResourceAllocation | ResourceAllocation |
| ReturnAuthorization | Transaction |
| SalesOrder | Transaction |
| SalesTaxItem | Item |
| SerializedAssemblyItem | Item |
| SerializedInventoryItem | Item |
| ServicePurchaseItem | Item |
| ServiceResaleItem | Item |
| ServiceSaleItem | Item |
| StatisticalJournalEntry | Transaction |
| SubtotalItem | Item |
| SupportCase | SupportCase |
| Task | Task |
| Term | Term |
| TimeSheet | TimeSheet |
| TransferOrder | Transaction |
| Usage | Usage |
| Vendor | Vendor |
| VendorBill | Transaction |
| VendorCredit | Transaction |
| VendorPayment | Transaction |
| VendorReturnAuthorization | Transaction |
| VendorSubsidiaryRelationship | VendorSubsidiaryRelationship |
| WinLossReason | WinLossReason |
| WorkOrder | Transaction |
| WorkOrderIssue | Transaction |
| WorkOrderCompletion | Transaction |
| WorkOrderClose | Transaction |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

To ensure we can provide you with up-to-date documentation, this section will only cover a few of the most popular tables NetSuite integration offers.

Refer to the [NetSuite SuiteTalk Schema Browser](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2024_2/schema/record/account.html) for information on objects not listed here, including the fields available in each object.

Depending on your destination, table and column names may not appear as they are outlined below.

### Account

The `Account` table contains info about the accounts in the Chart of Accounts in your NetSuite account.

#### Account table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Account.html) |

Account table schema

|  |
| --- |
| **\_class**  VARIES |
| **acctName**  STRING |
| **acctNumber**  STRING |
| **acctType**  VARIES |
| **billableExpensesAcct**  VARIES |
| **cashFlowRate**  VARIES |
| **category1099Misc**  VARIES |
| **curDocNum**  STRING, INTEGER |
| **currency**  VARIES |
| **customFieldList**  VARIES |
| **deferralAcct**  VARIES |
| **department**  VARIES |
| **description**  STRING |
| **eliminate**  BOOLEAN, STRING |
| **exchangeRate**  STRING |
| **externalId**  STRING |
| **generalRate**  VARIES |
| **includeChildren**  BOOLEAN, STRING |
| **internalId**  STRING |
| **inventory**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **legalName**  STRING |
| **localizationsList**  VARIES |
| **location**  VARIES |
| **nullFieldList**  VARIES |
| **openingBalance**  STRING, NUMBER |
| **parent**  VARIES |
| **restrictToAccountingBookList**  VARIES |
| **revalue**  BOOLEAN, STRING |
| **subsidiaryList**  VARIES |
| **tranDate**  STRING |
| **unit**  VARIES |
| **unitsType**  VARIES |

### AccountingPeriod

The `AccountingPeriod` table contains info about the accounting periods in your NetSuite account.

#### AccountingPeriod table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/AccountingPeriod.html) |

AccountingPeriod table schema

|  |
| --- |
| **allLocked**  BOOLEAN, STRING |
| **allowNonGLChanges**  BOOLEAN, STRING |
| **apLocked**  BOOLEAN, STRING |
| **arLocked**  BOOLEAN, STRING |
| **closed**  BOOLEAN, STRING |
| **closedOnDate**  STRING |
| **endDate**  STRING |
| **fiscalCalendar**  VARIES |
| **fiscalCalendarsList**  VARIES |
| **internalId**  STRING |
| **isAdjust**  BOOLEAN, STRING |
| **isQuarter**  BOOLEAN, STRING |
| **isYear**  BOOLEAN, STRING |
| **nullFieldList**  VARIES |
| **parent**  VARIES |
| **payrollLocked**  BOOLEAN, STRING |
| **periodName**  STRING |
| **startDate**  STRING |

### Address

The `Address` table contains info about the custom address forms in your NetSuite account.

Custom address forms can apply to entity, transaction, subsidiary, company information, location, and workplace records in NetSuite. As custom address forms inherit the permissions set on the parent record, the permissions required for the parent record are required to access custom address data.

For example: To get custom address data for a location, the user must have the permission for accessing location data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Address.html) |

Address table schema

|  |
| --- |
| **addr1**  STRING |
| **addr2**  STRING |
| **addr3**  STRING |
| **addrPhone**  STRING |
| **addrText**  STRING |
| **addressee**  STRING |
| **attention**  STRING |
| **city**  STRING |
| **country**  VARIES |
| **customFieldList**  VARIES |
| **internalId**  STRING |
| **nullFieldList**  VARIES |
| **override**  BOOLEAN, STRING |
| **state**  STRING |
| **zip**  STRING |

### BillingAccount

The `BillingAccount` table contains info about the billing accounts in your NetSuite account. A billing account is a record used to show all billing information for a customer or subcustomer. A billing account contains billing-specific information, including billing schedule, default payment terms, bill-to address, and currency.

#### BillingAccount table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/BillingAccount.html) |

BillingAccount table schema

|  |
| --- |
| **\_class**  VARIES |
| **billingSchedule**  VARIES |
| **cashSaleForm**  VARIES |
| **createdBy**  STRING |
| **createdDate**  STRING |
| **currency**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **customer**  VARIES |
| **customerDefault**  BOOLEAN, STRING |
| **department**  VARIES |
| **externalId**  STRING |
| **frequency**  VARIES |
| **idNumber**  STRING |
| **inactive**  BOOLEAN, STRING |
| **internalId**  STRING |
| **invoiceForm**  VARIES |
| **lastBillCycleDate**  STRING |
| **lastBillDate**  STRING |
| **location**  VARIES |
| **memo**  STRING |
| **name**  STRING |
| **nextBillCycleDate**  STRING |
| **nullFieldList**  VARIES |
| **startDate**  STRING |
| **subsidiary**  VARIES |

### BillingSchedule

The `BillingSchedule` table contains info about the billing schedules in your NetSuite account. Billing schedules are used to define how bills for transactions are relayed to customers. In general, a billing schedule determines the frequency with which the customer is billed and the amount of each bill. However, the exact effect of a billing schedule varies depending on its type.

#### BillingSchedule table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/BillingSchedule.html) |

BillingSchedule table schema

|  |
| --- |
| **applyToSubtotal**  BOOLEAN, STRING |
| **billForActuals**  BOOLEAN, STRING |
| **dayPeriod**  STRING, INTEGER |
| **externalId**  STRING |
| **frequency**  VARIES |
| **inArrears**  BOOLEAN, STRING |
| **initialAmount**  STRING |
| **initialTerms**  VARIES |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isPublic**  BOOLEAN, STRING |
| **milestoneList**  VARIES |
| **monthDom**  STRING, INTEGER |
| **monthDow**  VARIES |
| **monthDowim**  VARIES |
| **monthMode**  VARIES |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **numberRemaining**  STRING, INTEGER |
| **project**  VARIES |
| **recurrenceDowMaskList**  VARIES |
| **recurrenceList**  VARIES |
| **recurrencePattern**  VARIES |
| **recurrenceTerms**  VARIES |
| **repeatEvery**  VARIES |
| **scheduleType**  VARIES |
| **seriesStartDate**  STRING |
| **transaction**  VARIES |
| **yearDom**  STRING, INTEGER |
| **yearDow**  VARIES |
| **yearDowim**  VARIES |
| **yearDowimMonth**  VARIES |
| **yearMode**  VARIES |
| **yearMonth**  VARIES |

### Bin

The `Bin` table contains info about bins, or places in your warehouse where you store inventory items.

#### Bin table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Bin.html) |

Bin table schema

|  |
| --- |
| **binNumber**  STRING |
| **customFieldList**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **location**  VARIES |
| **memo**  STRING |
| **nullFieldList**  VARIES |

### Bom

The `Bom` table contains info about bills of materials (BOM): the quantities of raw materials, assemblies, sub-components, and parts needed to manufacture a product.

#### Bom table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Bom.html) |

Bom table schema

|  |
| --- |
| **availableForAllAssemblies**  BOOLEAN, STRING |
| **availableForAllLocations**  BOOLEAN, STRING |
| **createdDate**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **externalId**  STRING |
| **includeChildren**  BOOLEAN, STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **legacyBomForAssembly**  VARIES |
| **memo**  STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **restrictToAssembliesList**  VARIES |
| **restrictToLocationsList**  VARIES |
| **subsidiaryList**  VARIES |
| **useComponentYield**  BOOLEAN, STRING |
| **usedOnAssembly**  BOOLEAN, STRING |

### BomRevision

The `BomRevision` table contains info about updates on bills of materials.

#### BomRevision table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/BomRevision.html) |

BomRevision table schema

|  |
| --- |
| **billOfMaterials**  VARIES |
| **componentList**  VARIES |
| **createdDate**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **effectiveEndDate**  STRING |
| **effectiveStartDate**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **memo**  STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### Budget

The `Budget` table contains info about the budgets in your NetSuite account. A budget records the expected values of income and expenses for your business. Budgets can be created for specific customers, items, departments, classes, locations, or any combination of these criteria.

#### Budget table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Budget.html) |

Budget table schema

|  |
| --- |
| **\_class**  VARIES |
| **account**  VARIES |
| **accountingBook**  STRING, NUMBER |
| **amount**  STRING, NUMBER |
| **budgetType**  VARIES |
| **category**  VARIES |
| **currency**  VARIES |
| **customFieldList**  VARIES |
| **customer**  VARIES |
| **department**  VARIES |
| **internalId**  STRING |
| **item**  VARIES |
| **location**  VARIES |
| **nullFieldList**  VARIES |
| **periodAmount1**  STRING, NUMBER |
| **periodAmount10**  STRING, NUMBER |
| **periodAmount11**  STRING, NUMBER |
| **periodAmount12**  STRING, NUMBER |
| **periodAmount13**  STRING, NUMBER |
| **periodAmount14**  STRING, NUMBER |
| **periodAmount15**  STRING, NUMBER |
| **periodAmount16**  STRING, NUMBER |
| **periodAmount17**  STRING, NUMBER |
| **periodAmount18**  STRING, NUMBER |
| **periodAmount19**  STRING, NUMBER |
| **periodAmount2**  STRING, NUMBER |
| **periodAmount20**  STRING, NUMBER |
| **periodAmount21**  STRING, NUMBER |
| **periodAmount22**  STRING, NUMBER |
| **periodAmount23**  STRING, NUMBER |
| **periodAmount24**  STRING, NUMBER |
| **periodAmount3**  STRING, NUMBER |
| **periodAmount4**  STRING, NUMBER |
| **periodAmount5**  STRING, NUMBER |
| **periodAmount6**  STRING, NUMBER |
| **periodAmount7**  STRING, NUMBER |
| **periodAmount8**  STRING, NUMBER |
| **periodAmount9**  STRING, NUMBER |
| **subsidiary**  VARIES |
| **year**  VARIES |

### CalendarEvent

The `CalendarEvent` table contains info about the scheduled activities, or events, that are on the calendar in your NetSuite account.

#### CalendarEvent table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CalendarEvent.html) |

CalendarEvent table schema

|  |
| --- |
| **accessLevel**  VARIES |
| **allDayEvent**  BOOLEAN, STRING |
| **attendeeList**  VARIES |
| **company**  VARIES |
| **contact**  VARIES |
| **createdDate**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **endByDate**  STRING |
| **endDate**  STRING |
| **exclusionDateList**  VARIES |
| **externalId**  STRING |
| **frequency**  VARIES |
| **internalId**  STRING |
| **lastModifiedDate**  STRING |
| **location**  STRING |
| **message**  STRING |
| **noEndDate**  BOOLEAN, STRING |
| **nullFieldList**  VARIES |
| **organizer**  VARIES |
| **owner**  VARIES |
| **period**  STRING, INTEGER |
| **recurrence**  STRING |
| **recurrenceDow**  VARIES |
| **recurrenceDowMaskList**  VARIES |
| **recurrenceDowim**  VARIES |
| **reminderMinutes**  VARIES |
| **reminderType**  VARIES |
| **resourceList**  VARIES |
| **sendEmail**  BOOLEAN, STRING |
| **seriesStartDate**  STRING |
| **startDate**  STRING |
| **status**  VARIES |
| **supportCase**  VARIES |
| **timeItemList**  VARIES |
| **timedEvent**  BOOLEAN, STRING |
| **title**  STRING |
| **transaction**  VARIES |

### Campaign

The `Campaign` table contains info about the campaigns in your NetSuite account. Campaigns are used to manage marketing initiatives.

#### Campaign table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Campaign.html) |

Campaign table schema

|  |
| --- |
| **audience**  VARIES |
| **baseCost**  STRING, NUMBER |
| **campaignDirectMailList**  VARIES |
| **campaignEmailList**  VARIES |
| **campaignEventList**  VARIES |
| **campaignId**  STRING |
| **category**  VARIES |
| **convCostPerCustomer**  STRING, NUMBER |
| **conversions**  STRING, INTEGER |
| **cost**  STRING, NUMBER |
| **costPerCustomer**  STRING, NUMBER |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **endDate**  STRING |
| **eventResponseList**  VARIES |
| **expectedRevenue**  STRING, NUMBER |
| **externalId**  STRING |
| **family**  VARIES |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **itemList**  VARIES |
| **keyword**  STRING |
| **leadsGenerated**  STRING, INTEGER |
| **local**  BOOLEAN, STRING |
| **message**  STRING |
| **nullFieldList**  VARIES |
| **offer**  VARIES |
| **owner**  VARIES |
| **profit**  STRING, NUMBER |
| **promotionCode**  VARIES |
| **roi**  STRING, NUMBER |
| **searchEngine**  VARIES |
| **startDate**  STRING |
| **title**  STRING |
| **totalRevenue**  STRING, NUMBER |
| **uniqueVisitors**  STRING, INTEGER |
| **url**  STRING |
| **vertical**  VARIES |

### Charge

The `Charge` table contains info about the charges in your NetSuite account, which represent billable amounts that your clients must pay.

#### Charge table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Charge.html) |

Charge table schema

|  |
| --- |
| **\_class**  VARIES |
| **amount**  STRING, NUMBER |
| **billTo**  VARIES |
| **billingAccount**  VARIES |
| **billingItem**  VARIES |
| **chargeDate**  STRING |
| **chargeType**  VARIES |
| **createdDate**  STRING |
| **currency**  VARIES |
| **customForm**  VARIES |
| **department**  VARIES |
| **description**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **invoice**  VARIES |
| **invoiceLine**  VARIES |
| **location**  VARIES |
| **nullFieldList**  VARIES |
| **projectTask**  VARIES |
| **quantity**  STRING, NUMBER |
| **rate**  STRING |
| **rule**  VARIES |
| **runId**  STRING |
| **salesOrder**  VARIES |
| **salesOrderLine**  VARIES |
| **stage**  VARIES |
| **subscriptionLine**  VARIES |
| **timeRecord**  VARIES |
| **transaction**  VARIES |
| **transactionLine**  VARIES |
| **use**  VARIES |

### Classification

The `Classification` table contains info about the classifications in your NetSuite account.

As classifications inherit the permissions set on the parent record, the permissions required for the parent record are required to access classification data.

For example: To get classification data for a location, the user must have the permission for accessing location data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Classification.html) |

Classification table schema

|  |
| --- |
| **classTranslationList**  VARIES |
| **customFieldList**  VARIES |
| **externalId**  STRING |
| **includeChildren**  BOOLEAN, STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **parent**  VARIES |
| **subsidiaryList**  VARIES |

### ConsolidatedExchangeRate

The `ConsolidatedExchangeRate` table contains info about consolidated exchange rates. This is used in NetSuite OneWorld for consolidation purposes, ensuring currency amounts correctly roll up from child to parent subsidiaries.

#### ConsolidatedExchangeRate table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ConsolidatedExchangeRate.html) |

ConsolidatedExchangeRate table schema

|  |
| --- |
| **accountingBook**  STRING |
| **averageRate**  STRING, NUMBER |
| **currentRate**  STRING, NUMBER |
| **externalId**  STRING |
| **fromCurrency**  STRING |
| **fromSubsidiary**  STRING |
| **historicalRate**  STRING, NUMBER |
| **internalId**  STRING |
| **isDerived**  BOOLEAN, STRING |
| **isEliminationSubsidiary**  BOOLEAN, STRING |
| **isPeriodClosed**  BOOLEAN, STRING |
| **nullFieldList**  VARIES |
| **postingPeriod**  STRING |
| **toCurrency**  STRING |
| **toSubsidiary**  STRING |

### Contact

The `Contact` table contains info about contacts.

#### Contact table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Contact.html) |

Contact table schema

|  |
| --- |
| **addressbookList**  VARIES |
| **altEmail**  STRING |
| **assistant**  VARIES |
| **assistantPhone**  STRING |
| **billPay**  BOOLEAN, STRING |
| **categoryList**  VARIES |
| **comments**  STRING |
| **company**  VARIES |
| **contactSource**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **dateCreated**  STRING |
| **defaultAddress**  STRING |
| **email**  STRING |
| **entityId**  STRING |
| **externalId**  STRING |
| **fax**  STRING |
| **firstName**  STRING |
| **globalSubscriptionStatus**  VARIES |
| **homePhone**  STRING |
| **image**  VARIES |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isPrivate**  BOOLEAN, STRING |
| **lastModifiedDate**  STRING |
| **lastName**  STRING |
| **middleName**  STRING |
| **mobilePhone**  STRING |
| **nullFieldList**  VARIES |
| **officePhone**  STRING |
| **phone**  STRING |
| **phoneticName**  STRING |
| **salutation**  STRING |
| **subscriptionsList**  VARIES |
| **subsidiary**  VARIES |
| **supervisor**  VARIES |
| **supervisorPhone**  STRING |
| **title**  STRING |

### ContactCategory

The `ContactCategory` table contains info about the types of contacts in your NetSuite account.

#### ContactCategory table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ContactCategory.html) |

ContactCategory table schema

|  |
| --- |
| **\_private**  BOOLEAN, STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### ContactRole

The `ContactRole` table contains info about contact roles in your NetSuite account.

#### ContactRole table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ContactRole.html) |

ContactRole table schema

|  |
| --- |
| **description**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### CostCategory

The `CostCategory` table contains info about cost categories, which are used to classify different types of costs associated with items.

#### CostCategory table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CostCategory.html) |

CostCategory table schema

|  |
| --- |
| **account**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **itemCostType**  VARIES |
| **name**  STRING |
| **nullFieldList**  VARIES |

### CouponCode

The `CouponCode` table contains info about the coupon codes in your NetSuite account.

#### CouponCode table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CouponCode.html) |

CouponCode table schema

|  |
| --- |
| **code**  STRING |
| **dateSent**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **nullFieldList**  VARIES |
| **promotion**  VARIES |
| **recipient**  VARIES |
| **useCount**  STRING, INTEGER |
| **used**  BOOLEAN, STRING |

### CurrencyRate

The `CurrencyRate` table contains info about currency rate records in you NetSuite account. These are also known as Exchange Rate records in NetSuite.

#### CurrencyRate table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CurrencyRate.html) |

CurrencyRate table schema

|  |
| --- |
| **baseCurrency**  VARIES |
| **currencyRateType**  STRING |
| **effectiveDate**  STRING |
| **exchangeRate**  STRING, NUMBER |
| **internalId**  STRING |
| **nullFieldList**  VARIES |
| **transactionCurrency**  VARIES |

### CustomList

The `CustomList` table contains info about

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CustomList.html) |

CustomList table schema

|  |
| --- |
| **convertToCustomRecord**  BOOLEAN, STRING |
| **customValueList**  VARIES |
| **description**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isMatrixOption**  BOOLEAN, STRING |
| **isOrdered**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **owner**  VARIES |
| **scriptId**  STRING |
| **translationsList**  VARIES |

### Customer

The `Customer` table contains info about customers.

#### Customer table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Customer.html) |

Customer table schema

|  |
| --- |
| **accessRole**  VARIES |
| **accountNumber**  STRING |
| **addressbookList**  VARIES |
| **aging**  STRING, NUMBER |
| **aging1**  STRING, NUMBER |
| **aging2**  STRING, NUMBER |
| **aging3**  STRING, NUMBER |
| **aging4**  STRING, NUMBER |
| **alcoholRecipientType**  VARIES |
| **altEmail**  STRING |
| **altName**  STRING |
| **altPhone**  STRING |
| **assignedWebSite**  STRING |
| **balance**  STRING, NUMBER |
| **billPay**  BOOLEAN, STRING |
| **buyingReason**  VARIES |
| **buyingTimeFrame**  VARIES |
| **campaignCategory**  VARIES |
| **category**  VARIES |
| **clickStream**  STRING |
| **comments**  STRING |
| **companyName**  STRING |
| **consolAging**  STRING, NUMBER |
| **consolAging1**  STRING, NUMBER |
| **consolAging2**  STRING, NUMBER |
| **consolAging3**  STRING, NUMBER |
| **consolAging4**  STRING, NUMBER |
| **consolBalance**  STRING, NUMBER |
| **consolDaysOverdue**  STRING, INTEGER |
| **consolDepositBalance**  STRING, NUMBER |
| **consolOverdueBalance**  STRING, NUMBER |
| **consolUnbilledOrders**  STRING, NUMBER |
| **contactRolesList**  VARIES |
| **contribPct**  STRING |
| **creditCardsList**  VARIES |
| **creditHoldOverride**  VARIES |
| **creditLimit**  STRING, NUMBER |
| **currency**  VARIES |
| **currencyList**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **dateCreated**  STRING |
| **daysOverdue**  STRING, INTEGER |
| **defaultAddress**  STRING |
| **defaultAllocationStrategy**  STRING |
| **defaultOrderPriority**  STRING, NUMBER |
| **defaultTaxReg**  STRING |
| **depositBalance**  STRING, NUMBER |
| **displaySymbol**  STRING |
| **downloadList**  VARIES |
| **drAccount**  VARIES |
| **email**  STRING |
| **emailPreference**  VARIES |
| **emailTransactions**  BOOLEAN, STRING |
| **endDate**  STRING |
| **entityId**  STRING |
| **entityStatus**  VARIES |
| **estimatedBudget**  STRING, NUMBER |
| **externalId**  STRING |
| **fax**  STRING |
| **faxTransactions**  BOOLEAN, STRING |
| **firstName**  STRING |
| **firstVisit**  STRING |
| **fxAccount**  VARIES |
| **giveAccess**  BOOLEAN, STRING |
| **globalSubscriptionStatus**  VARIES |
| **groupPricingList**  VARIES |
| **homePhone**  STRING |
| **image**  VARIES |
| **internalId**  STRING |
| **isBudgetApproved**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **isPerson**  BOOLEAN, STRING |
| **itemPricingList**  VARIES |
| **keywords**  STRING |
| **language**  VARIES |
| **lastModifiedDate**  STRING |
| **lastName**  STRING |
| **lastPageVisited**  STRING |
| **lastVisit**  STRING |
| **leadSource**  VARIES |
| **middleName**  STRING |
| **mobilePhone**  STRING |
| **monthlyClosing**  VARIES |
| **negativeNumberFormat**  VARIES |
| **nullFieldList**  VARIES |
| **numberFormat**  VARIES |
| **openingBalance**  STRING, NUMBER |
| **openingBalanceAccount**  VARIES |
| **openingBalanceDate**  STRING |
| **overdueBalance**  STRING, NUMBER |
| **overrideCurrencyFormat**  BOOLEAN, STRING |
| **parent**  VARIES |
| **partner**  VARIES |
| **partnersList**  VARIES |
| **password**  STRING |
| **password2**  STRING |
| **phone**  STRING |
| **phoneticName**  STRING |
| **prefCCProcessor**  VARIES |
| **priceLevel**  VARIES |
| **printOnCheckAs**  STRING |
| **printTransactions**  BOOLEAN, STRING |
| **receivablesAccount**  VARIES |
| **referrer**  STRING |
| **reminderDays**  STRING, INTEGER |
| **representingSubsidiary**  VARIES |
| **requirePwdChange**  BOOLEAN, STRING |
| **resaleNumber**  STRING |
| **salesGroup**  VARIES |
| **salesReadiness**  VARIES |
| **salesRep**  VARIES |
| **salesTeamList**  VARIES |
| **salutation**  STRING |
| **sendEmail**  BOOLEAN, STRING |
| **shipComplete**  BOOLEAN, STRING |
| **shippingItem**  VARIES |
| **sourceWebSite**  STRING |
| **stage**  VARIES |
| **startDate**  STRING |
| **subscriptionsList**  VARIES |
| **subsidiary**  VARIES |
| **symbolPlacement**  VARIES |
| **syncPartnerTeams**  BOOLEAN, STRING |
| **taxExempt**  BOOLEAN, STRING |
| **taxItem**  VARIES |
| **taxRegistrationList**  STRING |
| **taxable**  BOOLEAN, STRING |
| **terms**  VARIES |
| **territory**  VARIES |
| **thirdPartyAcct**  STRING |
| **thirdPartyCarrier**  STRING |
| **thirdPartyCountry**  VARIES |
| **thirdPartyZipcode**  STRING |
| **title**  STRING |
| **unbilledOrders**  STRING, NUMBER |
| **url**  STRING |
| **vatRegNumber**  STRING |
| **visits**  STRING, INTEGER |
| **webLead**  STRING |

### CustomerCategory

The `CustomerCategory` table contains info about the types of customers in your NetSuite account.

#### CustomerCategory table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CustomerCategory.html) |

CustomerCategory table schema

|  |
| --- |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### CustomerMessage

The `CustomerMessage` table contains info about standardized customer messages in your NetSuite account.

#### CustomerMessage table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CustomerMessage.html) |

CustomerMessage table schema

|  |
| --- |
| **description**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **preferred**  BOOLEAN, STRING |

### CustomerStatus

The `CustomerStatus` table contains info about the stages for leads, prospects, and customers in your NetSuite sales cycle.

#### CustomerStatus table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CustomerStatus.html) |

CustomerStatus table schema

|  |
| --- |
| **description**  STRING |
| **externalId**  STRING |
| **includeInLeadReports**  BOOLEAN, STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **probability**  STRING, NUMBER |
| **stage**  VARIES |

### CustomerSubsidiaryRelationship

The `CustomerSubsidiaryRelationship` table contains info about customers shared with multiple subsidiaries.

#### CustomerSubsidiaryRelationship table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CustomerSubsidiaryRelationship.html) |

CustomerSubsidiaryRelationship table schema

|  |
| --- |
| **customFieldList**  VARIES |
| **entity**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **isPrimarySub**  BOOLEAN, STRING |
| **nullFieldList**  VARIES |
| **primaryCurrency**  VARIES |
| **subsidiary**  VARIES |

### Deleted

The `Deleted` table contains info about deleted records.

#### Deleted table replication requirements

Replicating this table requires the `View` permission in NetSuite.

#### Objects with delete support

According to [NetSuite’s documentation](https://system.netsuite.com/app/help/helpcenter.nl?fid=section_N3497592.html), only certain objects support the `` operation Qlik Talend Cloud uses to retrieve deleted record data from the SuiteTalk API.

Refer to the [Deleted records](#deleted-records) section for more info and a list of record types with delete support.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | internalId  type |
| **Replication Key** | deletedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Deleted.html)  [NetSuite API method](https://system.netsuite.com/app/help/helpcenter.nl?fid=section_N3497592.html "Opens in new tab: NetSuite API method") |

Deleted table schema

|  |
| --- |
| **customRecord**  BOOLEAN |
| **deletedDate**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **name**  STRING |
| **scriptId**  STRING |
| **type**  STRING |

### Department

The `Department` table contains info about the departments in your NetSuite account.

#### Department table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Department.html) |

Department table schema

|  |
| --- |
| **classTranslationList**  VARIES |
| **customFieldList**  VARIES |
| **externalId**  STRING |
| **includeChildren**  BOOLEAN, STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **parent**  VARIES |
| **subsidiaryList**  VARIES |

### Employee

The `Employee` table contains info about the employees in your NetSuite account.

#### Employee table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Employee.html) |

Employee table schema

|  |
| --- |
| **IPAddressRule**  STRING |
| **\_class**  VARIES |
| **accountNumber**  STRING |
| **accruedTimeList**  VARIES |
| **addressbookList**  VARIES |
| **adpId**  STRING |
| **altName**  STRING |
| **approvalLimit**  STRING, NUMBER |
| **approver**  VARIES |
| **baseWage**  STRING, NUMBER |
| **baseWageType**  VARIES |
| **billPay**  BOOLEAN, STRING |
| **billingClass**  VARIES |
| **birthDate**  STRING |
| **bonusTarget**  STRING, NUMBER |
| **bonusTargetComment**  STRING |
| **bonusTargetPayFrequency**  STRING |
| **bonusTargetType**  STRING |
| **comments**  STRING |
| **commissionPaymentPreference**  VARIES |
| **companyContributionList**  VARIES |
| **compensationCurrency**  VARIES |
| **concurrentWebServicesUser**  BOOLEAN, STRING |
| **currency**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **dateCreated**  STRING |
| **deductionList**  VARIES |
| **defaultAcctCorpCardExp**  STRING |
| **defaultAddress**  STRING |
| **defaultExpenseReportCurrency**  STRING |
| **department**  VARIES |
| **directDeposit**  BOOLEAN, STRING |
| **directDepositList**  VARIES |
| **earningList**  VARIES |
| **eligibleForCommission**  BOOLEAN, STRING |
| **email**  STRING |
| **emergencyContactList**  VARIES |
| **employeeStatus**  VARIES |
| **employeeType**  VARIES |
| **entityId**  STRING |
| **ethnicity**  VARIES |
| **expenseLimit**  STRING, NUMBER |
| **externalId**  STRING |
| **fax**  STRING |
| **firstName**  STRING |
| **gender**  VARIES |
| **giveAccess**  BOOLEAN, STRING |
| **globalSubscriptionStatus**  VARIES |
| **hasOfflineAccess**  BOOLEAN, STRING |
| **hcmPositionList**  VARIES |
| **hireDate**  STRING |
| **homePhone**  STRING |
| **hrEducationList**  VARIES |
| **image**  VARIES |
| **inheritIPRules**  BOOLEAN, STRING |
| **initials**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isJobManager**  BOOLEAN, STRING |
| **isJobResource**  BOOLEAN, STRING |
| **isSalesRep**  BOOLEAN, STRING |
| **isSupportRep**  BOOLEAN, STRING |
| **job**  VARIES |
| **jobDescription**  STRING |
| **laborCost**  STRING, NUMBER |
| **lastModifiedDate**  STRING |
| **lastName**  STRING |
| **lastPaidDate**  STRING |
| **lastReviewDate**  STRING |
| **location**  VARIES |
| **maritalStatus**  VARIES |
| **middleName**  STRING |
| **mobilePhone**  STRING |
| **nextReviewDate**  STRING |
| **nullFieldList**  VARIES |
| **officePhone**  STRING |
| **password**  STRING |
| **password2**  STRING |
| **payFrequency**  VARIES |
| **phone**  STRING |
| **phoneticName**  STRING |
| **purchaseOrderApprovalLimit**  STRING, NUMBER |
| **purchaseOrderApprover**  VARIES |
| **purchaseOrderLimit**  STRING, NUMBER |
| **ratesList**  VARIES |
| **releaseDate**  STRING |
| **requirePwdChange**  BOOLEAN, STRING |
| **rolesList**  VARIES |
| **salesRole**  VARIES |
| **salutation**  STRING |
| **sendEmail**  BOOLEAN, STRING |
| **socialSecurityNumber**  STRING |
| **startDateTimeOffCalc**  STRING |
| **subscriptionsList**  VARIES |
| **subsidiary**  VARIES |
| **supervisor**  VARIES |
| **targetUtilization**  STRING, NUMBER |
| **template**  VARIES |
| **terminationCategory**  VARIES |
| **terminationDetails**  STRING |
| **terminationReason**  VARIES |
| **terminationRegretted**  VARIES |
| **timeApprover**  VARIES |
| **timeOffPlan**  VARIES |
| **title**  STRING |
| **usePerquest**  BOOLEAN, STRING |
| **useTimeData**  VARIES |
| **workAssignment**  VARIES |
| **workCalendar**  VARIES |
| **workplace**  VARIES |

### EntityGroup

The `EntityGroup` table contains info about the groups in your NetSuite account.

#### EntityGroup table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/EntityGroup.html) |

EntityGroup table schema

|  |
| --- |
| **comments**  STRING |
| **customFieldList**  VARIES |
| **email**  STRING |
| **externalId**  STRING |
| **groupName**  STRING |
| **groupOwner**  VARIES |
| **groupType**  VARIES |
| **internalId**  STRING |
| **isFunctionalTeam**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **isManufacturingWorkCenter**  BOOLEAN, STRING |
| **isPrivate**  BOOLEAN, STRING |
| **isProductTeam**  BOOLEAN, STRING |
| **isSalesRep**  BOOLEAN, STRING |
| **isSalesTeam**  BOOLEAN, STRING |
| **isSavedSearch**  BOOLEAN, STRING |
| **isSupportRep**  BOOLEAN, STRING |
| **issueRole**  VARIES |
| **laborResources**  STRING, INTEGER |
| **machineResources**  STRING, INTEGER |
| **nullFieldList**  VARIES |
| **parentGroupType**  VARIES |
| **restrictionGroup**  VARIES |
| **savedSearch**  VARIES |
| **subsidiary**  VARIES |
| **workCalendar**  VARIES |

### ExpenseCategory

The `ExpenseCategory` table contains info about the expense categories in your NetSuite account.

#### ExpenseCategory table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ExpenseCategory.html) |

ExpenseCategory table schema

|  |
| --- |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **defaultRate**  STRING, NUMBER |
| **description**  STRING |
| **expenseAcct**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **rateRequired**  BOOLEAN, STRING |
| **ratesList**  VARIES |
| **subsidiaryList**  VARIES |
| **translationsList**  VARIES |

### FairValuePrice

The `FairValuePrice` table contains info about the fair value price list in your NetSuite account.

#### FairValuePrice table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/FairValuePrice.html) |

FairValuePrice table schema

|  |
| --- |
| **currency**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **dimensionList**  VARIES |
| **endDate**  STRING |
| **externalId**  STRING |
| **fairValue**  STRING, NUMBER |
| **fairValueFormula**  VARIES |
| **fairValueRangePolicy**  VARIES |
| **highValue**  STRING, NUMBER |
| **highValuePercent**  STRING, NUMBER |
| **internalId**  STRING |
| **isVsoePrice**  BOOLEAN, STRING |
| **item**  VARIES |
| **itemRevenueCategory**  VARIES |
| **lowValue**  STRING, NUMBER |
| **lowValuePercent**  STRING, NUMBER |
| **nullFieldList**  VARIES |
| **startDate**  STRING |
| **units**  VARIES |
| **unitsType**  VARIES |

### File

The `File` table contains info about the files in your NetSuite File Cabinet.

#### File table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/File.html) |

File table schema

|  |
| --- |
| **\_class**  STRING |
| **altTagCaption**  STRING |
| **attachFrom**  VARIES |
| **bundleable**  BOOLEAN, STRING |
| **caption**  STRING |
| **content**  STRING |
| **createdDate**  STRING |
| **department**  STRING |
| **description**  STRING |
| **encoding**  VARIES |
| **externalId**  STRING |
| **featuredDescription**  STRING |
| **fileSize**  STRING, NUMBER |
| **fileType**  VARIES |
| **folder**  VARIES |
| **hideInBundle**  BOOLEAN, STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isOnline**  BOOLEAN, STRING |
| **isPrivate**  BOOLEAN, STRING |
| **lastModifiedDate**  STRING |
| **mediaFile**  VARIES |
| **mediaTypeName**  STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **owner**  VARIES |
| **siteCategoryList**  VARIES |
| **siteDescription**  STRING |
| **storeDisplayThumbnail**  VARIES |
| **textFileEncoding**  VARIES |
| **url**  STRING |
| **urlComponent**  STRING |

### Folder

The `Folder` table contains info about the folders in your NetSuite File Cabinet.

#### Folder table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Folder.html) |

Folder table schema

|  |
| --- |
| **\_class**  VARIES |
| **bundleable**  BOOLEAN, STRING |
| **department**  VARIES |
| **description**  STRING |
| **externalId**  STRING |
| **folderType**  VARIES |
| **group**  VARIES |
| **hideInBundle**  BOOLEAN, STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isOnline**  BOOLEAN, STRING |
| **isPrivate**  BOOLEAN, STRING |
| **location**  VARIES |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **parent**  VARIES |
| **subsidiary**  VARIES |

### GiftCertificate

The `GiftCertificate` table contains info about the gift certificates in your NetSuite account.

#### GiftCertificate table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/GiftCertificate.html) |

GiftCertificate table schema

|  |
| --- |
| **amountRemaining**  STRING, NUMBER |
| **createdDate**  STRING |
| **email**  STRING |
| **expirationDate**  STRING |
| **giftCertCode**  STRING |
| **internalId**  STRING |
| **lastModifiedDate**  STRING |
| **message**  STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **originalAmount**  STRING, NUMBER |
| **sender**  STRING |

### GlobalAccountMapping

The `GlobalAccountMapping` table contains the global account mapping record details in your NetSuite account.

For NetSuite accounts using Multi-Book Accounting, the global account mapping record enables you to configure secondary accounting books to post to accounts different from the primary book. These mappings are used by transactions where the user can manually select the account to which the transaction posts.

#### GlobalAccountMapping table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/GlobalAccountMapping.html) |

GlobalAccountMapping table schema

|  |
| --- |
| **\_class**  VARIES |
| **accountingBook**  VARIES |
| **customDimension**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **department**  VARIES |
| **destinationAccount**  VARIES |
| **effectiveDate**  STRING |
| **endDate**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **location**  VARIES |
| **nullFieldList**  VARIES |
| **sourceAccount**  VARIES |
| **subsidiary**  VARIES |

### HcmJob

#### HcmJob table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/HcmJob.html) |

HcmJob table schema

|  |
| --- |
| **customFieldList**  VARIES |
| **description**  STRING |
| **employmentCategory**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **jobId**  STRING |
| **nullFieldList**  VARIES |
| **title**  STRING |

### InboundShipment

The `InboundShipment` table contains info about inbound shipments in your NetSuite account.

#### InboundShipment table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/InboundShipment.html) |

InboundShipment table schema

|  |
| --- |
| **actualDeliveryDate**  STRING |
| **actualShippingDate**  STRING |
| **billOfLading**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **expectedDeliveryDate**  STRING |
| **expectedShippingDate**  STRING |
| **externalDocumentNumber**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **itemsList**  VARIES |
| **nullFieldList**  VARIES |
| **shipmentBaseCurrency**  STRING |
| **shipmentMemo**  STRING |
| **shipmentNumber**  STRING |
| **shipmentStatus**  VARIES |
| **vesselNumber**  STRING |

### InventoryNumber

The `InventoryNumber` table contains info about the serial or lot numbers in your NetSuite account.

#### InventoryNumber table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/InventoryNumber.html) |

InventoryNumber table schema

|  |
| --- |
| **customFieldList**  VARIES |
| **expirationDate**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **inventoryNumber**  STRING |
| **item**  VARIES |
| **locationsList**  VARIES |
| **memo**  STRING |
| **nullFieldList**  VARIES |
| **status**  STRING |
| **units**  STRING |

### Issue

The `Issue` table contains info about the support cases in your NetSuite account.

#### Issue table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Issue.html) |

Issue table schema

|  |
| --- |
| **assigned**  VARIES |
| **brokenInVersionList**  VARIES |
| **buildBroken**  VARIES |
| **buildFixed**  VARIES |
| **buildTarget**  VARIES |
| **createdDate**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **emailAssignee**  BOOLEAN, STRING |
| **emailCellsList**  VARIES |
| **emailEmployeesList**  VARIES |
| **externalAbstract**  STRING |
| **externalDetails**  STRING |
| **externalId**  STRING |
| **fixedInVersionList**  VARIES |
| **internalId**  STRING |
| **isOwner**  BOOLEAN, STRING |
| **isReviewed**  BOOLEAN, STRING |
| **isShowStopper**  BOOLEAN, STRING |
| **issueAbstract**  STRING |
| **issueNumber**  STRING |
| **issueStatus**  VARIES |
| **issueTagsList**  VARIES |
| **issueType**  VARIES |
| **item**  VARIES |
| **lastModifiedDate**  STRING |
| **module**  VARIES |
| **newDetails**  STRING |
| **nullFieldList**  VARIES |
| **priority**  VARIES |
| **product**  VARIES |
| **productTeam**  VARIES |
| **relatedIssuesList**  VARIES |
| **reportedBy**  VARIES |
| **reproduce**  VARIES |
| **reviewer**  VARIES |
| **severity**  VARIES |
| **source**  VARIES |
| **targetVersionList**  VARIES |
| **trackCode**  VARIES |
| **versionBroken**  VARIES |
| **versionFixed**  VARIES |
| **versionTarget**  VARIES |

### Item

The `Item` table contains info about items.

#### Item table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/script/record/item.html) |

Item table schema

|  |
| --- |
| **\_class**  VARIES |
| **\_type**  STRING |
| **account**  VARIES |
| **accountingBookDetailList**  VARIES |
| **alternateDemandSourceItem**  VARIES |
| **amortizationPeriod**  STRING, INTEGER |
| **amortizationTemplate**  VARIES |
| **assetAccount**  VARIES |
| **authCodesList**  VARIES |
| **autoLeadTime**  BOOLEAN, STRING |
| **autoPreferredStockLevel**  BOOLEAN, STRING |
| **autoReorderPoint**  BOOLEAN, STRING |
| **availableToPartners**  BOOLEAN, STRING |
| **averageCost**  STRING, NUMBER |
| **backwardConsumptionDays**  STRING, INTEGER |
| **billExchRateVarianceAcct**  VARIES |
| **billOfMaterialsList**  VARIES |
| **billPriceVarianceAcct**  VARIES |
| **billQtyVarianceAcct**  VARIES |
| **billingRatesMatrix**  VARIES |
| **billingSchedule**  VARIES |
| **binNumberList**  VARIES |
| **buildEntireAssembly**  BOOLEAN, STRING |
| **buildTime**  STRING, NUMBER |
| **buildTimeLotSize**  STRING, NUMBER |
| **cogsAccount**  VARIES |
| **consumptionUnit**  STRING |
| **contingentRevenueHandling**  BOOLEAN, STRING |
| **conversionRate**  STRING, NUMBER |
| **copyDescription**  BOOLEAN, STRING |
| **cost**  STRING, NUMBER |
| **costCategory**  VARIES |
| **costEstimate**  STRING, NUMBER |
| **costEstimateType**  VARIES |
| **costEstimateUnits**  STRING |
| **costUnits**  STRING |
| **costingMethod**  VARIES |
| **costingMethodDisplay**  STRING |
| **countryOfManufacture**  VARIES |
| **createJob**  BOOLEAN, STRING |
| **createRevenuePlansOn**  VARIES |
| **createdDate**  STRING |
| **currency**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **dateConvertedToInv**  STRING |
| **daysBeforeExpiration**  STRING, INTEGER |
| **defaultItemShipMethod**  VARIES |
| **defaultReturnCost**  STRING, NUMBER |
| **defaultRevision**  STRING |
| **deferRevRec**  BOOLEAN, STRING |
| **deferralAccount**  VARIES |
| **deferredRevenueAccount**  VARIES |
| **demandModifier**  STRING, NUMBER |
| **demandSource**  VARIES |
| **demandTimeFence**  STRING, INTEGER |
| **department**  VARIES |
| **description**  STRING |
| **directRevenuePosting**  BOOLEAN, STRING |
| **displayName**  STRING |
| **distributionCategory**  VARIES |
| **distributionNetwork**  VARIES |
| **dontShowPrice**  BOOLEAN, STRING |
| **dropshipExpenseAccount**  VARIES |
| **effectiveBomControl**  VARIES |
| **enableCatchWeight**  BOOLEAN, STRING |
| **enforceMinQtyInternally**  BOOLEAN, STRING |
| **excludeFromSitemap**  BOOLEAN, STRING |
| **expenseAccount**  VARIES |
| **expirationDate**  STRING |
| **externalId**  STRING |
| **featuredDescription**  STRING |
| **fixedBuildTime**  STRING, NUMBER |
| **fixedLotSize**  STRING, NUMBER |
| **forwardConsumptionDays**  STRING, INTEGER |
| **fraudRisk**  VARIES |
| **futureHorizon**  STRING, INTEGER |
| **gainLossAccount**  VARIES |
| **generateAccruals**  BOOLEAN, STRING |
| **handlingCost**  STRING, NUMBER |
| **handlingCostUnits**  STRING |
| **hazmatHazardClass**  STRING |
| **hazmatId**  STRING |
| **hazmatItemUnits**  STRING |
| **hazmatItemUnitsQty**  STRING, NUMBER |
| **hazmatPackingGroup**  VARIES |
| **hazmatShippingName**  STRING |
| **immediateDownload**  BOOLEAN, STRING |
| **includeChildren**  BOOLEAN, STRING |
| **includeStartEndLines**  BOOLEAN, STRING |
| **incomeAccount**  VARIES |
| **intercoCogsAccount**  VARIES |
| **intercoDefRevAccount**  VARIES |
| **intercoExpenseAccount**  VARIES |
| **intercoIncomeAccount**  VARIES |
| **internalId**  STRING |
| **invtClassification**  VARIES |
| **invtCountInterval**  STRING, INTEGER |
| **isDonationItem**  BOOLEAN, STRING |
| **isDropShipItem**  BOOLEAN, STRING |
| **isFulfillable**  BOOLEAN, STRING |
| **isGcoCompliant**  BOOLEAN, STRING |
| **isHazmatItem**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **isOnline**  BOOLEAN, STRING |
| **isPhantom**  BOOLEAN, STRING |
| **isPreTax**  BOOLEAN, STRING |
| **isSpecialOrderItem**  BOOLEAN, STRING |
| **isSpecialWorkOrderItem**  BOOLEAN, STRING |
| **isStorePickupAllowed**  BOOLEAN, STRING |
| **isTaxable**  BOOLEAN, STRING |
| **isVsoeBundle**  BOOLEAN, STRING |
| **issueProduct**  VARIES |
| **itemCarrier**  VARIES |
| **itemId**  STRING |
| **itemNumberOptionsList**  VARIES |
| **itemOptionsList**  VARIES |
| **itemRevenueCategory**  VARIES |
| **itemShipMethodList**  VARIES |
| **itemTaskTemplatesList**  VARIES |
| **itemVendorList**  VARIES |
| **lastInvtCountDate**  STRING |
| **lastModifiedDate**  STRING |
| **lastPurchasePrice**  STRING, NUMBER |
| **leadTime**  STRING, INTEGER |
| **liabilityAccount**  VARIES |
| **location**  VARIES |
| **locationsList**  VARIES |
| **lowerWarningLimit**  STRING, NUMBER |
| **manufacturer**  STRING |
| **manufacturerAddr1**  STRING |
| **manufacturerCity**  STRING |
| **manufacturerState**  STRING |
| **manufacturerTariff**  STRING |
| **manufacturerTaxId**  STRING |
| **manufacturerZip**  STRING |
| **manufactureraddr1**  STRING |
| **manufacturingChargeItem**  BOOLEAN, STRING |
| **matchBillToReceipt**  BOOLEAN, STRING |
| **matrixItemNameTemplate**  STRING |
| **matrixOptionList**  VARIES |
| **matrixType**  VARIES |
| **maxDonationAmount**  STRING, NUMBER |
| **maximumQuantity**  STRING, INTEGER |
| **memberList**  VARIES |
| **metaTagHtml**  STRING |
| **minimumQuantity**  STRING, INTEGER |
| **minimumQuantityUnits**  STRING |
| **mpn**  STRING |
| **multManufactureAddr**  BOOLEAN, STRING |
| **nexTagCategory**  STRING |
| **nextInvtCountDate**  STRING |
| **noPriceMessage**  STRING |
| **nonPosting**  BOOLEAN, STRING |
| **nullFieldList**  VARIES |
| **numOfAllowedDownloads**  STRING, INTEGER |
| **numbersList**  VARIES |
| **offerSupport**  BOOLEAN, STRING |
| **onHandValueMli**  STRING, NUMBER |
| **onSpecial**  BOOLEAN, STRING |
| **originalItemSubtype**  VARIES |
| **originalItemType**  VARIES |
| **outOfStockBehavior**  VARIES |
| **outOfStockMessage**  STRING |
| **overallQuantityPricingType**  VARIES |
| **overheadType**  VARIES |
| **pageTitle**  STRING |
| **parent**  VARIES |
| **paymentMethod**  VARIES |
| **periodicLotSizeDays**  STRING, INTEGER |
| **periodicLotSizeType**  VARIES |
| **planningItemCategory**  STRING |
| **preferenceCriterion**  VARIES |
| **preferredLocation**  VARIES |
| **preferredStockLevel**  STRING, NUMBER |
| **preferredStockLevelDays**  STRING, NUMBER |
| **preferredStockLevelUnits**  STRING |
| **presentationItemList**  VARIES |
| **pricesIncludeTax**  BOOLEAN, STRING |
| **pricingGroup**  VARIES |
| **pricingMatrix**  VARIES |
| **printItems**  BOOLEAN, STRING |
| **prodPriceVarianceAcct**  VARIES |
| **prodQtyVarianceAcct**  VARIES |
| **producer**  BOOLEAN, STRING |
| **productFeedList**  VARIES |
| **purchaseDescription**  STRING |
| **purchaseOrderAmount**  STRING, NUMBER |
| **purchaseOrderQuantity**  STRING, NUMBER |
| **purchaseOrderQuantityDiff**  STRING, NUMBER |
| **purchasePriceVarianceAcct**  VARIES |
| **purchaseTaxCode**  VARIES |
| **purchaseUnit**  VARIES |
| **quantityAvailable**  STRING, NUMBER |
| **quantityAvailableUnits**  STRING |
| **quantityBackOrdered**  STRING, NUMBER |
| **quantityCommitted**  STRING, NUMBER |
| **quantityCommittedUnits**  STRING |
| **quantityOnHand**  STRING, NUMBER |
| **quantityOnHandUnits**  STRING |
| **quantityOnOrder**  STRING, NUMBER |
| **quantityOnOrderUnits**  STRING |
| **quantityPricingSchedule**  VARIES |
| **quantityReorderUnits**  STRING |
| **rate**  STRING, NUMBER |
| **receiptAmount**  STRING, NUMBER |
| **receiptQuantity**  STRING, NUMBER |
| **receiptQuantityDiff**  STRING, NUMBER |
| **relatedItemsDescription**  STRING |
| **reorderMultiple**  STRING, INTEGER |
| **reorderPoint**  STRING, NUMBER |
| **reorderPointUnits**  STRING |
| **rescheduleInDays**  STRING, INTEGER |
| **rescheduleOutDays**  STRING, INTEGER |
| **residual**  STRING |
| **revRecForecastRule**  VARIES |
| **revRecSchedule**  VARIES |
| **revReclassFXAccount**  VARIES |
| **revenueAllocationGroup**  VARIES |
| **revenueRecognitionRule**  VARIES |
| **roundUpAsComponent**  BOOLEAN, STRING |
| **safetyStockLevel**  STRING, NUMBER |
| **safetyStockLevelDays**  STRING, INTEGER |
| **safetyStockLevelUnits**  STRING |
| **saleUnit**  VARIES |
| **salesDescription**  STRING |
| **salesTaxCode**  VARIES |
| **scheduleBCode**  VARIES |
| **scheduleBNumber**  STRING |
| **scheduleBQuantity**  STRING, INTEGER |
| **scrapAcct**  VARIES |
| **searchKeywords**  STRING |
| **seasonalDemand**  BOOLEAN, STRING |
| **secondaryBaseUnit**  STRING |
| **secondaryConsumptionUnit**  VARIES |
| **secondaryPurchaseUnit**  STRING |
| **secondarySaleUnit**  STRING |
| **secondaryStockUnit**  STRING |
| **secondaryUnitsType**  STRING |
| **serialNumbers**  STRING |
| **shipIndividually**  BOOLEAN, STRING |
| **shipPackage**  VARIES |
| **shippingCost**  STRING, NUMBER |
| **shippingCostUnits**  STRING |
| **shoppingDotComCategory**  STRING |
| **shopzillaCategoryId**  STRING, INTEGER |
| **showDefaultDonationAmount**  BOOLEAN, STRING |
| **siteCategoryList**  VARIES |
| **sitemapPriority**  VARIES |
| **softDescriptor**  VARIES |
| **specialsDescription**  STRING |
| **stockDescription**  STRING |
| **stockUnit**  VARIES |
| **storeDescription**  STRING |
| **storeDetailedDescription**  STRING |
| **storeDisplayImage**  VARIES |
| **storeDisplayName**  STRING |
| **storeDisplayThumbnail**  VARIES |
| **storeItemTemplate**  VARIES |
| **subsidiaryList**  VARIES |
| **supplyLotSizingMethod**  VARIES |
| **supplyReplenishmentMethod**  VARIES |
| **supplyTimeFence**  STRING, INTEGER |
| **supplyType**  VARIES |
| **taxSchedule**  VARIES |
| **totalValue**  STRING, NUMBER |
| **trackLandedCost**  BOOLEAN, STRING |
| **transferPrice**  STRING, NUMBER |
| **translationsList**  VARIES |
| **unbuildVarianceAccount**  VARIES |
| **undepFunds**  BOOLEAN, STRING |
| **unitsType**  VARIES |
| **upcCode**  STRING |
| **upperWarningLimit**  STRING, NUMBER |
| **urlComponent**  STRING |
| **useBins**  BOOLEAN, STRING |
| **useComponentYield**  BOOLEAN, STRING |
| **useMarginalRates**  BOOLEAN, STRING |
| **vendor**  VARIES |
| **vendorName**  STRING |
| **vsoeDeferral**  VARIES |
| **vsoeDelivered**  BOOLEAN, STRING |
| **vsoePermitDiscount**  VARIES |
| **vsoePrice**  STRING, NUMBER |
| **vsoeSopGroup**  VARIES |
| **weight**  STRING, NUMBER |
| **weightUnit**  VARIES |
| **weightUnits**  STRING |
| **wipAcct**  VARIES |
| **wipVarianceAcct**  VARIES |

### ItemAccountMapping

The `ItemAccountMapping` table contains details about the item account mapping record in your NetSuite account.

For accounts using NetSuite Multi-Book Accounting, the item account mapping record enables you to configure secondary accounting books to post to accounts different from the primary book, based on the item that is the subject of the transaction. These mappings are used by transactions where the item determines the account to which the transaction posts.

#### ItemAccountMapping table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ItemAccountMapping.html) |

ItemAccountMapping table schema

|  |
| --- |
| **\_class**  VARIES |
| **accountingBook**  VARIES |
| **customDimension**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **department**  VARIES |
| **destinationAccount**  VARIES |
| **effectiveDate**  STRING |
| **endDate**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **itemAccount**  VARIES |
| **location**  VARIES |
| **nullFieldList**  VARIES |
| **sourceAccount**  VARIES |
| **subsidiary**  VARIES |

### ItemDemandPlan

The `ItemDemandPlan` table contains info about item demand plans in your NetSuite account. An item demand plan transaction stores the quantity expected to be needed, during specified time periods, for an item.

#### ItemDemandPlan table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ItemDemandPlan.html) |

ItemDemandPlan table schema

|  |
| --- |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **demandPlanCalendarType**  VARIES |
| **demandPlanMatrix**  VARIES |
| **endDate**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **item**  VARIES |
| **location**  VARIES |
| **memo**  STRING |
| **month**  VARIES |
| **nullFieldList**  VARIES |
| **startDate**  STRING |
| **subsidiary**  VARIES |
| **units**  VARIES |
| **year**  STRING, INTEGER |

### ItemRevision

The `ItemRevision` table contains info about item revisions in your NetSuite account.

#### ItemRevision table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ItemRevision.html) |

ItemRevision table schema

|  |
| --- |
| **effectiveDate**  STRING |
| **externalId**  STRING |
| **inactive**  BOOLEAN, STRING |
| **internalId**  STRING |
| **item**  VARIES |
| **memo**  STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **obsoleteDate**  STRING |

### ItemSupplyPlan

The `ItemSupplyPlan` table contains info about the item supply plans in your NetSuite account. An item supply plan lists the purchase orders or work orders required to ensure that item quantity meets expected demand.

#### ItemSupplyPlan table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ItemSupplyPlan.html) |

ItemSupplyPlan table schema

|  |
| --- |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **item**  VARIES |
| **location**  VARIES |
| **memo**  STRING |
| **nullFieldList**  VARIES |
| **orderList**  VARIES |
| **subsidiary**  VARIES |
| **units**  VARIES |

### Job

The `Job` table contains info about the projects in your NetSuite account.

#### Job table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Job.html) |

Job table schema

|  |
| --- |
| **accountNumber**  STRING |
| **actualTime**  VARIES |
| **addressbookList**  VARIES |
| **allocatePayrollExpenses**  BOOLEAN, STRING |
| **allowAllResourcesForTasks**  BOOLEAN, STRING |
| **allowExpenses**  BOOLEAN, STRING |
| **allowTime**  BOOLEAN, STRING |
| **altName**  STRING |
| **altPhone**  STRING |
| **applyProjectExpenseTypeToAll**  BOOLEAN, STRING |
| **billPay**  BOOLEAN, STRING |
| **billingRateCard**  STRING |
| **billingSchedule**  VARIES |
| **calculatedEndDate**  STRING |
| **calculatedEndDateBaseline**  STRING |
| **calculatedStartDate**  STRING |
| **category**  VARIES |
| **comments**  STRING |
| **companyName**  STRING |
| **createChargeRule**  BOOLEAN, STRING |
| **creditCardsList**  VARIES |
| **currency**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **dateCreated**  STRING |
| **defaultAddress**  STRING |
| **email**  STRING |
| **emailPreference**  VARIES |
| **endDate**  STRING |
| **entityId**  STRING |
| **entityStatus**  VARIES |
| **estimateRevRecTemplate**  VARIES |
| **estimatedCost**  STRING, NUMBER |
| **estimatedGrossProfit**  STRING, NUMBER |
| **estimatedGrossProfitPercent**  STRING, NUMBER |
| **estimatedLaborCost**  STRING, NUMBER |
| **estimatedLaborCostBaseline**  STRING, NUMBER |
| **estimatedLaborRevenue**  STRING, NUMBER |
| **estimatedRevenue**  STRING, NUMBER |
| **estimatedTime**  VARIES |
| **estimatedTimeOverride**  VARIES |
| **externalId**  STRING |
| **fax**  STRING |
| **fxRate**  STRING, NUMBER |
| **globalSubscriptionStatus**  VARIES |
| **includeCrmTasksInTotals**  BOOLEAN, STRING |
| **internalId**  STRING |
| **isExemptTime**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **isProductiveTime**  BOOLEAN, STRING |
| **isUtilizedTime**  BOOLEAN, STRING |
| **jobBillingType**  VARIES |
| **jobItem**  VARIES |
| **jobPrice**  STRING, NUMBER |
| **jobResourcesList**  VARIES |
| **jobType**  VARIES |
| **language**  VARIES |
| **lastBaselineDate**  STRING |
| **lastModifiedDate**  STRING |
| **limitTimeToAssignees**  BOOLEAN, STRING |
| **materializeTime**  BOOLEAN, STRING |
| **milestonesList**  VARIES |
| **nullFieldList**  VARIES |
| **openingBalance**  STRING, NUMBER |
| **openingBalanceAccount**  VARIES |
| **openingBalanceDate**  STRING |
| **parent**  VARIES |
| **percentComplete**  STRING, NUMBER |
| **percentCompleteOverrideList**  VARIES |
| **percentTimeComplete**  STRING, NUMBER |
| **phone**  STRING |
| **phoneticName**  STRING |
| **plStatementList**  VARIES |
| **plannedWork**  STRING |
| **plannedWorkBaseline**  STRING |
| **projectExpenseType**  VARIES |
| **projectManager**  STRING |
| **projectedEndDate**  STRING |
| **projectedEndDateBaseline**  STRING |
| **revRecForecastRule**  VARIES |
| **scheduledEndDate**  STRING |
| **schedulingMethod**  STRING |
| **sourceServiceItemFromRateCard**  BOOLEAN, STRING |
| **startDate**  STRING |
| **startDateBaseline**  STRING |
| **subsidiary**  VARIES |
| **timeApproval**  STRING |
| **timeRemaining**  VARIES |
| **usePercentCompleteOverride**  BOOLEAN, STRING |
| **workplace**  VARIES |

### JobStatus

The `JobStatus` table contains info about the statuses that can be applied to projects in your NetSuite account.

#### JobStatus table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/JobStatus.html) |

JobStatus table schema

|  |
| --- |
| **description**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### JobType

The `JobType` table contains info about the types that can be applied to projects in your NetSuite account.

#### JobType table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/JobType.html) |

JobType table schema

|  |
| --- |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **parent**  VARIES |

### Location

The `Location` table contains info about locations.

#### Location table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Location.html) |

Location table schema

|  |
| --- |
| **allowStorePickup**  BOOLEAN, STRING |
| **autoAssignmentRegionSetting**  VARIES |
| **bufferStock**  STRING, INTEGER |
| **businessHoursList**  VARIES |
| **classTranslationList**  VARIES |
| **customFieldList**  VARIES |
| **dailyShippingCapacity**  STRING, INTEGER |
| **excludeLocationRegionsList**  VARIES |
| **externalId**  STRING |
| **geolocationMethod**  VARIES |
| **includeChildren**  BOOLEAN, STRING |
| **includeInControlTower**  BOOLEAN, STRING |
| **includeLocationRegionsList**  VARIES |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **latitude**  STRING, NUMBER |
| **locationType**  VARIES |
| **logo**  VARIES |
| **longitude**  STRING, NUMBER |
| **mainAddress**  VARIES |
| **makeInventoryAvailable**  BOOLEAN, STRING |
| **makeInventoryAvailableStore**  BOOLEAN, STRING |
| **name**  STRING |
| **nextPickupCutOffTime**  STRING |
| **nullFieldList**  VARIES |
| **parent**  VARIES |
| **returnAddress**  VARIES |
| **soPredConfidence**  STRING, NUMBER |
| **soPredictedDays**  STRING, INTEGER |
| **storePickupBufferStock**  STRING, NUMBER |
| **subsidiaryList**  VARIES |
| **timeZone**  VARIES |
| **totalShippingCapacity**  STRING, INTEGER |
| **tranPrefix**  STRING |
| **useBins**  BOOLEAN, STRING |

### ManufacturingCostTemplate

The `ManufacturingCostTemplate` table contains info about the manufacturing cost templates in your NetSuite account.

A manufacturing cost template is a list of rates that can be associated with completing a specific operation. The template defines the activities that occur and related costs to be recorded each time this step is completed.

#### ManufacturingCostTemplate table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ManufacturingCostTemplate.html) |

ManufacturingCostTemplate table schema

|  |
| --- |
| **costDetailList**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **memo**  STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **subsidiary**  VARIES |

### ManufacturingOperationTask

The `ManufacturingOperationTask` table contains info about manufacturing operation tasks in your NetSuite account.

After a WIP work order that has a designated routing is saved in NetSuite, manufacturing operation tasks are created based on the routing. Each of these tasks is a step that must be done in order for the assembly process to be finished.

#### ManufacturingOperationTask table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ManufacturingOperationTask.html) |

ManufacturingOperationTask table schema

|  |
| --- |
| **actualWork**  STRING, NUMBER |
| **autoCalculateLag**  BOOLEAN, STRING |
| **completedQuantity**  STRING, NUMBER |
| **costDetailList**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **endDate**  STRING |
| **estimatedWork**  STRING, NUMBER |
| **externalId**  STRING |
| **inputQuantity**  STRING, NUMBER |
| **internalId**  STRING |
| **laborResources**  STRING, NUMBER |
| **machineResources**  STRING, NUMBER |
| **manufacturingCostTemplate**  VARIES |
| **manufacturingWorkCenter**  VARIES |
| **message**  STRING |
| **nullFieldList**  VARIES |
| **operationSequence**  STRING, INTEGER |
| **order**  VARIES |
| **predecessorList**  VARIES |
| **remainingWork**  STRING, NUMBER |
| **runRate**  STRING, NUMBER |
| **setupTime**  STRING, NUMBER |
| **startDate**  STRING |
| **status**  VARIES |
| **title**  STRING |
| **workOrder**  VARIES |

### ManufacturingRouting

The `ManufacturingRouting` table contains info about the manufacturing routing templates in your NetSuite account.

A manufacturing routing is a template that contains a list of steps required to build an assembly item. Each step is in a sequential order necessary to complete the operational sequence for completing the assembly. After you have created a routing record, that routing can be selected on a work order to direct the completion of the assembly. The routing determines the work center, cost template, labor resources, and machine resources that will be used during the assembly.

#### ManufacturingRouting table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ManufacturingRouting.html) |

ManufacturingRouting table schema

|  |
| --- |
| **autoCalculateLag**  BOOLEAN, STRING |
| **billOfMaterials**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **isDefault**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **item**  VARIES |
| **locationList**  VARIES |
| **memo**  STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **routingComponentList**  VARIES |
| **routingStepList**  VARIES |
| **subsidiary**  VARIES |

### MerchandiseHierarchyNode

The `MerchandiseHierarchyNode` table contains info about the the categorization of inventory items in your NetSuite account.

#### MerchandiseHierarchyNode table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/MerchandiseHierarchyNode.html) |

MerchandiseHierarchyNode table schema

|  |
| --- |
| **description**  STRING |
| **externalId**  STRING |
| **hierarchyVersionsList**  VARIES |
| **internalId**  STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### Message

The `Message` table contains info about the messages in your NetSuite account.

#### Message table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Message.html) |

Message table schema

|  |
| --- |
| **activity**  VARIES |
| **author**  VARIES |
| **authorEmail**  STRING |
| **bcc**  STRING |
| **cc**  STRING |
| **compressAttachments**  BOOLEAN, STRING |
| **dateTime**  STRING |
| **emailed**  BOOLEAN, STRING |
| **externalId**  STRING |
| **incoming**  BOOLEAN, STRING |
| **internalId**  STRING |
| **lastModifiedDate**  STRING |
| **mediaItemList**  VARIES |
| **message**  STRING |
| **messageDate**  STRING |
| **nullFieldList**  VARIES |
| **recipient**  VARIES |
| **recipientEmail**  STRING |
| **recordName**  STRING |
| **recordTypeName**  STRING |
| **subject**  STRING |
| **transaction**  VARIES |

### Nexus

The `Nexus` table contains info about the tax jurisdictions - or nexus - in your NetSuite account. A nexus is a tax jurisdiction, usually defined at the country level.

#### Nexus table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Nexus.html) |

Nexus table schema

|  |
| --- |
| **country**  VARIES |
| **description**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **nullFieldList**  VARIES |
| **parentNexus**  VARIES |
| **state**  VARIES |
| **taxAgency**  VARIES |
| **taxAgencyPst**  VARIES |
| **taxCode**  VARIES |
| **taxDateFromFulfillment**  BOOLEAN, STRING |

### Note

The `Note` table contains info about the notes in your NetSuite account.

#### Note table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Note.html) |

Note table schema

|  |
| --- |
| **activity**  VARIES |
| **author**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **direction**  VARIES |
| **entity**  VARIES |
| **externalId**  STRING |
| **folder**  VARIES |
| **internalId**  STRING |
| **item**  VARIES |
| **lastModifiedDate**  STRING |
| **media**  VARIES |
| **note**  STRING |
| **noteDate**  STRING |
| **noteType**  VARIES |
| **nullFieldList**  VARIES |
| **record**  VARIES |
| **recordType**  VARIES |
| **title**  STRING |
| **topic**  VARIES |
| **transaction**  VARIES |

### NoteType

The `NoteType` table contains info about the types that can be applied to notes in your NetSuite account.

#### NoteType table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/NoteType.html) |

NoteType table schema

|  |
| --- |
| **description**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### Opportunity

The `Opportunity` table contains info about the opportunities in your NetSuite account.

#### Opportunity table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Opportunity.html) |

Opportunity table schema

|  |
| --- |
| **\_class**  VARIES |
| **accountingBookDetailList**  VARIES |
| **actionItem**  STRING |
| **altSalesRangeHigh**  STRING, NUMBER |
| **altSalesRangeLow**  STRING, NUMBER |
| **billAddressList**  VARIES |
| **billingAddress**  VARIES |
| **buyingReason**  VARIES |
| **buyingTimeFrame**  VARIES |
| **closeDate**  STRING |
| **competitorsList**  VARIES |
| **contribPct**  STRING |
| **createdDate**  STRING |
| **currency**  VARIES |
| **currencyName**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **daysOpen**  STRING, INTEGER |
| **department**  VARIES |
| **entity**  VARIES |
| **entityStatus**  VARIES |
| **entityTaxRegNum**  VARIES |
| **estGrossProfit**  STRING, NUMBER |
| **estGrossProfitPercent**  STRING, NUMBER |
| **estimatedBudget**  STRING, NUMBER |
| **exchangeRate**  STRING, NUMBER |
| **expectedCloseDate**  STRING |
| **externalId**  STRING |
| **forecastType**  VARIES |
| **internalId**  STRING |
| **isBudgetApproved**  BOOLEAN, STRING |
| **itemList**  VARIES |
| **job**  VARIES |
| **lastModifiedDate**  STRING |
| **leadSource**  VARIES |
| **location**  VARIES |
| **memo**  STRING |
| **nexus**  VARIES |
| **nullFieldList**  VARIES |
| **oneTime**  STRING, NUMBER |
| **partner**  VARIES |
| **partnersList**  VARIES |
| **probability**  STRING, NUMBER |
| **projAltSalesAmt**  STRING, NUMBER |
| **projectedTotal**  STRING, NUMBER |
| **rangeHigh**  STRING, NUMBER |
| **rangeLow**  STRING, NUMBER |
| **recurAnnually**  STRING, NUMBER |
| **recurMonthly**  STRING, NUMBER |
| **recurQuarterly**  STRING, NUMBER |
| **recurWeekly**  STRING, NUMBER |
| **salesGroup**  VARIES |
| **salesReadiness**  VARIES |
| **salesRep**  VARIES |
| **salesTeamList**  VARIES |
| **shipAddressList**  VARIES |
| **shipIsResidential**  BOOLEAN, STRING |
| **shippingAddress**  VARIES |
| **source**  STRING |
| **status**  STRING |
| **subsidiary**  VARIES |
| **subsidiaryTaxRegNum**  VARIES |
| **syncPartnerTeams**  BOOLEAN, STRING |
| **syncSalesTeams**  BOOLEAN, STRING |
| **tax2Total**  STRING, NUMBER |
| **taxDetailsList**  VARIES |
| **taxDetailsOverride**  BOOLEAN, STRING |
| **taxPointDate**  STRING |
| **taxRegOverride**  BOOLEAN, STRING |
| **taxTotal**  STRING, NUMBER |
| **title**  STRING |
| **totalCostEstimate**  STRING, NUMBER |
| **tranDate**  STRING |
| **tranId**  STRING |
| **vatRegNum**  STRING |
| **weightedTotal**  STRING, NUMBER |
| **winLossReason**  VARIES |

### OtherNameCategory

The `OtherNameCategory` table contains info about the other name categories in your NetSuite account. Other name category values are used on other name records to categorize them. The list of other name records is a collection of records for people or companies who are not vendors, customers, or employees.

#### OtherNameCategory table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/OtherNameCategory.html) |

OtherNameCategory table schema

|  |
| --- |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### Partner

The `Partner` table contains info about the partners in your NetSuite account.

#### Partner table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Partner.html) |

Partner table schema

|  |
| --- |
| **\_class**  VARIES |
| **accessRole**  VARIES |
| **addressbookList**  VARIES |
| **altEmail**  STRING |
| **altName**  STRING |
| **bcn**  STRING |
| **categoryList**  VARIES |
| **comments**  STRING |
| **companyName**  STRING |
| **contactRolesList**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **dateCreated**  STRING |
| **defaultAddress**  STRING |
| **defaultTaxReg**  STRING |
| **department**  VARIES |
| **eligibleForCommission**  BOOLEAN, STRING |
| **email**  STRING |
| **emailPreference**  VARIES |
| **entityId**  STRING |
| **externalId**  STRING |
| **fax**  STRING |
| **firstName**  STRING |
| **giveAccess**  BOOLEAN, STRING |
| **globalSubscriptionStatus**  VARIES |
| **homePhone**  STRING |
| **image**  VARIES |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isPerson**  BOOLEAN, STRING |
| **lastModifiedDate**  STRING |
| **lastName**  STRING |
| **location**  VARIES |
| **loginAs**  STRING |
| **middleName**  STRING |
| **mobilePhone**  STRING |
| **nullFieldList**  VARIES |
| **parent**  VARIES |
| **partnerCode**  STRING |
| **password**  STRING |
| **password2**  STRING |
| **phone**  STRING |
| **phoneticName**  STRING |
| **printOnCheckAs**  STRING |
| **promoCodeList**  VARIES |
| **referringUrl**  STRING |
| **requirePwdChange**  BOOLEAN, STRING |
| **roleList**  VARIES |
| **salutation**  STRING |
| **sendEmail**  BOOLEAN, STRING |
| **subPartnerLogin**  BOOLEAN, STRING |
| **subscriptionsList**  VARIES |
| **subsidiary**  VARIES |
| **taxFractionUnit**  VARIES |
| **taxIdNum**  STRING |
| **taxRegistrationList**  VARIES |
| **taxRounding**  VARIES |
| **title**  STRING |
| **url**  STRING |
| **vatRegNumber**  STRING |

### PartnerCategory

The `PartnerCategory` table contains info about the categories that can be applied to partners in your NetSuite account.

#### PartnerCategory table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PartnerCategory.html) |

PartnerCategory table schema

|  |
| --- |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **parent**  VARIES |

### Paycheck

The `Paycheck` table contains info about the paycheck records in your NetSuite account.

#### Paycheck table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Paycheck.html) |

Paycheck table schema

|  |
| --- |
| **\_class**  VARIES |
| **account**  VARIES |
| **address**  STRING |
| **balance**  STRING, NUMBER |
| **batchNumber**  STRING |
| **createdDate**  STRING |
| **department**  VARIES |
| **entity**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **lastModifiedDate**  STRING |
| **location**  VARIES |
| **memo**  STRING |
| **nullFieldList**  VARIES |
| **payContribList**  VARIES |
| **payDeductList**  VARIES |
| **payDisburseList**  VARIES |
| **payEarnList**  VARIES |
| **payExpList**  VARIES |
| **payFrequency**  STRING |
| **payPtoList**  VARIES |
| **paySummaryList**  VARIES |
| **payTaxList**  VARIES |
| **payTimeList**  VARIES |
| **periodEnding**  STRING |
| **postingPeriod**  VARIES |
| **status**  STRING |
| **tranDate**  STRING |
| **tranId**  STRING |
| **userAmount**  STRING, NUMBER |
| **workplace**  VARIES |

### PaymentMethod

The `PaymentMethod` table contains info about the customer payment methods in your NetSuite account.

#### PaymentMethod table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PaymentMethod.html) |

PaymentMethod table schema

|  |
| --- |
| **account**  VARIES |
| **creditCard**  BOOLEAN, STRING |
| **expressCheckoutArrangement**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isDebitCard**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **isOnline**  BOOLEAN, STRING |
| **merchantAccountsList**  VARIES |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **payPalEmailAddress**  STRING |
| **undepFunds**  BOOLEAN, STRING |
| **useExpressCheckout**  BOOLEAN, STRING |
| **visualsList**  VARIES |

### PayrollItem

The `PayrollItem` table contains info about the payroll items, or payroll transaction line items, in your NetSuite account.

#### PayrollItem table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PayrollItem.html) |

PayrollItem table schema

|  |
| --- |
| **accountCategory**  VARIES |
| **customFieldList**  VARIES |
| **employeePaid**  BOOLEAN, STRING |
| **expenseAccount**  VARIES |
| **externalId**  STRING |
| **inactive**  BOOLEAN, STRING |
| **internalId**  STRING |
| **itemType**  VARIES |
| **liabilityAccount**  VARIES |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **subsidiary**  VARIES |
| **vendor**  VARIES |

### PhoneCall

The `PhoneCall` table contains info about the phone call records in your NetSuite account.

#### PhoneCall table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PhoneCall.html) |

PhoneCall table schema

|  |
| --- |
| **accessLevel**  BOOLEAN, STRING |
| **assigned**  VARIES |
| **company**  VARIES |
| **completedDate**  STRING |
| **contact**  VARIES |
| **contactList**  VARIES |
| **createdDate**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **endDate**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **lastModifiedDate**  STRING |
| **message**  STRING |
| **milestone**  VARIES |
| **nullFieldList**  VARIES |
| **owner**  VARIES |
| **phone**  STRING |
| **priority**  VARIES |
| **reminderMinutes**  VARIES |
| **reminderType**  VARIES |
| **sendEmail**  BOOLEAN, STRING |
| **startDate**  STRING |
| **status**  VARIES |
| **supportCase**  VARIES |
| **timeItemList**  VARIES |
| **timedEvent**  BOOLEAN, STRING |
| **title**  STRING |
| **transaction**  VARIES |

### PriceLevel

The `PriceLevel` table contains info about the price level list in your NetSuite account. Price level defines a list of values that are used by opportunity and item records to set the price level for a specific item.

#### PriceLevel table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PriceLevel.html) |

PriceLevel table schema

|  |
| --- |
| **discountpct**  STRING, NUMBER |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isOnline**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **updateExistingPrices**  BOOLEAN, STRING |

### PricingGroup

The `PricingGroup` table contains info about the pricing groups in your NetSuite account.

#### PricingGroup table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PricingGroup.html) |

PricingGroup table schema

|  |
| --- |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### ProjectTask

The `ProjectTask` table contains info about the project tasks in your NetSuite account.

#### ProjectTask table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ProjectTask.html) |

ProjectTask table schema

|  |
| --- |
| **actualWork**  STRING, NUMBER |
| **assigneeList**  VARIES |
| **company**  VARIES |
| **constraintType**  VARIES |
| **contact**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **endDate**  STRING |
| **endDateBaseline**  STRING |
| **estimatedWork**  STRING, NUMBER |
| **estimatedWorkBaseline**  STRING, NUMBER |
| **eventId**  VARIES |
| **externalId**  STRING |
| **finishByDate**  STRING |
| **internalId**  STRING |
| **isMilestone**  BOOLEAN, STRING |
| **isOnCriticalPath**  STRING |
| **lateEnd**  STRING |
| **lateStart**  STRING |
| **message**  STRING |
| **nonBillableTask**  BOOLEAN, STRING |
| **nullFieldList**  VARIES |
| **order**  VARIES |
| **owner**  VARIES |
| **parent**  VARIES |
| **percentTimeComplete**  STRING, NUMBER |
| **plannedWork**  STRING, NUMBER |
| **plannedWorkBaseline**  STRING, NUMBER |
| **predecessorList**  VARIES |
| **priority**  VARIES |
| **remainingWork**  STRING, NUMBER |
| **slackMinutes**  STRING, NUMBER |
| **startDate**  STRING |
| **startDateBaseline**  STRING |
| **status**  VARIES |
| **timeItemList**  VARIES |
| **title**  STRING |

### PromotionCode

The `PromotionCode` table contains info about the promotion codes in your NetSuite account.

#### PromotionCode table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PromotionCode.html) |

PromotionCode table schema

|  |
| --- |
| **applyDiscountTo**  VARIES |
| **code**  STRING |
| **codePattern**  STRING |
| **currencyList**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **description**  STRING |
| **discount**  VARIES |
| **discountType**  BOOLEAN, STRING |
| **displayLineDiscounts**  BOOLEAN, STRING |
| **endDate**  STRING |
| **excludeItems**  BOOLEAN, STRING |
| **externalId**  STRING |
| **freeShipMethod**  VARIES |
| **implementation**  VARIES |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isPublic**  BOOLEAN, STRING |
| **itemsList**  VARIES |
| **locationList**  VARIES |
| **minimumOrderAmount**  STRING, NUMBER |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **numberToGenerate**  STRING, INTEGER |
| **partnersList**  VARIES |
| **rate**  STRING |
| **startDate**  STRING |
| **useType**  VARIES |

### ResourceAllocation

The `ResourceAllocation` table contains info about resource allocations, or employee time reservations, in your NetSuite account.

#### ResourceAllocation table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ResourceAllocation.html) |

ResourceAllocation table schema

|  |
| --- |
| **allocationAmount**  STRING, NUMBER |
| **allocationResource**  VARIES |
| **allocationType**  VARIES |
| **allocationUnit**  VARIES |
| **approvalStatus**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **endDate**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **nextApprover**  VARIES |
| **notes**  STRING |
| **nullFieldList**  VARIES |
| **numberHours**  STRING, NUMBER |
| **percentOfTime**  STRING, NUMBER |
| **project**  VARIES |
| **requestedby**  VARIES |
| **startDate**  STRING |

### RevRecSchedule

The `RevRecSchedule` table contains info about the revenue recognition schedules in your NetSuite account. A revenue recognition schedule indicates the posting periods in which revenue should be recognized, and the amount to be recognized in each period, for an item sale.

#### RevRecSchedule table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/RevRecSchedule.html) |

RevRecSchedule table schema

|  |
| --- |
| **amortizationPeriod**  STRING, INTEGER |
| **amortizationType**  VARIES |
| **externalId**  STRING |
| **initialAmount**  STRING, NUMBER |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **periodOffset**  STRING, INTEGER |
| **recogIntervalSrc**  VARIES |
| **recurrenceList**  VARIES |
| **recurrenceType**  VARIES |
| **revRecOffset**  STRING, INTEGER |

### RevRecTemplate

The `RevRecTemplate` table contains info about the revenue recognition templates in your NetSuite account. A revenue recognition template indicates how revenue from associated items should be posted.

#### RevRecTemplate table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/RevRecTemplate.html) |

RevRecTemplate table schema

|  |
| --- |
| **amortizationPeriod**  STRING, INTEGER |
| **amortizationType**  VARIES |
| **externalId**  STRING |
| **initialAmount**  STRING, NUMBER |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **periodOffset**  STRING, INTEGER |
| **recogIntervalSrc**  VARIES |
| **recurrenceList**  VARIES |
| **recurrenceType**  VARIES |
| **revRecOffset**  STRING, INTEGER |

### SalesRole

The `SalesRole` table contains info about the sales roles in your NetSuite account.

#### SalesRole table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/SalesRole.html) |

SalesRole table schema

|  |
| --- |
| **description**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isSalesRep**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### SalesTaxItem

The `SalesTaxItem` table contains info about the sales tax items in your NetSuite account.

#### SalesTaxItem table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/SalesTaxItem.html) |

SalesTaxItem table schema

|  |
| --- |
| **available**  VARIES |
| **city**  STRING |
| **county**  STRING |
| **customFieldList**  VARIES |
| **description**  STRING |
| **displayName**  STRING |
| **eccode**  BOOLEAN, STRING |
| **effectiveFrom**  STRING |
| **excludeFromTaxReports**  BOOLEAN, STRING |
| **exempt**  BOOLEAN, STRING |
| **export**  BOOLEAN, STRING |
| **externalId**  STRING |
| **includeChildren**  BOOLEAN, STRING |
| **internalId**  STRING |
| **isDefault**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **itemId**  STRING |
| **name**  STRING |
| **nexusCountry**  VARIES |
| **nullFieldList**  VARIES |
| **parent**  VARIES |
| **purchaseAccount**  VARIES |
| **rate**  STRING |
| **reverseCharge**  BOOLEAN, STRING |
| **saleAccount**  VARIES |
| **service**  BOOLEAN, STRING |
| **state**  STRING |
| **subsidiaryList**  VARIES |
| **taxAccount**  VARIES |
| **taxAgency**  VARIES |
| **taxType**  VARIES |
| **validUntil**  STRING |
| **zip**  STRING |

### SiteCategory

The `SiteCategory` table contains info about the categories used to organize your website.

#### SiteCategory table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/SiteCategory.html) |

SiteCategory table schema

|  |
| --- |
| **categoryListLayout**  VARIES |
| **correlatedItemsListLayout**  VARIES |
| **description**  STRING |
| **excludeFromSitemap**  BOOLEAN, STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isOnline**  BOOLEAN, STRING |
| **itemId**  STRING |
| **itemListLayout**  VARIES |
| **metaTagHtml**  STRING |
| **nullFieldList**  VARIES |
| **pageTitle**  STRING |
| **parentCategory**  VARIES |
| **presentationItemList**  VARIES |
| **relatedItemsListLayout**  VARIES |
| **searchKeywords**  STRING |
| **sitemapPriority**  VARIES |
| **storeDetailedDescription**  STRING |
| **storeDisplayImage**  VARIES |
| **storeDisplayThumbnail**  VARIES |
| **translationsList**  VARIES |
| **urlComponent**  STRING |
| **website**  VARIES |

### Solution

The `Solution` table contains info about the solutions, or answers to customer issues, in your NetSuite account.

#### Solution table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Solution.html) |

Solution table schema

|  |
| --- |
| **assigned**  VARIES |
| **createdDate**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **displayOnline**  BOOLEAN, STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **lastModifiedDate**  STRING |
| **longDescription**  STRING |
| **message**  STRING |
| **nullFieldList**  VARIES |
| **solutionCode**  STRING |
| **solutionsList**  VARIES |
| **status**  VARIES |
| **title**  STRING |
| **topicsList**  VARIES |

### Subsidiary

The `Subsidiary` table contains info about the subsidiary records in your NetSuite account. A subsidiary represents a separate company within your global organization.

#### Subsidiary table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Subsidiary.html) |

Subsidiary table schema

|  |
| --- |
| **accountingBookDetailList**  VARIES |
| **addrLanguage**  STRING |
| **allowPayroll**  BOOLEAN, STRING |
| **checkLayout**  VARIES |
| **classTranslationList**  VARIES |
| **country**  VARIES |
| **currency**  VARIES |
| **customFieldList**  VARIES |
| **edition**  STRING |
| **email**  STRING |
| **externalId**  STRING |
| **fax**  STRING |
| **federalIdNumber**  STRING |
| **fiscalCalendar**  VARIES |
| **interCoAccount**  VARIES |
| **internalId**  STRING |
| **isElimination**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **legalName**  STRING |
| **logo**  VARIES |
| **mainAddress**  VARIES |
| **name**  STRING |
| **nexusList**  VARIES |
| **nullFieldList**  VARIES |
| **pageLogo**  VARIES |
| **parent**  VARIES |
| **purchaseOrderAmount**  STRING, NUMBER |
| **purchaseOrderQuantity**  STRING, NUMBER |
| **purchaseOrderQuantityDiff**  STRING, NUMBER |
| **receiptAmount**  STRING, NUMBER |
| **receiptQuantity**  STRING, NUMBER |
| **receiptQuantityDiff**  STRING, NUMBER |
| **returnAddress**  VARIES |
| **shippingAddress**  VARIES |
| **showSubsidiaryName**  BOOLEAN, STRING |
| **ssnOrTin**  STRING |
| **state**  STRING |
| **state1TaxNumber**  STRING |
| **taxFiscalCalendar**  VARIES |
| **taxRegistrationList**  VARIES |
| **tranPrefix**  STRING |
| **url**  STRING |

### SupportCase

The `SupportCase` table contains info about the support cases in your NetSuite account.

#### SupportCase table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/SupportCase.html) |

SupportCase table schema

|  |
| --- |
| **assigned**  VARIES |
| **caseNumber**  STRING |
| **category**  VARIES |
| **company**  VARIES |
| **contact**  VARIES |
| **createdDate**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **email**  STRING |
| **emailEmployeesList**  VARIES |
| **emailForm**  BOOLEAN, STRING |
| **endDate**  STRING |
| **escalateToList**  VARIES |
| **escalationMessage**  STRING |
| **externalId**  STRING |
| **helpDesk**  BOOLEAN, STRING |
| **inboundEmail**  STRING |
| **incomingMessage**  STRING |
| **insertSolution**  VARIES |
| **internalId**  STRING |
| **internalOnly**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **issue**  VARIES |
| **item**  VARIES |
| **lastMessageDate**  STRING |
| **lastModifiedDate**  STRING |
| **lastReopenedDate**  STRING |
| **module**  VARIES |
| **newSolutionFromMsg**  STRING |
| **nullFieldList**  VARIES |
| **origin**  VARIES |
| **outgoingMessage**  STRING |
| **phone**  STRING |
| **priority**  VARIES |
| **product**  VARIES |
| **profile**  VARIES |
| **searchSolution**  STRING |
| **serialNumber**  VARIES |
| **solutionsList**  VARIES |
| **startDate**  STRING |
| **status**  VARIES |
| **subsidiary**  VARIES |
| **timeItemList**  VARIES |
| **title**  STRING |

### Task

The `Task` table contains info about the tasks in your NetSuite account.

#### Task table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Task.html) |

Task table schema

|  |
| --- |
| **accessLevel**  BOOLEAN, STRING |
| **actualTime**  VARIES |
| **assigned**  VARIES |
| **company**  VARIES |
| **completedDate**  STRING |
| **contact**  VARIES |
| **contactList**  VARIES |
| **createdDate**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **dueDate**  STRING |
| **endDate**  STRING |
| **estimatedTime**  VARIES |
| **estimatedTimeOverride**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **lastModifiedDate**  STRING |
| **message**  STRING |
| **milestone**  VARIES |
| **nullFieldList**  VARIES |
| **owner**  VARIES |
| **parent**  VARIES |
| **percentComplete**  STRING, NUMBER |
| **percentTimeComplete**  STRING, NUMBER |
| **priority**  VARIES |
| **reminderMinutes**  VARIES |
| **reminderType**  VARIES |
| **sendEmail**  BOOLEAN, STRING |
| **startDate**  STRING |
| **status**  VARIES |
| **supportCase**  VARIES |
| **timeItemList**  VARIES |
| **timeRemaining**  VARIES |
| **timedEvent**  BOOLEAN, STRING |
| **title**  STRING |
| **transaction**  VARIES |

### TaxGroup

The `TaxGroup` table contains info about the tax groups in your NetSuite account.

#### TaxGroup table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TaxGroup.html) |

TaxGroup table schema

|  |
| --- |
| **city**  STRING |
| **county**  STRING |
| **description**  STRING |
| **externalId**  STRING |
| **includeChildren**  BOOLEAN, STRING |
| **internalId**  STRING |
| **isDefault**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **itemId**  STRING |
| **nexusCountry**  VARIES |
| **nullFieldList**  VARIES |
| **piggyback**  BOOLEAN, STRING |
| **rate**  STRING, NUMBER |
| **state**  STRING |
| **subsidiaryList**  VARIES |
| **taxItemList**  VARIES |
| **taxType**  VARIES |
| **taxitem1**  VARIES |
| **taxitem2**  VARIES |
| **unitprice1**  STRING |
| **unitprice2**  STRING |
| **zip**  STRING |

### TaxType

The `TaxType` table contains info about the tax types in your NetSuite account. A tax type determines where the tax paid or collected is tracked on the balance sheet. The balance sheet account to which NetSuite posts the collection or payment of tax is called the tax control account.

#### TaxType table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TaxType.html) |

TaxType table schema

|  |
| --- |
| **country**  VARIES |
| **description**  STRING |
| **doesNotAddToTotal**  BOOLEAN, STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nexusAccountsList**  VARIES |
| **nexusesTaxList**  VARIES |
| **nullFieldList**  VARIES |
| **postToItemCost**  BOOLEAN, STRING |
| **reverseCharge**  BOOLEAN, STRING |
| **taxInNetAmount**  BOOLEAN, STRING |

### Term

The `Term` table contains info about the terms in your NetSuite account. Terms are used to specify when payment is due on customer invoices.

#### Term table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Term.html) |

Term table schema

|  |
| --- |
| **dateDriven**  BOOLEAN, STRING |
| **dayDiscountExpires**  STRING, INTEGER |
| **dayOfMonthNetDue**  STRING, INTEGER |
| **daysUntilExpiry**  STRING, INTEGER |
| **daysUntilNetDue**  STRING, INTEGER |
| **discountPercent**  STRING, NUMBER |
| **discountPercentDateDriven**  STRING, NUMBER |
| **dueNextMonthIfWithinDays**  STRING, INTEGER |
| **externalId**  STRING |
| **installment**  BOOLEAN, STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **percentagesList**  VARIES |
| **preferred**  BOOLEAN, STRING |
| **recurrenceCount**  STRING, INTEGER |
| **recurrenceFrequency**  STRING |
| **repeatEvery**  STRING, INTEGER |
| **splitEvenly**  BOOLEAN, STRING |

### TimeBill

The `TimeBill` table contains info about the time transactions in your NetSuite account. Also known as time bills, these transactions records the hours worked by an employee. This transaction can be used to record billable hours and invoice customers.

#### TimeBill table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TimeBill.html) |

TimeBill table schema

|  |
| --- |
| **\_class**  VARIES |
| **approvalStatus**  VARIES |
| **caseTaskEvent**  VARIES |
| **createdDate**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **customer**  VARIES |
| **department**  VARIES |
| **employee**  VARIES |
| **externalId**  STRING |
| **hours**  VARIES |
| **internalId**  STRING |
| **isBillable**  BOOLEAN, STRING |
| **item**  VARIES |
| **lastModifiedDate**  STRING |
| **location**  VARIES |
| **memo**  STRING |
| **nullFieldList**  VARIES |
| **overrideRate**  BOOLEAN, STRING |
| **paidExternally**  BOOLEAN, STRING |
| **payrollItem**  VARIES |
| **price**  VARIES |
| **rate**  STRING, NUMBER |
| **rejectionNote**  STRING |
| **status**  STRING |
| **subsidiary**  VARIES |
| **supervisorApproval**  BOOLEAN, STRING |
| **temporaryLocalJurisdiction**  VARIES |
| **temporaryStateJurisdiction**  VARIES |
| **timeModified**  BOOLEAN, STRING |
| **timeSheet**  VARIES |
| **timeType**  VARIES |
| **tranDate**  STRING |
| **workplace**  VARIES |

### TimeEntry

The `TimeEntry` table contains info about the time entries in your NetSuite account.

#### TimeEntry table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TimeEntry.html) |

TimeEntry table schema

|  |
| --- |
| **\_class**  VARIES |
| **approvalStatus**  VARIES |
| **billingClass**  STRING |
| **caseTaskEvent**  VARIES |
| **createdDate**  STRING |
| **customFieldList**  VARIES |
| **customer**  VARIES |
| **department**  VARIES |
| **externalId**  STRING |
| **hours**  VARIES |
| **internalId**  STRING |
| **isBillable**  BOOLEAN, STRING |
| **item**  VARIES |
| **lastModifiedDate**  STRING |
| **location**  VARIES |
| **memo**  STRING |
| **nullFieldList**  VARIES |
| **overrideRate**  BOOLEAN, STRING |
| **paidExternally**  BOOLEAN, STRING |
| **payrollItem**  VARIES |
| **price**  VARIES |
| **rate**  STRING, NUMBER |
| **subsidiary**  VARIES |
| **timeType**  VARIES |

### TimeSheet

The `TimeSheet` table contains info about the time sheets in your NetSuite account.

#### TimeSheet table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TimeSheet.html) |

TimeSheet table schema

|  |
| --- |
| **approvalStatus**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **employee**  VARIES |
| **endDate**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **nullFieldList**  VARIES |
| **startDate**  STRING |
| **subsidiary**  VARIES |
| **timeGridList**  VARIES |
| **totalHours**  VARIES |

### Topic

The `Topic` table contains info about the topics used to organize knowledge base solutions in your NetSuite account.

#### Topic table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Topic.html) |

Topic table schema

|  |
| --- |
| **description**  STRING |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **longDescription**  STRING |
| **nullFieldList**  VARIES |
| **parentTopic**  VARIES |
| **solutionList**  VARIES |
| **title**  STRING |

### Transaction

The `Transaction` table contains info about transactions.

#### Supported transaction types

NetSuite integration supports replicating data for the the transaction types in the [Supported NetSuite transaction types](#supported-transaction-types) section.

#### Transaction table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/script/record/transaction.html) |

Transaction table schema

|  |
| --- |
| **\_class**  VARIES |
| **\_type**  STRING |
| **accessibilityTypeFedEx**  VARIES |
| **account**  VARIES |
| **accountingApproval**  BOOLEAN, STRING |
| **accountingBook**  VARIES |
| **accountingBookDetailList**  VARIES |
| **acctCorpCardExp**  VARIES |
| **actualProductionEndDate**  STRING |
| **actualProductionStartDate**  STRING |
| **actualShipDate**  STRING |
| **adjLocation**  VARIES |
| **advance**  STRING, NUMBER |
| **altHandlingCost**  STRING, NUMBER |
| **altSalesTotal**  STRING, NUMBER |
| **altShippingCost**  STRING, NUMBER |
| **amount**  STRING, NUMBER |
| **amountPaid**  STRING, NUMBER |
| **amountRemaining**  STRING, NUMBER |
| **ancillaryEndorsementFedEx**  VARIES |
| **apAcct**  VARIES |
| **applied**  STRING, NUMBER |
| **applyList**  VARIES |
| **approvalStatus**  VARIES |
| **approved**  BOOLEAN, STRING |
| **arAcct**  VARIES |
| **assemblyItem**  VARIES |
| **authCode**  STRING |
| **autoApply**  BOOLEAN, STRING |
| **autoCalculateLag**  BOOLEAN, STRING |
| **availableBalance**  STRING, NUMBER |
| **availableVendorCredit**  STRING, NUMBER |
| **b13AFilingOptionFedEx**  VARIES |
| **b13AStatementDataFedEx**  STRING |
| **backupEmailAddressFedEx**  STRING |
| **backupEmailAddressUps**  STRING |
| **balance**  STRING, NUMBER |
| **billAddressList**  VARIES |
| **billOfMaterials**  VARIES |
| **billOfMaterialsRevision**  VARIES |
| **billPay**  BOOLEAN, STRING |
| **billingAccount**  VARIES |
| **billingAddress**  VARIES |
| **billingSchedule**  VARIES |
| **binNumbers**  STRING |
| **blanketEndDateUps**  STRING |
| **blanketStartDateUps**  STRING |
| **bookingConfirmationNumFedEx**  STRING |
| **buildable**  STRING, NUMBER |
| **built**  STRING, NUMBER |
| **canHaveStackable**  BOOLEAN, STRING |
| **carrierIdUps**  STRING |
| **cashBackList**  VARIES |
| **ccApproved**  BOOLEAN, STRING |
| **ccAvsStreetMatch**  VARIES |
| **ccAvsZipMatch**  VARIES |
| **ccExpireDate**  STRING |
| **ccIsPurchaseCardBin**  BOOLEAN, STRING |
| **ccName**  STRING |
| **ccNumber**  STRING |
| **ccProcessAsPurchaseCard**  BOOLEAN, STRING |
| **ccSecurityCode**  STRING |
| **ccSecurityCodeMatch**  VARIES |
| **ccStreet**  STRING |
| **ccZipCode**  STRING |
| **chargeIt**  BOOLEAN, STRING |
| **checkNum**  STRING |
| **checkNumber**  STRING |
| **companyContributionList**  VARIES |
| **companyTaxList**  VARIES |
| **complete**  BOOLEAN, STRING |
| **completedQuantity**  STRING, NUMBER |
| **componentList**  VARIES |
| **contribPct**  STRING |
| **costComponentList**  VARIES |
| **createdDate**  STRING |
| **createdFrom**  VARIES |
| **createdFromShipGroup**  STRING, INTEGER |
| **creditCard**  VARIES |
| **creditCardProcessor**  VARIES |
| **creditLimit**  STRING, NUMBER |
| **creditList**  VARIES |
| **currency**  VARIES |
| **currencyName**  STRING |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **customer**  VARIES |
| **debitCardIssueNo**  STRING |
| **deductionList**  VARIES |
| **deferredRevenue**  STRING, NUMBER |
| **depDate**  STRING |
| **department**  VARIES |
| **deposit**  VARIES |
| **depositList**  VARIES |
| **discountAmount**  STRING, NUMBER |
| **discountDate**  STRING |
| **discountItem**  VARIES |
| **discountRate**  STRING |
| **discountTotal**  STRING, NUMBER |
| **drAccount**  VARIES |
| **dueDate**  STRING |
| **dynamicDescriptor**  STRING |
| **earningList**  VARIES |
| **eccNumberUps**  STRING |
| **email**  STRING |
| **employee**  VARIES |
| **employeeTaxList**  VARIES |
| **endDate**  STRING |
| **endOperation**  VARIES |
| **entity**  VARIES |
| **entityStatus**  VARIES |
| **entityTaxRegNum**  VARIES |
| **entryNumberUps**  STRING |
| **estGrossProfit**  STRING, NUMBER |
| **estGrossProfitPercent**  STRING, NUMBER |
| **estimatedTotalValue**  STRING, NUMBER |
| **exchangeRate**  STRING, NUMBER |
| **excludeCommission**  BOOLEAN, STRING |
| **expCostDiscAmount**  STRING, NUMBER |
| **expCostDiscPrint**  BOOLEAN, STRING |
| **expCostDiscRate**  STRING |
| **expCostDiscTax1Amt**  STRING, NUMBER |
| **expCostDiscTaxable**  BOOLEAN, STRING |
| **expCostDiscount**  VARIES |
| **expCostDiscprint**  BOOLEAN, STRING |
| **expCostList**  VARIES |
| **expCostTaxCode**  VARIES |
| **expCostTaxRate1**  STRING, NUMBER |
| **expCostTaxRate2**  STRING, NUMBER |
| **expandAssembly**  BOOLEAN, STRING |
| **expectedCloseDate**  STRING |
| **expenseList**  VARIES |
| **expenseReportCurrency**  VARIES |
| **expenseReportExchangeRate**  STRING, NUMBER |
| **expirationDate**  STRING |
| **exportTypeUps**  VARIES |
| **externalId**  STRING |
| **fax**  STRING |
| **firmed**  BOOLEAN, STRING |
| **fob**  STRING |
| **forecastType**  VARIES |
| **fxAccount**  VARIES |
| **generateIntegratedShipperLabel**  BOOLEAN, STRING |
| **getAuth**  BOOLEAN, STRING |
| **giftCert**  VARIES |
| **giftCertApplied**  STRING, NUMBER |
| **giftCertAvailable**  STRING, NUMBER |
| **giftCertRedemptionList**  VARIES |
| **giftCertTotal**  STRING, NUMBER |
| **halAddr1FedEx**  STRING |
| **halAddr2FedEx**  STRING |
| **halAddr3FedEx**  STRING |
| **halCityFedEx**  STRING |
| **halCountryFedEx**  STRING |
| **halPhoneFedEx**  STRING |
| **halStateFedEx**  STRING |
| **halZipFedEx**  STRING |
| **handlingCost**  STRING, NUMBER |
| **handlingMode**  VARIES |
| **handlingTax1Rate**  STRING, NUMBER |
| **handlingTax2Rate**  STRING, NUMBER |
| **handlingTaxCode**  VARIES |
| **hazmatTypeFedEx**  VARIES |
| **holdAtLocationFedEx**  BOOLEAN, STRING |
| **homeDeliveryDateFedEx**  STRING |
| **homeDeliveryTypeFedEx**  VARIES |
| **ignoreAvs**  BOOLEAN, STRING |
| **inbondCodeUps**  STRING |
| **inboundShipment**  VARIES |
| **includeInForecast**  BOOLEAN, STRING |
| **incoterm**  VARIES |
| **inputAuthCode**  STRING |
| **inputReferenceCode**  STRING |
| **insideDeliveryFedEx**  BOOLEAN, STRING |
| **insidePickupFedEx**  BOOLEAN, STRING |
| **installmentList**  VARIES |
| **intercoStatus**  VARIES |
| **intercoTransaction**  VARIES |
| **internalId**  STRING |
| **intlExemptionNumFedEx**  STRING |
| **inventoryDetail**  VARIES |
| **inventoryList**  VARIES |
| **inventoryValue**  STRING, NUMBER |
| **isBackflush**  BOOLEAN, STRING |
| **isBookSpecific**  BOOLEAN, STRING |
| **isCargoAircraftOnlyFedEx**  BOOLEAN, STRING |
| **isInTransitPayment**  BOOLEAN, STRING |
| **isMultiShipTo**  BOOLEAN, STRING |
| **isRecurringPayment**  BOOLEAN, STRING |
| **isRoutedExportTransactionUps**  BOOLEAN, STRING |
| **isTaxable**  BOOLEAN, STRING |
| **isWip**  BOOLEAN, STRING |
| **item**  VARIES |
| **itemCostDiscAmount**  STRING, NUMBER |
| **itemCostDiscPrint**  BOOLEAN, STRING |
| **itemCostDiscRate**  STRING |
| **itemCostDiscTax1Amt**  STRING, NUMBER |
| **itemCostDiscTaxable**  BOOLEAN, STRING |
| **itemCostDiscount**  VARIES |
| **itemCostList**  VARIES |
| **itemCostTaxCode**  VARIES |
| **itemCostTaxRate1**  STRING, NUMBER |
| **itemCostTaxRate2**  STRING, NUMBER |
| **itemFulfillment**  VARIES |
| **itemList**  VARIES |
| **job**  VARIES |
| **landedCostMethod**  VARIES |
| **landedCostPerLine**  BOOLEAN, STRING |
| **landedCostsList**  VARIES |
| **lastModifiedDate**  STRING |
| **leadSource**  VARIES |
| **licenseDateUps**  STRING |
| **licenseExceptionUps**  VARIES |
| **licenseNumberUps**  STRING |
| **lineList**  VARIES |
| **linkedTrackingNumbers**  STRING |
| **location**  VARIES |
| **manufacturingRouting**  VARIES |
| **memo**  STRING |
| **message**  STRING |
| **messageSel**  VARIES |
| **methodOfTransportUps**  VARIES |
| **nextApprover**  VARIES |
| **nextBill**  STRING |
| **nexus**  VARIES |
| **nullFieldList**  VARIES |
| **onCreditHold**  STRING |
| **oneTime**  STRING, NUMBER |
| **operationList**  VARIES |
| **opportunity**  VARIES |
| **options**  VARIES |
| **orderQuantity**  STRING, NUMBER |
| **orderStatus**  VARIES |
| **otherList**  VARIES |
| **otherRefNum**  STRING |
| **outputAuthCode**  STRING |
| **outputReferenceCode**  STRING |
| **overrideInstallments**  BOOLEAN, STRING |
| **packageFedExList**  VARIES |
| **packageList**  VARIES |
| **packageUpsList**  VARIES |
| **packageUspsList**  VARIES |
| **packedDate**  STRING |
| **parentExpenseAlloc**  VARIES |
| **partiesToTransactionUps**  BOOLEAN, STRING |
| **partner**  VARIES |
| **partnersList**  VARIES |
| **payPalAuthId**  STRING |
| **payPalProcess**  BOOLEAN, STRING |
| **payPalStatus**  STRING |
| **payPalTranId**  STRING |
| **payeeAddress**  VARIES |
| **payeeAddressList**  VARIES |
| **payment**  STRING, NUMBER |
| **paymentCardCsc**  STRING |
| **paymentEventDate**  STRING |
| **paymentEventHoldReason**  VARIES |
| **paymentEventResult**  VARIES |
| **paymentEventType**  VARIES |
| **paymentEventUpdatedBy**  STRING |
| **paymentHold**  BOOLEAN, STRING |
| **paymentList**  VARIES |
| **paymentMethod**  VARIES |
| **paymentOperation**  VARIES |
| **paymentOption**  STRING |
| **paymentProcessingProfile**  VARIES |
| **paypalAuthId**  STRING |
| **paypalProcess**  BOOLEAN, STRING |
| **pending**  STRING, NUMBER |
| **pickedDate**  STRING |
| **pnRefNum**  STRING |
| **policyViolated**  BOOLEAN, STRING |
| **postingPeriod**  VARIES |
| **printVoucher**  BOOLEAN, STRING |
| **probability**  STRING, NUMBER |
| **promoCode**  VARIES |
| **promotionsList**  VARIES |
| **purchaseContract**  VARIES |
| **purchaseOrderList**  VARIES |
| **quantity**  STRING, NUMBER |
| **recipientTaxIdUps**  STRING |
| **recognizedRevenue**  STRING, NUMBER |
| **recurAnnually**  STRING, NUMBER |
| **recurMonthly**  STRING, NUMBER |
| **recurQuarterly**  STRING, NUMBER |
| **recurWeekly**  STRING, NUMBER |
| **recurringBill**  BOOLEAN, STRING |
| **refundCheck**  BOOLEAN, STRING |
| **requestedBy**  VARIES |
| **requestedDate**  STRING |
| **revCommitStatus**  VARIES |
| **revRecEndDate**  STRING |
| **revRecOnRevCommitment**  BOOLEAN, STRING |
| **revRecSchedule**  VARIES |
| **revRecStartDate**  STRING |
| **revenueStatus**  VARIES |
| **reversalDate**  STRING |
| **reversalDefer**  BOOLEAN, STRING |
| **reversalEntry**  STRING |
| **revision**  VARIES |
| **salesEffectiveDate**  STRING |
| **salesGroup**  VARIES |
| **salesOrder**  VARIES |
| **salesOrderRequiredDepositDue**  STRING, NUMBER |
| **salesRep**  VARIES |
| **salesTeamList**  VARIES |
| **saturdayDeliveryFedEx**  BOOLEAN, STRING |
| **saturdayDeliveryUps**  BOOLEAN, STRING |
| **saturdayPickupFedex**  BOOLEAN, STRING |
| **saveOnAuthDecline**  BOOLEAN, STRING |
| **schedulingMethod**  VARIES |
| **scrapQuantity**  STRING, NUMBER |
| **sendBackupEmailFedEx**  BOOLEAN, STRING |
| **sendBackupEmailUps**  BOOLEAN, STRING |
| **sendShipNotifyEmailFedEx**  BOOLEAN, STRING |
| **sendShipNotifyEmailUps**  BOOLEAN, STRING |
| **serialNumbers**  STRING |
| **shipAddress**  STRING |
| **shipAddressList**  VARIES |
| **shipComplete**  BOOLEAN, STRING |
| **shipDate**  STRING |
| **shipDateFedEx**  STRING |
| **shipGroupList**  VARIES |
| **shipIsResidential**  BOOLEAN, STRING |
| **shipMethod**  VARIES |
| **shipNotifyEmailAddress2Ups**  STRING |
| **shipNotifyEmailAddressFedEx**  STRING |
| **shipNotifyEmailAddressUps**  STRING |
| **shipNotifyEmailMessageUps**  STRING |
| **shipStatus**  VARIES |
| **shipTo**  VARIES |
| **shipmentWeightFedEx**  STRING, NUMBER |
| **shipmentWeightUps**  STRING, NUMBER |
| **shippedDate**  STRING |
| **shippingAddress**  VARIES |
| **shippingCost**  STRING, NUMBER |
| **shippingTax1Rate**  STRING, NUMBER |
| **shippingTax2Rate**  STRING, NUMBER |
| **shippingTaxCode**  VARIES |
| **shopperIpAddress**  STRING |
| **signatureHomeDeliveryFedEx**  BOOLEAN, STRING |
| **softDescriptor**  STRING |
| **source**  STRING |
| **sourceTransactionId**  STRING |
| **sourceTransactionLine**  STRING, INTEGER |
| **specialOrder**  BOOLEAN, STRING |
| **startDate**  STRING |
| **startOperation**  VARIES |
| **status**  STRING |
| **subTotal**  STRING, NUMBER |
| **subsidiary**  VARIES |
| **subsidiaryTaxRegNum**  VARIES |
| **supervisorApproval**  BOOLEAN, STRING |
| **syncPartnerTeams**  BOOLEAN, STRING |
| **syncSalesTeams**  BOOLEAN, STRING |
| **tax1Amt**  STRING, NUMBER |
| **tax2Amt**  STRING, NUMBER |
| **tax2Total**  STRING, NUMBER |
| **taxDetailsList**  VARIES |
| **taxDetailsOverride**  BOOLEAN, STRING |
| **taxItem**  VARIES |
| **taxPointDate**  STRING |
| **taxRate**  STRING, NUMBER |
| **taxRegOverride**  BOOLEAN, STRING |
| **taxTotal**  STRING, NUMBER |
| **terms**  VARIES |
| **termsFreightChargeFedEx**  STRING, NUMBER |
| **termsInsuranceChargeFedEx**  STRING, NUMBER |
| **termsOfSaleFedEx**  VARIES |
| **thirdPartyAcctFedEx**  STRING |
| **thirdPartyAcctUps**  STRING |
| **thirdPartyCountryFedEx**  VARIES |
| **thirdPartyCountryUps**  VARIES |
| **thirdPartyTypeFedEx**  VARIES |
| **thirdPartyTypeUps**  VARIES |
| **thirdPartyZipcodeUps**  STRING |
| **threeDStatusCode**  STRING |
| **timeDiscAmount**  STRING, NUMBER |
| **timeDiscPrint**  BOOLEAN, STRING |
| **timeDiscRate**  STRING |
| **timeDiscTax1Amt**  STRING, NUMBER |
| **timeDiscTaxable**  BOOLEAN, STRING |
| **timeDiscount**  VARIES |
| **timeList**  VARIES |
| **timeTaxCode**  VARIES |
| **timeTaxRate1**  STRING, NUMBER |
| **timeTaxRate2**  STRING, NUMBER |
| **title**  STRING |
| **toAch**  BOOLEAN, STRING |
| **toBeEmailed**  BOOLEAN, STRING |
| **toBeFaxed**  BOOLEAN, STRING |
| **toBePrinted**  BOOLEAN, STRING |
| **toPrint2**  BOOLEAN, STRING |
| **toSubsidiary**  VARIES |
| **total**  STRING, NUMBER |
| **totalCostEstimate**  STRING, NUMBER |
| **trackingNumbers**  STRING |
| **tranDate**  STRING |
| **tranId**  STRING |
| **tranIsVsoeBundle**  BOOLEAN, STRING |
| **tranStatus**  STRING |
| **tranType**  STRING |
| **transactionNumber**  STRING |
| **transferLocation**  VARIES |
| **unApplied**  STRING, NUMBER |
| **unapplied**  STRING, NUMBER |
| **undepFunds**  BOOLEAN, STRING |
| **unitCost**  STRING, NUMBER |
| **units**  VARIES |
| **unitsType**  VARIES |
| **useItemCostAsTransferCost**  BOOLEAN, STRING |
| **useMultiCurrency**  BOOLEAN, STRING |
| **userTaxTotal**  STRING, NUMBER |
| **userTotal**  STRING, NUMBER |
| **validFrom**  STRING |
| **vatRegNum**  STRING |
| **visibleToCustomer**  BOOLEAN, STRING |
| **voidJournal**  VARIES |
| **vsoeAutoCalc**  BOOLEAN, STRING |

### UnitsType

The `UnitsType` table contains info about the unit types, or Units of Measure, in your NetSuite account.

#### UnitsType table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/UnitsType.html) |

UnitsType table schema

|  |
| --- |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
| **uomList**  VARIES |

### Usage

The `Usage` table contains info about the subscription billing lines in your NetSuite account. For example: Money, time, cellular data, internet data, etc.

#### Usage table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Usage.html) |

Usage table schema

|  |
| --- |
| **customForm**  VARIES |
| **customer**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **item**  VARIES |
| **memo**  STRING |
| **nullFieldList**  VARIES |
| **status**  STRING |
| **subscriptionPlan**  VARIES |
| **usageDate**  STRING |
| **usageQuantity**  STRING, NUMBER |
| **usageSubscription**  VARIES |
| **usageSubscriptionLine**  VARIES |

### Vendor

The `Vendor` table contains info about the vendors in your NetSuite account.

#### Vendor table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | internalId |
| **Replication Key** | lastModifiedDate |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Vendor.html) |

Vendor table schema

|  |
| --- |
| **accountNumber**  STRING |
| **addressbookList**  VARIES |
| **altEmail**  STRING |
| **altName**  STRING |
| **altPhone**  STRING |
| **balance**  STRING, NUMBER |
| **balancePrimary**  STRING, NUMBER |
| **bcn**  STRING |
| **billPay**  BOOLEAN, STRING |
| **category**  VARIES |
| **comments**  STRING |
| **companyName**  STRING |
| **creditLimit**  STRING, NUMBER |
| **currency**  VARIES |
| **currencyList**  VARIES |
| **customFieldList**  VARIES |
| **customForm**  VARIES |
| **dateCreated**  STRING |
| **defaultAddress**  STRING |
| **defaultTaxReg**  STRING |
| **eligibleForCommission**  BOOLEAN, STRING |
| **email**  STRING |
| **emailPreference**  VARIES |
| **emailTransactions**  BOOLEAN, STRING |
| **entityId**  STRING |
| **expenseAccount**  VARIES |
| **externalId**  STRING |
| **fax**  STRING |
| **faxTransactions**  BOOLEAN, STRING |
| **firstName**  STRING |
| **giveAccess**  BOOLEAN, STRING |
| **globalSubscriptionStatus**  VARIES |
| **homePhone**  STRING |
| **image**  VARIES |
| **incoterm**  VARIES |
| **internalId**  STRING |
| **is1099Eligible**  BOOLEAN, STRING |
| **isAccountant**  BOOLEAN, STRING |
| **isInactive**  BOOLEAN, STRING |
| **isJobResourceVend**  BOOLEAN, STRING |
| **isPerson**  BOOLEAN, STRING |
| **laborCost**  STRING, NUMBER |
| **lastModifiedDate**  STRING |
| **lastName**  STRING |
| **legalName**  STRING |
| **middleName**  STRING |
| **mobilePhone**  STRING |
| **nullFieldList**  VARIES |
| **openingBalance**  STRING, NUMBER |
| **openingBalanceAccount**  VARIES |
| **openingBalanceDate**  STRING |
| **password**  STRING |
| **password2**  STRING |
| **payablesAccount**  VARIES |
| **phone**  STRING |
| **phoneticName**  STRING |
| **predConfidence**  STRING, NUMBER |
| **predictedDays**  STRING, INTEGER |
| **pricingScheduleList**  VARIES |
| **printOnCheckAs**  STRING |
| **printTransactions**  BOOLEAN, STRING |
| **purchaseOrderAmount**  STRING, NUMBER |
| **purchaseOrderQuantity**  STRING, NUMBER |
| **purchaseOrderQuantityDiff**  STRING, NUMBER |
| **receiptAmount**  STRING, NUMBER |
| **receiptQuantity**  STRING, NUMBER |
| **receiptQuantityDiff**  STRING, NUMBER |
| **representingSubsidiary**  VARIES |
| **requirePwdChange**  BOOLEAN, STRING |
| **rolesList**  VARIES |
| **salutation**  STRING |
| **sendEmail**  BOOLEAN, STRING |
| **subscriptionsList**  VARIES |
| **subsidiary**  VARIES |
| **taxIdNum**  STRING |
| **taxItem**  VARIES |
| **taxRegistrationList**  STRING |
| **terms**  VARIES |
| **title**  STRING |
| **unbilledOrders**  STRING, NUMBER |
| **unbilledOrdersPrimary**  STRING, NUMBER |
| **url**  STRING |
| **vatRegNumber**  STRING |
| **workCalendar**  VARIES |

### VendorCategory

The `VendorCategory` table contains info about the categories that can be applied to vendors in your NetSuite account.

#### VendorCategory table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/VendorCategory.html) |

VendorCategory table schema

|  |
| --- |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **isTaxAgency**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |

### VendorSubsidiaryRelationship

The `VendorSubsidiaryRelationship` table contains info about vendors shared with multiple subsidiaries.

#### VendorSubsidiaryRelationship table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/VendorSubsidiaryRelationship.html) |

VendorSubsidiaryRelationship table schema

|  |
| --- |
| **baseCurrency**  VARIES |
| **creditLimit**  STRING, NUMBER |
| **customFieldList**  VARIES |
| **entity**  VARIES |
| **externalId**  STRING |
| **internalId**  STRING |
| **isPrimarySub**  BOOLEAN, STRING |
| **nullFieldList**  VARIES |
| **primaryCurrency**  VARIES |
| **subsidiary**  VARIES |
| **taxItem**  VARIES |

### WinLossReason

The `WinLossReason` table contains info about the win/loss reasons in your NetSuite account.

#### WinLossReason table replication requirements

Replicating this table requires the `View` permission in NetSuite.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | internalId |
| **Useful links** | [NetSuite documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/WinLossReason.html) |

WinLossReason table schema

|  |
| --- |
| **externalId**  STRING |
| **internalId**  STRING |
| **isInactive**  BOOLEAN, STRING |
| **name**  STRING |
| **nullFieldList**  VARIES |
