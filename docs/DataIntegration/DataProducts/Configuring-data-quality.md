---
title: "Configuring data quality"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Configuring-data-quality.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog", "Assessing data quality"]
---

# Configuring data quality

Once you have computed data quality on your dataset for the first time, you have the possibility to refresh this calculation and customize it according to your needs.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

## Selecting the sample size and processing mode

To be able to customize the sample size for quality computing, you need to have previously clicked Compute once on your dataset.

1. From Qlik Talend Data Integration > Catalog, open your dataset.
2. Depending on how you want to compute data quality:

   - Click Refresh to recalculate data quality using the previously applied parameters.
   - Click the down arrow next to the Refresh button to expand the Quality and profiling panel and customize the recalculation.
3. In Sample size, enter the size of the sample on which you want to calculate data quality:

   - Number of rows: Enter the number of rows on which you want to calculate data quality. The maximum value is 100000 rows in pullup mode, there is no maximum value in pushdown mode.
   - Percentage of the dataset: Alternatively, enter the percentage of the dataset on which you want to calculate data quality. Decimal values are not allowed. For big datasets, if 1% of the dataset equals more than the maximum number of rows allowed (100000 rows), this option is not displayed.
4. In Processing mode, select the processing mode to use when calculating data quality:

   - Pushdown: Currently only available for Snowflake and Databricks datasets. It triggers the quality computation on the database side, costing Snowflake credits or Databricks units (DBUs).
   - Pullup: Available for all datasets. It triggers the quality computation in Qlik Cloud.
5. Click Refresh to recompute the data quality according to your settings.

The data quality indicators as well as the sample size are displayed in the Overview. The processing time varies depending on the sample size.

Information noteData quality cannot be computed for datasets that have more than 500 columns.

The data quality computation can also be triggered and customized through the corresponding [Qlik Public API](https://qlik.dev/apis/rest/data-qualities/).

For data quality scheduling, the Qlik Automate template Schedule data quality computations can be used. See [*All templates*](../../../Sense_QlikAutomation/introduction/template-list.htm) for more information.

## Filtering the dataset preview by quality status

When viewing your dataset in the Data preview tab, quality results are visually represented using a color bar on column headers, as well as in the right-hand panel for data types and validation rules.

Each segment of the quality bar corresponds to one of the result categories. From the column header, you can see the following indicators:

- Invalid (red): Shows the percentage of values in the sample that are considered invalid.
- Empty or null (black): Indicates the percentage of values in the sample that are empty or null.
- Valid (green): Displays the percentage of valid values in the sample. The percentage does not take empty values into account.

Clicking a column header opens the right panel where you can see the same indicators for the data types.

Additionally, the quality bar for validation rules in the right panel displays:

- Not executable (light red): The rule cannot be executed on those values.
- Invalid (red). Either:
  - They fulfill the condition (if) but not the validation expression (then), and no alternative validation expression (else) has been defined.
  - They fulfill neither the condition (if) nor the alternative validation expression (else).
- Not applicable (light green): The values do not fulfill the condition (if) and no alternative validation expression (else) has been defined.
- Valid (green): The values fulfill all rule statements.

For more information on validation rules, see [*Working with validation rules*](Working-with-validation-rules.htm).

You can filter the dataset preview by clicking on any segment of the quality bar, either in the column header or in the rules and data types sections of the right panel. When you click a colored segment:

- A filter is applied to the current preview to display only the rows corresponding to that data quality result (for the selected column or group of columns) and to isolate quality issues.
- The filter can be removed to return to the full sample preview. To remove filters, click Clear all filters.

This filtering helps you quickly inspect only the values of interest in your dataset, simplifying the review and investigation of records by their data quality status.
