---
title: "Pepperjam"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Pepperjam.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Pepperjam

Pepperjam is an affiliate marketing solutions provider that powers growth for marketers seeking a scaled alternative to their primary sales and marketing channels.

Pepperjam integration replicates data using the [Pepperjam Advertiser API v20120402](https://ascendpartner.zendesk.com/hc/en-gb/articles/13501008650909-API-Overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Pepperjam has been rebranded as Ascend by Partnerize.

To retrieve your API key:

1. Log into your [Ascend](https://console.partnerize.com/login/partnerize/en) account.
2. Click the Resources tab.

   An additional drop-down menu appears.
3. Click API Keys > Generate New Key.
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

### creative\_advanced

The `creative_advanced` table contains information about advanced link creatives in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#AdvancedLinks "Opens in new tab: Pepperjam API method") |

creative\_advanced table foreign keys

| Join creative\_advanced with | on |
| --- | --- |
| [creative\_banner](#creative-banner) | ``` creative_advanced.private_affiliates.affiliate_id = creative_banner.private_affiliates.affiliate_id ```  ``` creative_advanced.promotions.id = creative_banner.promotions.id ``` |
| [creative\_coupon](#creative-coupon) | ``` creative_advanced.private_affiliates.affiliate_id = creative_coupon.private_affiliates.affiliate_id ```  ``` creative_advanced.promotions.id = creative_coupon.promotions.id ``` |
| [creative\_text](#creative-text) | ``` creative_advanced.private_affiliates.affiliate_id = creative_text.private_affiliates.affiliate_id ```  ``` creative_advanced.promotions.id = creative_text.promotions.id ``` |
| [creative\_promotion](#creative-promotion) | ``` creative_advanced.promotions.id = creative_promotion.id ``` |

creative\_advanced table schema

|  |
| --- |
| **code**  STRING |
| **created**  DATE-TIME |
| **description**  STRING |
| **end\_date**  DATE-TIME |
| **flash\_url**  STRING |
| **id**  INTEGER |
| **modified**  DATE-TIME |
| **name**  STRING |
| **personalized**  INTEGER |
| **private**  INTEGER |
| **private\_affiliates**  ARRAY This is a nested data structure:   - affiliate\_id: INTEGER - first\_name: STRING - last\_name: STRING |
| **promotions**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING |
| **start\_date**  DATE-TIME |
| **status**  STRING |
| **sub\_type**  STRING |
| **supression\_url**  STRING |
| **type**  STRING |
| **verified**  STRING |
| **view\_date**  DATE-TIME |

### creative\_banner

The `creative_banner` table contains information about banner creatives in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#Banner "Opens in new tab: Pepperjam API method") |

creative\_banner table foreign keys

| Join creative\_banner with | on |
| --- | --- |
| [creative\_advanced](#creative-advanced) | ``` creative_banner.private_affiliates.affiliate_id = creative_advanced.private_affiliates.affiliate_id ```  ``` creative_banner.promotions.id = creative_advanced.promotions.id ``` |
| [creative\_coupon](#creative-coupon) | ``` creative_banner.private_affiliates.affiliate_id = creative_coupon.private_affiliates.affiliate_id ```  ``` creative_banner.promotions.id = creative_coupon.promotions.id ``` |
| [creative\_text](#creative-text) | ``` creative_banner.private_affiliates.affiliate_id = creative_text.private_affiliates.affiliate_id ```  ``` creative_banner.promotions.id = creative_text.promotions.id ``` |
| [creative\_promotion](#creative-promotion) | ``` creative_banner.promotions.id = creative_promotion.id ``` |

creative\_banner table schema

|  |
| --- |
| **allow\_deep\_link**  INTEGER |
| **alt\_text**  STRING |
| **banner\_url**  STRING |
| **created**  DATE-TIME |
| **description**  STRING |
| **destination\_url**  STRING |
| **end\_date**  DATE-TIME |
| **height**  INTEGER |
| **id**  INTEGER |
| **modified**  DATE-TIME |
| **name**  STRING |
| **private**  INTEGER |
| **private\_affiliates**  ARRAY This is a nested data structure:   - affiliate\_id: INTEGER - first\_name: STRING - last\_name: STRING |
| **promotions**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING |
| **start\_date**  DATE-TIME |
| **status**  STRING |
| **type**  STRING |
| **view\_date**  DATE-TIME |
| **width**  INTEGER |

### creative\_coupon

The `creative_coupon` table contains information about coupon creatives in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#CouponCreative "Opens in new tab: Pepperjam API method") |

creative\_coupon table foreign keys

| Join creative\_coupon with | on |
| --- | --- |
| [creative\_advanced](#creative-advanced) | ``` creative_coupon.private_affiliates.affiliate_id = creative_advanced.private_affiliates.affiliate_id ```  ``` creative_coupon.promotions.id = creative_advanced.promotions.id ``` |
| [creative\_banner](#creative-banner) | ``` creative_coupon.private_affiliates.affiliate_id = creative_banner.private_affiliates.affiliate_id ```  ``` creative_coupon.promotions.id = creative_banner.promotions.id ``` |
| [creative\_text](#creative-text) | ``` creative_coupon.private_affiliates.affiliate_id = creative_text.private_affiliates.affiliate_id ```  ``` creative_coupon.promotions.id = creative_text.promotions.id ``` |
| [creative\_promotion](#creative-promotion) | ``` creative_coupon.promotions.id = creative_promotion.id ``` |

creative\_coupon table schema

|  |
| --- |
| **coupon\_code**  STRING |
| **created**  DATE-TIME |
| **description**  STRING |
| **end\_date**  DATE-TIME |
| **id**  INTEGER |
| **modified**  DATE-TIME |
| **name**  STRING |
| **personalized**  INTEGER |
| **private**  INTEGER |
| **private\_affiliates**  ARRAY This is a nested data structure:   - affiliate\_id: INTEGER - first\_name: STRING - last\_name: STRING |
| **promotions**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING  Click to expand promotions |  | | --- | | **id**  INTEGER | | **name**  STRING | |
| **start\_date**  DATE-TIME |
| **status**  STRING |
| **type**  STRING |
| **url**  STRING |
| **view\_date**  DATE-TIME |

### creative\_generic

The `creative_generic` table contains information about generic link creatives in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | type |
| **Replication Key** | modified |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#Generic "Opens in new tab: Pepperjam API method") |

creative\_generic table foreign keys

| Join creative\_generic with | on |
| --- | --- |
| [creative\_performance](#creative-performance) | ``` creative_generic.type = creative_performance.creative_type ``` |
| [creative\_performance\_by\_publisher](#creative-performance-by-publisher) | ``` creative_generic.type = creative_performance_by_publisher.creative_type ``` |

creative\_generic table schema

|  |
| --- |
| **allow\_deep\_link**  INTEGER |
| **modified**  DATE-TIME |
| **type**  STRING |
| **url**  STRING |

### creative\_performance

The `creative_performance` table contains information about your Pepperjam creatives’ performance within a -day time frame from the date of the last table replication.

**Note**: During every replication job, Stitch will replicate the last days’ worth of data for this table. Refer to the [Attribution windows and data extraction](#attribution-windows-data-extraction) section for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | creative\_id  creative\_type  date |
| **Replication Key** | datetime |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#CreativeDetails "Opens in new tab: Pepperjam API method") |

creative\_performance table foreign keys

| Join creative\_performance with | on |
| --- | --- |
| [creative\_performance\_by\_publisher](#creative-performance-by-publisher) | ``` creative_performance.creative_id = creative_performance_by_publisher.creative_id ```  ``` creative_performance.group_id = creative_performance_by_publisher.group_id ```  ``` creative_performance.creative_type = creative_performance_by_publisher.creative_type ``` |
| [transaction\_details](#transaction-details) | ``` creative_performance.creative_id = transaction_details.creative_id ```  ``` creative_performance.group_id = transaction_details.group_id ``` |
| [group](#group) | ``` creative_performance.group_id = group.id ``` |
| [group\_member](#group-member) | ``` creative_performance.group_id = group_member.group_id ``` |
| [publisher](#publisher) | ``` creative_performance.group_id = publisher.group.id ``` |
| [publisher\_performance](#publisher-performance) | ``` creative_performance.group_id = publisher_performance.group_id ``` |
| [transaction\_history](#transaction-history) | ``` creative_performance.group_id = transaction_history.group_id ``` |
| [creative\_generic](#creative-generic) | ``` creative_performance.creative_type = creative_generic.type ``` |

creative\_performance table schema

|  |
| --- |
| **affiliate\_usage**  INTEGER |
| **click\_through\_rate**  NUMBER |
| **clicks**  INTEGER |
| **commission**  NUMBER |
| **creative\_id**  INTEGER |
| **creative\_name**  STRING |
| **creative\_type**  STRING |
| **date**  DATE |
| **datetime**  DATE-TIME |
| **earnings\_per\_click**  NUMBER |
| **group\_id**  INTEGER |
| **impressions**  INTEGER |
| **items**  INTEGER |
| **sales**  NUMBER |
| **transactions**  INTEGER |

### creative\_performance\_by\_publisher

The `creative_performance_by_publisher` table contains information about your Pepperjam creatives’ performance, per publisher, within a -day time frame from the date of the last table replication.

**Note**: During every replication job, Stitch will replicate the last days’ worth of data for this table. Refer to the [Attribution windows and data extraction](#attribution-windows-data-extraction) section for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | creative\_id  creative\_type  date  publisher\_id |
| **Replication Key** | datetime |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#CreativePerformanceByPublisher "Opens in new tab: Pepperjam API method") |

creative\_performance\_by\_publisher table foreign keys

| Join creative\_performance\_by\_publisher with | on |
| --- | --- |
| [creative\_performance](#creative-performance) | ``` creative_performance_by_publisher.creative_id = creative_performance.creative_id ```  ``` creative_performance_by_publisher.group_id = creative_performance.group_id ```  ``` creative_performance_by_publisher.creative_type = creative_performance.creative_type ``` |
| [transaction\_details](#transaction-details) | ``` creative_performance_by_publisher.creative_id = transaction_details.creative_id ```  ``` creative_performance_by_publisher.group_id = transaction_details.group_id ```  ``` creative_performance_by_publisher.publisher_id = transaction_details.publisher_id ``` |
| [group](#group) | ``` creative_performance_by_publisher.group_id = group.id ``` |
| [group\_member](#group-member) | ``` creative_performance_by_publisher.group_id = group_member.group_id ``` |
| [publisher](#publisher) | ``` creative_performance_by_publisher.group_id = publisher.group.id ```  ``` creative_performance_by_publisher.publisher_id = publisher.id ``` |
| [publisher\_performance](#publisher-performance) | ``` creative_performance_by_publisher.group_id = publisher_performance.group_id ```  ``` creative_performance_by_publisher.publisher_id = publisher_performance.publisher_id ``` |
| [transaction\_history](#transaction-history) | ``` creative_performance_by_publisher.group_id = transaction_history.group_id ```  ``` creative_performance_by_publisher.publisher_id = transaction_history.publisher_id ``` |
| [creative\_generic](#creative-generic) | ``` creative_performance_by_publisher.creative_type = creative_generic.type ``` |

creative\_performance\_by\_publisher table schema

|  |
| --- |
| **affiliate\_usage**  INTEGER |
| **click\_through\_rate**  NUMBER |
| **clicks**  INTEGER |
| **commission**  NUMBER |
| **creative\_id**  INTEGER |
| **creative\_name**  STRING |
| **creative\_type**  STRING |
| **date**  DATE |
| **datetime**  DATE-TIME |
| **earnings\_per\_click**  NUMBER |
| **group\_id**  INTEGER |
| **impressions**  INTEGER |
| **items**  INTEGER |
| **publisher**  STRING |
| **publisher\_id**  INTEGER |
| **sales**  NUMBER |
| **transactions**  INTEGER |

### creative\_product

The `creative_product` table contains information about product creatives in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#ProductCreative "Opens in new tab: Pepperjam API method") |

creative\_product table schema

|  |
| --- |
| **age\_range**  STRING |
| **artist**  STRING |
| **aspect\_ratio**  STRING |
| **author**  STRING |
| **battery\_life**  STRING |
| **binding**  STRING |
| **buy\_url**  STRING |
| **category\_network**  STRING |
| **category\_program**  STRING |
| **color**  STRING |
| **color\_output**  STRING |
| **condition**  STRING |
| **description\_long**  STRING |
| **description\_short**  STRING |
| **director**  STRING |
| **discontinued**  STRING |
| **display\_type**  STRING |
| **edition**  STRING |
| **expiration\_date**  STRING |
| **features**  STRING |
| **focus\_type**  STRING |
| **functions**  STRING |
| **genre**  STRING |
| **heel\_height**  STRING |
| **height**  STRING |
| **id**  INTEGER |
| **image\_thumb\_url**  STRING |
| **image\_url**  STRING |
| **in\_stock**  STRING |
| **installation**  STRING |
| **isbn**  STRING |
| **keywords**  STRING |
| **length**  STRING |
| **load\_type**  STRING |
| **location**  STRING |
| **made\_in**  STRING |
| **manufacturer**  STRING |
| **material**  STRING |
| **megapixels**  STRING |
| **memory\_capacity**  STRING |
| **memory\_card\_slot**  STRING |
| **memory\_type**  STRING |
| **model\_number**  STRING |
| **mpn**  STRING |
| **name**  STRING |
| **occasion**  STRING |
| **operating\_system**  STRING |
| **optical\_drive**  STRING |
| **pages**  INTEGER |
| **payment\_accepted**  STRING |
| **payment\_notes**  STRING |
| **platform**  STRING |
| **price**  NUMBER |
| **price\_retail**  NUMBER |
| **price\_sale**  NUMBER |
| **price\_shipping**  NUMBER |
| **processor**  STRING |
| **product\_format**  STRING |
| **publisher**  STRING |
| **quantity\_in\_stock**  INTEGER |
| **rating**  STRING |
| **recommended\_usage**  STRING |
| **resolution**  STRING |
| **screen\_size**  STRING |
| **shipping\_method**  STRING |
| **shoe\_size**  STRING |
| **shoe\_width**  STRING |
| **size**  STRING |
| **sku**  STRING |
| **staring**  STRING |
| **style**  STRING |
| **tech\_spec\_url**  STRING |
| **tracks**  INTEGER |
| **upc**  STRING |
| **weight**  STRING |
| **width**  STRING |
| **wireless\_interface**  STRING |
| **year**  STRING |
| **zoom**  STRING |

### creative\_promotion

The `creative_promotion` table contains information about promotion creatives in your Pepperjam name account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#CreativePromotion "Opens in new tab: Pepperjam API method") |

creative\_promotion table foreign keys

| Join creative\_promotion with | on |
| --- | --- |
| [creative\_advanced](#creative-advanced) | ``` creative_promotion.id = creative_advanced.promotions.id ``` |
| [creative\_banner](#creative-banner) | ``` creative_promotion.id = creative_banner.promotions.id ``` |
| [creative\_coupon](#creative-coupon) | ``` creative_promotion.id = creative_coupon.promotions.id ``` |
| [creative\_text](#creative-text) | ``` creative_promotion.id = creative_text.promotions.id ``` |

creative\_promotion table schema

|  |
| --- |
| **id**  STRING |
| **name**  STRING |

### creative\_text

The creative\_text table contains information about text creatives in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#Text "Opens in new tab: Pepperjam API method") |

creative\_text table foreign keys

| Join creative\_text with | on |
| --- | --- |
| [creative\_advanced](#creative-advanced) | ``` creative_text.private_affiliates.affiliate_id = creative_advanced.private_affiliates.affiliate_id ```  ``` creative_text.promotions.id = creative_advanced.promotions.id ``` |
| [creative\_banner](#creative-banner) | ``` creative_text.private_affiliates.affiliate_id = creative_banner.private_affiliates.affiliate_id ```  ``` creative_text.promotions.id = creative_banner.promotions.id ``` |
| [creative\_coupon](#creative-coupon) | ``` creative_text.private_affiliates.affiliate_id = creative_coupon.private_affiliates.affiliate_id ```  ``` creative_text.promotions.id = creative_coupon.promotions.id ``` |
| [creative\_promotion](#creative-promotion) | ``` creative_text.promotions.id = creative_promotion.id ``` |

creative\_text table schema

|  |
| --- |
| **allow\_deep\_link**  INTEGER |
| **created**  DATE-TIME |
| **description**  STRING |
| **end\_date**  DATE-TIME |
| **id**  INTEGER |
| **link\_anchor\_text**  STRING |
| **modified**  DATE-TIME |
| **private**  INTEGER |
| **private\_affiliates**  ARRAY This is a nested data structure:   - affiliate\_id: INTEGER - first\_name: STRING - last\_name: STRING |
| **promotions**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING |
| **start\_date**  DATE-TIME |
| **status**  STRING |
| **type**  STRING |
| **url**  STRING |
| **view\_date**  DATE-TIME |

### group

The `group` table contains information about groups in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#Group "Opens in new tab: Pepperjam API method") |

group table foreign keys

| Join group with | on |
| --- | --- |
| [creative\_performance](#creative-performance) | ``` group.id = creative_performance.group_id ``` |
| [creative\_performance\_by\_publisher](#creative-performance-by-publisher) | ``` group.id = creative_performance_by_publisher.group_id ``` |
| [group\_member](#group-member) | ``` group.id = group_member.group_id ``` |
| [publisher](#publisher) | ``` group.id = publisher.group.id ``` |
| [publisher\_performance](#publisher-performance) | ``` group.id = publisher_performance.group_id ``` |
| [transaction\_details](#transaction-details) | ``` group.id = transaction_details.group_id ``` |
| [transaction\_history](#transaction-history) | ``` group.id = transaction_history.group_id ``` |

group table schema

|  |
| --- |
| **assigned\_publishers**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |

### group\_member

The `group_member` table contains information about members within groups in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#Member "Opens in new tab: Pepperjam API method") |

group\_member table foreign keys

| Join group\_member with | on |
| --- | --- |
| [creative\_performance](#creative-performance) | ``` group_member.group_id = creative_performance.group_id ``` |
| [creative\_performance\_by\_publisher](#creative-performance-by-publisher) | ``` group_member.group_id = creative_performance_by_publisher.group_id ``` |
| [group](#group) | ``` group_member.group_id = group.id ``` |
| [publisher](#publisher) | ``` group_member.group_id = publisher.group.id ``` |
| [publisher\_performance](#publisher-performance) | ``` group_member.group_id = publisher_performance.group_id ``` |
| [transaction\_details](#transaction-details) | ``` group_member.group_id = transaction_details.group_id ``` |
| [transaction\_history](#transaction-history) | ``` group_member.group_id = transaction_history.group_id ``` |

group\_member table schema

|  |
| --- |
| **default**  STRING |
| **group\_id**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **product\_count**  INTEGER |

### itemized\_list

The `itemized_list` table contains information about your itemized lists in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#ItemizedList "Opens in new tab: Pepperjam API method") |

itemized\_list table foreign keys

| Join itemized\_list with | on |
| --- | --- |
| [itemized\_list\_product](#itemized-list-product) | ``` itemized_list.id = itemized_list_product.list_id ``` |

itemized\_list table schema

|  |
| --- |
| **default**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **product\_count**  INTEGER |

### itemized\_list\_product

The `itemized_list_product` table contains information about products within your itemized lists in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#Product "Opens in new tab: Pepperjam API method") |

itemized\_list\_product table foreign keys

| Join itemized\_list\_product with | on |
| --- | --- |
| [itemized\_list](#itemized-list) | ``` itemized_list_product.list_id = itemized_list.id ``` |

itemized\_list\_product table schema

|  |
| --- |
| **id**  STRING |
| **list\_id**  INTEGER |
| **name**  STRING |

### publisher

The `publisher` table contains information about the publishers, the publishers’ status, and the publishers’ term in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#Publisher "Opens in new tab: Pepperjam API method") |

publisher table foreign keys

| Join publisher with | on |
| --- | --- |
| [creative\_performance](#creative-performance) | ``` publisher.group.id = creative_performance.group_id ``` |
| [creative\_performance\_by\_publisher](#creative-performance-by-publisher) | ``` publisher.group.id = creative_performance_by_publisher.group_id ```  ``` publisher.id = creative_performance_by_publisher.publisher_id ``` |
| [group](#group) | ``` publisher.group.id = group.id ``` |
| [group\_member](#group-member) | ``` publisher.group.id = group_member.group_id ``` |
| [publisher\_performance](#publisher-performance) | ``` publisher.group.id = publisher_performance.group_id ```  ``` publisher.id = publisher_performance.publisher_id ``` |
| [transaction\_details](#transaction-details) | ``` publisher.group.id = transaction_details.group_id ```  ``` publisher.id = transaction_details.publisher_id ``` |
| [transaction\_history](#transaction-history) | ``` publisher.group.id = transaction_history.group_id ```  ``` publisher.id = transaction_history.publisher_id ``` |
| [term](#term) | ``` publisher.term.id = term.id ``` |

publisher table schema

|  |
| --- |
| **category**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING |
| **company**  STRING |
| **country**  STRING |
| **first\_name**  STRING |
| **group**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING |
| **id**  INTEGER |
| **join\_date**  DATE-TIME |
| **last\_name**  STRING |
| **primary\_promo\_method**  STRING |
| **promotional\_method**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING |
| **request\_date**  DATE-TIME |
| **state**  STRING |
| **status**  STRING |
| **term**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING |
| **transparency**  INTEGER |
| **website**  STRING |

### publisher\_performance

The `publisher_performance` table contains information about publishers’ performance within a -day time frame from the date of the last table replication.

**Note**: During every replication job, Stitch will replicate the last days’ worth of data for this table. Refer to the [Attribution windows and data extraction](#attribution-windows-data-extraction) section for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | date  publisher\_id |
| **Replication Key** | datetime |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#PublisherPerformance "Opens in new tab: Pepperjam API method") |

publisher\_performance table foreign keys

| Join publisher\_performance with | on |
| --- | --- |
| [creative\_performance](#creative-performance) | ``` publisher_performance.group_id = creative_performance.group_id ``` |
| [creative\_performance\_by\_publisher](#creative-performance-by-publisher) | ``` publisher_performance.group_id = creative_performance_by_publisher.group_id ```  ``` publisher_performance.publisher_id = creative_performance_by_publisher.publisher_id ``` |
| [group](#group) | ``` publisher_performance.group_id = group.id ``` |
| [group\_member](#group-member) | ``` publisher_performance.group_id = group_member.group_id ``` |
| [publisher](#publisher) | ``` publisher_performance.group_id = publisher.group.id ```  ``` publisher_performance.publisher_id = publisher.id ``` |
| [transaction\_details](#transaction-details) | ``` publisher_performance.group_id = transaction_details.group_id ```  ``` publisher_performance.publisher_id = transaction_details.publisher_id ``` |
| [transaction\_history](#transaction-history) | ``` publisher_performance.group_id = transaction_history.group_id ```  ``` publisher_performance.publisher_id = transaction_history.publisher_id ``` |

publisher\_performance table schema

|  |
| --- |
| **bonus\_amount**  NUMBER |
| **clicks**  INTEGER |
| **company**  STRING |
| **date**  DATE |
| **datetime**  DATE-TIME |
| **earnings\_per\_click**  NUMBER |
| **group\_id**  INTEGER |
| **impressions**  INTEGER |
| **leads**  INTEGER |
| **publisher**  STRING |
| **publisher\_bonus**  NUMBER |
| **publisher\_commission**  NUMBER |
| **publisher\_id**  INTEGER |
| **publisher\_type**  STRING |
| **sale\_lead\_amount**  NUMBER |
| **sales**  INTEGER |
| **site\_bonus**  NUMBER |
| **site\_commission**  NUMBER |
| **state**  STRING |
| **total\_commission**  NUMBER |
| **website**  STRING |

### term

The `term` table contains information about the terms for your program in your Pepperjam account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#Term "Opens in new tab: Pepperjam API method") |

term table foreign keys

| Join term with | on |
| --- | --- |
| [publisher](#publisher) | ``` term.id = publisher.term.id ``` |

term table schema

|  |
| --- |
| **cookie\_duration**  STRING |
| **created**  DATE |
| **default**  STRING |
| **id**  INTEGER |
| **name**  STRING |

### transaction\_details

The transaction\_details table contains all publisher transaction details, within a -day time frame from the date of the last table replication.

**Note**: During every replication job, Stitch will replicate the last days’ worth of data for this table. Refer to the [Attribution windows and data extraction](#attribution-windows-data-extraction) section for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | transaction\_id |
| **Replication Key** | sale\_date |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#TransactionDetails "Opens in new tab: Pepperjam API method") |

transaction\_details table foreign keys

| Join transaction\_details with | on |
| --- | --- |
| [creative\_performance](#creative-performance) | ``` transaction_details.creative_id = creative_performance.creative_id ```  ``` transaction_details.group_id = creative_performance.group_id ``` |
| [creative\_performance\_by\_publisher](#creative-performance-by-publisher) | ``` transaction_details.creative_id = creative_performance_by_publisher.creative_id ```  ``` transaction_details.group_id = creative_performance_by_publisher.group_id ```  ``` transaction_details.publisher_id = creative_performance_by_publisher.publisher_id ``` |
| [group](#group) | ``` transaction_details.group_id = group.id ``` |
| [group\_member](#group-member) | ``` transaction_details.group_id = group_member.group_id ``` |
| [publisher](#publisher) | ``` transaction_details.group_id = publisher.group.id ```  ``` transaction_details.publisher_id = publisher.id ``` |
| [publisher\_performance](#publisher-performance) | ``` transaction_details.group_id = publisher_performance.group_id ```  ``` transaction_details.publisher_id = publisher_performance.publisher_id ``` |
| [transaction\_history](#transaction-history) | ``` transaction_details.group_id = transaction_history.group_id ```  ``` transaction_details.order_id = transaction_history.order_id ```  ``` transaction_details.publisher_id = transaction_history.publisher_id ```  ``` transaction_details.transaction_id = transaction_history.transaction_id ``` |

transaction\_details table schema

|  |
| --- |
| **click\_id**  STRING |
| **commission**  NUMBER |
| **commission\_publisher**  NUMBER |
| **commission\_site**  NUMBER |
| **company**  STRING |
| **coupons**  STRING |
| **creative\_id**  STRING |
| **device\_type**  STRING |
| **group\_id**  INTEGER |
| **link\_type**  STRING |
| **new\_to\_file**  STRING |
| **order\_id**  STRING |
| **publisher**  STRING |
| **publisher\_id**  INTEGER |
| **publisher\_type**  STRING |
| **sale\_amount**  NUMBER |
| **sale\_date**  DATE-TIME |
| **status**  STRING |
| **transaction\_id**  INTEGER |
| **transaction\_type**  STRING |

### transaction\_history

The transaction\_history table contains all historical publisher transactions, within a -day time frame from the date of the last table replication.

**Note**: During every replication job, Stitch will replicate the last days’ worth of data for this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | transaction\_id  process\_date  sale\_date |
| **Replication Key** | sale\_date |
| **Useful links** | [Pepperjam API method](https://support.pepperjam.com/s/advertiser-api-documentation#TransactionHistory "Opens in new tab: Pepperjam API method") |

transaction\_history table foreign keys

| Join transaction\_history with | on |
| --- | --- |
| [creative\_performance](#creative-performance) | ``` transaction_history.group_id = creative_performance.group_id ``` |
| [creative\_performance\_by\_publisher](#creative-performance-by-publisher) | ``` transaction_history.group_id = creative_performance_by_publisher.group_id ```  ``` transaction_history.publisher_id = creative_performance_by_publisher.publisher_id ``` |
| [group](#group) | ``` transaction_history.group_id = group.id ``` |
| [group\_member](#group-member) | ``` transaction_history.group_id = group_member.group_id ``` |
| [publisher](#publisher) | ``` transaction_history.group_id = publisher.group.id ```  ``` transaction_history.publisher_id = publisher.id ``` |
| [publisher\_performance](#publisher-performance) | ``` transaction_history.group_id = publisher_performance.group_id ```  ``` transaction_history.publisher_id = publisher_performance.publisher_id ``` |
| [transaction\_details](#transaction-details) | ``` transaction_history.group_id = transaction_details.group_id ```  ``` transaction_history.order_id = transaction_details.order_id ```  ``` transaction_history.publisher_id = transaction_details.publisher_id ```  ``` transaction_history.transaction_id = transaction_details.transaction_id ``` |

transaction\_history table schema

|  |
| --- |
| **commission**  NUMBER |
| **company**  STRING |
| **group\_id**  INTEGER |
| **item\_id**  STRING |
| **link\_type**  STRING |
| **order\_id**  STRING |
| **process\_date**  DATE-TIME |
| **publisher**  STRING |
| **publisher\_commission**  NUMBER |
| **publisher\_id**  INTEGER |
| **publisher\_type**  STRING |
| **revision**  STRING |
| **sale\_amount**  NUMBER |
| **sale\_date**  DATE-TIME |
| **site\_commission**  NUMBER |
| **status**  STRING |
| **transaction\_id**  INTEGER |
| **transaction\_type**  STRING |
| **website\_url**  STRING |
