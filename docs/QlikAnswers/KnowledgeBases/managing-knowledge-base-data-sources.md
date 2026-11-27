---
title: "Managing knowledge base data sources"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/KnowledgeBases/managing-knowledge-base-data-sources.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with knowledge bases"]
---

# Managing knowledge base data sources

You can manage your knowledge base's data sources and files from the source table in Summary.

In the source table, you can:

- Edit connection configurations to include or exclude files.
- Remove connections from the KB.
- Remove files from a connection.
- Restore files from a connection.

You can also index sources in the source table. For more information, see [*Indexing knowledge base data sources*](indexing-knowledge-bases.htm).

## Editing data source configurations

In the hierarchical view, you can edit the data source connections. You can:

- Change the files included by your manual selection.
- Change the dynamic rules used to select files.

Information note

You cannot change the type of selection used by a connection. If you want to switch to a manual or dynamic selection, you must add the files again, using the new selection type.

Do the following:

1. In the hierarchical view, click ![Source options](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Edit configuration on a connection.
2. Edit your selections.
3. Click Save.

## Removing connections

You can remove data source connections from your knowledge bases. Removing a connection removes all files from that connection.

Do the following:

- In the hierarchical view, click ![Source options](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Remove connection on a connection.

  Alternatively, select the connections you want to remove and select Remove from knowledge base.

## Removing files

You can remove individual files from your connection. Removed files are deleted when the connection is next indexed.

Do the following:

- In the flat file view, click ![Source options](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Remove file on the file.

  Alternatively, select the files you want to remove and select Remove from knowledge base.

## Restoring files

You can restore removed files before they are deleted in the next indexing.

Information noteYou cannot use Restore file on a file that will be removed due to changes to your dynamic selection rules. To restore the file, edit your dynamic selection rules to include the file.

Do the following:

- In the flat file view, click ![Source options](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Restore file on a removed file.

  Alternatively, select the files want to restore and select Restore selected items.
