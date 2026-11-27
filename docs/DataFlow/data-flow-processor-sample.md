---
title: "Sample processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-sample.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---

# Sample processor

Keeps only the first rows or a random subset of rows.

The Sample processor allows you to select a specific number or percentage of records from your input flow and make the data sample more representative of the whole dataset.

## Usage

- The Sample processor requires one input flow and can generate only one output flow.
- Using this processor will unsort the data if a Sort processor was used in the input flow.

## Properties

Properties to configure to select a subset of records from the input.

Configuration

| Property | Configuration |
| --- | --- |
| Sampling method | Select if you want to extract a fixed number of rows or a percentage of the total rows from the input flow:   - Random rows: Keeps a percentage of rows from across your dataset. - First rows: Keeps a fixed number of rows starting from the beginning of your dataset - Fixed number of random rows: Keeps a fixed number of rows randomly from across your dataset - Random stratified sampling: Keeps the chosen percentage of rows for each value of the stratum field.  Information noteDue to rounding, using this method can lead to significant deviations from the expected overall row count, especially when selecting small strata. Additionally, strata with only one row may not be represented at all in the output if the percentage of rows to sample is low. |
| Number of rows to extract | Enter the number of rows to keep. |
| Sampling ratio (%) | Enter the percentage of rows to keep. |
| Stratum field | From the dropdown list, select the field to use as stratum. |

To rename the processor or edit its description, point your mouse over the name or description to change in the Properties panel and click the ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit icon.

## Example

In this example, you are working on a dataset containing information on sales transactions from three regions: East, West, and Central.

![dataset containing customer information](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/sample_example_1.png)

Currently, the sample contains 20 rows, but you would like to reduce its size, while making sure that each region is evenly represented in the sampled data. You will use the Sample processor to change the size of the sample.

In the processor properties, select Random stratified sampling as sampling method, set the Sampling ratio (%) to 50, and select Region as stratum field.

Setting the stratified sampling to 50% means that the sample will contain approximately half of the rows from each region after rounding.

![a data flow configuration to sample the dataset by region](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/sample_example_2.png)

In the output of the processor, the sample now only contains approximately half the rows of the original, while keeping the same distribution of regions.
