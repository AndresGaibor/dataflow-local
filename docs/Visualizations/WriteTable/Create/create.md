---
title: "Creating write tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating write tables

You can create a write table on your sheet, adding dimensions, measures, and editable columns as needed. After creating a write table in an application, users with access to that application, as well as write table permissions, will be able to make changes to editable columns. Changes can then be exported to external systems.

## Write table concepts

The following topics outline key concepts for the write table:

- [*Working with change stores*](change-store.htm)
- [*Configuring editable columns*](editable-column.htm)
- [*Primary keys in write tables*](primary-key.htm)

## Create a write table

You can add a write table to your sheet at any time.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag a Write table to the sheet.
3. Click Add dimension and select a dimension or a field.
4. Add additional dimension and measure columns by clicking ![Open Add data asset menu](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) under Data in the properties panel. A dropdown opens. Select either of the following:

   - Fields & master items: Opens a searchable dialog box displaying every field and master item. You can choose to add any item as a dimension or measure.
   - Custom expression: Opens a dialog box where you can type in an expression, or open the expression editor ![Open Expression editor](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression.svg).
5. Add [editable columns](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/editable-column.htm) by clicking ![Add editable columns](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_user_outline.svg) under Data in the properties panel, and selecting one of the following:

   - Create new editable column: Create a new, blank editable column.
   - Add existing editable columns: Use existing editable columns that match the [primary keys](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/primary-key.htm) defined for your write table.
6. By default, a new [change store](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/change-store.htm) is created for newly created write tables. Optionally, under Change store in the properties panel, select an existing change store from the current space.
7. Define one or more [primary keys](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/primary-key.htm) for the table. In the write table, within the editable column, click Define, and select one or more dimension columns to use as the primary keys.
8. Click Save.

After you create the write table, allow users to interact with it and add changes to editable columns. You can also customize the appearance of the write table by configuring its properties and incorporating it into custom themes. See:

- [*Configuring write tables*](properties.htm)
- [Qlik Developer Portal: Write table theme properties](https://qlik.dev/extend/property-panel-basics/define-properties/themes-properties/#writetable)

## Extract and use changes

Application developers and system integrators can retrieve write table changes via the change-stores API. For more information, see [*Extracting changes from write tables*](../Extract/write-table-extract-data.htm).

## Permissions

To create write tables and interact with the change-stores API, you need specific permissions. For more information, see [*Write table permissions*](../Analyze/write-table.htm#Permissions).

## Learn more

- [*Write table*](../Analyze/write-table.htm)
- [How to extract changes from the Change Store (Write Table) and store them in a database using Qlik Automate](https://community.qlik.com/t5/Official-Support-Articles/How-to-extract-changes-from-the-Change-Store-Write-Table-and/ta-p/2537848)
- [*Working with change stores*](change-store.htm)
- [*Extracting changes from write tables*](../Extract/write-table-extract-data.htm)
- [*Configuring editable columns*](editable-column.htm)
- [*Primary keys in write tables*](primary-key.htm)
