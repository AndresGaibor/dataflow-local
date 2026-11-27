---
title: "Write table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Analyze/write-table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Write table

In the Write table, you can make changes in editable columns during data analysis. Your changes can be used by analytics developers to implement automated, real-time processes and ensure data quality.

Adding data to editable columns in a write table.

![Adding data to editable columns in a write table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_write-table.png "Click to view full size")

## Use cases

The [write table](#glossary-0 "Glossary term") speeds up the process of gathering, updating, and taking action on time-sensitive data. With the write table, you can allow your organization to move faster and more efficiently in response to changing data. It also makes it easy for analyzers to add feedback, corrections, and additional insights that may not yet be in the data model.

Examples of use cases for the write table include:

- [Real-time inventory management](../Stories/manage-inventory.htm).
- [Real-time delivery management](../Stories/manage-delivery.htm).
- Analyzing and taking action on internal employee feedback.
- Analyzing and taking action on sales opportunities, including up-sell and renewal.

## Working with write tables

This process outlines how you can incorporate the write table into your operations, from development to analysis to data-driven action.

1. Create a write table

   The application developer first creates the write table. They have to define a primary key based on one or more dimensions in the write table and then add editable columns that can be used to collect changes from users.

   [Creating a write table](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/create.htm#WorkflowCreate)
2. Use the write table

   Users interact with the chart and make changes in editable columns. For example, users can add updates about order statuses, inventory, or customer feedback.

   Changes are saved for 90 days in change stores provided by Qlik.

   [*Interacting with a write table*](#Using)
3. Extract changes

   Application developers retrieve the changes from the change store via API. The changes can be backed up permanently to Qlik Cloud or to external systems, and used in automated operations—for example, automated inventory purchasing with the click of a button.

   [*Extracting changes from write tables*](../Extract/write-table-extract-data.htm#Using)

## Interacting with a write table

You add changes to editable columns in the write table. Depending on how the chart has been configured by the application developer, there are three ways in which you add changes: manual entry, single selection, and date picker. After making your changes, save the changes so that they are sent to the [change store](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/change-store.htm) and become visible to others.

### Manual entry

With manual entry, you type directly into the cells of the editable column.

Do the following:

1. In an editable column, click a cell that you want to edit.
2. Enter the desired text.
3. Click Save.

The changes are saved to the change store.

Editing cells with manual entry.

![Write table showing text being entered manually into an editable column cell value](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_write-table-interaction-manual-entry.png "Click to view full size")

### Single selection

With single selection, you use a dropdown menu to choose between pre-configured values.

Do the following:

1. In an editable column, click a cell that you want to edit.
2. Select the desired option.
3. Click Save.

The changes are saved to the change store.

Editing cells with single selection.

![Write table with dropdown showing options for editable column cell value](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_write-table-interaction-single-selection.png "Click to view full size")

### Date picker

With date picker, you select a date for the editable cell.

Do the following:

1. In an editable column, click a cell that you want to edit.
2. Select the desired date and click Apply.
3. Click Save.

The changes are saved to the change store.

Editing a cell for an editable column configured as a date picker

![Write table with date picker input type](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_write-table-interaction-date-picker.png "Click to view full size")

### Cell statuses

Cells in an editable column can have indicators showing several different statuses. These are:

- Not saved (orange): The cell has been updated by the current user but the changes are not yet saved. The user has the option to cancel or save the changes.
- Saved (green): The text in the cell has been saved to the change store. Its new value is visible to others.
- Locked (blue): Another user is currently making changes to the row. The row is locked during this time. You cannot make changes to it until they are done.

## Other interactions

For other actions, you can interact with a write table as you do in other table-based charts.

### Making selections

You can make [selections](#glossary-1 "Glossary term") in a write table by clicking or drawing in the dimension columns. It is not possible to make selections on editable columns as that data is not part of the application’s data model.

Selections work the same way in write tables as they do in straight tables. For more information, refer to the straight table documentation at [*Selections in straight tables*](../../StraightTable/selections-in-tables.htm).

### Searching in columns

In a write table, you can search the [dimension](#glossary-2 "Glossary term") columns, and make selections in the resulting list.

Do the following:

1. Click the column header for a dimension that you want to search in.
2. Click ![Search](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search.svg) Search.

   A selection popup is displayed with a list of all values of the [field](#glossary-3 "Glossary term"). This includes values that are excluded by selections. Excluded values are dark gray.
3. Type your search string. You can use any of the available search types. See [*Searching within selections or visualizations*](../../../Selections/SelectionsToolbar/search-selections.htm).

   While you type, the list is filtered to only display matching items.
4. Make a selection by clicking or drawing.
5. Confirm your selection.

   Tip noteYou can confirm the selection of all matching items by pressing Enter.

### Selecting active fields from cyclic dimensions

If a write table uses a cyclic dimension, analyzers can select the active field from the cyclic dimension.

Do the following:

1. Click ![Menu](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) on a cyclic dimension column.
2. Click ![Cycle](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg) <Dimension name> and select a dimension from the cyclic dimension.

### Keyboard navigation

You can analyze and make changes in write tables using the available keyboard navigation options. For more information, see [*Keyboard navigation and shortcuts in apps*](../../../UserInterface/keyboard-navigation-and-shortcuts.htm).

## Write table permissions

Whether you can work with write tables is determined by the following permissions:

- Permissions assigned to you by an administrator: Control whether you have full, partial, or no access to working with write tables. If you have partial rather than full access, you will be able to view write tables and make changes in editable columns, but you will not be able to configure the chart. See:

  - [*Setting permissions for write tables*](../../../Admin/write-table-permissions.htm) (capacity-based subscriptions)
  - [*Setting permissions for write tables*](../../../Admin/write-table-permissions-capacity.htm) (user-based subscriptions)
- Space permissions: Control access to write tables in specific spaces. See below for more information.

### Space permissions

In addition to administrator-assigned permissions, space permissions further control your write table access for applications in shared and managed spaces.

#### Viewing and analyzing write tables

The following space roles are required to view write tables and make changes in editable columns.

- In shared spaces, one of the following:

  - Owner (of space)
  - Can manage
  - Can edit data in applications
  - Can edit
  - Can view
- In managed spaces, one of the following:

  - Owner (of space)
  - Can manage
  - Can contribute
  - Can view
  - Can operate (Professional and capacity-based subscription users only)

#### Configuring write tables

The following space roles are required to create, edit, and delete write table configurations.

- In shared spaces, one of the following:

  - Owner (of space)
  - Can manage
  - Can edit data in applications
  - Can edit
- In managed spaces, one of the following:

  - Owner (of space)
  - Can manage
  - Can contribute

### Additional information

Further information about space permissions in Qlik Cloud can be found at:

- [*Shared space permissions for Professional and capacity-based subscription users*](../../../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../../../Spaces/permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](../../../Spaces/permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../../../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../../../Spaces/permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](../../../Spaces/permissions-managed-space-admin.htm)

## Scenarios for moving, publishing, deletion, and duplication

### Change store lifecycle

For information about the lifecycle of write table content, see [*Change store lifecycle*](../Create/change-store.htm#LifeCycle).

### Duplication

Duplication happens in any of the following cases:

- A sheet or application containing a write table is copied and pasted, or duplicated.
- A write table visualization is copied and pasted.
- You export an application containing a write table and then import the application back into Qlik Cloud.
- You duplicate a write table using [enigma-js](https://qlik.dev/toolkits/enigma-js/#generic-object-model).

Duplication is not supported in the write table. For more information, see:

- [*Change store and data retention*](#LimitationChangeStore)
- [*Troubleshooting - Write table*](../Create/troubleshooting.htm)

## Limitations

### Data and configuration limits

- The maximum number of [[editable columns](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/editable-column.htm)](../Create/create.htm#Editable) per [[change store](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/change-store.htm)](../Create/create.htm#ChangeStore) is 50. This limitation is per change store and not per write table visualization.
- The maximum number of [primary key](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/primary-key.htm) fields is 20.
- Alternative columns cannot be added in a write table.
- You cannot add a show condition to a column that is used as a primary key.
- Cyclic dimensions cannot be used as primary keys.
- User can enter a maximum of 1000 characters per editable column cell.

### Change store and data retention

- Multiple write tables cannot be connected to the same change store. In the case of duplication, you must delete the duplicated write table visualization. For more information, see [*Duplication*](#Duplication).
- After a change in an editable column is saved, it is stored for 90 days in the change store. After 90 days, it is deleted and this cannot be undone. If you need to back up these values, use Qlik Automate or load scripts to extract these changes to external systems or QVDs in Qlik Cloud.

### Visualization and interaction restrictions

- Write tables cannot be defined as master visualizations.
- Zebra stripes and visualization filters are not supported in the write table.
- Pagination is turned on by default in the write table. You cannot turn pagination off in this visualization.
- The Wrap text in cells setting is not supported for editable columns in a write table.
- Multi-line inputs are not supported in editable columns.
- Editable columns do not represent dimensions or measures, and are not connected to the application data model. Therefore, many of the properties that are available for dimension and measure columns are not applicable to editable columns.
- Cut is not supported for write tables.
- Write tables cannot be dragged into tab containers or layout containers.
- [The write table supports custom themes](https://qlik.dev/extend/property-panel-basics/define-properties/themes-properties/#writetable). You cannot use custom themes to change the colors that define cell statuses (orange, green, and blue).
- You cannot download a write table as data.

### Application and platform availability

- Write table visualizations are not supported in on-demand template applications.
- Write tables cannot be defined as dynamic views.
- The write table is not available in Direct Query applications.
- The write table is not available in Qlik Sense Client-Managed.
- The write table does not support anonymous access and is not available in Qlik Anonymous Access subscriptions.
- The write table is only available for the following subscription products:

  - Qlik Cloud Analytics Premium
  - Qlik Cloud Enterprise
  - Qlik Sense Enterprise SaaS
- Embedding the write table is not supported.
- The [write table](#glossary-4 "Glossary term") does not support fine-grained access control. If a user has access to an application without being a member of the space, they cannot view, edit, analyze, or create write tables on sheets in the application.
- Write tables are not supported in application performance evaluation.

### Snapshot and storytelling support

- Snapshots are not supported for the write table. This includes storytelling snapshots, embed snapshots, and creating snapshot from APIs.

### Mobile and display behavior

- In the Qlik Analytics mobile app, write tables are displayed in read-only mode.
- Write tables are not available when you open an application offline in the Qlik Analytics mobile app.
- In small-screen mode, write tables are displayed in read-only mode.

### Section access limitations

Section access is applied only to data that is in use by the Qlik engine. Also, the records shown in a write table depend on the primary key, which is configured using engine data. Therefore, if the write table is used in an application that uses section access, the records shown in the table will be restricted by section access.

However, the write table interaction data—the edits created during analysis sessions—are stored in a change store, which is separate from the engine. Section access is not applied on a change store or on the change-stores API. Therefore, users with API permissions will be able to read all data from a change store regardless of the section access rules.

Warning noteA malicious user with access to an application, as well as write table permissions, could emulate a client session on an application containing a write table. By guessing primary key values, this user can gain access to changes that were made on records they cannot access according to an application's section access rules. Consider these risks when adding the write table to applications that use section access, and when giving users view and edit access to applications containing the write table.

## Learn more

- [*Creating write tables*](../Create/create.htm)
- [*Configuring editable columns*](../Create/editable-column.htm)
- [*Working with change stores*](../Create/change-store.htm)
- [*Primary keys in write tables*](../Create/primary-key.htm)
