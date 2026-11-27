---
title: "Creating a data model"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Create-data-model.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse"]
---

# Creating a data model

You can create relationships between the datasets that are included in a Storage or Transform data task to create a data model. The data model can be used by a data mart to automate code generation for denormalization of dimensions and fact tables.

- Click Model to open the data model view.

You can get recommendations for relationships, or add your own relationships.

## Using recommended relationships

You can get recommendation for relationships to create, based on primary keys and column names in the datasets.

1. Click ![Associate icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_associate.svg).

   You will see a list of recommended relationships. You can expand each relationship to inspect the suggested columns used to relate the datasets.

   Tip note

   You can also click Include AI recommendations to generate recommendations based on metadata using Generative AI.

   For more information about availability and information that is shared, see [*Generative AI-based assistant in Data Integration*](../../Admin/mc-manage-DI-features.htm#Generati).

   Govnote-not-inNot supported in Qlik Cloud Government.

   Information note

   To use AI model recommendations, you must opt in to cross-region inference. This allows Qlik Cloud to send inference requests outside your tenant region.

   For details and the latest information about inference processing locations, see [*Enabling cross-region inference*](../../Admin/cross-region-data-processing.htm).
2. Select the recommended relationships that you want to use.

   The model view is updated with dotted lines to indicate the relationships that will be created.
3. Click Apply to create the relationships.

   The lines in the model view become solid to indicate that the relationships is created.

## Adding relationships

You can also add relationships manually, if they are not included in the recommended relationships.

1. Click Add relationship.
2. Select a child dataset, and a parent dataset.

   You will see recommended relationships based on the primary keys of the parent data set.
3. You can adjust the columns selections for the child dataset.

   You can also adjust the name of the relationship.

   When you are ready, click OK to create the relationship.

## Editing relationships

1. Click ![Tile view icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid.svg) to go to the tile view.
2. Click ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a relationship and select Edit.
3. You can now edit the relationship settings.

   Click OK when you are ready.

## Deleting relationships

There are two ways to delete a relationship.

- In tile view (![Tile view icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid.svg)), click ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a relationship and select Delete.
- In model view (![Data model icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_data_model.svg)), click ![Delete icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cross.svg) on the relationship to delete.

Information noteDeleting a relationship can affect downstream data assets.

## Limitations

- Circular relationships are not supported. If you get warnings about this, consider consolidating the two datasets into one.
- The attributes used to relate two datasets must have the same data type. If they have different data types they are not ensured to be converted automatically, which may cause a runtime error when using this relationship later.
