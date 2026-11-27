---
title: "SAP Cloud for Customer V2"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SAP-Cloud-for-customerV2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# SAP Cloud for Customer V2

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

SAP Cloud for Customer is a SaaS platform for sales and service enablement. You can use SAP Cloud for Customer as a data source when landing or replicating data.

SAP Cloud for Customer integration replicates data using the [SAP Cloud for Customer OData API](https://help.sap.com/docs/sap-cloud-for-customer/odata-services/sap-cloud-for-customer-odata-api).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

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
| Username | Your user name in SAP Cloud for Customer. |
| Password | Your password in SAP Cloud for Customer. |
| OData URL | The OData discovery URL for your SAP Cloud for Customer tenant. Examples:   - Standard OData service: `https://<tenant>.crm.ondemand.com/sap/c4c/odata/v1/c4codataapi/` - Custom OData service: `https://<tenant>.crm.ondemand.com/sap/c4c/odata/cust/v1/<servicename>/`   Information noteChange data capture (CDC) is only supported when using the standard OData service URL (`c4codataapi`). Custom OData service URLs expose different entities and do not support CDC. |

## Schema

Information note

Schemas and naming conventions can change from version to version. Verify your version before continuing.

The schema information displayed below is for version 2.

The available datasets depend on your SAP Cloud for Customer source tenant configuration. Datasets are discovered dynamically using the `https://<tenant>.crm.ondemand.com/sap/c4c/odata/v1/c4codataapi` endpoint.

Depending on your destination, table and column names may not appear as they are outlined below.

### ActivityCollection

The `ActivityCollection` table contains info about activities in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/MemoActivity) |

### ContractCollection

The `ContractCollection` table contains info about contracts in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/Contract) |

### CorporateAccountCollection

The `CorporateAccountCollection` table contains info about corporate accounts in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/CorporateAccount) |

### EMailCollection

The `EMailCollection` table contains info about email records in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/EMail) |

### IndividualCustomerCollection

The `IndividualCustomerCollection` table contains info about individual customers in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/IndividualCustomer) |

### LeadCollection

The `LeadCollection` table contains info about sales leads in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/Lead) |

### OpportunityCollection

The `OpportunityCollection` table contains info about sales opportunities in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/Opportunity) |

### PhoneCallAttachmentFolder

The `PhoneCallAttachmentFolder` table contains info about attachments to phone call records in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/PhoneCallAttachmentFolder) |

### PhoneCallBTDReferenceCollection

The `PhoneCallBTDReferenceCollection` table contains info about business transaction document references for phone calls in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/PhoneCallBTDReference) |

### PhoneCallPartiesCollection

The `PhoneCallPartiesCollection` table contains info about parties involved in phone calls in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/PhoneCallParties) |

### PhoneCallNotesCollection

The `PhoneCallNotesCollection` table contains info about notes attached to phone calls in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/PhoneCallNotes) |

### PhoneCallParticipantsCollection

The `PhoneCallParticipantsCollection` table contains info about participants in phone calls in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/PhoneCallParticipants) |

### TasksCollection

The `TasksCollection` table contains info about tasks in your SAP Cloud for Customer account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ObjectID |
| **Replication Key** | EntityLastChangedOn |
| **Useful links** | [SAP Cloud for Customer OData API](https://help.sap.com/doc/d0f9ba822c08405da7d88174b304df84/CLOUD/en-US/index.html#/topic/Tasks) |
