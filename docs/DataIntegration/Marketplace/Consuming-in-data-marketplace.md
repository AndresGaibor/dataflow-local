---
title: "Activating data products to the data marketplace"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Marketplace/Consuming-in-data-marketplace.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Working with data products"]
---

# Activating data products to the data marketplace

All the data products that you have access to via spaces are visible in your Catalog view. To make the certified and trusted data products available more widely to your organization, they need to be activated on the Data marketplace.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

## What is data product activation?

When you activate a data product, it is copied into a managed space and at the same time it is made available in the Data Marketplace. The copy in the managed space is read-only.

## Activating a data product to the data marketplace

Information noteYou need the permission to manage data products.

Activating a data product to the data marketplace can also be performed through the corresponding [Qlik Public API](https://qlik.dev/apis/rest/data-governance/data-products/#post-api-data-governance-data-products-dataProductId-actions-activate).

1. From the launcher menu ![Launcher menu icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg), select Data products.
2. Click the data product you want to activate.
3. Click Activate.

   The Activate data product dialog opens.

   ![Data product activation menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/activate-data-product.png)
4. From the Sharing policy drop-down list, select a managed space in which the data product will be published.

   Activating a data product on the data marketplace actually publishes a copy in the managed space that you select during activation. So all users that are part of this managed space will see the activated data product both in their catalog and in the data marketplace.
5. In the Names, Description, and Tags fields, review or edit the information entered during the data product creation.
6. After looking at the Preview, click Activate.

The data product has now an active version on the data marketplace. As the owner of the data product, you will see in your catalog both the main data product, and the published copy.

When browsing the data marketplace, you will see the main data products in their original spaces.

## Deactivating a data product

Information noteYou need the permission to manage data products.

When you want to update a data product or if it's no longer relevant, you need to deactivate it.

Deactivating a data product can also be performed through the corresponding [Qlik Public API](https://qlik.dev/apis/rest/data-governance/data-products/#post-api-data-governance-data-products-dataProductId-actions-deactivate).

1. From Data products, click the data product to deactivate.
2. Click the three dots menu icon on the top right of the data product.
3. Click Deactivate.
4. In the confirmation dialog that opens, click Deactivate again.

Even if your data product has been used as source for one or more analytics applications, you can safely deactivate it and the application will still work.

## Updating an active data product

When you edit a data product that is activated to a managed space, your changes are not automatically published to the marketplace. The changes remain in your main data product until you update the marketplace copy.

Updating a data product can also be performed through the corresponding [Qlik Public API](https://qlik.dev/apis/rest/data-governance/data-products/#patch-api-data-governance-data-products-dataProductId).

To update the marketplace copy:

1. Edit the data product as needed.
2. See [*Updating the data product in the marketplace*](Updating-the-marketplace.htm) for instructions to update the marketplace.

The marketplace copy remains stable and read-only until you republish. Any existing applications based on the data product continue to work with the previous version until you update the marketplace copy.

## Consuming a data product

When you have found a data product with the data that corresponds to your needs, you can directly create an analytics application from it. You can customize your selection, choosing which components from the data product's semantic model to integrate into your application. For more information, see [*Consuming data products in applications*](../DataProducts/consuming-data-products-apps.htm).

Alternatively, you can consume the data product through APIs. For more information about the API endpoints, see [*Consuming data products through APIs*](../DataProducts/Consuming-data-products-through-apis.htm).
