---
title: "3PL Central"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-3PLCentral-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# 3PL Central

3PL Central is a cloud-based warehouse management system (WMS) solutions built to meet the needs of the 3PL warehousing community.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your API credentials:

1. Contact api@extensiv.com and request the following access information:
   - Base Url
   - Client ID
   - Client Secret
   - Facility ID
   - Customer ID
   - TPL Key
   - User Login
2. Once you have your access information, set up the integration app in 3PL Central.

   For more information, see [3PL Central's documentation](https://help.extensiv.com/en_US/366924-3pl-central/1624713-setting-up-extensiv-3pl-warehouse-manager).

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
| Base Url | Base URL. |
| Client ID | Client ID. |
| Client Secret | Client secret. |
| Customer ID | Customer ID. |
| Facility ID | Facility ID. |
| TPL Key | Warehouse-specific 3PL Central key. |
| User Login | User login. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### customers

This table contains information about customers.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | customer\_id |
| **Useful links** | [3PL Central documentation](http://api.3plcentral.com/rels/)  [3PL Central API method](http://api.3plcentral.com/rels/customers/customers "Opens in new tab: 3PL Central API method") |

customers table foreign keys

| Join customers with | on |
| --- | --- |
| [sku\_items](#sku-items) | ``` customers.customer_id = sku_items.customer_id ```  ``` customers.customer_id = sku_items.customer_identifier.id ```  ``` customers.facilities.id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ```  ``` customers.primary_facility_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ``` |
| [stock\_details](#stock-details) | ``` customers.customer_id = stock_details.customer_id ```  ``` customers.facilities.id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` customers.primary_facility_identifier.id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` customers.facilities.id = stock_details.pallet_identifier.name_key.facility_identifier.id ```  ``` customers.primary_facility_identifier.id = stock_details.pallet_identifier.name_key.facility_identifier.id ``` |
| [inventory](#inventory) | ``` customers.customer_id = inventory.customer_identifier.id ```  ``` customers.facilities.id = inventory.facility_identifier.id ```  ``` customers.primary_facility_identifier.id = inventory.facility_identifier.id ```  ``` customers.facilities.id = inventory.location_identifier.name_key.facility_identifier.id ```  ``` customers.primary_facility_identifier.id = inventory.location_identifier.name_key.facility_identifier.id ```  ``` customers.facilities.id = inventory.pallet_identifier.name_key.facility_identifier.id ```  ``` customers.primary_facility_identifier.id = inventory.pallet_identifier.name_key.facility_identifier.id ``` |
| [locations](#locations) | ``` customers.customer_id = locations.customer_identifier.id ```  ``` customers.facilities.id = locations.facility_id ```  ``` customers.primary_facility_identifier.id = locations.facility_id ```  ``` customers.facilities.id = locations.item_traits.pallet_identifier.name_key.facility_identifier.id ```  ``` customers.primary_facility_identifier.id = locations.item_traits.pallet_identifier.name_key.facility_identifier.id ```  ``` customers.facilities.id = locations.location_identifier.name_key.facility_identifier.id ```  ``` customers.primary_facility_identifier.id = locations.location_identifier.name_key.facility_identifier.id ``` |
| [orders](#orders) | ``` customers.customer_id = orders.customer_identifier.id ```  ``` customers.customer_id = orders.batch_identifier.name_key.customer_identifier.id ```  ``` customers.customer_id = orders.ship_to.retailer_info.name_key.customer_identifier.id ```  ``` customers.facilities.id = orders.facility_identifier.id ```  ``` customers.primary_facility_identifier.id = orders.facility_identifier.id ``` |
| [stock\_summaries](#stock-summaries) | ``` customers.facilities.id = stock_summaries.facility_id ```  ``` customers.primary_facility_identifier.id = stock_summaries.facility_id ``` |

customers table schema

|  |
| --- |
| **company\_info**  OBJECT This is a nested data structure:   - address1: STRING - address2: STRING - address\_status: INTEGER - city: STRING - code: STRING - company\_name: STRING - contact\_id: INTEGER - country: STRING - dept: STRING - email\_address: STRING - fax: STRING - name: STRING - phone\_number: STRING - state: STRING - title: STRING - zip: STRING |
| **creation\_date**  DATE-TIME |
| **customer\_id**  INTEGER |
| **deactivated**  BOOLEAN |
| **external\_id**  STRING |
| **facilities**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING |
| **groups**  ARRAY This is a nested data structure. |
| **options**  OBJECT This is a nested data structure:   - alerts: OBJECT, which is also a nested data structure.   - expiration\_notification\_threshold: INTEGER   - from\_email\_address: STRING   - notify\_ship\_to: BOOLEAN - edi: OBJECT, which is also a nested data structure.   - customer\_interchange\_id: STRING   - customer\_interchange\_id\_qual: STRING   - threepl\_interchange\_id: STRING   - threepl\_interchange\_id\_qual: STRING   - trading\_partner\_id: STRING - other\_system\_behaviors: OBJECT, which is also a nested data structure.   - flex\_fields: BOOLEAN   - require\_attached\_documents: BOOLEAN - packaging: OBJECT, which is also a nested data structure.   - small\_parcel\_create\_packages\_on\_find: BOOLEAN   - small\_parcel\_customize\_duties: BOOLEAN   - small\_parcel\_duties\_and\_taxes: STRING   - small\_parcel\_duty\_billing\_type: STRING   - small\_parcel\_high\_volume\_default\_checked: BOOLEAN   - small\_parcel\_high\_volume\_zpl\_batched: BOOLEAN   - small\_parcel\_rate\_shopping\_carrier\_ids: STRING   - small\_parcel\_rate\_shopping\_logic: STRING   - small\_parcel\_references: STRING   - small\_parcel\_return\_default\_checked: BOOLEAN   - small\_parcel\_return\_fed\_ex\_service: STRING   - small\_parcel\_return\_shipping\_cost: BOOLEAN   - small\_parcel\_return\_ups\_service: STRING   - small\_parcel\_usps\_3rd\_party: STRING   - small\_parcel\_usps\_return\_type: STRING   - sps\_close\_on\_update: BOOLEAN   - ucc128\_manufacturers\_id: INTEGER   - use\_vendor\_id\_on\_bol: BOOLEAN - receivers: OBJECT, which is also a nested data structure.   - defs: ARRAY, which is also a nested data structure.     - name: STRING     - required: BOOLEAN   - item\_defs: ARRAY, which is also a nested data structure.     - name: STRING     - required: BOOLEAN - receiving: OBJECT, which is also a nested data structure.   - autofill\_track\_bys: BOOLEAN   - create\_multiple\_mus: BOOLEAN   - inherit\_original\_receipt\_date\_on\_transfer: BOOLEAN   - purchase\_orders: BOOLEAN   - receive\_against\_asns: INTEGER   - require\_scac\_for\_asn: BOOLEAN   - suggest\_put\_away\_enabled: BOOLEAN   - track\_location: INTEGER   - track\_pallets: INTEGER   - track\_supplier: INTEGER - saved\_elements: OBJECT, which is also a nested data structure.   - orders: OBJECT, which is also a nested data structure.     - defs: ARRAY, which is also a nested data structure.       - name: STRING       - required: BOOLEAN     - item\_defs: ARRAY, which is also a nested data structure.       - name: STRING       - required: BOOLEAN - shipping: OBJECT, which is also a nested data structure.   - auto\_confirm\_order\_on\_tracking\_update: BOOLEAN   - bol\_num\_as\_trans\_num: BOOLEAN   - fed\_ex\_account\_number: STRING   - fulfillment\_invoicing: INTEGER   - next\_master\_bol\_id: INTEGER   - next\_master\_bol\_id\_override: INTEGER   - order\_queue: BOOLEAN   - packing\_list\_footer\_url: STRING   - packing\_list\_logo\_url: STRING   - prepopulate\_carrier\_info: INTEGER   - require\_tracking\_number: BOOLEAN   - roundupto\_full\_mu: BOOLEAN   - ups\_account\_number: STRING   - ups\_account\_zip: STRING - storage: OBJECT, which is also a nested data structure.   - accounting\_customer\_name: STRING   - autofill\_charges\_on\_confirm: BOOLEAN   - fuel\_surcharge: NUMBER   - set\_invoice\_date\_to\_xaction\_confirm\_date: BOOLEAN - user\_interface: OBJECT, which is also a nested data structure.   - auto\_check\_auto\_reallocate\_on\_receive: BOOLEAN   - branding\_image\_id: INTEGER   - dashboard: BOOLEAN   - exclude\_location\_with\_zero\_inventory: BOOLEAN   - hide\_location\_selected\_list: BOOLEAN   - mobile\_receipt\_quantity\_one\_default: BOOLEAN   - reallocate\_at\_pick\_time: BOOLEAN   - transaction\_confirm\_invoice\_create\_default: INTEGER |
| **other\_contacts**  ARRAY This is a nested data structure:   - address1: STRING - address2: STRING - address\_status: INTEGER - city: STRING - code: STRING - company\_name: STRING - contact\_id: INTEGER - country: STRING - dept: STRING - email\_address: STRING - fax: STRING - name: STRING - phone\_number: STRING - state: STRING - title: STRING - zip: STRING |
| **primary\_contact**  OBJECT This is a nested data structure:   - address1: STRING - address2: STRING - address\_status: INTEGER - city: STRING - code: STRING - company\_name: STRING - contact\_id: INTEGER - country: STRING - dept: STRING - email\_address: STRING - fax: STRING - name: STRING - phone\_number: STRING - state: STRING - title: STRING - zip: STRING |
| **primary\_facility\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **website**  STRING |

### inventory

This table contains information about inventory resources.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | receive\_item\_id |
| **Useful links** | [3PL Central documentation](http://api.3plcentral.com/rels/)  [3PL Central API method](http://api.3plcentral.com/rels/inventory/inventory "Opens in new tab: 3PL Central API method") |

inventory table foreign keys

| Join inventory with | on |
| --- | --- |
| [customers](#customers) | ``` inventory.customer_identifier.id = customers.customer_id ```  ``` inventory.facility_identifier.id = customers.facilities.id ```  ``` inventory.location_identifier.name_key.facility_identifier.id = customers.facilities.id ```  ``` inventory.pallet_identifier.name_key.facility_identifier.id = customers.facilities.id ```  ``` inventory.facility_identifier.id = customers.primary_facility_identifier.id ```  ``` inventory.location_identifier.name_key.facility_identifier.id = customers.primary_facility_identifier.id ```  ``` inventory.pallet_identifier.name_key.facility_identifier.id = customers.primary_facility_identifier.id ``` |
| [sku\_items](#sku-items) | ``` inventory.customer_identifier.id = sku_items.customer_id ```  ``` inventory.customer_identifier.id = sku_items.customer_identifier.id ```  ``` inventory.facility_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ```  ``` inventory.location_identifier.name_key.facility_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ```  ``` inventory.pallet_identifier.name_key.facility_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ```  ``` inventory.item_identifier.id = sku_items.item_id ```  ``` inventory.item_identifier.id = sku_items.kit.components.item_identifier.id ```  ``` inventory.location_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.id ``` |
| [stock\_details](#stock-details) | ``` inventory.customer_identifier.id = stock_details.customer_id ```  ``` inventory.facility_identifier.id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` inventory.location_identifier.name_key.facility_identifier.id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` inventory.pallet_identifier.name_key.facility_identifier.id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` inventory.facility_identifier.id = stock_details.pallet_identifier.name_key.facility_identifier.id ```  ``` inventory.location_identifier.name_key.facility_identifier.id = stock_details.pallet_identifier.name_key.facility_identifier.id ```  ``` inventory.pallet_identifier.name_key.facility_identifier.id = stock_details.pallet_identifier.name_key.facility_identifier.id ```  ``` inventory.item_identifier.id = stock_details.item_identifier.id ```  ``` inventory.location_identifier.id = stock_details.location_identifier.id ```  ``` inventory.pallet_identifier.id = stock_details.pallet_identifier.id ```  ``` inventory.receiver_id = stock_details.receiver_id ```  ``` inventory.receive_item_id = stock_details.receive_item_id ```  ``` inventory.supplier_identifier.id = stock_details.supplier_identifier.id ``` |
| [locations](#locations) | ``` inventory.customer_identifier.id = locations.customer_identifier.id ```  ``` inventory.facility_identifier.id = locations.facility_id ```  ``` inventory.location_identifier.name_key.facility_identifier.id = locations.facility_id ```  ``` inventory.pallet_identifier.name_key.facility_identifier.id = locations.facility_id ```  ``` inventory.facility_identifier.id = locations.item_traits.pallet_identifier.name_key.facility_identifier.id ```  ``` inventory.location_identifier.name_key.facility_identifier.id = locations.item_traits.pallet_identifier.name_key.facility_identifier.id ```  ``` inventory.pallet_identifier.name_key.facility_identifier.id = locations.item_traits.pallet_identifier.name_key.facility_identifier.id ```  ``` inventory.facility_identifier.id = locations.location_identifier.name_key.facility_identifier.id ```  ``` inventory.location_identifier.name_key.facility_identifier.id = locations.location_identifier.name_key.facility_identifier.id ```  ``` inventory.pallet_identifier.name_key.facility_identifier.id = locations.location_identifier.name_key.facility_identifier.id ```  ``` inventory.location_identifier.id = locations.location_id ```  ``` inventory.location_identifier.id = locations.location_identifier.id ```  ``` inventory.pallet_identifier.id = locations.item_traits.pallet_identifier.id ``` |
| [orders](#orders) | ``` inventory.customer_identifier.id = orders.customer_identifier.id ```  ``` inventory.customer_identifier.id = orders.batch_identifier.name_key.customer_identifier.id ```  ``` inventory.customer_identifier.id = orders.ship_to.retailer_info.name_key.customer_identifier.id ```  ``` inventory.facility_identifier.id = orders.facility_identifier.id ```  ``` inventory.location_identifier.name_key.facility_identifier.id = orders.facility_identifier.id ```  ``` inventory.pallet_identifier.name_key.facility_identifier.id = orders.facility_identifier.id ``` |
| [stock\_summaries](#stock-summaries) | ``` inventory.facility_identifier.id = stock_summaries.facility_id ```  ``` inventory.location_identifier.name_key.facility_identifier.id = stock_summaries.facility_id ```  ``` inventory.pallet_identifier.name_key.facility_identifier.id = stock_summaries.facility_id ``` |

inventory table schema

|  |
| --- |
| **available\_qty**  NUMBER |
| **cost**  NUMBER |
| **customer\_identifier**  OBJECT This is a nested data structure:   - external\_d: STRING - id: INTEGER - name: STRING |
| **expiration\_date**  DATE-TIME |
| **facility\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **inventory\_unit\_of\_measure\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **inventory\_units\_per\_secondary\_unity**  NUMBER |
| **item\_description**  STRING |
| **item\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - sku: STRING |
| **location\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name\_key: OBJECT, which is also a nested data structure.   - facility\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING   - name: STRING |
| **lot\_number**  STRING |
| **on\_hand\_qty**  NUMBER |
| **on\_hold**  BOOLEAN |
| **on\_hold\_date**  DATE-TIME |
| **on\_hold\_qty**  NUMBER |
| **on\_hold\_reason**  STRING |
| **on\_hold\_user\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **pallet\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name\_key: OBJECT, which is also a nested data structure.   - facility\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING   - name: STRING |
| **qualifier**  STRING |
| **quarantined**  BOOLEAN |
| **receive\_item\_id**  INTEGER |
| **receive\_qty**  NUMBER |
| **received\_date**  DATE-TIME |
| **receiver\_id**  INTEGER |
| **secondary\_available\_qty**  NUMBER |
| **secondary\_on\_hand\_qty**  NUMBER |
| **secondary\_on\_hold\_qty**  NUMBER |
| **secondary\_received\_qty**  NUMBER |
| **secondary\_unit\_of\_measure\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **serial\_number**  STRING |
| **supplier\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **weight\_imperial**  NUMBER |
| **weight\_imperial\_available**  NUMBER |
| **weight\_imperial\_on\_hand**  NUMBER |
| **weight\_metric**  NUMBER |
| **weight\_metric\_available**  NUMBER |
| **weight\_metric\_on\_hand**  NUMBER |

### locations

This table contains information about inventory facility locations.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | location\_id  facility\_id |
| **Useful links** | [3PL Central documentation](http://api.3plcentral.com/rels/)  [3PL Central API method](http://api.3plcentral.com/rels/inventory/locations "Opens in new tab: 3PL Central API method") |

locations table foreign keys

| Join locations with | on |
| --- | --- |
| [customers](#customers) | ``` locations.customer_identifier.id = customers.customer_id ```  ``` locations.facility_id = customers.facilities.id ```  ``` locations.item_traits.pallet_identifier.name_key.facility_identifier.id = customers.facilities.id ```  ``` locations.location_identifier.name_key.facility_identifier.id = customers.facilities.id ```  ``` locations.facility_id = customers.primary_facility_identifier.id ```  ``` locations.item_traits.pallet_identifier.name_key.facility_identifier.id = customers.primary_facility_identifier.id ```  ``` locations.location_identifier.name_key.facility_identifier.id = customers.primary_facility_identifier.id ``` |
| [sku\_items](#sku-items) | ``` locations.customer_identifier.id = sku_items.customer_id ```  ``` locations.customer_identifier.id = sku_items.customer_identifier.id ```  ``` locations.facility_id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ```  ``` locations.item_traits.pallet_identifier.name_key.facility_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ```  ``` locations.location_identifier.name_key.facility_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ```  ``` locations.item_traits.item_identifier.id = sku_items.item_id ```  ``` locations.location_id = sku_items.options.directed_put_away.preferred_location_identifier.id ```  ``` locations.location_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.id ``` |
| [stock\_details](#stock-details) | ``` locations.customer_identifier.id = stock_details.customer_id ```  ``` locations.facility_id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` locations.item_traits.pallet_identifier.name_key.facility_identifier.id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` locations.location_identifier.name_key.facility_identifier.id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` locations.facility_id = stock_details.pallet_identifier.name_key.facility_identifier.id ```  ``` locations.item_traits.pallet_identifier.name_key.facility_identifier.id = stock_details.pallet_identifier.name_key.facility_identifier.id ```  ``` locations.location_identifier.name_key.facility_identifier.id = stock_details.pallet_identifier.name_key.facility_identifier.id ```  ``` locations.location_id = stock_details.location_identifier.id ```  ``` locations.location_identifier.id = stock_details.location_identifier.id ```  ``` locations.item_traits.pallet_identifier.id = stock_details.pallet_identifier.id ``` |
| [inventory](#inventory) | ``` locations.customer_identifier.id = inventory.customer_identifier.id ```  ``` locations.facility_id = inventory.facility_identifier.id ```  ``` locations.item_traits.pallet_identifier.name_key.facility_identifier.id = inventory.facility_identifier.id ```  ``` locations.location_identifier.name_key.facility_identifier.id = inventory.facility_identifier.id ```  ``` locations.facility_id = inventory.location_identifier.name_key.facility_identifier.id ```  ``` locations.item_traits.pallet_identifier.name_key.facility_identifier.id = inventory.location_identifier.name_key.facility_identifier.id ```  ``` locations.location_identifier.name_key.facility_identifier.id = inventory.location_identifier.name_key.facility_identifier.id ```  ``` locations.facility_id = inventory.pallet_identifier.name_key.facility_identifier.id ```  ``` locations.item_traits.pallet_identifier.name_key.facility_identifier.id = inventory.pallet_identifier.name_key.facility_identifier.id ```  ``` locations.location_identifier.name_key.facility_identifier.id = inventory.pallet_identifier.name_key.facility_identifier.id ```  ``` locations.location_id = inventory.location_identifier.id ```  ``` locations.location_identifier.id = inventory.location_identifier.id ```  ``` locations.item_traits.pallet_identifier.id = inventory.pallet_identifier.id ``` |
| [orders](#orders) | ``` locations.customer_identifier.id = orders.customer_identifier.id ```  ``` locations.customer_identifier.id = orders.batch_identifier.name_key.customer_identifier.id ```  ``` locations.customer_identifier.id = orders.ship_to.retailer_info.name_key.customer_identifier.id ```  ``` locations.facility_id = orders.facility_identifier.id ```  ``` locations.item_traits.pallet_identifier.name_key.facility_identifier.id = orders.facility_identifier.id ```  ``` locations.location_identifier.name_key.facility_identifier.id = orders.facility_identifier.id ``` |
| [stock\_summaries](#stock-summaries) | ``` locations.facility_id = stock_summaries.facility_id ```  ``` locations.item_traits.pallet_identifier.name_key.facility_identifier.id = stock_summaries.facility_id ```  ``` locations.location_identifier.name_key.facility_identifier.id = stock_summaries.facility_id ```  ``` locations.item_traits.item_identifier.id = stock_summaries.item_id ``` |

locations table schema

|  |
| --- |
| **customer\_identifier**  OBJECT This is a nested data structure:   - external\_id: STRING - id: INTEGER - name: STRING |
| **description**  STRING |
| **facility\_id**  INTEGER |
| **item\_traits**  OBJECT This is a nested data structure:   - expiration\_date: DATE-TIME - item\_identifier: OBJECT, which is also a nested data structure.   - id: INTEGER   - sku: STRING - lot\_number: STRING - pallet\_identifier: OBJECT, which is also a nested data structure.   - id: INTEGER   - name\_key: OBJECT, which is also a nested data structure.     - facility\_identifier: OBJECT, which is also a nested data structure.       - id: INTEGER       - name: STRING     - name: STRING - qualifier: STRING - serial\_number: STRING |
| **location\_id**  INTEGER |
| **location\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name\_key: OBJECT, which is also a nested data structure.   - facility\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING   - name: STRING |
| **location\_type\_identifier**  OBJECT  - id: INTEGER - name: STRING |
| **on\_hand**  NUMBER |

### orders

This table contains information about orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | order\_id |
| **Replication Key** | last\_modified\_date |
| **Useful links** | [3PL Central documentation](http://api.3plcentral.com/rels/)  [3PL Central API method](http://api.3plcentral.com/rels/orders/orders "Opens in new tab: 3PL Central API method") |

orders table foreign keys

| Join orders with | on |
| --- | --- |
| [customers](#customers) | ``` orders.customer_identifier.id = customers.customer_id ```  ``` orders.batch_identifier.name_key.customer_identifier.id = customers.customer_id ```  ``` orders.ship_to.retailer_info.name_key.customer_identifier.id = customers.customer_id ```  ``` orders.facility_identifier.id = customers.facilities.id ```  ``` orders.facility_identifier.id = customers.primary_facility_identifier.id ``` |
| [sku\_items](#sku-items) | ``` orders.customer_identifier.id = sku_items.customer_id ```  ``` orders.batch_identifier.name_key.customer_identifier.id = sku_items.customer_id ```  ``` orders.ship_to.retailer_info.name_key.customer_identifier.id = sku_items.customer_id ```  ``` orders.customer_identifier.id = sku_items.customer_identifier.id ```  ``` orders.batch_identifier.name_key.customer_identifier.id = sku_items.customer_identifier.id ```  ``` orders.ship_to.retailer_info.name_key.customer_identifier.id = sku_items.customer_identifier.id ```  ``` orders.facility_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ``` |
| [stock\_details](#stock-details) | ``` orders.customer_identifier.id = stock_details.customer_id ```  ``` orders.batch_identifier.name_key.customer_identifier.id = stock_details.customer_id ```  ``` orders.ship_to.retailer_info.name_key.customer_identifier.id = stock_details.customer_id ```  ``` orders.facility_identifier.id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` orders.facility_identifier.id = stock_details.pallet_identifier.name_key.facility_identifier.id ``` |
| [inventory](#inventory) | ``` orders.customer_identifier.id = inventory.customer_identifier.id ```  ``` orders.batch_identifier.name_key.customer_identifier.id = inventory.customer_identifier.id ```  ``` orders.ship_to.retailer_info.name_key.customer_identifier.id = inventory.customer_identifier.id ```  ``` orders.facility_identifier.id = inventory.facility_identifier.id ```  ``` orders.facility_identifier.id = inventory.location_identifier.name_key.facility_identifier.id ```  ``` orders.facility_identifier.id = inventory.pallet_identifier.name_key.facility_identifier.id ``` |
| [locations](#locations) | ``` orders.customer_identifier.id = locations.customer_identifier.id ```  ``` orders.batch_identifier.name_key.customer_identifier.id = locations.customer_identifier.id ```  ``` orders.ship_to.retailer_info.name_key.customer_identifier.id = locations.customer_identifier.id ```  ``` orders.facility_identifier.id = locations.facility_id ```  ``` orders.facility_identifier.id = locations.item_traits.pallet_identifier.name_key.facility_identifier.id ```  ``` orders.facility_identifier.id = locations.location_identifier.name_key.facility_identifier.id ``` |
| [stock\_summaries](#stock-summaries) | ``` orders.facility_identifier.id = stock_summaries.facility_id ``` |

orders table schema

|  |
| --- |
| **add\_freight\_to\_cod**  BOOLEAN |
| **asn\_candidate**  INTEGER |
| **asn\_number**  STRING |
| **asn\_sent**  BOOLEAN |
| **asn\_sent\_date**  DATE-TIME |
| **batch\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name\_key: OBJECT, which is also a nested data structure.   - facility\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING   - name: STRING |
| **bill\_to**  OBJECT This is a nested data structure:   - address1: STRING - address2: STRING - address\_status: INTEGER - city: STRING - code: STRING - company\_name: STRING - contact\_id: INTEGER - country: STRING - dept: STRING - email\_address: STRING - fax: STRING - name: STRING - phone\_number: STRING - state: STRING - title: STRING - zip: STRING |
| **billing**  OBJECT This is a nested data structure:   - billing\_charges: ARRAY, which is also a nested data structure.   - charge\_type: INTEGER   - details: ARRAY, which is also a nested data structure.     - charge\_label: STRING     - charge\_per\_unit: NUMBER     - gl\_acct\_num: STRING     - num\_units: NUMBER     - pt\_ar\_acct: STRING     - pt\_item: STRING     - pt\_item\_description: STRING     - sku: STRING     - system\_generated: BOOLEAN     - unit\_description: STRING     - warehouse\_transaction\_price\_calc\_id: INTEGER   - subtotal: NUMBER |
| **billing\_code**  STRING |
| **created\_by\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **creation\_date**  DATE-TIME |
| **customer\_identifier**  OBJECT This is a nested data structure:   - external\_id: STRING - id: INTEGER - name: STRING |
| **defer\_notification**  BOOLEAN |
| **description**  STRING |
| **earliest\_ship\_date**  DATE-TIME |
| **export\_channel\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **export\_module\_ids**  STRING |
| **external\_id**  STRING |
| **facility\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **fulfill\_inv\_info**  OBJECT This is a nested data structure:   - fulfill\_inv\_amount: NUMBER - fulfill\_inv\_discount\_code: STRING - fulfill\_inv\_message: STRING - fulfill\_inv\_shipping\_and\_handling: NUMBER - fulfill\_inv\_tax: NUMBER |
| **fully\_allocated**  BOOLEAN |
| **import\_channel\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **invoice\_delivered\_date**  DATE-TIME |
| **invoice\_exported\_date**  DATE-TIME |
| **invoice\_number**  STRING |
| **is\_closed**  BOOLEAN |
| **labels\_exported**  BOOLEAN |
| **last\_modified\_by\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **last\_modified\_date**  DATE-TIME |
| **load\_out\_done\_date**  DATE-TIME |
| **loaded\_state**  INTEGER |
| **master\_billing\_of\_lading\_id**  STRING |
| **notes**  STRING |
| **num\_units**  NUMBER |
| **order\_id**  INTEGER |
| **order\_items**  ARRAY This is a nested data structure:   - expiration\_date: DATE-TIME - external\_id: STRING - fulfill\_inv\_discount\_amt: NUMBER - fulfill\_inv\_discount\_pct: NUMBER - fulfill\_inv\_note: STRING - fulfill\_inv\_sale\_price: NUMBER - item\_identifier: OBJECT, which is also a nested data structure.   - id: INTEGER   - sku: STRING - lot\_number: STRING - notes: STRING - order\_item\_packages: ARRAY, which is also a nested data structure.   - package\_number: INTEGER   - quantity: NUMBER - proposed\_allocations: ARRAY, which is also a nested data structure.   - qty: NUMBER   - receive\_item\_id: INTEGER - qty: NUMBER - qualifier: STRING - read\_only: OBJECT, which is also a nested data structure.   - allocations: ARRAY, which is also a nested data structure.     - detail: OBJECT, which is also a nested data structure.       - expiration\_date: DATE-TIME       - item\_traits: OBJECT, which is also a nested data structure.         - id: INTEGER         - sku: STRING       - location\_identifier: OBJECT, which is also a nested data structure.         - id: INTEGER         - name\_key: OBJECT, which is also a nested data structure.           - facility\_identifier: OBJECT, which is also a nested data structure.             - id: INTEGER             - name: STRING           - name: STRING       - lot\_number: STRING       - pallet\_identifier: OBJECT, which is also a nested data structure.         - id: INTEGER         - name\_key: OBJECT, which is also a nested data structure.           - facility\_identifier: OBJECT, which is also a nested data structure.             - id: INTEGER             - name: STRING           - name: STRING       - qualifier: STRING       - serial\_number: STRING     - loaded\_out: BOOLEAN     - properly\_picked\_primary: NUMBER     - properly\_picked\_secondary: NUMBER     - qty: NUMBER     - receive\_item\_id: INTEGER   - estimated\_qty: NUMBER   - estimated\_secondary\_qty: NUMBER   - full\_allocated: BOOLEAN   - is\_order\_qty\_secondary: BOOLEAN   - order\_item\_id: INTEGER   - pick\_exceptions: ARRAY, which is also a nested data structure.     - expiration\_date: DATE-TIME     - location\_id: INTEGER     - lot\_number: STRING     - order\_id: INTEGER     - order\_item\_id: INTEGER     - order\_item\_pick\_exception\_id: INTEGER     - picked\_primary\_qty: NUMBER     - picked\_secondary\_qty: NUMBER     - reason: STRING     - receive\_item\_id: INTEGER     - serial\_number: STRING   - secondary\_unit\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING   - unit\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING - saved\_elements: ARRAY, which is also a nested data structure.   - name: STRING   - value: STRING - secondary\_qty: NUMBER - serial\_number: STRING - weight\_imperial: NUMBER - weight\_metric: NUMBER |
| **outbound\_serial\_numbers**  ARRAY This is a nested data structure:   - item\_identifier: OBJECT, which is also a nested data structure.   - id: INTEGER   - sku: STRING - qualifier: STRING - serial\_numbers: ARRAY, which is also a nested data structure. |
| **pack\_done\_date**  DATE-TIME |
| **packages**  ARRAY This is a nested data structure:   - cod: BOOLEAN - cod\_amount: NUMBER - create\_date: DATE-TIME - description: STRING - height: NUMBER - insured\_amount: NUMBER - label: STRING - length: NUMBER - oversize: BOOLEAN - package\_contents: ARRAY, which is also a nested data structure.   - create\_date: DATE-TIME   - expiration\_date: DATE-TIME   - lot\_number: STRING   - order\_item\_id: INTEGER   - order\_item\_pick\_exception\_id: INTEGER   - package\_content\_id: INTEGER   - package\_id: INTEGER   - qty: NUMBER   - receive\_item\_id: INTEGER   - serial\_number: STRING   - serial\_numbers: ARRAY, which is also a nested data structure. - package\_id: INTEGER - package\_type\_id: INTEGER - tracking\_number: STRING - ucc128: INTEGER - weight: NUMBER - width: NUMBER |
| **parcel\_label\_type**  INTEGER |
| **pick\_done\_date**  DATE-TIME |
| **pick\_ticket\_print\_date**  DATE-TIME |
| **pkgs\_exported**  BOOLEAN |
| **po\_num**  STRING |
| **process\_date**  DATE-TIME |
| **reallocated\_after\_pick\_ticket\_date**  DATE-TIME |
| **reference\_num**  STRING |
| **route\_candidate**  INTEGER |
| **route\_pickup\_date**  DATE-TIME |
| **route\_sent**  BOOLEAN |
| **routing\_info**  OBJECT This is a nested data structure:   - account: STRING - bill\_of\_lading: STRING - capacity\_identifier: OBJECT, which is also a nested data structure.   - id: INTEGER   - name: STRING - carrier: STRING - door\_number: STRING - is\_cod: BOOLEAN - is\_insurance: BOOLEAN - load\_number: STRING - mode: STRING - pickup\_date: DATE-TIME - required\_delivery\_conf: BOOLEAN - required\_return\_receipt: BOOLEAN - scac\_code: STRING - seal\_number: STRING - ship\_point\_zip: STRING - tracking\_number: STRING - trailer\_number: STRING |
| **saved\_elements**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **ship\_cancel\_date**  DATE-TIME |
| **ship\_to**  OBJECT This is a nested data structure:   - address1: STRING - address2: STRING - address\_status: STRING - city: STRING - code: STRING - company\_name: STRING - contact\_id: INTEGER - country: STRING - dept: STRING - email\_address: STRING - fax: STRING - is\_quick\_lookup: BOOLEAN - name: STRING - phone\_number: STRING - retailer\_id: INTEGER - retailer\_info: OBJECT, which is also a nested data structure.   - id: INTEGER   - name\_key: OBJECT, which is also a nested data structure.     - customer\_identifier: OBJECT, which is also a nested data structure.       - external\_id: STRING       - id: INTEGER       - name: STRING     - name: STRING     - number: STRING - same\_as: INTEGER - state: STRING - title: STRING - zip: STRING |
| **shipping\_notes**  STRING |
| **sold\_to**  OBJECT This is a nested data structure:   - address1: STRING - address2: STRING - address\_status: STRING - city: STRING - code: STRING - company\_name: STRING - contact\_id: INTEGER - country: STRING - dept: STRING - email\_address: STRING - fax: STRING - is\_quick\_lookup: BOOLEAN - name: STRING - phone\_number: STRING - retailer\_id: INTEGER - same\_as: INTEGER - state: STRING - title: STRING - zip: STRING |
| **status**  INTEGER |
| **total\_volume**  NUMBER |
| **total\_weight**  NUMBER |
| **transaction\_entry\_type**  INTEGER |
| **unit2\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **up\_service\_option\_charge**  NUMBER |
| **up\_transportation\_charge**  NUMBER |
| **ups\_is\_residential**  NUMBER |
| **warehouse\_transaction\_source\_type**  INTEGER |

### sku\_items

This table contains information about SKU items.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | item\_id |
| **Replication Key** | last\_modified\_date |
| **Useful links** | [3PL Central documentation](http://api.3plcentral.com/rels/)  [3PL Central API method](http://api.3plcentral.com/rels/customers/items "Opens in new tab: 3PL Central API method") |

sku\_items table foreign keys

| Join sku\_items with | on |
| --- | --- |
| [customers](#customers) | ``` sku_items.customer_id = customers.customer_id ```  ``` sku_items.customer_identifier.id = customers.customer_id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = customers.facilities.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = customers.primary_facility_identifier.id ``` |
| [stock\_details](#stock-details) | ``` sku_items.customer_id = stock_details.customer_id ```  ``` sku_items.customer_identifier.id = stock_details.customer_id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = stock_details.pallet_identifier.name_key.facility_identifier.id ```  ``` sku_items.item_id = stock_details.item_identifier.id ```  ``` sku_items.kit.components.item_identifier.id = stock_details.item_identifier.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.id = stock_details.location_identifier.id ``` |
| [inventory](#inventory) | ``` sku_items.customer_id = inventory.customer_identifier.id ```  ``` sku_items.customer_identifier.id = inventory.customer_identifier.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = inventory.facility_identifier.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = inventory.location_identifier.name_key.facility_identifier.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = inventory.pallet_identifier.name_key.facility_identifier.id ```  ``` sku_items.item_id = inventory.item_identifier.id ```  ``` sku_items.kit.components.item_identifier.id = inventory.item_identifier.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.id = inventory.location_identifier.id ``` |
| [locations](#locations) | ``` sku_items.customer_id = locations.customer_identifier.id ```  ``` sku_items.customer_identifier.id = locations.customer_identifier.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = locations.facility_id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = locations.item_traits.pallet_identifier.name_key.facility_identifier.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = locations.location_identifier.name_key.facility_identifier.id ```  ``` sku_items.item_id = locations.item_traits.item_identifier.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.id = locations.location_id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.id = locations.location_identifier.id ``` |
| [orders](#orders) | ``` sku_items.customer_id = orders.customer_identifier.id ```  ``` sku_items.customer_identifier.id = orders.customer_identifier.id ```  ``` sku_items.customer_id = orders.batch_identifier.name_key.customer_identifier.id ```  ``` sku_items.customer_identifier.id = orders.batch_identifier.name_key.customer_identifier.id ```  ``` sku_items.customer_id = orders.ship_to.retailer_info.name_key.customer_identifier.id ```  ``` sku_items.customer_identifier.id = orders.ship_to.retailer_info.name_key.customer_identifier.id ```  ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = orders.facility_identifier.id ``` |
| [stock\_summaries](#stock-summaries) | ``` sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id = stock_summaries.facility_id ```  ``` sku_items.item_id = stock_summaries.item_id ``` |

sku\_items table schema

|  |
| --- |
| **account\_ref**  STRING |
| **classification\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **cost**  NUMBER |
| **country\_of\_manufacture**  STRING |
| **creation\_date**  DATE-TIME |
| **customer\_id**  INTEGER |
| **customer\_identifier**  OBJECT This is a nested data structure:   - external\_d: STRING - id: INTEGER - name: STRING |
| **deactivated**  BOOLEAN |
| **description**  STRING |
| **description2**  STRING |
| **harmonized\_code**  STRING |
| **inventory\_category**  STRING |
| **item**  ARRAY This is a nested data structure:   - qualifier: STRING |
| **item\_id**  INTEGER |
| **kit**  OBJECT This is a nested data structure:   - components: ARRAY, which is also a nested data structure.   - item\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - sku: STRING   - non\_sku\_material: STRING   - qty: NUMBER   - qualifier: STRING - material\_notes: STRING |
| **last\_modified\_date**  DATE-TIME |
| **last\_price\_change**  DATE-TIME |
| **nmfc**  STRING |
| **options**  OBJECT This is a nested data structure:   - auto\_hold\_on\_receive: INTEGER - days\_between\_counts: INTEGER - directed\_put\_away: OBJECT, which is also a nested data structure.   - allow\_mixed\_item\_storage: BOOLEAN   - allow\_mixed\_lot\_storage: BOOLEAN   - force\_into\_preferred\_location: BOOLEAN   - location\_zones: STRING   - mixed\_expiration\_days\_threshold: BOOLEAN   - over\_alloc\_location\_zones: STRING   - pallet\_location\_zones: STRING   - preferred\_location\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name\_key: OBJECT, which is also a nested data structure.       - facility\_identifier: OBJECT, which is also a nested data structure.         - id: INTEGER         - name: STRING       - name: STRING - haz\_mat: OBJECT, which is also a nested data structure.   - flag: STRING   - flash\_point: STRING   - hazard\_class: STRING   - id: INTEGER   - is\_haz\_mat: BOOLEAN   - label\_code: STRING   - packing\_group: STRING   - shipping\_name: STRING - inventory\_unit: OBJECT, which is also a nested data structure.   - inventory\_method: INTEGER   - maximum\_stock: NUMBER   - minimum\_stock: NUMBER   - reorder\_quantity: NUMBER   - unit\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING - package\_unit: OBJECT, which is also a nested data structure.   - imperial: OBJECT, which is also a nested data structure.     - height: NUMBER     - length: NUMBER     - net\_weight: NUMBER     - weight: NUMBER     - width: NUMBER   - metric: OBJECT, which is also a nested data structure.     - height: NUMBER     - length: NUMBER     - net\_weight: NUMBER     - weight: NUMBER     - width: NUMBER   - unit\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING   - upc: STRING - pallets: OBJECT, which is also a nested data structure.   - high: NUMBER   - imperial: OBJECT, which is also a nested data structure.     - height: NUMBER     - length: NUMBER     - weight: NUMBER     - width: NUMBER   - metric: OBJECT, which is also a nested data structure.     - height: NUMBER     - length: NUMBER     - weight: NUMBER     - width: NUMBER   - qyt: NUMBER   - tie: NUMBER   - type\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING   - upc: STRING - secondary\_unit: OBJECT, which is also a nested data structure.   - inventory\_also: BOOLEAN   - inventory\_units\_per\_unit: NUMBER   - unit\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING - track\_by: OBJECT, which is also a nested data structure.   - auto\_hold\_expiration\_days\_threshold: INTEGER   - outbound\_mobile\_serialization: INTEGER   - track\_cost: INTEGER   - track\_expiration\_date: INTEGER   - track\_lot\_number: INTEGER   - track\_serial\_number: INTEGER |
| **price**  NUMBER |
| **qualifier\_renamers**  ARRAY This is a nested data structure:   - qualifier: STRING - rename: STRING |
| **sku**  STRING |
| **temperature**  NUMBER |
| **upc**  STRING |

### stock\_details

This table contains information about stock details.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | receive\_item\_id |
| **Useful links** | [3PL Central documentation](http://api.3plcentral.com/rels/)  [3PL Central API method](http://api.3plcentral.com/rels/inventory/stockdetails "Opens in new tab: 3PL Central API method") |

stock\_details table foreign keys

| Join stock\_details with | on |
| --- | --- |
| [customers](#customers) | ``` stock_details.customer_id = customers.customer_id ```  ``` stock_details.location_identifier.name_key.facility_identifier.id = customers.facilities.id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = customers.facilities.id ```  ``` stock_details.location_identifier.name_key.facility_identifier.id = customers.primary_facility_identifier.id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = customers.primary_facility_identifier.id ``` |
| [sku\_items](#sku-items) | ``` stock_details.customer_id = sku_items.customer_id ```  ``` stock_details.customer_id = sku_items.customer_identifier.id ```  ``` stock_details.location_identifier.name_key.facility_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ```  ``` stock_details.item_identifier.id = sku_items.item_id ```  ``` stock_details.item_identifier.id = sku_items.kit.components.item_identifier.id ```  ``` stock_details.location_identifier.id = sku_items.options.directed_put_away.preferred_location_identifier.id ``` |
| [inventory](#inventory) | ``` stock_details.customer_id = inventory.customer_identifier.id ```  ``` stock_details.location_identifier.name_key.facility_identifier.id = inventory.facility_identifier.id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = inventory.facility_identifier.id ```  ``` stock_details.location_identifier.name_key.facility_identifier.id = inventory.location_identifier.name_key.facility_identifier.id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = inventory.location_identifier.name_key.facility_identifier.id ```  ``` stock_details.location_identifier.name_key.facility_identifier.id = inventory.pallet_identifier.name_key.facility_identifier.id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = inventory.pallet_identifier.name_key.facility_identifier.id ```  ``` stock_details.item_identifier.id = inventory.item_identifier.id ```  ``` stock_details.location_identifier.id = inventory.location_identifier.id ```  ``` stock_details.pallet_identifier.id = inventory.pallet_identifier.id ```  ``` stock_details.receiver_id = inventory.receiver_id ```  ``` stock_details.receive_item_id = inventory.receive_item_id ```  ``` stock_details.supplier_identifier.id = inventory.supplier_identifier.id ``` |
| [locations](#locations) | ``` stock_details.customer_id = locations.customer_identifier.id ```  ``` stock_details.location_identifier.name_key.facility_identifier.id = locations.facility_id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = locations.facility_id ```  ``` stock_details.location_identifier.name_key.facility_identifier.id = locations.item_traits.pallet_identifier.name_key.facility_identifier.id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = locations.item_traits.pallet_identifier.name_key.facility_identifier.id ```  ``` stock_details.location_identifier.name_key.facility_identifier.id = locations.location_identifier.name_key.facility_identifier.id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = locations.location_identifier.name_key.facility_identifier.id ```  ``` stock_details.location_identifier.id = locations.location_id ```  ``` stock_details.location_identifier.id = locations.location_identifier.id ```  ``` stock_details.pallet_identifier.id = locations.item_traits.pallet_identifier.id ``` |
| [orders](#orders) | ``` stock_details.customer_id = orders.customer_identifier.id ```  ``` stock_details.customer_id = orders.batch_identifier.name_key.customer_identifier.id ```  ``` stock_details.customer_id = orders.ship_to.retailer_info.name_key.customer_identifier.id ```  ``` stock_details.location_identifier.name_key.facility_identifier.id = orders.facility_identifier.id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = orders.facility_identifier.id ``` |
| [stock\_summaries](#stock-summaries) | ``` stock_details.location_identifier.name_key.facility_identifier.id = stock_summaries.facility_id ```  ``` stock_details.pallet_identifier.name_key.facility_identifier.id = stock_summaries.facility_id ``` |

stock\_details table schema

|  |
| --- |
| **available**  NUMBER |
| **cost**  NUMBER |
| **customer\_id**  INTEGER |
| **description**  STRING |
| **expiration\_date**  DATE-TIME |
| **inventory\_unit\_of\_measure\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - sku: STRING |
| **is\_on\_hold**  BOOLEAN |
| **item\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - sku: STRING |
| **location\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name\_key: OBJECT, which is also a nested data structure.   - facility\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING   - name: STRING |
| **lot\_number**  STRING |
| **on\_hand**  NUMBER |
| **pallet\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name\_key: OBJECT, which is also a nested data structure.   - facility\_identifier: OBJECT, which is also a nested data structure.     - id: INTEGER     - name: STRING   - name: STRING |
| **po\_num**  STRING |
| **qualifier**  STRING |
| **quarantined**  BOOLEAN |
| **receive\_item\_id**  INTEGER |
| **received**  NUMBER |
| **received\_date**  DATE-TIME |
| **receiver\_id**  INTEGER |
| **reference\_num**  STRING |
| **saved\_elements**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **serial\_number**  STRING |
| **supplier\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **trailer\_number**  STRING |

### stock\_summaries

This table contains information about stock summaries.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | facility\_id  item\_id |
| **Useful links** | [3PL Central documentation](http://api.3plcentral.com/rels/)  [3PL Central API method](http://api.3plcentral.com/rels/inventory/stocksummaries "Opens in new tab: 3PL Central API method") |

stock\_summaries table foreign keys

| Join stock\_summaries with | on |
| --- | --- |
| [customers](#customers) | ``` stock_summaries.facility_id = customers.facilities.id ```  ``` stock_summaries.facility_id = customers.primary_facility_identifier.id ``` |
| [inventory](#inventory) | ``` stock_summaries.facility_id = inventory.facility_identifier.id ```  ``` stock_summaries.facility_id = inventory.location_identifier.name_key.facility_identifier.id ```  ``` stock_summaries.facility_id = inventory.pallet_identifier.name_key.facility_identifier.id ``` |
| [locations](#locations) | ``` stock_summaries.facility_id = locations.facility_id ```  ``` stock_summaries.facility_id = locations.item_traits.pallet_identifier.name_key.facility_identifier.id ```  ``` stock_summaries.facility_id = locations.location_identifier.name_key.facility_identifier.id ```  ``` stock_summaries.item_id = locations.item_traits.item_identifier.id ``` |
| [orders](#orders) | ``` stock_summaries.facility_id = orders.facility_identifier.id ``` |
| [sku\_items](#sku-items) | ``` stock_summaries.facility_id = sku_items.options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id ```  ``` stock_summaries.item_id = sku_items.item_id ``` |
| [stock\_details](#stock-details) | ``` stock_summaries.facility_id = stock_details.location_identifier.name_key.facility_identifier.id ```  ``` stock_summaries.facility_id = stock_details.pallet_identifier.name_key.facility_identifier.id ``` |

stock\_summaries table schema

|  |
| --- |
| **allocated**  NUMBER |
| **available**  NUMBER |
| **facility\_id**  INTEGER |
| **item\_id**  INTEGER |
| **item\_identifier**  OBJECT This is a nested data structure:   - id: INTEGER - sku: STRING |
| **on\_hand**  NUMBER |
| **on\_hold**  NUMBER |
| **qualifier**  STRING |
| **total\_received**  NUMBER |
