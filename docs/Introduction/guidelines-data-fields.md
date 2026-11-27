---
title: "Guidelines for data and fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/guidelines-data-fields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting"]
---

# Guidelines for data and fields

There are certain conventions and limitations you need to be aware of when working with scripting. For example: the upper limit for data tables and fields as well as maximum amount of loaded data in a Qlik Sense application.

## Guidelines for amount of loaded data

The amount of data that can be loaded into Qlik Sense is primarily, but not exclusively, limited by the amount of primary memory of the computer.

## Upper limits for data tables and fields

Be aware when building very large applications or scripts that an application or script cannot have more than 2,147,483,648 distinct values in one field.

The number of fields and data tables as well as the number of table cells and table rows that can be loaded, is mainly limited by RAM.

When importing a dataset file into a Qlik Sense application or space with Data manager (drag-and-drop or other direct uploads), the maximum number of fields that can be loaded is 5000.

## Recommended limit for load script sections

The recommended maximum number of characters to be used per [load script](#glossary-1 "Glossary term") section is 50,000 characters.
