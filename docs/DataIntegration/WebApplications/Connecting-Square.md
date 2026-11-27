---
title: "Square"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Square.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Square

Square is a large business technology platform serving all kinds of businesses. The Square operating system allows business owners to sell anywhere.

Square integration replicates data using the [Square API version 2023-06-08](https://developer.squareup.com/reference/square).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You must have administrator permissions for your Square Developer account.

Connections from Qlik Talend Cloud to the Square Sandbox instance are not currently supported.

To obtain your application ID and application secret:

1. Log into your [Square Developer](https://app.squareup.com/signup?country_code=fr&v=developers) account.
2. Click + to create an app.
3. Enter a name for your app.
4. In the left navigation bar, select OAuth, and then select Production.
5. Set Production Redirect URL to https://connector.qlik.com/auth/oauth/v3.htm.
6. On the OAuth > Production page, copy your application ID and application secret into a secured file.

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
| Application ID | Application ID. |
| Application Secret | Application secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### bank\_accounts

The `bank_accounts` contains information about a merchant’s bank account in Square.

**Note**: This table can’t be replicated if the **Connect to a sandbox environment** box is checked in the [integration’s settings](#add-stitch-data-source) due to limits imposed by Square.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/bank-accounts-api)  [Square API method](https://developer.squareup.com/reference/square/bank-accounts-api/get-bank-account "Opens in new tab: Square API method") |

bank\_accounts table foreign keys

| Join bank\_accounts with | on |
| --- | --- |
| [categories](#categories) | ``` bank_accounts.id = categories.absent_at_location_ids ``` |
| [discounts](#discounts) | ``` bank_accounts.id = discounts.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` bank_accounts.id = team_members.assigned_locations.location_ids ``` |
| [inventories](#inventories) | ``` bank_accounts.id = inventories.location_id ``` |
| [items](#items) | ``` bank_accounts.id = items.absent_at_location_ids ```  ``` bank_accounts.id = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` bank_accounts.id = items.item_data.variations.present_at_location_ids ```  ``` bank_accounts.id = items.present_at_location_ids ``` |
| [locations](#locations) | ``` bank_accounts.id = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` bank_accounts.id = modifier_lists.absent_at_location_ids ``` |
| [orders](#orders) | ``` bank_accounts.id = orders.id ```  ``` bank_accounts.id = orders.refunds.id ```  ``` bank_accounts.id = orders.tenders.id ``` |
| [payments](#payments) | ``` bank_accounts.id = payments.id ``` |
| [refunds](#refunds) | ``` bank_accounts.id = refunds.id ``` |
| [shifts](#shifts) | ``` bank_accounts.id = shifts.id ``` |
| [taxes](#taxes) | ``` bank_accounts.id = taxes.absent_at_location_ids ``` |

bank\_accounts table schema

|  |
| --- |
| **account\_number\_suffix**  STRING |
| **account\_type**  STRING |
| **bank\_name**  STRING |
| **country**  STRING |
| **creditable**  BOOLEAN |
| **currency**  STRING |
| **debit\_mandate\_reference\_id**  STRING |
| **debitable**  BOOLEAN |
| **holder\_name**  STRING |
| **id**  STRING |
| **location\_id**  STRING |
| **primary\_bank\_identification\_number**  STRING |
| **reference\_id**  STRING |
| **secondary\_bank\_identification\_number**  STRING |
| **status**  STRING |
| **version**  INTEGER |

### cash\_drawer\_shifts

The `cash_drawer_shifts` table contains infomration about cash transactions in Square.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/cash-drawers-api/retrieve-cash-drawer-shift#response-body)  [Square API method](https://developer.squareup.com/reference/square/cash-drawers-api/retrieve-cash-drawer-shift "Opens in new tab: Square API method") |

cash\_drawer\_shifts table schema

|  |
| --- |
| **closed\_at**  DATE-TIME |
| **closed\_cash\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **ended\_at**  DATE-TIME |
| **expected\_cash\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **id**  STRING |
| **location\_id**  STRING |
| **opened\_at**  DATE-TIME |
| **opened\_cash\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **state**  STRING |
| **updated\_at**  DATE-TIME |

### categories

The `categories` table contains information about item categories for a given location in Square.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/catalog-api/v1-list-categories)  [Square API method](https://developer.squareup.com/reference/square/catalog-api/list-catalog "Opens in new tab: Square API method") |

categories table foreign keys

| Join categories with | on |
| --- | --- |
| [items](#items) | ``` categories.id = items.item_data.category_id ```  ``` categories.absent_at_location_ids = items.absent_at_location_ids ```  ``` categories.absent_at_location_ids = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` categories.absent_at_location_ids = items.item_data.variations.present_at_location_ids ```  ``` categories.absent_at_location_ids = items.present_at_location_ids ``` |
| [bank\_accounts](#bank-accounts) | ``` categories.absent_at_location_ids = bank_accounts.id ``` |
| [discounts](#discounts) | ``` categories.absent_at_location_ids = discounts.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` categories.absent_at_location_ids = team_members.assigned_locations.location_ids ``` |
| [inventories](#inventories) | ``` categories.absent_at_location_ids = inventories.location_id ``` |
| [locations](#locations) | ``` categories.absent_at_location_ids = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` categories.absent_at_location_ids = modifier_lists.absent_at_location_ids ``` |
| [orders](#orders) | ``` categories.absent_at_location_ids = orders.id ```  ``` categories.absent_at_location_ids = orders.refunds.id ```  ``` categories.absent_at_location_ids = orders.tenders.id ``` |
| [payments](#payments) | ``` categories.absent_at_location_ids = payments.id ``` |
| [refunds](#refunds) | ``` categories.absent_at_location_ids = refunds.id ``` |
| [shifts](#shifts) | ``` categories.absent_at_location_ids = shifts.id ``` |
| [taxes](#taxes) | ``` categories.absent_at_location_ids = taxes.absent_at_location_ids ``` |

categories table schema

|  |
| --- |
| **absent\_at\_location\_ids**  ARRAY |
| **category\_data**  OBJECT This is a nested data structure:   - name: STRING |
| **id**  STRING |
| **is\_deleted**  BOOLEAN |
| **present\_at\_all\_locations**  BOOLEAN |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **version**  INTEGER |

### customers

The `customers` contains information about customer profiles associated with your Square account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | updated\_at |
| **Useful links** | [Square API method](https://developer.squareup.com/reference/square/customers-api/list-customers "Opens in new tab: Square API method") |

customers table schema

|  |
| --- |
| **address**  OBJECT This is a nested data structure:   - address\_line\_1: STRING - address\_line\_2: STRING - address\_line\_3: STRING - administrative\_district\_level\_1: STRING - administrative\_district\_level\_2: STRING - administrative\_district\_level\_3: STRING - country: STRING - first\_name: STRING - last\_name: STRING - locality: STRING - postal\_code: STRING - sublocality: STRING - sublocality\_2: STRING - sublocality\_3: STRING |
| **birthday**  DATE-TIME  STRING |
| **company\_name**  STRING |
| **created\_at**  DATE-TIME |
| **creation\_source**  STRING |
| **email\_address**  STRING |
| **family\_name**  STRING |
| **given\_name**  STRING |
| **group\_ids**  ARRAY |
| **id**  STRING |
| **nickname**  STRING |
| **note**  STRING |
| **phone\_number**  STRING |
| **preferences**  OBJECT This is a nested data structure:   - email\_unsubscribed: BOOLEAN |
| **reference\_id**  STRING |
| **segment\_ids**  ARRAY |
| **tax\_ids**  OBJECT This is a nested data structure:   - eu\_vat: STRING |
| **updated\_at**  DATE-TIME |
| **version**  INTEGER |

### discounts

The `discounts` table contains information about discounts for a given location in Square.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Square API method](https://developer.squareup.com/reference/square/catalog-api/list-catalog "Opens in new tab: Square API method") |

discounts table foreign keys

| Join discounts with | on |
| --- | --- |
| [bank\_accounts](#bank-accounts) | ``` discounts.absent_at_location_ids = bank_accounts.id ``` |
| [categories](#categories) | ``` discounts.absent_at_location_ids = categories.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` discounts.absent_at_location_ids = team_members.assigned_locations.location_ids ``` |
| [inventories](#inventories) | ``` discounts.absent_at_location_ids = inventories.location_id ``` |
| [items](#items) | ``` discounts.absent_at_location_ids = items.absent_at_location_ids ```  ``` discounts.absent_at_location_ids = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` discounts.absent_at_location_ids = items.item_data.variations.present_at_location_ids ```  ``` discounts.absent_at_location_ids = items.present_at_location_ids ``` |
| [locations](#locations) | ``` discounts.absent_at_location_ids = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` discounts.absent_at_location_ids = modifier_lists.absent_at_location_ids ``` |
| [orders](#orders) | ``` discounts.absent_at_location_ids = orders.id ```  ``` discounts.absent_at_location_ids = orders.refunds.id ```  ``` discounts.absent_at_location_ids = orders.tenders.id ``` |
| [payments](#payments) | ``` discounts.absent_at_location_ids = payments.id ``` |
| [refunds](#refunds) | ``` discounts.absent_at_location_ids = refunds.id ``` |
| [shifts](#shifts) | ``` discounts.absent_at_location_ids = shifts.id ``` |
| [taxes](#taxes) | ``` discounts.absent_at_location_ids = taxes.absent_at_location_ids ``` |

discounts table schema

|  |
| --- |
| **absent\_at\_location\_ids**  ARRAY |
| **discount\_data**  OBJECT This is a nested data structure:   - amount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - application\_method: STRING - discount\_type: STRING - label\_color: STRING - modify\_tax\_basis: STRING - name: STRING - percentage: STRING - pin\_required: BOOLEAN |
| **id**  STRING |
| **is\_deleted**  BOOLEAN |
| **present\_at\_all\_locations**  BOOLEAN |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **version**  INTEGER |

### inventories

The `inventories` table contains info about the current calculated stock count for a Square location.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Loading Behavior** | Append-Only |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/inventory-api)  [Square API method](https://developer.squareup.com/reference/square/inventory-api/retrieve-inventory-count "Opens in new tab: Square API method") |

inventories table foreign keys

| Join inventories with | on |
| --- | --- |
| [bank\_accounts](#bank-accounts) | ``` inventories.location_id = bank_accounts.id ``` |
| [categories](#categories) | ``` inventories.location_id = categories.absent_at_location_ids ``` |
| [discounts](#discounts) | ``` inventories.location_id = discounts.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` inventories.location_id = team_members.assigned_locations.location_ids ``` |
| [items](#items) | ``` inventories.location_id = items.absent_at_location_ids ```  ``` inventories.location_id = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` inventories.location_id = items.item_data.variations.present_at_location_ids ```  ``` inventories.location_id = items.present_at_location_ids ``` |
| [locations](#locations) | ``` inventories.location_id = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` inventories.location_id = modifier_lists.absent_at_location_ids ``` |
| [orders](#orders) | ``` inventories.location_id = orders.id ```  ``` inventories.location_id = orders.refunds.id ```  ``` inventories.location_id = orders.tenders.id ``` |
| [payments](#payments) | ``` inventories.location_id = payments.id ``` |
| [refunds](#refunds) | ``` inventories.location_id = refunds.id ``` |
| [shifts](#shifts) | ``` inventories.location_id = shifts.id ``` |
| [taxes](#taxes) | ``` inventories.location_id = taxes.absent_at_location_ids ``` |

inventories table schema

|  |
| --- |
| **calculated\_at**  DATE-TIME |
| **catalog\_object\_id**  STRING |
| **catalog\_object\_type**  STRING |
| **location\_id**  STRING |
| **quantity**  STRING |
| **state**  STRING |

### items

The `items` table contains information about items for a given location in Square.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/catalog-api)  [Square API method](https://developer.squareup.com/reference/square/catalog-api/list-catalog "Opens in new tab: Square API method") |

items table foreign keys

| Join items with | on |
| --- | --- |
| [categories](#categories) | ``` items.item_data.category_id = categories.id ```  ``` items.absent_at_location_ids = categories.absent_at_location_ids ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = categories.absent_at_location_ids ```  ``` items.item_data.variations.present_at_location_ids = categories.absent_at_location_ids ```  ``` items.present_at_location_ids = categories.absent_at_location_ids ``` |
| [bank\_accounts](#bank-accounts) | ``` items.absent_at_location_ids = bank_accounts.id ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = bank_accounts.id ```  ``` items.item_data.variations.present_at_location_ids = bank_accounts.id ```  ``` items.present_at_location_ids = bank_accounts.id ``` |
| [discounts](#discounts) | ``` items.absent_at_location_ids = discounts.absent_at_location_ids ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = discounts.absent_at_location_ids ```  ``` items.item_data.variations.present_at_location_ids = discounts.absent_at_location_ids ```  ``` items.present_at_location_ids = discounts.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` items.absent_at_location_ids = team_members.assigned_locations.location_ids ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = team_members.assigned_locations.location_ids ```  ``` items.item_data.variations.present_at_location_ids = team_members.assigned_locations.location_ids ```  ``` items.present_at_location_ids = team_members.assigned_locations.location_ids ``` |
| [inventories](#inventories) | ``` items.absent_at_location_ids = inventories.location_id ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = inventories.location_id ```  ``` items.item_data.variations.present_at_location_ids = inventories.location_id ```  ``` items.present_at_location_ids = inventories.location_id ``` |
| [locations](#locations) | ``` items.absent_at_location_ids = locations.id ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = locations.id ```  ``` items.item_data.variations.present_at_location_ids = locations.id ```  ``` items.present_at_location_ids = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` items.absent_at_location_ids = modifier_lists.absent_at_location_ids ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = modifier_lists.absent_at_location_ids ```  ``` items.item_data.variations.present_at_location_ids = modifier_lists.absent_at_location_ids ```  ``` items.present_at_location_ids = modifier_lists.absent_at_location_ids ```  ``` items.item_data.modifier_list_info.modifier_list_id = modifier_lists.id ```  ``` items.item_data.modifier_list_info.modifier_list_id = modifier_lists.modifier_list_data.modifiers.modifier_data.modifier_list_id ``` |
| [orders](#orders) | ``` items.absent_at_location_ids = orders.id ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = orders.id ```  ``` items.item_data.variations.present_at_location_ids = orders.id ```  ``` items.present_at_location_ids = orders.id ```  ``` items.absent_at_location_ids = orders.refunds.id ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = orders.refunds.id ```  ``` items.item_data.variations.present_at_location_ids = orders.refunds.id ```  ``` items.present_at_location_ids = orders.refunds.id ```  ``` items.absent_at_location_ids = orders.tenders.id ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = orders.tenders.id ```  ``` items.item_data.variations.present_at_location_ids = orders.tenders.id ```  ``` items.present_at_location_ids = orders.tenders.id ``` |
| [payments](#payments) | ``` items.absent_at_location_ids = payments.id ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = payments.id ```  ``` items.item_data.variations.present_at_location_ids = payments.id ```  ``` items.present_at_location_ids = payments.id ``` |
| [refunds](#refunds) | ``` items.absent_at_location_ids = refunds.id ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = refunds.id ```  ``` items.item_data.variations.present_at_location_ids = refunds.id ```  ``` items.present_at_location_ids = refunds.id ``` |
| [shifts](#shifts) | ``` items.absent_at_location_ids = shifts.id ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = shifts.id ```  ``` items.item_data.variations.present_at_location_ids = shifts.id ```  ``` items.present_at_location_ids = shifts.id ``` |
| [taxes](#taxes) | ``` items.absent_at_location_ids = taxes.absent_at_location_ids ```  ``` items.item_data.variations.item_variation_data.location_overrides.location_id = taxes.absent_at_location_ids ```  ``` items.item_data.variations.present_at_location_ids = taxes.absent_at_location_ids ```  ``` items.present_at_location_ids = taxes.absent_at_location_ids ```  ``` items.item_data.tax_ids = taxes.id ``` |

items table schema

|  |
| --- |
| **absent\_at\_location\_ids**  ARRAY |
| **id**  STRING |
| **is\_deleted**  BOOLEAN |
| **item\_data**  OBJECT This is a nested data structure:   - abbreviation: STRING - available\_electronically: BOOLEAN - available\_for\_pickup: BOOLEAN - available\_online: BOOLEAN - category\_id: STRING - description: STRING - item\_options: ARRAY, which is also a nested data structure.   - item\_option\_id: STRING - label\_color: STRING - legacy\_tax\_ids: ARRAY - modifier\_list\_info: ARRAY, which is also a nested data structure.   - enabled: BOOLEAN   - modifier\_list\_id: STRING - name: STRING - product\_type: STRING - skip\_modifier\_screen: BOOLEAN - tax\_ids: ARRAY - variations: ARRAY, which is also a nested data structure.   - id: STRING   - is\_deleted: BOOLEAN   - item\_variation\_data: OBJECT, which is also a nested data structure.     - inventory\_alert\_type: STRING     - item\_id: STRING     - location\_overrides: ARRAY, which is also a nested data structure.       - inventory\_alert\_threshold: INTEGER       - inventory\_alert\_type: STRING       - location\_id: STRING       - sold\_out: BOOLEAN       - track\_inventory: BOOLEAN     - name: STRING     - ordinal: INTEGER     - price\_money: OBJECT, which is also a nested data structure.       - amount: INTEGER       - currency: STRING     - pricing\_type: STRING     - sku: STRING     - track\_inventory: BOOLEAN     - user\_data: STRING   - present\_at\_all\_locations: BOOLEAN   - present\_at\_location\_ids: ARRAY   - type: STRING   - updated\_at: DATE-TIME   - version: INTEGER - visibility: STRING |
| **present\_at\_all\_locations**  BOOLEAN |
| **present\_at\_location\_ids**  ARRAY |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **version**  INTEGER |

### locations

The `locations` table contains information about all of your business locations in Square.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/locations-api)  [Square API method](https://developer.squareup.com/reference/square/locations-api/list-locations "Opens in new tab: Square API method") |

locations table foreign keys

| Join locations with | on |
| --- | --- |
| [bank\_accounts](#bank-accounts) | ``` locations.id = bank_accounts.id ``` |
| [categories](#categories) | ``` locations.id = categories.absent_at_location_ids ``` |
| [discounts](#discounts) | ``` locations.id = discounts.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` locations.id = team_members.assigned_locations.location_ids ``` |
| [inventories](#inventories) | ``` locations.id = inventories.location_id ``` |
| [items](#items) | ``` locations.id = items.absent_at_location_ids ```  ``` locations.id = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` locations.id = items.item_data.variations.present_at_location_ids ```  ``` locations.id = items.present_at_location_ids ``` |
| [modifier\_lists](#modifier-lists) | ``` locations.id = modifier_lists.absent_at_location_ids ``` |
| [orders](#orders) | ``` locations.id = orders.id ```  ``` locations.id = orders.refunds.id ```  ``` locations.id = orders.tenders.id ``` |
| [payments](#payments) | ``` locations.id = payments.id ``` |
| [refunds](#refunds) | ``` locations.id = refunds.id ``` |
| [shifts](#shifts) | ``` locations.id = shifts.id ``` |
| [taxes](#taxes) | ``` locations.id = taxes.absent_at_location_ids ``` |

locations table schema

|  |
| --- |
| **address**  OBJECT This is a nested data structure:   - address\_line\_1: STRING - address\_line\_2: STRING - address\_line\_3: STRING - administrative\_district\_level\_1: STRING - administrative\_district\_level\_2: STRING - administrative\_district\_level\_3: STRING - country: STRING - first\_name: STRING - last\_name: STRING - locality: STRING - postal\_code: STRING - sublocality: STRING - sublocality\_2: STRING - sublocality\_3: STRING |
| **business\_email**  STRING |
| **business\_hours**  OBJECT This is a nested data structure:   - periods: ARRAY, which is also a nested data structure.   - day\_of\_week: STRING   - end\_local\_time: STRING   - start\_local\_time: STRING |
| **business\_name**  STRING |
| **capabilities**  ARRAY |
| **coordinates**  OBJECT This is a nested data structure:   - latitude: NUMBER - longitude: NUMBER |
| **country**  STRING |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **description**  STRING |
| **facebook\_url**  STRING |
| **full\_format\_logo\_url**  STRING |
| **id**  STRING |
| **instagram\_username**  STRING |
| **language\_code**  STRING |
| **logo\_url**  STRING |
| **mcc**  STRING |
| **merchant\_id**  STRING |
| **name**  STRING |
| **phone\_number**  STRING |
| **pos\_background\_url**  STRING |
| **status**  STRING |
| **timezone**  STRING |
| **twitter\_username**  STRING |
| **type**  STRING |
| **website\_url**  STRING |

### modifier\_lists

The `modifier_lists` table contains information about modifier lists for a given location in Square.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/catalog-api/v1-list-modifier-lists)  [Square API method](https://developer.squareup.com/reference/square/catalog-api/list-catalog "Opens in new tab: Square API method") |

modifier\_lists table foreign keys

| Join modifier\_lists with | on |
| --- | --- |
| [bank\_accounts](#bank-accounts) | ``` modifier_lists.absent_at_location_ids = bank_accounts.id ``` |
| [categories](#categories) | ``` modifier_lists.absent_at_location_ids = categories.absent_at_location_ids ``` |
| [discounts](#discounts) | ``` modifier_lists.absent_at_location_ids = discounts.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` modifier_lists.absent_at_location_ids = team_members.assigned_locations.location_ids ``` |
| [inventories](#inventories) | ``` modifier_lists.absent_at_location_ids = inventories.location_id ``` |
| [items](#items) | ``` modifier_lists.absent_at_location_ids = items.absent_at_location_ids ```  ``` modifier_lists.absent_at_location_ids = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` modifier_lists.absent_at_location_ids = items.item_data.variations.present_at_location_ids ```  ``` modifier_lists.absent_at_location_ids = items.present_at_location_ids ```  ``` modifier_lists.id = items.item_data.modifier_list_info.modifier_list_id ```  ``` modifier_lists.modifier_list_data.modifiers.modifier_data.modifier_list_id = items.item_data.modifier_list_info.modifier_list_id ``` |
| [locations](#locations) | ``` modifier_lists.absent_at_location_ids = locations.id ``` |
| [orders](#orders) | ``` modifier_lists.absent_at_location_ids = orders.id ```  ``` modifier_lists.absent_at_location_ids = orders.refunds.id ```  ``` modifier_lists.absent_at_location_ids = orders.tenders.id ``` |
| [payments](#payments) | ``` modifier_lists.absent_at_location_ids = payments.id ``` |
| [refunds](#refunds) | ``` modifier_lists.absent_at_location_ids = refunds.id ``` |
| [shifts](#shifts) | ``` modifier_lists.absent_at_location_ids = shifts.id ``` |
| [taxes](#taxes) | ``` modifier_lists.absent_at_location_ids = taxes.absent_at_location_ids ``` |

modifier\_lists table schema

|  |
| --- |
| **absent\_at\_location\_ids**  ARRAY |
| **id**  STRING |
| **is\_deleted**  BOOLEAN |
| **modifier\_list\_data**  OBJECT This is a nested data structure:   - modifiers: ARRAY, which is also a nested data structure.   - id: STRING   - is\_deleted: BOOLEAN   - modifier\_data: OBJECT, which is also a nested data structure.     - modifier\_list\_id: STRING     - name: STRING     - on\_by\_default: BOOLEAN     - ordinal: INTEGER     - price\_money: OBJECT, which is also a nested data structure.       - amount: INTEGER       - currency: STRING   - present\_at\_all\_locations: BOOLEAN   - type: STRING   - updated\_at: DATE-TIME   - version: INTEGER - name: STRING - ordinal: INTEGER - selection\_type: STRING |
| **present\_at\_all\_locations**  BOOLEAN |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **version**  INTEGER |

### orders

The `orders` table contains information about order updates in Square.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | updated\_at |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/orders-api)  [Square API method](https://developer.squareup.com/reference/square/orders-api/search-orders "Opens in new tab: Square API method") |

orders table foreign keys

| Join orders with | on |
| --- | --- |
| [bank\_accounts](#bank-accounts) | ``` orders.id = bank_accounts.id ```  ``` orders.refunds.id = bank_accounts.id ```  ``` orders.tenders.id = bank_accounts.id ``` |
| [categories](#categories) | ``` orders.id = categories.absent_at_location_ids ```  ``` orders.refunds.id = categories.absent_at_location_ids ```  ``` orders.tenders.id = categories.absent_at_location_ids ``` |
| [discounts](#discounts) | ``` orders.id = discounts.absent_at_location_ids ```  ``` orders.refunds.id = discounts.absent_at_location_ids ```  ``` orders.tenders.id = discounts.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` orders.id = team_members.assigned_locations.location_ids ```  ``` orders.refunds.id = team_members.assigned_locations.location_ids ```  ``` orders.tenders.id = team_members.assigned_locations.location_ids ``` |
| [inventories](#inventories) | ``` orders.id = inventories.location_id ```  ``` orders.refunds.id = inventories.location_id ```  ``` orders.tenders.id = inventories.location_id ``` |
| [items](#items) | ``` orders.id = items.absent_at_location_ids ```  ``` orders.refunds.id = items.absent_at_location_ids ```  ``` orders.tenders.id = items.absent_at_location_ids ```  ``` orders.id = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` orders.refunds.id = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` orders.tenders.id = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` orders.id = items.item_data.variations.present_at_location_ids ```  ``` orders.refunds.id = items.item_data.variations.present_at_location_ids ```  ``` orders.tenders.id = items.item_data.variations.present_at_location_ids ```  ``` orders.id = items.present_at_location_ids ```  ``` orders.refunds.id = items.present_at_location_ids ```  ``` orders.tenders.id = items.present_at_location_ids ``` |
| [locations](#locations) | ``` orders.id = locations.id ```  ``` orders.refunds.id = locations.id ```  ``` orders.tenders.id = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` orders.id = modifier_lists.absent_at_location_ids ```  ``` orders.refunds.id = modifier_lists.absent_at_location_ids ```  ``` orders.tenders.id = modifier_lists.absent_at_location_ids ``` |
| [payments](#payments) | ``` orders.id = payments.id ```  ``` orders.refunds.id = payments.id ```  ``` orders.tenders.id = payments.id ```  ``` orders.id = payments.order_id ```  ``` orders.returns.source_order_id = payments.order_id ```  ``` orders.refunds.id = payments.order_id ```  ``` orders.refunds.id = payments.refund_ids ``` |
| [refunds](#refunds) | ``` orders.id = refunds.id ```  ``` orders.refunds.id = refunds.id ```  ``` orders.tenders.id = refunds.id ```  ``` orders.id = refunds.order_id ```  ``` orders.returns.source_order_id = refunds.order_id ```  ``` orders.tenders.id = refunds.payment_id ``` |
| [shifts](#shifts) | ``` orders.id = shifts.id ```  ``` orders.refunds.id = shifts.id ```  ``` orders.tenders.id = shifts.id ``` |
| [taxes](#taxes) | ``` orders.id = taxes.absent_at_location_ids ```  ``` orders.refunds.id = taxes.absent_at_location_ids ```  ``` orders.tenders.id = taxes.absent_at_location_ids ``` |

orders table schema

|  |
| --- |
| **closed\_at**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **discounts**  ARRAY This is a nested data structure:   - amount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - applied\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - catalog\_object\_id: STRING - catalog\_version: INTEGER - name: STRING - percentage: STRING - pricing\_rule\_id: STRING - scope: STRING - type: STRING |
| **fulfillments**  ARRAY This is a nested data structure:   - pickup\_details: OBJECT, which is also a nested data structure.   - accepted\_at: DATE-TIME   - auto\_complete\_duration: STRING   - cancel\_reason: STRING   - canceled\_at: DATE-TIME   - expired\_at: DATE-TIME   - expires\_at: DATE-TIME   - note: STRING   - picked\_up\_at: DATE-TIME   - pickup\_at: DATE-TIME   - pickup\_window\_duration: STRING   - placed\_at: DATE-TIME   - prep\_time\_duration: STRING   - ready\_at: DATE-TIME   - recipient: OBJECT, which is also a nested data structure.     - customer\_id: STRING     - display\_name: STRING     - email\_address: STRING     - phone\_number: STRING   - rejected\_at: DATE-TIME   - schedule\_type: STRING - state: STRING - type: STRING - uid: STRING |
| **id**  STRING |
| **line\_items**  ARRAY This is a nested data structure:   - base\_price\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - catalog\_object\_id: STRING - catalog\_version: INTEGER - gross\_sales\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - item\_type: STRING - modifiers: ARRAY, which is also a nested data structure.   - base\_price\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - catalog\_object\_id: STRING   - catalog\_version: INTEGER   - name: STRING   - quantity: STRING   - total\_price\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING - name: STRING - note: STRING - quantity: STRING - quantity\_unit: OBJECT, which is also a nested data structure.   - catalog\_object\_id: STRING   - catalog\_version: INTEGER   - measurement\_unit: OBJECT, which is also a nested data structure.     - area\_unit: STRING     - custom\_unit: OBJECT, which is also a nested data structure.       - abbreviation: STRING       - name: STRING     - generic\_unit: STRING     - length\_unit: STRING     - time\_unit: STRING     - type: STRING     - volume\_unit: STRING     - weight\_unit: STRING   - precision: INTEGER - total\_discount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - total\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - total\_tax\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - uid: STRING - variation\_name: STRING - variation\_total\_price\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING |
| **location\_id**  STRING |
| **net\_amount\_due\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **net\_amounts**  OBJECT This is a nested data structure:   - discount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - service\_charge\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - tax\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - tip\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - total\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING |
| **pricing\_options**  OBJECT This is a nested data structure:   - auto\_apply\_discounts: BOOLEAN |
| **reference\_id**  STRING |
| **refunds**  ARRAY This is a nested data structure:   - amount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - created\_at: DATE-TIME - id: STRING - location\_id: STRING - processing\_fee\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - reason: STRING - status: STRING - tender\_id: STRING - transaction\_id: STRING |
| **return\_amounts**  OBJECT This is a nested data structure:   - discount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - service\_charge\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - tax\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - tip\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - total\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING |
| **returns**  ARRAY This is a nested data structure:   - return\_amounts: OBJECT, which is also a nested data structure.   - discount\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - service\_charge\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - tax\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - tip\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - total\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING - return\_discounts: ARRAY, which is also a nested data structure.   - amount\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - applied\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - catalog\_object\_id: STRING   - catalog\_version: INTEGER   - name: STRING   - percentage: STRING   - scope: STRING   - source\_discount\_uid: STRING   - type: STRING   - uid: STRING - return\_line\_items: ARRAY, which is also a nested data structure.   - applied\_discounts: ARRAY, which is also a nested data structure.     - applied\_money: OBJECT, which is also a nested data structure.       - amount: INTEGER       - currency: STRING     - discount\_uid: STRING     - uid: STRING   - applied\_service\_charges: ARRAY, which is also a nested data structure.     - applied\_money: OBJECT, which is also a nested data structure.       - amount: INTEGER       - currency: STRING     - service\_charge\_uid: STRING     - uid: STRING   - applied\_taxes: ARRAY, which is also a nested data structure.     - applied\_money: OBJECT, which is also a nested data structure.       - amount: INTEGER       - currency: STRING     - tax\_uid: STRING     - uid: STRING   - base\_price\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - catalog\_object\_id: STRING   - catalog\_version: INTEGER   - gross\_return\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - item\_type: STRING   - name: STRING   - note: STRING   - quantity: STRING   - quantity\_unit: OBJECT, which is also a nested data structure.     - catalog\_object\_id: STRING     - catalog\_version: INTEGER     - measurement\_unit: OBJECT, which is also a nested data structure.       - area\_unit: STRING       - custom\_unit: OBJECT, which is also a nested data structure.         - abbreviation: STRING         - name: STRING       - generic\_unit: STRING       - length\_unit: STRING       - time\_unit: STRING       - type: STRING       - volume\_unit: STRING       - weight\_unit: STRING     - precision: INTEGER   - return\_modifiers: ARRAY, which is also a nested data structure.     - base\_price\_money: OBJECT, which is also a nested data structure.       - amount: INTEGER       - currency: STRING     - catalog\_object\_id: STRING     - catalog\_version: INTEGER     - name: STRING     - quantity: STRING     - source\_modifier\_uid: STRING     - total\_price\_money: OBJECT, which is also a nested data structure.       - amount: INTEGER       - currency: STRING     - uid: STRING   - source\_line\_item\_uid: STRING   - total\_discount\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - total\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - total\_service\_charge\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - total\_tax\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - uid: STRING   - variation\_name: STRING   - variation\_total\_price\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING - return\_service\_charges: ARRAY, which is also a nested data structure.   - amount\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - applied\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - calculation\_phase: STRING   - catalog\_object\_id: STRING   - catalog\_version: INTEGER   - name: STRING   - percentage: STRING   - source\_service\_charge\_uid: STRING   - taxable: BOOLEAN   - total\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - total\_tax\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING - return\_taxes: ARRAY, which is also a nested data structure.   - applied\_money: OBJECT, which is also a nested data structure.   - catalog\_object\_id: STRING   - catalog\_version: INTEGER   - name: STRING   - percentage: STRING   - scope: STRING   - source\_tax\_uid: STRING   - type: STRING   - uid: STRING - rounding\_adjustment: OBJECT, which is also a nested data structure.   - amount\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - name: STRING   - uid: STRING - source\_order\_id: STRING - uid: STRING |
| **service\_charges**  ARRAY This is a nested data structure:   - amount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - applied\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - calculation\_phase: STRING - catalog\_object\_id: STRING - catalog\_version: INTEGER - name: STRING - percentage: STRING - taxable: BOOLEAN - total\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - total\_tax\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - type: STRING |
| **source**  OBJECT This is a nested data structure:   - name: STRING |
| **state**  STRING |
| **taxes**  ARRAY This is a nested data structure:   - applied\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - catalog\_object\_id: STRING - catalog\_version: INTEGER - name: STRING - percentage: STRING - scope: STRING - type: STRING |
| **tenders**  ARRAY This is a nested data structure:   - amount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - card\_details: OBJECT, which is also a nested data structure.   - card: OBJECT, which is also a nested data structure.     - billing\_address: OBJECT, which is also a nested data structure.       - address\_line\_1: STRING       - address\_line\_2: STRING       - address\_line\_3: STRING       - administrative\_district\_level\_1: STRING       - administrative\_district\_level\_2: STRING       - administrative\_district\_level\_3: STRING       - country: STRING       - first\_name: STRING       - last\_name: STRING       - locality: STRING       - postal\_code: STRING       - sublocality: STRING       - sublocality\_2: STRING       - sublocality\_3: STRING     - bin: STRING     - card\_brand: STRING     - card\_co\_brand: STRING     - card\_type: STRING     - cardholder\_name: STRING     - customer\_id: STRING     - enabled: BOOLEAN     - exp\_month: INTEGER     - exp\_year: INTEGER     - fingerprint: STRING     - id: STRING     - last\_4: STRING     - merchant\_id: STRING     - prepaid\_type: STRING     - reference\_id: STRING     - version: INTEGER   - entry\_method: STRING   - status: STRING - cash\_details: OBJECT, which is also a nested data structure.   - buyer\_tendered\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING   - change\_back\_money: OBJECT, which is also a nested data structure.     - amount: INTEGER     - currency: STRING - created\_at: DATE-TIME - customer\_id: STRING - id: STRING - location\_id: STRING - note: STRING - payment\_id: STRING - processing\_fee\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - tip\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - transaction\_id: STRING - type: STRING |
| **total\_discount\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **total\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **total\_service\_charge\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **total\_tax\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **total\_tip\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **updated\_at**  DATE-TIME |
| **version**  INTEGER |

### payments

The `payments` table contains information about all payments taken in Square.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/payments-api)  [Square API method](https://developer.squareup.com/reference/square/payments-api/list-payments "Opens in new tab: Square API method") |

payments table foreign keys

| Join payments with | on |
| --- | --- |
| [bank\_accounts](#bank-accounts) | ``` payments.id = bank_accounts.id ``` |
| [categories](#categories) | ``` payments.id = categories.absent_at_location_ids ``` |
| [discounts](#discounts) | ``` payments.id = discounts.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` payments.id = team_members.assigned_locations.location_ids ``` |
| [inventories](#inventories) | ``` payments.id = inventories.location_id ``` |
| [items](#items) | ``` payments.id = items.absent_at_location_ids ```  ``` payments.id = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` payments.id = items.item_data.variations.present_at_location_ids ```  ``` payments.id = items.present_at_location_ids ``` |
| [locations](#locations) | ``` payments.id = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` payments.id = modifier_lists.absent_at_location_ids ``` |
| [orders](#orders) | ``` payments.id = orders.id ```  ``` payments.id = orders.refunds.id ```  ``` payments.id = orders.tenders.id ```  ``` payments.order_id = orders.id ```  ``` payments.order_id = orders.returns.source_order_id ```  ``` payments.order_id = orders.refunds.id ```  ``` payments.refund_ids = orders.refunds.id ``` |
| [refunds](#refunds) | ``` payments.id = refunds.id ```  ``` payments.order_id = refunds.order_id ```  ``` payments.id = refunds.payment_id ```  ``` payments.order_id = refunds.id ```  ``` payments.refund_ids = refunds.id ``` |
| [shifts](#shifts) | ``` payments.id = shifts.id ``` |
| [taxes](#taxes) | ``` payments.id = taxes.absent_at_location_ids ``` |

payments table schema

|  |
| --- |
| **amount\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **app\_fee\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **application\_details**  OBJECT This is a nested data structure:   - application\_id: STRING - square\_product: STRING |
| **approved\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **bank\_account\_details**  OBJECT This is a nested data structure:   - account\_ownership\_type: STRING - ach\_details: OBJECT, which is also a nested data structure.   - account\_number\_suffix: STRING   - account\_type: STRING   - routing\_number: STRIN - bank\_name: STRING - country: STRING - errors: ARRAY, which is also a nested data structure.   - category: STRING   - code: STRING   - detail: STRING   - field: STRING - fingerprint: STRING - statement\_description: STRING - transfer\_type: STRING |
| **billing\_address**  OBJECT This is a nested data structure:   - address\_line\_1: STRING - address\_line\_2: STRING - address\_line\_3: STRING - administrative\_district\_level\_1: STRING - administrative\_district\_level\_2: STRING - administrative\_district\_level\_3: STRING - country: STRING - first\_name: STRING - last\_name: STRING - locality: STRING - postal\_code: STRING - sublocality: STRING - sublocality\_2: STRING - sublocality\_3: STRING |
| **buy\_now\_pay\_later\_details**  OBJECT This is a nested data structure:   - afterpay\_details: OBJECT, which is also a nested data structure.   - email\_address: STRING - brand: STRING - clearpay\_details: OBJECT, which is also a nested data structure.   - email\_address: STRING |
| **buyer\_email\_address**  STRING |
| **capabilities**  ARRAY |
| **card\_details**  OBJECT This is a nested data structure:   - application\_cryptogram: STRING - application\_identifier: STRING - application\_name: STRING - auth\_result\_code: STRING - avs\_status: STRING - card: OBJECT, which is also a nested data structure.   - billing\_address: OBJECT, which is also a nested data structure.   - bin: STRING   - card\_brand: STRING   - card\_co\_brand: STRING   - card\_type: STRING   - cardholder\_name: STRING   - customer\_id: STRING   - enabled: BOOLEAN   - exp\_month: INTEGER   - exp\_year: INTEGER   - fingerprint: STRING   - id: STRING   - last\_4: STRING   - merchant\_id: STRING   - prepaid\_type: STRING   - reference\_id: STRING   - version: INTEGER - card\_payment\_timeline: OBJECT, which is also a nested data structure.   - authorized\_at: DATE-TIME   - captured\_at: DATE-TIME   - voided\_at: DATE-TIME - cvv\_status: STRING - entry\_method: STRING - errors: ARRAY, which is also a nested data structure.   - category: STRING   - code: STRING   - detail: STRING   - field: STRING - statement\_description: STRING - status: STRING - verification\_method: STRING - verification\_results: STRING |
| **cash\_details**  OBJECT This is a nested data structure:   - buyer\_supplied\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - change\_back\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING |
| **created\_at**  DATE-TIME |
| **customer\_id**  STRING |
| **delay\_action**  STRING |
| **delay\_duration**  STRING |
| **delayed\_until**  DATE-TIME |
| **device\_details**  OBJECT This is a nested data structure:   - device\_id: STRING - device\_installation\_id: STRING - device\_name: STRING |
| **external\_details**  OBJECT This is a nested data structure:   - source: STRING - source\_fee\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - source\_id: STRING - type: STRING |
| **id**  STRING |
| **location\_id**  STRING |
| **note**  STRING |
| **order\_id**  STRING |
| **processing\_fee**  ARRAY This is a nested data structure:   - amount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - effective\_at: DATE-TIME - type: STRING |
| **receipt\_number**  STRING |
| **receipt\_url**  STRING |
| **reference\_id**  STRING |
| **refund\_ids**  ARRAY |
| **refunded\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **risk\_evaluation**  OBJECT This is a nested data structure:   - created\_at: DATE-TIME - risk\_level: STRING |
| **shipping\_address**  OBJECT This is a nested data structure:   - address\_line\_1: STRING - address\_line\_2: STRING - address\_line\_3: STRING - administrative\_district\_level\_1: STRING - administrative\_district\_level\_2: STRING - administrative\_district\_level\_3: STRING - country: STRING - first\_name: STRING - last\_name: STRING - locality: STRING - postal\_code: STRING - sublocality: STRING - sublocality\_2: STRING - sublocality\_3: STRING |
| **source\_type**  STRING |
| **statement\_description\_identifier**  STRING |
| **status**  STRING |
| **team\_member\_id**  STRING |
| **tip\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **total\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **updated\_at**  DATE-TIME |
| **version\_token**  STRING |
| **wallet\_details**  OBJECT This is a nested data structure:   - brand: STRING - cash\_app\_details: OBJECT, which is also a nested data structure.   - buyer\_cashtag: STRING   - buyer\_country\_code: STRING   - buyer\_full\_name: STRING - status: STRING |

### payouts

The `payouts` table contains information about all payouts made in Square.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/payouts-api)  [Square API method](https://developer.squareup.com/reference/square/payouts-api/list-payouts "Opens in new tab: Square API method") |

payouts table schema

|  |
| --- |
| **amount\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **arrival\_date**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **destination**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **end\_to\_end\_id**  STRING |
| **id**  STRING |
| **location\_id**  STRING |
| **payout\_fee**  ARRAY This is a nested data structure:   - amount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - effective\_at: DATE-TIME - type: STRING |
| **status**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **version**  INTEGER |

### refunds

The `refunds` table contains information about refunds on items in Square.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/refunds-api)  [Square API method](https://developer.squareup.com/reference/square/refunds-api/list-payment-refunds "Opens in new tab: Square API method") |

refunds table foreign keys

| Join refunds with | on |
| --- | --- |
| [bank\_accounts](#bank-accounts) | ``` refunds.id = bank_accounts.id ``` |
| [categories](#categories) | ``` refunds.id = categories.absent_at_location_ids ``` |
| [discounts](#discounts) | ``` refunds.id = discounts.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` refunds.id = team_members.assigned_locations.location_ids ``` |
| [inventories](#inventories) | ``` refunds.id = inventories.location_id ``` |
| [items](#items) | ``` refunds.id = items.absent_at_location_ids ```  ``` refunds.id = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` refunds.id = items.item_data.variations.present_at_location_ids ```  ``` refunds.id = items.present_at_location_ids ``` |
| [locations](#locations) | ``` refunds.id = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` refunds.id = modifier_lists.absent_at_location_ids ``` |
| [orders](#orders) | ``` refunds.id = orders.id ```  ``` refunds.id = orders.refunds.id ```  ``` refunds.id = orders.tenders.id ```  ``` refunds.order_id = orders.id ```  ``` refunds.order_id = orders.returns.source_order_id ```  ``` refunds.payment_id = orders.tenders.id ``` |
| [payments](#payments) | ``` refunds.id = payments.id ```  ``` refunds.order_id = payments.order_id ```  ``` refunds.payment_id = payments.id ```  ``` refunds.id = payments.order_id ```  ``` refunds.id = payments.refund_ids ``` |
| [shifts](#shifts) | ``` refunds.id = shifts.id ``` |
| [taxes](#taxes) | ``` refunds.id = taxes.absent_at_location_ids ``` |

refunds table schema

|  |
| --- |
| **amount\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **app\_fee\_money**  OBJECT This is a nested data structure:   - amount: INTEGER - currency: STRING |
| **created\_at**  DATE-TIME |
| **destination\_details**  OBJECT This is a nested data structure:   - card\_details: OBJECT, which is also a nested data structure.   - card: OBJECT, which is also a nested data structure.     - billing\_address: OBJECT, which is also a nested data structure.       - address\_line\_1: STRING       - address\_line\_2: STRING       - address\_line\_3: STRING       - administrative\_district\_level\_1: STRING       - administrative\_district\_level\_2: STRING       - administrative\_district\_level\_3: STRING       - country: STRING       - first\_name: STRING       - last\_name: STRING       - locality: STRING       - postal\_code: STRING       - sublocality: STRING       - sublocality\_2: STRING       - sublocality\_3: STRING     - bin: STRING     - card\_brand: STRING     - card\_co\_brand: STRING     - card\_type: STRING     - cardholder\_name: STRING     - customer\_id: STRING     - enabled: BOOLEAN     - exp\_month: INTEGER     - exp\_year: INTEGER     - fingerprint: STRING     - id: STRING     - last\_4: STRING     - merchant\_id: STRING     - prepaid\_type: STRING     - reference\_id: STRING     - version: INTEGER   - entry\_method: STRING |
| **destination\_type**  STRING |
| **id**  STRING |
| **location\_id**  STRING |
| **order\_id**  STRING |
| **payment\_id**  STRING |
| **processing\_fee**  ARRAY This is a nested data structure:   - amount\_money: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - effective\_at: DATE-TIME - type: STRING |
| **reason**  STRING |
| **status**  STRING |
| **team\_member\_id**  STRING |
| **unlinked**  BOOLEAN |
| **updated\_at**  DATE-TIME |

### roles

The `roles` table contains information about employees’ roles in Square.

**Note**: This table can’t be replicated if the **Connect to a sandbox environment** box is checked in the [integration’s settings](#add-stitch-data-source) due to limits imposed by Square.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/employees-api)  [Square API method](https://developer.squareup.com/reference/square/employees-api/v1-list-employee-roles "Opens in new tab: Square API method") |

roles table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **id**  STRING |
| **is\_owner**  BOOLEAN |
| **name**  STRING |
| **permissions**  ARRAY |
| **updated\_at**  DATE-TIME |

### shifts

The `shifts` table contains information about employee’s shifts in Square.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | updated\_at |
| **Useful links** | [Square documentation](https://developer.squareup.com/reference/square/labor-api)  [Square API method](https://developer.squareup.com/reference/square/labor-api/search-shifts "Opens in new tab: Square API method") |

shifts table foreign keys

| Join shifts with | on |
| --- | --- |
| [team\_members](#team-members) | ``` shifts.team_member_id = team_members.id ```  ``` shifts.id = team_members.assigned_locations.location_ids ``` |
| [bank\_accounts](#bank-accounts) | ``` shifts.id = bank_accounts.id ``` |
| [categories](#categories) | ``` shifts.id = categories.absent_at_location_ids ``` |
| [discounts](#discounts) | ``` shifts.id = discounts.absent_at_location_ids ``` |
| [inventories](#inventories) | ``` shifts.id = inventories.location_id ``` |
| [items](#items) | ``` shifts.id = items.absent_at_location_ids ```  ``` shifts.id = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` shifts.id = items.item_data.variations.present_at_location_ids ```  ``` shifts.id = items.present_at_location_ids ``` |
| [locations](#locations) | ``` shifts.id = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` shifts.id = modifier_lists.absent_at_location_ids ``` |
| [orders](#orders) | ``` shifts.id = orders.id ```  ``` shifts.id = orders.refunds.id ```  ``` shifts.id = orders.tenders.id ``` |
| [payments](#payments) | ``` shifts.id = payments.id ``` |
| [refunds](#refunds) | ``` shifts.id = refunds.id ``` |
| [taxes](#taxes) | ``` shifts.id = taxes.absent_at_location_ids ``` |

shifts table schema

|  |
| --- |
| **breaks**  ARRAY This is a nested data structure:   - break\_type\_id: STRING - end\_at: DATE-TIME - expected\_duration: STRING - id: STRING - is\_paid: BOOLEAN - name: STRING - start\_at: DATE-TIME |
| **created\_at**  DATE-TIME |
| **end\_at**  DATE-TIME |
| **id**  STRING |
| **location\_id**  STRING |
| **start\_at**  DATE-TIME |
| **status**  STRING |
| **team\_member\_id**  STRING |
| **timezone**  STRING |
| **updated\_at**  DATE-TIME |
| **version**  INTEGER |
| **wage**  OBJECT This is a nested data structure:   - hourly\_rate: OBJECT, which is also a nested data structure.   - amount: INTEGER   - currency: STRING - job\_id: STRING - title: STRING |

### taxes

The `taxes` table contains information about taxes enabled on your items in Square.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Square API method](https://developer.squareup.com/reference/square/catalog-api/list-catalog "Opens in new tab: Square API method") |

taxes table foreign keys

| Join taxes with | on |
| --- | --- |
| [bank\_accounts](#bank-accounts) | ``` taxes.absent_at_location_ids = bank_accounts.id ``` |
| [categories](#categories) | ``` taxes.absent_at_location_ids = categories.absent_at_location_ids ``` |
| [discounts](#discounts) | ``` taxes.absent_at_location_ids = discounts.absent_at_location_ids ``` |
| [team\_members](#team-members) | ``` taxes.absent_at_location_ids = team_members.assigned_locations.location_ids ``` |
| [inventories](#inventories) | ``` taxes.absent_at_location_ids = inventories.location_id ``` |
| [items](#items) | ``` taxes.absent_at_location_ids = items.absent_at_location_ids ```  ``` taxes.absent_at_location_ids = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` taxes.absent_at_location_ids = items.item_data.variations.present_at_location_ids ```  ``` taxes.absent_at_location_ids = items.present_at_location_ids ```  ``` taxes.id = items.item_data.tax_ids ``` |
| [locations](#locations) | ``` taxes.absent_at_location_ids = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` taxes.absent_at_location_ids = modifier_lists.absent_at_location_ids ``` |
| [orders](#orders) | ``` taxes.absent_at_location_ids = orders.id ```  ``` taxes.absent_at_location_ids = orders.refunds.id ```  ``` taxes.absent_at_location_ids = orders.tenders.id ``` |
| [payments](#payments) | ``` taxes.absent_at_location_ids = payments.id ``` |
| [refunds](#refunds) | ``` taxes.absent_at_location_ids = refunds.id ``` |
| [shifts](#shifts) | ``` taxes.absent_at_location_ids = shifts.id ``` |

taxes table schema

|  |
| --- |
| **absent\_at\_location\_ids**  ARRAY |
| **id**  STRING |
| **is\_deleted**  BOOLEAN |
| **present\_at\_all\_locations**  BOOLEAN |
| **tax\_data**  OBJECT This is a nested data structure:   - applies\_to\_custom\_amounts: BOOLEAN - calculation\_phase: STRING - enabled: BOOLEAN - inclusion\_type: STRING - name: STRING - percentage: STRING - tax\_type\_id: STRING - tax\_type\_name: STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **version**  INTEGER |

### team\_members

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | updated\_at |
| **Useful links** | Square documentation  [Square API method](https://developer.squareup.com/reference/square/team-api/search-team-members "Opens in new tab: Square API method") |

team\_members table foreign keys

| Join team\_members with | on |
| --- | --- |
| [shifts](#shifts) | ``` team_members.id = shifts.team_member_id ```  ``` team_members.assigned_locations.location_ids = shifts.id ``` |
| [bank\_accounts](#bank-accounts) | ``` team_members.assigned_locations.location_ids = bank_accounts.id ``` |
| [categories](#categories) | ``` team_members.assigned_locations.location_ids = categories.absent_at_location_ids ``` |
| [discounts](#discounts) | ``` team_members.assigned_locations.location_ids = discounts.absent_at_location_ids ``` |
| [inventories](#inventories) | ``` team_members.assigned_locations.location_ids = inventories.location_id ``` |
| [items](#items) | ``` team_members.assigned_locations.location_ids = items.absent_at_location_ids ```  ``` team_members.assigned_locations.location_ids = items.item_data.variations.item_variation_data.location_overrides.location_id ```  ``` team_members.assigned_locations.location_ids = items.item_data.variations.present_at_location_ids ```  ``` team_members.assigned_locations.location_ids = items.present_at_location_ids ``` |
| [locations](#locations) | ``` team_members.assigned_locations.location_ids = locations.id ``` |
| [modifier\_lists](#modifier-lists) | ``` team_members.assigned_locations.location_ids = modifier_lists.absent_at_location_ids ``` |
| [orders](#orders) | ``` team_members.assigned_locations.location_ids = orders.id ```  ``` team_members.assigned_locations.location_ids = orders.refunds.id ```  ``` team_members.assigned_locations.location_ids = orders.tenders.id ``` |
| [payments](#payments) | ``` team_members.assigned_locations.location_ids = payments.id ``` |
| [refunds](#refunds) | ``` team_members.assigned_locations.location_ids = refunds.id ``` |
| [taxes](#taxes) | ``` team_members.assigned_locations.location_ids = taxes.absent_at_location_ids ``` |

team\_members table schema

|  |
| --- |
| **assigned\_locations**  OBJECT This is a nested data structure:   - assignment\_type: STRING - location\_ids: ARRAY |
| **created\_at**  DATE-TIME |
| **email\_address**  STRING |
| **family\_name**  STRING |
| **given\_name**  STRING |
| **id**  STRING |
| **is\_owner**  BOOLEAN |
| **phone\_number**  STRING |
| **reference\_id**  STRING |
| **status**  STRING |
| **updated\_at**  DATE-TIME |
