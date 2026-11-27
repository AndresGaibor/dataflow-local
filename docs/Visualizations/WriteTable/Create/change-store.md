---
title: "Working with change stores"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/change-store.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating write tables", "Configuring write tables"]
---

# Working with change stores

Change stores contain the user edits to editable columns in [write tables](#glossary-0 "Glossary term").

## What is a change store?

A change store is a Qlik-managed storage location that contains the user-added changes from [editable columns](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/editable-column.htm) in a write table. The change store is a temporary storage location—changes are stored for a maximum of 90 days, after which they are deleted.

You can either keep the automatically assigned change store or select an existing change store from the current space. When selecting an existing change store, make sure the primary keys in the write table match the primary keys defined in that change store.

Change store content is accessed via the change-stores API. With your change store ID, you can formulate API requests and automations that extract user changes to a permanent location such as a spreadsheet or database. For more information, see [*Extracting changes from write tables*](../Extract/write-table-extract-data.htm).

## Managing change stores

By default, a new change store is created for newly created write tables. With respect to change stores, you can customize the following:

- Select an exist change store to connect to your write table.

  [*Selecting a different change store for a write table*](#Selecting)
- Give change stores unique names.

  [*Renaming change stores*](#Renaming)

### Selecting a different change store for a write table

Optionally, under Change store in the properties panel, select an existing change store from the current space.

Requirements and behavior are as follows:

- The primary keys need to match between the current write table and the selected change store.
- A single change store cannot be connected to multiple write tables.

Do the following:

1. In the properties panel, expand Change store.
2. Next to Change store ID, click Select.

### Renaming change stores

Change stores have customizable names. You can rename each change store to make them unique and recognizable.

Do the following:

1. In the properties panel, expand Change store.
2. Click ![Edit](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
3. Type the change store name, and click to confirm.

## Copying the change store ID

You can copy the change store ID in two ways:

- In sheet edit mode after you create the write table. In the properties panel, under Change store > Change store ID, click ![Copy](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) Copy ID.

  Copying the change store ID from the properties panel.

  ![Clicking the 'Copy ID' button in the write table properties to obtain the change store ID](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_write-table-change-store-copy-id.png "Click to view full size")
- In analysis mode when viewing the write table. Click the ![Info](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) icon in the bottom right corner. Click ![Copy](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) to copy the change store ID.

  Copying the change store ID when viewing a write table.

  ![Clicking the 'Copy' icon from the info tooltip when viewing a write table, copying the change store ID](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_write-table-change-store-copy-view.png "Click to view full size")

## Extracting changes from a change store

Application developers and system integrators can extract change store data from write tables, using it to implement real-time automations and other workflows. See [*Extracting changes from write tables*](../Extract/write-table-extract-data.htm).

## Change store lifecycle

This section outlines the expected behavior for change stores when content is moved, published, and deleted.

### Publishing

Different behavior is expected between when the application is first published to a managed space, and for each time the application is subsequently republished.

#### First publish

When an application with a write table is first published to a managed space:

- New change stores are created in the target space
- The published application will use these new change stores

#### Republishing without changes to write configuration

In this scenario, nothing changes. The published application continues to use the change stores in the managed space.

#### Republishing after new editable columns are added in the source application

In this scenario, the target change stores are updated to support these new columns.

#### Republishing after removing editable columns in the source application

In this scenario:

- The write table in the published application will no longer show the deleted editable columns.
- The target change stores retain these deleted columns.

### Deletion

Deletion involves the deleting of charts, sheets, applications, and spaces.

#### Delete chart, sheet, or application

After a chart, sheet, or application containing a write table is deleted, the change store still exists in the space. You can still:

- Access the change store via the change-stores API.
- Connect a different write table to the change store, if the primary keys match. See [*Selecting a different change store for a write table*](#Selecting).

#### Delete space

When a space containing write tables is deleted, any change stores that were in the space are lost and not recoverable.

### Moving

Moving happens when an application with a write table is moved to a different space. With moving, the following happens:

- An empty change store will be created in the target space.
- The write table in the application will no longer be linked to the change store in the original space.

After the move, you can reconfigure the write table to select an existing change store in the target space.

## Limitations

For change store limitations, see [*Change store and data retention*](../Analyze/write-table.htm#LimitationChangeStore).

## Learn more

- [*Extracting changes from write tables*](../Extract/write-table-extract-data.htm)
- [*Creating write tables*](create.htm)
- [*Write table*](../Analyze/write-table.htm)
- [*Configuring editable columns*](editable-column.htm)
- [*Primary keys in write tables*](primary-key.htm)
- [How to extract changes from the Change Store (Write Table) and store them in a database using Qlik Automate](https://community.qlik.com/t5/Official-Support-Articles/How-to-extract-changes-from-the-Change-Store-Write-Table-and/ta-p/2537848)
