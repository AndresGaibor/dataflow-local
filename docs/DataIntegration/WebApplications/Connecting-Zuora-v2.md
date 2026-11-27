---
title: "Zuora"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Zuora-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Zuora

Zuora is a software for subscription revenue management automation. You can connect to Zuora to land data as a data source when landing or replicating data with Data Gateway - Data Movement.

For more information about the API, see [REST API](https://www.zuora.com/developer/api-reference/) and [AQuA API](https://knowledgecenter.zuora.com/DC_Developers/AB_Aggregate_Query_API/AA_AQuA_API_Introduction).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up Zuora, you need a Zuora user. Creating a-specific user ensures that Qlik is distinguishable in any logs or audits

To replicate your Zuora data, you need:

- Standard user permissions. While Qlik will only ever read your data, these permissions are required to access certain objects in Zuora.
- Two-factor authentication disabled. If this is enabled, connection and replication issues will occur after setup. See the Disable or Reset Two-Factor Authentication sections [in Zuora documentation](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Two-Factor_Authentication).
- Credentials that don’t expire. This is applicable only if your company enforces password expiration rules. If Zuora credentials expire, connection issues may arise. [See this Zuora support article for a workaround](https://knowledgecenter.zuora.com/kb/How_do_I_prevent_my_API_user_login_from_expiring%3F).

1. Log into your Zuora account as the tenant administrator.
2. Click your username in the top-right corner > Administration > Manage User Roles.
3. Click Add new role.
4. Enter a first and last name for the user.
5. Enter an email address in the Work Email and Login Field fields.
6. In the Zuora Platform Role field, select Standard User.
7. For the remaining Role fields, select the Standard User option.
8. Leave Locale and Language fields as default .
9. Click Save to create the user.

After the user is created, Zuora sends a verification email to the email address in the Work Email field. Complete the verification and set a password for the user before moving on to the next step.

### Selecting a Zuora extraction API

Zuora integration gives you the ability to select the API that you want to use to extract data. If you are not sure which API you should use, take a look at the brief comparison below.

This setting can be changed at any time, but will only affect extractions that take place after the change.

Once you have decided, click the radio button next to the API you want to use.

Information note
When using the AQuA API, you will need to enter a partner ID in the Zuora Partner ID field. If you do not already have this credential, reach out to [Zuora Global Support](http://support.zuora.com/) before proceeding.

|  |  |  |
| --- | --- | --- |
|  | REST API | AQuA API |
| Good for replicating | Small datasets, more frequently | Large datasets, less frequently |
| Deleted records | Unsupported | Supported.  An additional column (deleted) will be added to objects that support deletions, which indicates the record’s deletion status.  Deleted data extraction is unsupported by the AQuA API for the following objects:   - accountingPeriod - contactSnapshot - discountAppliedMetrics - paymentGaterwayReconciliationEventLog - paymentTransactionLog - paymentMethodTransactionLog - paymentReconciliationJob - paymentReconciliationLog - processedUsage - refundTransactionLog - updaterBatch - updaterDetail   See [Zuora’s documentation](https://knowledgecenter.zuora.com/Zuora_Platform/Integration/API/AB_Aggregate_Query_API/B_Submit_Query/a_Export_Deleted_Data) for more info. |
| Requires additional Zuora credentials | Not required | Required.  Using the AQuA API requires a Partner ID - to obtain one, reach out to [Zuora Global Support](https://zuora.zendesk.com/). |

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
| Zuora username | Zuora username. |
| Zuora password | Zuora password. |
| Connect to a sandbox environment | If the Zuora instance to whiçh you want to connect is a sandbox, select the checkbox. |
| Connect to a European endpoint | If the Zuora instance to which you want to connect is based in Europe, select the check box. If you are not sure if this is applicable to you, [refer to Zuora’s documentation](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Zuora_Data_Centers). |
| API Type | Select the type from the drop-down list. The AQuA API is Zuora's API. It supports retrieving deleted data and exporting data in segments, which is useful for large amounts of data.  The REST API is recommended for smaller datasets and when deleted data is not important. |
| Zuora Partner ID | Zuora partner ID. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

### Zuora object relationships

To get a better understanding of how Zuora objects relate to each other, check out [Zuora’s Entity Relationship Diagram](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Business_Objects_Relationship).

Understanding the relationships between different datasets lets you perform more in-depth and complex analyses.

Depending on your destination, table and column names may not appear as they are outlined below.

### Account

The `Account` table contains information about the customer accounts in your Zuora instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Accounts/) |

Account table foreign keys

| Join Account with | on |
| --- | --- |
| [ContactSnapshot](#contactsnapshot) | ``` Account.id = ContactSnapshot.accountId ```  ``` Account.billToContactId = ContactSnapshot.contactId ```  ``` Account.soldToContactId = ContactSnapshot.contactId ``` |
| [Invoice](#invoice) | ``` Account.id = Invoice.accountId ```  ``` Account.billToContactId = Invoice.billToContactId ```  ``` Account.soldToContactId = Invoice.billToContactId ```  ``` Account.billToContactId = Invoice.soldToContactId ```  ``` Account.soldToContactId = Invoice.soldToContactId ```  ``` Account.defaultPaymentMethodId = Invoice.defaultPaymentMethodId ```  ``` Account.parentAccountId = Invoice.parentAccountId ``` |
| [Payment](#payment) | ``` Account.id = Payment.accountId ``` |
| [Refund](#refund) | ``` Account.id = Refund.accountId ```  ``` Account.billToContactId = Refund.billToContactId ```  ``` Account.soldToContactId = Refund.billToContactId ```  ``` Account.billToContactId = Refund.soldToContactId ```  ``` Account.soldToContactId = Refund.soldToContactId ```  ``` Account.parentAccountId = Refund.parentAccountId ``` |
| [Subscription](#subscription) | ``` Account.id = Subscription.accountId ``` |
| [Contact](#contact) | ``` Account.billToContactId = Contact.id ```  ``` Account.soldToContactId = Contact.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` Account.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` Account.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` Account.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` Account.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` Account.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` Account.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` Account.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` Account.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` Account.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` Account.parentAccountId = DiscountAppliedMetrics.parentAccountId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` Account.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` Account.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` Account.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` Account.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` Account.parentAccountId = InvoiceItemAdjustment.parentAccountId ``` |
| [ProcessedUsage](#processedusage) | ``` Account.billToContactId = ProcessedUsage.billToContactId ```  ``` Account.soldToContactId = ProcessedUsage.billToContactId ```  ``` Account.billToContactId = ProcessedUsage.soldToContactId ```  ``` Account.soldToContactId = ProcessedUsage.soldToContactId ```  ``` Account.parentAccountId = ProcessedUsage.parentAccountId ``` |
| [RatePlan](#rateplan) | ``` Account.billToContactId = RatePlan.billToContactId ```  ``` Account.soldToContactId = RatePlan.billToContactId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` Account.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` Account.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` Account.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` Account.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` Account.parentAccountId = RevenueChargeSummaryItem.parentAccountId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` Account.billToContactId = RevenueEventItem.billToContactId ```  ``` Account.soldToContactId = RevenueEventItem.billToContactId ```  ``` Account.billToContactId = RevenueEventItem.soldToContactId ```  ``` Account.soldToContactId = RevenueEventItem.soldToContactId ```  ``` Account.id = RevenueEventItem.deferredRevenueAccountingCodeId ```  ``` Account.parentAccountId = RevenueEventItem.parentAccountId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` Account.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` Account.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` Account.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` Account.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` Account.id = RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` Account.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` Account.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` Account.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` Account.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` Account.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` Account.id = RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` Account.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` Account.billToContactId = RevenueScheduleItem.billToContactId ```  ``` Account.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` Account.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` Account.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` Account.id = RevenueScheduleItem.deferredRevenueAccountingCodeId ```  ``` Account.parentAccountId = RevenueScheduleItem.parentAccountId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` Account.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` Account.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` Account.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` Account.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` Account.id = RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` Account.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` Account.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` Account.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` Account.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` Account.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` Account.id = RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` Account.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ``` |
| [CommunicationProfile](#communicationprofile) | ``` Account.communicationProfileId = CommunicationProfile.id ``` |
| [PaymentMethod](#paymentmethod) | ``` Account.defaultPaymentMethodId = PaymentMethod.id ``` |

Account table schema

|  |
| --- |
| **accountNumber**  STRING |
| **additionalEmailAddresses**  STRING |
| **allowInvoiceEdit**  BOOLEAN |
| **autoPay**  BOOLEAN |
| **balance**  DECIMAL |
| **batch**  STRING |
| **bcdSettingOption**  STRING |
| **billCycleDay**  INTEGER |
| **billToContactId**  STRING |
| **communicationProfileId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **creditBalance**  DECIMAL |
| **crmId**  STRING |
| **currency**  STRING |
| **customerServiceRepName**  STRING |
| **defaultPaymentMethodId**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **invoiceDeliveryPrefsEmail**  BOOLEAN |
| **invoiceDeliveryPrefsPrint**  BOOLEAN |
| **invoiceTemplateId**  STRING |
| **lastInvoiceDate**  DATE-TIME |
| **name**  STRING |
| **notes**  STRING |
| **parentAccountId**  STRING |
| **paymentGateway**  STRING |
| **paymentTerm**  STRING |
| **purchaseOrderNumber**  STRING |
| **salesRepName**  STRING |
| **soldToContactId**  STRING |
| **status**  STRING |
| **taxExemptCertificateId**  STRING |
| **taxExemptCertificateType**  STRING |
| **taxExemptDescription**  STRING |
| **taxExemptEffectiveDate**  DATE-TIME |
| **taxExemptExpirationDate**  DATE-TIME |
| **taxExemptIssuingJurisdiction**  STRING |
| **taxExemptStatus**  STRING |
| **totalInvoiceBalance**  DECIMAL |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### AccountingCode

The `AccountingCode` table contains information about the accounting codes in your Zuora instance. Accounting codes are used to categorize transactions for accounting purposes.

**Note**: To replicate this table, you must have Zuora Finance enabled.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/operation/GET_AllAccountingCodes/) |

AccountingCode table foreign keys

| Join AccountingCode with | on |
| --- | --- |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` AccountingCode.id = CreditBalanceAdjustment.accountingCode ```  ``` AccountingCode.id = CreditBalanceAdjustment.accountReceivableAccountingCodeId ```  ``` AccountingCode.id = CreditBalanceAdjustment.cashOnAccountAccountingCodeId ``` |
| [InvoiceItem](#invoiceitem) | ``` AccountingCode.id = InvoiceItem.accountingCode ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` AccountingCode.id = InvoiceItemAdjustment.accountingCode ```  ``` AccountingCode.id = InvoiceItemAdjustment.accountReceivableAccountingCodeId ```  ``` AccountingCode.id = InvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` AccountingCode.id = InvoiceItemAdjustment.salesTaxPayableAccountingCodeId ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` AccountingCode.id = ProductRatePlanCharge.accountingCode ``` |
| [RevenueEventItem](#revenueeventitem) | ``` AccountingCode.id = RevenueEventItem.recognizedRevenueAccountingCodeId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` AccountingCode.id = RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` AccountingCode.id = RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` AccountingCode.id = RevenueScheduleItem.recognizedRevenueAccountingCodeId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` AccountingCode.id = RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` AccountingCode.id = RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ``` |

AccountingCode table schema

|  |
| --- |
| **category**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **glAccountName**  STRING |
| **glAccountNumber**  STRING |
| **id**  STRING |
| **name**  STRING |
| **notes**  STRING |
| **status**  STRING |
| **type**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### AccountingPeriod

The `AccountingPeriod` table contains information about the [accounting periods](https://knowledgecenter.zuora.com/CC_Finance/E_Accounting_Periods) in your Zuora account.

**Note**: To replicate this table, you must have Zuora Finance enabled.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Accounting-Periods/) |

AccountingPeriod table foreign keys

| Join AccountingPeriod with | on |
| --- | --- |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` AccountingPeriod.id = CreditBalanceAdjustment.accountingPeriodId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` AccountingPeriod.id = InvoiceItemAdjustment.accountingPeriodId ``` |
| [JournalEntry](#journalentry) | ``` AccountingPeriod.id = JournalEntry.accountingPeriodId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` AccountingPeriod.id = RevenueChargeSummaryItem.accountingPeriodId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` AccountingPeriod.id = RevenueEventItemInvoiceItem.accountingPeriodId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` AccountingPeriod.id = RevenueEventItemInvoiceItemAdjustment.accountingPeriodId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` AccountingPeriod.id = RevenueScheduleItem.accountingPeriodId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` AccountingPeriod.id = RevenueScheduleItemInvoiceItem.accountingPeriodId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` AccountingPeriod.id = RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId ``` |

AccountingPeriod table schema

|  |
| --- |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **endDate**  DATE-TIME |
| **fiscalQuarter**  STRING |
| **fiscalYear**  STRING |
| **id**  STRING |
| **name**  STRING |
| **notes**  STRING |
| **runTrialBalanceEnd**  DATE-TIME |
| **runTrialBalanceErrorMessage**  STRING |
| **runTrialBalanceStart**  DATE-TIME |
| **runTrialBalanceStatus**  STRING |
| **startDate**  DATE-TIME |
| **status**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### Amendment

The `Amendment` table contains information about subscription amendments, which are changes to customer subscriptions. For example: Changing the terms of a contract, adding/removing a product, canceling a subscription, etc.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/older-api/operation/Object_GETAmendment/) |

Amendment table foreign keys

| Join Amendment with | on |
| --- | --- |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` Amendment.id = DiscountAppliedMetrics.amendmentId ```  ``` Amendment.subscriptionId = DiscountAppliedMetrics.subscriptionId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` Amendment.id = InvoiceItemAdjustment.amendmentId ```  ``` Amendment.subscriptionId = InvoiceItemAdjustment.subscriptionId ``` |
| [ProcessedUsage](#processedusage) | ``` Amendment.id = ProcessedUsage.amendmentId ``` |
| [RatePlan](#rateplan) | ``` Amendment.id = RatePlan.amendmentId ```  ``` Amendment.subscriptionId = RatePlan.subscriptionId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` Amendment.id = RatePlanChargeTier.amendmentId ```  ``` Amendment.subscriptionId = RatePlanChargeTier.subscriptionId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` Amendment.id = RevenueChargeSummaryItem.amendmentId ```  ``` Amendment.subscriptionId = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` Amendment.id = RevenueEventItem.amendmentId ```  ``` Amendment.subscriptionId = RevenueEventItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` Amendment.id = RevenueEventItemInvoiceItem.amendmentId ```  ``` Amendment.subscriptionId = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` Amendment.id = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` Amendment.subscriptionId = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` Amendment.id = RevenueScheduleItem.amendmentId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` Amendment.id = RevenueScheduleItemInvoiceItem.amendmentId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` Amendment.id = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` Amendment.subscriptionId = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |
| [Subscription](#subscription) | ``` Amendment.subscriptionId = Subscription.id ``` |
| [InvoiceItem](#invoiceitem) | ``` Amendment.subscriptionId = InvoiceItem.subscriptionId ``` |

Amendment table schema

|  |
| --- |
| **autoRenew**  BOOLEAN |
| **code**  STRING |
| **contractEffectiveDate**  DATE-TIME |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **currentTerm**  INTEGER |
| **currentTermPeriodType**  STRING |
| **customerAcceptanceDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **effectiveDate**  DATE-TIME |
| **id**  STRING |
| **name**  STRING |
| **renewalSetting**  STRING |
| **renewalTerm**  STRING |
| **renewalTermPeriodType**  STRING |
| **serviceActivationDate**  DATE-TIME |
| **specificUpdateDate**  DATE-TIME |
| **status**  STRING |
| **subscriptionId**  STRING |
| **termStartDate**  STRING |
| **type**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### BillingRun

The `BillingRun` table contains information about billing runs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Bill-Run/) |

BillingRun table foreign keys

| Join BillingRun with | on |
| --- | --- |
| [PaymentRun](#paymentrun) | ``` BillingRun.id = PaymentRun.billingRunId ``` |

BillingRun table schema

|  |
| --- |
| **autoEmail**  BOOLEAN |
| **autoPost**  BOOLEAN |
| **autoRenewal**  BOOLEAN |
| **batch**  STRING |
| **billCycleDay**  STRING |
| **billRunNumber**  STRING |
| **chargeTypeToExclude**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **errorMessage**  STRING |
| **executedDate**  DATE-TIME |
| **id**  STRING |
| **invoiceDate**  DATE-TIME |
| **invoicesEmailed**  BOOLEAN |
| **lastEmailSentTime**  DATE-TIME |
| **noEmailForZeroAmountInvoice**  BOOLEAN |
| **numberOfAccounts**  INTEGER |
| **numberOfInvoices**  INTEGER |
| **status**  STRING |
| **targetDate**  DATE-TIME |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### CommunicationProfile

The `CommunicationProfile` table contains information about communication profiles, which are sets of policies that determine how to communicate with the contacts associated with a specific customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://knowledgecenter.zuora.com/Zuora_Platform/System_Management/Settings_API/Settings_API_tutorials/Get_a_Communication_Profile) |

CommunicationProfile table foreign keys

| Join CommunicationProfile with | on |
| --- | --- |
| [Account](#account) | ``` CommunicationProfile.id = Account.communicationProfileId ``` |

CommunicationProfile table schema

|  |
| --- |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **id**  STRING |
| **profileName**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### Contact

The `Contact` table contains info about an account’s point-of-contact.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Contacts/) |

Contact table foreign keys

| Join Contact with | on |
| --- | --- |
| [Account](#account) | ``` Contact.id = Account.billToContactId ```  ``` Contact.id = Account.soldToContactId ``` |
| [ContactSnapshot](#contactsnapshot) | ``` Contact.id = ContactSnapshot.contactId ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` Contact.id = CreditBalanceAdjustment.billToContactId ```  ``` Contact.id = CreditBalanceAdjustment.soldToContactId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` Contact.id = DiscountAppliedMetrics.billToContactId ```  ``` Contact.id = DiscountAppliedMetrics.soldToContactId ``` |
| [Invoice](#invoice) | ``` Contact.id = Invoice.billToContactId ```  ``` Contact.id = Invoice.soldToContactId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` Contact.id = InvoiceItemAdjustment.billToContactId ```  ``` Contact.id = InvoiceItemAdjustment.soldToContactId ``` |
| [ProcessedUsage](#processedusage) | ``` Contact.id = ProcessedUsage.billToContactId ```  ``` Contact.id = ProcessedUsage.soldToContactId ``` |
| [RatePlan](#rateplan) | ``` Contact.id = RatePlan.billToContactId ``` |
| [Refund](#refund) | ``` Contact.id = Refund.billToContactId ```  ``` Contact.id = Refund.soldToContactId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` Contact.id = RevenueChargeSummaryItem.billToContactId ```  ``` Contact.id = RevenueChargeSummaryItem.soldToContactId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` Contact.id = RevenueEventItem.billToContactId ```  ``` Contact.id = RevenueEventItem.soldToContactId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` Contact.id = RevenueEventItemInvoiceItem.billToContactId ```  ``` Contact.id = RevenueEventItemInvoiceItem.soldToContactId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` Contact.id = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` Contact.id = RevenueEventItemInvoiceItemAdjustment.soldToContactId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` Contact.id = RevenueScheduleItem.billToContactId ```  ``` Contact.id = RevenueScheduleItem.soldToContactId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` Contact.id = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` Contact.id = RevenueScheduleItemInvoiceItem.soldToContactId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` Contact.id = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` Contact.id = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ``` |

Contact table schema

|  |
| --- |
| **accountId**  STRING |
| **address1**  STRING |
| **address2**  STRING |
| **city**  STRING |
| **country**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **fax**  STRING |
| **firstName**  STRING |
| **homePhone**  STRING |
| **id**  STRING |
| **lastName**  STRING |
| **mobilePhone**  STRING |
| **nickName**  STRING |
| **otherPhone**  STRING |
| **otherPhoneType**  STRING |
| **personalEmail**  STRING |
| **postalCode**  STRING |
| **state**  STRING |
| **taxRegion**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |
| **workEmail**  STRING |
| **workPhone**  STRING |

### ContactSnapshot

The `ContactSnapshot` table contains ‘snapshot’ records of Bill-To or Sold-To contacts on customer accounts. Snapshots are record preservations at specific points in time. When invoices are posted, Zuora will preserve the data for the Bill-To and Sold-To contacts at that point in time.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Contacts/) |

ContactSnapshot table foreign keys

| Join ContactSnapshot with | on |
| --- | --- |
| [Account](#account) | ``` ContactSnapshot.accountId = Account.id ```  ``` ContactSnapshot.contactId = Account.billToContactId ```  ``` ContactSnapshot.contactId = Account.soldToContactId ``` |
| [Invoice](#invoice) | ``` ContactSnapshot.accountId = Invoice.accountId ```  ``` ContactSnapshot.contactId = Invoice.billToContactId ```  ``` ContactSnapshot.contactId = Invoice.billToContactSnapshotId ```  ``` ContactSnapshot.contactId = Invoice.soldToContactId ```  ``` ContactSnapshot.contactId = Invoice.soldToContactSnapshotId ``` |
| [Payment](#payment) | ``` ContactSnapshot.accountId = Payment.accountId ``` |
| [Refund](#refund) | ``` ContactSnapshot.accountId = Refund.accountId ```  ``` ContactSnapshot.contactId = Refund.billToContactId ```  ``` ContactSnapshot.contactId = Refund.soldToContactId ``` |
| [Subscription](#subscription) | ``` ContactSnapshot.accountId = Subscription.accountId ``` |
| [Contact](#contact) | ``` ContactSnapshot.contactId = Contact.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` ContactSnapshot.contactId = CreditBalanceAdjustment.billToContactId ```  ``` ContactSnapshot.contactId = CreditBalanceAdjustment.soldToContactId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` ContactSnapshot.contactId = DiscountAppliedMetrics.billToContactId ```  ``` ContactSnapshot.contactId = DiscountAppliedMetrics.soldToContactId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` ContactSnapshot.contactId = InvoiceItemAdjustment.billToContactId ```  ``` ContactSnapshot.contactId = InvoiceItemAdjustment.soldToContactId ``` |
| [ProcessedUsage](#processedusage) | ``` ContactSnapshot.contactId = ProcessedUsage.billToContactId ```  ``` ContactSnapshot.contactId = ProcessedUsage.soldToContactId ``` |
| [RatePlan](#rateplan) | ``` ContactSnapshot.contactId = RatePlan.billToContactId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` ContactSnapshot.contactId = RevenueChargeSummaryItem.billToContactId ```  ``` ContactSnapshot.contactId = RevenueChargeSummaryItem.soldToContactId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` ContactSnapshot.contactId = RevenueEventItem.billToContactId ```  ``` ContactSnapshot.contactId = RevenueEventItem.soldToContactId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` ContactSnapshot.contactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` ContactSnapshot.contactId = RevenueEventItemInvoiceItem.soldToContactId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` ContactSnapshot.contactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` ContactSnapshot.contactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` ContactSnapshot.contactId = RevenueScheduleItem.billToContactId ```  ``` ContactSnapshot.contactId = RevenueScheduleItem.soldToContactId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` ContactSnapshot.contactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` ContactSnapshot.contactId = RevenueScheduleItemInvoiceItem.soldToContactId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` ContactSnapshot.contactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` ContactSnapshot.contactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ``` |

ContactSnapshot table schema

|  |
| --- |
| **accountId**  STRING |
| **address1**  STRING |
| **address2**  STRING |
| **city**  STRING |
| **contactId**  STRING |
| **country**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **description**  STRING |
| **fax**  STRING |
| **firstName**  STRING |
| **homePhone**  STRING |
| **id**  STRING |
| **lastName**  STRING |
| **mobilePhone**  STRING |
| **nickName**  STRING |
| **otherPhone**  STRING |
| **otherPhoneType**  STRING |
| **personalEmail**  STRING |
| **postalCode**  STRING |
| **state**  STRING |
| **taxRegion**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |
| **workEmail**  STRING |
| **workPhone**  STRING |

### CreditBalanceAdjustment

The `CreditBalanceAdjustment` table contains information about [credit balance adjustments](https://knowledgecenter.zuora.com/CB_Billing/G_Credit_Balances), or the application of credit balances to invoices, payments, and refunds.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://knowledgecenter.zuora.com/Zuora_Platform/Integration/API/G_SOAP_API/E1_SOAP_API_Object_Reference/CreditBalanceAdjustment) |

CreditBalanceAdjustment table foreign keys

| Join CreditBalanceAdjustment with | on |
| --- | --- |
| [AccountingCode](#accountingcode) | ``` CreditBalanceAdjustment.accountingCode = AccountingCode.id ```  ``` CreditBalanceAdjustment.accountReceivableAccountingCodeId = AccountingCode.id ```  ``` CreditBalanceAdjustment.cashOnAccountAccountingCodeId = AccountingCode.id ``` |
| [InvoiceItem](#invoiceitem) | ``` CreditBalanceAdjustment.accountingCode = InvoiceItem.accountingCode ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` CreditBalanceAdjustment.accountingCode = InvoiceItemAdjustment.accountingCode ```  ``` CreditBalanceAdjustment.accountingPeriodId = InvoiceItemAdjustment.accountingPeriodId ```  ``` CreditBalanceAdjustment.accountReceivableAccountingCodeId = InvoiceItemAdjustment.accountReceivableAccountingCodeId ```  ``` CreditBalanceAdjustment.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` CreditBalanceAdjustment.journalEntryId = InvoiceItemAdjustment.journalEntryId ```  ``` CreditBalanceAdjustment.journalRunId = InvoiceItemAdjustment.journalRunId ```  ``` CreditBalanceAdjustment.parentAccountId = InvoiceItemAdjustment.parentAccountId ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` CreditBalanceAdjustment.accountingCode = ProductRatePlanCharge.accountingCode ``` |
| [AccountingPeriod](#accountingperiod) | ``` CreditBalanceAdjustment.accountingPeriodId = AccountingPeriod.id ``` |
| [JournalEntry](#journalentry) | ``` CreditBalanceAdjustment.accountingPeriodId = JournalEntry.accountingPeriodId ```  ``` CreditBalanceAdjustment.journalEntryId = JournalEntry.id ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` CreditBalanceAdjustment.accountingPeriodId = RevenueChargeSummaryItem.accountingPeriodId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` CreditBalanceAdjustment.parentAccountId = RevenueChargeSummaryItem.parentAccountId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` CreditBalanceAdjustment.accountingPeriodId = RevenueEventItemInvoiceItem.accountingPeriodId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` CreditBalanceAdjustment.journalEntryId = RevenueEventItemInvoiceItem.journalEntryId ```  ``` CreditBalanceAdjustment.journalRunId = RevenueEventItemInvoiceItem.journalRunId ```  ``` CreditBalanceAdjustment.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` CreditBalanceAdjustment.accountingPeriodId = RevenueEventItemInvoiceItemAdjustment.accountingPeriodId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` CreditBalanceAdjustment.journalEntryId = RevenueEventItemInvoiceItemAdjustment.journalEntryId ```  ``` CreditBalanceAdjustment.journalRunId = RevenueEventItemInvoiceItemAdjustment.journalRunId ```  ``` CreditBalanceAdjustment.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` CreditBalanceAdjustment.accountingPeriodId = RevenueScheduleItem.accountingPeriodId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueScheduleItem.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` CreditBalanceAdjustment.parentAccountId = RevenueScheduleItem.parentAccountId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` CreditBalanceAdjustment.accountingPeriodId = RevenueScheduleItemInvoiceItem.accountingPeriodId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` CreditBalanceAdjustment.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` CreditBalanceAdjustment.accountingPeriodId = RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` CreditBalanceAdjustment.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ``` |
| [Account](#account) | ``` CreditBalanceAdjustment.billToContactId = Account.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = Account.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = Account.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = Account.soldToContactId ```  ``` CreditBalanceAdjustment.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` CreditBalanceAdjustment.billToContactId = Contact.id ```  ``` CreditBalanceAdjustment.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` CreditBalanceAdjustment.billToContactId = ContactSnapshot.contactId ```  ``` CreditBalanceAdjustment.soldToContactId = ContactSnapshot.contactId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` CreditBalanceAdjustment.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` CreditBalanceAdjustment.parentAccountId = DiscountAppliedMetrics.parentAccountId ``` |
| [Invoice](#invoice) | ``` CreditBalanceAdjustment.billToContactId = Invoice.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = Invoice.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = Invoice.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = Invoice.soldToContactId ```  ``` CreditBalanceAdjustment.invoiceId = Invoice.id ```  ``` CreditBalanceAdjustment.sourceTransactionId = Invoice.id ```  ``` CreditBalanceAdjustment.sourceTransactionNumber = Invoice.invoiceNumber ```  ``` CreditBalanceAdjustment.parentAccountId = Invoice.parentAccountId ``` |
| [ProcessedUsage](#processedusage) | ``` CreditBalanceAdjustment.billToContactId = ProcessedUsage.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = ProcessedUsage.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = ProcessedUsage.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = ProcessedUsage.soldToContactId ```  ``` CreditBalanceAdjustment.parentAccountId = ProcessedUsage.parentAccountId ``` |
| [RatePlan](#rateplan) | ``` CreditBalanceAdjustment.billToContactId = RatePlan.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RatePlan.billToContactId ``` |
| [Refund](#refund) | ``` CreditBalanceAdjustment.billToContactId = Refund.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = Refund.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = Refund.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = Refund.soldToContactId ```  ``` CreditBalanceAdjustment.parentAccountId = Refund.parentAccountId ```  ``` CreditBalanceAdjustment.paymentMethodId = Refund.paymentMethodId ```  ``` CreditBalanceAdjustment.paymentMethodSnapshotId = Refund.paymentMethodSnapshotId ```  ``` CreditBalanceAdjustment.refundId = Refund.id ```  ``` CreditBalanceAdjustment.sourceTransactionId = Refund.id ``` |
| [RevenueEventItem](#revenueeventitem) | ``` CreditBalanceAdjustment.billToContactId = RevenueEventItem.billToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueEventItem.billToContactId ```  ``` CreditBalanceAdjustment.billToContactId = RevenueEventItem.soldToContactId ```  ``` CreditBalanceAdjustment.soldToContactId = RevenueEventItem.soldToContactId ```  ``` CreditBalanceAdjustment.journalEntryId = RevenueEventItem.journalEntryId ```  ``` CreditBalanceAdjustment.journalRunId = RevenueEventItem.journalRunId ```  ``` CreditBalanceAdjustment.parentAccountId = RevenueEventItem.parentAccountId ``` |
| [JournalEntryItem](#journalentryitem) | ``` CreditBalanceAdjustment.journalEntryId = JournalEntryItem.journalEntryId ```  ``` CreditBalanceAdjustment.journalRunId = JournalEntryItem.journalRunId ``` |
| [JournalRun](#journalrun) | ``` CreditBalanceAdjustment.journalRunId = JournalRun.id ``` |
| [Payment](#payment) | ``` CreditBalanceAdjustment.paymentId = Payment.id ```  ``` CreditBalanceAdjustment.sourceTransactionId = Payment.id ```  ``` CreditBalanceAdjustment.paymentMethodId = Payment.paymentMethodId ```  ``` CreditBalanceAdjustment.paymentMethodSnapshotId = Payment.paymentMethodSnapshotId ``` |
| [PaymentMethod](#paymentmethod) | ``` CreditBalanceAdjustment.paymentMethodId = PaymentMethod.id ``` |
| [PaymentMethodSnapshot](#paymentmethodsnapshot) | ``` CreditBalanceAdjustment.paymentMethodSnapshotId = PaymentMethodSnapshot.id ``` |

CreditBalanceAdjustment table schema

|  |
| --- |
| **accountId**  STRING |
| **accountReceivableAccountingCodeId**  STRING |
| **accountingCode**  STRING |
| **accountingPeriodId**  STRING |
| **adjustmentDate**  DATE-TIME |
| **amount**  DOUBLE |
| **billToContactId**  STRING |
| **cancelledOn**  DATE-TIME |
| **cashOnAccountAccountingCodeId**  STRING |
| **comment**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **defaultPaymentMethodId**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **invoiceId**  STRING |
| **journalEntryId**  STRING |
| **journalRunId**  STRING |
| **number**  STRING |
| **parentAccountId**  STRING |
| **paymentId**  STRING |
| **paymentMethodId**  STRING |
| **paymentMethodSnapshotId**  STRING |
| **reasonCode**  STRING |
| **referenceId**  STRING |
| **refundId**  STRING |
| **soldToContactId**  STRING |
| **sourceTransactionId**  STRING |
| **sourceTransactionNumber**  STRING |
| **sourceTransactionType**  STRING |
| **status**  STRING |
| **transferredToAccounting**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### DiscountAppliedMetrics

The `DiscountAppliedMetrics` table contains information about rate plan charges that use either a discount-fixed amount or discount-percentage charge model.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://knowledgecenter.zuora.com/Zuora_Platform/Data/Reporting/D_Data_Sources_and_Exports/C_Data_Source_Reference/Discount_Applied_Metrics_Data_Source) |

DiscountAppliedMetrics table foreign keys

| Join DiscountAppliedMetrics with | on |
| --- | --- |
| [Amendment](#amendment) | ``` DiscountAppliedMetrics.amendmentId = Amendment.id ```  ``` DiscountAppliedMetrics.subscriptionId = Amendment.subscriptionId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` DiscountAppliedMetrics.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` DiscountAppliedMetrics.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = InvoiceItemAdjustment.parentAccountId ```  ``` DiscountAppliedMetrics.productId = InvoiceItemAdjustment.productId ```  ``` DiscountAppliedMetrics.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = InvoiceItemAdjustment.ratePlanId ```  ``` DiscountAppliedMetrics.subscriptionId = InvoiceItemAdjustment.subscriptionId ``` |
| [ProcessedUsage](#processedusage) | ``` DiscountAppliedMetrics.amendmentId = ProcessedUsage.amendmentId ```  ``` DiscountAppliedMetrics.billToContactId = ProcessedUsage.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = ProcessedUsage.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = ProcessedUsage.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = ProcessedUsage.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = ProcessedUsage.parentAccountId ```  ``` DiscountAppliedMetrics.productId = ProcessedUsage.productId ```  ``` DiscountAppliedMetrics.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` DiscountAppliedMetrics.amendmentId = RatePlan.amendmentId ```  ``` DiscountAppliedMetrics.billToContactId = RatePlan.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RatePlan.billToContactId ```  ``` DiscountAppliedMetrics.productRatePlanId = RatePlan.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanId = RatePlan.id ```  ``` DiscountAppliedMetrics.subscriptionId = RatePlan.subscriptionId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` DiscountAppliedMetrics.amendmentId = RatePlanChargeTier.amendmentId ```  ``` DiscountAppliedMetrics.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = RatePlanChargeTier.ratePlanId ```  ``` DiscountAppliedMetrics.subscriptionId = RatePlanChargeTier.subscriptionId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` DiscountAppliedMetrics.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = RevenueChargeSummaryItem.parentAccountId ```  ``` DiscountAppliedMetrics.productId = RevenueChargeSummaryItem.productId ```  ``` DiscountAppliedMetrics.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = RevenueChargeSummaryItem.ratePlanId ```  ``` DiscountAppliedMetrics.subscriptionId = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` DiscountAppliedMetrics.amendmentId = RevenueEventItem.amendmentId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueEventItem.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueEventItem.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueEventItem.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueEventItem.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = RevenueEventItem.parentAccountId ```  ``` DiscountAppliedMetrics.productId = RevenueEventItem.productId ```  ``` DiscountAppliedMetrics.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = RevenueEventItem.ratePlanId ```  ``` DiscountAppliedMetrics.subscriptionId = RevenueEventItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` DiscountAppliedMetrics.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ```  ``` DiscountAppliedMetrics.productId = RevenueEventItemInvoiceItem.productId ```  ``` DiscountAppliedMetrics.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ```  ``` DiscountAppliedMetrics.subscriptionId = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` DiscountAppliedMetrics.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ```  ``` DiscountAppliedMetrics.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` DiscountAppliedMetrics.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ```  ``` DiscountAppliedMetrics.subscriptionId = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` DiscountAppliedMetrics.amendmentId = RevenueScheduleItem.amendmentId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueScheduleItem.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = RevenueScheduleItem.parentAccountId ```  ``` DiscountAppliedMetrics.productId = RevenueScheduleItem.productId ```  ``` DiscountAppliedMetrics.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = RevenueScheduleItem.ratePlanId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` DiscountAppliedMetrics.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ```  ``` DiscountAppliedMetrics.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` DiscountAppliedMetrics.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` DiscountAppliedMetrics.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ```  ``` DiscountAppliedMetrics.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` DiscountAppliedMetrics.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ```  ``` DiscountAppliedMetrics.subscriptionId = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |
| [Account](#account) | ``` DiscountAppliedMetrics.billToContactId = Account.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = Account.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = Account.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = Account.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` DiscountAppliedMetrics.billToContactId = Contact.id ```  ``` DiscountAppliedMetrics.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` DiscountAppliedMetrics.billToContactId = ContactSnapshot.contactId ```  ``` DiscountAppliedMetrics.soldToContactId = ContactSnapshot.contactId ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` DiscountAppliedMetrics.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [Invoice](#invoice) | ``` DiscountAppliedMetrics.billToContactId = Invoice.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = Invoice.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = Invoice.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = Invoice.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = Invoice.parentAccountId ``` |
| [Refund](#refund) | ``` DiscountAppliedMetrics.billToContactId = Refund.billToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = Refund.billToContactId ```  ``` DiscountAppliedMetrics.billToContactId = Refund.soldToContactId ```  ``` DiscountAppliedMetrics.soldToContactId = Refund.soldToContactId ```  ``` DiscountAppliedMetrics.parentAccountId = Refund.parentAccountId ``` |
| [RatePlanCharge](#rateplancharge) | ``` DiscountAppliedMetrics.discountRatePlanChargeId = RatePlanCharge.id ```  ``` DiscountAppliedMetrics.ratePlanChargeId = RatePlanCharge.id ``` |
| [Product](#product) | ``` DiscountAppliedMetrics.productId = Product.id ``` |
| [InvoiceItem](#invoiceitem) | ``` DiscountAppliedMetrics.productId = InvoiceItem.productId ```  ``` DiscountAppliedMetrics.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = InvoiceItem.ratePlanChargeId ```  ``` DiscountAppliedMetrics.subscriptionId = InvoiceItem.subscriptionId ``` |
| [ProductRatePlan](#productrateplan) | ``` DiscountAppliedMetrics.productId = ProductRatePlan.productId ```  ``` DiscountAppliedMetrics.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` DiscountAppliedMetrics.productRatePlanChargeId = ProductRatePlanCharge.id ```  ``` DiscountAppliedMetrics.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` DiscountAppliedMetrics.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` DiscountAppliedMetrics.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` DiscountAppliedMetrics.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` DiscountAppliedMetrics.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [Subscription](#subscription) | ``` DiscountAppliedMetrics.subscriptionId = Subscription.id ``` |

DiscountAppliedMetrics table schema

|  |
| --- |
| **accountId**  STRING |
| **amendmentId**  STRING |
| **billToContactId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **defaultPaymentMethodId**  STRING |
| **discountRatePlanChargeId**  STRING |
| **id**  STRING |
| **mrr**  STRING |
| **parentAccountId**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **soldToContactId**  STRING |
| **startDate**  DATE-TIME |
| **subscriptionId**  STRING |
| **tcv**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### Export

The `Export` table contains information about export jobs and files.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://knowledgecenter.zuora.com/Zuora_Platform/Integration/API/G_SOAP_API/E1_SOAP_API_Object_Reference/Export) |

Export table schema

|  |
| --- |
| **convertToCurrencies**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **encrypted**  BOOLEAN |
| **fileId**  STRING |
| **format**  STRING |
| **id**  STRING |
| **name**  STRING |
| **query**  STRING |
| **size**  INTEGER |
| **status**  STRING |
| **statusReason**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |
| **zip**  BOOLEAN |

### Import

The `Import` table contains information about content uploads.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Imports/) |

Import table schema

|  |
| --- |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **importType**  STRING |
| **importedCount**  INTEGER |
| **md5**  STRING |
| **name**  STRING |
| **originalResourceUrl**  STRING |
| **resultResourceUrl**  STRING |
| **status**  STRING |
| **statusReason**  STRING |
| **totalCount**  INTEGER |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### Invoice

The `Invoice` table contains info about invoices, which are bills to customers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Invoices/) |

Invoice table foreign keys

| Join Invoice with | on |
| --- | --- |
| [Account](#account) | ``` Invoice.accountId = Account.id ```  ``` Invoice.billToContactId = Account.billToContactId ```  ``` Invoice.soldToContactId = Account.billToContactId ```  ``` Invoice.billToContactId = Account.soldToContactId ```  ``` Invoice.soldToContactId = Account.soldToContactId ```  ``` Invoice.defaultPaymentMethodId = Account.defaultPaymentMethodId ```  ``` Invoice.parentAccountId = Account.parentAccountId ``` |
| [ContactSnapshot](#contactsnapshot) | ``` Invoice.accountId = ContactSnapshot.accountId ```  ``` Invoice.billToContactId = ContactSnapshot.contactId ```  ``` Invoice.billToContactSnapshotId = ContactSnapshot.contactId ```  ``` Invoice.soldToContactId = ContactSnapshot.contactId ```  ``` Invoice.soldToContactSnapshotId = ContactSnapshot.contactId ``` |
| [Payment](#payment) | ``` Invoice.accountId = Payment.accountId ```  ``` Invoice.id = Payment.id ```  ``` Invoice.invoiceNumber = Payment.number ``` |
| [Refund](#refund) | ``` Invoice.accountId = Refund.accountId ```  ``` Invoice.billToContactId = Refund.billToContactId ```  ``` Invoice.soldToContactId = Refund.billToContactId ```  ``` Invoice.billToContactId = Refund.soldToContactId ```  ``` Invoice.soldToContactId = Refund.soldToContactId ```  ``` Invoice.parentAccountId = Refund.parentAccountId ```  ``` Invoice.id = Refund.id ```  ``` Invoice.invoiceNumber = Refund.number ``` |
| [Subscription](#subscription) | ``` Invoice.accountId = Subscription.accountId ``` |
| [Contact](#contact) | ``` Invoice.billToContactId = Contact.id ```  ``` Invoice.soldToContactId = Contact.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` Invoice.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` Invoice.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` Invoice.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` Invoice.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` Invoice.id = CreditBalanceAdjustment.invoiceId ```  ``` Invoice.id = CreditBalanceAdjustment.sourceTransactionId ```  ``` Invoice.invoiceNumber = CreditBalanceAdjustment.sourceTransactionNumber ```  ``` Invoice.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` Invoice.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` Invoice.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` Invoice.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` Invoice.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` Invoice.parentAccountId = DiscountAppliedMetrics.parentAccountId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` Invoice.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` Invoice.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` Invoice.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` Invoice.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` Invoice.parentAccountId = InvoiceItemAdjustment.parentAccountId ``` |
| [ProcessedUsage](#processedusage) | ``` Invoice.billToContactId = ProcessedUsage.billToContactId ```  ``` Invoice.soldToContactId = ProcessedUsage.billToContactId ```  ``` Invoice.billToContactId = ProcessedUsage.soldToContactId ```  ``` Invoice.soldToContactId = ProcessedUsage.soldToContactId ```  ``` Invoice.parentAccountId = ProcessedUsage.parentAccountId ``` |
| [RatePlan](#rateplan) | ``` Invoice.billToContactId = RatePlan.billToContactId ```  ``` Invoice.soldToContactId = RatePlan.billToContactId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` Invoice.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` Invoice.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` Invoice.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` Invoice.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` Invoice.parentAccountId = RevenueChargeSummaryItem.parentAccountId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` Invoice.billToContactId = RevenueEventItem.billToContactId ```  ``` Invoice.soldToContactId = RevenueEventItem.billToContactId ```  ``` Invoice.billToContactId = RevenueEventItem.soldToContactId ```  ``` Invoice.soldToContactId = RevenueEventItem.soldToContactId ```  ``` Invoice.parentAccountId = RevenueEventItem.parentAccountId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` Invoice.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` Invoice.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` Invoice.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` Invoice.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` Invoice.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` Invoice.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` Invoice.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` Invoice.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` Invoice.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` Invoice.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` Invoice.billToContactId = RevenueScheduleItem.billToContactId ```  ``` Invoice.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` Invoice.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` Invoice.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` Invoice.parentAccountId = RevenueScheduleItem.parentAccountId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` Invoice.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` Invoice.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` Invoice.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` Invoice.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` Invoice.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` Invoice.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` Invoice.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` Invoice.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` Invoice.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` Invoice.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ``` |
| [PaymentMethod](#paymentmethod) | ``` Invoice.defaultPaymentMethodId = PaymentMethod.id ``` |

Invoice table schema

|  |
| --- |
| **accountId**  STRING |
| **adjustmentAccount**  DOUBLE |
| **amount**  DOUBLE |
| **amountWithoutTax**  DOUBLE |
| **autoPay**  BOOLEAN |
| **balance**  DOUBLE |
| **billRunId**  STRING |
| **billToContactId**  STRING |
| **billToContactSnapshotId**  STRING |
| **comments**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **creditBalanceAdjustmentAmount**  DOUBLE |
| **defaultPaymentMethodId**  STRING |
| **deleted**  BOOLEAN |
| **dueDate**  DATE-TIME |
| **id**  STRING |
| **includesOneTime**  BOOLEAN |
| **includesRecurring**  BOOLEAN |
| **includesUsage**  BOOLEAN |
| **invoiceDate**  DATE-TIME |
| **invoiceNumber**  STRING |
| **lastEmailSentDate**  DATE-TIME |
| **parentAccountId**  STRING |
| **paymentAmount**  DOUBLE |
| **postedBy**  STRING |
| **postedDate**  DATE-TIME |
| **refundAmount**  DOUBLE |
| **soldToContactId**  STRING |
| **soldToContactSnapshotId**  STRING |
| **source**  STRING |
| **sourceId**  STRING |
| **status**  STRING |
| **targetDate**  DATE-TIME |
| **taxAmount**  DOUBLE |
| **taxExemptAmount**  DOUBLE |
| **transferredToAccounting**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### InvoiceItem

The `InvoiceItem` table contains info about the line items in invoices.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://knowledgecenter.zuora.com/Zuora_Platform/Integration/API/G_SOAP_API/E1_SOAP_API_Object_Reference/InvoiceItem) |

InvoiceItem table foreign keys

| Join InvoiceItem with | on |
| --- | --- |
| [AccountingCode](#accountingcode) | ``` InvoiceItem.accountingCode = AccountingCode.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` InvoiceItem.accountingCode = CreditBalanceAdjustment.accountingCode ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` InvoiceItem.accountingCode = InvoiceItemAdjustment.accountingCode ```  ``` InvoiceItem.productId = InvoiceItemAdjustment.productId ```  ``` InvoiceItem.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` InvoiceItem.subscriptionId = InvoiceItemAdjustment.subscriptionId ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` InvoiceItem.accountingCode = ProductRatePlanCharge.accountingCode ```  ``` InvoiceItem.productRatePlanChargeId = ProductRatePlanCharge.id ``` |
| [ProcessedUsage](#processedusage) | ``` InvoiceItem.id = ProcessedUsage.invoiceItemId ```  ``` InvoiceItem.productId = ProcessedUsage.productId ```  ``` InvoiceItem.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` InvoiceItem.id = RevenueEventItemInvoiceItem.invoiceItemId ```  ``` InvoiceItem.productId = RevenueEventItemInvoiceItem.productId ```  ``` InvoiceItem.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` InvoiceItem.subscriptionId = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` InvoiceItem.id = RevenueEventItemInvoiceItemAdjustment.invoiceItemId ```  ``` InvoiceItem.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` InvoiceItem.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` InvoiceItem.subscriptionId = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` InvoiceItem.id = RevenueScheduleItemInvoiceItem.invoiceItemId ```  ``` InvoiceItem.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` InvoiceItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` InvoiceItem.id = RevenueScheduleItemInvoiceItemAdjustment.invoiceItemId ```  ``` InvoiceItem.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` InvoiceItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` InvoiceItem.subscriptionId = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |
| [Product](#product) | ``` InvoiceItem.productId = Product.id ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` InvoiceItem.productId = DiscountAppliedMetrics.productId ```  ``` InvoiceItem.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` InvoiceItem.subscriptionId = DiscountAppliedMetrics.subscriptionId ``` |
| [ProductRatePlan](#productrateplan) | ``` InvoiceItem.productId = ProductRatePlan.productId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` InvoiceItem.productId = RevenueChargeSummaryItem.productId ```  ``` InvoiceItem.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` InvoiceItem.subscriptionId = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` InvoiceItem.productId = RevenueEventItem.productId ```  ``` InvoiceItem.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` InvoiceItem.subscriptionId = RevenueEventItem.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` InvoiceItem.productId = RevenueScheduleItem.productId ```  ``` InvoiceItem.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` InvoiceItem.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` InvoiceItem.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ``` |
| [RatePlanCharge](#rateplancharge) | ``` InvoiceItem.ratePlanChargeId = RatePlanCharge.id ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` InvoiceItem.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` InvoiceItem.subscriptionId = RatePlanChargeTier.subscriptionId ``` |
| [Subscription](#subscription) | ``` InvoiceItem.subscriptionId = Subscription.id ``` |
| [Amendment](#amendment) | ``` InvoiceItem.subscriptionId = Amendment.subscriptionId ``` |
| [RatePlan](#rateplan) | ``` InvoiceItem.subscriptionId = RatePlan.subscriptionId ``` |

InvoiceItem table schema

|  |
| --- |
| **accountingCode**  STRING |
| **appliedToChargeNumber**  STRING |
| **appliedToInvoiceItemId**  STRING |
| **chargeAmount**  DECIMAL |
| **chargeDate**  DATE-TIME |
| **chargeName**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **invoiceId**  STRING |
| **processingType**  DECIMAL |
| **productDescription**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **quantity**  DECIMAL |
| **ratePlanChargeId**  STRING |
| **revRecCode**  STRING |
| **revRecStartDate**  DATE-TIME |
| **revRecTriggerCondition**  STRING |
| **serviceEndDate**  DATE-TIME |
| **serviceStartDate**  DATE-TIME |
| **sku**  STRING |
| **subscriptionId**  STRING |
| **taxAmaount**  DOUBLE |
| **taxCode**  STRING |
| **taxExemptAmount**  DOUBLE |
| **taxMode**  STRING |
| **unitPrice**  DOUBLE |
| **uom**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### InvoiceItemAdjustment

The `InvoiceItemAdjustment` table contains info about adjustments applied to invoice line items.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://knowledgecenter.zuora.com/Zuora_Platform/Integration/API/G_SOAP_API/E1_SOAP_API_Object_Reference/InvoiceItem) |

InvoiceItemAdjustment table foreign keys

| Join InvoiceItemAdjustment with | on |
| --- | --- |
| [AccountingCode](#accountingcode) | ``` InvoiceItemAdjustment.accountingCode = AccountingCode.id ```  ``` InvoiceItemAdjustment.accountReceivableAccountingCodeId = AccountingCode.id ```  ``` InvoiceItemAdjustment.recognizedRevenueAccountingCodeId = AccountingCode.id ```  ``` InvoiceItemAdjustment.salesTaxPayableAccountingCodeId = AccountingCode.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` InvoiceItemAdjustment.accountingCode = CreditBalanceAdjustment.accountingCode ```  ``` InvoiceItemAdjustment.accountingPeriodId = CreditBalanceAdjustment.accountingPeriodId ```  ``` InvoiceItemAdjustment.accountReceivableAccountingCodeId = CreditBalanceAdjustment.accountReceivableAccountingCodeId ```  ``` InvoiceItemAdjustment.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` InvoiceItemAdjustment.journalEntryId = CreditBalanceAdjustment.journalEntryId ```  ``` InvoiceItemAdjustment.journalRunId = CreditBalanceAdjustment.journalRunId ```  ``` InvoiceItemAdjustment.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [InvoiceItem](#invoiceitem) | ``` InvoiceItemAdjustment.accountingCode = InvoiceItem.accountingCode ```  ``` InvoiceItemAdjustment.productId = InvoiceItem.productId ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = InvoiceItem.ratePlanChargeId ```  ``` InvoiceItemAdjustment.subscriptionId = InvoiceItem.subscriptionId ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` InvoiceItemAdjustment.accountingCode = ProductRatePlanCharge.accountingCode ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = ProductRatePlanCharge.id ``` |
| [AccountingPeriod](#accountingperiod) | ``` InvoiceItemAdjustment.accountingPeriodId = AccountingPeriod.id ``` |
| [JournalEntry](#journalentry) | ``` InvoiceItemAdjustment.accountingPeriodId = JournalEntry.accountingPeriodId ```  ``` InvoiceItemAdjustment.journalEntryId = JournalEntry.id ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` InvoiceItemAdjustment.accountingPeriodId = RevenueChargeSummaryItem.accountingPeriodId ```  ``` InvoiceItemAdjustment.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` InvoiceItemAdjustment.parentAccountId = RevenueChargeSummaryItem.parentAccountId ```  ``` InvoiceItemAdjustment.productId = RevenueChargeSummaryItem.productId ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = RevenueChargeSummaryItem.ratePlanId ```  ``` InvoiceItemAdjustment.subscriptionId = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` InvoiceItemAdjustment.accountingPeriodId = RevenueEventItemInvoiceItem.accountingPeriodId ```  ``` InvoiceItemAdjustment.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` InvoiceItemAdjustment.journalEntryId = RevenueEventItemInvoiceItem.journalEntryId ```  ``` InvoiceItemAdjustment.journalRunId = RevenueEventItemInvoiceItem.journalRunId ```  ``` InvoiceItemAdjustment.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ```  ``` InvoiceItemAdjustment.productId = RevenueEventItemInvoiceItem.productId ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ```  ``` InvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` InvoiceItemAdjustment.subscriptionId = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` InvoiceItemAdjustment.accountingPeriodId = RevenueEventItemInvoiceItemAdjustment.accountingPeriodId ```  ``` InvoiceItemAdjustment.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` InvoiceItemAdjustment.id = RevenueEventItemInvoiceItemAdjustment.invoiceItemAdjustmentId ```  ``` InvoiceItemAdjustment.journalEntryId = RevenueEventItemInvoiceItemAdjustment.journalEntryId ```  ``` InvoiceItemAdjustment.journalRunId = RevenueEventItemInvoiceItemAdjustment.journalRunId ```  ``` InvoiceItemAdjustment.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ```  ``` InvoiceItemAdjustment.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ```  ``` InvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` InvoiceItemAdjustment.subscriptionId = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` InvoiceItemAdjustment.accountingPeriodId = RevenueScheduleItem.accountingPeriodId ```  ``` InvoiceItemAdjustment.amendmentId = RevenueScheduleItem.amendmentId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueScheduleItem.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` InvoiceItemAdjustment.parentAccountId = RevenueScheduleItem.parentAccountId ```  ``` InvoiceItemAdjustment.productId = RevenueScheduleItem.productId ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = RevenueScheduleItem.ratePlanId ```  ``` InvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueScheduleItem.recognizedRevenueAccountingCodeId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` InvoiceItemAdjustment.accountingPeriodId = RevenueScheduleItemInvoiceItem.accountingPeriodId ```  ``` InvoiceItemAdjustment.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` InvoiceItemAdjustment.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ```  ``` InvoiceItemAdjustment.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ```  ``` InvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` InvoiceItemAdjustment.accountingPeriodId = RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId ```  ``` InvoiceItemAdjustment.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` InvoiceItemAdjustment.id = RevenueScheduleItemInvoiceItemAdjustment.invoiceItemAdjustmentId ```  ``` InvoiceItemAdjustment.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ```  ``` InvoiceItemAdjustment.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ```  ``` InvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` InvoiceItemAdjustment.subscriptionId = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |
| [Amendment](#amendment) | ``` InvoiceItemAdjustment.amendmentId = Amendment.id ```  ``` InvoiceItemAdjustment.subscriptionId = Amendment.subscriptionId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` InvoiceItemAdjustment.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` InvoiceItemAdjustment.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` InvoiceItemAdjustment.parentAccountId = DiscountAppliedMetrics.parentAccountId ```  ``` InvoiceItemAdjustment.productId = DiscountAppliedMetrics.productId ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = DiscountAppliedMetrics.ratePlanId ```  ``` InvoiceItemAdjustment.subscriptionId = DiscountAppliedMetrics.subscriptionId ``` |
| [ProcessedUsage](#processedusage) | ``` InvoiceItemAdjustment.amendmentId = ProcessedUsage.amendmentId ```  ``` InvoiceItemAdjustment.billToContactId = ProcessedUsage.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = ProcessedUsage.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = ProcessedUsage.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = ProcessedUsage.soldToContactId ```  ``` InvoiceItemAdjustment.parentAccountId = ProcessedUsage.parentAccountId ```  ``` InvoiceItemAdjustment.productId = ProcessedUsage.productId ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` InvoiceItemAdjustment.amendmentId = RatePlan.amendmentId ```  ``` InvoiceItemAdjustment.billToContactId = RatePlan.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RatePlan.billToContactId ```  ``` InvoiceItemAdjustment.ratePlanId = RatePlan.id ```  ``` InvoiceItemAdjustment.subscriptionId = RatePlan.subscriptionId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` InvoiceItemAdjustment.amendmentId = RatePlanChargeTier.amendmentId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = RatePlanChargeTier.ratePlanId ```  ``` InvoiceItemAdjustment.subscriptionId = RatePlanChargeTier.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` InvoiceItemAdjustment.amendmentId = RevenueEventItem.amendmentId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueEventItem.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueEventItem.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = RevenueEventItem.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = RevenueEventItem.soldToContactId ```  ``` InvoiceItemAdjustment.journalEntryId = RevenueEventItem.journalEntryId ```  ``` InvoiceItemAdjustment.journalRunId = RevenueEventItem.journalRunId ```  ``` InvoiceItemAdjustment.parentAccountId = RevenueEventItem.parentAccountId ```  ``` InvoiceItemAdjustment.productId = RevenueEventItem.productId ```  ``` InvoiceItemAdjustment.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = RevenueEventItem.ratePlanId ```  ``` InvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueEventItem.recognizedRevenueAccountingCodeId ```  ``` InvoiceItemAdjustment.subscriptionId = RevenueEventItem.subscriptionId ``` |
| [Account](#account) | ``` InvoiceItemAdjustment.billToContactId = Account.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = Account.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = Account.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = Account.soldToContactId ```  ``` InvoiceItemAdjustment.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` InvoiceItemAdjustment.billToContactId = Contact.id ```  ``` InvoiceItemAdjustment.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` InvoiceItemAdjustment.billToContactId = ContactSnapshot.contactId ```  ``` InvoiceItemAdjustment.soldToContactId = ContactSnapshot.contactId ``` |
| [Invoice](#invoice) | ``` InvoiceItemAdjustment.billToContactId = Invoice.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = Invoice.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = Invoice.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = Invoice.soldToContactId ```  ``` InvoiceItemAdjustment.parentAccountId = Invoice.parentAccountId ``` |
| [Refund](#refund) | ``` InvoiceItemAdjustment.billToContactId = Refund.billToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = Refund.billToContactId ```  ``` InvoiceItemAdjustment.billToContactId = Refund.soldToContactId ```  ``` InvoiceItemAdjustment.soldToContactId = Refund.soldToContactId ```  ``` InvoiceItemAdjustment.parentAccountId = Refund.parentAccountId ``` |
| [JournalEntryItem](#journalentryitem) | ``` InvoiceItemAdjustment.journalEntryId = JournalEntryItem.journalEntryId ```  ``` InvoiceItemAdjustment.journalRunId = JournalEntryItem.journalRunId ``` |
| [JournalRun](#journalrun) | ``` InvoiceItemAdjustment.journalRunId = JournalRun.id ``` |
| [Product](#product) | ``` InvoiceItemAdjustment.productId = Product.id ``` |
| [ProductRatePlan](#productrateplan) | ``` InvoiceItemAdjustment.productId = ProductRatePlan.productId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` InvoiceItemAdjustment.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` InvoiceItemAdjustment.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` InvoiceItemAdjustment.ratePlanChargeId = RatePlanCharge.id ``` |
| [Subscription](#subscription) | ``` InvoiceItemAdjustment.subscriptionId = Subscription.id ``` |

InvoiceItemAdjustment table schema

|  |
| --- |
| **accountId**  STRING |
| **accountReceivableAccountingCodeId**  STRING |
| **accountingCode**  STRING |
| **accountingPeriodId**  STRING |
| **adjustmentDate**  DATE-TIME |
| **adjustmentNumber**  STRING |
| **amendmentId**  STRING |
| **amount**  DOUBLE |
| **billToContactId**  STRING |
| **cancelledById**  STRING |
| **cancelledDate**  DATE-TIME |
| **comment**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **customerName**  STRING |
| **customerNumber**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **invoiceId**  STRING |
| **invoiceItemName**  STRING |
| **invoiceNumber**  STRING |
| **journalEntryId**  STRING |
| **journalRunId**  STRING |
| **parentAccountId**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **reasonCode**  STRING |
| **recognizedRevenueAccountingCodeId**  DATE-TIME |
| **referenceId**  STRING |
| **salesTaxPayableAccountingCodeId**  STRING |
| **serviceEndDate**  DATE-TIME |
| **serviceStartDate**  DATE-TIME |
| **soldToContactId**  STRING |
| **sourceId**  STRING |
| **sourceType**  STRING |
| **status**  STRING |
| **subscriptionId**  STRING |
| **taxationItemId**  STRING |
| **transferredToAccounting**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### JournalEntry

The `JournalEntry` table contains information about

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Accounts/) |

JournalEntry table foreign keys

| Join JournalEntry with | on |
| --- | --- |
| [AccountingPeriod](#accountingperiod) | ``` JournalEntry.accountingPeriodId = AccountingPeriod.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` JournalEntry.accountingPeriodId = CreditBalanceAdjustment.accountingPeriodId ```  ``` JournalEntry.id = CreditBalanceAdjustment.journalEntryId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` JournalEntry.accountingPeriodId = InvoiceItemAdjustment.accountingPeriodId ```  ``` JournalEntry.id = InvoiceItemAdjustment.journalEntryId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` JournalEntry.accountingPeriodId = RevenueChargeSummaryItem.accountingPeriodId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` JournalEntry.accountingPeriodId = RevenueEventItemInvoiceItem.accountingPeriodId ```  ``` JournalEntry.id = RevenueEventItemInvoiceItem.journalEntryId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` JournalEntry.accountingPeriodId = RevenueEventItemInvoiceItemAdjustment.accountingPeriodId ```  ``` JournalEntry.id = RevenueEventItemInvoiceItemAdjustment.journalEntryId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` JournalEntry.accountingPeriodId = RevenueScheduleItem.accountingPeriodId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` JournalEntry.accountingPeriodId = RevenueScheduleItemInvoiceItem.accountingPeriodId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` JournalEntry.accountingPeriodId = RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId ``` |
| [JournalEntryItem](#journalentryitem) | ``` JournalEntry.id = JournalEntryItem.journalEntryId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` JournalEntry.id = RevenueEventItem.journalEntryId ``` |

JournalEntry table schema

|  |
| --- |
| **accountingPeriodId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **currency**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **journalEntryDate**  DATE-TIME |
| **journalRunId**  STRING |
| **notes**  STRING |
| **number**  STRING |
| **status**  STRING |
| **transferDate**  DATE-TIME |
| **transferredBy**  STRING |
| **updatedDate**  DATE-TIME |

### JournalEntryItem

The `JournalEntryItem` table contains information about journal entry items.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Summary-Journal-Entries/) |

JournalEntryItem table foreign keys

| Join JournalEntryItem with | on |
| --- | --- |
| [JournalEntry](#journalentry) | ``` JournalEntryItem.journalEntryId = JournalEntry.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` JournalEntryItem.journalEntryId = CreditBalanceAdjustment.journalEntryId ```  ``` JournalEntryItem.journalRunId = CreditBalanceAdjustment.journalRunId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` JournalEntryItem.journalEntryId = InvoiceItemAdjustment.journalEntryId ```  ``` JournalEntryItem.journalRunId = InvoiceItemAdjustment.journalRunId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` JournalEntryItem.journalEntryId = RevenueEventItem.journalEntryId ```  ``` JournalEntryItem.journalRunId = RevenueEventItem.journalRunId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` JournalEntryItem.journalEntryId = RevenueEventItemInvoiceItem.journalEntryId ```  ``` JournalEntryItem.journalRunId = RevenueEventItemInvoiceItem.journalRunId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` JournalEntryItem.journalEntryId = RevenueEventItemInvoiceItemAdjustment.journalEntryId ```  ``` JournalEntryItem.journalRunId = RevenueEventItemInvoiceItemAdjustment.journalRunId ``` |
| [JournalRun](#journalrun) | ``` JournalEntryItem.journalRunId = JournalRun.id ``` |

JournalEntryItem table schema

|  |
| --- |
| **accountingCodeId**  STRING |
| **accountingCodeType**  STRING |
| **amount**  DOUBLE |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **journalEntryId**  STRING |
| **journalRunId**  STRING |
| **type**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### JournalRun

The `JournalRun` table contains information about journal runs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Journal-Runs/) |

JournalRun table foreign keys

| Join JournalRun with | on |
| --- | --- |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` JournalRun.id = CreditBalanceAdjustment.journalRunId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` JournalRun.id = InvoiceItemAdjustment.journalRunId ``` |
| [JournalEntryItem](#journalentryitem) | ``` JournalRun.id = JournalEntryItem.journalRunId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` JournalRun.id = RevenueEventItem.journalRunId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` JournalRun.id = RevenueEventItemInvoiceItem.journalRunId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` JournalRun.id = RevenueEventItemInvoiceItemAdjustment.journalRunId ``` |

JournalRun table schema

|  |
| --- |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **executedOn**  DATE-TIME |
| **id**  STRING |
| **number**  STRING |
| **segmentationRuleName**  STRING |
| **status**  STRING |
| **targetEndDate**  DATE-TIME |
| **targetStartDate**  DATE-TIME |
| **totalJournalEntryCount**  INTEGER |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### Payment

The `payment` table contains info about customer payments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Payments/) |

Payment table foreign keys

| Join Payment with | on |
| --- | --- |
| [Account](#account) | ``` Payment.accountId = Account.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` Payment.accountId = ContactSnapshot.accountId ``` |
| [Invoice](#invoice) | ``` Payment.accountId = Invoice.accountId ```  ``` Payment.id = Invoice.id ```  ``` Payment.number = Invoice.invoiceNumber ``` |
| [Refund](#refund) | ``` Payment.accountId = Refund.accountId ```  ``` Payment.paymentMethodId = Refund.paymentMethodId ```  ``` Payment.paymentMethodSnapshotId = Refund.paymentMethodSnapshotId ```  ``` Payment.id = Refund.id ```  ``` Payment.number = Refund.number ``` |
| [Subscription](#subscription) | ``` Payment.accountId = Subscription.accountId ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` Payment.id = CreditBalanceAdjustment.paymentId ```  ``` Payment.id = CreditBalanceAdjustment.sourceTransactionId ```  ``` Payment.paymentMethodId = CreditBalanceAdjustment.paymentMethodId ```  ``` Payment.paymentMethodSnapshotId = CreditBalanceAdjustment.paymentMethodSnapshotId ``` |
| [PaymentMethod](#paymentmethod) | ``` Payment.paymentMethodId = PaymentMethod.id ``` |
| [PaymentMethodSnapshot](#paymentmethodsnapshot) | ``` Payment.paymentMethodSnapshotId = PaymentMethodSnapshot.id ``` |

Payment table schema

|  |
| --- |
| **accountId**  STRING |
| **amount**  NUMBER |
| **appliedAmount**  STRING |
| **authTransactionId**  STRING |
| **bankIdentificationNumber**  STRING |
| **cancelledOn**  DATE-TIME |
| **comment**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **creditBalanceAmount**  NUMBER |
| **currency**  STRING |
| **deleted**  BOOLEAN |
| **effectiveDate**  DATE-TIME |
| **gatewayId**  STRING |
| **gatewayResponse**  STRING |
| **gatewayResponseCode**  STRING |
| **gatewayState**  STRING |
| **id**  STRING |
| **markedForSubmissionOn**  DATE-TIME |
| **number**  STRING |
| **paymentDate**  DATE-TIME |
| **paymentId**  STRING |
| **paymentMethodId**  STRING |
| **paymentMethodSnapshotId**  STRING |
| **paymentTransactionTime**  DATE-TIME |
| **referenceId**  STRING |
| **refundAmount**  NUMBER |
| **secondPaymentReferenceId**  STRING |
| **settledOn**  DATE-TIME |
| **softDescriptor**  STRING |
| **softDescriptorPhone**  STRING |
| **status**  STRING |
| **submittedOn**  DATE-TIME |
| **success**  BOOLEAN |
| **type**  STRING |
| **unappliedAmount**  NUMBER |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### PaymentRun

The `PaymentRun` table contains information about payment runs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Payment-Runs/) |

PaymentRun table foreign keys

| Join PaymentRun with | on |
| --- | --- |
| [BillingRun](#billingrun) | ``` PaymentRun.billingRunId = BillingRun.id ``` |

PaymentRun table schema

|  |
| --- |
| **batch**  STRING |
| **billCycleDay**  STRING |
| **billingRunId**  STRING |
| **completedOn**  DATE-TIME |
| **consolidatedPayment**  BOOLEAN |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **currency**  STRING |
| **deleted**  BOOLEAN |
| **executedOn**  DATE-TIME |
| **id**  STRING |
| **number**  STRING |
| **numberOfErrors**  INTEGER |
| **numberOfInvoices**  INTEGER |
| **numberOfPayments**  INTEGER |
| **status**  STRING |
| **targetDate**  DATE-TIME |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### ProcessedUsage

The `ProcessedUsage` table contains information about usage.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Accounts/) |

ProcessedUsage table foreign keys

| Join ProcessedUsage with | on |
| --- | --- |
| [Amendment](#amendment) | ``` ProcessedUsage.amendmentId = Amendment.id ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` ProcessedUsage.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` ProcessedUsage.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` ProcessedUsage.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` ProcessedUsage.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` ProcessedUsage.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` ProcessedUsage.parentAccountId = DiscountAppliedMetrics.parentAccountId ```  ``` ProcessedUsage.productId = DiscountAppliedMetrics.productId ```  ``` ProcessedUsage.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` ProcessedUsage.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` ProcessedUsage.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = DiscountAppliedMetrics.ratePlanId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` ProcessedUsage.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` ProcessedUsage.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` ProcessedUsage.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` ProcessedUsage.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` ProcessedUsage.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` ProcessedUsage.parentAccountId = InvoiceItemAdjustment.parentAccountId ```  ``` ProcessedUsage.productId = InvoiceItemAdjustment.productId ```  ``` ProcessedUsage.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` ProcessedUsage.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = InvoiceItemAdjustment.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` ProcessedUsage.amendmentId = RatePlan.amendmentId ```  ``` ProcessedUsage.billToContactId = RatePlan.billToContactId ```  ``` ProcessedUsage.soldToContactId = RatePlan.billToContactId ```  ``` ProcessedUsage.productRatePlanId = RatePlan.productRatePlanId ```  ``` ProcessedUsage.ratePlanId = RatePlan.id ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` ProcessedUsage.amendmentId = RatePlanChargeTier.amendmentId ```  ``` ProcessedUsage.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` ProcessedUsage.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = RatePlanChargeTier.ratePlanId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` ProcessedUsage.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` ProcessedUsage.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` ProcessedUsage.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` ProcessedUsage.parentAccountId = RevenueChargeSummaryItem.parentAccountId ```  ``` ProcessedUsage.productId = RevenueChargeSummaryItem.productId ```  ``` ProcessedUsage.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` ProcessedUsage.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` ProcessedUsage.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = RevenueChargeSummaryItem.ratePlanId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` ProcessedUsage.amendmentId = RevenueEventItem.amendmentId ```  ``` ProcessedUsage.billToContactId = RevenueEventItem.billToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueEventItem.billToContactId ```  ``` ProcessedUsage.billToContactId = RevenueEventItem.soldToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueEventItem.soldToContactId ```  ``` ProcessedUsage.parentAccountId = RevenueEventItem.parentAccountId ```  ``` ProcessedUsage.productId = RevenueEventItem.productId ```  ``` ProcessedUsage.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` ProcessedUsage.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` ProcessedUsage.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = RevenueEventItem.ratePlanId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` ProcessedUsage.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` ProcessedUsage.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` ProcessedUsage.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` ProcessedUsage.invoiceItemId = RevenueEventItemInvoiceItem.invoiceItemId ```  ``` ProcessedUsage.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ```  ``` ProcessedUsage.productId = RevenueEventItemInvoiceItem.productId ```  ``` ProcessedUsage.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` ProcessedUsage.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` ProcessedUsage.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` ProcessedUsage.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` ProcessedUsage.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` ProcessedUsage.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` ProcessedUsage.invoiceItemId = RevenueEventItemInvoiceItemAdjustment.invoiceItemId ```  ``` ProcessedUsage.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ```  ``` ProcessedUsage.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` ProcessedUsage.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` ProcessedUsage.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` ProcessedUsage.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` ProcessedUsage.amendmentId = RevenueScheduleItem.amendmentId ```  ``` ProcessedUsage.billToContactId = RevenueScheduleItem.billToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` ProcessedUsage.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` ProcessedUsage.parentAccountId = RevenueScheduleItem.parentAccountId ```  ``` ProcessedUsage.productId = RevenueScheduleItem.productId ```  ``` ProcessedUsage.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` ProcessedUsage.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` ProcessedUsage.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = RevenueScheduleItem.ratePlanId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` ProcessedUsage.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` ProcessedUsage.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` ProcessedUsage.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` ProcessedUsage.invoiceItemId = RevenueScheduleItemInvoiceItem.invoiceItemId ```  ``` ProcessedUsage.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ```  ``` ProcessedUsage.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` ProcessedUsage.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` ProcessedUsage.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` ProcessedUsage.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` ProcessedUsage.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` ProcessedUsage.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` ProcessedUsage.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` ProcessedUsage.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` ProcessedUsage.invoiceItemId = RevenueScheduleItemInvoiceItemAdjustment.invoiceItemId ```  ``` ProcessedUsage.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ```  ``` ProcessedUsage.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` ProcessedUsage.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` ProcessedUsage.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` ProcessedUsage.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ``` |
| [Account](#account) | ``` ProcessedUsage.billToContactId = Account.billToContactId ```  ``` ProcessedUsage.soldToContactId = Account.billToContactId ```  ``` ProcessedUsage.billToContactId = Account.soldToContactId ```  ``` ProcessedUsage.soldToContactId = Account.soldToContactId ```  ``` ProcessedUsage.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` ProcessedUsage.billToContactId = Contact.id ```  ``` ProcessedUsage.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` ProcessedUsage.billToContactId = ContactSnapshot.contactId ```  ``` ProcessedUsage.soldToContactId = ContactSnapshot.contactId ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` ProcessedUsage.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` ProcessedUsage.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` ProcessedUsage.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` ProcessedUsage.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` ProcessedUsage.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [Invoice](#invoice) | ``` ProcessedUsage.billToContactId = Invoice.billToContactId ```  ``` ProcessedUsage.soldToContactId = Invoice.billToContactId ```  ``` ProcessedUsage.billToContactId = Invoice.soldToContactId ```  ``` ProcessedUsage.soldToContactId = Invoice.soldToContactId ```  ``` ProcessedUsage.parentAccountId = Invoice.parentAccountId ``` |
| [Refund](#refund) | ``` ProcessedUsage.billToContactId = Refund.billToContactId ```  ``` ProcessedUsage.soldToContactId = Refund.billToContactId ```  ``` ProcessedUsage.billToContactId = Refund.soldToContactId ```  ``` ProcessedUsage.soldToContactId = Refund.soldToContactId ```  ``` ProcessedUsage.parentAccountId = Refund.parentAccountId ``` |
| [InvoiceItem](#invoiceitem) | ``` ProcessedUsage.invoiceItemId = InvoiceItem.id ```  ``` ProcessedUsage.productId = InvoiceItem.productId ```  ``` ProcessedUsage.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` ProcessedUsage.ratePlanChargeId = InvoiceItem.ratePlanChargeId ``` |
| [Product](#product) | ``` ProcessedUsage.productId = Product.id ``` |
| [ProductRatePlan](#productrateplan) | ``` ProcessedUsage.productId = ProductRatePlan.productId ```  ``` ProcessedUsage.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` ProcessedUsage.productRatePlanChargeId = ProductRatePlanCharge.id ```  ``` ProcessedUsage.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` ProcessedUsage.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` ProcessedUsage.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` ProcessedUsage.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` ProcessedUsage.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` ProcessedUsage.ratePlanChargeId = RatePlanCharge.id ``` |

ProcessedUsage table schema

|  |
| --- |
| **accountId**  STRING |
| **amendmentId**  STRING |
| **amount**  DOUBLE |
| **billToContactId**  STRING |
| **billingPeriodEndDate**  DATE-TIME |
| **billingPeriodStartDate**  DATE-TIME |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **defaultPaymentMethodId**  STRING |
| **id**  STRING |
| **invoiceId**  STRING |
| **invoiceItemId**  STRING |
| **parentAccountId**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **soldToContactId**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |
| **usageId**  STRING |

### Product

The `Product` table contains info about your company’s product offerings.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](http://knowledgecenter.zuora.com/DC_Developers/SOAP_API/E1_SOAP_API_Object_Reference/Product#Field_Descriptions) |

Product table foreign keys

| Join Product with | on |
| --- | --- |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` Product.id = DiscountAppliedMetrics.productId ``` |
| [InvoiceItem](#invoiceitem) | ``` Product.id = InvoiceItem.productId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` Product.id = InvoiceItemAdjustment.productId ``` |
| [ProcessedUsage](#processedusage) | ``` Product.id = ProcessedUsage.productId ``` |
| [ProductRatePlan](#productrateplan) | ``` Product.id = ProductRatePlan.productId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` Product.id = RevenueChargeSummaryItem.productId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` Product.id = RevenueEventItem.productId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` Product.id = RevenueEventItemInvoiceItem.productId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` Product.id = RevenueEventItemInvoiceItemAdjustment.productId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` Product.id = RevenueScheduleItem.productId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` Product.id = RevenueScheduleItemInvoiceItem.productId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` Product.id = RevenueScheduleItemInvoiceItemAdjustment.productId ``` |

Product table schema

|  |
| --- |
| **allowFeatureChanges**  BOOLEAN |
| **category**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **effectiveEndDate**  DATE-TIME |
| **effectiveStartDate**  DATE-TIME |
| **id**  STRING |
| **name**  STRING |
| **sku**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### ProductRatePlan

The `ProductRatePlan` table contains info about product rate plans, or the part of a product that customers can subscribe to.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Product-Rate-Plans/) |

ProductRatePlan table foreign keys

| Join ProductRatePlan with | on |
| --- | --- |
| [Product](#product) | ``` ProductRatePlan.productId = Product.id ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` ProductRatePlan.productId = DiscountAppliedMetrics.productId ```  ``` ProductRatePlan.id = DiscountAppliedMetrics.productRatePlanId ``` |
| [InvoiceItem](#invoiceitem) | ``` ProductRatePlan.productId = InvoiceItem.productId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` ProductRatePlan.productId = InvoiceItemAdjustment.productId ``` |
| [ProcessedUsage](#processedusage) | ``` ProductRatePlan.productId = ProcessedUsage.productId ```  ``` ProductRatePlan.id = ProcessedUsage.productRatePlanId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` ProductRatePlan.productId = RevenueChargeSummaryItem.productId ```  ``` ProductRatePlan.id = RevenueChargeSummaryItem.productRatePlanId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` ProductRatePlan.productId = RevenueEventItem.productId ```  ``` ProductRatePlan.id = RevenueEventItem.productRatePlanId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` ProductRatePlan.productId = RevenueEventItemInvoiceItem.productId ```  ``` ProductRatePlan.id = RevenueEventItemInvoiceItem.productRatePlanId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` ProductRatePlan.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` ProductRatePlan.id = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` ProductRatePlan.productId = RevenueScheduleItem.productId ```  ``` ProductRatePlan.id = RevenueScheduleItem.productRatePlanId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` ProductRatePlan.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` ProductRatePlan.id = RevenueScheduleItemInvoiceItem.productRatePlanId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` ProductRatePlan.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` ProductRatePlan.id = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` ProductRatePlan.id = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` ProductRatePlan.id = ProductRatePlanChargeTier.productRatePlanId ``` |
| [RatePlan](#rateplan) | ``` ProductRatePlan.id = RatePlan.productRatePlanId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` ProductRatePlan.id = RatePlanChargeTier.productRatePlanId ``` |

ProductRatePlan table schema

|  |
| --- |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **defaultPaymentMethodId**  STRING |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **effectiveEndDate**  DATE-TIME |
| **effectiveStartDate**  DATE-TIME |
| **id**  STRING |
| **name**  STRING |
| **productId**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### ProductRatePlanCharge

The `ProductRatePlanCharge` table contains info about product rate plan charges, which are a charge model or set of fees associated with a product rate plan.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Product-Rate-Plan-Charges/) |

ProductRatePlanCharge table foreign keys

| Join ProductRatePlanCharge with | on |
| --- | --- |
| [AccountingCode](#accountingcode) | ``` ProductRatePlanCharge.accountingCode = AccountingCode.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` ProductRatePlanCharge.accountingCode = CreditBalanceAdjustment.accountingCode ``` |
| [InvoiceItem](#invoiceitem) | ``` ProductRatePlanCharge.accountingCode = InvoiceItem.accountingCode ```  ``` ProductRatePlanCharge.id = InvoiceItem.productRatePlanChargeId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` ProductRatePlanCharge.accountingCode = InvoiceItemAdjustment.accountingCode ```  ``` ProductRatePlanCharge.id = InvoiceItemAdjustment.productRatePlanChargeId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` ProductRatePlanCharge.id = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` ProductRatePlanCharge.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ``` |
| [ProcessedUsage](#processedusage) | ``` ProductRatePlanCharge.id = ProcessedUsage.productRatePlanChargeId ```  ``` ProductRatePlanCharge.productRatePlanId = ProcessedUsage.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` ProductRatePlanCharge.id = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` ProductRatePlanCharge.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` ProductRatePlanCharge.id = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` ProductRatePlanCharge.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` ProductRatePlanCharge.id = RevenueEventItem.productRatePlanChargeId ```  ``` ProductRatePlanCharge.productRatePlanId = RevenueEventItem.productRatePlanId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` ProductRatePlanCharge.id = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` ProductRatePlanCharge.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` ProductRatePlanCharge.id = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` ProductRatePlanCharge.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` ProductRatePlanCharge.id = RevenueScheduleItem.productRatePlanChargeId ```  ``` ProductRatePlanCharge.productRatePlanId = RevenueScheduleItem.productRatePlanId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` ProductRatePlanCharge.id = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` ProductRatePlanCharge.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` ProductRatePlanCharge.id = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` ProductRatePlanCharge.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ``` |
| [ProductRatePlan](#productrateplan) | ``` ProductRatePlanCharge.productRatePlanId = ProductRatePlan.id ``` |
| [RatePlan](#rateplan) | ``` ProductRatePlanCharge.productRatePlanId = RatePlan.productRatePlanId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` ProductRatePlanCharge.productRatePlanId = RatePlanChargeTier.productRatePlanId ``` |

ProductRatePlanCharge table schema

|  |
| --- |
| **accountingCode**  STRING |
| **applyDiscountTo**  STRING |
| **billCycleDay**  INTEGER |
| **billCycleType**  STRING |
| **billingPeriod**  STRING |
| **billingPeriodAlignment**  STRING |
| **billingTiming**  STRING |
| **chargeModel**  STRING |
| **chargeType**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **defaultQuantity**  DECIMAL |
| **deferredRevenueAccount**  STRING |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **discountClass**  STRING |
| **discountLevel**  STRING |
| **endDateCondition**  STRING |
| **id**  STRING |
| **includedUnits**  DECIMAL |
| **listPriceBase**  STRING |
| **maxQuantity**  DECIMAL |
| **minQuantity**  DECIMAL |
| **name**  STRING |
| **numberOfPeriod**  INTEGER |
| **overCalculationOption**  STRING |
| **overageUnusedUnitsCreditOption**  STRING |
| **priceChangeOption**  STRING |
| **priceIncreaseOption**  STRING |
| **productRatePlanId**  STRING |
| **recognizedRevenueAccount**  STRING |
| **revRecCode**  STRING |
| **revRecTriggerCondition**  STRING |
| **revenueRecognitionRuleName**  STRING |
| **smoothingModel**  STRING |
| **specificBillingPeriod**  INTEGER |
| **taxCode**  STRING |
| **taxMode**  STRING |
| **taxable**  BOOLEAN |
| **triggerEvent**  STRING |
| **uom**  STRING |
| **upToPeriods**  INTEGER |
| **upToPeriodsType**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |
| **useDiscountSpecificAccountingCode**  BOOLEAN |
| **useTenantDefaultForPriceChange**  BOOLEAN |
| **weeklyBillCycleDay**  STRING |

### ProductRatePlanChargeTier

The `ProductRatePlanChargeTier` table contains pricing info for product rate plan charges.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Product-Rate-Plan-Charge-Tiers/) |

ProductRatePlanChargeTier table foreign keys

| Join ProductRatePlanChargeTier with | on |
| --- | --- |
| [ProductRatePlanCharge](#productrateplancharge) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = ProductRatePlanCharge.id ```  ``` ProductRatePlanChargeTier.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = DiscountAppliedMetrics.ratePlanId ``` |
| [InvoiceItem](#invoiceitem) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = InvoiceItem.ratePlanChargeId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = InvoiceItemAdjustment.ratePlanId ``` |
| [ProcessedUsage](#processedusage) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = RevenueChargeSummaryItem.ratePlanId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = RevenueEventItem.ratePlanId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = RevenueScheduleItem.ratePlanId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` ProductRatePlanChargeTier.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` ProductRatePlanChargeTier.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ``` |
| [ProductRatePlan](#productrateplan) | ``` ProductRatePlanChargeTier.productRatePlanId = ProductRatePlan.id ``` |
| [RatePlan](#rateplan) | ``` ProductRatePlanChargeTier.productRatePlanId = RatePlan.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanId = RatePlan.id ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` ProductRatePlanChargeTier.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` ProductRatePlanChargeTier.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` ProductRatePlanChargeTier.ratePlanId = RatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` ProductRatePlanChargeTier.ratePlanChargeId = RatePlanCharge.id ``` |

ProductRatePlanChargeTier table schema

|  |
| --- |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **currency**  STRING |
| **deleted**  BOOLEAN |
| **endingUnit**  NUMBER |
| **id**  STRING |
| **price**  NUMBER |
| **priceFormat**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **startingUnit**  NUMBER |
| **tier**  INTEGER |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### RatePlan

The `RatePlan` table contains info about rate plans, which is a price or collection of prices for services.

#### Custom fields

In addition to the attributes listed below, our Zuora integration will also replicate any custom fields.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Rate-Plans/) |

RatePlan table foreign keys

| Join RatePlan with | on |
| --- | --- |
| [Amendment](#amendment) | ``` RatePlan.amendmentId = Amendment.id ```  ``` RatePlan.subscriptionId = Amendment.subscriptionId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` RatePlan.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` RatePlan.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RatePlan.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RatePlan.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` RatePlan.id = DiscountAppliedMetrics.ratePlanId ```  ``` RatePlan.subscriptionId = DiscountAppliedMetrics.subscriptionId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` RatePlan.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` RatePlan.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RatePlan.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RatePlan.id = InvoiceItemAdjustment.ratePlanId ```  ``` RatePlan.subscriptionId = InvoiceItemAdjustment.subscriptionId ``` |
| [ProcessedUsage](#processedusage) | ``` RatePlan.amendmentId = ProcessedUsage.amendmentId ```  ``` RatePlan.billToContactId = ProcessedUsage.billToContactId ```  ``` RatePlan.billToContactId = ProcessedUsage.soldToContactId ```  ``` RatePlan.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` RatePlan.id = ProcessedUsage.ratePlanId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` RatePlan.amendmentId = RatePlanChargeTier.amendmentId ```  ``` RatePlan.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` RatePlan.id = RatePlanChargeTier.ratePlanId ```  ``` RatePlan.subscriptionId = RatePlanChargeTier.subscriptionId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` RatePlan.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` RatePlan.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RatePlan.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RatePlan.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` RatePlan.id = RevenueChargeSummaryItem.ratePlanId ```  ``` RatePlan.subscriptionId = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` RatePlan.amendmentId = RevenueEventItem.amendmentId ```  ``` RatePlan.billToContactId = RevenueEventItem.billToContactId ```  ``` RatePlan.billToContactId = RevenueEventItem.soldToContactId ```  ``` RatePlan.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` RatePlan.id = RevenueEventItem.ratePlanId ```  ``` RatePlan.subscriptionId = RevenueEventItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` RatePlan.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` RatePlan.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RatePlan.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RatePlan.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` RatePlan.id = RevenueEventItemInvoiceItem.ratePlanId ```  ``` RatePlan.subscriptionId = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` RatePlan.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` RatePlan.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RatePlan.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RatePlan.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` RatePlan.id = RevenueEventItemInvoiceItemAdjustment.ratePlanId ```  ``` RatePlan.subscriptionId = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` RatePlan.amendmentId = RevenueScheduleItem.amendmentId ```  ``` RatePlan.billToContactId = RevenueScheduleItem.billToContactId ```  ``` RatePlan.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` RatePlan.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` RatePlan.id = RevenueScheduleItem.ratePlanId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` RatePlan.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` RatePlan.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RatePlan.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RatePlan.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` RatePlan.id = RevenueScheduleItemInvoiceItem.ratePlanId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` RatePlan.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` RatePlan.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RatePlan.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RatePlan.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` RatePlan.id = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ```  ``` RatePlan.subscriptionId = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |
| [Account](#account) | ``` RatePlan.billToContactId = Account.billToContactId ```  ``` RatePlan.billToContactId = Account.soldToContactId ``` |
| [Contact](#contact) | ``` RatePlan.billToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` RatePlan.billToContactId = ContactSnapshot.contactId ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` RatePlan.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RatePlan.billToContactId = CreditBalanceAdjustment.soldToContactId ``` |
| [Invoice](#invoice) | ``` RatePlan.billToContactId = Invoice.billToContactId ```  ``` RatePlan.billToContactId = Invoice.soldToContactId ``` |
| [Refund](#refund) | ``` RatePlan.billToContactId = Refund.billToContactId ```  ``` RatePlan.billToContactId = Refund.soldToContactId ``` |
| [ProductRatePlan](#productrateplan) | ``` RatePlan.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` RatePlan.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` RatePlan.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` RatePlan.id = ProductRatePlanChargeTier.ratePlanId ``` |
| [Subscription](#subscription) | ``` RatePlan.subscriptionId = Subscription.id ``` |
| [InvoiceItem](#invoiceitem) | ``` RatePlan.subscriptionId = InvoiceItem.subscriptionId ``` |

RatePlan table schema

|  |
| --- |
| **amendmentId**  STRING |
| **amendmentType**  STRING |
| **billToContactId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **name**  STRING |
| **productRatePlanId**  STRING |
| **subscriptionId**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### RatePlanChargeTier

The `RatePlanChargeTier` table contains pricing info for rate plan charges.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Product-Rate-Plan-Charge-Tiers/) |

RatePlanChargeTier table foreign keys

| Join RatePlanChargeTier with | on |
| --- | --- |
| [Amendment](#amendment) | ``` RatePlanChargeTier.amendmentId = Amendment.id ```  ``` RatePlanChargeTier.subscriptionId = Amendment.subscriptionId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` RatePlanChargeTier.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` RatePlanChargeTier.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = DiscountAppliedMetrics.ratePlanId ```  ``` RatePlanChargeTier.subscriptionId = DiscountAppliedMetrics.subscriptionId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` RatePlanChargeTier.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` RatePlanChargeTier.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = InvoiceItemAdjustment.ratePlanId ```  ``` RatePlanChargeTier.subscriptionId = InvoiceItemAdjustment.subscriptionId ``` |
| [ProcessedUsage](#processedusage) | ``` RatePlanChargeTier.amendmentId = ProcessedUsage.amendmentId ```  ``` RatePlanChargeTier.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` RatePlanChargeTier.amendmentId = RatePlan.amendmentId ```  ``` RatePlanChargeTier.productRatePlanId = RatePlan.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanId = RatePlan.id ```  ``` RatePlanChargeTier.subscriptionId = RatePlan.subscriptionId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` RatePlanChargeTier.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` RatePlanChargeTier.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = RevenueChargeSummaryItem.ratePlanId ```  ``` RatePlanChargeTier.subscriptionId = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` RatePlanChargeTier.amendmentId = RevenueEventItem.amendmentId ```  ``` RatePlanChargeTier.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = RevenueEventItem.ratePlanId ```  ``` RatePlanChargeTier.subscriptionId = RevenueEventItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` RatePlanChargeTier.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` RatePlanChargeTier.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ```  ``` RatePlanChargeTier.subscriptionId = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` RatePlanChargeTier.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` RatePlanChargeTier.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ```  ``` RatePlanChargeTier.subscriptionId = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` RatePlanChargeTier.amendmentId = RevenueScheduleItem.amendmentId ```  ``` RatePlanChargeTier.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = RevenueScheduleItem.ratePlanId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` RatePlanChargeTier.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` RatePlanChargeTier.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` RatePlanChargeTier.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` RatePlanChargeTier.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ```  ``` RatePlanChargeTier.subscriptionId = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |
| [ProductRatePlan](#productrateplan) | ``` RatePlanChargeTier.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` RatePlanChargeTier.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` RatePlanChargeTier.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` RatePlanChargeTier.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` RatePlanChargeTier.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` RatePlanChargeTier.ratePlanChargeId = RatePlanCharge.id ``` |
| [InvoiceItem](#invoiceitem) | ``` RatePlanChargeTier.ratePlanChargeId = InvoiceItem.ratePlanChargeId ```  ``` RatePlanChargeTier.subscriptionId = InvoiceItem.subscriptionId ``` |
| [Subscription](#subscription) | ``` RatePlanChargeTier.subscriptionId = Subscription.id ``` |

RatePlanChargeTier table schema

|  |
| --- |
| **amendmentId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **price**  NUMBER |
| **priceFormat**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **startingUnit**  NUMBER |
| **subscriptionId**  STRING |
| **tier**  INTEGER |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### Refund

The `Refund` table contains info about refunds, or transactions where money is returned to a customer.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Refunds/) |

Refund table foreign keys

| Join Refund with | on |
| --- | --- |
| [Account](#account) | ``` Refund.accountId = Account.id ```  ``` Refund.billToContactId = Account.billToContactId ```  ``` Refund.soldToContactId = Account.billToContactId ```  ``` Refund.billToContactId = Account.soldToContactId ```  ``` Refund.soldToContactId = Account.soldToContactId ```  ``` Refund.parentAccountId = Account.parentAccountId ``` |
| [ContactSnapshot](#contactsnapshot) | ``` Refund.accountId = ContactSnapshot.accountId ```  ``` Refund.billToContactId = ContactSnapshot.contactId ```  ``` Refund.soldToContactId = ContactSnapshot.contactId ``` |
| [Invoice](#invoice) | ``` Refund.accountId = Invoice.accountId ```  ``` Refund.billToContactId = Invoice.billToContactId ```  ``` Refund.soldToContactId = Invoice.billToContactId ```  ``` Refund.billToContactId = Invoice.soldToContactId ```  ``` Refund.soldToContactId = Invoice.soldToContactId ```  ``` Refund.parentAccountId = Invoice.parentAccountId ```  ``` Refund.id = Invoice.id ```  ``` Refund.number = Invoice.invoiceNumber ``` |
| [Payment](#payment) | ``` Refund.accountId = Payment.accountId ```  ``` Refund.paymentMethodId = Payment.paymentMethodId ```  ``` Refund.paymentMethodSnapshotId = Payment.paymentMethodSnapshotId ```  ``` Refund.id = Payment.id ```  ``` Refund.number = Payment.number ``` |
| [Subscription](#subscription) | ``` Refund.accountId = Subscription.accountId ``` |
| [Contact](#contact) | ``` Refund.billToContactId = Contact.id ```  ``` Refund.soldToContactId = Contact.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` Refund.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` Refund.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` Refund.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` Refund.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` Refund.parentAccountId = CreditBalanceAdjustment.parentAccountId ```  ``` Refund.paymentMethodId = CreditBalanceAdjustment.paymentMethodId ```  ``` Refund.paymentMethodSnapshotId = CreditBalanceAdjustment.paymentMethodSnapshotId ```  ``` Refund.id = CreditBalanceAdjustment.refundId ```  ``` Refund.id = CreditBalanceAdjustment.sourceTransactionId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` Refund.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` Refund.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` Refund.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` Refund.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` Refund.parentAccountId = DiscountAppliedMetrics.parentAccountId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` Refund.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` Refund.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` Refund.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` Refund.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` Refund.parentAccountId = InvoiceItemAdjustment.parentAccountId ``` |
| [ProcessedUsage](#processedusage) | ``` Refund.billToContactId = ProcessedUsage.billToContactId ```  ``` Refund.soldToContactId = ProcessedUsage.billToContactId ```  ``` Refund.billToContactId = ProcessedUsage.soldToContactId ```  ``` Refund.soldToContactId = ProcessedUsage.soldToContactId ```  ``` Refund.parentAccountId = ProcessedUsage.parentAccountId ``` |
| [RatePlan](#rateplan) | ``` Refund.billToContactId = RatePlan.billToContactId ```  ``` Refund.soldToContactId = RatePlan.billToContactId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` Refund.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` Refund.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` Refund.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` Refund.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` Refund.parentAccountId = RevenueChargeSummaryItem.parentAccountId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` Refund.billToContactId = RevenueEventItem.billToContactId ```  ``` Refund.soldToContactId = RevenueEventItem.billToContactId ```  ``` Refund.billToContactId = RevenueEventItem.soldToContactId ```  ``` Refund.soldToContactId = RevenueEventItem.soldToContactId ```  ``` Refund.parentAccountId = RevenueEventItem.parentAccountId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` Refund.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` Refund.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` Refund.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` Refund.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` Refund.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` Refund.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` Refund.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` Refund.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` Refund.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` Refund.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` Refund.billToContactId = RevenueScheduleItem.billToContactId ```  ``` Refund.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` Refund.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` Refund.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` Refund.parentAccountId = RevenueScheduleItem.parentAccountId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` Refund.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` Refund.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` Refund.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` Refund.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` Refund.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` Refund.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` Refund.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` Refund.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` Refund.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` Refund.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ``` |
| [PaymentMethod](#paymentmethod) | ``` Refund.paymentMethodId = PaymentMethod.id ``` |
| [PaymentMethodSnapshot](#paymentmethodsnapshot) | ``` Refund.paymentMethodSnapshotId = PaymentMethodSnapshot.id ``` |

Refund table schema

|  |
| --- |
| **accountId**  STRING |
| **amount**  NUMBER |
| **billToContactId**  STRING |
| **cancelledOn**  DATE-TIME |
| **comment**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **creditMemoId**  STRING |
| **defaultPaymentMethodId**  STRING |
| **deleted**  BOOLEAN |
| **gatewayId**  STRING |
| **gatewayResponse**  STRING |
| **gatewayResponseCode**  STRING |
| **gatewayState**  STRING |
| **id**  STRING |
| **markedForSubmissionOn**  DATE-TIME |
| **methodType**  STRING |
| **number**  STRING |
| **parentAccountId**  STRING |
| **paymentId**  STRING |
| **paymentMethodId**  STRING |
| **paymentMethodSnapshotId**  STRING |
| **reasonCode**  STRING |
| **referenceId**  STRING |
| **refundDate**  DATE-TIME |
| **refundTransactionTime**  DATE-TIME |
| **secondRefundReferenceId**  STRING |
| **settledOn**  DATE-TIME |
| **softDescriptor**  STRING |
| **softDescriptorPhone**  STRING |
| **soldToContactId**  STRING |
| **status**  STRING |
| **submittedOn**  DATE-TIME |
| **success**  BOOLEAN |
| **type**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### RevenueChargeSummaryItem

The `RevenueChargeSummaryItem` table contains information about [charge revenue summaries](https://knowledgecenter.zuora.com/CC_Finance/Revenue_Recognition/G_Revenue_Schedules/M_Charge_Revenue_Summary), which are summaries of all revenue distributions associated with a subscription charge.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/older-api/operation/GET_CRSByCRSNumber/) |

RevenueChargeSummaryItem table foreign keys

| Join RevenueChargeSummaryItem with | on |
| --- | --- |
| [AccountingPeriod](#accountingperiod) | ``` RevenueChargeSummaryItem.accountingPeriodId = AccountingPeriod.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` RevenueChargeSummaryItem.accountingPeriodId = CreditBalanceAdjustment.accountingPeriodId ```  ``` RevenueChargeSummaryItem.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` RevenueChargeSummaryItem.accountingPeriodId = InvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueChargeSummaryItem.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` RevenueChargeSummaryItem.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = InvoiceItemAdjustment.parentAccountId ```  ``` RevenueChargeSummaryItem.productId = InvoiceItemAdjustment.productId ```  ``` RevenueChargeSummaryItem.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = InvoiceItemAdjustment.ratePlanId ```  ``` RevenueChargeSummaryItem.subscriptionId = InvoiceItemAdjustment.subscriptionId ``` |
| [JournalEntry](#journalentry) | ``` RevenueChargeSummaryItem.accountingPeriodId = JournalEntry.accountingPeriodId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` RevenueChargeSummaryItem.accountingPeriodId = RevenueEventItemInvoiceItem.accountingPeriodId ```  ``` RevenueChargeSummaryItem.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ```  ``` RevenueChargeSummaryItem.productId = RevenueEventItemInvoiceItem.productId ```  ``` RevenueChargeSummaryItem.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ```  ``` RevenueChargeSummaryItem.revenueChargeSummaryId = RevenueEventItemInvoiceItem.revenueChargeSummaryId ```  ``` RevenueChargeSummaryItem.subscriptionId = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` RevenueChargeSummaryItem.accountingPeriodId = RevenueEventItemInvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueChargeSummaryItem.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueChargeSummaryItem.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` RevenueChargeSummaryItem.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueChargeSummaryItem.revenueChargeSummaryId = RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId ```  ``` RevenueChargeSummaryItem.subscriptionId = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` RevenueChargeSummaryItem.accountingPeriodId = RevenueScheduleItem.accountingPeriodId ```  ``` RevenueChargeSummaryItem.amendmentId = RevenueScheduleItem.amendmentId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = RevenueScheduleItem.parentAccountId ```  ``` RevenueChargeSummaryItem.productId = RevenueScheduleItem.productId ```  ``` RevenueChargeSummaryItem.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = RevenueScheduleItem.ratePlanId ```  ``` RevenueChargeSummaryItem.revenueChargeSummaryId = RevenueScheduleItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` RevenueChargeSummaryItem.accountingPeriodId = RevenueScheduleItemInvoiceItem.accountingPeriodId ```  ``` RevenueChargeSummaryItem.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ```  ``` RevenueChargeSummaryItem.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` RevenueChargeSummaryItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ```  ``` RevenueChargeSummaryItem.revenueChargeSummaryId = RevenueScheduleItemInvoiceItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` RevenueChargeSummaryItem.accountingPeriodId = RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueChargeSummaryItem.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueChargeSummaryItem.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` RevenueChargeSummaryItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueChargeSummaryItem.revenueChargeSummaryId = RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId ```  ``` RevenueChargeSummaryItem.subscriptionId = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |
| [Amendment](#amendment) | ``` RevenueChargeSummaryItem.amendmentId = Amendment.id ```  ``` RevenueChargeSummaryItem.subscriptionId = Amendment.subscriptionId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` RevenueChargeSummaryItem.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` RevenueChargeSummaryItem.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = DiscountAppliedMetrics.parentAccountId ```  ``` RevenueChargeSummaryItem.productId = DiscountAppliedMetrics.productId ```  ``` RevenueChargeSummaryItem.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = DiscountAppliedMetrics.ratePlanId ```  ``` RevenueChargeSummaryItem.subscriptionId = DiscountAppliedMetrics.subscriptionId ``` |
| [ProcessedUsage](#processedusage) | ``` RevenueChargeSummaryItem.amendmentId = ProcessedUsage.amendmentId ```  ``` RevenueChargeSummaryItem.billToContactId = ProcessedUsage.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = ProcessedUsage.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = ProcessedUsage.parentAccountId ```  ``` RevenueChargeSummaryItem.productId = ProcessedUsage.productId ```  ``` RevenueChargeSummaryItem.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` RevenueChargeSummaryItem.amendmentId = RatePlan.amendmentId ```  ``` RevenueChargeSummaryItem.billToContactId = RatePlan.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RatePlan.billToContactId ```  ``` RevenueChargeSummaryItem.productRatePlanId = RatePlan.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanId = RatePlan.id ```  ``` RevenueChargeSummaryItem.subscriptionId = RatePlan.subscriptionId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` RevenueChargeSummaryItem.amendmentId = RatePlanChargeTier.amendmentId ```  ``` RevenueChargeSummaryItem.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = RatePlanChargeTier.ratePlanId ```  ``` RevenueChargeSummaryItem.subscriptionId = RatePlanChargeTier.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` RevenueChargeSummaryItem.amendmentId = RevenueEventItem.amendmentId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueEventItem.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueEventItem.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = RevenueEventItem.parentAccountId ```  ``` RevenueChargeSummaryItem.productId = RevenueEventItem.productId ```  ``` RevenueChargeSummaryItem.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = RevenueEventItem.ratePlanId ```  ``` RevenueChargeSummaryItem.revenueChargeSummaryId = RevenueEventItem.revenueChargeSummaryId ```  ``` RevenueChargeSummaryItem.subscriptionId = RevenueEventItem.subscriptionId ``` |
| [Account](#account) | ``` RevenueChargeSummaryItem.billToContactId = Account.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = Account.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = Account.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = Account.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` RevenueChargeSummaryItem.billToContactId = Contact.id ```  ``` RevenueChargeSummaryItem.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` RevenueChargeSummaryItem.billToContactId = ContactSnapshot.contactId ```  ``` RevenueChargeSummaryItem.soldToContactId = ContactSnapshot.contactId ``` |
| [Invoice](#invoice) | ``` RevenueChargeSummaryItem.billToContactId = Invoice.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = Invoice.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = Invoice.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = Invoice.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = Invoice.parentAccountId ``` |
| [Refund](#refund) | ``` RevenueChargeSummaryItem.billToContactId = Refund.billToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = Refund.billToContactId ```  ``` RevenueChargeSummaryItem.billToContactId = Refund.soldToContactId ```  ``` RevenueChargeSummaryItem.soldToContactId = Refund.soldToContactId ```  ``` RevenueChargeSummaryItem.parentAccountId = Refund.parentAccountId ``` |
| [Product](#product) | ``` RevenueChargeSummaryItem.productId = Product.id ``` |
| [InvoiceItem](#invoiceitem) | ``` RevenueChargeSummaryItem.productId = InvoiceItem.productId ```  ``` RevenueChargeSummaryItem.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = InvoiceItem.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.subscriptionId = InvoiceItem.subscriptionId ``` |
| [ProductRatePlan](#productrateplan) | ``` RevenueChargeSummaryItem.productId = ProductRatePlan.productId ```  ``` RevenueChargeSummaryItem.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` RevenueChargeSummaryItem.productRatePlanChargeId = ProductRatePlanCharge.id ```  ``` RevenueChargeSummaryItem.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` RevenueChargeSummaryItem.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` RevenueChargeSummaryItem.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` RevenueChargeSummaryItem.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` RevenueChargeSummaryItem.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` RevenueChargeSummaryItem.ratePlanChargeId = RatePlanCharge.id ``` |
| [Subscription](#subscription) | ``` RevenueChargeSummaryItem.subscriptionId = Subscription.id ``` |

RevenueChargeSummaryItem table schema

|  |
| --- |
| **accountId**  STRING |
| **accountingPeriodId**  STRING |
| **amendmentId**  STRING |
| **amount**  DOUBLE |
| **billToContactId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **currency**  STRING |
| **defaultPaymentMethodId**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **parentAccountId**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **revenueChargeSummaryId**  STRING |
| **soldToContactId**  STRING |
| **subscriptionId**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### RevenueEventItem

The `RevenueEventItem` table contains information about revenue events. A revenue event is a change to a revenue schedule, such as creating the initial schedule, canceling an invoice, or recognizing an undistributed amount.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/older-api/tag/Revenue-Events/) |

RevenueEventItem table foreign keys

| Join RevenueEventItem with | on |
| --- | --- |
| [Amendment](#amendment) | ``` RevenueEventItem.amendmentId = Amendment.id ```  ``` RevenueEventItem.subscriptionId = Amendment.subscriptionId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` RevenueEventItem.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` RevenueEventItem.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueEventItem.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueEventItem.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueEventItem.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueEventItem.parentAccountId = DiscountAppliedMetrics.parentAccountId ```  ``` RevenueEventItem.productId = DiscountAppliedMetrics.productId ```  ``` RevenueEventItem.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` RevenueEventItem.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` RevenueEventItem.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = DiscountAppliedMetrics.ratePlanId ```  ``` RevenueEventItem.subscriptionId = DiscountAppliedMetrics.subscriptionId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` RevenueEventItem.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` RevenueEventItem.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItem.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItem.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItem.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItem.journalEntryId = InvoiceItemAdjustment.journalEntryId ```  ``` RevenueEventItem.journalRunId = InvoiceItemAdjustment.journalRunId ```  ``` RevenueEventItem.parentAccountId = InvoiceItemAdjustment.parentAccountId ```  ``` RevenueEventItem.productId = InvoiceItemAdjustment.productId ```  ``` RevenueEventItem.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueEventItem.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = InvoiceItemAdjustment.ratePlanId ```  ``` RevenueEventItem.recognizedRevenueAccountingCodeId = InvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItem.subscriptionId = InvoiceItemAdjustment.subscriptionId ``` |
| [ProcessedUsage](#processedusage) | ``` RevenueEventItem.amendmentId = ProcessedUsage.amendmentId ```  ``` RevenueEventItem.billToContactId = ProcessedUsage.billToContactId ```  ``` RevenueEventItem.soldToContactId = ProcessedUsage.billToContactId ```  ``` RevenueEventItem.billToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueEventItem.soldToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueEventItem.parentAccountId = ProcessedUsage.parentAccountId ```  ``` RevenueEventItem.productId = ProcessedUsage.productId ```  ``` RevenueEventItem.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` RevenueEventItem.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` RevenueEventItem.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` RevenueEventItem.amendmentId = RatePlan.amendmentId ```  ``` RevenueEventItem.billToContactId = RatePlan.billToContactId ```  ``` RevenueEventItem.soldToContactId = RatePlan.billToContactId ```  ``` RevenueEventItem.productRatePlanId = RatePlan.productRatePlanId ```  ``` RevenueEventItem.ratePlanId = RatePlan.id ```  ``` RevenueEventItem.subscriptionId = RatePlan.subscriptionId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` RevenueEventItem.amendmentId = RatePlanChargeTier.amendmentId ```  ``` RevenueEventItem.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` RevenueEventItem.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = RatePlanChargeTier.ratePlanId ```  ``` RevenueEventItem.subscriptionId = RatePlanChargeTier.subscriptionId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` RevenueEventItem.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` RevenueEventItem.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueEventItem.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueEventItem.parentAccountId = RevenueChargeSummaryItem.parentAccountId ```  ``` RevenueEventItem.productId = RevenueChargeSummaryItem.productId ```  ``` RevenueEventItem.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` RevenueEventItem.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` RevenueEventItem.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = RevenueChargeSummaryItem.ratePlanId ```  ``` RevenueEventItem.revenueChargeSummaryId = RevenueChargeSummaryItem.revenueChargeSummaryId ```  ``` RevenueEventItem.subscriptionId = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` RevenueEventItem.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` RevenueEventItem.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueEventItem.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueEventItem.deferredRevenueAccountingCodeId = RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` RevenueEventItem.journalEntryId = RevenueEventItemInvoiceItem.journalEntryId ```  ``` RevenueEventItem.journalRunId = RevenueEventItemInvoiceItem.journalRunId ```  ``` RevenueEventItem.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ```  ``` RevenueEventItem.productId = RevenueEventItemInvoiceItem.productId ```  ``` RevenueEventItem.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueEventItem.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` RevenueEventItem.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ```  ``` RevenueEventItem.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItem.revenueChargeSummaryId = RevenueEventItemInvoiceItem.revenueChargeSummaryId ```  ``` RevenueEventItem.subscriptionId = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` RevenueEventItem.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueEventItem.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItem.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItem.deferredRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` RevenueEventItem.journalEntryId = RevenueEventItemInvoiceItemAdjustment.journalEntryId ```  ``` RevenueEventItem.journalRunId = RevenueEventItemInvoiceItemAdjustment.journalRunId ```  ``` RevenueEventItem.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueEventItem.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` RevenueEventItem.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueEventItem.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueEventItem.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueEventItem.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItem.revenueChargeSummaryId = RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId ```  ``` RevenueEventItem.subscriptionId = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` RevenueEventItem.amendmentId = RevenueScheduleItem.amendmentId ```  ``` RevenueEventItem.billToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueEventItem.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueEventItem.deferredRevenueAccountingCodeId = RevenueScheduleItem.deferredRevenueAccountingCodeId ```  ``` RevenueEventItem.parentAccountId = RevenueScheduleItem.parentAccountId ```  ``` RevenueEventItem.productId = RevenueScheduleItem.productId ```  ``` RevenueEventItem.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` RevenueEventItem.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` RevenueEventItem.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = RevenueScheduleItem.ratePlanId ```  ``` RevenueEventItem.recognizedRevenueAccountingCodeId = RevenueScheduleItem.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItem.revenueChargeSummaryId = RevenueScheduleItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` RevenueEventItem.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` RevenueEventItem.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueEventItem.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueEventItem.deferredRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` RevenueEventItem.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ```  ``` RevenueEventItem.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` RevenueEventItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueEventItem.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` RevenueEventItem.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ```  ``` RevenueEventItem.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItem.revenueChargeSummaryId = RevenueScheduleItemInvoiceItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` RevenueEventItem.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueEventItem.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItem.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItem.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItem.deferredRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` RevenueEventItem.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueEventItem.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` RevenueEventItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueEventItem.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueEventItem.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueEventItem.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItem.revenueChargeSummaryId = RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId ```  ``` RevenueEventItem.subscriptionId = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |
| [Account](#account) | ``` RevenueEventItem.billToContactId = Account.billToContactId ```  ``` RevenueEventItem.soldToContactId = Account.billToContactId ```  ``` RevenueEventItem.billToContactId = Account.soldToContactId ```  ``` RevenueEventItem.soldToContactId = Account.soldToContactId ```  ``` RevenueEventItem.deferredRevenueAccountingCodeId = Account.id ```  ``` RevenueEventItem.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` RevenueEventItem.billToContactId = Contact.id ```  ``` RevenueEventItem.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` RevenueEventItem.billToContactId = ContactSnapshot.contactId ```  ``` RevenueEventItem.soldToContactId = ContactSnapshot.contactId ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` RevenueEventItem.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueEventItem.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueEventItem.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueEventItem.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueEventItem.journalEntryId = CreditBalanceAdjustment.journalEntryId ```  ``` RevenueEventItem.journalRunId = CreditBalanceAdjustment.journalRunId ```  ``` RevenueEventItem.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [Invoice](#invoice) | ``` RevenueEventItem.billToContactId = Invoice.billToContactId ```  ``` RevenueEventItem.soldToContactId = Invoice.billToContactId ```  ``` RevenueEventItem.billToContactId = Invoice.soldToContactId ```  ``` RevenueEventItem.soldToContactId = Invoice.soldToContactId ```  ``` RevenueEventItem.parentAccountId = Invoice.parentAccountId ``` |
| [Refund](#refund) | ``` RevenueEventItem.billToContactId = Refund.billToContactId ```  ``` RevenueEventItem.soldToContactId = Refund.billToContactId ```  ``` RevenueEventItem.billToContactId = Refund.soldToContactId ```  ``` RevenueEventItem.soldToContactId = Refund.soldToContactId ```  ``` RevenueEventItem.parentAccountId = Refund.parentAccountId ``` |
| [JournalEntry](#journalentry) | ``` RevenueEventItem.journalEntryId = JournalEntry.id ``` |
| [JournalEntryItem](#journalentryitem) | ``` RevenueEventItem.journalEntryId = JournalEntryItem.journalEntryId ```  ``` RevenueEventItem.journalRunId = JournalEntryItem.journalRunId ``` |
| [JournalRun](#journalrun) | ``` RevenueEventItem.journalRunId = JournalRun.id ``` |
| [Product](#product) | ``` RevenueEventItem.productId = Product.id ``` |
| [InvoiceItem](#invoiceitem) | ``` RevenueEventItem.productId = InvoiceItem.productId ```  ``` RevenueEventItem.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` RevenueEventItem.ratePlanChargeId = InvoiceItem.ratePlanChargeId ```  ``` RevenueEventItem.subscriptionId = InvoiceItem.subscriptionId ``` |
| [ProductRatePlan](#productrateplan) | ``` RevenueEventItem.productId = ProductRatePlan.productId ```  ``` RevenueEventItem.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` RevenueEventItem.productRatePlanChargeId = ProductRatePlanCharge.id ```  ``` RevenueEventItem.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` RevenueEventItem.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` RevenueEventItem.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` RevenueEventItem.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` RevenueEventItem.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` RevenueEventItem.ratePlanChargeId = RatePlanCharge.id ``` |
| [AccountingCode](#accountingcode) | ``` RevenueEventItem.recognizedRevenueAccountingCodeId = AccountingCode.id ``` |
| [Subscription](#subscription) | ``` RevenueEventItem.subscriptionId = Subscription.id ``` |

RevenueEventItem table schema

|  |
| --- |
| **accountId**  STRING |
| **amendmentId**  STRING |
| **amount**  DOUBLE |
| **billToContactId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **defaultPaymentMethodId**  STRING |
| **deferredRevenueAccountingCodeId**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **journalEntryId**  STRING |
| **journalRunId**  STRING |
| **parentAccountId**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **recognizedRevenueAccountingCodeId**  STRING |
| **revenueChargeSummaryId**  STRING |
| **revenueEventId**  STRING |
| **revenueEventTypeId**  STRING |
| **revenueScheduleId**  STRING |
| **soldToContactId**  STRING |
| **subscriptionId**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### RevenueEventItemInvoiceItem

The `RevenueEventItemInvoiceItem` table contains information about revenue event items that are associated with invoice items.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/older-api/tag/Revenue-Events/) |

RevenueEventItemInvoiceItem table foreign keys

| Join RevenueEventItemInvoiceItem with | on |
| --- | --- |
| [AccountingPeriod](#accountingperiod) | ``` RevenueEventItemInvoiceItem.accountingPeriodId = AccountingPeriod.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` RevenueEventItemInvoiceItem.accountingPeriodId = CreditBalanceAdjustment.accountingPeriodId ```  ``` RevenueEventItemInvoiceItem.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItem.journalEntryId = CreditBalanceAdjustment.journalEntryId ```  ``` RevenueEventItemInvoiceItem.journalRunId = CreditBalanceAdjustment.journalRunId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` RevenueEventItemInvoiceItem.accountingPeriodId = InvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueEventItemInvoiceItem.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` RevenueEventItemInvoiceItem.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItem.journalEntryId = InvoiceItemAdjustment.journalEntryId ```  ``` RevenueEventItemInvoiceItem.journalRunId = InvoiceItemAdjustment.journalRunId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = InvoiceItemAdjustment.parentAccountId ```  ``` RevenueEventItemInvoiceItem.productId = InvoiceItemAdjustment.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = InvoiceItemAdjustment.ratePlanId ```  ``` RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId = InvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.subscriptionId = InvoiceItemAdjustment.subscriptionId ``` |
| [JournalEntry](#journalentry) | ``` RevenueEventItemInvoiceItem.accountingPeriodId = JournalEntry.accountingPeriodId ```  ``` RevenueEventItemInvoiceItem.journalEntryId = JournalEntry.id ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` RevenueEventItemInvoiceItem.accountingPeriodId = RevenueChargeSummaryItem.accountingPeriodId ```  ``` RevenueEventItemInvoiceItem.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = RevenueChargeSummaryItem.parentAccountId ```  ``` RevenueEventItemInvoiceItem.productId = RevenueChargeSummaryItem.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = RevenueChargeSummaryItem.ratePlanId ```  ``` RevenueEventItemInvoiceItem.revenueChargeSummaryId = RevenueChargeSummaryItem.revenueChargeSummaryId ```  ``` RevenueEventItemInvoiceItem.subscriptionId = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` RevenueEventItemInvoiceItem.accountingPeriodId = RevenueEventItemInvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueEventItemInvoiceItem.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.invoiceItemId = RevenueEventItemInvoiceItemAdjustment.invoiceItemId ```  ``` RevenueEventItemInvoiceItem.journalEntryId = RevenueEventItemInvoiceItemAdjustment.journalEntryId ```  ``` RevenueEventItemInvoiceItem.journalRunId = RevenueEventItemInvoiceItemAdjustment.journalRunId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueEventItemInvoiceItem.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.revenueChargeSummaryId = RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId ```  ``` RevenueEventItemInvoiceItem.subscriptionId = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` RevenueEventItemInvoiceItem.accountingPeriodId = RevenueScheduleItem.accountingPeriodId ```  ``` RevenueEventItemInvoiceItem.amendmentId = RevenueScheduleItem.amendmentId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId = RevenueScheduleItem.deferredRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = RevenueScheduleItem.parentAccountId ```  ``` RevenueEventItemInvoiceItem.productId = RevenueScheduleItem.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = RevenueScheduleItem.ratePlanId ```  ``` RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId = RevenueScheduleItem.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.revenueChargeSummaryId = RevenueScheduleItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` RevenueEventItemInvoiceItem.accountingPeriodId = RevenueScheduleItemInvoiceItem.accountingPeriodId ```  ``` RevenueEventItemInvoiceItem.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.invoiceItemId = RevenueScheduleItemInvoiceItem.invoiceItemId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ```  ``` RevenueEventItemInvoiceItem.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ```  ``` RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.revenueChargeSummaryId = RevenueScheduleItemInvoiceItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` RevenueEventItemInvoiceItem.accountingPeriodId = RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueEventItemInvoiceItem.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.invoiceItemId = RevenueScheduleItemInvoiceItemAdjustment.invoiceItemId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueEventItemInvoiceItem.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.revenueChargeSummaryId = RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId ```  ``` RevenueEventItemInvoiceItem.subscriptionId = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |
| [Amendment](#amendment) | ``` RevenueEventItemInvoiceItem.amendmentId = Amendment.id ```  ``` RevenueEventItemInvoiceItem.subscriptionId = Amendment.subscriptionId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` RevenueEventItemInvoiceItem.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` RevenueEventItemInvoiceItem.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = DiscountAppliedMetrics.parentAccountId ```  ``` RevenueEventItemInvoiceItem.productId = DiscountAppliedMetrics.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = DiscountAppliedMetrics.ratePlanId ```  ``` RevenueEventItemInvoiceItem.subscriptionId = DiscountAppliedMetrics.subscriptionId ``` |
| [ProcessedUsage](#processedusage) | ``` RevenueEventItemInvoiceItem.amendmentId = ProcessedUsage.amendmentId ```  ``` RevenueEventItemInvoiceItem.billToContactId = ProcessedUsage.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = ProcessedUsage.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueEventItemInvoiceItem.invoiceItemId = ProcessedUsage.invoiceItemId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = ProcessedUsage.parentAccountId ```  ``` RevenueEventItemInvoiceItem.productId = ProcessedUsage.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` RevenueEventItemInvoiceItem.amendmentId = RatePlan.amendmentId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RatePlan.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RatePlan.billToContactId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = RatePlan.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = RatePlan.id ```  ``` RevenueEventItemInvoiceItem.subscriptionId = RatePlan.subscriptionId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` RevenueEventItemInvoiceItem.amendmentId = RatePlanChargeTier.amendmentId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = RatePlanChargeTier.ratePlanId ```  ``` RevenueEventItemInvoiceItem.subscriptionId = RatePlanChargeTier.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` RevenueEventItemInvoiceItem.amendmentId = RevenueEventItem.amendmentId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueEventItem.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueEventItem.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId = RevenueEventItem.deferredRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.journalEntryId = RevenueEventItem.journalEntryId ```  ``` RevenueEventItemInvoiceItem.journalRunId = RevenueEventItem.journalRunId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = RevenueEventItem.parentAccountId ```  ``` RevenueEventItemInvoiceItem.productId = RevenueEventItem.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = RevenueEventItem.ratePlanId ```  ``` RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId = RevenueEventItem.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItem.revenueChargeSummaryId = RevenueEventItem.revenueChargeSummaryId ```  ``` RevenueEventItemInvoiceItem.subscriptionId = RevenueEventItem.subscriptionId ``` |
| [Account](#account) | ``` RevenueEventItemInvoiceItem.billToContactId = Account.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = Account.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = Account.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = Account.soldToContactId ```  ``` RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId = Account.id ```  ``` RevenueEventItemInvoiceItem.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` RevenueEventItemInvoiceItem.billToContactId = Contact.id ```  ``` RevenueEventItemInvoiceItem.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` RevenueEventItemInvoiceItem.billToContactId = ContactSnapshot.contactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = ContactSnapshot.contactId ``` |
| [Invoice](#invoice) | ``` RevenueEventItemInvoiceItem.billToContactId = Invoice.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = Invoice.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = Invoice.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = Invoice.soldToContactId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = Invoice.parentAccountId ``` |
| [Refund](#refund) | ``` RevenueEventItemInvoiceItem.billToContactId = Refund.billToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = Refund.billToContactId ```  ``` RevenueEventItemInvoiceItem.billToContactId = Refund.soldToContactId ```  ``` RevenueEventItemInvoiceItem.soldToContactId = Refund.soldToContactId ```  ``` RevenueEventItemInvoiceItem.parentAccountId = Refund.parentAccountId ``` |
| [InvoiceItem](#invoiceitem) | ``` RevenueEventItemInvoiceItem.invoiceItemId = InvoiceItem.id ```  ``` RevenueEventItemInvoiceItem.productId = InvoiceItem.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = InvoiceItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.subscriptionId = InvoiceItem.subscriptionId ``` |
| [JournalEntryItem](#journalentryitem) | ``` RevenueEventItemInvoiceItem.journalEntryId = JournalEntryItem.journalEntryId ```  ``` RevenueEventItemInvoiceItem.journalRunId = JournalEntryItem.journalRunId ``` |
| [JournalRun](#journalrun) | ``` RevenueEventItemInvoiceItem.journalRunId = JournalRun.id ``` |
| [Product](#product) | ``` RevenueEventItemInvoiceItem.productId = Product.id ``` |
| [ProductRatePlan](#productrateplan) | ``` RevenueEventItemInvoiceItem.productId = ProductRatePlan.productId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = ProductRatePlanCharge.id ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` RevenueEventItemInvoiceItem.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItem.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` RevenueEventItemInvoiceItem.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItem.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` RevenueEventItemInvoiceItem.ratePlanChargeId = RatePlanCharge.id ``` |
| [AccountingCode](#accountingcode) | ``` RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId = AccountingCode.id ``` |
| [Subscription](#subscription) | ``` RevenueEventItemInvoiceItem.subscriptionId = Subscription.id ``` |

RevenueEventItemInvoiceItem table schema

|  |
| --- |
| **accountId**  STRING |
| **accountingPeriodId**  STRING |
| **amendmentId**  STRING |
| **amount**  DOUBLE |
| **billToContactId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **currency**  STRING |
| **defaultPaymentMethodId**  STRING |
| **deferredRevenueAccountingCodeId**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **invoiceId**  STRING |
| **invoiceItemId**  STRING |
| **journalEntryId**  STRING |
| **journalRunId**  STRING |
| **parentAccountId**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **recognizedRevenueAccountingCodeId**  STRING |
| **revenueChargeSummaryId**  STRING |
| **revenueEventId**  STRING |
| **revenueEventInvoiceId**  STRING |
| **revenueEventTypeId**  STRING |
| **revenueScheduleId**  STRING |
| **soldToContactId**  STRING |
| **subscriptionId**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### RevenueEventItemInvoiceItemAdjustment

The `RevenueEventItemInvoiceItemAdjustment` table contains information about revenue event items that are associated with invoice item adjustments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/older-api/tag/Revenue-Events/) |

RevenueEventItemInvoiceItemAdjustment table foreign keys

| Join RevenueEventItemInvoiceItemAdjustment with | on |
| --- | --- |
| [AccountingPeriod](#accountingperiod) | ``` RevenueEventItemInvoiceItemAdjustment.accountingPeriodId = AccountingPeriod.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` RevenueEventItemInvoiceItemAdjustment.accountingPeriodId = CreditBalanceAdjustment.accountingPeriodId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.journalEntryId = CreditBalanceAdjustment.journalEntryId ```  ``` RevenueEventItemInvoiceItemAdjustment.journalRunId = CreditBalanceAdjustment.journalRunId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` RevenueEventItemInvoiceItemAdjustment.accountingPeriodId = InvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.invoiceItemAdjustmentId = InvoiceItemAdjustment.id ```  ``` RevenueEventItemInvoiceItemAdjustment.journalEntryId = InvoiceItemAdjustment.journalEntryId ```  ``` RevenueEventItemInvoiceItemAdjustment.journalRunId = InvoiceItemAdjustment.journalRunId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = InvoiceItemAdjustment.parentAccountId ```  ``` RevenueEventItemInvoiceItemAdjustment.productId = InvoiceItemAdjustment.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = InvoiceItemAdjustment.ratePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = InvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = InvoiceItemAdjustment.subscriptionId ``` |
| [JournalEntry](#journalentry) | ``` RevenueEventItemInvoiceItemAdjustment.accountingPeriodId = JournalEntry.accountingPeriodId ```  ``` RevenueEventItemInvoiceItemAdjustment.journalEntryId = JournalEntry.id ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` RevenueEventItemInvoiceItemAdjustment.accountingPeriodId = RevenueChargeSummaryItem.accountingPeriodId ```  ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = RevenueChargeSummaryItem.parentAccountId ```  ``` RevenueEventItemInvoiceItemAdjustment.productId = RevenueChargeSummaryItem.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = RevenueChargeSummaryItem.ratePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueChargeSummaryItem.revenueChargeSummaryId ```  ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` RevenueEventItemInvoiceItemAdjustment.accountingPeriodId = RevenueEventItemInvoiceItem.accountingPeriodId ```  ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.invoiceItemId = RevenueEventItemInvoiceItem.invoiceItemId ```  ``` RevenueEventItemInvoiceItemAdjustment.journalEntryId = RevenueEventItemInvoiceItem.journalEntryId ```  ``` RevenueEventItemInvoiceItemAdjustment.journalRunId = RevenueEventItemInvoiceItem.journalRunId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ```  ``` RevenueEventItemInvoiceItemAdjustment.productId = RevenueEventItemInvoiceItem.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueEventItemInvoiceItem.revenueChargeSummaryId ```  ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` RevenueEventItemInvoiceItemAdjustment.accountingPeriodId = RevenueScheduleItem.accountingPeriodId ```  ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = RevenueScheduleItem.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = RevenueScheduleItem.deferredRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = RevenueScheduleItem.parentAccountId ```  ``` RevenueEventItemInvoiceItemAdjustment.productId = RevenueScheduleItem.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = RevenueScheduleItem.ratePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueScheduleItem.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueScheduleItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` RevenueEventItemInvoiceItemAdjustment.accountingPeriodId = RevenueScheduleItemInvoiceItem.accountingPeriodId ```  ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.invoiceItemId = RevenueScheduleItemInvoiceItem.invoiceItemId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ```  ``` RevenueEventItemInvoiceItemAdjustment.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueScheduleItemInvoiceItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` RevenueEventItemInvoiceItemAdjustment.accountingPeriodId = RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.invoiceItemAdjustmentId = RevenueScheduleItemInvoiceItemAdjustment.invoiceItemAdjustmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.invoiceItemId = RevenueScheduleItemInvoiceItemAdjustment.invoiceItemId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueEventItemInvoiceItemAdjustment.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId ```  ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |
| [Amendment](#amendment) | ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = Amendment.id ```  ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = Amendment.subscriptionId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = DiscountAppliedMetrics.parentAccountId ```  ``` RevenueEventItemInvoiceItemAdjustment.productId = DiscountAppliedMetrics.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = DiscountAppliedMetrics.ratePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = DiscountAppliedMetrics.subscriptionId ``` |
| [ProcessedUsage](#processedusage) | ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = ProcessedUsage.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = ProcessedUsage.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = ProcessedUsage.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.invoiceItemId = ProcessedUsage.invoiceItemId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = ProcessedUsage.parentAccountId ```  ``` RevenueEventItemInvoiceItemAdjustment.productId = ProcessedUsage.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = RatePlan.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RatePlan.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RatePlan.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = RatePlan.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = RatePlan.id ```  ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = RatePlan.subscriptionId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = RatePlanChargeTier.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = RatePlanChargeTier.ratePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = RatePlanChargeTier.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` RevenueEventItemInvoiceItemAdjustment.amendmentId = RevenueEventItem.amendmentId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueEventItem.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueEventItem.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = RevenueEventItem.deferredRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.journalEntryId = RevenueEventItem.journalEntryId ```  ``` RevenueEventItemInvoiceItemAdjustment.journalRunId = RevenueEventItem.journalRunId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = RevenueEventItem.parentAccountId ```  ``` RevenueEventItemInvoiceItemAdjustment.productId = RevenueEventItem.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = RevenueEventItem.ratePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueEventItem.recognizedRevenueAccountingCodeId ```  ``` RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueEventItem.revenueChargeSummaryId ```  ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = RevenueEventItem.subscriptionId ``` |
| [Account](#account) | ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = Account.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = Account.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = Account.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = Account.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = Account.id ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = Contact.id ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = ContactSnapshot.contactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = ContactSnapshot.contactId ``` |
| [Invoice](#invoice) | ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = Invoice.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = Invoice.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = Invoice.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = Invoice.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = Invoice.parentAccountId ``` |
| [Refund](#refund) | ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = Refund.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = Refund.billToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.billToContactId = Refund.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.soldToContactId = Refund.soldToContactId ```  ``` RevenueEventItemInvoiceItemAdjustment.parentAccountId = Refund.parentAccountId ``` |
| [InvoiceItem](#invoiceitem) | ``` RevenueEventItemInvoiceItemAdjustment.invoiceItemId = InvoiceItem.id ```  ``` RevenueEventItemInvoiceItemAdjustment.productId = InvoiceItem.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = InvoiceItem.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = InvoiceItem.subscriptionId ``` |
| [JournalEntryItem](#journalentryitem) | ``` RevenueEventItemInvoiceItemAdjustment.journalEntryId = JournalEntryItem.journalEntryId ```  ``` RevenueEventItemInvoiceItemAdjustment.journalRunId = JournalEntryItem.journalRunId ``` |
| [JournalRun](#journalrun) | ``` RevenueEventItemInvoiceItemAdjustment.journalRunId = JournalRun.id ``` |
| [Product](#product) | ``` RevenueEventItemInvoiceItemAdjustment.productId = Product.id ``` |
| [ProductRatePlan](#productrateplan) | ``` RevenueEventItemInvoiceItemAdjustment.productId = ProductRatePlan.productId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = ProductRatePlanCharge.id ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` RevenueEventItemInvoiceItemAdjustment.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId = RatePlanCharge.id ``` |
| [AccountingCode](#accountingcode) | ``` RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = AccountingCode.id ``` |
| [Subscription](#subscription) | ``` RevenueEventItemInvoiceItemAdjustment.subscriptionId = Subscription.id ``` |

RevenueEventItemInvoiceItemAdjustment table schema

|  |
| --- |
| **accountId**  STRING |
| **accountingPeriodId**  STRING |
| **amendmentId**  STRING |
| **amount**  DOUBLE |
| **billToContactId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **currency**  STRING |
| **defaultPaymentMethodId**  STRING |
| **deferredRevenueAccountingCodeId**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **invoiceId**  STRING |
| **invoiceItemAdjustmentId**  STRING |
| **invoiceItemId**  STRING |
| **journalEntryId**  STRING |
| **journalRunId**  STRING |
| **parentAccountId**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **recognizedRevenueAccountingCodeId**  STRING |
| **revenueChargeSummaryId**  STRING |
| **revenueEventInvoiceId**  STRING |
| **revenueEventInvoiceItemAdjustmentId**  STRING |
| **revenueEventTypeId**  STRING |
| **revenueScheduleInvoiceItemAdjustmentId**  STRING |
| **soldToContactId**  STRING |
| **subscriptionId**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### RevenueScheduleItem

The `RevenueScheduleItem` table contains information about revenue schedules. A [revenue schedule](https://knowledgecenter.zuora.com/CC_Finance/Revenue_Recognition/G_Revenue_Schedules) represents how revenue amounts from single charges are distributed over time and recognized in accounting periods.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/older-api/tag/Revenue-Items/) |

RevenueScheduleItem table foreign keys

| Join RevenueScheduleItem with | on |
| --- | --- |
| [AccountingPeriod](#accountingperiod) | ``` RevenueScheduleItem.accountingPeriodId = AccountingPeriod.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` RevenueScheduleItem.accountingPeriodId = CreditBalanceAdjustment.accountingPeriodId ```  ``` RevenueScheduleItem.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueScheduleItem.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueScheduleItem.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` RevenueScheduleItem.accountingPeriodId = InvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueScheduleItem.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` RevenueScheduleItem.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItem.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItem.parentAccountId = InvoiceItemAdjustment.parentAccountId ```  ``` RevenueScheduleItem.productId = InvoiceItemAdjustment.productId ```  ``` RevenueScheduleItem.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueScheduleItem.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = InvoiceItemAdjustment.ratePlanId ```  ``` RevenueScheduleItem.recognizedRevenueAccountingCodeId = InvoiceItemAdjustment.recognizedRevenueAccountingCodeId ``` |
| [JournalEntry](#journalentry) | ``` RevenueScheduleItem.accountingPeriodId = JournalEntry.accountingPeriodId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` RevenueScheduleItem.accountingPeriodId = RevenueChargeSummaryItem.accountingPeriodId ```  ``` RevenueScheduleItem.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` RevenueScheduleItem.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueScheduleItem.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueScheduleItem.parentAccountId = RevenueChargeSummaryItem.parentAccountId ```  ``` RevenueScheduleItem.productId = RevenueChargeSummaryItem.productId ```  ``` RevenueScheduleItem.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` RevenueScheduleItem.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = RevenueChargeSummaryItem.ratePlanId ```  ``` RevenueScheduleItem.revenueChargeSummaryId = RevenueChargeSummaryItem.revenueChargeSummaryId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` RevenueScheduleItem.accountingPeriodId = RevenueEventItemInvoiceItem.accountingPeriodId ```  ``` RevenueScheduleItem.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` RevenueScheduleItem.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueScheduleItem.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueScheduleItem.deferredRevenueAccountingCodeId = RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItem.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ```  ``` RevenueScheduleItem.productId = RevenueEventItemInvoiceItem.productId ```  ``` RevenueScheduleItem.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueScheduleItem.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ```  ``` RevenueScheduleItem.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItem.revenueChargeSummaryId = RevenueEventItemInvoiceItem.revenueChargeSummaryId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` RevenueScheduleItem.accountingPeriodId = RevenueEventItemInvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueScheduleItem.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueScheduleItem.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItem.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItem.deferredRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItem.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueScheduleItem.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` RevenueScheduleItem.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueScheduleItem.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueScheduleItem.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItem.revenueChargeSummaryId = RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` RevenueScheduleItem.accountingPeriodId = RevenueScheduleItemInvoiceItem.accountingPeriodId ```  ``` RevenueScheduleItem.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` RevenueScheduleItem.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueScheduleItem.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueScheduleItem.deferredRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItem.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ```  ``` RevenueScheduleItem.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` RevenueScheduleItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueScheduleItem.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ```  ``` RevenueScheduleItem.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItem.revenueChargeSummaryId = RevenueScheduleItemInvoiceItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` RevenueScheduleItem.accountingPeriodId = RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueScheduleItem.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueScheduleItem.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItem.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItem.deferredRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItem.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueScheduleItem.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` RevenueScheduleItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueScheduleItem.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueScheduleItem.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItem.revenueChargeSummaryId = RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId ``` |
| [Amendment](#amendment) | ``` RevenueScheduleItem.amendmentId = Amendment.id ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` RevenueScheduleItem.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` RevenueScheduleItem.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueScheduleItem.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueScheduleItem.parentAccountId = DiscountAppliedMetrics.parentAccountId ```  ``` RevenueScheduleItem.productId = DiscountAppliedMetrics.productId ```  ``` RevenueScheduleItem.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` RevenueScheduleItem.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = DiscountAppliedMetrics.ratePlanId ``` |
| [ProcessedUsage](#processedusage) | ``` RevenueScheduleItem.amendmentId = ProcessedUsage.amendmentId ```  ``` RevenueScheduleItem.billToContactId = ProcessedUsage.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = ProcessedUsage.billToContactId ```  ``` RevenueScheduleItem.billToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueScheduleItem.parentAccountId = ProcessedUsage.parentAccountId ```  ``` RevenueScheduleItem.productId = ProcessedUsage.productId ```  ``` RevenueScheduleItem.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` RevenueScheduleItem.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` RevenueScheduleItem.amendmentId = RatePlan.amendmentId ```  ``` RevenueScheduleItem.billToContactId = RatePlan.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = RatePlan.billToContactId ```  ``` RevenueScheduleItem.productRatePlanId = RatePlan.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanId = RatePlan.id ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` RevenueScheduleItem.amendmentId = RatePlanChargeTier.amendmentId ```  ``` RevenueScheduleItem.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = RatePlanChargeTier.ratePlanId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` RevenueScheduleItem.amendmentId = RevenueEventItem.amendmentId ```  ``` RevenueScheduleItem.billToContactId = RevenueEventItem.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueEventItem.billToContactId ```  ``` RevenueScheduleItem.billToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueScheduleItem.deferredRevenueAccountingCodeId = RevenueEventItem.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItem.parentAccountId = RevenueEventItem.parentAccountId ```  ``` RevenueScheduleItem.productId = RevenueEventItem.productId ```  ``` RevenueScheduleItem.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` RevenueScheduleItem.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = RevenueEventItem.ratePlanId ```  ``` RevenueScheduleItem.recognizedRevenueAccountingCodeId = RevenueEventItem.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItem.revenueChargeSummaryId = RevenueEventItem.revenueChargeSummaryId ``` |
| [Account](#account) | ``` RevenueScheduleItem.billToContactId = Account.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = Account.billToContactId ```  ``` RevenueScheduleItem.billToContactId = Account.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = Account.soldToContactId ```  ``` RevenueScheduleItem.deferredRevenueAccountingCodeId = Account.id ```  ``` RevenueScheduleItem.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` RevenueScheduleItem.billToContactId = Contact.id ```  ``` RevenueScheduleItem.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` RevenueScheduleItem.billToContactId = ContactSnapshot.contactId ```  ``` RevenueScheduleItem.soldToContactId = ContactSnapshot.contactId ``` |
| [Invoice](#invoice) | ``` RevenueScheduleItem.billToContactId = Invoice.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = Invoice.billToContactId ```  ``` RevenueScheduleItem.billToContactId = Invoice.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = Invoice.soldToContactId ```  ``` RevenueScheduleItem.parentAccountId = Invoice.parentAccountId ``` |
| [Refund](#refund) | ``` RevenueScheduleItem.billToContactId = Refund.billToContactId ```  ``` RevenueScheduleItem.soldToContactId = Refund.billToContactId ```  ``` RevenueScheduleItem.billToContactId = Refund.soldToContactId ```  ``` RevenueScheduleItem.soldToContactId = Refund.soldToContactId ```  ``` RevenueScheduleItem.parentAccountId = Refund.parentAccountId ``` |
| [Product](#product) | ``` RevenueScheduleItem.productId = Product.id ``` |
| [InvoiceItem](#invoiceitem) | ``` RevenueScheduleItem.productId = InvoiceItem.productId ```  ``` RevenueScheduleItem.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` RevenueScheduleItem.ratePlanChargeId = InvoiceItem.ratePlanChargeId ``` |
| [ProductRatePlan](#productrateplan) | ``` RevenueScheduleItem.productId = ProductRatePlan.productId ```  ``` RevenueScheduleItem.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` RevenueScheduleItem.productRatePlanChargeId = ProductRatePlanCharge.id ```  ``` RevenueScheduleItem.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` RevenueScheduleItem.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` RevenueScheduleItem.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` RevenueScheduleItem.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` RevenueScheduleItem.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` RevenueScheduleItem.ratePlanChargeId = RatePlanCharge.id ``` |
| [AccountingCode](#accountingcode) | ``` RevenueScheduleItem.recognizedRevenueAccountingCodeId = AccountingCode.id ``` |

RevenueScheduleItem table schema

|  |
| --- |
| **accountId**  STRING |
| **accountingPeriodId**  STRING |
| **amendmentId**  STRING |
| **amount**  DOUBLE |
| **billToContactId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **currency**  STRING |
| **defaultPaymentMethodId**  STRING |
| **deferredRevenueAccountingCodeId**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **parentAccountId**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **recognizedRevenueAccountingCodeId**  STRING |
| **revenueChargeSummaryId**  STRING |
| **revenueEventId**  STRING |
| **revenueEventTypeId**  STRING |
| **revenueScheduleId**  STRING |
| **soldToContactId**  STRING |
| **subscription**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### RevenueScheduleItemInvoiceItem

The `RevenueScheduleItemInvoiceItem` table contains information about revenue schedule item - invoice items.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/older-api/tag/Revenue-Items/) |

RevenueScheduleItemInvoiceItem table foreign keys

| Join RevenueScheduleItemInvoiceItem with | on |
| --- | --- |
| [AccountingPeriod](#accountingperiod) | ``` RevenueScheduleItemInvoiceItem.accountingPeriodId = AccountingPeriod.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` RevenueScheduleItemInvoiceItem.accountingPeriodId = CreditBalanceAdjustment.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` RevenueScheduleItemInvoiceItem.accountingPeriodId = InvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItem.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = InvoiceItemAdjustment.parentAccountId ```  ``` RevenueScheduleItemInvoiceItem.productId = InvoiceItemAdjustment.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = InvoiceItemAdjustment.ratePlanId ```  ``` RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId = InvoiceItemAdjustment.recognizedRevenueAccountingCodeId ``` |
| [JournalEntry](#journalentry) | ``` RevenueScheduleItemInvoiceItem.accountingPeriodId = JournalEntry.accountingPeriodId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` RevenueScheduleItemInvoiceItem.accountingPeriodId = RevenueChargeSummaryItem.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItem.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = RevenueChargeSummaryItem.parentAccountId ```  ``` RevenueScheduleItemInvoiceItem.productId = RevenueChargeSummaryItem.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = RevenueChargeSummaryItem.ratePlanId ```  ``` RevenueScheduleItemInvoiceItem.revenueChargeSummaryId = RevenueChargeSummaryItem.revenueChargeSummaryId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` RevenueScheduleItemInvoiceItem.accountingPeriodId = RevenueEventItemInvoiceItem.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItem.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId = RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItem.invoiceItemId = RevenueEventItemInvoiceItem.invoiceItemId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ```  ``` RevenueScheduleItemInvoiceItem.productId = RevenueEventItemInvoiceItem.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ```  ``` RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItem.revenueChargeSummaryId = RevenueEventItemInvoiceItem.revenueChargeSummaryId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` RevenueScheduleItemInvoiceItem.accountingPeriodId = RevenueEventItemInvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItem.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItem.invoiceItemId = RevenueEventItemInvoiceItemAdjustment.invoiceItemId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueScheduleItemInvoiceItem.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItem.revenueChargeSummaryId = RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` RevenueScheduleItemInvoiceItem.accountingPeriodId = RevenueScheduleItem.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItem.amendmentId = RevenueScheduleItem.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId = RevenueScheduleItem.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = RevenueScheduleItem.parentAccountId ```  ``` RevenueScheduleItemInvoiceItem.productId = RevenueScheduleItem.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = RevenueScheduleItem.ratePlanId ```  ``` RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId = RevenueScheduleItem.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItem.revenueChargeSummaryId = RevenueScheduleItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` RevenueScheduleItemInvoiceItem.accountingPeriodId = RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItem.amendmentId = RevenueScheduleItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueScheduleItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItem.invoiceItemId = RevenueScheduleItemInvoiceItemAdjustment.invoiceItemId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = RevenueScheduleItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueScheduleItemInvoiceItem.productId = RevenueScheduleItemInvoiceItemAdjustment.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = RevenueScheduleItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItem.revenueChargeSummaryId = RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId ``` |
| [Amendment](#amendment) | ``` RevenueScheduleItemInvoiceItem.amendmentId = Amendment.id ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` RevenueScheduleItemInvoiceItem.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = DiscountAppliedMetrics.parentAccountId ```  ``` RevenueScheduleItemInvoiceItem.productId = DiscountAppliedMetrics.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = DiscountAppliedMetrics.ratePlanId ``` |
| [ProcessedUsage](#processedusage) | ``` RevenueScheduleItemInvoiceItem.amendmentId = ProcessedUsage.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = ProcessedUsage.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = ProcessedUsage.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.invoiceItemId = ProcessedUsage.invoiceItemId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = ProcessedUsage.parentAccountId ```  ``` RevenueScheduleItemInvoiceItem.productId = ProcessedUsage.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` RevenueScheduleItemInvoiceItem.amendmentId = RatePlan.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RatePlan.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RatePlan.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = RatePlan.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = RatePlan.id ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` RevenueScheduleItemInvoiceItem.amendmentId = RatePlanChargeTier.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = RatePlanChargeTier.ratePlanId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` RevenueScheduleItemInvoiceItem.amendmentId = RevenueEventItem.amendmentId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueEventItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueEventItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId = RevenueEventItem.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = RevenueEventItem.parentAccountId ```  ``` RevenueScheduleItemInvoiceItem.productId = RevenueEventItem.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = RevenueEventItem.ratePlanId ```  ``` RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId = RevenueEventItem.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItem.revenueChargeSummaryId = RevenueEventItem.revenueChargeSummaryId ``` |
| [Account](#account) | ``` RevenueScheduleItemInvoiceItem.billToContactId = Account.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = Account.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = Account.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = Account.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId = Account.id ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` RevenueScheduleItemInvoiceItem.billToContactId = Contact.id ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` RevenueScheduleItemInvoiceItem.billToContactId = ContactSnapshot.contactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = ContactSnapshot.contactId ``` |
| [Invoice](#invoice) | ``` RevenueScheduleItemInvoiceItem.billToContactId = Invoice.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = Invoice.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = Invoice.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = Invoice.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = Invoice.parentAccountId ``` |
| [Refund](#refund) | ``` RevenueScheduleItemInvoiceItem.billToContactId = Refund.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = Refund.billToContactId ```  ``` RevenueScheduleItemInvoiceItem.billToContactId = Refund.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.soldToContactId = Refund.soldToContactId ```  ``` RevenueScheduleItemInvoiceItem.parentAccountId = Refund.parentAccountId ``` |
| [InvoiceItem](#invoiceitem) | ``` RevenueScheduleItemInvoiceItem.invoiceItemId = InvoiceItem.id ```  ``` RevenueScheduleItemInvoiceItem.productId = InvoiceItem.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = InvoiceItem.ratePlanChargeId ``` |
| [Product](#product) | ``` RevenueScheduleItemInvoiceItem.productId = Product.id ``` |
| [ProductRatePlan](#productrateplan) | ``` RevenueScheduleItemInvoiceItem.productId = ProductRatePlan.productId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = ProductRatePlanCharge.id ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` RevenueScheduleItemInvoiceItem.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItem.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` RevenueScheduleItemInvoiceItem.ratePlanChargeId = RatePlanCharge.id ``` |
| [AccountingCode](#accountingcode) | ``` RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId = AccountingCode.id ``` |

RevenueScheduleItemInvoiceItem table schema

|  |
| --- |
| **accountId**  STRING |
| **accountingPeriodId**  STRING |
| **amendmentId**  STRING |
| **amount**  DOUBLE |
| **billToContactId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **currency**  STRING |
| **defaultPaymentMethodId**  STRING |
| **deferredRevenueAccountingCodeId**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **invoiceId**  STRING |
| **invoiceItemId**  STRING |
| **parentAccountId**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **recognizedRevenueAccountingCodeId**  STRING |
| **revenueChargeSummaryId**  STRING |
| **revenueScheduleInvoiceItemId**  STRING |
| **soldToContactId**  STRING |
| **subscription**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### RevenueScheduleItemInvoiceItemAdjustment

The `RevenueScheduleItemInvoiceItemAdjustment` table contains information about revenue schedule item - invoice items.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/older-api/tag/Revenue-Items/) |

RevenueScheduleItemInvoiceItemAdjustment table foreign keys

| Join RevenueScheduleItemInvoiceItemAdjustment with | on |
| --- | --- |
| [AccountingPeriod](#accountingperiod) | ``` RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId = AccountingPeriod.id ``` |
| [CreditBalanceAdjustment](#creditbalanceadjustment) | ``` RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId = CreditBalanceAdjustment.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = CreditBalanceAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = CreditBalanceAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = CreditBalanceAdjustment.parentAccountId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId = InvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = InvoiceItemAdjustment.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = InvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = InvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.invoiceItemAdjustmentId = InvoiceItemAdjustment.id ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = InvoiceItemAdjustment.parentAccountId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productId = InvoiceItemAdjustment.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = InvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = InvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = InvoiceItemAdjustment.ratePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = InvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = InvoiceItemAdjustment.subscriptionId ``` |
| [JournalEntry](#journalentry) | ``` RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId = JournalEntry.accountingPeriodId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId = RevenueChargeSummaryItem.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = RevenueChargeSummaryItem.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueChargeSummaryItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueChargeSummaryItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = RevenueChargeSummaryItem.parentAccountId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productId = RevenueChargeSummaryItem.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueChargeSummaryItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = RevenueChargeSummaryItem.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = RevenueChargeSummaryItem.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = RevenueChargeSummaryItem.ratePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueChargeSummaryItem.revenueChargeSummaryId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId = RevenueEventItemInvoiceItem.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = RevenueEventItemInvoiceItem.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueEventItemInvoiceItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueEventItemInvoiceItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = RevenueEventItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.invoiceItemId = RevenueEventItemInvoiceItem.invoiceItemId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = RevenueEventItemInvoiceItem.parentAccountId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productId = RevenueEventItemInvoiceItem.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueEventItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = RevenueEventItemInvoiceItem.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = RevenueEventItemInvoiceItem.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = RevenueEventItemInvoiceItem.ratePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueEventItemInvoiceItem.revenueChargeSummaryId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId = RevenueEventItemInvoiceItemAdjustment.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = RevenueEventItemInvoiceItemAdjustment.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueEventItemInvoiceItemAdjustment.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueEventItemInvoiceItemAdjustment.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.invoiceItemAdjustmentId = RevenueEventItemInvoiceItemAdjustment.invoiceItemAdjustmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.invoiceItemId = RevenueEventItemInvoiceItemAdjustment.invoiceItemId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = RevenueEventItemInvoiceItemAdjustment.parentAccountId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productId = RevenueEventItemInvoiceItemAdjustment.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueEventItemInvoiceItemAdjustment.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = RevenueEventItemInvoiceItemAdjustment.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = RevenueEventItemInvoiceItemAdjustment.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = RevenueEventItemInvoiceItemAdjustment.ratePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueEventItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueEventItemInvoiceItemAdjustment.revenueChargeSummaryId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItem](#revenuescheduleitem) | ``` RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId = RevenueScheduleItem.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = RevenueScheduleItem.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueScheduleItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueScheduleItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = RevenueScheduleItem.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = RevenueScheduleItem.parentAccountId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productId = RevenueScheduleItem.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueScheduleItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = RevenueScheduleItem.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = RevenueScheduleItem.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = RevenueScheduleItem.ratePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueScheduleItem.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueScheduleItem.revenueChargeSummaryId ``` |
| [RevenueScheduleItemInvoiceItem](#revenuescheduleiteminvoiceitem) | ``` RevenueScheduleItemInvoiceItemAdjustment.accountingPeriodId = RevenueScheduleItemInvoiceItem.accountingPeriodId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = RevenueScheduleItemInvoiceItem.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueScheduleItemInvoiceItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueScheduleItemInvoiceItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.invoiceItemId = RevenueScheduleItemInvoiceItem.invoiceItemId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = RevenueScheduleItemInvoiceItem.parentAccountId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productId = RevenueScheduleItemInvoiceItem.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueScheduleItemInvoiceItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = RevenueScheduleItemInvoiceItem.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = RevenueScheduleItemInvoiceItem.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = RevenueScheduleItemInvoiceItem.ratePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueScheduleItemInvoiceItem.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueScheduleItemInvoiceItem.revenueChargeSummaryId ``` |
| [Amendment](#amendment) | ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = Amendment.id ```  ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = Amendment.subscriptionId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = DiscountAppliedMetrics.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = DiscountAppliedMetrics.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = DiscountAppliedMetrics.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = DiscountAppliedMetrics.parentAccountId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productId = DiscountAppliedMetrics.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = DiscountAppliedMetrics.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = DiscountAppliedMetrics.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = DiscountAppliedMetrics.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = DiscountAppliedMetrics.ratePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = DiscountAppliedMetrics.subscriptionId ``` |
| [ProcessedUsage](#processedusage) | ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = ProcessedUsage.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = ProcessedUsage.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = ProcessedUsage.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = ProcessedUsage.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.invoiceItemId = ProcessedUsage.invoiceItemId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = ProcessedUsage.parentAccountId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productId = ProcessedUsage.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = ProcessedUsage.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = ProcessedUsage.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = ProcessedUsage.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = ProcessedUsage.ratePlanId ``` |
| [RatePlan](#rateplan) | ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = RatePlan.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RatePlan.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RatePlan.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = RatePlan.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = RatePlan.id ```  ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = RatePlan.subscriptionId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = RatePlanChargeTier.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = RatePlanChargeTier.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = RatePlanChargeTier.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = RatePlanChargeTier.ratePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = RatePlanChargeTier.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` RevenueScheduleItemInvoiceItemAdjustment.amendmentId = RevenueEventItem.amendmentId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueEventItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueEventItem.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = RevenueEventItem.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = RevenueEventItem.deferredRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = RevenueEventItem.parentAccountId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productId = RevenueEventItem.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = RevenueEventItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = RevenueEventItem.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = RevenueEventItem.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = RevenueEventItem.ratePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = RevenueEventItem.recognizedRevenueAccountingCodeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.revenueChargeSummaryId = RevenueEventItem.revenueChargeSummaryId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = RevenueEventItem.subscriptionId ``` |
| [Account](#account) | ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = Account.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = Account.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = Account.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = Account.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.deferredRevenueAccountingCodeId = Account.id ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = Account.parentAccountId ``` |
| [Contact](#contact) | ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = Contact.id ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = Contact.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = ContactSnapshot.contactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = ContactSnapshot.contactId ``` |
| [Invoice](#invoice) | ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = Invoice.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = Invoice.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = Invoice.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = Invoice.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = Invoice.parentAccountId ``` |
| [Refund](#refund) | ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = Refund.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = Refund.billToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.billToContactId = Refund.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.soldToContactId = Refund.soldToContactId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.parentAccountId = Refund.parentAccountId ``` |
| [InvoiceItem](#invoiceitem) | ``` RevenueScheduleItemInvoiceItemAdjustment.invoiceItemId = InvoiceItem.id ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productId = InvoiceItem.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = InvoiceItem.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = InvoiceItem.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = InvoiceItem.subscriptionId ``` |
| [Product](#product) | ``` RevenueScheduleItemInvoiceItemAdjustment.productId = Product.id ``` |
| [ProductRatePlan](#productrateplan) | ``` RevenueScheduleItemInvoiceItemAdjustment.productId = ProductRatePlan.productId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = ProductRatePlan.id ``` |
| [ProductRatePlanCharge](#productrateplancharge) | ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = ProductRatePlanCharge.id ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = ProductRatePlanCharge.productRatePlanId ``` |
| [ProductRatePlanChargeTier](#productrateplanchargetier) | ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanChargeId = ProductRatePlanChargeTier.productRatePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.productRatePlanId = ProductRatePlanChargeTier.productRatePlanId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = ProductRatePlanChargeTier.ratePlanChargeId ```  ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanId = ProductRatePlanChargeTier.ratePlanId ``` |
| [RatePlanCharge](#rateplancharge) | ``` RevenueScheduleItemInvoiceItemAdjustment.ratePlanChargeId = RatePlanCharge.id ``` |
| [AccountingCode](#accountingcode) | ``` RevenueScheduleItemInvoiceItemAdjustment.recognizedRevenueAccountingCodeId = AccountingCode.id ``` |
| [Subscription](#subscription) | ``` RevenueScheduleItemInvoiceItemAdjustment.subscriptionId = Subscription.id ``` |

RevenueScheduleItemInvoiceItemAdjustment table schema

|  |
| --- |
| **accountId**  STRING |
| **accountingPeriodId**  STRING |
| **amendmentId**  STRING |
| **amount**  DOUBLE |
| **billToContactId**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **currency**  STRING |
| **defaultPaymentMethodId**  STRING |
| **deferredRevenueAccountingCodeId**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **invoiceId**  STRING |
| **invoiceItemAdjustmentId**  STRING |
| **invoiceItemId**  STRING |
| **parentAccountId**  STRING |
| **productId**  STRING |
| **productRatePlanChargeId**  STRING |
| **productRatePlanId**  STRING |
| **ratePlanChargeId**  STRING |
| **ratePlanId**  STRING |
| **recognizedRevenueAccountingCodeId**  STRING |
| **revenueChargeSummaryId**  STRING |
| **revenueScheduleInvoiceItemAdjustmentId**  STRING |
| **soldToContactId**  STRING |
| **subscriptionId**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |

### Subscription

The `Subscription` table contains info about your products and/or services with recurring charges.

### Custom Attributes

If your Zuora subscription records contain custom attributes, they will be replicated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedDate |
| **Useful links** | [Zuora documentation](https://developer.zuora.com/v1-api-reference/api/tag/Subscriptions/) |

Subscription table foreign keys

| Join Subscription with | on |
| --- | --- |
| [Account](#account) | ``` Subscription.accountId = Account.id ``` |
| [ContactSnapshot](#contactsnapshot) | ``` Subscription.accountId = ContactSnapshot.accountId ``` |
| [Invoice](#invoice) | ``` Subscription.accountId = Invoice.accountId ``` |
| [Payment](#payment) | ``` Subscription.accountId = Payment.accountId ``` |
| [Refund](#refund) | ``` Subscription.accountId = Refund.accountId ``` |
| [Amendment](#amendment) | ``` Subscription.id = Amendment.subscriptionId ``` |
| [DiscountAppliedMetrics](#discountappliedmetrics) | ``` Subscription.id = DiscountAppliedMetrics.subscriptionId ``` |
| [InvoiceItem](#invoiceitem) | ``` Subscription.id = InvoiceItem.subscriptionId ``` |
| [InvoiceItemAdjustment](#invoiceitemadjustment) | ``` Subscription.id = InvoiceItemAdjustment.subscriptionId ``` |
| [RatePlan](#rateplan) | ``` Subscription.id = RatePlan.subscriptionId ``` |
| [RatePlanChargeTier](#rateplanchargetier) | ``` Subscription.id = RatePlanChargeTier.subscriptionId ``` |
| [RevenueChargeSummaryItem](#revenuechargesummaryitem) | ``` Subscription.id = RevenueChargeSummaryItem.subscriptionId ``` |
| [RevenueEventItem](#revenueeventitem) | ``` Subscription.id = RevenueEventItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItem](#revenueeventiteminvoiceitem) | ``` Subscription.id = RevenueEventItemInvoiceItem.subscriptionId ``` |
| [RevenueEventItemInvoiceItemAdjustment](#revenueeventiteminvoiceitemadjustment) | ``` Subscription.id = RevenueEventItemInvoiceItemAdjustment.subscriptionId ``` |
| [RevenueScheduleItemInvoiceItemAdjustment](#revenuescheduleiteminvoiceitemadjustment) | ``` Subscription.id = RevenueScheduleItemInvoiceItemAdjustment.subscriptionId ``` |

Subscription table schema

|  |
| --- |
| **accountId**  STRING |
| **autoRenew**  BOOLEAN |
| **cancelledDate**  DATE-TIME |
| **contractAcceptanceDate**  DATE-TIME |
| **contractEffectiveDate**  DATE-TIME |
| **cpqBundleJsonId\_\_qt**  STRING |
| **createdById**  STRING |
| **createdDate**  DATE-TIME |
| **creatorAccountId**  STRING |
| **creatorInvoiceOwnerId**  STRING |
| **currentTerm**  INTEGER |
| **currentTermPeriodType**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **initialTerm**  INTEGER |
| **initialTermPeriodType**  STRING |
| **invoiceOwnerId**  STRING |
| **isInvoiceSeparate**  BOOLEAN |
| **name**  STRING |
| **notes**  STRING |
| **opportunityCloseDate\_\_qt**  DATE-TIME |
| **opportunityName\_qt**  STRING |
| **originalCreatedDate**  DATE-TIME |
| **originalId**  STRING |
| **previousSubscriptionId**  STRING |
| **quoteBusinessType\_\_qt**  STRING |
| **quoteNumber\_\_qt**  STRING |
| **quoteType\_\_at**  STRING |
| **renewalSetting**  STRING |
| **renewalTerm**  INTEGER |
| **renewalTermPeriodType**  STRING |
| **serviceActivationDate**  DATE-TIME |
| **status**  STRING |
| **subscriptionEndDate**  DATE-TIME |
| **subscriptionStartDate**  DATE-TIME |
| **termEndDate**  DATE-TIME |
| **termStartDate**  DATE-TIME |
| **termType**  STRING |
| **updatedById**  STRING |
| **updatedDate**  DATE-TIME |
