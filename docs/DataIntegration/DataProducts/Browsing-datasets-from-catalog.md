---
title: "Browsing datasets from the Catalog"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Browsing-datasets-from-catalog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog"]
---

# Browsing datasets from the Catalog

From the left menu of the Qlik Talend Data Integration homepage, you can access the Catalog page. This is your tool to explore all the assets you have access to in your available spaces.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

![Overview of the Catalog page in Qlik Talend Data Integration](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/catalog-overview-2.png)

Using filters, you will be able to browse and look for trusted datasets to use in data products. Datasets can be the result of a manual upload, or created from a pipeline project when using the Publish to catalog option. For more information on publishing to Catalog, see [*Data pipeline project settings*](../Introduction/Data-project-settings.htm).

When opening a dataset from your Catalog, you can access many details, benefit from several data quality indicators and look into the data itself. This information is organized in multiple tabs.

Information noteA Qlik Cloud Analytics connection is required to compute the quality and profiling of your datasets. For more information, see [*Data quality for connection-based datasets*](Data-quality-connections.htm)

## Overview

In the Overview tab, you can get general details about your dataset as well as data quality indicators:

- On top of the page, you can see an editable description, the data quality calculated on this dataset, or the data freshness.

  You can generate the dataset description using an AI. For more information, see [Generating an AI-based dataset description](Generating-AI-based-description.htm).

  The Freshness time expresses the last update of the data source. For more information, see [*Configuring data quality*](Configuring-data-quality.htm) and [*Data freshness*](Data-freshness.htm).
- At the center of the page, you can see:

  - The global Qlik Trust Score™ for the selected datasets and a percentage representing their healthiness. For more information, see [*Qlik Trust Score™*](Qlik-Trust-score.htm).
  - An overview of the validation rules applied to the dataset. Only the four rules with the most negative impact on the quality are displayed. The impact mostly depends on the severity of the rules. For more information, see [*Working with validation rules*](Working-with-validation-rules.htm).
  - An overview of the dataset schema. For more information, see [*Managing semantic types*](Managing-semantic-types.htm).
- On the bottom right side of the page, you can see the number of dependencies (Analytics applications, data flows, etc.) based on this dataset in the Used in tile, and the number of views and visitors in the View activity tile.
- On the right panel, you can see general information about the dataset source such as the connection it is based on, the [*Data spaces*](../DataSpaces/data-space.htm), the tags used, the dataset creation and update dates, the dataset owner and creator.

For more information on data quality, see [*Assessing data quality*](Data-quality-and-data-discovery.htm).

![Overview tab of a dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dataset_overview_ts.png)

## Profile

The Profile tab contains graphical representations of your data. The type of visualization or histogram depends on the data type, and you can get statistics and information on the repartition of values for each field of your dataset. See [*Managing field-level metadata and data profiling*](../../Catalog/Profiling-data.htm) for more information.

![Profile tab of a dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dataset_profile.png)

## Data preview

You can look at the data itself in the form of a sample. For each column, you can see the data type, and the number of valid and invalid values is visible in a quality bar. Invalid values are also highlighted across the dataset.

![Data preview tab of a dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dataset-preview.png)

## Lineage

The Lineage tab offers a visual representation of the origin of the data contained in the dataset, such as the source table, and the data pipeline used to import it. See [*Analyzing lineage in Analytics*](../../Catalog/lineage.htm) for more information.

![Lineage tab of a dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dataset-lineage_.png)

## Impact analysis

The impact analysis of a dataset allows you to see the apps or data products that use this dataset and that will be impacted if you edit or delete it. See [*Analyzing impact analysis in Analytics*](../../Catalog/impact-analysis2.htm) for more information.

![Impact analysis tab of a dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dataset-impact-analysis.png)

## Validation rules

In the Validation rules tab, you can see all the validation rules applied to the dataset. For more information, see [*Working with validation rules*](Working-with-validation-rules.htm).

From this tab, you can also edit the rules, activate or deactivate them, and remove them from the dataset.

![Validation rules tab of a dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dataset-validation-rules.png)

## Data contract

The Data contract tab shows the status of the quality expectations defined for the dataset. You can review the status of each expectation and configure thresholds, warning ranges for applicable quality metrics, and notifications. The volume expectation uses a record range and does not support warning ranges. For more information, see [*Managing data contracts*](Managing-data-contracts.htm).

![Data contract tab of a dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/data-contract-overview.png)
