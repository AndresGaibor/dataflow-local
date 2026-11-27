---
title: "Qlik Trust Score™"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Qlik-Trust-score.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog"]
---

# Qlik Trust Score™

The Qlik Trust Score™ helps you answer the question "How trustable is my dataset?". This global quality indicator aggregates several metrics into a single and easy-to-understand score, providing visibility not only on the healthiness of individual datasets, but also at the data product level.

The overall Qlik Trust Score™ for a data product is the average of the trust scores of all included datasets, including datasets that are not visible, allowing you to assess and monitor data quality across your entire data landscape.

The Qlik Trust Score™ can be tailored according to the data quality needs of your company, and give you visibility on the healthiness of any dataset or data product.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

## Overview

From a dataset overview, you can find the Qlik Trust Score™, and comprehensive insights such as:

- The global Qlik Trust Score™ for the selected datasets and a percentage or 5-point rating indicating their healthiness.
- The different factors that can raise or lower the Qlik Trust Score™ of a dataset. They are regrouped under these main dimensions:

  - Validity, that assesses the quality of the dataset itself, including the use of semantic types and the applied validation rules, and reflects the proportion of valid values across the dataset sample. Empty values are not considered as valid in the calculation of this dimension.
  - Completeness, that depends on the number of empty records in the dataset sample.
  - Discoverability, that measures how easily users can find and understand your dataset through its metadata, directly impacting adoption rates.

    It takes into account the fact that this dataset is referenced in activated data products, and reflects how well-documented your dataset is. A well-documented dataset uses proper metadata such as descriptions or tags, both on the dataset itself and on the dataset fields.
  - Usage, that shows how much your dataset is used across dependencies such as Analytics applications, data preparations, data flows, etc. It also takes into account the number of views these dependencies have.

    Information noteIf there is no score displayed for this dimension, ensure that usage metrics are enabled. Navigate to Administration > Settings, then enable Usage metrics under the Feature control section.
  - Timeliness, that checks the current data freshness against the threshold you configured. For more information, see [*Data freshness*](Data-freshness.htm). To set the threshold, click ![Configure](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_configure.png) to open the corresponding configuration panel:

    - Freshness threshold: Choose the maximum acceptable age of the data by selecting a value and unit (Minutes, Hours, Days, or Months). This threshold represents how often the dataset should be updated to remain relevant for your needs. When the dataset’s freshness exceeds the specified threshold, the timeliness score decreases, indicating the data may be outdated or less reliable for current analysis.

      Setting a freshness threshold ensures your dataset is regularly refreshed and meets your expectations for timely, relevant data. The configuration only impacts the selected dataset.
  - Accuracy, that takes into account the result of the data quality validation rules that have the category Accuracy, as well as their severity levels.

    If there is no score displayed for this dimension, it means that there are no validation rules applied to any of the dataset fields. For more information on validation rules, see [*Working with validation rules*](Working-with-validation-rules.htm).
  - Diversity, that takes into account the dataset diversity, including expectations regarding content evenness and volume distribution. To configure this dimension, click ![Configure](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_configure.png) to open the corresponding configuration panel and set the desired number of fields and rows:

    - Fields: This option evaluates diversity across the fields (columns) in your dataset. It checks how evenly data is distributed among the columns and whether each column contributes meaningful and varied data to the dataset.
    - Rows: This option assesses the distribution and variability of data across the records (rows) in your dataset. It helps identify whether the dataset contains a balanced and representative sample of records, without overrepresentation or underrepresentation of particular values.

      Setting minimum acceptable values for these parameters ensures that your dataset meets your requirements for both structure (fields) and sample size (rows). The configuration only impacts the selected dataset.

To be able to see the Qlik Trust Score™ of your dataset, you need to have computed the data quality at least once.

If you do not see all dimensions of the Qlik Trust Score™ from your dataset or data product, make sure they are enabled in the Qlik Trust score™ configuration page.

## Configuring the Qlik Trust Score™

From the Qlik Trust score™ page, you can configure and customize the weight of each dimension used to calculate the Qlik Trust Score™, as well as the display format. Note that this configuration will be applied to all existing datasets of your tenant.

