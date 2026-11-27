---
title: "Synchronizing scripted tables in Data manager"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/synchronizing-scripted-tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager"]
---

# Synchronizing scripted tables in Data manager

By default, scripted tables added in the data load editor cannot use the tools available in [Data manager](#glossary-0 "Glossary term").

For example, you cannot associate scripted tables with other tables in Data manager or transform fields in scripted tables using the data profiling cards. If you synchronize your scripted tables in Data manager, you can replace your scripted tables in Data manager with managed scripted tables. These tables have access to all the same tools as tables added in Data manager, including:

- Editing tables, such as adding calculated fields.
- Transforming fields, such as changing the field types or transforming fields with data profiling cards.
- Transforming tables, such as unpivoting or concatenating tables.

Synchronization and managed scripted tables have the following limitations:

- Scripted tables must be located before the Auto-generated section in the data load script to be synchronized as managed scripted tables. Tables after the Auto-generated section in the data load script will not be synchronized.
- You cannot use Select data from source to change the selection of fields in a managed scripted table.

Warning note

Do not synchronize your scripted tables if your data [load script](#glossary-1 "Glossary term") contains an Exit statement or dynamic fields.

To convert your scripted tables into managed scripted tables, synchronize your scripted tables in Data manager. Synchronization does the following:

- Replaces all synchronized scripted tables as managed scripted tables.
- Deletes any managed scripted tables whose scripted tables have been removed in the data load script.
- Updates any managed scripted tables whose source tables were changed in the data load script.

  Warning note

  If you have synchronized tables, you should not make changes in the data load editor with Data manager open in another tab.

  Warning note

  Avoid changing the data load script for tables already synchronized in Data manager. If you remove or modify fields in data load editor, you must delete or redo any derived fields or associations in the synchronized table. Derived fields using a removed or modified [field](#glossary-2 "Glossary term") such as a calculated field or fields created by the Split card, display null values.

After synchronization, you can use the managed scripted tables in Data manager like any other table. Data manager prompts you to synchronize again if it detects differences between a managed scripted table and the source scripted table.

To change managed scripted tables back into scripted tables, delete them in Data manager. You must repeat the deletion if you synchronize again.

## Synchronizing scripted tables

Do the following:

1. In Data manager, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).

   Alternatively, select a scripted table.
2. Click Synchronize scripted tables.

Managed scripted tables replace all the scripted tables in Data manager.

## Removing managed scripted tables

Do the following:

1. In Data manager, select Tables view.
2. On the managed scripted table you want to remove, click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg).
3. Click Load data.

The managed scripted table changes back to a scripted table.
