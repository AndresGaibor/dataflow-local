---
title: "Assessing data quality"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Data-quality-and-data-discovery.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog"]
---

# Assessing data quality

After you open a dataset, review the overview to learn about overall quality, schema, quality statistics, and semantic types for each column.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

## Quality indicators of the dataset

Information noteA Qlik Cloud Analytics connection is required to compute the quality and profiling of your datasets. For more information, see [*Data quality for connection-based datasets*](Data-quality-connections.htm)

When you open the overview of a dataset that has just been registered, most of the information is grayed out. To calculate the data quality for the first time, click the Compute button. If the quality has already been computed once before, but you want to make sure that the data is up to date, click the Refresh button.

Each compute or refresh in pushdown will induce some costs in your Cloud data warehouse (Snowflake or Databricks). For more information, see [*Data quality for connection-based datasets*](Data-quality-connections.htm).

There are two main sections where the quality is displayed.

- The Data quality area, that includes a quality bar with three colors, and their respective percentages:

  - Invalid (red): Shows the percentage of values in the sample that are considered invalid.
  - Empty or null (black): Indicates the percentage of values in the sample that are empty or null.
  - Valid (green): Displays the percentage of valid values in the sample. The percentage does not take empty values into account.
- The Schema area that shows the different fields of the dataset, which data type or semantic type has been applied, and a quality bar for each field of the dataset.

Tip noteFor connection-based datasets, if the schema and quality of the dataset fails to be retrieved, check if the connection you have set up in the Qlik Analytics Services hub has the Role field properly filled, or if the role itself grants the necessary permissions on the database table.

## Semantic types discovery

Each column of a dataset is automatically assigned a semantic type to better describe its content. Behind the scenes a data discovery operation occurs to determine which type to assign.

Detected semantic types can also support data classification and regulatory review. Before you apply field-level classifications, verify semantic type assignments for sensitive fields.

You can also create semantic types and manage the values in each semantic type.

For more information, see [Managing semantic types](Managing-semantic-types.htm).

## Sampling modes for compute modes

The sampling mode used for data samples depends on the compute mode selected:

- **Pull-up mode:** A head sample is used, meaning the first rows of the dataset are taken as the sample.
- **Pushdown mode:** A random sample is used, ensuring a more distributed representation of the dataset. This mode is currently supported only for Databricks and Snowflake.

For QVD files, both head and random sampling are used to provide a more representative sample.

Understanding the sampling mode helps in interpreting the data quality metrics accurately based on the compute mode.

## Working with data quality in Qlik Answers

You can also work with data quality using natural language with the agentic experience in Qlik Answers. For more information, see [*Managing data quality with Qlik Answers*](../../QlikAnswers/data-quality-agent.htm).
