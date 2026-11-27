---
title: "Hash processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-hash.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---

# Hash processor

Hides the original data through hashing.

The Hash processor allows you to protect sensitive data such as PII by using the 256 bit version of the Fowler-Noll-Vo algorithm. The original data is altered and replaced with a functional substitute.

## Usage

The Hash processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to hash your data.

Configuration

| Property | Configuration |
| --- | --- |
| Field to hash | Select the field or fields on which you want to apply the Fowler-Noll-Vo algorithm. |
| Create new field | Enable this option to create a new field after applying the function. If you do not enable this option, the existing field will be kept and modified. |
| Rename new field | Give a custom name to the newly created field. |

To rename the processor or edit its description, point your mouse over the name or description to change in the Properties panel and click the ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit icon.