Before configuring the Qlik Trust Score™, make sure that data quality is supported for your tenant. The same features and limitations that apply to data quality also apply to the Qlik Trust Score™, such as the supported file types. For more information, see [*Data quality for connection-based datasets*](Data-quality-connections.htm) and [*Data quality for uploaded files*](Data-quality-files.htm).

1. In Qlik Talend Data Integration > Data quality, click Qlik Trust score™.
2. To activate or deactivate a dimension, click the toggle on its left.

   The Validity and Completeness cannot be deactivated as they are the most essential parameters to determine the Qlik Trust Score™.
3. To adjust the weight of each dimension, click the plus and minus signs on its right.

   The total of percentages of all dimensions must equal 100%.
4. To customize the display of the Qlik Trust Score™, select either A score out of 5, or A percentage depending on the display format you want.

## Viewing the Qlik Trust Score™ history

The Qlik Trust Score™ continuously evolves along with your dataset life cycle, including changes in dimension weights, quality computation, tags, descriptions, usage, etc.

The historization feature allows you to consult the trends and evolution of the Qlik Trust Score™ directly from the dataset or data product overview:

- The main trends are directly displayed in the overview, next to the Qlik Trust score™, and next to each of its dimensions, representing the change compared to the previous score.
- You can access the Qlik Trust Score™ history detailed panel in two ways :

  - From a dataset overview: Click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) next to the Qlik Trust score™, and select View history.
  - From a data product overview: Click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) next to the dataset in the list, and select Qlik Trust Score™ history.

  The Qlik Trust Score™ history displays all events that resulted in a score change, organized chronologically. For each event, it provides a timestamp, a brief description of the triggering action, and the specific dimension or dimensions that were impacted by the change.

By default, the Qlik Trust Score™ history is shown as a graph. To display the data in a table format, click the table icon located on the right side of the graph. The most recent 500 events are loaded initially, and you can load additional events directly from the table view.

## Data product trust score insights

In a data product, the Quality tab provides a consolidated view of data quality at the data product level. It helps you understand how the overall Qlik Trust Score™ evolves over time, which datasets contribute most to score changes, and why variations occurred, so you can take timely and targeted corrective actions.

From the Quality tab, you can:

- Track the data product’s overall Qlik Trust Score™ evolution and review insights for each available dimension.

  The Validity view displays the global validity score, including information about validation rules and data types, and the validity score for each dataset in the data product.

  The Completeness view displays the global completeness score, data types ranked from most incomplete to most complete, and the completeness score for each dataset in the data product.

  The Discoverability view displays the global discoverability score and highlights how metadata quality impacts the data product score. It helps you identify datasets that need better documentation, such as missing or incomplete descriptions and tags on datasets and fields.

  When clicking on a validation rule or semantic type, you can drill down into more information in the right panel about where and how they are applied in each dataset.

  The Accuracy view displays the global accuracy score for the entire data product and lists all data quality validation rules categorized as Accuracy. For each contributing dataset, the view displays its individual accuracy score.

  The Timeliness view displays the global timeliness score and a score distribution across datasets. It also highlights datasets without a timeliness score, for example when timeliness is not configured or not supported for the dataset type.

  The Usage view displays the global usage score for the entire data product and the usage score for each dataset, including information about their dependencies such as analytics applications, data preparations, and data flows, and the number of views these dependencies have. It also highlights datasets without a usage score, for example when usage metrics are not enabled in the Administration settings.

  From dimension views, you can open dataset details in the right panel to investigate score contribution and understand what changed over time.
- Identify dataset-level drivers behind score changes, making it easier to pinpoint which datasets raised or lowered the composite score and which dimensions were impacted.
- Detect quality contract breaches (when available), such as constraints not being met (for example, Validity < 100% or timeliness thresholds exceeded), to support proactive monitoring and accountability.

Use these insights to prioritize remediation, focus on the datasets that most affect the data product health, and maintain compliance with your organization’s data governance requirements.
