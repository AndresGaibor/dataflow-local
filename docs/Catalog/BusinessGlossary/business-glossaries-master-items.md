---
title: "Linking terms to master items"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/BusinessGlossary/business-glossaries-master-items.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with business glossaries"]
---

# Linking terms to master items

Link terms in your business glossary to master items in apps.

You can link master dimensions and master measures to terms in your business glossary. This brings the business glossary into apps and can help users better understand different dimensions and measures. For example, in managed spaces, users creating their own sheets only have access to master items. Linked terms can help provide context and clarity over the meaning and use of master dimensions and measures for these users.

Any user with Can edit or greater permissions in the app can link master items to terms in the glossary. A single term can be linked to the master item as the definition. Multiple terms can be linked to a master item as related terms.

When a term is linked to a master item, the master items are visible under Linked resources in the business glossary.

## Viewing master items and linked terms

To view the master items with linked terms, a user must have Can view or greater permission in the space with the source business glossary.

In a sheet in analysis mode, you can view master items and their linked terms in Details in visualizations using those master items. Click ![Show details](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) on a visualization using the master item to open Details. Hovering the cursor over the term shows the definition of the term. Clicking on the term opens the business glossary entry for the term.

Linked master item in Detail

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_businessGlossary_master_measure_details.png "Click to view full size")

In edit mode, you can view the associated terms by opening Master items and clicking on the master item.

Linked term in a sheet in edit mode

![The master measure Gross margin open showing the term for gross margin from the glossary.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_businessGlossary_master_measure.png "Click to view full size")

## Linked terms in published apps in managed spaces

When an app is published to a managed space, the linked terms and definitions are included. You cannot link terms to master items in apps already published in a managed space.

Users must have at least Can view access to the space the business glossary is in to view the terms. Users clicking to see the term in the business glossary need Can view access in the shared space containing the business glossary.

As a best practice, to ensure all users can access a business glossary, place the business glossary in a shared space where all tenant users have Can view access.

## Linking existing glossary terms to master items

Do the following:

1. In an open master item, after Glossary terms, click ![Add glossary term link](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg).

   The term selection pane opens. By default, it will search for a term using the master item name.
2. Select a term.
3. Select the relationship between the term and the master item:

   - Definition: The term contains the definition of the master item. Only a single term can be set as the definition.
   - Related: The term is related to the master item. Multiple terms can be set as related terms.
4. Click Select.

## Linking new glossary terms to master items

Do the following:

1. In an open master item, after Glossary terms, click ![Add glossary term link](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg).
2. Click ![Create new term](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) Create new term.

   The new term will use the master item name and description in the Name and Description fields.
3. Under Select glossary, select the glossary to which to add the term.
4. Click Create to create the term and continue with linking the term to the master item.

   Alternatively, to close your app and open the glossary, click Create and open in glossary to open the term in the glossary for additional configuration.
5. Select your new term.
6. Select the relationship between the term and the master item:

   - Definition: The term contains the definition of the master item. Only a single term can be set as the definition.
   - Related: The term is related to the master item. Multiple terms can be set as related terms.
7. Click Select.
