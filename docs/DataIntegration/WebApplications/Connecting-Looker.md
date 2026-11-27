---
title: "Looker"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Looker.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Looker

Looker is an enterprise platform for BI, data applications, and embedded analytics that helps organizations explore and share insights in real time.

Looker integration replicates data using the [Looker v4 API](https://developers.looker.com/api/explorer/4.0).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need administrator permissions in your Looker account.

To retrieve your client ID and client secret:

1. Log into your [Looker](https://lookerstudio.google.com/overview) account.
2. Navigate to Edit Users > Edit Keys.
3. On the Edit User API3 Keys page, click New API3 key.
4. Copy and paste your client ID and client secret into a secured file.

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
| API Port | The API port is typically `19999`. If you host the API internally, use the internal API port instead. |
| Client ID | Client ID. |
| Client Secret | Client secret. |
| Subdomain | You can find your subdomain in your Looker URL. If the URL is https://demo.cloud.looker.com/folders/home, the subdomain is demo. |
| Domain | You can find your domain in your Looker URL. If the URL is https://demo.cloud.looker.com/folders/home, the domain is looker.com, unless you use a custom domain. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### color\_collections

The `color_collections` table contains information about color collections in your Looker account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/color-collection#get_all_color_collections "Opens in new tab: Looker API method") |

color\_collections table foreign keys

| Join color\_collections with | on |
| --- | --- |
| [themes](#themes) | ``` color_collections.id = themes.settings.color_collection_id ``` |

color\_collections table schema

|  |
| --- |
| **categoricalPalettes**  ARRAY This is a nested data structure:   - colors: ARRAY, which is also a nested data structure. - id: STRING - label: STRING - type: STRING |
| **divergingPalettes**  ARRAY This is a nested data structure:   - id: STRING - label: STRING - stops: ARRAY, which is also a nested data structure.   - color: STRING   - offset: NUMBER - type: STRING |
| **id**  STRING |
| **label**  STRING |
| **sequentialPalettes**  ARRAY This is a nested data structure:   - id: STRING - label: STRING - stops: ARRAY, which is also a nested data structure.   - color: STRING   - offset: NUMBER - type: STRING |

### connections

The `connections` table contains information about connections in your Looker account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | name |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/connection#get_all_connections "Opens in new tab: Looker API method") |

connections table foreign keys

| Join connections with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` connections.user_id = content_favorites.dashboard.folder.creator_id ```  ``` connections.user_id = content_favorites.dashboard.space.creator_id ```  ``` connections.user_id = content_favorites.user_id ``` |
| [content\_views](#content-views) | ``` connections.user_id = content_views.user_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` connections.user_id = dashboard_elements.look.deleter_id ```  ``` connections.user_id = dashboard_elements.look.folder.creator_id ```  ``` connections.user_id = dashboard_elements.look.last_updater_id ```  ``` connections.user_id = dashboard_elements.look.space.creator_id ```  ``` connections.user_id = dashboard_elements.look.user.id ```  ``` connections.user_id = dashboard_elements.look.user_id ``` |
| [dashboards](#dashboards) | ``` connections.user_id = dashboards.space.creator_id ```  ``` connections.user_id = dashboards.user_id ``` |
| [folders](#folders) | ``` connections.user_id = folders.creator_id ```  ``` connections.user_id = folders.dashboards.user_id ```  ``` connections.user_id = folders.dashboards.folder.creator_id ```  ``` connections.user_id = folders.dashboards.space.creator_id ```  ``` connections.user_id = folders.looks.deleter_id ```  ``` connections.user_id = folders.looks.last_updater_id ```  ``` connections.user_id = folders.looks.user.id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` connections.user_id = lookml_dashboards.folder.creator_id ```  ``` connections.user_id = lookml_dashboards.space.creator_id ```  ``` connections.user_id = lookml_dashboards.user_id ``` |
| [looks](#looks) | ``` connections.user_id = looks.deleter_id ```  ``` connections.user_id = looks.folder.creator_id ```  ``` connections.user_id = looks.user.id ```  ``` connections.user_id = looks.user_id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` connections.user_id = scheduled_plans.user.id ```  ``` connections.user_id = scheduled_plans.user_id ``` |
| [user\_login\_lockouts](#user-login-lockouts) | ``` connections.user_id = user_login_lockouts.user_id ``` |
| [users](#users) | ``` connections.user_id = users.id ``` |

connections table schema

|  |
| --- |
| **after\_connect\_statements**  STRING |
| **certificate**  STRING |
| **created\_at**  STRING |
| **database**  STRING |
| **db\_timezone**  STRING |
| **dialect**  OBJECT This is a nested data structure:   - automatically\_run\_sql\_runner\_snippets: BOOLEAN - connection\_tests: ARRAY, which is also a nested data structure. - label: STRING - name: STRING - persistent\_table\_distkey: STRING - persistent\_table\_indexes: STRING - persistent\_table\_sortkeys: STRING - supports\_cost\_estimate: BOOLEAN - supports\_inducer: BOOLEAN - supports\_streaming: BOOLEAN - supports\_upload\_tables: BOOLEAN |
| **dialect\_name**  STRING |
| **example**  BOOLEAN |
| **file\_type**  STRING |
| **host**  STRING |
| **jdbc\_additional\_params**  STRING |
| **last\_reap\_at**  INTEGER |
| **last\_regen\_at**  INTEGER |
| **maintenance\_cron**  STRING |
| **max\_billing\_gigabytes**  NUMBER |
| **max\_connections**  INTEGER |
| **name**  STRING |
| **password**  STRING |
| **pdt\_context\_override**  OBJECT This is a nested data structure:   - after\_connect\_statements: STRING - certificate: STRING - context: STRING - database: STRING - file\_type: STRING - has\_password: BOOLEAN - host: STRING - jdbc\_additional\_params: STRING - password: STRING - port: STRING - schema: STRING - username: STRING |
| **pool\_timeout**  INTEGER |
| **port**  STRING |
| **query\_timezone**  STRING |
| **schema**  STRING |
| **snippets**  ARRAY This is a nested data structure:   - label: STRING - name: STRING - sql: STRING |
| **sql\_runner\_precache\_tables**  BOOLEAN |
| **ssl**  BOOLEAN |
| **tmp\_db\_name**  STRING |
| **user\_attribute\_fields**  ARRAY This is a nested data structure. |
| **user\_db\_credentials**  BOOLEAN |
| **user\_id**  STRING |
| **username**  STRING |
| **uses\_oauth**  BOOLEAN |
| **verify\_ssl**  BOOLEAN |

### content\_favorites

The `content_favorites` table contains info about users’ favorite content in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#search_favorite_contents "Opens in new tab: Looker API method") |

content\_favorites table foreign keys

| Join content\_favorites with | on |
| --- | --- |
| [dashboard\_elements](#dashboard-elements) | ``` content_favorites.id = dashboard_elements.look.content_favorite_id ```  ``` content_favorites.dashboard.content_favorite_id = dashboard_elements.look.content_favorite_id ```  ``` content_favorites.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` content_favorites.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` content_favorites.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` content_favorites.dashboard.id = dashboard_elements.dashboard_id ```  ``` content_favorites.dashboard_id = dashboard_elements.dashboard_id ```  ``` content_favorites.dashboard.folder.id = dashboard_elements.look.folder.id ```  ``` content_favorites.dashboard.folder.parent_id = dashboard_elements.look.folder.id ```  ``` content_favorites.dashboard.folder.id = dashboard_elements.look.folder.parent_id ```  ``` content_favorites.dashboard.folder.parent_id = dashboard_elements.look.folder.parent_id ```  ``` content_favorites.dashboard.folder.id = dashboard_elements.look.folder_id ```  ``` content_favorites.dashboard.folder.parent_id = dashboard_elements.look.folder_id ```  ``` content_favorites.look_id = dashboard_elements.look.id ```  ``` content_favorites.look.id = dashboard_elements.look.id ```  ``` content_favorites.look_id = dashboard_elements.look_id ```  ``` content_favorites.look.id = dashboard_elements.look_id ```  ``` content_favorites.dashboard.model.id = dashboard_elements.look.model.id ```  ``` content_favorites.dashboard.space.id = dashboard_elements.look.space.id ```  ``` content_favorites.dashboard.space.parent_id = dashboard_elements.look.space.id ```  ``` content_favorites.dashboard.space.id = dashboard_elements.look.space.parent_id ```  ``` content_favorites.dashboard.space.parent_id = dashboard_elements.look.space.parent_id ```  ``` content_favorites.dashboard.folder.creator_id = dashboard_elements.look.deleter_id ```  ``` content_favorites.dashboard.space.creator_id = dashboard_elements.look.deleter_id ```  ``` content_favorites.user_id = dashboard_elements.look.deleter_id ```  ``` content_favorites.dashboard.folder.creator_id = dashboard_elements.look.folder.creator_id ```  ``` content_favorites.dashboard.space.creator_id = dashboard_elements.look.folder.creator_id ```  ``` content_favorites.user_id = dashboard_elements.look.folder.creator_id ```  ``` content_favorites.dashboard.folder.creator_id = dashboard_elements.look.last_updater_id ```  ``` content_favorites.dashboard.space.creator_id = dashboard_elements.look.last_updater_id ```  ``` content_favorites.user_id = dashboard_elements.look.last_updater_id ```  ``` content_favorites.dashboard.folder.creator_id = dashboard_elements.look.space.creator_id ```  ``` content_favorites.dashboard.space.creator_id = dashboard_elements.look.space.creator_id ```  ``` content_favorites.user_id = dashboard_elements.look.space.creator_id ```  ``` content_favorites.dashboard.folder.creator_id = dashboard_elements.look.user.id ```  ``` content_favorites.dashboard.space.creator_id = dashboard_elements.look.user.id ```  ``` content_favorites.user_id = dashboard_elements.look.user.id ```  ``` content_favorites.dashboard.folder.creator_id = dashboard_elements.look.user_id ```  ``` content_favorites.dashboard.space.creator_id = dashboard_elements.look.user_id ```  ``` content_favorites.user_id = dashboard_elements.look.user_id ``` |
| [dashboards](#dashboards) | ``` content_favorites.id = dashboards.content_favorite_id ```  ``` content_favorites.dashboard.content_favorite_id = dashboards.content_favorite_id ```  ``` content_favorites.content_metadata_id = dashboards.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = dashboards.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = dashboards.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = dashboards.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = dashboards.content_metadata_id ```  ``` content_favorites.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` content_favorites.content_metadata_id = dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = dashboards.space.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.id = dashboards.id ```  ``` content_favorites.dashboard_id = dashboards.id ```  ``` content_favorites.dashboard.folder.id = dashboards.folder.id ```  ``` content_favorites.dashboard.folder.parent_id = dashboards.folder.id ```  ``` content_favorites.dashboard.folder.id = dashboards.folder.parent_id ```  ``` content_favorites.dashboard.folder.parent_id = dashboards.folder.parent_id ```  ``` content_favorites.dashboard.model.id = dashboards.model.id ```  ``` content_favorites.dashboard.space.id = dashboards.space.id ```  ``` content_favorites.dashboard.space.parent_id = dashboards.space.id ```  ``` content_favorites.dashboard.space.id = dashboards.space.parent_id ```  ``` content_favorites.dashboard.space.parent_id = dashboards.space.parent_id ```  ``` content_favorites.dashboard.folder.creator_id = dashboards.space.creator_id ```  ``` content_favorites.dashboard.space.creator_id = dashboards.space.creator_id ```  ``` content_favorites.user_id = dashboards.space.creator_id ```  ``` content_favorites.dashboard.folder.creator_id = dashboards.user_id ```  ``` content_favorites.dashboard.space.creator_id = dashboards.user_id ```  ``` content_favorites.user_id = dashboards.user_id ``` |
| [folders](#folders) | ``` content_favorites.id = folders.dashboards.content_favorite_id ```  ``` content_favorites.dashboard.content_favorite_id = folders.dashboards.content_favorite_id ```  ``` content_favorites.id = folders.looks.content_favorite_id ```  ``` content_favorites.dashboard.content_favorite_id = folders.looks.content_favorite_id ```  ``` content_favorites.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` content_favorites.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` content_favorites.content_metadata_id = folders.looks.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = folders.looks.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = folders.looks.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = folders.looks.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = folders.looks.content_metadata_id ```  ``` content_favorites.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` content_favorites.dashboard.id = folders.dashboards.id ```  ``` content_favorites.dashboard_id = folders.dashboards.id ```  ``` content_favorites.dashboard.folder.id = folders.id ```  ``` content_favorites.dashboard.folder.parent_id = folders.id ```  ``` content_favorites.dashboard.folder.id = folders.dashboards.folder.id ```  ``` content_favorites.dashboard.folder.parent_id = folders.dashboards.folder.id ```  ``` content_favorites.dashboard.folder.id = folders.dashboards.folder.parent_id ```  ``` content_favorites.dashboard.folder.parent_id = folders.dashboards.folder.parent_id ```  ``` content_favorites.dashboard.folder.id = folders.looks.folder.id ```  ``` content_favorites.dashboard.folder.parent_id = folders.looks.folder.id ```  ``` content_favorites.dashboard.folder.id = folders.looks.folder.parent_id ```  ``` content_favorites.dashboard.folder.parent_id = folders.looks.folder.parent_id ```  ``` content_favorites.dashboard.folder.id = folders.parent_id ```  ``` content_favorites.dashboard.folder.parent_id = folders.parent_id ```  ``` content_favorites.look_id = folders.looks.id ```  ``` content_favorites.look.id = folders.looks.id ```  ``` content_favorites.dashboard.model.id = folders.dashboards.model.id ```  ``` content_favorites.dashboard.model.id = folders.looks.model.id ```  ``` content_favorites.dashboard.space.id = folders.dashboards.space.id ```  ``` content_favorites.dashboard.space.parent_id = folders.dashboards.space.id ```  ``` content_favorites.dashboard.space.id = folders.dashboards.space.parent_id ```  ``` content_favorites.dashboard.space.parent_id = folders.dashboards.space.parent_id ```  ``` content_favorites.dashboard.space.id = folders.looks.space.id ```  ``` content_favorites.dashboard.space.parent_id = folders.looks.space.id ```  ``` content_favorites.dashboard.space.id = folders.looks.space.parent_id ```  ``` content_favorites.dashboard.space.parent_id = folders.looks.space.parent_id ```  ``` content_favorites.dashboard.space.id = folders.looks.space_id ```  ``` content_favorites.dashboard.space.parent_id = folders.looks.space_id ```  ``` content_favorites.dashboard.folder.creator_id = folders.creator_id ```  ``` content_favorites.dashboard.space.creator_id = folders.creator_id ```  ``` content_favorites.user_id = folders.creator_id ```  ``` content_favorites.dashboard.folder.creator_id = folders.dashboards.user_id ```  ``` content_favorites.dashboard.space.creator_id = folders.dashboards.user_id ```  ``` content_favorites.user_id = folders.dashboards.user_id ```  ``` content_favorites.dashboard.folder.creator_id = folders.dashboards.folder.creator_id ```  ``` content_favorites.dashboard.space.creator_id = folders.dashboards.folder.creator_id ```  ``` content_favorites.user_id = folders.dashboards.folder.creator_id ```  ``` content_favorites.dashboard.folder.creator_id = folders.dashboards.space.creator_id ```  ``` content_favorites.dashboard.space.creator_id = folders.dashboards.space.creator_id ```  ``` content_favorites.user_id = folders.dashboards.space.creator_id ```  ``` content_favorites.dashboard.folder.creator_id = folders.looks.deleter_id ```  ``` content_favorites.dashboard.space.creator_id = folders.looks.deleter_id ```  ``` content_favorites.user_id = folders.looks.deleter_id ```  ``` content_favorites.dashboard.folder.creator_id = folders.looks.last_updater_id ```  ``` content_favorites.dashboard.space.creator_id = folders.looks.last_updater_id ```  ``` content_favorites.user_id = folders.looks.last_updater_id ```  ``` content_favorites.dashboard.folder.creator_id = folders.looks.user.id ```  ``` content_favorites.dashboard.space.creator_id = folders.looks.user.id ```  ``` content_favorites.user_id = folders.looks.user.id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` content_favorites.id = lookml_dashboards.content_favorite_id ```  ``` content_favorites.dashboard.content_favorite_id = lookml_dashboards.content_favorite_id ```  ``` content_favorites.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` content_favorites.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` content_favorites.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` content_favorites.dashboard.folder.id = lookml_dashboards.folder.id ```  ``` content_favorites.dashboard.folder.parent_id = lookml_dashboards.folder.id ```  ``` content_favorites.dashboard.folder.id = lookml_dashboards.folder.parent_id ```  ``` content_favorites.dashboard.folder.parent_id = lookml_dashboards.folder.parent_id ```  ``` content_favorites.dashboard.model.id = lookml_dashboards.model.id ```  ``` content_favorites.dashboard.space.id = lookml_dashboards.space.id ```  ``` content_favorites.dashboard.space.parent_id = lookml_dashboards.space.id ```  ``` content_favorites.dashboard.space.id = lookml_dashboards.space.parent_id ```  ``` content_favorites.dashboard.space.parent_id = lookml_dashboards.space.parent_id ```  ``` content_favorites.dashboard.folder.creator_id = lookml_dashboards.folder.creator_id ```  ``` content_favorites.dashboard.space.creator_id = lookml_dashboards.folder.creator_id ```  ``` content_favorites.user_id = lookml_dashboards.folder.creator_id ```  ``` content_favorites.dashboard.folder.creator_id = lookml_dashboards.space.creator_id ```  ``` content_favorites.dashboard.space.creator_id = lookml_dashboards.space.creator_id ```  ``` content_favorites.user_id = lookml_dashboards.space.creator_id ```  ``` content_favorites.dashboard.folder.creator_id = lookml_dashboards.user_id ```  ``` content_favorites.dashboard.space.creator_id = lookml_dashboards.user_id ```  ``` content_favorites.user_id = lookml_dashboards.user_id ``` |
| [looks](#looks) | ``` content_favorites.id = looks.content_favorite_id ```  ``` content_favorites.dashboard.content_favorite_id = looks.content_favorite_id ```  ``` content_favorites.content_metadata_id = looks.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = looks.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = looks.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = looks.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = looks.content_metadata_id ```  ``` content_favorites.dashboard.folder.id = looks.folder.id ```  ``` content_favorites.dashboard.folder.parent_id = looks.folder.id ```  ``` content_favorites.dashboard.folder.id = looks.folder_id ```  ``` content_favorites.dashboard.folder.parent_id = looks.folder_id ```  ``` content_favorites.dashboard.folder.id = looks.folder.parent_id ```  ``` content_favorites.dashboard.folder.parent_id = looks.folder.parent_id ```  ``` content_favorites.look_id = looks.id ```  ``` content_favorites.look.id = looks.id ```  ``` content_favorites.dashboard.model.id = looks.model.id ```  ``` content_favorites.dashboard.space.id = looks.space.id ```  ``` content_favorites.dashboard.space.parent_id = looks.space.id ```  ``` content_favorites.dashboard.space.id = looks.space.parent_id ```  ``` content_favorites.dashboard.space.parent_id = looks.space.parent_id ```  ``` content_favorites.dashboard.space.id = looks.space_id ```  ``` content_favorites.dashboard.space.parent_id = looks.space_id ```  ``` content_favorites.dashboard.folder.creator_id = looks.deleter_id ```  ``` content_favorites.dashboard.space.creator_id = looks.deleter_id ```  ``` content_favorites.user_id = looks.deleter_id ```  ``` content_favorites.dashboard.folder.creator_id = looks.folder.creator_id ```  ``` content_favorites.dashboard.space.creator_id = looks.folder.creator_id ```  ``` content_favorites.user_id = looks.folder.creator_id ```  ``` content_favorites.dashboard.folder.creator_id = looks.user.id ```  ``` content_favorites.dashboard.space.creator_id = looks.user.id ```  ``` content_favorites.user_id = looks.user.id ```  ``` content_favorites.dashboard.folder.creator_id = looks.user_id ```  ``` content_favorites.dashboard.space.creator_id = looks.user_id ```  ``` content_favorites.user_id = looks.user_id ``` |
| [content\_metadata](#content-metadata) | ``` content_favorites.content_metadata_id = content_metadata.id ```  ``` content_favorites.dashboard.content_metadata_id = content_metadata.id ```  ``` content_favorites.dashboard.folder.content_metadata_id = content_metadata.id ```  ``` content_favorites.dashboard.space.content_metadata_id = content_metadata.id ```  ``` content_favorites.look.content_metadata_id = content_metadata.id ```  ``` content_favorites.content_metadata_id = content_metadata.parent_id ```  ``` content_favorites.dashboard.content_metadata_id = content_metadata.parent_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = content_metadata.parent_id ```  ``` content_favorites.dashboard.space.content_metadata_id = content_metadata.parent_id ```  ``` content_favorites.look.content_metadata_id = content_metadata.parent_id ```  ``` content_favorites.dashboard.id = content_metadata.dashboard_id ```  ``` content_favorites.dashboard_id = content_metadata.dashboard_id ```  ``` content_favorites.look_id = content_metadata.look_id ```  ``` content_favorites.look.id = content_metadata.look_id ```  ``` content_favorites.dashboard.space.id = content_metadata.space_id ```  ``` content_favorites.dashboard.space.parent_id = content_metadata.space_id ``` |
| [content\_metadata\_access](#content-metadata-access) | ``` content_favorites.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = content_metadata_access.content_metadata_id ``` |
| [content\_views](#content-views) | ``` content_favorites.content_metadata_id = content_views.content_metadata_id ```  ``` content_favorites.dashboard.content_metadata_id = content_views.content_metadata_id ```  ``` content_favorites.dashboard.folder.content_metadata_id = content_views.content_metadata_id ```  ``` content_favorites.dashboard.space.content_metadata_id = content_views.content_metadata_id ```  ``` content_favorites.look.content_metadata_id = content_views.content_metadata_id ```  ``` content_favorites.dashboard.id = content_views.dashboard_id ```  ``` content_favorites.dashboard_id = content_views.dashboard_id ```  ``` content_favorites.look_id = content_views.look_id ```  ``` content_favorites.look.id = content_views.look_id ```  ``` content_favorites.dashboard.folder.creator_id = content_views.user_id ```  ``` content_favorites.dashboard.space.creator_id = content_views.user_id ```  ``` content_favorites.user_id = content_views.user_id ``` |
| [dashboard\_filters](#dashboard-filters) | ``` content_favorites.dashboard.id = dashboard_filters.dashboard_id ```  ``` content_favorites.dashboard_id = dashboard_filters.dashboard_id ``` |
| [dashboard\_layouts](#dashboard-layouts) | ``` content_favorites.dashboard.id = dashboard_layouts.dashboard_id ```  ``` content_favorites.dashboard_id = dashboard_layouts.dashboard_id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` content_favorites.dashboard.id = scheduled_plans.dashboard_id ```  ``` content_favorites.dashboard_id = scheduled_plans.dashboard_id ```  ``` content_favorites.look_id = scheduled_plans.look_id ```  ``` content_favorites.look.id = scheduled_plans.look_id ```  ``` content_favorites.dashboard.folder.creator_id = scheduled_plans.user.id ```  ``` content_favorites.dashboard.space.creator_id = scheduled_plans.user.id ```  ``` content_favorites.user_id = scheduled_plans.user.id ```  ``` content_favorites.dashboard.folder.creator_id = scheduled_plans.user_id ```  ``` content_favorites.dashboard.space.creator_id = scheduled_plans.user_id ```  ``` content_favorites.user_id = scheduled_plans.user_id ``` |
| [users](#users) | ``` content_favorites.dashboard.folder.id = users.home_folder_id ```  ``` content_favorites.dashboard.folder.parent_id = users.home_folder_id ```  ``` content_favorites.dashboard.folder.id = users.personal_folder_id ```  ``` content_favorites.dashboard.folder.parent_id = users.personal_folder_id ```  ``` content_favorites.dashboard.space.id = users.home_space_id ```  ``` content_favorites.dashboard.space.parent_id = users.home_space_id ```  ``` content_favorites.dashboard.space.id = users.personal_space_id ```  ``` content_favorites.dashboard.space.parent_id = users.personal_space_id ```  ``` content_favorites.dashboard.folder.creator_id = users.id ```  ``` content_favorites.dashboard.space.creator_id = users.id ```  ``` content_favorites.user_id = users.id ``` |
| [roles](#roles) | ``` content_favorites.dashboard.model.id = roles.model_set.models ``` |
| [connections](#connections) | ``` content_favorites.dashboard.folder.creator_id = connections.user_id ```  ``` content_favorites.dashboard.space.creator_id = connections.user_id ```  ``` content_favorites.user_id = connections.user_id ``` |
| [user\_login\_lockouts](#user-login-lockouts) | ``` content_favorites.dashboard.folder.creator_id = user_login_lockouts.user_id ```  ``` content_favorites.dashboard.space.creator_id = user_login_lockouts.user_id ```  ``` content_favorites.user_id = user_login_lockouts.user_id ``` |

content\_favorites table schema

|  |
| --- |
| **content\_metadata\_id**  STRING |
| **dashboard**  OBJECT This is a nested data structure:   - content\_favorite\_id: STRING - content\_metadata\_id: STRING - description: STRING - folder: OBJECT, which is also a nested data structure.   - child\_count: INTEGER   - content\_metadata\_id: STRING   - creator\_id: STRING   - external\_id: STRING   - id: STRING   - is\_embed: BOOLEAN   - is\_embed\_shared\_root: BOOLEAN   - is\_embed\_users\_root: BOOLEAN   - is\_personal: BOOLEAN   - is\_personal\_descendant: BOOLEAN   - is\_shared\_root: BOOLEAN   - is\_users\_root: BOOLEAN   - name: STRING   - parent\_id: STRING - hidden: BOOLEAN - id: STRING - model: OBJECT, which is also a nested data structure.   - id: STRING   - label: STRING - query\_timezone: STRING - readonly: BOOLEAN - refresh\_interval: STRING - refresh\_interval\_to\_i: INTEGER - space: OBJECT, which is also a nested data structure.   - child\_count: INTEGER   - content\_metadata\_id: STRING   - creator\_id: STRING   - external\_id: STRING   - id: STRING   - is\_embed: BOOLEAN   - is\_embed\_shared\_root: BOOLEAN   - is\_embed\_users\_root: BOOLEAN   - is\_personal: BOOLEAN   - is\_personal\_descendant: BOOLEAN   - is\_shared\_root: BOOLEAN   - is\_users\_root: BOOLEAN   - name: STRING   - parent\_id: STRING - title: STRING - user\_id: STRING |
| **dashboard\_id**  STRING |
| **id**  STRING |
| **look**  OBJECT This is a nested data structure:   - content\_metadata\_id: STRING - id: STRING - title: STRING |
| **look\_id**  STRING |
| **user\_id**  STRING |

### content\_metadata

The `content_metadata` table contains information about content metadata in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#get_all_content_metadatas "Opens in new tab: Looker API method") |

content\_metadata table foreign keys

| Join content\_metadata with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` content_metadata.id = content_favorites.content_metadata_id ```  ``` content_metadata.parent_id = content_favorites.content_metadata_id ```  ``` content_metadata.id = content_favorites.dashboard.content_metadata_id ```  ``` content_metadata.parent_id = content_favorites.dashboard.content_metadata_id ```  ``` content_metadata.id = content_favorites.dashboard.folder.content_metadata_id ```  ``` content_metadata.parent_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` content_metadata.id = content_favorites.dashboard.space.content_metadata_id ```  ``` content_metadata.parent_id = content_favorites.dashboard.space.content_metadata_id ```  ``` content_metadata.id = content_favorites.look.content_metadata_id ```  ``` content_metadata.parent_id = content_favorites.look.content_metadata_id ```  ``` content_metadata.dashboard_id = content_favorites.dashboard.id ```  ``` content_metadata.dashboard_id = content_favorites.dashboard_id ```  ``` content_metadata.look_id = content_favorites.look_id ```  ``` content_metadata.look_id = content_favorites.look.id ```  ``` content_metadata.space_id = content_favorites.dashboard.space.id ```  ``` content_metadata.space_id = content_favorites.dashboard.space.parent_id ``` |
| [content\_metadata\_access](#content-metadata-access) | ``` content_metadata.id = content_metadata_access.content_metadata_id ```  ``` content_metadata.parent_id = content_metadata_access.content_metadata_id ``` |
| [content\_views](#content-views) | ``` content_metadata.id = content_views.content_metadata_id ```  ``` content_metadata.parent_id = content_views.content_metadata_id ```  ``` content_metadata.dashboard_id = content_views.dashboard_id ```  ``` content_metadata.look_id = content_views.look_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` content_metadata.id = dashboard_elements.look.content_metadata_id ```  ``` content_metadata.parent_id = dashboard_elements.look.content_metadata_id ```  ``` content_metadata.id = dashboard_elements.look.folder.content_metadata_id ```  ``` content_metadata.parent_id = dashboard_elements.look.folder.content_metadata_id ```  ``` content_metadata.id = dashboard_elements.look.space.content_metadata_id ```  ``` content_metadata.parent_id = dashboard_elements.look.space.content_metadata_id ```  ``` content_metadata.dashboard_id = dashboard_elements.dashboard_id ```  ``` content_metadata.look_id = dashboard_elements.look.id ```  ``` content_metadata.look_id = dashboard_elements.look_id ```  ``` content_metadata.space_id = dashboard_elements.look.space.id ```  ``` content_metadata.space_id = dashboard_elements.look.space.parent_id ``` |
| [dashboards](#dashboards) | ``` content_metadata.id = dashboards.content_metadata_id ```  ``` content_metadata.parent_id = dashboards.content_metadata_id ```  ``` content_metadata.id = dashboards.folder.content_metadata_id ```  ``` content_metadata.parent_id = dashboards.folder.content_metadata_id ```  ``` content_metadata.id = dashboards.space.content_metadata_id ```  ``` content_metadata.parent_id = dashboards.space.content_metadata_id ```  ``` content_metadata.dashboard_id = dashboards.id ```  ``` content_metadata.space_id = dashboards.space.id ```  ``` content_metadata.space_id = dashboards.space.parent_id ``` |
| [folders](#folders) | ``` content_metadata.id = folders.dashboards.folder.content_metadata_id ```  ``` content_metadata.parent_id = folders.dashboards.folder.content_metadata_id ```  ``` content_metadata.id = folders.dashboards.space.content_metadata_id ```  ``` content_metadata.parent_id = folders.dashboards.space.content_metadata_id ```  ``` content_metadata.id = folders.looks.content_metadata_id ```  ``` content_metadata.parent_id = folders.looks.content_metadata_id ```  ``` content_metadata.id = folders.looks.folder.content_metadata_id ```  ``` content_metadata.parent_id = folders.looks.folder.content_metadata_id ```  ``` content_metadata.dashboard_id = folders.dashboards.id ```  ``` content_metadata.look_id = folders.looks.id ```  ``` content_metadata.space_id = folders.dashboards.space.id ```  ``` content_metadata.space_id = folders.dashboards.space.parent_id ```  ``` content_metadata.space_id = folders.looks.space.id ```  ``` content_metadata.space_id = folders.looks.space.parent_id ```  ``` content_metadata.space_id = folders.looks.space_id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` content_metadata.id = lookml_dashboards.content_metadata_id ```  ``` content_metadata.parent_id = lookml_dashboards.content_metadata_id ```  ``` content_metadata.id = lookml_dashboards.folder.content_metadata_id ```  ``` content_metadata.parent_id = lookml_dashboards.folder.content_metadata_id ```  ``` content_metadata.id = lookml_dashboards.space.content_metadata_id ```  ``` content_metadata.parent_id = lookml_dashboards.space.content_metadata_id ```  ``` content_metadata.space_id = lookml_dashboards.space.id ```  ``` content_metadata.space_id = lookml_dashboards.space.parent_id ``` |
| [looks](#looks) | ``` content_metadata.id = looks.content_metadata_id ```  ``` content_metadata.parent_id = looks.content_metadata_id ```  ``` content_metadata.look_id = looks.id ```  ``` content_metadata.space_id = looks.space.id ```  ``` content_metadata.space_id = looks.space.parent_id ```  ``` content_metadata.space_id = looks.space_id ``` |
| [dashboard\_filters](#dashboard-filters) | ``` content_metadata.dashboard_id = dashboard_filters.dashboard_id ``` |
| [dashboard\_layouts](#dashboard-layouts) | ``` content_metadata.dashboard_id = dashboard_layouts.dashboard_id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` content_metadata.dashboard_id = scheduled_plans.dashboard_id ```  ``` content_metadata.look_id = scheduled_plans.look_id ``` |
| [users](#users) | ``` content_metadata.space_id = users.home_space_id ```  ``` content_metadata.space_id = users.personal_space_id ``` |

content\_metadata table schema

|  |
| --- |
| **content\_type**  STRING |
| **dashboard\_id**  STRING |
| **folder\_id**  STRING |
| **id**  STRING |
| **inheriting\_id**  STRING |
| **inherits**  BOOLEAN |
| **look\_id**  STRING |
| **name**  STRING |
| **parent\_id**  STRING |
| **slug**  STRING |
| **space\_id**  STRING |

### content\_metadata\_access

The `content_metadata_access` table contains information about content metadata access records in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#get_all_content_metadata_accesses "Opens in new tab: Looker API method") |

content\_metadata\_access table foreign keys

| Join content\_metadata\_access with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` content_metadata_access.content_metadata_id = content_favorites.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = content_favorites.look.content_metadata_id ``` |
| [content\_metadata](#content-metadata) | ``` content_metadata_access.content_metadata_id = content_metadata.id ```  ``` content_metadata_access.content_metadata_id = content_metadata.parent_id ``` |
| [content\_views](#content-views) | ``` content_metadata_access.content_metadata_id = content_views.content_metadata_id ```  ``` content_metadata_access.group_id = content_views.group_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` content_metadata_access.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = dashboard_elements.look.space.content_metadata_id ``` |
| [dashboards](#dashboards) | ``` content_metadata_access.content_metadata_id = dashboards.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = dashboards.space.content_metadata_id ``` |
| [folders](#folders) | ``` content_metadata_access.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = folders.looks.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = folders.looks.folder.content_metadata_id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` content_metadata_access.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` content_metadata_access.content_metadata_id = lookml_dashboards.space.content_metadata_id ``` |
| [looks](#looks) | ``` content_metadata_access.content_metadata_id = looks.content_metadata_id ``` |
| [groups](#groups) | ``` content_metadata_access.group_id = groups.id ``` |
| [groups\_in\_group](#groups-in-group) | ``` content_metadata_access.group_id = groups_in_group.id ```  ``` content_metadata_access.group_id = groups_in_group.parent_group_id ``` |
| [user\_attribute\_group\_values](#user-attribute-group-values) | ``` content_metadata_access.group_id = user_attribute_group_values.group_id ``` |
| [users](#users) | ``` content_metadata_access.group_id = users.group_ids ``` |

content\_metadata\_access table schema

|  |
| --- |
| **content\_metadata\_id**  STRING |
| **group\_id**  STRING |
| **id**  STRING |
| **permission\_type**  STRING |
| **user\_id**  STRING |

### content\_views

The `content_views` table contains info about user content views recorded in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user#search_users "Opens in new tab: Looker API method") |

content\_views table foreign keys

| Join content\_views with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` content_views.content_metadata_id = content_favorites.content_metadata_id ```  ``` content_views.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` content_views.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` content_views.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` content_views.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` content_views.dashboard_id = content_favorites.dashboard.id ```  ``` content_views.dashboard_id = content_favorites.dashboard_id ```  ``` content_views.look_id = content_favorites.look_id ```  ``` content_views.look_id = content_favorites.look.id ```  ``` content_views.user_id = content_favorites.dashboard.folder.creator_id ```  ``` content_views.user_id = content_favorites.dashboard.space.creator_id ```  ``` content_views.user_id = content_favorites.user_id ``` |
| [content\_metadata](#content-metadata) | ``` content_views.content_metadata_id = content_metadata.id ```  ``` content_views.content_metadata_id = content_metadata.parent_id ```  ``` content_views.dashboard_id = content_metadata.dashboard_id ```  ``` content_views.look_id = content_metadata.look_id ``` |
| [content\_metadata\_access](#content-metadata-access) | ``` content_views.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` content_views.group_id = content_metadata_access.group_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` content_views.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` content_views.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` content_views.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` content_views.dashboard_id = dashboard_elements.dashboard_id ```  ``` content_views.look_id = dashboard_elements.look.id ```  ``` content_views.look_id = dashboard_elements.look_id ```  ``` content_views.user_id = dashboard_elements.look.deleter_id ```  ``` content_views.user_id = dashboard_elements.look.folder.creator_id ```  ``` content_views.user_id = dashboard_elements.look.last_updater_id ```  ``` content_views.user_id = dashboard_elements.look.space.creator_id ```  ``` content_views.user_id = dashboard_elements.look.user.id ```  ``` content_views.user_id = dashboard_elements.look.user_id ``` |
| [dashboards](#dashboards) | ``` content_views.content_metadata_id = dashboards.content_metadata_id ```  ``` content_views.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` content_views.content_metadata_id = dashboards.space.content_metadata_id ```  ``` content_views.dashboard_id = dashboards.id ```  ``` content_views.user_id = dashboards.space.creator_id ```  ``` content_views.user_id = dashboards.user_id ``` |
| [folders](#folders) | ``` content_views.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` content_views.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` content_views.content_metadata_id = folders.looks.content_metadata_id ```  ``` content_views.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` content_views.dashboard_id = folders.dashboards.id ```  ``` content_views.look_id = folders.looks.id ```  ``` content_views.user_id = folders.creator_id ```  ``` content_views.user_id = folders.dashboards.user_id ```  ``` content_views.user_id = folders.dashboards.folder.creator_id ```  ``` content_views.user_id = folders.dashboards.space.creator_id ```  ``` content_views.user_id = folders.looks.deleter_id ```  ``` content_views.user_id = folders.looks.last_updater_id ```  ``` content_views.user_id = folders.looks.user.id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` content_views.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` content_views.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` content_views.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` content_views.user_id = lookml_dashboards.folder.creator_id ```  ``` content_views.user_id = lookml_dashboards.space.creator_id ```  ``` content_views.user_id = lookml_dashboards.user_id ``` |
| [looks](#looks) | ``` content_views.content_metadata_id = looks.content_metadata_id ```  ``` content_views.look_id = looks.id ```  ``` content_views.user_id = looks.deleter_id ```  ``` content_views.user_id = looks.folder.creator_id ```  ``` content_views.user_id = looks.user.id ```  ``` content_views.user_id = looks.user_id ``` |
| [dashboard\_filters](#dashboard-filters) | ``` content_views.dashboard_id = dashboard_filters.dashboard_id ``` |
| [dashboard\_layouts](#dashboard-layouts) | ``` content_views.dashboard_id = dashboard_layouts.dashboard_id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` content_views.dashboard_id = scheduled_plans.dashboard_id ```  ``` content_views.look_id = scheduled_plans.look_id ```  ``` content_views.user_id = scheduled_plans.user.id ```  ``` content_views.user_id = scheduled_plans.user_id ``` |
| [groups](#groups) | ``` content_views.group_id = groups.id ``` |
| [groups\_in\_group](#groups-in-group) | ``` content_views.group_id = groups_in_group.id ```  ``` content_views.group_id = groups_in_group.parent_group_id ``` |
| [user\_attribute\_group\_values](#user-attribute-group-values) | ``` content_views.group_id = user_attribute_group_values.group_id ``` |
| [users](#users) | ``` content_views.group_id = users.group_ids ```  ``` content_views.user_id = users.id ``` |
| [connections](#connections) | ``` content_views.user_id = connections.user_id ``` |
| [user\_login\_lockouts](#user-login-lockouts) | ``` content_views.user_id = user_login_lockouts.user_id ``` |

content\_views table schema

|  |
| --- |
| **content\_metadata\_id**  STRING |
| **dashboard\_id**  STRING |
| **favorite\_count**  INTEGER |
| **group\_id**  STRING |
| **id**  STRING |
| **last\_viewed\_at**  STRING |
| **look\_id**  STRING |
| **start\_of\_week\_date**  STRING |
| **user\_id**  STRING |
| **view\_count**  INTEGER |

### dashboard\_elements

The `dashboard_elements` table contains information about all dashboard elements in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboardelements "Opens in new tab: Looker API method") |

dashboard\_elements table foreign keys

| Join dashboard\_elements with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` dashboard_elements.look.content_favorite_id = content_favorites.id ```  ``` dashboard_elements.look.content_favorite_id = content_favorites.dashboard.content_favorite_id ```  ``` dashboard_elements.look.content_metadata_id = content_favorites.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = content_favorites.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = content_favorites.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` dashboard_elements.dashboard_id = content_favorites.dashboard.id ```  ``` dashboard_elements.dashboard_id = content_favorites.dashboard_id ```  ``` dashboard_elements.look.folder.id = content_favorites.dashboard.folder.id ```  ``` dashboard_elements.look.folder.parent_id = content_favorites.dashboard.folder.id ```  ``` dashboard_elements.look.folder_id = content_favorites.dashboard.folder.id ```  ``` dashboard_elements.look.folder.id = content_favorites.dashboard.folder.parent_id ```  ``` dashboard_elements.look.folder.parent_id = content_favorites.dashboard.folder.parent_id ```  ``` dashboard_elements.look.folder_id = content_favorites.dashboard.folder.parent_id ```  ``` dashboard_elements.look.id = content_favorites.look_id ```  ``` dashboard_elements.look_id = content_favorites.look_id ```  ``` dashboard_elements.look.id = content_favorites.look.id ```  ``` dashboard_elements.look_id = content_favorites.look.id ```  ``` dashboard_elements.look.model.id = content_favorites.dashboard.model.id ```  ``` dashboard_elements.look.space.id = content_favorites.dashboard.space.id ```  ``` dashboard_elements.look.space.parent_id = content_favorites.dashboard.space.id ```  ``` dashboard_elements.look.space.id = content_favorites.dashboard.space.parent_id ```  ``` dashboard_elements.look.space.parent_id = content_favorites.dashboard.space.parent_id ```  ``` dashboard_elements.look.deleter_id = content_favorites.dashboard.folder.creator_id ```  ``` dashboard_elements.look.folder.creator_id = content_favorites.dashboard.folder.creator_id ```  ``` dashboard_elements.look.last_updater_id = content_favorites.dashboard.folder.creator_id ```  ``` dashboard_elements.look.space.creator_id = content_favorites.dashboard.folder.creator_id ```  ``` dashboard_elements.look.user.id = content_favorites.dashboard.folder.creator_id ```  ``` dashboard_elements.look.user_id = content_favorites.dashboard.folder.creator_id ```  ``` dashboard_elements.look.deleter_id = content_favorites.dashboard.space.creator_id ```  ``` dashboard_elements.look.folder.creator_id = content_favorites.dashboard.space.creator_id ```  ``` dashboard_elements.look.last_updater_id = content_favorites.dashboard.space.creator_id ```  ``` dashboard_elements.look.space.creator_id = content_favorites.dashboard.space.creator_id ```  ``` dashboard_elements.look.user.id = content_favorites.dashboard.space.creator_id ```  ``` dashboard_elements.look.user_id = content_favorites.dashboard.space.creator_id ```  ``` dashboard_elements.look.deleter_id = content_favorites.user_id ```  ``` dashboard_elements.look.folder.creator_id = content_favorites.user_id ```  ``` dashboard_elements.look.last_updater_id = content_favorites.user_id ```  ``` dashboard_elements.look.space.creator_id = content_favorites.user_id ```  ``` dashboard_elements.look.user.id = content_favorites.user_id ```  ``` dashboard_elements.look.user_id = content_favorites.user_id ``` |
| [dashboards](#dashboards) | ``` dashboard_elements.look.content_favorite_id = dashboards.content_favorite_id ```  ``` dashboard_elements.look.content_metadata_id = dashboards.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = dashboards.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = dashboards.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = dashboards.space.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = dashboards.space.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = dashboards.space.content_metadata_id ```  ``` dashboard_elements.dashboard_id = dashboards.id ```  ``` dashboard_elements.look.folder.id = dashboards.folder.id ```  ``` dashboard_elements.look.folder.parent_id = dashboards.folder.id ```  ``` dashboard_elements.look.folder_id = dashboards.folder.id ```  ``` dashboard_elements.look.folder.id = dashboards.folder.parent_id ```  ``` dashboard_elements.look.folder.parent_id = dashboards.folder.parent_id ```  ``` dashboard_elements.look.folder_id = dashboards.folder.parent_id ```  ``` dashboard_elements.look.model.id = dashboards.model.id ```  ``` dashboard_elements.look.space.id = dashboards.space.id ```  ``` dashboard_elements.look.space.parent_id = dashboards.space.id ```  ``` dashboard_elements.look.space.id = dashboards.space.parent_id ```  ``` dashboard_elements.look.space.parent_id = dashboards.space.parent_id ```  ``` dashboard_elements.look.deleter_id = dashboards.space.creator_id ```  ``` dashboard_elements.look.folder.creator_id = dashboards.space.creator_id ```  ``` dashboard_elements.look.last_updater_id = dashboards.space.creator_id ```  ``` dashboard_elements.look.space.creator_id = dashboards.space.creator_id ```  ``` dashboard_elements.look.user.id = dashboards.space.creator_id ```  ``` dashboard_elements.look.user_id = dashboards.space.creator_id ```  ``` dashboard_elements.look.deleter_id = dashboards.user_id ```  ``` dashboard_elements.look.folder.creator_id = dashboards.user_id ```  ``` dashboard_elements.look.last_updater_id = dashboards.user_id ```  ``` dashboard_elements.look.space.creator_id = dashboards.user_id ```  ``` dashboard_elements.look.user.id = dashboards.user_id ```  ``` dashboard_elements.look.user_id = dashboards.user_id ``` |
| [folders](#folders) | ``` dashboard_elements.look.content_favorite_id = folders.dashboards.content_favorite_id ```  ``` dashboard_elements.look.content_favorite_id = folders.looks.content_favorite_id ```  ``` dashboard_elements.look.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = folders.looks.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = folders.looks.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = folders.looks.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` dashboard_elements.dashboard_id = folders.dashboards.id ```  ``` dashboard_elements.look.folder.id = folders.id ```  ``` dashboard_elements.look.folder.parent_id = folders.id ```  ``` dashboard_elements.look.folder_id = folders.id ```  ``` dashboard_elements.look.folder.id = folders.dashboards.folder.id ```  ``` dashboard_elements.look.folder.parent_id = folders.dashboards.folder.id ```  ``` dashboard_elements.look.folder_id = folders.dashboards.folder.id ```  ``` dashboard_elements.look.folder.id = folders.dashboards.folder.parent_id ```  ``` dashboard_elements.look.folder.parent_id = folders.dashboards.folder.parent_id ```  ``` dashboard_elements.look.folder_id = folders.dashboards.folder.parent_id ```  ``` dashboard_elements.look.folder.id = folders.looks.folder.id ```  ``` dashboard_elements.look.folder.parent_id = folders.looks.folder.id ```  ``` dashboard_elements.look.folder_id = folders.looks.folder.id ```  ``` dashboard_elements.look.folder.id = folders.looks.folder.parent_id ```  ``` dashboard_elements.look.folder.parent_id = folders.looks.folder.parent_id ```  ``` dashboard_elements.look.folder_id = folders.looks.folder.parent_id ```  ``` dashboard_elements.look.folder.id = folders.parent_id ```  ``` dashboard_elements.look.folder.parent_id = folders.parent_id ```  ``` dashboard_elements.look.folder_id = folders.parent_id ```  ``` dashboard_elements.look.id = folders.looks.id ```  ``` dashboard_elements.look_id = folders.looks.id ```  ``` dashboard_elements.look.model.id = folders.dashboards.model.id ```  ``` dashboard_elements.look.model.id = folders.looks.model.id ```  ``` dashboard_elements.look.query.id = folders.looks.query_id ```  ``` dashboard_elements.look.query_id = folders.looks.query_id ```  ``` dashboard_elements.query.id = folders.looks.query_id ```  ``` dashboard_elements.query_id = folders.looks.query_id ```  ``` dashboard_elements.result_maker.query.id = folders.looks.query_id ```  ``` dashboard_elements.result_maker.query_id = folders.looks.query_id ```  ``` dashboard_elements.look.space.id = folders.dashboards.space.id ```  ``` dashboard_elements.look.space.parent_id = folders.dashboards.space.id ```  ``` dashboard_elements.look.space.id = folders.dashboards.space.parent_id ```  ``` dashboard_elements.look.space.parent_id = folders.dashboards.space.parent_id ```  ``` dashboard_elements.look.space.id = folders.looks.space.id ```  ``` dashboard_elements.look.space.parent_id = folders.looks.space.id ```  ``` dashboard_elements.look.space.id = folders.looks.space.parent_id ```  ``` dashboard_elements.look.space.parent_id = folders.looks.space.parent_id ```  ``` dashboard_elements.look.space.id = folders.looks.space_id ```  ``` dashboard_elements.look.space.parent_id = folders.looks.space_id ```  ``` dashboard_elements.look.deleter_id = folders.creator_id ```  ``` dashboard_elements.look.folder.creator_id = folders.creator_id ```  ``` dashboard_elements.look.last_updater_id = folders.creator_id ```  ``` dashboard_elements.look.space.creator_id = folders.creator_id ```  ``` dashboard_elements.look.user.id = folders.creator_id ```  ``` dashboard_elements.look.user_id = folders.creator_id ```  ``` dashboard_elements.look.deleter_id = folders.dashboards.user_id ```  ``` dashboard_elements.look.folder.creator_id = folders.dashboards.user_id ```  ``` dashboard_elements.look.last_updater_id = folders.dashboards.user_id ```  ``` dashboard_elements.look.space.creator_id = folders.dashboards.user_id ```  ``` dashboard_elements.look.user.id = folders.dashboards.user_id ```  ``` dashboard_elements.look.user_id = folders.dashboards.user_id ```  ``` dashboard_elements.look.deleter_id = folders.dashboards.folder.creator_id ```  ``` dashboard_elements.look.folder.creator_id = folders.dashboards.folder.creator_id ```  ``` dashboard_elements.look.last_updater_id = folders.dashboards.folder.creator_id ```  ``` dashboard_elements.look.space.creator_id = folders.dashboards.folder.creator_id ```  ``` dashboard_elements.look.user.id = folders.dashboards.folder.creator_id ```  ``` dashboard_elements.look.user_id = folders.dashboards.folder.creator_id ```  ``` dashboard_elements.look.deleter_id = folders.dashboards.space.creator_id ```  ``` dashboard_elements.look.folder.creator_id = folders.dashboards.space.creator_id ```  ``` dashboard_elements.look.last_updater_id = folders.dashboards.space.creator_id ```  ``` dashboard_elements.look.space.creator_id = folders.dashboards.space.creator_id ```  ``` dashboard_elements.look.user.id = folders.dashboards.space.creator_id ```  ``` dashboard_elements.look.user_id = folders.dashboards.space.creator_id ```  ``` dashboard_elements.look.deleter_id = folders.looks.deleter_id ```  ``` dashboard_elements.look.folder.creator_id = folders.looks.deleter_id ```  ``` dashboard_elements.look.last_updater_id = folders.looks.deleter_id ```  ``` dashboard_elements.look.space.creator_id = folders.looks.deleter_id ```  ``` dashboard_elements.look.user.id = folders.looks.deleter_id ```  ``` dashboard_elements.look.user_id = folders.looks.deleter_id ```  ``` dashboard_elements.look.deleter_id = folders.looks.last_updater_id ```  ``` dashboard_elements.look.folder.creator_id = folders.looks.last_updater_id ```  ``` dashboard_elements.look.last_updater_id = folders.looks.last_updater_id ```  ``` dashboard_elements.look.space.creator_id = folders.looks.last_updater_id ```  ``` dashboard_elements.look.user.id = folders.looks.last_updater_id ```  ``` dashboard_elements.look.user_id = folders.looks.last_updater_id ```  ``` dashboard_elements.look.deleter_id = folders.looks.user.id ```  ``` dashboard_elements.look.folder.creator_id = folders.looks.user.id ```  ``` dashboard_elements.look.last_updater_id = folders.looks.user.id ```  ``` dashboard_elements.look.space.creator_id = folders.looks.user.id ```  ``` dashboard_elements.look.user.id = folders.looks.user.id ```  ``` dashboard_elements.look.user_id = folders.looks.user.id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` dashboard_elements.look.content_favorite_id = lookml_dashboards.content_favorite_id ```  ``` dashboard_elements.look.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` dashboard_elements.look.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` dashboard_elements.look.folder.id = lookml_dashboards.folder.id ```  ``` dashboard_elements.look.folder.parent_id = lookml_dashboards.folder.id ```  ``` dashboard_elements.look.folder_id = lookml_dashboards.folder.id ```  ``` dashboard_elements.look.folder.id = lookml_dashboards.folder.parent_id ```  ``` dashboard_elements.look.folder.parent_id = lookml_dashboards.folder.parent_id ```  ``` dashboard_elements.look.folder_id = lookml_dashboards.folder.parent_id ```  ``` dashboard_elements.look.model.id = lookml_dashboards.model.id ```  ``` dashboard_elements.look.space.id = lookml_dashboards.space.id ```  ``` dashboard_elements.look.space.parent_id = lookml_dashboards.space.id ```  ``` dashboard_elements.look.space.id = lookml_dashboards.space.parent_id ```  ``` dashboard_elements.look.space.parent_id = lookml_dashboards.space.parent_id ```  ``` dashboard_elements.look.deleter_id = lookml_dashboards.folder.creator_id ```  ``` dashboard_elements.look.folder.creator_id = lookml_dashboards.folder.creator_id ```  ``` dashboard_elements.look.last_updater_id = lookml_dashboards.folder.creator_id ```  ``` dashboard_elements.look.space.creator_id = lookml_dashboards.folder.creator_id ```  ``` dashboard_elements.look.user.id = lookml_dashboards.folder.creator_id ```  ``` dashboard_elements.look.user_id = lookml_dashboards.folder.creator_id ```  ``` dashboard_elements.look.deleter_id = lookml_dashboards.space.creator_id ```  ``` dashboard_elements.look.folder.creator_id = lookml_dashboards.space.creator_id ```  ``` dashboard_elements.look.last_updater_id = lookml_dashboards.space.creator_id ```  ``` dashboard_elements.look.space.creator_id = lookml_dashboards.space.creator_id ```  ``` dashboard_elements.look.user.id = lookml_dashboards.space.creator_id ```  ``` dashboard_elements.look.user_id = lookml_dashboards.space.creator_id ```  ``` dashboard_elements.look.deleter_id = lookml_dashboards.user_id ```  ``` dashboard_elements.look.folder.creator_id = lookml_dashboards.user_id ```  ``` dashboard_elements.look.last_updater_id = lookml_dashboards.user_id ```  ``` dashboard_elements.look.space.creator_id = lookml_dashboards.user_id ```  ``` dashboard_elements.look.user.id = lookml_dashboards.user_id ```  ``` dashboard_elements.look.user_id = lookml_dashboards.user_id ``` |
| [looks](#looks) | ``` dashboard_elements.look.content_favorite_id = looks.content_favorite_id ```  ``` dashboard_elements.look.content_metadata_id = looks.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = looks.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = looks.content_metadata_id ```  ``` dashboard_elements.look.folder.id = looks.folder.id ```  ``` dashboard_elements.look.folder.parent_id = looks.folder.id ```  ``` dashboard_elements.look.folder_id = looks.folder.id ```  ``` dashboard_elements.look.folder.id = looks.folder_id ```  ``` dashboard_elements.look.folder.parent_id = looks.folder_id ```  ``` dashboard_elements.look.folder_id = looks.folder_id ```  ``` dashboard_elements.look.folder.id = looks.folder.parent_id ```  ``` dashboard_elements.look.folder.parent_id = looks.folder.parent_id ```  ``` dashboard_elements.look.folder_id = looks.folder.parent_id ```  ``` dashboard_elements.look.id = looks.id ```  ``` dashboard_elements.look_id = looks.id ```  ``` dashboard_elements.look.model.id = looks.model.id ```  ``` dashboard_elements.look.query.id = looks.query_id ```  ``` dashboard_elements.look.query_id = looks.query_id ```  ``` dashboard_elements.query.id = looks.query_id ```  ``` dashboard_elements.query_id = looks.query_id ```  ``` dashboard_elements.result_maker.query.id = looks.query_id ```  ``` dashboard_elements.result_maker.query_id = looks.query_id ```  ``` dashboard_elements.look.space.id = looks.space.id ```  ``` dashboard_elements.look.space.parent_id = looks.space.id ```  ``` dashboard_elements.look.space.id = looks.space.parent_id ```  ``` dashboard_elements.look.space.parent_id = looks.space.parent_id ```  ``` dashboard_elements.look.space.id = looks.space_id ```  ``` dashboard_elements.look.space.parent_id = looks.space_id ```  ``` dashboard_elements.look.deleter_id = looks.deleter_id ```  ``` dashboard_elements.look.folder.creator_id = looks.deleter_id ```  ``` dashboard_elements.look.last_updater_id = looks.deleter_id ```  ``` dashboard_elements.look.space.creator_id = looks.deleter_id ```  ``` dashboard_elements.look.user.id = looks.deleter_id ```  ``` dashboard_elements.look.user_id = looks.deleter_id ```  ``` dashboard_elements.look.deleter_id = looks.folder.creator_id ```  ``` dashboard_elements.look.folder.creator_id = looks.folder.creator_id ```  ``` dashboard_elements.look.last_updater_id = looks.folder.creator_id ```  ``` dashboard_elements.look.space.creator_id = looks.folder.creator_id ```  ``` dashboard_elements.look.user.id = looks.folder.creator_id ```  ``` dashboard_elements.look.user_id = looks.folder.creator_id ```  ``` dashboard_elements.look.deleter_id = looks.user.id ```  ``` dashboard_elements.look.folder.creator_id = looks.user.id ```  ``` dashboard_elements.look.last_updater_id = looks.user.id ```  ``` dashboard_elements.look.space.creator_id = looks.user.id ```  ``` dashboard_elements.look.user.id = looks.user.id ```  ``` dashboard_elements.look.user_id = looks.user.id ```  ``` dashboard_elements.look.deleter_id = looks.user_id ```  ``` dashboard_elements.look.folder.creator_id = looks.user_id ```  ``` dashboard_elements.look.last_updater_id = looks.user_id ```  ``` dashboard_elements.look.space.creator_id = looks.user_id ```  ``` dashboard_elements.look.user.id = looks.user_id ```  ``` dashboard_elements.look.user_id = looks.user_id ``` |
| [content\_metadata](#content-metadata) | ``` dashboard_elements.look.content_metadata_id = content_metadata.id ```  ``` dashboard_elements.look.folder.content_metadata_id = content_metadata.id ```  ``` dashboard_elements.look.space.content_metadata_id = content_metadata.id ```  ``` dashboard_elements.look.content_metadata_id = content_metadata.parent_id ```  ``` dashboard_elements.look.folder.content_metadata_id = content_metadata.parent_id ```  ``` dashboard_elements.look.space.content_metadata_id = content_metadata.parent_id ```  ``` dashboard_elements.dashboard_id = content_metadata.dashboard_id ```  ``` dashboard_elements.look.id = content_metadata.look_id ```  ``` dashboard_elements.look_id = content_metadata.look_id ```  ``` dashboard_elements.look.space.id = content_metadata.space_id ```  ``` dashboard_elements.look.space.parent_id = content_metadata.space_id ``` |
| [content\_metadata\_access](#content-metadata-access) | ``` dashboard_elements.look.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = content_metadata_access.content_metadata_id ``` |
| [content\_views](#content-views) | ``` dashboard_elements.look.content_metadata_id = content_views.content_metadata_id ```  ``` dashboard_elements.look.folder.content_metadata_id = content_views.content_metadata_id ```  ``` dashboard_elements.look.space.content_metadata_id = content_views.content_metadata_id ```  ``` dashboard_elements.dashboard_id = content_views.dashboard_id ```  ``` dashboard_elements.look.id = content_views.look_id ```  ``` dashboard_elements.look_id = content_views.look_id ```  ``` dashboard_elements.look.deleter_id = content_views.user_id ```  ``` dashboard_elements.look.folder.creator_id = content_views.user_id ```  ``` dashboard_elements.look.last_updater_id = content_views.user_id ```  ``` dashboard_elements.look.space.creator_id = content_views.user_id ```  ``` dashboard_elements.look.user.id = content_views.user_id ```  ``` dashboard_elements.look.user_id = content_views.user_id ``` |
| [dashboard\_filters](#dashboard-filters) | ``` dashboard_elements.dashboard_id = dashboard_filters.dashboard_id ``` |
| [dashboard\_layouts](#dashboard-layouts) | ``` dashboard_elements.dashboard_id = dashboard_layouts.dashboard_id ```  ``` dashboard_elements.id = dashboard_layouts.dashboard_layout_components.dashboard_element_id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` dashboard_elements.dashboard_id = scheduled_plans.dashboard_id ```  ``` dashboard_elements.look.id = scheduled_plans.look_id ```  ``` dashboard_elements.look_id = scheduled_plans.look_id ```  ``` dashboard_elements.look.query.id = scheduled_plans.query_id ```  ``` dashboard_elements.look.query_id = scheduled_plans.query_id ```  ``` dashboard_elements.query.id = scheduled_plans.query_id ```  ``` dashboard_elements.query_id = scheduled_plans.query_id ```  ``` dashboard_elements.result_maker.query.id = scheduled_plans.query_id ```  ``` dashboard_elements.result_maker.query_id = scheduled_plans.query_id ```  ``` dashboard_elements.look.deleter_id = scheduled_plans.user.id ```  ``` dashboard_elements.look.folder.creator_id = scheduled_plans.user.id ```  ``` dashboard_elements.look.last_updater_id = scheduled_plans.user.id ```  ``` dashboard_elements.look.space.creator_id = scheduled_plans.user.id ```  ``` dashboard_elements.look.user.id = scheduled_plans.user.id ```  ``` dashboard_elements.look.user_id = scheduled_plans.user.id ```  ``` dashboard_elements.look.deleter_id = scheduled_plans.user_id ```  ``` dashboard_elements.look.folder.creator_id = scheduled_plans.user_id ```  ``` dashboard_elements.look.last_updater_id = scheduled_plans.user_id ```  ``` dashboard_elements.look.space.creator_id = scheduled_plans.user_id ```  ``` dashboard_elements.look.user.id = scheduled_plans.user_id ```  ``` dashboard_elements.look.user_id = scheduled_plans.user_id ``` |
| [users](#users) | ``` dashboard_elements.look.folder.id = users.home_folder_id ```  ``` dashboard_elements.look.folder.parent_id = users.home_folder_id ```  ``` dashboard_elements.look.folder_id = users.home_folder_id ```  ``` dashboard_elements.look.folder.id = users.personal_folder_id ```  ``` dashboard_elements.look.folder.parent_id = users.personal_folder_id ```  ``` dashboard_elements.look.folder_id = users.personal_folder_id ```  ``` dashboard_elements.look.space.id = users.home_space_id ```  ``` dashboard_elements.look.space.parent_id = users.home_space_id ```  ``` dashboard_elements.look.space.id = users.personal_space_id ```  ``` dashboard_elements.look.space.parent_id = users.personal_space_id ```  ``` dashboard_elements.look.deleter_id = users.id ```  ``` dashboard_elements.look.folder.creator_id = users.id ```  ``` dashboard_elements.look.last_updater_id = users.id ```  ``` dashboard_elements.look.space.creator_id = users.id ```  ``` dashboard_elements.look.user.id = users.id ```  ``` dashboard_elements.look.user_id = users.id ``` |
| [roles](#roles) | ``` dashboard_elements.look.model.id = roles.model_set.models ``` |
| [queries](#queries) | ``` dashboard_elements.look.query.id = queries.id ```  ``` dashboard_elements.look.query_id = queries.id ```  ``` dashboard_elements.query.id = queries.id ```  ``` dashboard_elements.query_id = queries.id ```  ``` dashboard_elements.result_maker.query.id = queries.id ```  ``` dashboard_elements.result_maker.query_id = queries.id ``` |
| [connections](#connections) | ``` dashboard_elements.look.deleter_id = connections.user_id ```  ``` dashboard_elements.look.folder.creator_id = connections.user_id ```  ``` dashboard_elements.look.last_updater_id = connections.user_id ```  ``` dashboard_elements.look.space.creator_id = connections.user_id ```  ``` dashboard_elements.look.user.id = connections.user_id ```  ``` dashboard_elements.look.user_id = connections.user_id ``` |
| [user\_login\_lockouts](#user-login-lockouts) | ``` dashboard_elements.look.deleter_id = user_login_lockouts.user_id ```  ``` dashboard_elements.look.folder.creator_id = user_login_lockouts.user_id ```  ``` dashboard_elements.look.last_updater_id = user_login_lockouts.user_id ```  ``` dashboard_elements.look.space.creator_id = user_login_lockouts.user_id ```  ``` dashboard_elements.look.user.id = user_login_lockouts.user_id ```  ``` dashboard_elements.look.user_id = user_login_lockouts.user_id ``` |

dashboard\_elements table schema

|  |
| --- |
| **alert\_count**  INTEGER |
| **body\_text**  STRING |
| **body\_text\_as\_html**  STRING |
| **dashboard\_id**  STRING |
| **edit\_uri**  STRING |
| **id**  STRING |
| **look**  OBJECT This is a nested data structure:   - content\_favorite\_id: STRING - content\_metadata\_id: STRING - created\_at: DATE-TIME - deleted: BOOLEAN - deleted\_at: DATE-TIME - deleter\_id: STRING - description: STRING - embed\_url: STRING - excel\_file\_url: STRING - favorite\_count: INTEGER - folder: OBJECT, which is also a nested data structure.   - child\_count: INTEGER   - content\_metadata\_id: STRING   - creator\_id: STRING   - external\_id: STRING   - id: STRING   - is\_embed: BOOLEAN   - is\_embed\_shared\_root: BOOLEAN   - is\_embed\_users\_root: BOOLEAN   - is\_personal: BOOLEAN   - is\_personal\_descendant: BOOLEAN   - is\_shared\_root: BOOLEAN   - is\_users\_root: BOOLEAN   - name: STRING   - parent\_id: STRING - folder\_id: STRING - google\_spreadsheet\_formula: STRING - id: STRING - image\_embed\_url: STRING - is\_run\_on\_load: BOOLEAN - last\_accessed\_at: DATE-TIME - last\_updater\_id: STRING - last\_viewed\_at: DATE-TIME - model: OBJECT, which is also a nested data structure.   - id: STRING   - label: STRING - public: BOOLEAN - public\_slug: STRING - public\_url: STRING - query: OBJECT, which is also a nested data structure.   - client\_id: STRING   - column\_limit: STRING   - dynamic\_fields: STRING   - expanded\_share\_url: STRING   - fields: ARRAY, which is also a nested data structure.   - fill\_fields: ARRAY, which is also a nested data structure.   - filter\_config: OBJECT, which is also a nested data structure.   - filter\_expression: STRING   - filters: OBJECT, which is also a nested data structure.   - has\_table\_calculations: BOOLEAN   - id: STRING   - limit: STRING   - model: STRING   - pivots: ARRAY, which is also a nested data structure.   - query\_timezone: STRING   - row\_total: STRING   - runtime: NUMBER   - share\_url: STRING   - slug: STRING   - sorts: ARRAY, which is also a nested data structure.   - subtotals: ARRAY, which is also a nested data structure.   - total: BOOLEAN   - url: STRING   - view: STRING   - vis\_config: OBJECT, which is also a nested data structure.   - visible\_ui\_sections: STRING - query\_id: STRING - short\_url: STRING - space: OBJECT, which is also a nested data structure.   - child\_count: INTEGER   - content\_metadata\_id: STRING   - creator\_id: STRING   - external\_id: STRING   - id: STRING   - is\_embed: BOOLEAN   - is\_embed\_shared\_root: BOOLEAN   - is\_embed\_users\_root: BOOLEAN   - is\_personal: BOOLEAN   - is\_personal\_descendant: BOOLEAN   - is\_shared\_root: BOOLEAN   - is\_users\_root: BOOLEAN   - name: STRING   - parent\_id: STRING - space\_id: STRING - title: STRING - updated\_at: DATE-TIME - url: STRING - user: OBJECT, which is also a nested data structure.   - id: STRING - user\_id: STRING - view\_count: INTEGER |
| **look\_id**  STRING |
| **lookml\_link\_id**  STRING |
| **merge\_result\_id**  STRING |
| **note\_display**  STRING |
| **note\_state**  STRING |
| **note\_text**  STRING |
| **note\_text\_as\_html**  STRING |
| **query**  OBJECT This is a nested data structure:   - client\_id: STRING - column\_limit: STRING - dynamic\_fields: STRING - expanded\_share\_url: STRING - fields: ARRAY, which is also a nested data structure. - fill\_fields: ARRAY, which is also a nested data structure. - filter\_config: OBJECT, which is also a nested data structure. - filter\_expression: STRING - filters: OBJECT, which is also a nested data structure. - has\_table\_calculations: BOOLEAN - id: STRING - limit: STRING - model: STRING - pivots: ARRAY, which is also a nested data structure. - query\_timezone: STRING - row\_total: STRING - runtime: NUMBER - share\_url: STRING - slug: STRING - sorts: ARRAY, which is also a nested data structure. - subtotals: ARRAY, which is also a nested data structure. - total: BOOLEAN - url: STRING - view: STRING - vis\_config: OBJECT, which is also a nested data structure. - visible\_ui\_sections: STRING |
| **query\_id**  STRING |
| **refresh\_interval**  STRING |
| **refresh\_interval\_to\_i**  INTEGER |
| **result\_maker**  OBJECT This is a nested data structure:   - dynamic\_fields: STRING - filterables: ARRAY, which is also a nested data structure.   - listen: ARRAY, which is also a nested data structure.     - dashboard\_filter\_name: STRING     - field: STRING   - model: STRING   - name: STRING   - view: STRING - id: STRING - merge\_result\_id: STRING - query: OBJECT, which is also a nested data structure.   - client\_id: STRING   - column\_limit: STRING   - dynamic\_fields: STRING   - expanded\_share\_url: STRING   - fields: ARRAY, which is also a nested data structure.   - fill\_fields: ARRAY, which is also a nested data structure.   - filter\_config: OBJECT, which is also a nested data structure.   - filter\_expression: STRING   - filters: OBJECT, which is also a nested data structure.   - has\_table\_calculations: BOOLEAN   - id: STRING   - limit: STRING   - model: STRING   - pivots: ARRAY, which is also a nested data structure.   - query\_timezone: STRING   - row\_total: STRING   - runtime: NUMBER   - share\_url: STRING   - slug: STRING   - sorts: ARRAY, which is also a nested data structure.   - subtotals: ARRAY, which is also a nested data structure.   - total: BOOLEAN   - url: STRING   - view: STRING   - vis\_config: OBJECT, which is also a nested data structure.   - visible\_ui\_sections: STRING - query\_id: STRING - sorts: ARRAY, which is also a nested data structure. - total: BOOLEAN - vis\_config: OBJECT, which is also a nested data structure. |
| **result\_maker\_id**  STRING |
| **subtitle\_text**  STRING |
| **title**  STRING |
| **title\_hidden**  BOOLEAN |
| **title\_text**  STRING |
| **type**  STRING |

### dashboard\_filters

The `dashboard_filters` table contains information about all dashboard filters in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboard_filters "Opens in new tab: Looker API method") |

dashboard\_filters table foreign keys

| Join dashboard\_filters with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` dashboard_filters.dashboard_id = content_favorites.dashboard.id ```  ``` dashboard_filters.dashboard_id = content_favorites.dashboard_id ``` |
| [content\_metadata](#content-metadata) | ``` dashboard_filters.dashboard_id = content_metadata.dashboard_id ``` |
| [content\_views](#content-views) | ``` dashboard_filters.dashboard_id = content_views.dashboard_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` dashboard_filters.dashboard_id = dashboard_elements.dashboard_id ``` |
| [dashboard\_layouts](#dashboard-layouts) | ``` dashboard_filters.dashboard_id = dashboard_layouts.dashboard_id ``` |
| [dashboards](#dashboards) | ``` dashboard_filters.dashboard_id = dashboards.id ``` |
| [folders](#folders) | ``` dashboard_filters.dashboard_id = folders.dashboards.id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` dashboard_filters.dashboard_id = scheduled_plans.dashboard_id ``` |

dashboard\_filters table schema

|  |
| --- |
| **allow\_multiple\_values**  BOOLEAN |
| **dashboard\_id**  STRING |
| **default\_value**  STRING |
| **dimension**  STRING |
| **explore**  STRING |
| **field**  OBJECT This is a nested data structure. |
| **id**  STRING |
| **listens\_to\_filters**  ARRAY This is a nested data structure. |
| **model**  STRING |
| **name**  STRING |
| **required**  BOOLEAN |
| **row**  INTEGER |
| **title**  STRING |
| **type**  STRING |
| **ui\_config**  OBJECT This is a nested data structure. |

### dashboard\_layouts

The `dashboard_layouts` table contains information about all dashboard layouts in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboardlayouts "Opens in new tab: Looker API method") |

dashboard\_layouts table foreign keys

| Join dashboard\_layouts with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` dashboard_layouts.dashboard_id = content_favorites.dashboard.id ```  ``` dashboard_layouts.dashboard_id = content_favorites.dashboard_id ``` |
| [content\_metadata](#content-metadata) | ``` dashboard_layouts.dashboard_id = content_metadata.dashboard_id ``` |
| [content\_views](#content-views) | ``` dashboard_layouts.dashboard_id = content_views.dashboard_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` dashboard_layouts.dashboard_id = dashboard_elements.dashboard_id ```  ``` dashboard_layouts.dashboard_layout_components.dashboard_element_id = dashboard_elements.id ``` |
| [dashboard\_filters](#dashboard-filters) | ``` dashboard_layouts.dashboard_id = dashboard_filters.dashboard_id ``` |
| [dashboards](#dashboards) | ``` dashboard_layouts.dashboard_id = dashboards.id ``` |
| [folders](#folders) | ``` dashboard_layouts.dashboard_id = folders.dashboards.id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` dashboard_layouts.dashboard_id = scheduled_plans.dashboard_id ``` |

dashboard\_layouts table schema

|  |
| --- |
| **active**  BOOLEAN |
| **column\_width**  INTEGER |
| **dashboard\_id**  STRING |
| **dashboard\_layout\_components**  ARRAY This is a nested data structure:   - column: INTEGER - dashboard\_element\_id: STRING - dashboard\_layout\_id: STRING - deleted: BOOLEAN - element\_title: STRING - element\_title\_hidden: BOOLEAN - height: INTEGER - id: STRING - row: INTEGER - vis\_type: STRING - width: INTEGER |
| **dashboard\_title**  STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **type**  STRING |
| **width**  INTEGER |

### dashboards

The `dashboards` table contains information about all active dashboards in your Looker account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboards "Opens in new tab: Looker API method") |

dashboards table foreign keys

| Join dashboards with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` dashboards.content_favorite_id = content_favorites.id ```  ``` dashboards.content_favorite_id = content_favorites.dashboard.content_favorite_id ```  ``` dashboards.content_metadata_id = content_favorites.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = content_favorites.content_metadata_id ```  ``` dashboards.space.content_metadata_id = content_favorites.content_metadata_id ```  ``` dashboards.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` dashboards.space.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` dashboards.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` dashboards.space.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` dashboards.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` dashboards.space.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` dashboards.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` dashboards.space.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` dashboards.id = content_favorites.dashboard.id ```  ``` dashboards.id = content_favorites.dashboard_id ```  ``` dashboards.folder.id = content_favorites.dashboard.folder.id ```  ``` dashboards.folder.parent_id = content_favorites.dashboard.folder.id ```  ``` dashboards.folder.id = content_favorites.dashboard.folder.parent_id ```  ``` dashboards.folder.parent_id = content_favorites.dashboard.folder.parent_id ```  ``` dashboards.model.id = content_favorites.dashboard.model.id ```  ``` dashboards.space.id = content_favorites.dashboard.space.id ```  ``` dashboards.space.parent_id = content_favorites.dashboard.space.id ```  ``` dashboards.space.id = content_favorites.dashboard.space.parent_id ```  ``` dashboards.space.parent_id = content_favorites.dashboard.space.parent_id ```  ``` dashboards.space.creator_id = content_favorites.dashboard.folder.creator_id ```  ``` dashboards.user_id = content_favorites.dashboard.folder.creator_id ```  ``` dashboards.space.creator_id = content_favorites.dashboard.space.creator_id ```  ``` dashboards.user_id = content_favorites.dashboard.space.creator_id ```  ``` dashboards.space.creator_id = content_favorites.user_id ```  ``` dashboards.user_id = content_favorites.user_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` dashboards.content_favorite_id = dashboard_elements.look.content_favorite_id ```  ``` dashboards.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` dashboards.space.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` dashboards.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` dashboards.space.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` dashboards.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` dashboards.space.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` dashboards.id = dashboard_elements.dashboard_id ```  ``` dashboards.folder.id = dashboard_elements.look.folder.id ```  ``` dashboards.folder.parent_id = dashboard_elements.look.folder.id ```  ``` dashboards.folder.id = dashboard_elements.look.folder.parent_id ```  ``` dashboards.folder.parent_id = dashboard_elements.look.folder.parent_id ```  ``` dashboards.folder.id = dashboard_elements.look.folder_id ```  ``` dashboards.folder.parent_id = dashboard_elements.look.folder_id ```  ``` dashboards.model.id = dashboard_elements.look.model.id ```  ``` dashboards.space.id = dashboard_elements.look.space.id ```  ``` dashboards.space.parent_id = dashboard_elements.look.space.id ```  ``` dashboards.space.id = dashboard_elements.look.space.parent_id ```  ``` dashboards.space.parent_id = dashboard_elements.look.space.parent_id ```  ``` dashboards.space.creator_id = dashboard_elements.look.deleter_id ```  ``` dashboards.user_id = dashboard_elements.look.deleter_id ```  ``` dashboards.space.creator_id = dashboard_elements.look.folder.creator_id ```  ``` dashboards.user_id = dashboard_elements.look.folder.creator_id ```  ``` dashboards.space.creator_id = dashboard_elements.look.last_updater_id ```  ``` dashboards.user_id = dashboard_elements.look.last_updater_id ```  ``` dashboards.space.creator_id = dashboard_elements.look.space.creator_id ```  ``` dashboards.user_id = dashboard_elements.look.space.creator_id ```  ``` dashboards.space.creator_id = dashboard_elements.look.user.id ```  ``` dashboards.user_id = dashboard_elements.look.user.id ```  ``` dashboards.space.creator_id = dashboard_elements.look.user_id ```  ``` dashboards.user_id = dashboard_elements.look.user_id ``` |
| [folders](#folders) | ``` dashboards.content_favorite_id = folders.dashboards.content_favorite_id ```  ``` dashboards.content_favorite_id = folders.looks.content_favorite_id ```  ``` dashboards.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` dashboards.space.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` dashboards.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` dashboards.space.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` dashboards.content_metadata_id = folders.looks.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = folders.looks.content_metadata_id ```  ``` dashboards.space.content_metadata_id = folders.looks.content_metadata_id ```  ``` dashboards.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` dashboards.space.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` dashboards.id = folders.dashboards.id ```  ``` dashboards.folder.id = folders.id ```  ``` dashboards.folder.parent_id = folders.id ```  ``` dashboards.folder.id = folders.dashboards.folder.id ```  ``` dashboards.folder.parent_id = folders.dashboards.folder.id ```  ``` dashboards.folder.id = folders.dashboards.folder.parent_id ```  ``` dashboards.folder.parent_id = folders.dashboards.folder.parent_id ```  ``` dashboards.folder.id = folders.looks.folder.id ```  ``` dashboards.folder.parent_id = folders.looks.folder.id ```  ``` dashboards.folder.id = folders.looks.folder.parent_id ```  ``` dashboards.folder.parent_id = folders.looks.folder.parent_id ```  ``` dashboards.folder.id = folders.parent_id ```  ``` dashboards.folder.parent_id = folders.parent_id ```  ``` dashboards.model.id = folders.dashboards.model.id ```  ``` dashboards.model.id = folders.looks.model.id ```  ``` dashboards.space.id = folders.dashboards.space.id ```  ``` dashboards.space.parent_id = folders.dashboards.space.id ```  ``` dashboards.space.id = folders.dashboards.space.parent_id ```  ``` dashboards.space.parent_id = folders.dashboards.space.parent_id ```  ``` dashboards.space.id = folders.looks.space.id ```  ``` dashboards.space.parent_id = folders.looks.space.id ```  ``` dashboards.space.id = folders.looks.space.parent_id ```  ``` dashboards.space.parent_id = folders.looks.space.parent_id ```  ``` dashboards.space.id = folders.looks.space_id ```  ``` dashboards.space.parent_id = folders.looks.space_id ```  ``` dashboards.space.creator_id = folders.creator_id ```  ``` dashboards.user_id = folders.creator_id ```  ``` dashboards.space.creator_id = folders.dashboards.user_id ```  ``` dashboards.user_id = folders.dashboards.user_id ```  ``` dashboards.space.creator_id = folders.dashboards.folder.creator_id ```  ``` dashboards.user_id = folders.dashboards.folder.creator_id ```  ``` dashboards.space.creator_id = folders.dashboards.space.creator_id ```  ``` dashboards.user_id = folders.dashboards.space.creator_id ```  ``` dashboards.space.creator_id = folders.looks.deleter_id ```  ``` dashboards.user_id = folders.looks.deleter_id ```  ``` dashboards.space.creator_id = folders.looks.last_updater_id ```  ``` dashboards.user_id = folders.looks.last_updater_id ```  ``` dashboards.space.creator_id = folders.looks.user.id ```  ``` dashboards.user_id = folders.looks.user.id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` dashboards.content_favorite_id = lookml_dashboards.content_favorite_id ```  ``` dashboards.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` dashboards.space.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` dashboards.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` dashboards.space.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` dashboards.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` dashboards.space.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` dashboards.folder.id = lookml_dashboards.folder.id ```  ``` dashboards.folder.parent_id = lookml_dashboards.folder.id ```  ``` dashboards.folder.id = lookml_dashboards.folder.parent_id ```  ``` dashboards.folder.parent_id = lookml_dashboards.folder.parent_id ```  ``` dashboards.model.id = lookml_dashboards.model.id ```  ``` dashboards.space.id = lookml_dashboards.space.id ```  ``` dashboards.space.parent_id = lookml_dashboards.space.id ```  ``` dashboards.space.id = lookml_dashboards.space.parent_id ```  ``` dashboards.space.parent_id = lookml_dashboards.space.parent_id ```  ``` dashboards.space.creator_id = lookml_dashboards.folder.creator_id ```  ``` dashboards.user_id = lookml_dashboards.folder.creator_id ```  ``` dashboards.space.creator_id = lookml_dashboards.space.creator_id ```  ``` dashboards.user_id = lookml_dashboards.space.creator_id ```  ``` dashboards.space.creator_id = lookml_dashboards.user_id ```  ``` dashboards.user_id = lookml_dashboards.user_id ``` |
| [looks](#looks) | ``` dashboards.content_favorite_id = looks.content_favorite_id ```  ``` dashboards.content_metadata_id = looks.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = looks.content_metadata_id ```  ``` dashboards.space.content_metadata_id = looks.content_metadata_id ```  ``` dashboards.folder.id = looks.folder.id ```  ``` dashboards.folder.parent_id = looks.folder.id ```  ``` dashboards.folder.id = looks.folder_id ```  ``` dashboards.folder.parent_id = looks.folder_id ```  ``` dashboards.folder.id = looks.folder.parent_id ```  ``` dashboards.folder.parent_id = looks.folder.parent_id ```  ``` dashboards.model.id = looks.model.id ```  ``` dashboards.space.id = looks.space.id ```  ``` dashboards.space.parent_id = looks.space.id ```  ``` dashboards.space.id = looks.space.parent_id ```  ``` dashboards.space.parent_id = looks.space.parent_id ```  ``` dashboards.space.id = looks.space_id ```  ``` dashboards.space.parent_id = looks.space_id ```  ``` dashboards.space.creator_id = looks.deleter_id ```  ``` dashboards.user_id = looks.deleter_id ```  ``` dashboards.space.creator_id = looks.folder.creator_id ```  ``` dashboards.user_id = looks.folder.creator_id ```  ``` dashboards.space.creator_id = looks.user.id ```  ``` dashboards.user_id = looks.user.id ```  ``` dashboards.space.creator_id = looks.user_id ```  ``` dashboards.user_id = looks.user_id ``` |
| [content\_metadata](#content-metadata) | ``` dashboards.content_metadata_id = content_metadata.id ```  ``` dashboards.folder.content_metadata_id = content_metadata.id ```  ``` dashboards.space.content_metadata_id = content_metadata.id ```  ``` dashboards.content_metadata_id = content_metadata.parent_id ```  ``` dashboards.folder.content_metadata_id = content_metadata.parent_id ```  ``` dashboards.space.content_metadata_id = content_metadata.parent_id ```  ``` dashboards.id = content_metadata.dashboard_id ```  ``` dashboards.space.id = content_metadata.space_id ```  ``` dashboards.space.parent_id = content_metadata.space_id ``` |
| [content\_metadata\_access](#content-metadata-access) | ``` dashboards.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` dashboards.space.content_metadata_id = content_metadata_access.content_metadata_id ``` |
| [content\_views](#content-views) | ``` dashboards.content_metadata_id = content_views.content_metadata_id ```  ``` dashboards.folder.content_metadata_id = content_views.content_metadata_id ```  ``` dashboards.space.content_metadata_id = content_views.content_metadata_id ```  ``` dashboards.id = content_views.dashboard_id ```  ``` dashboards.space.creator_id = content_views.user_id ```  ``` dashboards.user_id = content_views.user_id ``` |
| [dashboard\_filters](#dashboard-filters) | ``` dashboards.id = dashboard_filters.dashboard_id ``` |
| [dashboard\_layouts](#dashboard-layouts) | ``` dashboards.id = dashboard_layouts.dashboard_id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` dashboards.id = scheduled_plans.dashboard_id ```  ``` dashboards.space.creator_id = scheduled_plans.user.id ```  ``` dashboards.user_id = scheduled_plans.user.id ```  ``` dashboards.space.creator_id = scheduled_plans.user_id ```  ``` dashboards.user_id = scheduled_plans.user_id ``` |
| [users](#users) | ``` dashboards.folder.id = users.home_folder_id ```  ``` dashboards.folder.parent_id = users.home_folder_id ```  ``` dashboards.folder.id = users.personal_folder_id ```  ``` dashboards.folder.parent_id = users.personal_folder_id ```  ``` dashboards.space.id = users.home_space_id ```  ``` dashboards.space.parent_id = users.home_space_id ```  ``` dashboards.space.id = users.personal_space_id ```  ``` dashboards.space.parent_id = users.personal_space_id ```  ``` dashboards.space.creator_id = users.id ```  ``` dashboards.user_id = users.id ``` |
| [roles](#roles) | ``` dashboards.model.id = roles.model_set.models ``` |
| [connections](#connections) | ``` dashboards.space.creator_id = connections.user_id ```  ``` dashboards.user_id = connections.user_id ``` |
| [user\_login\_lockouts](#user-login-lockouts) | ``` dashboards.space.creator_id = user_login_lockouts.user_id ```  ``` dashboards.user_id = user_login_lockouts.user_id ``` |

dashboards table schema

|  |
| --- |
| **content\_favorite\_id**  STRING |
| **content\_metadata\_id**  STRING |
| **description**  STRING |
| **folder**  OBJECT This is a nested data structure:   - child\_count: INTEGER - content\_metadata\_id: STRING - creator\_id: STRING - external\_id: STRING - id: STRING - is\_embed: BOOLEAN - is\_embed\_shared\_root: BOOLEAN - is\_embed\_users\_root: BOOLEAN - is\_personal: BOOLEAN - is\_personal\_descendant: BOOLEAN - is\_shared\_root: BOOLEAN - is\_users\_root: BOOLEAN - name: STRING - parent\_id: STRING |
| **hidden**  BOOLEAN |
| **id**  STRING |
| **model**  OBJECT This is a nested data structure:   - id: STRING - label: STRING |
| **query\_timezone**  STRING |
| **readonly**  BOOLEAN |
| **refresh\_interval**  STRING |
| **refresh\_interval\_to\_i**  INTEGER |
| **space**  OBJECT This is a nested data structure:   - child\_count: INTEGER - content\_metadata\_id: STRING - creator\_id: STRING - external\_id: STRING - id: STRING - is\_embed: BOOLEAN - is\_embed\_shared\_root: BOOLEAN - is\_embed\_users\_root: BOOLEAN - is\_personal: BOOLEAN - is\_personal\_descendant: BOOLEAN - is\_shared\_root: BOOLEAN - is\_users\_root: BOOLEAN - name: STRING - parent\_id: STRING |
| **title**  STRING |
| **user\_id**  STRING |

### datagroups

The `datagroups` table contains information about all datagroups in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/datagroup#get_all_datagroups "Opens in new tab: Looker API method") |

datagroups table schema

|  |
| --- |
| **created\_at**  INTEGER |
| **id**  STRING |
| **model\_name**  STRING |
| **name**  STRING |
| **stale\_before**  INTEGER |
| **trigger\_check\_at**  INTEGER |
| **trigger\_error**  STRING |
| **trigger\_value**  STRING |
| **triggered\_at**  INTEGER |

### explores

The `explores` table contains information about LookML model explores in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/lookml-model#get_lookml_model_explore "Opens in new tab: Looker API method") |

explores table schema

|  |
| --- |
| **access\_filter\_fields**  ARRAY This is a nested data structure. |
| **access\_filters**  ARRAY This is a nested data structure:   - field: STRING - user\_attribute: STRING |
| **aliases**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **always\_filter**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **can\_explain**  BOOLEAN |
| **can\_pivot\_in\_db**  BOOLEAN |
| **can\_save**  BOOLEAN |
| **can\_subtotal**  BOOLEAN |
| **can\_total**  BOOLEAN |
| **conditionally\_filter**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **connection\_name**  STRING |
| **description**  STRING |
| **errors**  ARRAY This is a nested data structure:   - details: ANY - error\_pos: STRING - field\_error: BOOLEAN - message: STRING |
| **fields**  OBJECT This is a nested data structure:   - dimensions: ARRAY, which is also a nested data structure.   - align: STRING   - can\_filter: BOOLEAN   - can\_time\_filter: BOOLEAN   - category: STRING   - default\_filter\_value: STRING   - description: STRING   - dynamic: BOOLEAN   - enumerations: ARRAY, which is also a nested data structure.     - label: STRING     - value: STRING   - error: STRING   - field\_group\_label: STRING   - field\_group\_variant: STRING   - fill\_style: STRING   - fiscal\_month\_offset: INTEGER   - has\_allowed\_values: BOOLEAN   - hidden: BOOLEAN   - is\_filter: BOOLEAN   - is\_fiscal: BOOLEAN   - is\_numeric: BOOLEAN   - is\_timeframe: BOOLEAN   - label: STRING   - label\_from\_parameter: STRING   - label\_short: STRING   - lookml\_link: STRING   - map\_layer: OBJECT, which is also a nested data structure.     - extents\_json\_url: STRING     - feature\_key: STRING     - format: STRING     - max\_zoom\_level: INTEGER     - min\_zoom\_level: INTEGER     - name: STRING     - projection: STRING     - property\_key: STRING     - property\_label\_key: STRING     - url: STRING   - measure: BOOLEAN   - name: STRING   - parameter: BOOLEAN   - permanent: BOOLEAN   - primary\_key: BOOLEAN   - project\_name: STRING   - requires\_refresh\_on\_sort: BOOLEAN   - scope: STRING   - sortable: BOOLEAN   - source\_file: STRING   - source\_file\_path: STRING   - sql: STRING   - sql\_case: ARRAY, which is also a nested data structure.     - condition: STRING     - value: STRING   - strict\_value\_format: BOOLEAN   - suggest\_dimension: STRING   - suggest\_explore: STRING   - suggestable: BOOLEAN   - suggestions: ARRAY, which is also a nested data structure.   - tags: ARRAY, which is also a nested data structure.   - time\_interval: OBJECT, which is also a nested data structure.     - count: STRING     - name: STRING   - type: STRING   - user\_attribute\_filter\_types: ARRAY, which is also a nested data structure.   - value\_format: STRING   - view: STRING   - view\_label: STRING   - week\_start\_day: STRING - filters: ARRAY, which is also a nested data structure.   - align: STRING   - can\_filter: BOOLEAN   - can\_time\_filter: BOOLEAN   - category: STRING   - default\_filter\_value: STRING   - description: STRING   - dynamic: BOOLEAN   - enumerations: ARRAY, which is also a nested data structure.     - label: STRING     - value: STRING   - error: STRING   - field\_group\_label: STRING   - field\_group\_variant: STRING   - fill\_style: STRING   - fiscal\_month\_offset: INTEGER   - has\_allowed\_values: BOOLEAN   - hidden: BOOLEAN   - is\_filter: BOOLEAN   - is\_fiscal: BOOLEAN   - is\_numeric: BOOLEAN   - is\_timeframe: BOOLEAN   - label: STRING   - label\_from\_parameter: STRING   - label\_short: STRING   - lookml\_link: STRING   - map\_layer: OBJECT, which is also a nested data structure.     - extents\_json\_url: STRING     - feature\_key: STRING     - format: STRING     - max\_zoom\_level: INTEGER     - min\_zoom\_level: INTEGER     - name: STRING     - projection: STRING     - property\_key: STRING     - property\_label\_key: STRING     - url: STRING   - measure: BOOLEAN   - name: STRING   - parameter: BOOLEAN   - permanent: BOOLEAN   - primary\_key: BOOLEAN   - project\_name: STRING   - requires\_refresh\_on\_sort: BOOLEAN   - scope: STRING   - sortable: BOOLEAN   - source\_file: STRING   - source\_file\_path: STRING   - sql: STRING   - sql\_case: ARRAY, which is also a nested data structure.     - condition: STRING     - value: STRING   - strict\_value\_format: BOOLEAN   - suggest\_dimension: STRING   - suggest\_explore: STRING   - suggestable: BOOLEAN   - suggestions: ARRAY, which is also a nested data structure.   - tags: ARRAY, which is also a nested data structure.   - time\_interval: OBJECT, which is also a nested data structure.     - count: STRING     - name: STRING   - type: STRING   - user\_attribute\_filter\_types: ARRAY, which is also a nested data structure.   - value\_format: STRING   - view: STRING   - view\_label: STRING   - week\_start\_day: STRING - measures: ARRAY, which is also a nested data structure.   - align: STRING   - can\_filter: BOOLEAN   - can\_time\_filter: BOOLEAN   - category: STRING   - default\_filter\_value: STRING   - description: STRING   - dynamic: BOOLEAN   - enumerations: ARRAY, which is also a nested data structure.     - label: STRING     - value: STRING   - error: STRING   - field\_group\_label: STRING   - field\_group\_variant: STRING   - fill\_style: STRING   - fiscal\_month\_offset: INTEGER   - has\_allowed\_values: BOOLEAN   - hidden: BOOLEAN   - is\_filter: BOOLEAN   - is\_fiscal: BOOLEAN   - is\_numeric: BOOLEAN   - is\_timeframe: BOOLEAN   - label: STRING   - label\_from\_parameter: STRING   - label\_short: STRING   - lookml\_link: STRING   - map\_layer: OBJECT, which is also a nested data structure.     - extents\_json\_url: STRING     - feature\_key: STRING     - format: STRING     - max\_zoom\_level: INTEGER     - min\_zoom\_level: INTEGER     - name: STRING     - projection: STRING     - property\_key: STRING     - property\_label\_key: STRING     - url: STRING   - measure: BOOLEAN   - name: STRING   - parameter: BOOLEAN   - permanent: BOOLEAN   - primary\_key: BOOLEAN   - project\_name: STRING   - requires\_refresh\_on\_sort: BOOLEAN   - scope: STRING   - sortable: BOOLEAN   - source\_file: STRING   - source\_file\_path: STRING   - sql: STRING   - sql\_case: ARRAY, which is also a nested data structure.     - condition: STRING     - value: STRING   - strict\_value\_format: BOOLEAN   - suggest\_dimension: STRING   - suggest\_explore: STRING   - suggestable: BOOLEAN   - suggestions: ARRAY, which is also a nested data structure.   - tags: ARRAY, which is also a nested data structure.   - time\_interval: OBJECT, which is also a nested data structure.     - count: STRING     - name: STRING   - type: STRING   - user\_attribute\_filter\_types: ARRAY, which is also a nested data structure.   - value\_format: STRING   - view: STRING   - view\_label: STRING   - week\_start\_day: STRING - parameters: ARRAY, which is also a nested data structure.   - align: STRING   - can\_filter: BOOLEAN   - can\_time\_filter: BOOLEAN   - category: STRING   - default\_filter\_value: STRING   - description: STRING   - dynamic: BOOLEAN   - enumerations: ARRAY, which is also a nested data structure.     - label: STRING     - value: STRING   - error: STRING   - field\_group\_label: STRING   - field\_group\_variant: STRING   - fill\_style: STRING   - fiscal\_month\_offset: INTEGER   - has\_allowed\_values: BOOLEAN   - hidden: BOOLEAN   - is\_filter: BOOLEAN   - is\_fiscal: BOOLEAN   - is\_numeric: BOOLEAN   - is\_timeframe: BOOLEAN   - label: STRING   - label\_from\_parameter: STRING   - label\_short: STRING   - lookml\_link: STRING   - map\_layer: OBJECT, which is also a nested data structure.     - extents\_json\_url: STRING     - feature\_key: STRING     - format: STRING     - max\_zoom\_level: INTEGER     - min\_zoom\_level: INTEGER     - name: STRING     - projection: STRING     - property\_key: STRING     - property\_label\_key: STRING     - url: STRING   - measure: BOOLEAN   - name: STRING   - parameter: BOOLEAN   - permanent: BOOLEAN   - primary\_key: BOOLEAN   - project\_name: STRING   - requires\_refresh\_on\_sort: BOOLEAN   - scope: STRING   - sortable: BOOLEAN   - source\_file: STRING   - source\_file\_path: STRING   - sql: STRING   - sql\_case: ARRAY, which is also a nested data structure.     - condition: STRING     - value: STRING   - strict\_value\_format: BOOLEAN   - suggest\_dimension: STRING   - suggest\_explore: STRING   - suggestable: BOOLEAN   - suggestions: ARRAY, which is also a nested data structure.   - tags: ARRAY, which is also a nested data structure.   - time\_interval: OBJECT, which is also a nested data structure.     - count: STRING     - name: STRING   - type: STRING   - user\_attribute\_filter\_types: ARRAY, which is also a nested data structure.   - value\_format: STRING   - view: STRING   - view\_label: STRING   - week\_start\_day: STRING |
| **files**  ARRAY This is a nested data structure. |
| **group\_label**  STRING |
| **has\_timezone\_support**  BOOLEAN |
| **hidden**  BOOLEAN |
| **id**  STRING |
| **index\_fields**  ARRAY This is a nested data structure. |
| **joins**  ARRAY This is a nested data structure:   - dependent\_fields: ARRAY, which is also a nested data structure. - fields: ARRAY, which is also a nested data structure. - foreign\_key: STRING - from: STRING - name: STRING - outer\_only: BOOLEAN - relationship: STRING - required\_joins: ARRAY, which is also a nested data structure. - sql\_foreign\_key: STRING - sql\_on: STRING - sql\_table\_name: STRING - type: STRING - view\_label: STRING |
| **label**  STRING |
| **model\_name**  STRING |
| **name**  STRING |
| **null\_sort\_treatment**  STRING |
| **project\_name**  STRING |
| **scopes**  ARRAY This is a nested data structure. |
| **sets**  ARRAY This is a nested data structure:   - name: STRING - value: ARRAY, which is also a nested data structure. |
| **source\_file**  STRING |
| **sql\_table\_name**  STRING |
| **supported\_measure\_types**  ARRAY This is a nested data structure:   - dimension\_type: STRING - measure\_types: ARRAY, which is also a nested data structure. |
| **supports\_cost\_estimate**  BOOLEAN |
| **tags**  ARRAY This is a nested data structure. |
| **view\_name**  STRING |

### folders

The `folders` table contains information about all folders in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/folder#get_all_folders "Opens in new tab: Looker API method") |

folders table foreign keys

| Join folders with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` folders.dashboards.content_favorite_id = content_favorites.id ```  ``` folders.looks.content_favorite_id = content_favorites.id ```  ``` folders.dashboards.content_favorite_id = content_favorites.dashboard.content_favorite_id ```  ``` folders.looks.content_favorite_id = content_favorites.dashboard.content_favorite_id ```  ``` folders.dashboards.folder.content_metadata_id = content_favorites.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = content_favorites.content_metadata_id ```  ``` folders.looks.content_metadata_id = content_favorites.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = content_favorites.content_metadata_id ```  ``` folders.dashboards.folder.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` folders.looks.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` folders.dashboards.folder.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` folders.looks.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` folders.dashboards.folder.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` folders.looks.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` folders.dashboards.folder.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` folders.looks.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` folders.dashboards.id = content_favorites.dashboard.id ```  ``` folders.dashboards.id = content_favorites.dashboard_id ```  ``` folders.id = content_favorites.dashboard.folder.id ```  ``` folders.dashboards.folder.id = content_favorites.dashboard.folder.id ```  ``` folders.dashboards.folder.parent_id = content_favorites.dashboard.folder.id ```  ``` folders.looks.folder.id = content_favorites.dashboard.folder.id ```  ``` folders.looks.folder.parent_id = content_favorites.dashboard.folder.id ```  ``` folders.parent_id = content_favorites.dashboard.folder.id ```  ``` folders.id = content_favorites.dashboard.folder.parent_id ```  ``` folders.dashboards.folder.id = content_favorites.dashboard.folder.parent_id ```  ``` folders.dashboards.folder.parent_id = content_favorites.dashboard.folder.parent_id ```  ``` folders.looks.folder.id = content_favorites.dashboard.folder.parent_id ```  ``` folders.looks.folder.parent_id = content_favorites.dashboard.folder.parent_id ```  ``` folders.parent_id = content_favorites.dashboard.folder.parent_id ```  ``` folders.looks.id = content_favorites.look_id ```  ``` folders.looks.id = content_favorites.look.id ```  ``` folders.dashboards.model.id = content_favorites.dashboard.model.id ```  ``` folders.looks.model.id = content_favorites.dashboard.model.id ```  ``` folders.dashboards.space.id = content_favorites.dashboard.space.id ```  ``` folders.dashboards.space.parent_id = content_favorites.dashboard.space.id ```  ``` folders.looks.space.id = content_favorites.dashboard.space.id ```  ``` folders.looks.space.parent_id = content_favorites.dashboard.space.id ```  ``` folders.looks.space_id = content_favorites.dashboard.space.id ```  ``` folders.dashboards.space.id = content_favorites.dashboard.space.parent_id ```  ``` folders.dashboards.space.parent_id = content_favorites.dashboard.space.parent_id ```  ``` folders.looks.space.id = content_favorites.dashboard.space.parent_id ```  ``` folders.looks.space.parent_id = content_favorites.dashboard.space.parent_id ```  ``` folders.looks.space_id = content_favorites.dashboard.space.parent_id ```  ``` folders.creator_id = content_favorites.dashboard.folder.creator_id ```  ``` folders.dashboards.user_id = content_favorites.dashboard.folder.creator_id ```  ``` folders.dashboards.folder.creator_id = content_favorites.dashboard.folder.creator_id ```  ``` folders.dashboards.space.creator_id = content_favorites.dashboard.folder.creator_id ```  ``` folders.looks.deleter_id = content_favorites.dashboard.folder.creator_id ```  ``` folders.looks.last_updater_id = content_favorites.dashboard.folder.creator_id ```  ``` folders.looks.user.id = content_favorites.dashboard.folder.creator_id ```  ``` folders.creator_id = content_favorites.dashboard.space.creator_id ```  ``` folders.dashboards.user_id = content_favorites.dashboard.space.creator_id ```  ``` folders.dashboards.folder.creator_id = content_favorites.dashboard.space.creator_id ```  ``` folders.dashboards.space.creator_id = content_favorites.dashboard.space.creator_id ```  ``` folders.looks.deleter_id = content_favorites.dashboard.space.creator_id ```  ``` folders.looks.last_updater_id = content_favorites.dashboard.space.creator_id ```  ``` folders.looks.user.id = content_favorites.dashboard.space.creator_id ```  ``` folders.creator_id = content_favorites.user_id ```  ``` folders.dashboards.user_id = content_favorites.user_id ```  ``` folders.dashboards.folder.creator_id = content_favorites.user_id ```  ``` folders.dashboards.space.creator_id = content_favorites.user_id ```  ``` folders.looks.deleter_id = content_favorites.user_id ```  ``` folders.looks.last_updater_id = content_favorites.user_id ```  ``` folders.looks.user.id = content_favorites.user_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` folders.dashboards.content_favorite_id = dashboard_elements.look.content_favorite_id ```  ``` folders.looks.content_favorite_id = dashboard_elements.look.content_favorite_id ```  ``` folders.dashboards.folder.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` folders.looks.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` folders.dashboards.folder.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` folders.looks.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` folders.dashboards.folder.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` folders.looks.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` folders.dashboards.id = dashboard_elements.dashboard_id ```  ``` folders.id = dashboard_elements.look.folder.id ```  ``` folders.dashboards.folder.id = dashboard_elements.look.folder.id ```  ``` folders.dashboards.folder.parent_id = dashboard_elements.look.folder.id ```  ``` folders.looks.folder.id = dashboard_elements.look.folder.id ```  ``` folders.looks.folder.parent_id = dashboard_elements.look.folder.id ```  ``` folders.parent_id = dashboard_elements.look.folder.id ```  ``` folders.id = dashboard_elements.look.folder.parent_id ```  ``` folders.dashboards.folder.id = dashboard_elements.look.folder.parent_id ```  ``` folders.dashboards.folder.parent_id = dashboard_elements.look.folder.parent_id ```  ``` folders.looks.folder.id = dashboard_elements.look.folder.parent_id ```  ``` folders.looks.folder.parent_id = dashboard_elements.look.folder.parent_id ```  ``` folders.parent_id = dashboard_elements.look.folder.parent_id ```  ``` folders.id = dashboard_elements.look.folder_id ```  ``` folders.dashboards.folder.id = dashboard_elements.look.folder_id ```  ``` folders.dashboards.folder.parent_id = dashboard_elements.look.folder_id ```  ``` folders.looks.folder.id = dashboard_elements.look.folder_id ```  ``` folders.looks.folder.parent_id = dashboard_elements.look.folder_id ```  ``` folders.parent_id = dashboard_elements.look.folder_id ```  ``` folders.looks.id = dashboard_elements.look.id ```  ``` folders.looks.id = dashboard_elements.look_id ```  ``` folders.dashboards.model.id = dashboard_elements.look.model.id ```  ``` folders.looks.model.id = dashboard_elements.look.model.id ```  ``` folders.looks.query_id = dashboard_elements.look.query.id ```  ``` folders.looks.query_id = dashboard_elements.look.query_id ```  ``` folders.looks.query_id = dashboard_elements.query.id ```  ``` folders.looks.query_id = dashboard_elements.query_id ```  ``` folders.looks.query_id = dashboard_elements.result_maker.query.id ```  ``` folders.looks.query_id = dashboard_elements.result_maker.query_id ```  ``` folders.dashboards.space.id = dashboard_elements.look.space.id ```  ``` folders.dashboards.space.parent_id = dashboard_elements.look.space.id ```  ``` folders.looks.space.id = dashboard_elements.look.space.id ```  ``` folders.looks.space.parent_id = dashboard_elements.look.space.id ```  ``` folders.looks.space_id = dashboard_elements.look.space.id ```  ``` folders.dashboards.space.id = dashboard_elements.look.space.parent_id ```  ``` folders.dashboards.space.parent_id = dashboard_elements.look.space.parent_id ```  ``` folders.looks.space.id = dashboard_elements.look.space.parent_id ```  ``` folders.looks.space.parent_id = dashboard_elements.look.space.parent_id ```  ``` folders.looks.space_id = dashboard_elements.look.space.parent_id ```  ``` folders.creator_id = dashboard_elements.look.deleter_id ```  ``` folders.dashboards.user_id = dashboard_elements.look.deleter_id ```  ``` folders.dashboards.folder.creator_id = dashboard_elements.look.deleter_id ```  ``` folders.dashboards.space.creator_id = dashboard_elements.look.deleter_id ```  ``` folders.looks.deleter_id = dashboard_elements.look.deleter_id ```  ``` folders.looks.last_updater_id = dashboard_elements.look.deleter_id ```  ``` folders.looks.user.id = dashboard_elements.look.deleter_id ```  ``` folders.creator_id = dashboard_elements.look.folder.creator_id ```  ``` folders.dashboards.user_id = dashboard_elements.look.folder.creator_id ```  ``` folders.dashboards.folder.creator_id = dashboard_elements.look.folder.creator_id ```  ``` folders.dashboards.space.creator_id = dashboard_elements.look.folder.creator_id ```  ``` folders.looks.deleter_id = dashboard_elements.look.folder.creator_id ```  ``` folders.looks.last_updater_id = dashboard_elements.look.folder.creator_id ```  ``` folders.looks.user.id = dashboard_elements.look.folder.creator_id ```  ``` folders.creator_id = dashboard_elements.look.last_updater_id ```  ``` folders.dashboards.user_id = dashboard_elements.look.last_updater_id ```  ``` folders.dashboards.folder.creator_id = dashboard_elements.look.last_updater_id ```  ``` folders.dashboards.space.creator_id = dashboard_elements.look.last_updater_id ```  ``` folders.looks.deleter_id = dashboard_elements.look.last_updater_id ```  ``` folders.looks.last_updater_id = dashboard_elements.look.last_updater_id ```  ``` folders.looks.user.id = dashboard_elements.look.last_updater_id ```  ``` folders.creator_id = dashboard_elements.look.space.creator_id ```  ``` folders.dashboards.user_id = dashboard_elements.look.space.creator_id ```  ``` folders.dashboards.folder.creator_id = dashboard_elements.look.space.creator_id ```  ``` folders.dashboards.space.creator_id = dashboard_elements.look.space.creator_id ```  ``` folders.looks.deleter_id = dashboard_elements.look.space.creator_id ```  ``` folders.looks.last_updater_id = dashboard_elements.look.space.creator_id ```  ``` folders.looks.user.id = dashboard_elements.look.space.creator_id ```  ``` folders.creator_id = dashboard_elements.look.user.id ```  ``` folders.dashboards.user_id = dashboard_elements.look.user.id ```  ``` folders.dashboards.folder.creator_id = dashboard_elements.look.user.id ```  ``` folders.dashboards.space.creator_id = dashboard_elements.look.user.id ```  ``` folders.looks.deleter_id = dashboard_elements.look.user.id ```  ``` folders.looks.last_updater_id = dashboard_elements.look.user.id ```  ``` folders.looks.user.id = dashboard_elements.look.user.id ```  ``` folders.creator_id = dashboard_elements.look.user_id ```  ``` folders.dashboards.user_id = dashboard_elements.look.user_id ```  ``` folders.dashboards.folder.creator_id = dashboard_elements.look.user_id ```  ``` folders.dashboards.space.creator_id = dashboard_elements.look.user_id ```  ``` folders.looks.deleter_id = dashboard_elements.look.user_id ```  ``` folders.looks.last_updater_id = dashboard_elements.look.user_id ```  ``` folders.looks.user.id = dashboard_elements.look.user_id ``` |
| [dashboards](#dashboards) | ``` folders.dashboards.content_favorite_id = dashboards.content_favorite_id ```  ``` folders.looks.content_favorite_id = dashboards.content_favorite_id ```  ``` folders.dashboards.folder.content_metadata_id = dashboards.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = dashboards.content_metadata_id ```  ``` folders.looks.content_metadata_id = dashboards.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = dashboards.content_metadata_id ```  ``` folders.dashboards.folder.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` folders.looks.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` folders.dashboards.folder.content_metadata_id = dashboards.space.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = dashboards.space.content_metadata_id ```  ``` folders.looks.content_metadata_id = dashboards.space.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = dashboards.space.content_metadata_id ```  ``` folders.dashboards.id = dashboards.id ```  ``` folders.id = dashboards.folder.id ```  ``` folders.dashboards.folder.id = dashboards.folder.id ```  ``` folders.dashboards.folder.parent_id = dashboards.folder.id ```  ``` folders.looks.folder.id = dashboards.folder.id ```  ``` folders.looks.folder.parent_id = dashboards.folder.id ```  ``` folders.parent_id = dashboards.folder.id ```  ``` folders.id = dashboards.folder.parent_id ```  ``` folders.dashboards.folder.id = dashboards.folder.parent_id ```  ``` folders.dashboards.folder.parent_id = dashboards.folder.parent_id ```  ``` folders.looks.folder.id = dashboards.folder.parent_id ```  ``` folders.looks.folder.parent_id = dashboards.folder.parent_id ```  ``` folders.parent_id = dashboards.folder.parent_id ```  ``` folders.dashboards.model.id = dashboards.model.id ```  ``` folders.looks.model.id = dashboards.model.id ```  ``` folders.dashboards.space.id = dashboards.space.id ```  ``` folders.dashboards.space.parent_id = dashboards.space.id ```  ``` folders.looks.space.id = dashboards.space.id ```  ``` folders.looks.space.parent_id = dashboards.space.id ```  ``` folders.looks.space_id = dashboards.space.id ```  ``` folders.dashboards.space.id = dashboards.space.parent_id ```  ``` folders.dashboards.space.parent_id = dashboards.space.parent_id ```  ``` folders.looks.space.id = dashboards.space.parent_id ```  ``` folders.looks.space.parent_id = dashboards.space.parent_id ```  ``` folders.looks.space_id = dashboards.space.parent_id ```  ``` folders.creator_id = dashboards.space.creator_id ```  ``` folders.dashboards.user_id = dashboards.space.creator_id ```  ``` folders.dashboards.folder.creator_id = dashboards.space.creator_id ```  ``` folders.dashboards.space.creator_id = dashboards.space.creator_id ```  ``` folders.looks.deleter_id = dashboards.space.creator_id ```  ``` folders.looks.last_updater_id = dashboards.space.creator_id ```  ``` folders.looks.user.id = dashboards.space.creator_id ```  ``` folders.creator_id = dashboards.user_id ```  ``` folders.dashboards.user_id = dashboards.user_id ```  ``` folders.dashboards.folder.creator_id = dashboards.user_id ```  ``` folders.dashboards.space.creator_id = dashboards.user_id ```  ``` folders.looks.deleter_id = dashboards.user_id ```  ``` folders.looks.last_updater_id = dashboards.user_id ```  ``` folders.looks.user.id = dashboards.user_id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` folders.dashboards.content_favorite_id = lookml_dashboards.content_favorite_id ```  ``` folders.looks.content_favorite_id = lookml_dashboards.content_favorite_id ```  ``` folders.dashboards.folder.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` folders.looks.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` folders.dashboards.folder.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` folders.looks.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` folders.dashboards.folder.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` folders.looks.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` folders.id = lookml_dashboards.folder.id ```  ``` folders.dashboards.folder.id = lookml_dashboards.folder.id ```  ``` folders.dashboards.folder.parent_id = lookml_dashboards.folder.id ```  ``` folders.looks.folder.id = lookml_dashboards.folder.id ```  ``` folders.looks.folder.parent_id = lookml_dashboards.folder.id ```  ``` folders.parent_id = lookml_dashboards.folder.id ```  ``` folders.id = lookml_dashboards.folder.parent_id ```  ``` folders.dashboards.folder.id = lookml_dashboards.folder.parent_id ```  ``` folders.dashboards.folder.parent_id = lookml_dashboards.folder.parent_id ```  ``` folders.looks.folder.id = lookml_dashboards.folder.parent_id ```  ``` folders.looks.folder.parent_id = lookml_dashboards.folder.parent_id ```  ``` folders.parent_id = lookml_dashboards.folder.parent_id ```  ``` folders.dashboards.model.id = lookml_dashboards.model.id ```  ``` folders.looks.model.id = lookml_dashboards.model.id ```  ``` folders.dashboards.space.id = lookml_dashboards.space.id ```  ``` folders.dashboards.space.parent_id = lookml_dashboards.space.id ```  ``` folders.looks.space.id = lookml_dashboards.space.id ```  ``` folders.looks.space.parent_id = lookml_dashboards.space.id ```  ``` folders.looks.space_id = lookml_dashboards.space.id ```  ``` folders.dashboards.space.id = lookml_dashboards.space.parent_id ```  ``` folders.dashboards.space.parent_id = lookml_dashboards.space.parent_id ```  ``` folders.looks.space.id = lookml_dashboards.space.parent_id ```  ``` folders.looks.space.parent_id = lookml_dashboards.space.parent_id ```  ``` folders.looks.space_id = lookml_dashboards.space.parent_id ```  ``` folders.creator_id = lookml_dashboards.folder.creator_id ```  ``` folders.dashboards.user_id = lookml_dashboards.folder.creator_id ```  ``` folders.dashboards.folder.creator_id = lookml_dashboards.folder.creator_id ```  ``` folders.dashboards.space.creator_id = lookml_dashboards.folder.creator_id ```  ``` folders.looks.deleter_id = lookml_dashboards.folder.creator_id ```  ``` folders.looks.last_updater_id = lookml_dashboards.folder.creator_id ```  ``` folders.looks.user.id = lookml_dashboards.folder.creator_id ```  ``` folders.creator_id = lookml_dashboards.space.creator_id ```  ``` folders.dashboards.user_id = lookml_dashboards.space.creator_id ```  ``` folders.dashboards.folder.creator_id = lookml_dashboards.space.creator_id ```  ``` folders.dashboards.space.creator_id = lookml_dashboards.space.creator_id ```  ``` folders.looks.deleter_id = lookml_dashboards.space.creator_id ```  ``` folders.looks.last_updater_id = lookml_dashboards.space.creator_id ```  ``` folders.looks.user.id = lookml_dashboards.space.creator_id ```  ``` folders.creator_id = lookml_dashboards.user_id ```  ``` folders.dashboards.user_id = lookml_dashboards.user_id ```  ``` folders.dashboards.folder.creator_id = lookml_dashboards.user_id ```  ``` folders.dashboards.space.creator_id = lookml_dashboards.user_id ```  ``` folders.looks.deleter_id = lookml_dashboards.user_id ```  ``` folders.looks.last_updater_id = lookml_dashboards.user_id ```  ``` folders.looks.user.id = lookml_dashboards.user_id ``` |
| [looks](#looks) | ``` folders.dashboards.content_favorite_id = looks.content_favorite_id ```  ``` folders.looks.content_favorite_id = looks.content_favorite_id ```  ``` folders.dashboards.folder.content_metadata_id = looks.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = looks.content_metadata_id ```  ``` folders.looks.content_metadata_id = looks.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = looks.content_metadata_id ```  ``` folders.id = looks.folder.id ```  ``` folders.dashboards.folder.id = looks.folder.id ```  ``` folders.dashboards.folder.parent_id = looks.folder.id ```  ``` folders.looks.folder.id = looks.folder.id ```  ``` folders.looks.folder.parent_id = looks.folder.id ```  ``` folders.parent_id = looks.folder.id ```  ``` folders.id = looks.folder_id ```  ``` folders.dashboards.folder.id = looks.folder_id ```  ``` folders.dashboards.folder.parent_id = looks.folder_id ```  ``` folders.looks.folder.id = looks.folder_id ```  ``` folders.looks.folder.parent_id = looks.folder_id ```  ``` folders.parent_id = looks.folder_id ```  ``` folders.id = looks.folder.parent_id ```  ``` folders.dashboards.folder.id = looks.folder.parent_id ```  ``` folders.dashboards.folder.parent_id = looks.folder.parent_id ```  ``` folders.looks.folder.id = looks.folder.parent_id ```  ``` folders.looks.folder.parent_id = looks.folder.parent_id ```  ``` folders.parent_id = looks.folder.parent_id ```  ``` folders.looks.id = looks.id ```  ``` folders.dashboards.model.id = looks.model.id ```  ``` folders.looks.model.id = looks.model.id ```  ``` folders.looks.query_id = looks.query_id ```  ``` folders.dashboards.space.id = looks.space.id ```  ``` folders.dashboards.space.parent_id = looks.space.id ```  ``` folders.looks.space.id = looks.space.id ```  ``` folders.looks.space.parent_id = looks.space.id ```  ``` folders.looks.space_id = looks.space.id ```  ``` folders.dashboards.space.id = looks.space.parent_id ```  ``` folders.dashboards.space.parent_id = looks.space.parent_id ```  ``` folders.looks.space.id = looks.space.parent_id ```  ``` folders.looks.space.parent_id = looks.space.parent_id ```  ``` folders.looks.space_id = looks.space.parent_id ```  ``` folders.dashboards.space.id = looks.space_id ```  ``` folders.dashboards.space.parent_id = looks.space_id ```  ``` folders.looks.space.id = looks.space_id ```  ``` folders.looks.space.parent_id = looks.space_id ```  ``` folders.looks.space_id = looks.space_id ```  ``` folders.creator_id = looks.deleter_id ```  ``` folders.dashboards.user_id = looks.deleter_id ```  ``` folders.dashboards.folder.creator_id = looks.deleter_id ```  ``` folders.dashboards.space.creator_id = looks.deleter_id ```  ``` folders.looks.deleter_id = looks.deleter_id ```  ``` folders.looks.last_updater_id = looks.deleter_id ```  ``` folders.looks.user.id = looks.deleter_id ```  ``` folders.creator_id = looks.folder.creator_id ```  ``` folders.dashboards.user_id = looks.folder.creator_id ```  ``` folders.dashboards.folder.creator_id = looks.folder.creator_id ```  ``` folders.dashboards.space.creator_id = looks.folder.creator_id ```  ``` folders.looks.deleter_id = looks.folder.creator_id ```  ``` folders.looks.last_updater_id = looks.folder.creator_id ```  ``` folders.looks.user.id = looks.folder.creator_id ```  ``` folders.creator_id = looks.user.id ```  ``` folders.dashboards.user_id = looks.user.id ```  ``` folders.dashboards.folder.creator_id = looks.user.id ```  ``` folders.dashboards.space.creator_id = looks.user.id ```  ``` folders.looks.deleter_id = looks.user.id ```  ``` folders.looks.last_updater_id = looks.user.id ```  ``` folders.looks.user.id = looks.user.id ```  ``` folders.creator_id = looks.user_id ```  ``` folders.dashboards.user_id = looks.user_id ```  ``` folders.dashboards.folder.creator_id = looks.user_id ```  ``` folders.dashboards.space.creator_id = looks.user_id ```  ``` folders.looks.deleter_id = looks.user_id ```  ``` folders.looks.last_updater_id = looks.user_id ```  ``` folders.looks.user.id = looks.user_id ``` |
| [content\_metadata](#content-metadata) | ``` folders.dashboards.folder.content_metadata_id = content_metadata.id ```  ``` folders.dashboards.space.content_metadata_id = content_metadata.id ```  ``` folders.looks.content_metadata_id = content_metadata.id ```  ``` folders.looks.folder.content_metadata_id = content_metadata.id ```  ``` folders.dashboards.folder.content_metadata_id = content_metadata.parent_id ```  ``` folders.dashboards.space.content_metadata_id = content_metadata.parent_id ```  ``` folders.looks.content_metadata_id = content_metadata.parent_id ```  ``` folders.looks.folder.content_metadata_id = content_metadata.parent_id ```  ``` folders.dashboards.id = content_metadata.dashboard_id ```  ``` folders.looks.id = content_metadata.look_id ```  ``` folders.dashboards.space.id = content_metadata.space_id ```  ``` folders.dashboards.space.parent_id = content_metadata.space_id ```  ``` folders.looks.space.id = content_metadata.space_id ```  ``` folders.looks.space.parent_id = content_metadata.space_id ```  ``` folders.looks.space_id = content_metadata.space_id ``` |
| [content\_metadata\_access](#content-metadata-access) | ``` folders.dashboards.folder.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` folders.looks.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = content_metadata_access.content_metadata_id ``` |
| [content\_views](#content-views) | ``` folders.dashboards.folder.content_metadata_id = content_views.content_metadata_id ```  ``` folders.dashboards.space.content_metadata_id = content_views.content_metadata_id ```  ``` folders.looks.content_metadata_id = content_views.content_metadata_id ```  ``` folders.looks.folder.content_metadata_id = content_views.content_metadata_id ```  ``` folders.dashboards.id = content_views.dashboard_id ```  ``` folders.looks.id = content_views.look_id ```  ``` folders.creator_id = content_views.user_id ```  ``` folders.dashboards.user_id = content_views.user_id ```  ``` folders.dashboards.folder.creator_id = content_views.user_id ```  ``` folders.dashboards.space.creator_id = content_views.user_id ```  ``` folders.looks.deleter_id = content_views.user_id ```  ``` folders.looks.last_updater_id = content_views.user_id ```  ``` folders.looks.user.id = content_views.user_id ``` |
| [dashboard\_filters](#dashboard-filters) | ``` folders.dashboards.id = dashboard_filters.dashboard_id ``` |
| [dashboard\_layouts](#dashboard-layouts) | ``` folders.dashboards.id = dashboard_layouts.dashboard_id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` folders.dashboards.id = scheduled_plans.dashboard_id ```  ``` folders.looks.id = scheduled_plans.look_id ```  ``` folders.looks.query_id = scheduled_plans.query_id ```  ``` folders.creator_id = scheduled_plans.user.id ```  ``` folders.dashboards.user_id = scheduled_plans.user.id ```  ``` folders.dashboards.folder.creator_id = scheduled_plans.user.id ```  ``` folders.dashboards.space.creator_id = scheduled_plans.user.id ```  ``` folders.looks.deleter_id = scheduled_plans.user.id ```  ``` folders.looks.last_updater_id = scheduled_plans.user.id ```  ``` folders.looks.user.id = scheduled_plans.user.id ```  ``` folders.creator_id = scheduled_plans.user_id ```  ``` folders.dashboards.user_id = scheduled_plans.user_id ```  ``` folders.dashboards.folder.creator_id = scheduled_plans.user_id ```  ``` folders.dashboards.space.creator_id = scheduled_plans.user_id ```  ``` folders.looks.deleter_id = scheduled_plans.user_id ```  ``` folders.looks.last_updater_id = scheduled_plans.user_id ```  ``` folders.looks.user.id = scheduled_plans.user_id ``` |
| [users](#users) | ``` folders.id = users.home_folder_id ```  ``` folders.dashboards.folder.id = users.home_folder_id ```  ``` folders.dashboards.folder.parent_id = users.home_folder_id ```  ``` folders.looks.folder.id = users.home_folder_id ```  ``` folders.looks.folder.parent_id = users.home_folder_id ```  ``` folders.parent_id = users.home_folder_id ```  ``` folders.id = users.personal_folder_id ```  ``` folders.dashboards.folder.id = users.personal_folder_id ```  ``` folders.dashboards.folder.parent_id = users.personal_folder_id ```  ``` folders.looks.folder.id = users.personal_folder_id ```  ``` folders.looks.folder.parent_id = users.personal_folder_id ```  ``` folders.parent_id = users.personal_folder_id ```  ``` folders.dashboards.space.id = users.home_space_id ```  ``` folders.dashboards.space.parent_id = users.home_space_id ```  ``` folders.looks.space.id = users.home_space_id ```  ``` folders.looks.space.parent_id = users.home_space_id ```  ``` folders.looks.space_id = users.home_space_id ```  ``` folders.dashboards.space.id = users.personal_space_id ```  ``` folders.dashboards.space.parent_id = users.personal_space_id ```  ``` folders.looks.space.id = users.personal_space_id ```  ``` folders.looks.space.parent_id = users.personal_space_id ```  ``` folders.looks.space_id = users.personal_space_id ```  ``` folders.creator_id = users.id ```  ``` folders.dashboards.user_id = users.id ```  ``` folders.dashboards.folder.creator_id = users.id ```  ``` folders.dashboards.space.creator_id = users.id ```  ``` folders.looks.deleter_id = users.id ```  ``` folders.looks.last_updater_id = users.id ```  ``` folders.looks.user.id = users.id ``` |
| [roles](#roles) | ``` folders.dashboards.model.id = roles.model_set.models ```  ``` folders.looks.model.id = roles.model_set.models ``` |
| [queries](#queries) | ``` folders.looks.query_id = queries.id ``` |
| [connections](#connections) | ``` folders.creator_id = connections.user_id ```  ``` folders.dashboards.user_id = connections.user_id ```  ``` folders.dashboards.folder.creator_id = connections.user_id ```  ``` folders.dashboards.space.creator_id = connections.user_id ```  ``` folders.looks.deleter_id = connections.user_id ```  ``` folders.looks.last_updater_id = connections.user_id ```  ``` folders.looks.user.id = connections.user_id ``` |
| [user\_login\_lockouts](#user-login-lockouts) | ``` folders.creator_id = user_login_lockouts.user_id ```  ``` folders.dashboards.user_id = user_login_lockouts.user_id ```  ``` folders.dashboards.folder.creator_id = user_login_lockouts.user_id ```  ``` folders.dashboards.space.creator_id = user_login_lockouts.user_id ```  ``` folders.looks.deleter_id = user_login_lockouts.user_id ```  ``` folders.looks.last_updater_id = user_login_lockouts.user_id ```  ``` folders.looks.user.id = user_login_lockouts.user_id ``` |

folders table schema

|  |
| --- |
| **child\_count**  INTEGER |
| **content\_metadata\_id**  STRING |
| **creator\_id**  STRING |
| **dashboards**  ARRAY This is a nested data structure:   - content\_favorite\_id: STRING - content\_metadata\_id: STRING - description: STRING - folder: OBJECT, which is also a nested data structure.   - child\_count: INTEGER   - content\_metadata\_id: STRING   - creator\_id: STRING   - external\_id: STRING   - id: STRING   - is\_embed: BOOLEAN   - is\_embed\_shared\_root: BOOLEAN   - is\_embed\_users\_root: BOOLEAN   - is\_personal: BOOLEAN   - is\_personal\_descendant: BOOLEAN   - is\_shared\_root: BOOLEAN   - is\_users\_root: BOOLEAN   - name: STRING   - parent\_id: STRING - hidden: BOOLEAN - id: STRING - model: OBJECT, which is also a nested data structure.   - id: STRING   - label: STRING - query\_timezone: STRING - readonly: BOOLEAN - refresh\_interval: STRING - refresh\_interval\_to\_i: INTEGER - space: OBJECT, which is also a nested data structure.   - child\_count: INTEGER   - content\_metadata\_id: STRING   - creator\_id: STRING   - external\_id: STRING   - id: STRING   - is\_embed: BOOLEAN   - is\_embed\_shared\_root: BOOLEAN   - is\_embed\_users\_root: BOOLEAN   - is\_personal: BOOLEAN   - is\_personal\_descendant: BOOLEAN   - is\_shared\_root: BOOLEAN   - is\_users\_root: BOOLEAN   - name: STRING   - parent\_id: STRING - title: STRING - user\_id: STRING |
| **external\_id**  STRING |
| **id**  STRING |
| **is\_embed**  BOOLEAN |
| **is\_embed\_shared\_root**  BOOLEAN |
| **is\_embed\_users\_root**  BOOLEAN |
| **is\_personal**  BOOLEAN |
| **is\_personal\_descendant**  BOOLEAN |
| **is\_shared\_root**  BOOLEAN |
| **is\_users\_root**  BOOLEAN |
| **looks**  ARRAY This is a nested data structure:   - content\_favorite\_id: STRING - content\_metadata\_id: STRING - created\_at: DATE-TIME - dashboards: ARRAY, which is also a nested data structure.   - content\_favorite\_id: STRING   - content\_metadata\_id: STRING   - description: STRING   - folder: OBJECT, which is also a nested data structure.     - child\_count: INTEGER     - content\_metadata\_id: STRING     - creator\_id: STRING     - external\_id: STRING     - id: STRING     - is\_embed: BOOLEAN     - is\_embed\_shared\_root: BOOLEAN     - is\_embed\_users\_root: BOOLEAN     - is\_personal: BOOLEAN     - is\_personal\_descendant: BOOLEAN     - is\_shared\_root: BOOLEAN     - is\_users\_root: BOOLEAN     - name: STRING     - parent\_id: STRING   - hidden: BOOLEAN   - id: STRING   - model: OBJECT, which is also a nested data structure.     - id: STRING     - label: STRING   - query\_timezone: STRING   - readonly: BOOLEAN   - refresh\_interval: STRING   - refresh\_interval\_to\_i: INTEGER   - space: OBJECT, which is also a nested data structure.     - child\_count: INTEGER     - content\_metadata\_id: STRING     - creator\_id: STRING     - external\_id: STRING     - id: STRING     - is\_embed: BOOLEAN     - is\_embed\_shared\_root: BOOLEAN     - is\_embed\_users\_root: BOOLEAN     - is\_personal: BOOLEAN     - is\_personal\_descendant: BOOLEAN     - is\_shared\_root: BOOLEAN     - is\_users\_root: BOOLEAN     - name: STRING     - parent\_id: STRING   - title: STRING   - user\_id: STRING - deleted: BOOLEAN - deleted\_at: DATE-TIME - deleter\_id: STRING - description: STRING - embed\_url: STRING - excel\_file\_url: STRING - favorite\_count: INTEGER - folder: OBJECT, which is also a nested data structure.   - child\_count: INTEGER   - content\_metadata\_id: STRING   - creator\_id: STRING   - external\_id: STRING   - id: STRING   - is\_embed: BOOLEAN   - is\_embed\_shared\_root: BOOLEAN   - is\_embed\_users\_root: BOOLEAN   - is\_personal: BOOLEAN   - is\_personal\_descendant: BOOLEAN   - is\_shared\_root: BOOLEAN   - is\_users\_root: BOOLEAN   - name: STRING   - parent\_id: STRING - folder\_id: STRING - google\_spreadsheet\_formula: STRING - id: STRING - image\_embed\_url: STRING - is\_run\_on\_load: BOOLEAN - last\_accessed\_at: DATE-TIME - last\_updater\_id: STRING - last\_viewed\_at: DATE-TIME - model: OBJECT, which is also a nested data structure.   - id: STRING   - label: STRING - public: BOOLEAN - public\_slug: STRING - public\_url: STRING - query\_id: STRING - short\_url: STRING - space: OBJECT, which is also a nested data structure.   - child\_count: INTEGER   - content\_metadata\_id: STRING   - creator\_id: STRING   - external\_id: STRING   - id: STRING   - is\_embed: BOOLEAN   - is\_embed\_shared\_root: BOOLEAN   - is\_embed\_users\_root: BOOLEAN   - is\_personal: BOOLEAN   - is\_personal\_descendant: BOOLEAN   - is\_shared\_root: BOOLEAN   - is\_users\_root: BOOLEAN   - name: STRING   - parent\_id: STRING - space\_id: STRING - title: STRING - updated\_at: DATE-TIME - user: OBJECT, which is also a nested data structure.   - id: STRING - user\_id: STRING - view\_count: INTEGER |
| **name**  STRING |
| **parent\_id**  STRING |

### git\_branches

The `git_branches` table contains info about the git branches associated with projects in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | name  project\_id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/project#get_all_git_branches "Opens in new tab: Looker API method") |

git\_branches table foreign keys

| Join git\_branches with | on |
| --- | --- |
| [project\_files](#project-files) | ``` git_branches.project_id = project_files.project_id ``` |
| [projects](#projects) | ``` git_branches.project_id = projects.id ``` |
| [workspaces](#workspaces) | ``` git_branches.project_id = workspaces.projects.id ``` |

git\_branches table schema

|  |
| --- |
| **ahead\_count**  INTEGER |
| **behind\_count**  INTEGER |
| **commit\_at**  INTEGER |
| **error**  STRING |
| **is\_local**  BOOLEAN |
| **is\_production**  BOOLEAN |
| **is\_remote**  BOOLEAN |
| **message**  STRING |
| **name**  STRING |
| **owner\_name**  STRING |
| **personal**  BOOLEAN |
| **project\_id**  STRING |
| **readonly**  BOOLEAN |
| **ref**  STRING |
| **remote**  STRING |
| **remote\_name**  STRING |
| **remote\_ref**  STRING |

### groups

The `groups` table contains information about all groups in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/group#get_all_groups "Opens in new tab: Looker API method") |

groups table foreign keys

| Join groups with | on |
| --- | --- |
| [content\_metadata\_access](#content-metadata-access) | ``` groups.id = content_metadata_access.group_id ``` |
| [content\_views](#content-views) | ``` groups.id = content_views.group_id ``` |
| [groups\_in\_group](#groups-in-group) | ``` groups.id = groups_in_group.id ```  ``` groups.id = groups_in_group.parent_group_id ``` |
| [user\_attribute\_group\_values](#user-attribute-group-values) | ``` groups.id = user_attribute_group_values.group_id ``` |
| [users](#users) | ``` groups.id = users.group_ids ``` |

groups table schema

|  |
| --- |
| **can\_add\_to\_content\_metadata**  BOOLEAN |
| **contains\_current\_user**  BOOLEAN |
| **external\_group\_id**  STRING |
| **externally\_managed**  BOOLEAN |
| **id**  STRING |
| **include\_by\_default**  BOOLEAN |
| **name**  STRING |
| **user\_count**  INTEGER |

### groups\_in\_group

The `groups_in_group` table contains info about the groups contained within groups in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/group#get_all_groups_in_group "Opens in new tab: Looker API method") |

groups\_in\_group table foreign keys

| Join groups\_in\_group with | on |
| --- | --- |
| [content\_metadata\_access](#content-metadata-access) | ``` groups_in_group.id = content_metadata_access.group_id ```  ``` groups_in_group.parent_group_id = content_metadata_access.group_id ``` |
| [content\_views](#content-views) | ``` groups_in_group.id = content_views.group_id ```  ``` groups_in_group.parent_group_id = content_views.group_id ``` |
| [groups](#groups) | ``` groups_in_group.id = groups.id ```  ``` groups_in_group.parent_group_id = groups.id ``` |
| [user\_attribute\_group\_values](#user-attribute-group-values) | ``` groups_in_group.id = user_attribute_group_values.group_id ```  ``` groups_in_group.parent_group_id = user_attribute_group_values.group_id ``` |
| [users](#users) | ``` groups_in_group.id = users.group_ids ```  ``` groups_in_group.parent_group_id = users.group_ids ``` |

groups\_in\_group table schema

|  |
| --- |
| **can\_add\_to\_content\_metadata**  BOOLEAN |
| **contains\_current\_user**  BOOLEAN |
| **external\_group\_id**  STRING |
| **externally\_managed**  BOOLEAN |
| **id**  STRING |
| **include\_by\_default**  BOOLEAN |
| **name**  STRING |
| **parent\_group\_id**  STRING |
| **user\_count**  INTEGER |

### integration\_hubs

The `integration_hubs` table contains information about Integration Hubs in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/integration#get_all_integration_hubs "Opens in new tab: Looker API method") |

integration\_hubs table foreign keys

| Join integration\_hubs with | on |
| --- | --- |
| [integrations](#integrations) | ``` integration_hubs.id = integrations.integration_hub_id ``` |

integration\_hubs table schema

|  |
| --- |
| **authorization\_token**  STRING |
| **fetch\_error\_message**  STRING |
| **has\_authorization\_token**  BOOLEAN |
| **id**  STRING |
| **label**  STRING |
| **legal\_agreement\_required**  BOOLEAN |
| **legal\_agreement\_signed**  BOOLEAN |
| **legal\_agreement\_text**  STRING |
| **official**  BOOLEAN |
| **url**  STRING |

### integrations

The `integrations` table contains information about all integrations in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/integration#get_all_integrations "Opens in new tab: Looker API method") |

integrations table foreign keys

| Join integrations with | on |
| --- | --- |
| [integration\_hubs](#integration-hubs) | ``` integrations.integration_hub_id = integration_hubs.id ``` |

integrations table schema

|  |
| --- |
| **delegate\_oauth**  BOOLEAN |
| **description**  STRING |
| **enabled**  BOOLEAN |
| **icon\_url**  STRING |
| **id**  STRING |
| **installed\_delegate\_oauth**  STRING |
| **integration\_hub\_id**  STRING |
| **label**  STRING |
| **params**  ARRAY This is a nested data structure:   - delegate\_oauth\_url: STRING - description: STRING - has\_value: BOOLEAN - label: STRING - name: STRING - per\_user: BOOLEAN - required: BOOLEAN - sensitive: BOOLEAN - user\_attribute\_name: STRING - value: STRING |
| **required\_fields**  ARRAY This is a nested data structure:   - all\_tags: ARRAY, which is also a nested data structure. - any\_tag: ARRAY, which is also a nested data structure. - tag: STRING |
| **supported\_action\_types**  ARRAY This is a nested data structure. |
| **supported\_download\_settings**  ARRAY This is a nested data structure. |
| **supported\_formats**  ARRAY This is a nested data structure. |
| **supported\_formattings**  ARRAY This is a nested data structure. |
| **supported\_visualization\_formattings**  ARRAY This is a nested data structure. |
| **uses\_oauth**  BOOLEAN |

### lookml\_dashboards

The `lookml_dashboards` table contains information about LookML dashboards in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboards "Opens in new tab: Looker API method") |

lookml\_dashboards table foreign keys

| Join lookml\_dashboards with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` lookml_dashboards.content_favorite_id = content_favorites.id ```  ``` lookml_dashboards.content_favorite_id = content_favorites.dashboard.content_favorite_id ```  ``` lookml_dashboards.content_metadata_id = content_favorites.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = content_favorites.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = content_favorites.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` lookml_dashboards.folder.id = content_favorites.dashboard.folder.id ```  ``` lookml_dashboards.folder.parent_id = content_favorites.dashboard.folder.id ```  ``` lookml_dashboards.folder.id = content_favorites.dashboard.folder.parent_id ```  ``` lookml_dashboards.folder.parent_id = content_favorites.dashboard.folder.parent_id ```  ``` lookml_dashboards.model.id = content_favorites.dashboard.model.id ```  ``` lookml_dashboards.space.id = content_favorites.dashboard.space.id ```  ``` lookml_dashboards.space.parent_id = content_favorites.dashboard.space.id ```  ``` lookml_dashboards.space.id = content_favorites.dashboard.space.parent_id ```  ``` lookml_dashboards.space.parent_id = content_favorites.dashboard.space.parent_id ```  ``` lookml_dashboards.folder.creator_id = content_favorites.dashboard.folder.creator_id ```  ``` lookml_dashboards.space.creator_id = content_favorites.dashboard.folder.creator_id ```  ``` lookml_dashboards.user_id = content_favorites.dashboard.folder.creator_id ```  ``` lookml_dashboards.folder.creator_id = content_favorites.dashboard.space.creator_id ```  ``` lookml_dashboards.space.creator_id = content_favorites.dashboard.space.creator_id ```  ``` lookml_dashboards.user_id = content_favorites.dashboard.space.creator_id ```  ``` lookml_dashboards.folder.creator_id = content_favorites.user_id ```  ``` lookml_dashboards.space.creator_id = content_favorites.user_id ```  ``` lookml_dashboards.user_id = content_favorites.user_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` lookml_dashboards.content_favorite_id = dashboard_elements.look.content_favorite_id ```  ``` lookml_dashboards.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` lookml_dashboards.folder.id = dashboard_elements.look.folder.id ```  ``` lookml_dashboards.folder.parent_id = dashboard_elements.look.folder.id ```  ``` lookml_dashboards.folder.id = dashboard_elements.look.folder.parent_id ```  ``` lookml_dashboards.folder.parent_id = dashboard_elements.look.folder.parent_id ```  ``` lookml_dashboards.folder.id = dashboard_elements.look.folder_id ```  ``` lookml_dashboards.folder.parent_id = dashboard_elements.look.folder_id ```  ``` lookml_dashboards.model.id = dashboard_elements.look.model.id ```  ``` lookml_dashboards.space.id = dashboard_elements.look.space.id ```  ``` lookml_dashboards.space.parent_id = dashboard_elements.look.space.id ```  ``` lookml_dashboards.space.id = dashboard_elements.look.space.parent_id ```  ``` lookml_dashboards.space.parent_id = dashboard_elements.look.space.parent_id ```  ``` lookml_dashboards.folder.creator_id = dashboard_elements.look.deleter_id ```  ``` lookml_dashboards.space.creator_id = dashboard_elements.look.deleter_id ```  ``` lookml_dashboards.user_id = dashboard_elements.look.deleter_id ```  ``` lookml_dashboards.folder.creator_id = dashboard_elements.look.folder.creator_id ```  ``` lookml_dashboards.space.creator_id = dashboard_elements.look.folder.creator_id ```  ``` lookml_dashboards.user_id = dashboard_elements.look.folder.creator_id ```  ``` lookml_dashboards.folder.creator_id = dashboard_elements.look.last_updater_id ```  ``` lookml_dashboards.space.creator_id = dashboard_elements.look.last_updater_id ```  ``` lookml_dashboards.user_id = dashboard_elements.look.last_updater_id ```  ``` lookml_dashboards.folder.creator_id = dashboard_elements.look.space.creator_id ```  ``` lookml_dashboards.space.creator_id = dashboard_elements.look.space.creator_id ```  ``` lookml_dashboards.user_id = dashboard_elements.look.space.creator_id ```  ``` lookml_dashboards.folder.creator_id = dashboard_elements.look.user.id ```  ``` lookml_dashboards.space.creator_id = dashboard_elements.look.user.id ```  ``` lookml_dashboards.user_id = dashboard_elements.look.user.id ```  ``` lookml_dashboards.folder.creator_id = dashboard_elements.look.user_id ```  ``` lookml_dashboards.space.creator_id = dashboard_elements.look.user_id ```  ``` lookml_dashboards.user_id = dashboard_elements.look.user_id ``` |
| [dashboards](#dashboards) | ``` lookml_dashboards.content_favorite_id = dashboards.content_favorite_id ```  ``` lookml_dashboards.content_metadata_id = dashboards.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = dashboards.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = dashboards.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = dashboards.space.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = dashboards.space.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = dashboards.space.content_metadata_id ```  ``` lookml_dashboards.folder.id = dashboards.folder.id ```  ``` lookml_dashboards.folder.parent_id = dashboards.folder.id ```  ``` lookml_dashboards.folder.id = dashboards.folder.parent_id ```  ``` lookml_dashboards.folder.parent_id = dashboards.folder.parent_id ```  ``` lookml_dashboards.model.id = dashboards.model.id ```  ``` lookml_dashboards.space.id = dashboards.space.id ```  ``` lookml_dashboards.space.parent_id = dashboards.space.id ```  ``` lookml_dashboards.space.id = dashboards.space.parent_id ```  ``` lookml_dashboards.space.parent_id = dashboards.space.parent_id ```  ``` lookml_dashboards.folder.creator_id = dashboards.space.creator_id ```  ``` lookml_dashboards.space.creator_id = dashboards.space.creator_id ```  ``` lookml_dashboards.user_id = dashboards.space.creator_id ```  ``` lookml_dashboards.folder.creator_id = dashboards.user_id ```  ``` lookml_dashboards.space.creator_id = dashboards.user_id ```  ``` lookml_dashboards.user_id = dashboards.user_id ``` |
| [folders](#folders) | ``` lookml_dashboards.content_favorite_id = folders.dashboards.content_favorite_id ```  ``` lookml_dashboards.content_favorite_id = folders.looks.content_favorite_id ```  ``` lookml_dashboards.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = folders.looks.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = folders.looks.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = folders.looks.content_metadata_id ```  ``` lookml_dashboards.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` lookml_dashboards.folder.id = folders.id ```  ``` lookml_dashboards.folder.parent_id = folders.id ```  ``` lookml_dashboards.folder.id = folders.dashboards.folder.id ```  ``` lookml_dashboards.folder.parent_id = folders.dashboards.folder.id ```  ``` lookml_dashboards.folder.id = folders.dashboards.folder.parent_id ```  ``` lookml_dashboards.folder.parent_id = folders.dashboards.folder.parent_id ```  ``` lookml_dashboards.folder.id = folders.looks.folder.id ```  ``` lookml_dashboards.folder.parent_id = folders.looks.folder.id ```  ``` lookml_dashboards.folder.id = folders.looks.folder.parent_id ```  ``` lookml_dashboards.folder.parent_id = folders.looks.folder.parent_id ```  ``` lookml_dashboards.folder.id = folders.parent_id ```  ``` lookml_dashboards.folder.parent_id = folders.parent_id ```  ``` lookml_dashboards.model.id = folders.dashboards.model.id ```  ``` lookml_dashboards.model.id = folders.looks.model.id ```  ``` lookml_dashboards.space.id = folders.dashboards.space.id ```  ``` lookml_dashboards.space.parent_id = folders.dashboards.space.id ```  ``` lookml_dashboards.space.id = folders.dashboards.space.parent_id ```  ``` lookml_dashboards.space.parent_id = folders.dashboards.space.parent_id ```  ``` lookml_dashboards.space.id = folders.looks.space.id ```  ``` lookml_dashboards.space.parent_id = folders.looks.space.id ```  ``` lookml_dashboards.space.id = folders.looks.space.parent_id ```  ``` lookml_dashboards.space.parent_id = folders.looks.space.parent_id ```  ``` lookml_dashboards.space.id = folders.looks.space_id ```  ``` lookml_dashboards.space.parent_id = folders.looks.space_id ```  ``` lookml_dashboards.folder.creator_id = folders.creator_id ```  ``` lookml_dashboards.space.creator_id = folders.creator_id ```  ``` lookml_dashboards.user_id = folders.creator_id ```  ``` lookml_dashboards.folder.creator_id = folders.dashboards.user_id ```  ``` lookml_dashboards.space.creator_id = folders.dashboards.user_id ```  ``` lookml_dashboards.user_id = folders.dashboards.user_id ```  ``` lookml_dashboards.folder.creator_id = folders.dashboards.folder.creator_id ```  ``` lookml_dashboards.space.creator_id = folders.dashboards.folder.creator_id ```  ``` lookml_dashboards.user_id = folders.dashboards.folder.creator_id ```  ``` lookml_dashboards.folder.creator_id = folders.dashboards.space.creator_id ```  ``` lookml_dashboards.space.creator_id = folders.dashboards.space.creator_id ```  ``` lookml_dashboards.user_id = folders.dashboards.space.creator_id ```  ``` lookml_dashboards.folder.creator_id = folders.looks.deleter_id ```  ``` lookml_dashboards.space.creator_id = folders.looks.deleter_id ```  ``` lookml_dashboards.user_id = folders.looks.deleter_id ```  ``` lookml_dashboards.folder.creator_id = folders.looks.last_updater_id ```  ``` lookml_dashboards.space.creator_id = folders.looks.last_updater_id ```  ``` lookml_dashboards.user_id = folders.looks.last_updater_id ```  ``` lookml_dashboards.folder.creator_id = folders.looks.user.id ```  ``` lookml_dashboards.space.creator_id = folders.looks.user.id ```  ``` lookml_dashboards.user_id = folders.looks.user.id ``` |
| [looks](#looks) | ``` lookml_dashboards.content_favorite_id = looks.content_favorite_id ```  ``` lookml_dashboards.content_metadata_id = looks.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = looks.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = looks.content_metadata_id ```  ``` lookml_dashboards.folder.id = looks.folder.id ```  ``` lookml_dashboards.folder.parent_id = looks.folder.id ```  ``` lookml_dashboards.folder.id = looks.folder_id ```  ``` lookml_dashboards.folder.parent_id = looks.folder_id ```  ``` lookml_dashboards.folder.id = looks.folder.parent_id ```  ``` lookml_dashboards.folder.parent_id = looks.folder.parent_id ```  ``` lookml_dashboards.model.id = looks.model.id ```  ``` lookml_dashboards.space.id = looks.space.id ```  ``` lookml_dashboards.space.parent_id = looks.space.id ```  ``` lookml_dashboards.space.id = looks.space.parent_id ```  ``` lookml_dashboards.space.parent_id = looks.space.parent_id ```  ``` lookml_dashboards.space.id = looks.space_id ```  ``` lookml_dashboards.space.parent_id = looks.space_id ```  ``` lookml_dashboards.folder.creator_id = looks.deleter_id ```  ``` lookml_dashboards.space.creator_id = looks.deleter_id ```  ``` lookml_dashboards.user_id = looks.deleter_id ```  ``` lookml_dashboards.folder.creator_id = looks.folder.creator_id ```  ``` lookml_dashboards.space.creator_id = looks.folder.creator_id ```  ``` lookml_dashboards.user_id = looks.folder.creator_id ```  ``` lookml_dashboards.folder.creator_id = looks.user.id ```  ``` lookml_dashboards.space.creator_id = looks.user.id ```  ``` lookml_dashboards.user_id = looks.user.id ```  ``` lookml_dashboards.folder.creator_id = looks.user_id ```  ``` lookml_dashboards.space.creator_id = looks.user_id ```  ``` lookml_dashboards.user_id = looks.user_id ``` |
| [content\_metadata](#content-metadata) | ``` lookml_dashboards.content_metadata_id = content_metadata.id ```  ``` lookml_dashboards.folder.content_metadata_id = content_metadata.id ```  ``` lookml_dashboards.space.content_metadata_id = content_metadata.id ```  ``` lookml_dashboards.content_metadata_id = content_metadata.parent_id ```  ``` lookml_dashboards.folder.content_metadata_id = content_metadata.parent_id ```  ``` lookml_dashboards.space.content_metadata_id = content_metadata.parent_id ```  ``` lookml_dashboards.space.id = content_metadata.space_id ```  ``` lookml_dashboards.space.parent_id = content_metadata.space_id ``` |
| [content\_metadata\_access](#content-metadata-access) | ``` lookml_dashboards.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = content_metadata_access.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = content_metadata_access.content_metadata_id ``` |
| [content\_views](#content-views) | ``` lookml_dashboards.content_metadata_id = content_views.content_metadata_id ```  ``` lookml_dashboards.folder.content_metadata_id = content_views.content_metadata_id ```  ``` lookml_dashboards.space.content_metadata_id = content_views.content_metadata_id ```  ``` lookml_dashboards.folder.creator_id = content_views.user_id ```  ``` lookml_dashboards.space.creator_id = content_views.user_id ```  ``` lookml_dashboards.user_id = content_views.user_id ``` |
| [users](#users) | ``` lookml_dashboards.folder.id = users.home_folder_id ```  ``` lookml_dashboards.folder.parent_id = users.home_folder_id ```  ``` lookml_dashboards.folder.id = users.personal_folder_id ```  ``` lookml_dashboards.folder.parent_id = users.personal_folder_id ```  ``` lookml_dashboards.space.id = users.home_space_id ```  ``` lookml_dashboards.space.parent_id = users.home_space_id ```  ``` lookml_dashboards.space.id = users.personal_space_id ```  ``` lookml_dashboards.space.parent_id = users.personal_space_id ```  ``` lookml_dashboards.folder.creator_id = users.id ```  ``` lookml_dashboards.space.creator_id = users.id ```  ``` lookml_dashboards.user_id = users.id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` lookml_dashboards.id = scheduled_plans.lookml_dashboard_id ```  ``` lookml_dashboards.folder.creator_id = scheduled_plans.user.id ```  ``` lookml_dashboards.space.creator_id = scheduled_plans.user.id ```  ``` lookml_dashboards.user_id = scheduled_plans.user.id ```  ``` lookml_dashboards.folder.creator_id = scheduled_plans.user_id ```  ``` lookml_dashboards.space.creator_id = scheduled_plans.user_id ```  ``` lookml_dashboards.user_id = scheduled_plans.user_id ``` |
| [roles](#roles) | ``` lookml_dashboards.model.id = roles.model_set.models ``` |
| [connections](#connections) | ``` lookml_dashboards.folder.creator_id = connections.user_id ```  ``` lookml_dashboards.space.creator_id = connections.user_id ```  ``` lookml_dashboards.user_id = connections.user_id ``` |
| [user\_login\_lockouts](#user-login-lockouts) | ``` lookml_dashboards.folder.creator_id = user_login_lockouts.user_id ```  ``` lookml_dashboards.space.creator_id = user_login_lockouts.user_id ```  ``` lookml_dashboards.user_id = user_login_lockouts.user_id ``` |

lookml\_dashboards table schema

|  |
| --- |
| **content\_favorite\_id**  STRING |
| **content\_metadata\_id**  STRING |
| **description**  STRING |
| **folder**  OBJECT This is a nested data structure:   - child\_count: INTEGER - content\_metadata\_id: STRING - creator\_id: STRING - external\_id: STRING - id: STRING - is\_embed: BOOLEAN - is\_embed\_shared\_root: BOOLEAN - is\_embed\_users\_root: BOOLEAN - is\_personal: BOOLEAN - is\_personal\_descendant: BOOLEAN - is\_shared\_root: BOOLEAN - is\_users\_root: BOOLEAN - name: STRING - parent\_id: STRING |
| **hidden**  BOOLEAN |
| **id**  STRING |
| **model**  OBJECT This is a nested data structure:   - id: STRING - label: STRING |
| **query\_timezone**  STRING |
| **readonly**  BOOLEAN |
| **refresh\_interval**  STRING |
| **refresh\_interval\_to\_i**  INTEGER |
| **space**  OBJECT This is a nested data structure:   - child\_count: INTEGER - content\_metadata\_id: STRING - creator\_id: STRING - external\_id: STRING - id: STRING - is\_embed: BOOLEAN - is\_embed\_shared\_root: BOOLEAN - is\_embed\_users\_root: BOOLEAN - is\_personal: BOOLEAN - is\_personal\_descendant: BOOLEAN - is\_shared\_root: BOOLEAN - is\_users\_root: BOOLEAN - name: STRING - parent\_id: STRING |
| **title**  STRING |
| **user\_id**  STRING |

### lookml\_models

The `lookml_models` table contains information about all LookML models in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | name  project\_name |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/lookml-model#get_all_lookml_models "Opens in new tab: Looker API method") |

lookml\_models table schema

|  |
| --- |
| **allowed\_db\_connection\_names**  ARRAY |
| **explores**  ARRAY This is a nested data structure:   - description: STRING - group\_label: STRING - hidden: BOOLEAN - label: STRING - name: STRING |
| **has\_content**  BOOLEAN |
| **label**  STRING |
| **name**  STRING |
| **project\_name**  STRING |
| **unlimited\_db\_connections**  BOOLEAN |

### looks

The `looks` table contains information about all active looks in your Looker account. **Note**: Based on Looker’s documentation, this table doesn’t include soft-deleted looks.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/look#get_all_looks "Opens in new tab: Looker API method") |

looks table foreign keys

| Join looks with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` looks.content_favorite_id = content_favorites.id ```  ``` looks.content_favorite_id = content_favorites.dashboard.content_favorite_id ```  ``` looks.content_metadata_id = content_favorites.content_metadata_id ```  ``` looks.content_metadata_id = content_favorites.dashboard.content_metadata_id ```  ``` looks.content_metadata_id = content_favorites.dashboard.folder.content_metadata_id ```  ``` looks.content_metadata_id = content_favorites.dashboard.space.content_metadata_id ```  ``` looks.content_metadata_id = content_favorites.look.content_metadata_id ```  ``` looks.folder.id = content_favorites.dashboard.folder.id ```  ``` looks.folder_id = content_favorites.dashboard.folder.id ```  ``` looks.folder.parent_id = content_favorites.dashboard.folder.id ```  ``` looks.folder.id = content_favorites.dashboard.folder.parent_id ```  ``` looks.folder_id = content_favorites.dashboard.folder.parent_id ```  ``` looks.folder.parent_id = content_favorites.dashboard.folder.parent_id ```  ``` looks.id = content_favorites.look_id ```  ``` looks.id = content_favorites.look.id ```  ``` looks.model.id = content_favorites.dashboard.model.id ```  ``` looks.space.id = content_favorites.dashboard.space.id ```  ``` looks.space.parent_id = content_favorites.dashboard.space.id ```  ``` looks.space_id = content_favorites.dashboard.space.id ```  ``` looks.space.id = content_favorites.dashboard.space.parent_id ```  ``` looks.space.parent_id = content_favorites.dashboard.space.parent_id ```  ``` looks.space_id = content_favorites.dashboard.space.parent_id ```  ``` looks.deleter_id = content_favorites.dashboard.folder.creator_id ```  ``` looks.folder.creator_id = content_favorites.dashboard.folder.creator_id ```  ``` looks.user.id = content_favorites.dashboard.folder.creator_id ```  ``` looks.user_id = content_favorites.dashboard.folder.creator_id ```  ``` looks.deleter_id = content_favorites.dashboard.space.creator_id ```  ``` looks.folder.creator_id = content_favorites.dashboard.space.creator_id ```  ``` looks.user.id = content_favorites.dashboard.space.creator_id ```  ``` looks.user_id = content_favorites.dashboard.space.creator_id ```  ``` looks.deleter_id = content_favorites.user_id ```  ``` looks.folder.creator_id = content_favorites.user_id ```  ``` looks.user.id = content_favorites.user_id ```  ``` looks.user_id = content_favorites.user_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` looks.content_favorite_id = dashboard_elements.look.content_favorite_id ```  ``` looks.content_metadata_id = dashboard_elements.look.content_metadata_id ```  ``` looks.content_metadata_id = dashboard_elements.look.folder.content_metadata_id ```  ``` looks.content_metadata_id = dashboard_elements.look.space.content_metadata_id ```  ``` looks.folder.id = dashboard_elements.look.folder.id ```  ``` looks.folder_id = dashboard_elements.look.folder.id ```  ``` looks.folder.parent_id = dashboard_elements.look.folder.id ```  ``` looks.folder.id = dashboard_elements.look.folder.parent_id ```  ``` looks.folder_id = dashboard_elements.look.folder.parent_id ```  ``` looks.folder.parent_id = dashboard_elements.look.folder.parent_id ```  ``` looks.folder.id = dashboard_elements.look.folder_id ```  ``` looks.folder_id = dashboard_elements.look.folder_id ```  ``` looks.folder.parent_id = dashboard_elements.look.folder_id ```  ``` looks.id = dashboard_elements.look.id ```  ``` looks.id = dashboard_elements.look_id ```  ``` looks.model.id = dashboard_elements.look.model.id ```  ``` looks.query_id = dashboard_elements.look.query.id ```  ``` looks.query_id = dashboard_elements.look.query_id ```  ``` looks.query_id = dashboard_elements.query.id ```  ``` looks.query_id = dashboard_elements.query_id ```  ``` looks.query_id = dashboard_elements.result_maker.query.id ```  ``` looks.query_id = dashboard_elements.result_maker.query_id ```  ``` looks.space.id = dashboard_elements.look.space.id ```  ``` looks.space.parent_id = dashboard_elements.look.space.id ```  ``` looks.space_id = dashboard_elements.look.space.id ```  ``` looks.space.id = dashboard_elements.look.space.parent_id ```  ``` looks.space.parent_id = dashboard_elements.look.space.parent_id ```  ``` looks.space_id = dashboard_elements.look.space.parent_id ```  ``` looks.deleter_id = dashboard_elements.look.deleter_id ```  ``` looks.folder.creator_id = dashboard_elements.look.deleter_id ```  ``` looks.user.id = dashboard_elements.look.deleter_id ```  ``` looks.user_id = dashboard_elements.look.deleter_id ```  ``` looks.deleter_id = dashboard_elements.look.folder.creator_id ```  ``` looks.folder.creator_id = dashboard_elements.look.folder.creator_id ```  ``` looks.user.id = dashboard_elements.look.folder.creator_id ```  ``` looks.user_id = dashboard_elements.look.folder.creator_id ```  ``` looks.deleter_id = dashboard_elements.look.last_updater_id ```  ``` looks.folder.creator_id = dashboard_elements.look.last_updater_id ```  ``` looks.user.id = dashboard_elements.look.last_updater_id ```  ``` looks.user_id = dashboard_elements.look.last_updater_id ```  ``` looks.deleter_id = dashboard_elements.look.space.creator_id ```  ``` looks.folder.creator_id = dashboard_elements.look.space.creator_id ```  ``` looks.user.id = dashboard_elements.look.space.creator_id ```  ``` looks.user_id = dashboard_elements.look.space.creator_id ```  ``` looks.deleter_id = dashboard_elements.look.user.id ```  ``` looks.folder.creator_id = dashboard_elements.look.user.id ```  ``` looks.user.id = dashboard_elements.look.user.id ```  ``` looks.user_id = dashboard_elements.look.user.id ```  ``` looks.deleter_id = dashboard_elements.look.user_id ```  ``` looks.folder.creator_id = dashboard_elements.look.user_id ```  ``` looks.user.id = dashboard_elements.look.user_id ```  ``` looks.user_id = dashboard_elements.look.user_id ``` |
| [dashboards](#dashboards) | ``` looks.content_favorite_id = dashboards.content_favorite_id ```  ``` looks.content_metadata_id = dashboards.content_metadata_id ```  ``` looks.content_metadata_id = dashboards.folder.content_metadata_id ```  ``` looks.content_metadata_id = dashboards.space.content_metadata_id ```  ``` looks.folder.id = dashboards.folder.id ```  ``` looks.folder_id = dashboards.folder.id ```  ``` looks.folder.parent_id = dashboards.folder.id ```  ``` looks.folder.id = dashboards.folder.parent_id ```  ``` looks.folder_id = dashboards.folder.parent_id ```  ``` looks.folder.parent_id = dashboards.folder.parent_id ```  ``` looks.model.id = dashboards.model.id ```  ``` looks.space.id = dashboards.space.id ```  ``` looks.space.parent_id = dashboards.space.id ```  ``` looks.space_id = dashboards.space.id ```  ``` looks.space.id = dashboards.space.parent_id ```  ``` looks.space.parent_id = dashboards.space.parent_id ```  ``` looks.space_id = dashboards.space.parent_id ```  ``` looks.deleter_id = dashboards.space.creator_id ```  ``` looks.folder.creator_id = dashboards.space.creator_id ```  ``` looks.user.id = dashboards.space.creator_id ```  ``` looks.user_id = dashboards.space.creator_id ```  ``` looks.deleter_id = dashboards.user_id ```  ``` looks.folder.creator_id = dashboards.user_id ```  ``` looks.user.id = dashboards.user_id ```  ``` looks.user_id = dashboards.user_id ``` |
| [folders](#folders) | ``` looks.content_favorite_id = folders.dashboards.content_favorite_id ```  ``` looks.content_favorite_id = folders.looks.content_favorite_id ```  ``` looks.content_metadata_id = folders.dashboards.folder.content_metadata_id ```  ``` looks.content_metadata_id = folders.dashboards.space.content_metadata_id ```  ``` looks.content_metadata_id = folders.looks.content_metadata_id ```  ``` looks.content_metadata_id = folders.looks.folder.content_metadata_id ```  ``` looks.folder.id = folders.id ```  ``` looks.folder_id = folders.id ```  ``` looks.folder.parent_id = folders.id ```  ``` looks.folder.id = folders.dashboards.folder.id ```  ``` looks.folder_id = folders.dashboards.folder.id ```  ``` looks.folder.parent_id = folders.dashboards.folder.id ```  ``` looks.folder.id = folders.dashboards.folder.parent_id ```  ``` looks.folder_id = folders.dashboards.folder.parent_id ```  ``` looks.folder.parent_id = folders.dashboards.folder.parent_id ```  ``` looks.folder.id = folders.looks.folder.id ```  ``` looks.folder_id = folders.looks.folder.id ```  ``` looks.folder.parent_id = folders.looks.folder.id ```  ``` looks.folder.id = folders.looks.folder.parent_id ```  ``` looks.folder_id = folders.looks.folder.parent_id ```  ``` looks.folder.parent_id = folders.looks.folder.parent_id ```  ``` looks.folder.id = folders.parent_id ```  ``` looks.folder_id = folders.parent_id ```  ``` looks.folder.parent_id = folders.parent_id ```  ``` looks.id = folders.looks.id ```  ``` looks.model.id = folders.dashboards.model.id ```  ``` looks.model.id = folders.looks.model.id ```  ``` looks.query_id = folders.looks.query_id ```  ``` looks.space.id = folders.dashboards.space.id ```  ``` looks.space.parent_id = folders.dashboards.space.id ```  ``` looks.space_id = folders.dashboards.space.id ```  ``` looks.space.id = folders.dashboards.space.parent_id ```  ``` looks.space.parent_id = folders.dashboards.space.parent_id ```  ``` looks.space_id = folders.dashboards.space.parent_id ```  ``` looks.space.id = folders.looks.space.id ```  ``` looks.space.parent_id = folders.looks.space.id ```  ``` looks.space_id = folders.looks.space.id ```  ``` looks.space.id = folders.looks.space.parent_id ```  ``` looks.space.parent_id = folders.looks.space.parent_id ```  ``` looks.space_id = folders.looks.space.parent_id ```  ``` looks.space.id = folders.looks.space_id ```  ``` looks.space.parent_id = folders.looks.space_id ```  ``` looks.space_id = folders.looks.space_id ```  ``` looks.deleter_id = folders.creator_id ```  ``` looks.folder.creator_id = folders.creator_id ```  ``` looks.user.id = folders.creator_id ```  ``` looks.user_id = folders.creator_id ```  ``` looks.deleter_id = folders.dashboards.user_id ```  ``` looks.folder.creator_id = folders.dashboards.user_id ```  ``` looks.user.id = folders.dashboards.user_id ```  ``` looks.user_id = folders.dashboards.user_id ```  ``` looks.deleter_id = folders.dashboards.folder.creator_id ```  ``` looks.folder.creator_id = folders.dashboards.folder.creator_id ```  ``` looks.user.id = folders.dashboards.folder.creator_id ```  ``` looks.user_id = folders.dashboards.folder.creator_id ```  ``` looks.deleter_id = folders.dashboards.space.creator_id ```  ``` looks.folder.creator_id = folders.dashboards.space.creator_id ```  ``` looks.user.id = folders.dashboards.space.creator_id ```  ``` looks.user_id = folders.dashboards.space.creator_id ```  ``` looks.deleter_id = folders.looks.deleter_id ```  ``` looks.folder.creator_id = folders.looks.deleter_id ```  ``` looks.user.id = folders.looks.deleter_id ```  ``` looks.user_id = folders.looks.deleter_id ```  ``` looks.deleter_id = folders.looks.last_updater_id ```  ``` looks.folder.creator_id = folders.looks.last_updater_id ```  ``` looks.user.id = folders.looks.last_updater_id ```  ``` looks.user_id = folders.looks.last_updater_id ```  ``` looks.deleter_id = folders.looks.user.id ```  ``` looks.folder.creator_id = folders.looks.user.id ```  ``` looks.user.id = folders.looks.user.id ```  ``` looks.user_id = folders.looks.user.id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` looks.content_favorite_id = lookml_dashboards.content_favorite_id ```  ``` looks.content_metadata_id = lookml_dashboards.content_metadata_id ```  ``` looks.content_metadata_id = lookml_dashboards.folder.content_metadata_id ```  ``` looks.content_metadata_id = lookml_dashboards.space.content_metadata_id ```  ``` looks.folder.id = lookml_dashboards.folder.id ```  ``` looks.folder_id = lookml_dashboards.folder.id ```  ``` looks.folder.parent_id = lookml_dashboards.folder.id ```  ``` looks.folder.id = lookml_dashboards.folder.parent_id ```  ``` looks.folder_id = lookml_dashboards.folder.parent_id ```  ``` looks.folder.parent_id = lookml_dashboards.folder.parent_id ```  ``` looks.model.id = lookml_dashboards.model.id ```  ``` looks.space.id = lookml_dashboards.space.id ```  ``` looks.space.parent_id = lookml_dashboards.space.id ```  ``` looks.space_id = lookml_dashboards.space.id ```  ``` looks.space.id = lookml_dashboards.space.parent_id ```  ``` looks.space.parent_id = lookml_dashboards.space.parent_id ```  ``` looks.space_id = lookml_dashboards.space.parent_id ```  ``` looks.deleter_id = lookml_dashboards.folder.creator_id ```  ``` looks.folder.creator_id = lookml_dashboards.folder.creator_id ```  ``` looks.user.id = lookml_dashboards.folder.creator_id ```  ``` looks.user_id = lookml_dashboards.folder.creator_id ```  ``` looks.deleter_id = lookml_dashboards.space.creator_id ```  ``` looks.folder.creator_id = lookml_dashboards.space.creator_id ```  ``` looks.user.id = lookml_dashboards.space.creator_id ```  ``` looks.user_id = lookml_dashboards.space.creator_id ```  ``` looks.deleter_id = lookml_dashboards.user_id ```  ``` looks.folder.creator_id = lookml_dashboards.user_id ```  ``` looks.user.id = lookml_dashboards.user_id ```  ``` looks.user_id = lookml_dashboards.user_id ``` |
| [content\_metadata](#content-metadata) | ``` looks.content_metadata_id = content_metadata.id ```  ``` looks.content_metadata_id = content_metadata.parent_id ```  ``` looks.id = content_metadata.look_id ```  ``` looks.space.id = content_metadata.space_id ```  ``` looks.space.parent_id = content_metadata.space_id ```  ``` looks.space_id = content_metadata.space_id ``` |
| [content\_metadata\_access](#content-metadata-access) | ``` looks.content_metadata_id = content_metadata_access.content_metadata_id ``` |
| [content\_views](#content-views) | ``` looks.content_metadata_id = content_views.content_metadata_id ```  ``` looks.id = content_views.look_id ```  ``` looks.deleter_id = content_views.user_id ```  ``` looks.folder.creator_id = content_views.user_id ```  ``` looks.user.id = content_views.user_id ```  ``` looks.user_id = content_views.user_id ``` |
| [users](#users) | ``` looks.folder.id = users.home_folder_id ```  ``` looks.folder_id = users.home_folder_id ```  ``` looks.folder.parent_id = users.home_folder_id ```  ``` looks.folder.id = users.personal_folder_id ```  ``` looks.folder_id = users.personal_folder_id ```  ``` looks.folder.parent_id = users.personal_folder_id ```  ``` looks.space.id = users.home_space_id ```  ``` looks.space.parent_id = users.home_space_id ```  ``` looks.space_id = users.home_space_id ```  ``` looks.space.id = users.personal_space_id ```  ``` looks.space.parent_id = users.personal_space_id ```  ``` looks.space_id = users.personal_space_id ```  ``` looks.deleter_id = users.id ```  ``` looks.folder.creator_id = users.id ```  ``` looks.user.id = users.id ```  ``` looks.user_id = users.id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` looks.id = scheduled_plans.look_id ```  ``` looks.query_id = scheduled_plans.query_id ```  ``` looks.deleter_id = scheduled_plans.user.id ```  ``` looks.folder.creator_id = scheduled_plans.user.id ```  ``` looks.user.id = scheduled_plans.user.id ```  ``` looks.user_id = scheduled_plans.user.id ```  ``` looks.deleter_id = scheduled_plans.user_id ```  ``` looks.folder.creator_id = scheduled_plans.user_id ```  ``` looks.user.id = scheduled_plans.user_id ```  ``` looks.user_id = scheduled_plans.user_id ``` |
| [roles](#roles) | ``` looks.model.id = roles.model_set.models ``` |
| [queries](#queries) | ``` looks.query_id = queries.id ``` |
| [connections](#connections) | ``` looks.deleter_id = connections.user_id ```  ``` looks.folder.creator_id = connections.user_id ```  ``` looks.user.id = connections.user_id ```  ``` looks.user_id = connections.user_id ``` |
| [user\_login\_lockouts](#user-login-lockouts) | ``` looks.deleter_id = user_login_lockouts.user_id ```  ``` looks.folder.creator_id = user_login_lockouts.user_id ```  ``` looks.user.id = user_login_lockouts.user_id ```  ``` looks.user_id = user_login_lockouts.user_id ``` |

looks table schema

|  |
| --- |
| **content\_favorite\_id**  STRING |
| **content\_metadata\_id**  STRING |
| **created\_at**  DATE-TIME |
| **deleted**  BOOLEAN |
| **deleted\_at**  DATE-TIME |
| **deleter\_id**  STRING |
| **description**  STRING |
| **embed\_url**  STRING |
| **excel\_file\_url**  STRING |
| **favorite\_count**  INTEGER |
| **folder**  OBJECT This is a nested data structure:   - child\_count: INTEGER - content\_metadata\_id: STRING - creator\_id: STRING - external\_id: STRING - id: STRING - is\_embed: BOOLEAN - is\_embed\_shared\_root: BOOLEAN - is\_embed\_users\_root: BOOLEAN - is\_personal: BOOLEAN - is\_personal\_descendant: BOOLEAN - is\_shared\_root: BOOLEAN - is\_users\_root: BOOLEAN - name: STRING - parent\_id: STRING |
| **folder\_id**  STRING |
| **google\_spreadsheet\_formula**  STRING |
| **id**  STRING |
| **image\_embed\_url**  STRING |
| **is\_run\_on\_load**  BOOLEAN |
| **last\_accessed\_at**  DATE-TIME |
| **last\_updater\_id**  STRING |
| **last\_viewed\_at**  DATE-TIME |
| **model**  OBJECT This is a nested data structure:   - id: STRING - label: STRING |
| **public**  BOOLEAN |
| **public\_slug**  STRING |
| **public\_url**  STRING |
| **query\_id**  STRING |
| **short\_url**  STRING |
| **space**  OBJECT This is a nested data structure:   - child\_count: INTEGER - content\_metadata\_id: STRING - creator\_id: STRING - external\_id: STRING - id: STRING - is\_embed: BOOLEAN - is\_embed\_shared\_root: BOOLEAN - is\_embed\_users\_root: BOOLEAN - is\_personal: BOOLEAN - is\_personal\_descendant: BOOLEAN - is\_shared\_root: BOOLEAN - is\_users\_root: BOOLEAN - name: STRING - parent\_id: STRING |
| **space\_id**  STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |
| **user**  OBJECT This is a nested data structure:   - id: STRING |
| **user\_id**  STRING |
| **view\_count**  INTEGER |

### merge\_queries

The `merge_queries` table contains info about the merge queries in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/query#get_merge_query "Opens in new tab: Looker API method") |

merge\_queries table schema

|  |
| --- |
| **column\_limit**  STRING |
| **dynamic\_fields**  STRING |
| **id**  STRING |
| **pivots**  ARRAY This is a nested data structure. |
| **result\_maker\_id**  STRING |
| **sorts**  ARRAY This is a nested data structure. |
| **source\_queries**  ARRAY This is a nested data structure:   - merge\_fields: ARRAY, which is also a nested data structure.   - field\_name: STRING   - source\_field\_name: STRING - name: STRING - query\_id: STRING |
| **total**  BOOLEAN |
| **vis\_config**  OBJECT This is a nested data structure. |

### model\_sets

The `model_sets` table contains info about the role model sets in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/role#get_all_model_sets "Opens in new tab: Looker API method") |

model\_sets table foreign keys

| Join model\_sets with | on |
| --- | --- |
| [roles](#roles) | ``` model_sets.id = roles.model_set.id ```  ``` model_sets.id = roles.model_set_id ``` |

model\_sets table schema

|  |
| --- |
| **all\_access**  BOOLEAN |
| **built\_in**  BOOLEAN |
| **id**  STRING |
| **models**  ARRAY This is a nested data structure. |
| **name**  STRING |
| **url**  STRING |

### models

The `models` table contains information about individual models in your Looker account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | name  project\_name |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/lookml-model#get_lookml_model "Opens in new tab: Looker API method") |

models table schema

|  |
| --- |
| **allowed\_db\_connection\_names**  ARRAY This is a nested data structure. |
| **explores**  ARRAY This is a nested data structure:   - description: STRING - group\_label: STRING - hidden: BOOLEAN - label: STRING - name: STRING |
| **has\_content**  BOOLEAN |
| **label**  STRING |
| **name**  STRING |
| **project\_name**  STRING |
| **unlimited\_db\_connections**  BOOLEAN |

### permission\_sets

The `permission_sets` table contains info about the role permission sets in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/role#get_all_permission_sets "Opens in new tab: Looker API method") |

permission\_sets table foreign keys

| Join permission\_sets with | on |
| --- | --- |
| [roles](#roles) | ``` permission_sets.id = roles.permission_set_id ```  ``` permission_sets.id = roles.id ``` |

permission\_sets table schema

|  |
| --- |
| **all\_access**  BOOLEAN |
| **built\_in**  BOOLEAN |
| **id**  STRING |
| **name**  STRING |
| **permissions**  ARRAY This is a nested data structure. |
| **url**  STRING |

### permissions

The `permissions` table contains info about the permissions listed in your Looker account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | permission |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/role#get_all_permissions "Opens in new tab: Looker API method") |

permissions table schema

|  |
| --- |
| **description**  STRING |
| **parent**  STRING |
| **permission**  STRING |

### project\_files

The `project_files` table contains info about the files associated with projects in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/project#get_all_project_files "Opens in new tab: Looker API method") |

project\_files table foreign keys

| Join project\_files with | on |
| --- | --- |
| [git\_branches](#git-branches) | ``` project_files.project_id = git_branches.project_id ``` |
| [projects](#projects) | ``` project_files.project_id = projects.id ``` |
| [workspaces](#workspaces) | ``` project_files.project_id = workspaces.projects.id ``` |

project\_files table schema

|  |
| --- |
| **editable**  BOOLEAN |
| **extension**  STRING |
| **git\_status**  OBJECT This is a nested data structure:   - action: STRING - conflict: BOOLEAN - revertable: BOOLEAN - text: STRING |
| **id**  STRING |
| **mime\_type**  STRING |
| **path**  STRING |
| **project\_id**  STRING |
| **title**  STRING |
| **type**  STRING |

### projects

The `projects` table contains info about the projects in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/project#get_all_projects "Opens in new tab: Looker API method") |

projects table foreign keys

| Join projects with | on |
| --- | --- |
| [git\_branches](#git-branches) | ``` projects.id = git_branches.project_id ``` |
| [project\_files](#project-files) | ``` projects.id = project_files.project_id ``` |
| [workspaces](#workspaces) | ``` projects.id = workspaces.projects.id ``` |

projects table schema

|  |
| --- |
| **allow\_warnings**  BOOLEAN |
| **deploy\_secret**  STRING |
| **folders\_enabled**  BOOLEAN |
| **git\_password**  STRING |
| **git\_password\_user\_attribute**  STRING |
| **git\_remote\_url**  STRING |
| **git\_service\_name**  STRING |
| **git\_username**  STRING |
| **git\_username\_user\_attribute**  STRING |
| **id**  STRING |
| **is\_example**  BOOLEAN |
| **name**  STRING |
| **pull\_request\_mode**  STRING |
| **unset\_deploy\_secret**  BOOLEAN |
| **uses\_git**  BOOLEAN |
| **validation\_required**  BOOLEAN |

### queries

The `queries` table contains info about the queries that exist in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/query#get_query "Opens in new tab: Looker API method") |

queries table foreign keys

| Join queries with | on |
| --- | --- |
| [dashboard\_elements](#dashboard-elements) | ``` queries.id = dashboard_elements.look.query.id ```  ``` queries.id = dashboard_elements.look.query_id ```  ``` queries.id = dashboard_elements.query.id ```  ``` queries.id = dashboard_elements.query_id ```  ``` queries.id = dashboard_elements.result_maker.query.id ```  ``` queries.id = dashboard_elements.result_maker.query_id ``` |
| [folders](#folders) | ``` queries.id = folders.looks.query_id ``` |
| [looks](#looks) | ``` queries.id = looks.query_id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` queries.id = scheduled_plans.query_id ``` |

queries table schema

|  |
| --- |
| **client\_id**  STRING |
| **column\_limit**  STRING |
| **dynamic\_fields**  STRING |
| **expanded\_share\_url**  STRING |
| **fields**  ARRAY This is a nested data structure. |
| **fill\_fields**  ARRAY This is a nested data structure. |
| **filter\_config**  OBJECT This is a nested data structure. |
| **filter\_expression**  STRING |
| **filters**  OBJECT This is a nested data structure. |
| **has\_table\_calculations**  BOOLEAN |
| **id**  STRING |
| **limit**  STRING |
| **model**  STRING |
| **pivots**  ARRAY This is a nested data structure. |
| **query\_timezone**  STRING |
| **row\_total**  STRING |
| **runtime**  NUMBER |
| **share\_url**  STRING |
| **slug**  STRING |
| **sorts**  ARRAY This is a nested data structure. |
| **subtotals**  ARRAY This is a nested data structure. |
| **total**  BOOLEAN |
| **url**  STRING |
| **view**  STRING |
| **vis\_config**  OBJECT This is a nested data structure. |
| **visible\_ui\_sections**  STRING |

### query\_history

The `query_history` table contains query history data pulled from Looker’s [History Explore](https://docs.looker.com/admin-options/tutorials/i__looker), or `i__looker` database, for queries run in the past seven days.

To extract this data, a query will be submitted to the Looker API. The results of query are then extracted and replicated to your destination.

**Note**: Looker integration only replicates the **past seven days** of query history at any given time.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | dims\_hash\_key  history\_created\_date  query\_id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/query#run_inline_query "Opens in new tab: Looker API method") |

query\_history table schema

|  |
| --- |
| **dashboard\_id**  STRING |
| **dims\_hash\_key**  STRING |
| **history\_created\_date**  STRING |
| **history\_query\_run\_count**  INTEGER |
| **history\_total\_runtime**  NUMBER |
| **look\_id**  STRING |
| **query\_id**  STRING |
| **query\_model**  STRING |
| **query\_view**  STRING |
| **space\_id**  STRING |
| **user\_id**  STRING |

### role\_groups

The `role_groups` table contains info about the role groups in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/role#get_role_groups "Opens in new tab: Looker API method") |

role\_groups table foreign keys

| Join role\_groups with | on |
| --- | --- |
| [roles](#roles) | ``` role_groups.role_id = roles.id ``` |
| [users](#users) | ``` role_groups.role_id = users.role_ids ``` |

role\_groups table schema

|  |
| --- |
| **can\_add\_to\_content\_metadata**  BOOLEAN |
| **contains\_current\_user**  BOOLEAN |
| **external\_group\_id**  STRING |
| **externally\_managed**  BOOLEAN |
| **id**  STRING |
| **include\_by\_default**  BOOLEAN |
| **name**  STRING |
| **role\_id**  STRING |
| **user\_count**  INTEGER |

### roles

The `roles` table contains info about the user roles in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/role#get_all_roles "Opens in new tab: Looker API method") |

roles table foreign keys

| Join roles with | on |
| --- | --- |
| [model\_sets](#model-sets) | ``` roles.model_set.id = model_sets.id ```  ``` roles.model_set_id = model_sets.id ``` |
| [content\_favorites](#content-favorites) | ``` roles.model_set.models = content_favorites.dashboard.model.id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` roles.model_set.models = dashboard_elements.look.model.id ``` |
| [dashboards](#dashboards) | ``` roles.model_set.models = dashboards.model.id ``` |
| [folders](#folders) | ``` roles.model_set.models = folders.dashboards.model.id ```  ``` roles.model_set.models = folders.looks.model.id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` roles.model_set.models = lookml_dashboards.model.id ``` |
| [looks](#looks) | ``` roles.model_set.models = looks.model.id ``` |
| [permission\_sets](#permission-sets) | ``` roles.permission_set_id = permission_sets.id ```  ``` roles.id = permission_sets.id ``` |
| [role\_groups](#role-groups) | ``` roles.id = role_groups.role_id ``` |
| [users](#users) | ``` roles.id = users.role_ids ``` |

roles table schema

|  |
| --- |
| **id**  STRING |
| **model\_set**  OBJECT This is a nested data structure:   - all\_access: BOOLEAN - built\_in: BOOLEAN - id: STRING - models: ARRAY, which is also a nested data structure. - name: STRING - url: STRING |
| **model\_set\_id**  STRING |
| **name**  STRING |
| **permission\_set**  OBJECT This is a nested data structure:   - all\_access: BOOLEAN - built\_in: BOOLEAN - id: STRING - name: STRING - permissions: ARRAY, which is also a nested data structure. - url: STRING |
| **permission\_set\_id**  STRING |
| **url**  STRING |
| **users\_url**  STRING |

### scheduled\_plans

The `scheduled_plans` table contains info about all scheduled plans in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/scheduled-plan#get_all_scheduled_plans "Opens in new tab: Looker API method") |

scheduled\_plans table foreign keys

| Join scheduled\_plans with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` scheduled_plans.dashboard_id = content_favorites.dashboard.id ```  ``` scheduled_plans.dashboard_id = content_favorites.dashboard_id ```  ``` scheduled_plans.look_id = content_favorites.look_id ```  ``` scheduled_plans.look_id = content_favorites.look.id ```  ``` scheduled_plans.user.id = content_favorites.dashboard.folder.creator_id ```  ``` scheduled_plans.user_id = content_favorites.dashboard.folder.creator_id ```  ``` scheduled_plans.user.id = content_favorites.dashboard.space.creator_id ```  ``` scheduled_plans.user_id = content_favorites.dashboard.space.creator_id ```  ``` scheduled_plans.user.id = content_favorites.user_id ```  ``` scheduled_plans.user_id = content_favorites.user_id ``` |
| [content\_metadata](#content-metadata) | ``` scheduled_plans.dashboard_id = content_metadata.dashboard_id ```  ``` scheduled_plans.look_id = content_metadata.look_id ``` |
| [content\_views](#content-views) | ``` scheduled_plans.dashboard_id = content_views.dashboard_id ```  ``` scheduled_plans.look_id = content_views.look_id ```  ``` scheduled_plans.user.id = content_views.user_id ```  ``` scheduled_plans.user_id = content_views.user_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` scheduled_plans.dashboard_id = dashboard_elements.dashboard_id ```  ``` scheduled_plans.look_id = dashboard_elements.look.id ```  ``` scheduled_plans.look_id = dashboard_elements.look_id ```  ``` scheduled_plans.query_id = dashboard_elements.look.query.id ```  ``` scheduled_plans.query_id = dashboard_elements.look.query_id ```  ``` scheduled_plans.query_id = dashboard_elements.query.id ```  ``` scheduled_plans.query_id = dashboard_elements.query_id ```  ``` scheduled_plans.query_id = dashboard_elements.result_maker.query.id ```  ``` scheduled_plans.query_id = dashboard_elements.result_maker.query_id ```  ``` scheduled_plans.user.id = dashboard_elements.look.deleter_id ```  ``` scheduled_plans.user_id = dashboard_elements.look.deleter_id ```  ``` scheduled_plans.user.id = dashboard_elements.look.folder.creator_id ```  ``` scheduled_plans.user_id = dashboard_elements.look.folder.creator_id ```  ``` scheduled_plans.user.id = dashboard_elements.look.last_updater_id ```  ``` scheduled_plans.user_id = dashboard_elements.look.last_updater_id ```  ``` scheduled_plans.user.id = dashboard_elements.look.space.creator_id ```  ``` scheduled_plans.user_id = dashboard_elements.look.space.creator_id ```  ``` scheduled_plans.user.id = dashboard_elements.look.user.id ```  ``` scheduled_plans.user_id = dashboard_elements.look.user.id ```  ``` scheduled_plans.user.id = dashboard_elements.look.user_id ```  ``` scheduled_plans.user_id = dashboard_elements.look.user_id ``` |
| [dashboard\_filters](#dashboard-filters) | ``` scheduled_plans.dashboard_id = dashboard_filters.dashboard_id ``` |
| [dashboard\_layouts](#dashboard-layouts) | ``` scheduled_plans.dashboard_id = dashboard_layouts.dashboard_id ``` |
| [dashboards](#dashboards) | ``` scheduled_plans.dashboard_id = dashboards.id ```  ``` scheduled_plans.user.id = dashboards.space.creator_id ```  ``` scheduled_plans.user_id = dashboards.space.creator_id ```  ``` scheduled_plans.user.id = dashboards.user_id ```  ``` scheduled_plans.user_id = dashboards.user_id ``` |
| [folders](#folders) | ``` scheduled_plans.dashboard_id = folders.dashboards.id ```  ``` scheduled_plans.look_id = folders.looks.id ```  ``` scheduled_plans.query_id = folders.looks.query_id ```  ``` scheduled_plans.user.id = folders.creator_id ```  ``` scheduled_plans.user_id = folders.creator_id ```  ``` scheduled_plans.user.id = folders.dashboards.user_id ```  ``` scheduled_plans.user_id = folders.dashboards.user_id ```  ``` scheduled_plans.user.id = folders.dashboards.folder.creator_id ```  ``` scheduled_plans.user_id = folders.dashboards.folder.creator_id ```  ``` scheduled_plans.user.id = folders.dashboards.space.creator_id ```  ``` scheduled_plans.user_id = folders.dashboards.space.creator_id ```  ``` scheduled_plans.user.id = folders.looks.deleter_id ```  ``` scheduled_plans.user_id = folders.looks.deleter_id ```  ``` scheduled_plans.user.id = folders.looks.last_updater_id ```  ``` scheduled_plans.user_id = folders.looks.last_updater_id ```  ``` scheduled_plans.user.id = folders.looks.user.id ```  ``` scheduled_plans.user_id = folders.looks.user.id ``` |
| [looks](#looks) | ``` scheduled_plans.look_id = looks.id ```  ``` scheduled_plans.query_id = looks.query_id ```  ``` scheduled_plans.user.id = looks.deleter_id ```  ``` scheduled_plans.user_id = looks.deleter_id ```  ``` scheduled_plans.user.id = looks.folder.creator_id ```  ``` scheduled_plans.user_id = looks.folder.creator_id ```  ``` scheduled_plans.user.id = looks.user.id ```  ``` scheduled_plans.user_id = looks.user.id ```  ``` scheduled_plans.user.id = looks.user_id ```  ``` scheduled_plans.user_id = looks.user_id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` scheduled_plans.lookml_dashboard_id = lookml_dashboards.id ```  ``` scheduled_plans.user.id = lookml_dashboards.folder.creator_id ```  ``` scheduled_plans.user_id = lookml_dashboards.folder.creator_id ```  ``` scheduled_plans.user.id = lookml_dashboards.space.creator_id ```  ``` scheduled_plans.user_id = lookml_dashboards.space.creator_id ```  ``` scheduled_plans.user.id = lookml_dashboards.user_id ```  ``` scheduled_plans.user_id = lookml_dashboards.user_id ``` |
| [queries](#queries) | ``` scheduled_plans.query_id = queries.id ``` |
| [connections](#connections) | ``` scheduled_plans.user.id = connections.user_id ```  ``` scheduled_plans.user_id = connections.user_id ``` |
| [user\_login\_lockouts](#user-login-lockouts) | ``` scheduled_plans.user.id = user_login_lockouts.user_id ```  ``` scheduled_plans.user_id = user_login_lockouts.user_id ``` |
| [users](#users) | ``` scheduled_plans.user.id = users.id ```  ``` scheduled_plans.user_id = users.id ``` |

scheduled\_plans table schema

|  |
| --- |
| **color\_theme**  STRING |
| **created\_at**  DATE-TIME |
| **crontab**  STRING |
| **dashboard\_filters**  STRING |
| **dashboard\_id**  STRING |
| **datagroup**  STRING |
| **embed**  BOOLEAN |
| **enabled**  BOOLEAN |
| **filters\_string**  STRING |
| **id**  STRING |
| **include\_links**  BOOLEAN |
| **last\_run\_at**  DATE-TIME |
| **long\_tables**  BOOLEAN |
| **look\_id**  STRING |
| **lookml\_dashboard\_id**  STRING |
| **name**  STRING |
| **next\_run\_at**  DATE-TIME |
| **pdf\_landscape**  BOOLEAN |
| **pdf\_paper\_size**  STRING |
| **query\_id**  STRING |
| **require\_change**  BOOLEAN |
| **require\_no\_results**  BOOLEAN |
| **require\_results**  BOOLEAN |
| **run\_as\_recipient**  BOOLEAN |
| **run\_once**  BOOLEAN |
| **scheduled\_plan\_destination**  ARRAY This is a nested data structure:   - address: STRING - apply\_formatting: BOOLEAN - apply\_vis: BOOLEAN - format: STRING - id: STRING - looker\_recipient: BOOLEAN - message: STRING - parameters: STRING - scheduled\_plan\_id: STRING - secret\_parameters: STRING - type: STRING |
| **send\_all\_results**  BOOLEAN |
| **timezone**  STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |
| **user**  OBJECT This is a nested data structure:   - avatar\_url: STRING - display\_name: STRING - first\_name: STRING - id: STRING - last\_name: STRING - url: STRING |
| **user\_id**  STRING |

### themes

The `themes` table contains info about the themes in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/theme#get_all_themes "Opens in new tab: Looker API method") |

themes table foreign keys

| Join themes with | on |
| --- | --- |
| [color\_collections](#color-collections) | ``` themes.settings.color_collection_id = color_collections.id ``` |

themes table schema

|  |
| --- |
| **begin\_at**  DATE-TIME |
| **end\_at**  DATE-TIME |
| **id**  STRING |
| **name**  STRING |
| **settings**  OBJECT This is a nested data structure:   - background\_color: STRING - base\_font\_size: STRING - color\_collection\_id: STRING - font\_color: STRING - font\_family: STRING - font\_source: STRING - info\_button\_color: STRING - primary\_button\_color: STRING - show\_filters\_bar: BOOLEAN - show\_title: BOOLEAN - text\_tile\_text\_color: STRING - tile\_background\_color: STRING - tile\_text\_color: STRING - title\_color: STRING - warn\_button\_color: STRING |

### user\_attribute\_group\_values

The `user_attribute_group_values` table contains info about the values of user attributes defined by user groups in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user-attribute#get_user_attribute_group_values "Opens in new tab: Looker API method") |

user\_attribute\_group\_values table foreign keys

| Join user\_attribute\_group\_values with | on |
| --- | --- |
| [content\_metadata\_access](#content-metadata-access) | ``` user_attribute_group_values.group_id = content_metadata_access.group_id ``` |
| [content\_views](#content-views) | ``` user_attribute_group_values.group_id = content_views.group_id ``` |
| [groups](#groups) | ``` user_attribute_group_values.group_id = groups.id ``` |
| [groups\_in\_group](#groups-in-group) | ``` user_attribute_group_values.group_id = groups_in_group.id ```  ``` user_attribute_group_values.group_id = groups_in_group.parent_group_id ``` |
| [users](#users) | ``` user_attribute_group_values.group_id = users.group_ids ``` |
| [user\_attributes](#user-attributes) | ``` user_attribute_group_values.user_attribute_id = user_attributes.id ``` |

user\_attribute\_group\_values table schema

|  |
| --- |
| **group\_id**  STRING |
| **id**  STRING |
| **rank**  INTEGER |
| **user\_attribute\_id**  STRING |
| **value**  STRING |
| **value\_is\_hidden**  BOOLEAN |

### user\_attribute\_values

The `user_attribute_values` table contains info about the values for user attributes defined in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | user\_attribute\_id  user\_id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user#get_user_attribute_values "Opens in new tab: Looker API method") |

user\_attribute\_values table schema

|  |
| --- |
| **hidden\_value\_domain\_whitelist**  STRING |
| **label**  STRING |
| **name**  STRING |
| **rank**  INTEGER |
| **source**  STRING |
| **user\_attribute\_id**  STRING |
| **user\_can\_edit**  BOOLEAN |
| **user\_id**  STRING |
| **value**  STRING |
| **value\_is\_hidden**  BOOLEAN |

### user\_attributes

The `user_attributes` table contains info about user attributes in your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user-attribute#get_all_user_attributes "Opens in new tab: Looker API method") |

user\_attributes table foreign keys

| Join user\_attributes with | on |
| --- | --- |
| [user\_attribute\_group\_values](#user-attribute-group-values) | ``` user_attributes.id = user_attribute_group_values.user_attribute_id ``` |

user\_attributes table schema

|  |
| --- |
| **default\_value**  STRING |
| **hidden\_value\_domain\_whitelist**  STRING |
| **id**  STRING |
| **is\_permanent**  BOOLEAN |
| **is\_system**  BOOLEAN |
| **label**  STRING |
| **name**  STRING |
| **type**  STRING |
| **user\_can\_edit**  BOOLEAN |
| **user\_can\_view**  BOOLEAN |
| **value\_is\_hidden**  BOOLEAN |

### user\_login\_lockouts

The `user_login_lockouts` table contains info about lockouts for user logins associated with your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | key |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/auth#get_all_user_login_lockouts "Opens in new tab: Looker API method") |

user\_login\_lockouts table foreign keys

| Join user\_login\_lockouts with | on |
| --- | --- |
| [connections](#connections) | ``` user_login_lockouts.user_id = connections.user_id ``` |
| [content\_favorites](#content-favorites) | ``` user_login_lockouts.user_id = content_favorites.dashboard.folder.creator_id ```  ``` user_login_lockouts.user_id = content_favorites.dashboard.space.creator_id ```  ``` user_login_lockouts.user_id = content_favorites.user_id ``` |
| [content\_views](#content-views) | ``` user_login_lockouts.user_id = content_views.user_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` user_login_lockouts.user_id = dashboard_elements.look.deleter_id ```  ``` user_login_lockouts.user_id = dashboard_elements.look.folder.creator_id ```  ``` user_login_lockouts.user_id = dashboard_elements.look.last_updater_id ```  ``` user_login_lockouts.user_id = dashboard_elements.look.space.creator_id ```  ``` user_login_lockouts.user_id = dashboard_elements.look.user.id ```  ``` user_login_lockouts.user_id = dashboard_elements.look.user_id ``` |
| [dashboards](#dashboards) | ``` user_login_lockouts.user_id = dashboards.space.creator_id ```  ``` user_login_lockouts.user_id = dashboards.user_id ``` |
| [folders](#folders) | ``` user_login_lockouts.user_id = folders.creator_id ```  ``` user_login_lockouts.user_id = folders.dashboards.user_id ```  ``` user_login_lockouts.user_id = folders.dashboards.folder.creator_id ```  ``` user_login_lockouts.user_id = folders.dashboards.space.creator_id ```  ``` user_login_lockouts.user_id = folders.looks.deleter_id ```  ``` user_login_lockouts.user_id = folders.looks.last_updater_id ```  ``` user_login_lockouts.user_id = folders.looks.user.id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` user_login_lockouts.user_id = lookml_dashboards.folder.creator_id ```  ``` user_login_lockouts.user_id = lookml_dashboards.space.creator_id ```  ``` user_login_lockouts.user_id = lookml_dashboards.user_id ``` |
| [looks](#looks) | ``` user_login_lockouts.user_id = looks.deleter_id ```  ``` user_login_lockouts.user_id = looks.folder.creator_id ```  ``` user_login_lockouts.user_id = looks.user.id ```  ``` user_login_lockouts.user_id = looks.user_id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` user_login_lockouts.user_id = scheduled_plans.user.id ```  ``` user_login_lockouts.user_id = scheduled_plans.user_id ``` |
| [users](#users) | ``` user_login_lockouts.user_id = users.id ``` |

user\_login\_lockouts table schema

|  |
| --- |
| **auth\_type**  STRING |
| **email**  STRING |
| **fail\_count**  INTEGER |
| **full\_name**  STRING |
| **ip**  STRING |
| **key**  STRING |
| **lockout\_at**  DATE-TIME |
| **remote\_id**  STRING |
| **user\_id**  STRING |

### user\_sessions

The `user_sessions` table contains info about user web login sessions associated with your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user#get_all_web_login_sessions "Opens in new tab: Looker API method") |

user\_sessions table foreign keys

| Join user\_sessions with | on |
| --- | --- |
| [users](#users) | ``` user_sessions.id = users.sessions.id ``` |

user\_sessions table schema

|  |
| --- |
| **browser**  STRING |
| **city**  STRING |
| **country**  STRING |
| **created\_at**  STRING |
| **credentials\_type**  STRING |
| **expires\_at**  STRING |
| **extended\_at**  STRING |
| **extended\_count**  INTEGER |
| **id**  STRING |
| **ip\_address**  STRING |
| **operating\_system**  STRING |
| **state**  STRING |
| **sudo\_user\_id**  STRING |
| **url**  STRING |

### users

The `users` table contains info about users associated with your Looker account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user#get_all_users "Opens in new tab: Looker API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [content\_favorites](#content-favorites) | ``` users.home_folder_id = content_favorites.dashboard.folder.id ```  ``` users.personal_folder_id = content_favorites.dashboard.folder.id ```  ``` users.home_folder_id = content_favorites.dashboard.folder.parent_id ```  ``` users.personal_folder_id = content_favorites.dashboard.folder.parent_id ```  ``` users.home_space_id = content_favorites.dashboard.space.id ```  ``` users.personal_space_id = content_favorites.dashboard.space.id ```  ``` users.home_space_id = content_favorites.dashboard.space.parent_id ```  ``` users.personal_space_id = content_favorites.dashboard.space.parent_id ```  ``` users.id = content_favorites.dashboard.folder.creator_id ```  ``` users.id = content_favorites.dashboard.space.creator_id ```  ``` users.id = content_favorites.user_id ``` |
| [dashboard\_elements](#dashboard-elements) | ``` users.home_folder_id = dashboard_elements.look.folder.id ```  ``` users.personal_folder_id = dashboard_elements.look.folder.id ```  ``` users.home_folder_id = dashboard_elements.look.folder.parent_id ```  ``` users.personal_folder_id = dashboard_elements.look.folder.parent_id ```  ``` users.home_folder_id = dashboard_elements.look.folder_id ```  ``` users.personal_folder_id = dashboard_elements.look.folder_id ```  ``` users.home_space_id = dashboard_elements.look.space.id ```  ``` users.personal_space_id = dashboard_elements.look.space.id ```  ``` users.home_space_id = dashboard_elements.look.space.parent_id ```  ``` users.personal_space_id = dashboard_elements.look.space.parent_id ```  ``` users.id = dashboard_elements.look.deleter_id ```  ``` users.id = dashboard_elements.look.folder.creator_id ```  ``` users.id = dashboard_elements.look.last_updater_id ```  ``` users.id = dashboard_elements.look.space.creator_id ```  ``` users.id = dashboard_elements.look.user.id ```  ``` users.id = dashboard_elements.look.user_id ``` |
| [dashboards](#dashboards) | ``` users.home_folder_id = dashboards.folder.id ```  ``` users.personal_folder_id = dashboards.folder.id ```  ``` users.home_folder_id = dashboards.folder.parent_id ```  ``` users.personal_folder_id = dashboards.folder.parent_id ```  ``` users.home_space_id = dashboards.space.id ```  ``` users.personal_space_id = dashboards.space.id ```  ``` users.home_space_id = dashboards.space.parent_id ```  ``` users.personal_space_id = dashboards.space.parent_id ```  ``` users.id = dashboards.space.creator_id ```  ``` users.id = dashboards.user_id ``` |
| [folders](#folders) | ``` users.home_folder_id = folders.id ```  ``` users.personal_folder_id = folders.id ```  ``` users.home_folder_id = folders.dashboards.folder.id ```  ``` users.personal_folder_id = folders.dashboards.folder.id ```  ``` users.home_folder_id = folders.dashboards.folder.parent_id ```  ``` users.personal_folder_id = folders.dashboards.folder.parent_id ```  ``` users.home_folder_id = folders.looks.folder.id ```  ``` users.personal_folder_id = folders.looks.folder.id ```  ``` users.home_folder_id = folders.looks.folder.parent_id ```  ``` users.personal_folder_id = folders.looks.folder.parent_id ```  ``` users.home_folder_id = folders.parent_id ```  ``` users.personal_folder_id = folders.parent_id ```  ``` users.home_space_id = folders.dashboards.space.id ```  ``` users.personal_space_id = folders.dashboards.space.id ```  ``` users.home_space_id = folders.dashboards.space.parent_id ```  ``` users.personal_space_id = folders.dashboards.space.parent_id ```  ``` users.home_space_id = folders.looks.space.id ```  ``` users.personal_space_id = folders.looks.space.id ```  ``` users.home_space_id = folders.looks.space.parent_id ```  ``` users.personal_space_id = folders.looks.space.parent_id ```  ``` users.home_space_id = folders.looks.space_id ```  ``` users.personal_space_id = folders.looks.space_id ```  ``` users.id = folders.creator_id ```  ``` users.id = folders.dashboards.user_id ```  ``` users.id = folders.dashboards.folder.creator_id ```  ``` users.id = folders.dashboards.space.creator_id ```  ``` users.id = folders.looks.deleter_id ```  ``` users.id = folders.looks.last_updater_id ```  ``` users.id = folders.looks.user.id ``` |
| [lookml\_dashboards](#lookml-dashboards) | ``` users.home_folder_id = lookml_dashboards.folder.id ```  ``` users.personal_folder_id = lookml_dashboards.folder.id ```  ``` users.home_folder_id = lookml_dashboards.folder.parent_id ```  ``` users.personal_folder_id = lookml_dashboards.folder.parent_id ```  ``` users.home_space_id = lookml_dashboards.space.id ```  ``` users.personal_space_id = lookml_dashboards.space.id ```  ``` users.home_space_id = lookml_dashboards.space.parent_id ```  ``` users.personal_space_id = lookml_dashboards.space.parent_id ```  ``` users.id = lookml_dashboards.folder.creator_id ```  ``` users.id = lookml_dashboards.space.creator_id ```  ``` users.id = lookml_dashboards.user_id ``` |
| [looks](#looks) | ``` users.home_folder_id = looks.folder.id ```  ``` users.personal_folder_id = looks.folder.id ```  ``` users.home_folder_id = looks.folder_id ```  ``` users.personal_folder_id = looks.folder_id ```  ``` users.home_folder_id = looks.folder.parent_id ```  ``` users.personal_folder_id = looks.folder.parent_id ```  ``` users.home_space_id = looks.space.id ```  ``` users.personal_space_id = looks.space.id ```  ``` users.home_space_id = looks.space.parent_id ```  ``` users.personal_space_id = looks.space.parent_id ```  ``` users.home_space_id = looks.space_id ```  ``` users.personal_space_id = looks.space_id ```  ``` users.id = looks.deleter_id ```  ``` users.id = looks.folder.creator_id ```  ``` users.id = looks.user.id ```  ``` users.id = looks.user_id ``` |
| [content\_metadata\_access](#content-metadata-access) | ``` users.group_ids = content_metadata_access.group_id ``` |
| [content\_views](#content-views) | ``` users.group_ids = content_views.group_id ```  ``` users.id = content_views.user_id ``` |
| [groups](#groups) | ``` users.group_ids = groups.id ``` |
| [groups\_in\_group](#groups-in-group) | ``` users.group_ids = groups_in_group.id ```  ``` users.group_ids = groups_in_group.parent_group_id ``` |
| [user\_attribute\_group\_values](#user-attribute-group-values) | ``` users.group_ids = user_attribute_group_values.group_id ``` |
| [versions](#versions) | ``` users.looker_versions = versions.looker_release_version ```  ``` users.looker_versions = versions.current_version.full_version ```  ``` users.looker_versions = versions.supported_versions.full_version ``` |
| [role\_groups](#role-groups) | ``` users.role_ids = role_groups.role_id ``` |
| [roles](#roles) | ``` users.role_ids = roles.id ``` |
| [content\_metadata](#content-metadata) | ``` users.home_space_id = content_metadata.space_id ```  ``` users.personal_space_id = content_metadata.space_id ``` |
| [user\_sessions](#user-sessions) | ``` users.sessions.id = user_sessions.id ``` |
| [connections](#connections) | ``` users.id = connections.user_id ``` |
| [scheduled\_plans](#scheduled-plans) | ``` users.id = scheduled_plans.user.id ```  ``` users.id = scheduled_plans.user_id ``` |
| [user\_login\_lockouts](#user-login-lockouts) | ``` users.id = user_login_lockouts.user_id ``` |

users table schema

|  |
| --- |
| **avatar\_url**  STRING |
| **avatar\_url\_without\_sizing**  STRING |
| **credentials\_api3**  ARRAY This is a nested data structure:   - client\_id: STRING - created\_at: STRING - id: STRING - is\_disabled: BOOLEAN - type: STRING - url: STRING |
| **credentials\_email**  OBJECT This is a nested data structure:   - created\_at: STRING - email: STRING - forced\_password\_reset\_at\_next\_login: BOOLEAN - is\_disabled: BOOLEAN - logged\_in\_at: STRING - password\_reset\_url: STRING - type: STRING - url: STRING - user\_url: STRING |
| **credentials\_embed**  ARRAY This is a nested data structure:   - created\_at: STRING - external\_group\_id: STRING - external\_user\_id: STRING - id: STRING - is\_disabled: BOOLEAN - logged\_in\_at: STRING - type: STRING - url: STRING |
| **credentials\_google**  OBJECT This is a nested data structure:   - created\_at: STRING - domain: STRING - email: STRING - google\_user\_id: STRING - is\_disabled: BOOLEAN - logged\_in\_at: STRING - type: STRING - url: STRING |
| **credentials\_ldap**  OBJECT This is a nested data structure:   - created\_at: STRING - email: STRING - is\_disabled: BOOLEAN - ldap\_dn: STRING - ldap\_id: STRING - logged\_in\_at: STRING - type: STRING - url: STRING |
| **credentials\_looker\_openid**  OBJECT This is a nested data structure:   - created\_at: STRING - email: STRING - is\_disabled: BOOLEAN - logged\_in\_at: STRING - logged\_in\_ip: STRING - type: STRING - url: STRING - user\_url: STRING |
| **credentials\_oidc**  OBJECT This is a nested data structure:   - created\_at: STRING - email: STRING - is\_disabled: BOOLEAN - logged\_in\_at: STRING - oidc\_user\_id: STRING - type: STRING - url: STRING |
| **credentials\_saml**  OBJECT This is a nested data structure:   - created\_at: STRING - email: STRING - is\_disabled: BOOLEAN - logged\_in\_at: STRING - saml\_user\_id: STRING - type: STRING - url: STRING |
| **credentials\_totp**  OBJECT This is a nested data structure:   - created\_at: STRING - is\_disabled: BOOLEAN - type: STRING - url: STRING - verified: BOOLEAN |
| **display\_name**  STRING |
| **email**  STRING |
| **embed\_group\_space\_id**  STRING |
| **first\_name**  STRING |
| **group\_ids**  ARRAY This is a nested data structure. |
| **home\_folder\_id**  STRING |
| **home\_space\_id**  STRING |
| **id**  STRING |
| **is\_disabled**  BOOLEAN |
| **last\_name**  STRING |
| **locale**  STRING |
| **looker\_versions**  ARRAY This is a nested data structure. |
| **models\_dir\_validated**  BOOLEAN |
| **personal\_folder\_id**  STRING |
| **personal\_space\_id**  STRING |
| **presumed\_looker\_employee**  BOOLEAN |
| **role\_ids**  ARRAY This is a nested data structure. |
| **roles\_externally\_managed**  BOOLEAN |
| **sessions**  ARRAY This is a nested data structure:   - browser: STRING - city: STRING - country: STRING - created\_at: STRING - credentials\_type: STRING - expires\_at: STRING - extended\_at: STRING - extended\_count: INTEGER - id: STRING - ip\_address: STRING - operating\_system: STRING - state: STRING - sudo\_user\_id: STRING - url: STRING |
| **ui\_state**  OBJECT This is a nested data structure. |
| **url**  STRING |
| **verified\_looker\_employee**  BOOLEAN |

### versions

The `versions` table contains info about the API versions supported by your Looker instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | looker\_release\_version |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/config#get_apiversion "Opens in new tab: Looker API method") |

versions table foreign keys

| Join versions with | on |
| --- | --- |
| [users](#users) | ``` versions.looker_release_version = users.looker_versions ```  ``` versions.current_version.full_version = users.looker_versions ```  ``` versions.supported_versions.full_version = users.looker_versions ``` |

versions table schema

|  |
| --- |
| **current\_version**  OBJECT This is a nested data structure:   - full\_version: STRING - status: STRING - swagger\_url: STRING - version: STRING |
| **looker\_release\_version**  STRING |
| **supported\_versions**  ARRAY This is a nested data structure:   - full\_version: STRING - status: STRING - swagger\_url: STRING - version: STRING |

### workspaces

The `workspaces` table contains info about the workspaces available to the user who authorized the Looker integration in Stitch.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Looker API method](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/workspace#get_all_workspaces "Opens in new tab: Looker API method") |

workspaces table foreign keys

| Join workspaces with | on |
| --- | --- |
| [git\_branches](#git-branches) | ``` workspaces.projects.id = git_branches.project_id ``` |
| [project\_files](#project-files) | ``` workspaces.projects.id = project_files.project_id ``` |
| [projects](#projects) | ``` workspaces.projects.id = projects.id ``` |

workspaces table schema

|  |
| --- |
| **id**  STRING |
| **projects**  ARRAY This is a nested data structure:   - allow\_warnings: BOOLEAN - deploy\_secret: STRING - folders\_enabled: BOOLEAN - git\_password: STRING - git\_password\_user\_attribute: STRING - git\_remote\_url: STRING - git\_service\_name: STRING - git\_username: STRING - git\_username\_user\_attribute: STRING - id: STRING - is\_example: BOOLEAN - name: STRING - pull\_request\_mode: STRING - unset\_deploy\_secret: BOOLEAN - uses\_git: BOOLEAN - validation\_required: BOOLEAN |
