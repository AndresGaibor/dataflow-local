---
title: "Youtube Analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Youtube-Analytics-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Youtube Analytics

Youtube Analytics is the analytics service by Youtube to better understand your video and channel performance with key metrics.

Youtube Analytics integration replicates data using the [Youtube Reporting API](https://developers.google.com/youtube/reporting/v1/reports) and [Youtube Data API](https://developers.google.com/youtube/v3/docs).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your client ID and client secret:

1. Log into Google Cloud Console.
2. Go to APIs & Services > OAuth Consent Screens > Get Started.
3. In the Audience field, select External.
4. Go to APIs & Services > Credentials.
5. Click Create Credentials > OAuth client ID.
6. In the Application type field, select Web application.
7. In the Name field, type a name for the credentials.
8. Click Create.
9. Copy and paste your client ID and client secret into a secured file.

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
| Channel IDs | Youtube channel ID. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### channels

The `channels` table contains info about the channels in your Youtube Analytics account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Youtube Analytics documentation](https://developers.google.com/youtube/v3/docs/channels/list) |

### playlists

The `playlists` table contains info about the playlists in your Youtube Analytics account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Youtube Analytics documentation](https://developers.google.com/youtube/v3/docs/playlists/list) |

### playlist\_items

The `playlist_items` table contains info about the playlist items in your Youtube Analytics account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | published\_at |
| **Useful links** | [Youtube Analytics documentation](https://developers.google.com/youtube/v3/docs/playlistItems/list) |

### videos

The `videos` table contains info about the videos in your Youtube Analytics account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | published\_at |
| **Useful links** | [Youtube Analytics documentation](https://developers.google.com/youtube/v3/docs/videos/list) |

### YouTube Reporting Streams

The `YouTube Reporting Streams` table contains info about the reporting streams in your Youtube Analytics account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | dimensions\_hash\_key  date |
| **Replication Keys** | create\_time |
| **Useful links** | [Youtube Analytics documentation](https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs.reports/list) |
