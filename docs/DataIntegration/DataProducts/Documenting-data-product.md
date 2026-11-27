---
title: "Documenting a data product"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Documenting-data-product.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Working with data products"]
---

# Documenting a data product

You can find two types of documentation for each of your data products.

- The general documentation that recaps your data product such as the datasets, the data freshness, the data quality, semantic models, etc.
- The Read me section that contains all the info the data product manager wants to share about the data product.

If your data product includes a semantic model, the generated documentation includes information about the tables, relationships, measures, and dimensions defined in the semantic model.

You can also add key contacts to your data products and attach business glossaries to make standardized business definitions available to consumers.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

Information noteYou need the permission to manage data products.

## Generating the general documentation of a data product

You can generate, view, and download the documentation of a data product to collect all the information about it in one file such as the data quality, the number of datasets, the quality of each dataset, the fields of each dataset, etc.

Generating the general documentation of a data product can also be performed through the corresponding [Qlik Public API](https://qlik.dev/apis/rest/data-governance/data-products/#get-api-data-governance-data-products-dataProductId-actions-export-documentation).

You can download the documentation in markdown format (`.md`).

When a dataset in the data product is in a space to which you do not have access, you can still generate and download the documentation but the dataset and its data will not be included in the documentation.

1. Open the data product from the Catalog or Data products menu.
2. On the right, click ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) > Get documentation. The Documentation window opens.
3. To download in MD format, click Download.

   You can also download in PDF format from your browser. Right-click the documentation > Print....

## Editing the read me section

As a data product manager, you can edit the Read me section as much as needed. The rich text format allows you to structure the section to make it as clear as possible.

1. Make sure you have the following roles or permissions:
   - The Data Product Manager role or the Manage data products permission.
   - The permission to edit the space.
2. Open the data product from the Catalog or Data products menu.
3. Select the Documentation tab.
4. Click Edit in the Read me section.
5. Enter the information and click Save.

You can also edit the Read me section by clicking ![Edit button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/di_edit_button.png) > Documentation on the right.

## Adding key contacts

Add key contacts to specify who consumers can contact for any questions or issues with the data product.

1. Make sure you have the following roles or permissions:
   - The Data Product Manager role or the Manage data products permission.
   - The permission to edit the space.
2. Open the data product from the Catalog or Data products menu.
3. Select the Documentation tab.
4. Click Edit in the Contacts section.
5. Enter the key contacts and click Save.

You can also edit the key contacts by clicking ![Edit button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/di_edit_button.png) > Documentation > Key contacts on the right.

## Viewing attached business glossaries

Data products can include attached business glossaries that provide standardized business definitions for the data product contents. Glossaries are displayed in the Documentation tab alongside the Read me section and key contacts.

### As a data product manager

You can view and manage attached glossaries:

1. Open the data product from the Catalog or Data products menu.
2. Select the Documentation tab.
3. Scroll to the Glossaries section to see attached glossaries.
4. Click Edit to add, replace, or remove glossaries. For detailed instructions, see [*Adding business glossaries to a data product*](Adding-business-glossaries.htm).

### As a data product consumer

You can view business glossaries attached to data products you have access to:

1. Open the data product from the Catalog.
2. Select the Documentation tab.
3. View the Glossaries section to see business definitions relevant to the data product.

Only glossaries you have read access to are displayed. If you cannot see a glossary in the Documentation tab, contact your administrator or the data product manager to request access.
