---
title: "Navigating datasets in the catalog"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/navigation-datasets-catalog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Understanding your data with catalog tools"]
---

# Navigating datasets in the catalog

When opening a dataset from Catalog, you can access many details, benefit from several data quality indicators and look into the data itself. This information is organized into tabs. The dataset header provides key information and actions you can do with your dataset.

Information note

Depending on your subscription, the following capabilities might be available when accessing a dataset from the catalog:

- Data quality

  [*Assessing data quality*](../DataIntegration/DataProducts/Data-quality-and-data-discovery.htm)
- Data freshness

  [*Data freshness*](../DataIntegration/DataProducts/Data-freshness.htm)
- Qlik Trust Score™

  [*Qlik Trust Score™*](../DataIntegration/DataProducts/Qlik-Trust-score.htm)

In particular, the following subscriptions allow access to one or more of these capabilities:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

## Dataset header

Dataset displays the selected dataset and key metadata. You can view the following information in the dataset header:

- File type
- Number of rows
- Number of fields
- File size

Dataset header

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dataset-header.png "Click to view full size")

The dataset header provides options for different actions you can take with the dataset. The following actions are available from the dataset header:

- Compute/ Refresh: Refresh your dataset profile and metadata.
- Use in: You can create analytics content from the dataset.
- Add to favorites (![Add to favorites icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_star_2.svg))/ Remove from favorites (![Remove from favorites icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_star.svg)): You can add or remove the dataset to your favorites.

Additionally, the following actions are available from the ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu:

- Add to Collection: Collections are organizations of objects in [activity centers](#glossary-0 "Glossary term"). Select this option to:

- Search for a [collection](#glossary-1 "Glossary term")
- Create collection
- Add to a collection

- Apply validation rule: See [*Working with validation rules*](../DataIntegration/DataProducts/Working-with-validation-rules.htm).
- Edit: Select to edit Name, Description, or Tags.

  Information noteUpdating the Name of a dataset does not change the name of the underlying data file. Instead, it creates an alias for the dataset. This can be useful for datasets that are only accessed using catalog tools. However, this action can cause the name of the data file and its dataset to become out of sync, which can cause confusion if the file is used in analytics development. For more information, see [*Distinctions between data files and datasets*](data-files-and-datasets.htm).
- Lineage: See [*Analyzing lineage in Analytics*](lineage.htm)
- Impact analysis: See [*Analyzing impact analysis in Analytics*](impact-analysis2.htm)
- File format settings: See [*Uploading datasets and editing file format settings*](file-format-settings.htm)

## Dataset tabs

Dataset is organized into the following tabs:

- Overview
- Profile
- Data preview
- Lineage
- Impact analysis

### Overview

In the Overview tab, you can get general details about your dataset such as the connection it is based on, its description, when the data was last refreshed, and more importantly, data quality indicators.

Overview tab

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_catalog_overview.png "Click to view full size")

### Profile

The Profile tab contains graphical representations of your data. The type of visualization or histogram depends on the data type, and you can get statistics and information on the values for each field of your dataset. For more information, see [*Managing field-level metadata and data profiling*](Profiling-data.htm).

Profile tab

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_catalog_profile.png "Click to view full size")

By default, all datasets aside from QVD and Parquet files are profiled automatically. QVD and Parquet files must be manually profiled.

### Data preview

In Data preview, you can look at the data itself in the form of a preview.

Data preview tab

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_catalog_data_preview.png "Click to view full size")

### Lineage

The Lineage tab offers a visual representation of the origin of the data contained in the dataset, such as the source table, and the data pipeline used to import it. See [*Analyzing lineage in Analytics*](lineage.htm) for more information.

Lineage tab

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_catalog_lineage.png "Click to view full size")

### Impact analysis

The impact analysis of a dataset allows you to see the applications or data products that use this dataset and that will be impacted if you edit or delete it. See [*Analyzing impact analysis in Analytics*](impact-analysis2.htm) for more information.

Impact analysis tab

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_catalog_impact_analysis.png "Click to view full size")
