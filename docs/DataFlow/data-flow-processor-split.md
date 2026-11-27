---
title: "Split fields processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-split.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---

# Split fields processor

Splits fields using a separator or regex.

The Split fields processor allows you to split the content of one or multiple fields into the selected number of parts, based on a separator or regular expression, and create multiple new fields.

## Usage

The Split fields processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to split a text in parts.

Configuration

| Property | Configuration |
| --- | --- |
| Function name | - Split text in parts: Splits fields based on separators. - Extract values by regex: Splits fields based on a regular expression. Use a regex with a single group that matches all parts to extract. |
| Fields to process | Select the field or fields on which you want to apply a function in the list. |
| Parts | Enter the number of parts in which the data should be split. If there are more parts than specified in the Parts property, they are ignored. |
| Separator | Select which character to base the split on from the list, or use a custom one. |

To rename the processor or edit its description, point your mouse over the name or description to change in the Properties panel and click the ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit icon.
