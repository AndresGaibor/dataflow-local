---
title: "FullStory"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-FullStory.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# FullStory

FullStory is a Digital Experience Intelligence (DXI) platform that helps businesses understand how users interact with their digital products.

FullStory integration relies on the Data Export pack add-on to replicate data through the [FullStory Data Export REST API](https://help.fullstory.com/hc/en-us/articles/360020624194-HTTP-API-Retrieving-Data-Export-Extracts).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your API key:

1. Log into your [FullStory](https://app.fullstory.com/login?dest=%2Funified%3Fdest%3Dhttps%253A%252F%252Fauth.fullstory.com%252Fidp%252Ftoken%252FcompleteAuthentication%253Fsp%253Dzendesk%2526csrfTokenId%253DA4BRn2ZbNprLHMzj7%25252FtMtec7xKM%25253D%2526flow%253Dtoken) account.
2. Click your user menu in the upper-right corner, and then click Settings.
3. Navigate to Integrations & API Keys > API Key.
4. Copy and paste your API key into a secured file.

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

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### users

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/users/list-users/) |

### user

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/users/get-user/) |

### block\_rules

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | created  createdBy  lastUpdated |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/settings/get-recording-block-rules/) |

### block\_rules\_history

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | created  createdBy  lastUpdated |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/settings/get-recording-block-rules-history/) |

### domain\_settings\_history

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | created  createdBy  lastUpdated |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/settings/get-domain-settings-history/) |

### domain\_settings

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | created  createdBy  lastUpdated |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/settings/get-domain-settings/) |

### geo\_settings\_history

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | created  createdBy  lastUpdated |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/settings/get-geo-settings-history/) |

### privacy\_settings

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | created  createdBy  lastUpdated |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/settings/get-privacy-settings/) |

### privacy\_settings\_history

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | created  createdBy  lastUpdated |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/settings/get-privacy-settings/) |

### recording\_features

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | created  createdBy  lastUpdated |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/settings/get-recording-features/) |

### recording\_features\_history

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | created  createdBy  lastUpdated |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/settings/get-recording-features-history/) |

### target\_rule\_history

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | created  createdBy  lastUpdated |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/settings/get-targeting-settings-history/) |

### segments

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [FullStory documentation](https://developer.fullstory.com/server/v1/segments/list-segments/) |
