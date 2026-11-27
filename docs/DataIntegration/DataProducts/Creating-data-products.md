---
title: "Creating data products"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Creating-data-products.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Working with data products"]
---

# Creating data products

Trusted datasets that have been created as a result of a data project or that you have manually uploaded, can be grouped and packaged in the form of a data product, to make it easier to consume in analytics applications.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

Information noteYou need the permission to manage data products.

## Creating a data product

The first step is to create a new empty data product.

Creating a data product can also be performed through the corresponding [Qlik Public API](https://qlik.dev/apis/rest/data-governance/data-products/#post-api-data-governance-data-products).

1. From the launcher menu ![Launcher menu icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg), select  Data products.
2. Click the Create new button.

   The New data product dialog opens
3. In the corresponding field, enter a Name for your data product.
4. From the corresponding drop-down list, select in which Space you want to save the data product.
5. Add a Description to document the purpose of the data product.
6. Add some Tags to the data product to make it easier to find.
7. Optionally select the Open data product check box to view the data product once it’s created.
8. Click Continue.

The data product has been created and is empty for now. Edit it to start adding datasets.

After creation, the data product view includes tabs such as Overview, Semantic model, and Documentation.

## Adding datasets to a data product

If you need to add datasets to an empty data product or update the current content, you can do that with the Edit menu.

Information noteTo add and remove datasets, you need the permission to edit the data product.

1. From the launcher menu ![Launcher menu icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg), select Catalog, or Data products.
2. Click the empty data product to which you want to add datasets.
3. Click the Edit button.
4. Using the Next and Previous navigation buttons, you can review or edit the configuration of your data product in the following pages:

1. General, where you can update the Name, Space, Description, and Tags.
2. Datasets. Click Add datasets to open the list of all the datasets that you have access to from your Catalog and select the ones you want to include using the check boxes. Click Confirm to resume the data product configuration with your selection.

   ![Selecting datasets to add in the data product](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/data_product_dataset_selection-2.png)

   If the data product you are editing already contains datasets, click the Edit button to update your selection.
3. Documentation, where you can add or edit Read me information, if you want to give more context on the data product, or give specific instructions on how to consume it for example. You can also enter one or more Key contact using the Add button, so that users know who they can reach for questions related to this data product.
4. Glossaries, where you can select business glossaries to attach to your data product. Attached glossaries provide standardized business definitions for data product consumers. For step-by-step instructions, see [*Adding business glossaries to a data product*](Adding-business-glossaries.htm).

5. Click Save.

Your data product now contains datasets and is well documented. You can look at several quality indicators, like the validity and completeness of the whole data product, as well as the quality of each individual dataset. It is now ready to be used as source for an analytics application, or to be made available more widely in your organization via the data marketplace.

## Creating a semantic model (optional)

After adding datasets to your data product, you can optionally create a semantic model to define relationships, measures, and dimensions that Analytics developers can reuse in their applications.

To create a semantic model:

1. In the data product view, click the Semantic model tab.
2. Click Create semantic model.
3. Add tables from your datasets, define relationships, and create measures and dimensions.
4. Save the semantic model.

For detailed instructions on creating and managing semantic models, see [*Managing semantic models in data products*](managing-semantic-models.htm).

## Data product changelog

All edits and updates made to a data product, such as adding or removing datasets, or adding documentation, are tracked in a changelog available in Data products.

1. Click the three dots menu icon of a data product.
2. From the menu, select Changelog.

![Changelog of the data product](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/data-product-changelog.png)

You can see a timeline showing what edits were made, by whom, and when.
