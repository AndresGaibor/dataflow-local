---
title: "Primary keys in write tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/primary-key.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating write tables", "Configuring write tables"]
---

# Primary keys in write tables

To add editable columns to a write table, you need to define at least one primary key.

## What is a primary key?

A primary key is a field used to link changes to editable columns back to the original data from the data model. Primary keys provide the mapping between records in the write table — which represent data from the data model — and the edits that users introduce within editable columns.

The primary key can be a single field, or it could be a composite key that spans multiple fields.

The primary key is also important when you pull changes from the change-stores API.

## Defining primary keys

Do the following:

1. In the properties panel, expand Change store.
2. Next to Primary keys, click Define or Modify.

## Learn more

- [*Creating write tables*](create.htm)
- [*Write table*](../Analyze/write-table.htm)
- [*Configuring editable columns*](editable-column.htm)
- [*Working with change stores*](change-store.htm)
- [How to extract changes from the Change Store (Write Table) and store them in a database using Qlik Automate](https://community.qlik.com/t5/Official-Support-Articles/How-to-extract-changes-from-the-Change-Store-Write-Table-and/ta-p/2537848)
