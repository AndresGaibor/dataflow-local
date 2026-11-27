---
title: "Google Search Console"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Google-Search-Console.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Google Search Console

Google Search Console provides information on how Google crawls, indexes, and serves websites.

Google Search Console integration replicates data using the [Google Search Console API](https://developers.google.com/webmaster-tools/search-console-api-original/v3/how-tos/search_analytics).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

The Admin access persmission is required in your Google Search Console account to change settings required for the connection.

To obtain your client ID and secret:

1. Log into your [Google Search Console](https://console.developers.google.com) account.
2. Create or select a project.
3. Select the Credentials tab on the left.
4. Select your OAuth app in the OAuth 2.0 Client IDs section. The client ID and secret are displayed.
5. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.
6. To create a new client ID, click Create Credentials.

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
| Site URLs | The URL for the site from which you are collecting search data. Example: `https://www.qlik.com` |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### performance\_report\_country

The `performance_report_country` table contains information about the performance of your sites in Google searches. This particular table is filtered and grouped by country.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | site\_url  search\_type  country  date |
| **Replication Key** | date |
| **Useful links** | [Google Search Console documentation](https://support.google.com/webmasters/answer/7576553?hl=en)  [Google Search Console API method](https://developers.google.com/webmaster-tools/search-console-api-original/v3/searchanalytics/query "Opens in new tab: Google Search Console API method") |

performance\_report\_country table foreign keys

| Join performance\_report\_country with | on |
| --- | --- |
| [sites](#sites) | ``` performance_report_country.site_url = sites.site_url ``` |
| [sitemaps](#sitemaps) | ``` performance_report_country.site_url = sitemaps.site_url ``` |
| [performance\_report\_custom](#performance-report-custom) | ``` performance_report_country.site_url = performance_report_custom.site_url ```  ``` performance_report_country.search_type = performance_report_custom.search_type ``` |
| [performance\_report\_date](#performance-report-date) | ``` performance_report_country.site_url = performance_report_date.site_url ```  ``` performance_report_country.search_type = performance_report_date.search_type ``` |
| [performance\_report\_device](#performance-report-device) | ``` performance_report_country.site_url = performance_report_device.site_url ```  ``` performance_report_country.search_type = performance_report_device.search_type ``` |
| [performance\_report\_page](#performance-report-page) | ``` performance_report_country.site_url = performance_report_page.site_url ```  ``` performance_report_country.search_type = performance_report_page.search_type ``` |
| [performance\_report\_query](#performance-report-query) | ``` performance_report_country.site_url = performance_report_query.site_url ```  ``` performance_report_country.search_type = performance_report_query.search_type ``` |

performance\_report\_country table schema

|  |
| --- |
| **clicks**  INTEGER |
| **country**  STRING |
| **ctr**  NUMBER |
| **date**  DATE-TIME |
| **impressions**  INTEGER |
| **position**  NUMBER |
| **search\_type**  STRING |
| **site\_url**  STRING |

### performance\_report\_custom

The `performance_report_custom` table contains information about the performance of your sites in Google searches. This particular table is filtered and grouped by your custom dimensions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | search\_type  site\_url  dimensions\_hash\_key  date |
| **Replication Key** | date |
| **Useful links** | [Google Search Console documentation](https://support.google.com/webmasters/answer/7576553?hl=en)  [Google Search Console API method](https://developers.google.com/webmaster-tools/search-console-api-original/v3/searchanalytics/query "Opens in new tab: Google Search Console API method") |

performance\_report\_custom table foreign keys

| Join performance\_report\_custom with | on |
| --- | --- |
| [sites](#sites) | ``` performance_report_custom.site_url = sites.site_url ``` |
| [sitemaps](#sitemaps) | ``` performance_report_custom.site_url = sitemaps.site_url ``` |
| [performance\_report\_country](#performance-report-country) | ``` performance_report_custom.site_url = performance_report_country.site_url ```  ``` performance_report_custom.search_type = performance_report_country.search_type ``` |
| [performance\_report\_date](#performance-report-date) | ``` performance_report_custom.site_url = performance_report_date.site_url ```  ``` performance_report_custom.search_type = performance_report_date.search_type ``` |
| [performance\_report\_device](#performance-report-device) | ``` performance_report_custom.site_url = performance_report_device.site_url ```  ``` performance_report_custom.search_type = performance_report_device.search_type ``` |
| [performance\_report\_page](#performance-report-page) | ``` performance_report_custom.site_url = performance_report_page.site_url ```  ``` performance_report_custom.search_type = performance_report_page.search_type ``` |
| [performance\_report\_query](#performance-report-query) | ``` performance_report_custom.site_url = performance_report_query.site_url ```  ``` performance_report_custom.search_type = performance_report_query.search_type ``` |

performance\_report\_custom table schema

|  |
| --- |
| **clicks**  INTEGER |
| **country**  STRING |
| **ctr**  NUMBER |
| **date**  DATE-TIME |
| **device**  STRING |
| **dimensions\_hash\_key**  STRING |
| **impressions**  INTEGER |
| **page**  STRING |
| **position**  NUMBER |
| **query**  STRING |
| **search\_type**  STRING |
| **site\_url**  STRING |

### performance\_report\_date

The `performance_report_date` table contains information about the performance of your sites in Google searches. This particular table is filtered and grouped by date.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | search\_type  site\_url  date |
| **Replication Key** | date |
| **Useful links** | [Google Search Console documentation](https://support.google.com/webmasters/answer/7576553?hl=en)  [Google Search Console API method](https://developers.google.com/webmaster-tools/search-console-api-original/v3/searchanalytics/query "Opens in new tab: Google Search Console API method") |

performance\_report\_date table foreign keys

| Join performance\_report\_date with | on |
| --- | --- |
| [sites](#sites) | ``` performance_report_date.site_url = sites.site_url ``` |
| [sitemaps](#sitemaps) | ``` performance_report_date.site_url = sitemaps.site_url ``` |
| [performance\_report\_country](#performance-report-country) | ``` performance_report_date.site_url = performance_report_country.site_url ```  ``` performance_report_date.search_type = performance_report_country.search_type ``` |
| [performance\_report\_custom](#performance-report-custom) | ``` performance_report_date.site_url = performance_report_custom.site_url ```  ``` performance_report_date.search_type = performance_report_custom.search_type ``` |
| [performance\_report\_device](#performance-report-device) | ``` performance_report_date.site_url = performance_report_device.site_url ```  ``` performance_report_date.search_type = performance_report_device.search_type ``` |
| [performance\_report\_page](#performance-report-page) | ``` performance_report_date.site_url = performance_report_page.site_url ```  ``` performance_report_date.search_type = performance_report_page.search_type ``` |
| [performance\_report\_query](#performance-report-query) | ``` performance_report_date.site_url = performance_report_query.site_url ```  ``` performance_report_date.search_type = performance_report_query.search_type ``` |

performance\_report\_date table schema

|  |
| --- |
| **clicks**  INTEGER |
| **ctr**  NUMBER |
| **date**  DATE-TIME |
| **impressions**  INTEGER |
| **position**  NUMBER |
| **search\_type**  STRING |
| **site\_url**  STRING |

### performance\_report\_device

The `performance_report_device` table contains information about the performance of your sites in Google searches. This particular table is filtered and grouped by the user’s device type.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | search\_type  site\_url  device  date |
| **Replication Key** | date |
| **Useful links** | [Google Search Console documentation](https://support.google.com/webmasters/answer/7576553?hl=en)  [Google Search Console API method](https://developers.google.com/webmaster-tools/search-console-api-original/v3/searchanalytics/query "Opens in new tab: Google Search Console API method") |

performance\_report\_device table foreign keys

| Join performance\_report\_device with | on |
| --- | --- |
| [sites](#sites) | ``` performance_report_device.site_url = sites.site_url ``` |
| [sitemaps](#sitemaps) | ``` performance_report_device.site_url = sitemaps.site_url ``` |
| [performance\_report\_country](#performance-report-country) | ``` performance_report_device.site_url = performance_report_country.site_url ```  ``` performance_report_device.search_type = performance_report_country.search_type ``` |
| [performance\_report\_custom](#performance-report-custom) | ``` performance_report_device.site_url = performance_report_custom.site_url ```  ``` performance_report_device.search_type = performance_report_custom.search_type ``` |
| [performance\_report\_date](#performance-report-date) | ``` performance_report_device.site_url = performance_report_date.site_url ```  ``` performance_report_device.search_type = performance_report_date.search_type ``` |
| [performance\_report\_page](#performance-report-page) | ``` performance_report_device.site_url = performance_report_page.site_url ```  ``` performance_report_device.search_type = performance_report_page.search_type ``` |
| [performance\_report\_query](#performance-report-query) | ``` performance_report_device.site_url = performance_report_query.site_url ```  ``` performance_report_device.search_type = performance_report_query.search_type ``` |

performance\_report\_device table schema

|  |
| --- |
| **clicks**  INTEGER |
| **ctr**  NUMBER |
| **date**  DATE-TIME |
| **device**  STRING |
| **impressions**  INTEGER |
| **position**  NUMBER |
| **search\_type**  STRING |
| **site\_url**  STRING |

### performance\_report\_page

The `performance_report_page` table contains information about the performance of your sites in Google searches. This particular table is filtered and grouped by your landing page URLs that show up in Google search results.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | search\_type  site\_url  page  date |
| **Replication Key** | date |
| **Useful links** | [Google Search Console documentation](https://support.google.com/webmasters/answer/7576553?hl=en)  [Google Search Console API method](https://developers.google.com/webmaster-tools/search-console-api-original/v3/searchanalytics/query "Opens in new tab: Google Search Console API method") |

performance\_report\_page table foreign keys

| Join performance\_report\_page with | on |
| --- | --- |
| [sites](#sites) | ``` performance_report_page.site_url = sites.site_url ``` |
| [sitemaps](#sitemaps) | ``` performance_report_page.site_url = sitemaps.site_url ``` |
| [performance\_report\_country](#performance-report-country) | ``` performance_report_page.site_url = performance_report_country.site_url ```  ``` performance_report_page.search_type = performance_report_country.search_type ``` |
| [performance\_report\_custom](#performance-report-custom) | ``` performance_report_page.site_url = performance_report_custom.site_url ```  ``` performance_report_page.search_type = performance_report_custom.search_type ``` |
| [performance\_report\_date](#performance-report-date) | ``` performance_report_page.site_url = performance_report_date.site_url ```  ``` performance_report_page.search_type = performance_report_date.search_type ``` |
| [performance\_report\_device](#performance-report-device) | ``` performance_report_page.site_url = performance_report_device.site_url ```  ``` performance_report_page.search_type = performance_report_device.search_type ``` |
| [performance\_report\_query](#performance-report-query) | ``` performance_report_page.site_url = performance_report_query.site_url ```  ``` performance_report_page.search_type = performance_report_query.search_type ``` |

performance\_report\_page table schema

|  |
| --- |
| **clicks**  INTEGER |
| **ctr**  NUMBER |
| **date**  DATE-TIME |
| **impressions**  INTEGER |
| **page**  STRING |
| **position**  NUMBER |
| **search\_type**  STRING |
| **site\_url**  STRING |

### performance\_report\_query

The `performance_report_query` table contains information about the performance of your sites in Google searches. This particular table is filtered and grouped by the users’ search queries that resulted in your sites appearing in the search results.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | search\_type  site\_url  query  date |
| **Replication Key** | date |
| **Useful links** | [Google Search Console documentation](https://support.google.com/webmasters/answer/7576553?hl=en)  [Google Search Console API method](https://developers.google.com/webmaster-tools/search-console-api-original/v3/searchanalytics/query "Opens in new tab: Google Search Console API method") |

performance\_report\_query table foreign keys

| Join performance\_report\_query with | on |
| --- | --- |
| [sites](#sites) | ``` performance_report_query.site_url = sites.site_url ``` |
| [sitemaps](#sitemaps) | ``` performance_report_query.site_url = sitemaps.site_url ``` |
| [performance\_report\_country](#performance-report-country) | ``` performance_report_query.site_url = performance_report_country.site_url ```  ``` performance_report_query.search_type = performance_report_country.search_type ``` |
| [performance\_report\_custom](#performance-report-custom) | ``` performance_report_query.site_url = performance_report_custom.site_url ```  ``` performance_report_query.search_type = performance_report_custom.search_type ``` |
| [performance\_report\_date](#performance-report-date) | ``` performance_report_query.site_url = performance_report_date.site_url ```  ``` performance_report_query.search_type = performance_report_date.search_type ``` |
| [performance\_report\_device](#performance-report-device) | ``` performance_report_query.site_url = performance_report_device.site_url ```  ``` performance_report_query.search_type = performance_report_device.search_type ``` |
| [performance\_report\_page](#performance-report-page) | ``` performance_report_query.site_url = performance_report_page.site_url ```  ``` performance_report_query.search_type = performance_report_page.search_type ``` |

performance\_report\_query table schema

|  |
| --- |
| **clicks**  INTEGER |
| **ctr**  NUMBER |
| **date**  DATE-TIME |
| **impressions**  INTEGER |
| **position**  NUMBER |
| **query**  STRING |
| **search\_type**  STRING |
| **site\_url**  STRING |

### sitemaps

The `sitemaps` table contains information about the sitemap entries in your Google Search Console.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | site\_url  path  last\_submitted |
| **Useful links** | [Google Search Console documentation](https://developers.google.com/webmaster-tools/search-console-api-original/v3/sitemaps)  [Google Search Console API method](https://developers.google.com/webmaster-tools/search-console-api-original/v3/sitemaps/list "Opens in new tab: Google Search Console API method") |

sitemaps table foreign keys

| Join sitemaps with | on |
| --- | --- |
| [sites](#sites) | ``` sitemaps.site_url = sites.site_url ``` |
| [performance\_report\_country](#performance-report-country) | ``` sitemaps.site_url = performance_report_country.site_url ``` |
| [performance\_report\_custom](#performance-report-custom) | ``` sitemaps.site_url = performance_report_custom.site_url ``` |
| [performance\_report\_date](#performance-report-date) | ``` sitemaps.site_url = performance_report_date.site_url ``` |
| [performance\_report\_device](#performance-report-device) | ``` sitemaps.site_url = performance_report_device.site_url ``` |
| [performance\_report\_page](#performance-report-page) | ``` sitemaps.site_url = performance_report_page.site_url ``` |
| [performance\_report\_query](#performance-report-query) | ``` sitemaps.site_url = performance_report_query.site_url ``` |

sitemaps table schema

|  |
| --- |
| **contents**    ARRAY  This is a nested data structure:   - **indexed**: INTEGER - **submitted**: INTEGER - **type**: STRING |
| **errors**  INTEGER |
| **is\_pending**  BOOLEAN |
| **is\_sitemaps\_index**  BOOLEAN |
| **last\_downloaded**  DATE-TIME |
| **last\_submitted**  DATE-TIME |
| **path**  STRING |
| **site\_url**  STRING |
| **type**  STRING |
| **warnings**  INTEGER |

### sites

The `sites` contains information about your Google Search Console sites at a permission level.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | site\_url |
| **Useful links** | [Google Search Console documentation](https://developers.google.com/webmaster-tools/search-console-api-original/v3/sites)  [Google Search Console API method](https://developers.google.com/webmaster-tools/search-console-api-original/v3/sites/get "Opens in new tab: Google Search Console API method") |

sites table foreign keys

| Join sites with | on |
| --- | --- |
| [sitemaps](#sitemaps) | ``` sites.site_url = sitemaps.site_url ``` |
| [performance\_report\_country](#performance-report-country) | ``` sites.site_url = performance_report_country.site_url ``` |
| [performance\_report\_custom](#performance-report-custom) | ``` sites.site_url = performance_report_custom.site_url ``` |
| [performance\_report\_date](#performance-report-date) | ``` sites.site_url = performance_report_date.site_url ``` |
| [performance\_report\_device](#performance-report-device) | ``` sites.site_url = performance_report_device.site_url ``` |
| [performance\_report\_page](#performance-report-page) | ``` sites.site_url = performance_report_page.site_url ``` |
| [performance\_report\_query](#performance-report-query) | ``` sites.site_url = performance_report_query.site_url ``` |

sites table schema

|  |
| --- |
| **permission\_level**  STRING |
| **site\_url**  STRING |
