---
title: "Troubleshooting - Write table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/troubleshooting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating write tables"]
---

# Troubleshooting - Write table

This help topic provides guidance for common errors you can encounter when working with [write tables](#glossary-0 "Glossary term").

## Write table displays as invalid visualization

When you open a sheet that contains a write table, the write table is not displayed. Instead, an error message displays Invalid visualization.

Possible cause 1

You have been given access to the application, not the space containing the application. The write table does not support fine-grained access control. See [*Sharing applications with users who are not space members*](../../../Spaces/sharing-content-with-non-space-members.htm).

Proposed action 1

The space owner or manager must give you the required access to the space containing the application with the write table. For the specific space roles, see [*Space permissions*](../Analyze/write-table.htm#Space).

Possible cause 2

You do not have the required space role to view or use the write table.

Proposed action 2

The space owner or manager must give you the required access to the space containing the application with the write table. For the specific space roles, see [*Space permissions*](../Analyze/write-table.htm#Space).

Possible cause 3

An administrator has not assigned you the required permissions for working with write tables.

Proposed action 3

Contact your [tenant administrator](#glossary-1 "Glossary term") and request to be assigned the required value for the Manage write table charts permission.

For more information, an administrator can refer to:

- [*Setting permissions for write tables*](../../../Admin/write-table-permissions.htm) (capacity-based subscriptions)
- [*Setting permissions for write tables*](../../../Admin/write-table-permissions-capacity.htm) (user-based subscriptions)

## Error in editable columns

An error in editable columns is shown. The error could be any of the following:

- The write table does not support duplication. Please delete this object.
- Unable to connect to change store.
- Primary key does not exist in the column list

Possible cause 1

The write table does not support duplication. Duplication happens in any of the following cases:

- A sheet or application containing a write table is copied and pasted, or duplicated.
- A write table visualization is copied and pasted.
- You export an application containing a write table and then import the application back into Qlik Cloud.
- You duplicate a write table using [enigma-js](https://qlik.dev/toolkits/enigma-js/#generic-object-model).

For more information, see [*Change store and data retention*](../Analyze/write-table.htm#LimitationChangeStore).

Possible cause 2

The underlying change store for the write table does not exist.

Proposed action

Recreate the write table by configuring a new chart. For more information, see [*Creating write tables*](create.htm).

Possible cause 3

The selected change store is incompatible with the primary keys in the write table.

Proposed action

Select a different change store, or update the primary keys in the write table so they match the selected change store. For more information, see [*Working with change stores*](change-store.htm) and [*Primary keys in write tables*](primary-key.htm).

## Cannot make or save changes to editable columns

Possible cause

Touch screen mode is turned on in the application. In touch screen mode, the write table is view-only.

Proposed action

Turn off touch screen mode in the application.

You can toggle touch support on and off by clicking or tapping the application navigation button (![Navigation](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg)) and using the toggle for ![Touch screen mode](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_touch_outline.svg) Touch screen mode.

## Learn more

- [*Write table*](../Analyze/write-table.htm)
