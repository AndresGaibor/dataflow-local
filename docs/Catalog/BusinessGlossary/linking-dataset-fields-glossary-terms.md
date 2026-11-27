---
title: "Linking dataset fields to business glossary terms"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/BusinessGlossary/linking-dataset-fields-glossary-terms.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with business glossaries"]
---

# Linking dataset fields to business glossary terms

Link a dataset field to a term in your business glossary to bring standardized business definitions into dataset profiling and preview.

You can link a field (column) in a dataset to a term in your business glossary. This helps data analysts and business users understand the business meaning of a field without leaving the dataset profile or data preview. You can link a field to an existing glossary term, or create a new term directly from the field.

You link a field to a term from the field Details panel, which opens to the right of the grid in the Profile tab or the Data preview tab of a dataset. For more information on opening the Details panel for a field, see [*Managing field-level metadata and data profiling*](../Profiling-data.htm).

![linking a dataset field to a glossary term](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/glossary_link_term.png)

Information note

Linking a field to a glossary term requires the same permissions as editing other field-level metadata (Field alias, Description, Tags, and Classification). You must have the Update role in the dataset's space.

Information note

If you only have read-only (Can view) access to the dataset, you can still see glossary terms already linked to a field, but the link is read-only: you cannot add, change, or remove it.

## Viewing linked terms

Open a field's Details panel to see whether a glossary term is linked to that field. If a term is linked, its name and definition display under Glossary terms in the panel. Click the term name to open the full term entry in the business glossary.

When a term is linked to a dataset field, the field is visible under Linked resources on that term in the business glossary. For more information, see [*Navigating business glossaries*](navigating-business-glossaries.htm).

## Linking an existing glossary term to a dataset field

Do the following:

1. In the dataset Profile tab or Data preview tab, select a field to open its Details panel.
2. After Glossary terms, click ![Add glossary term link](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg).

   The term selection pane opens. By default, it searches for a term using the field name.
3. Select a term.
4. Click Select.

## Linking a new glossary term to a dataset field

Do the following:

1. In the dataset Profile tab or Data preview tab, select a field to open its Details panel.
2. After Glossary terms, click ![Add glossary term link](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg).
3. Click ![Create new term](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) Create new term.

   ![Creating a new term](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/glossary_select_create_term.png) Use the edit icon to modify the term if needed.

   The new term uses the field name and description in the Name and Description fields.
4. Under Select glossary, select the glossary to which to add the term.
5. Click Create to create the term and continue with linking the term to the field.
6. Select your new term.
7. Click Select.
