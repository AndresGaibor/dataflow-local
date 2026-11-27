---
title: "SparkPost"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SparkPost.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# SparkPost

SparkPost is an email delivery platform that provides transactional and marketing email services.

SparkPost integration replicates data using the [SparkPost API](https://developers.sparkpost.com/api/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To create your API key:

1. Log into your [SparkPost](https://login.sparkpost.com/u/login?state=hKFo2SBGTUhCMnhzWnE2Q0RlaVdSZzVBcGxRTFFGUmEwMTc3LaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIGFmenNmYWl5a21teFVuMndqNWFyNlQ3bmhnR0RhNzRIo2NpZNkgUXR5QVJpOEZoTlpUZ2xCWXdPNWRTeXpzZG5RdmR4Q3k) account.
2. Navigate to Configuration > API Keys > Create API Key.
3. Name the API key.
4. Choose which permissions you want the API key to have.
5. Click Create API Key.
6. Copy and paste your API key into a secured file.

Restrict API key network traffic by allowing only specific IP addresses. To configure this, locate your Qlik Talend Cloud tenant IP addresses. For more information, see [Allowlisting domains and IP addresses](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qlik-cloud-dns-ip.htm).

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
| Precision | The default setting is DAY. Use this parameter to aggregate time-series data returned by the SparkPost Metrics API. Select one of the following options to define the aggregation level:  - DAY - HOUR - MIN |

## Schema

Depending on your destination, table and column names may not appear as they are outlined below.

### events

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | event\_id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/events/) |

### webhooks

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/webhooks/) |

### templates

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/templates/) |

### sending\_domains

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | domain |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/sending-domains/) |

### tracking\_domains

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | domain |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/tracking-domains/) |

### suppression\_list

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | recipient |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/suppression-list/) |

### recipient\_lists

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/recipient-lists/) |

### account

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | customer\_id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/account/) |

### usage

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | timestamp |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/usage/) |

### subaccounts

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/subaccounts/) |

### ip\_pools

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/ip-pools/) |

### metrics\_recipient\_domain

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  domain |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-metrics-by-recipient-domain) |

### metrics\_sending\_ip

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  sending\_ip |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-metrics-by-sending-ip) |

### metrics\_ip\_pool

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  ip\_pool |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-metrics-by-ip-pool) |

### metrics\_sending\_domain

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  sending\_domain |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-metrics-by-sending-domain) |

### metrics\_subaccount

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  subaccount\_id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/) |

### metrics\_campaign

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  campaign\_id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-metrics-by-campaign) |

### metrics\_template

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  template\_id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-metrics-by-template) |

### metrics\_subject\_campaign

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  subject\_campaign |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-metrics-by-subject-campaign) |

### metrics\_watched\_domain

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  watched\_domain |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-metrics-by-watched-domain) |

### metrics\_mailbox\_provider

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  mailbox\_provider |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-metrics-by-mailbox-provider) |

### metrics\_mailbox\_provider\_region

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  mailbox\_provider\_region |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-metrics-by-mailbox-provider-region) |

### metrics\_time\_series

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-time-series-metrics) |

### metrics\_bounce\_reason

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  reason  classification\_id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-bounce-reason-metrics) |

### metrics\_bounce\_reason\_by\_domain

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  reason  domain  classification\_id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-bounce-reason-metrics-by-domain) |

### metrics\_bounce\_classification

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  classification\_id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-bounce-classification-metrics) |

### metrics\_rejection\_reason

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  reason  rejection\_category\_id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-rejection-reason-metrics) |

### metrics\_rejection\_reason\_by\_domain

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  reason  domain  rejection\_category\_id |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-rejection-reason-metrics-by-domain) |

### metrics\_delay\_reason

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  reason |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-delay-reason-metrics) |

### metrics\_delay\_reason\_by\_domain

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  reason  domain |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-delay-reason-metrics-by-domain) |

### metrics\_engagement\_details

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  link\_name |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-engagement-details) |

### metrics\_deliveries\_by\_attempt

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp  attempt |
| **Useful links** | [SparkPost documentation](https://developers.sparkpost.com/api/metrics/#metrics-get-deliveries-by-attempt) |
