---
title: "Working with knowledge bases"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/KnowledgeBases/knowledge-bases.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Working with knowledge bases

Knowledge bases are collections of individual data sources, connected through a data connection, that are indexed for use in generating responses to user questions.

Knowledge bases provide a single place for searching and maintaining sources of unstructured data. Knowledge bases should align with a specific topical domain. For example, marketing knowledge bases might contain:

- Sales enablement
- Competitive analyses
- Customer references
- Use cases

You add unstructured data sources to your knowledge bases, either by uploading them to Qlik Cloud or by using a data connection. Once added, Qlik Answers indexes the data sources. Indexed data sources can then be used by Qlik Answers assistants to generate answers.

Information noteIn addition to textual unstructured data, knowledge bases support indexing images in PDF files as unstructured data sources. This allows textual content in diagrams, charts, or screenshots to be available to Qlik Answers.

To update indexed files in a knowledge base after the data sources are updated, you can manually index the files or schedule daily indexing for the knowledge base. For more information, see [*Indexing knowledge base data sources*](indexing-knowledge-bases.htm).

## Navigating knowledge bases

Knowledge bases have two sections:

- Summary
- Index history

### Summary

Summary provides details for the knowledge base, as well as a source table outlining the data sources and files used by the knowledge base. You can also view which assistants use a knowledge base and how often it is sourced by clicking View <number> assistants. This is only visible when there is at least 1 assistant linked.

Summary

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_KB-summary.png "Click to view full size")

Summary provides the following metadata for the knowledge base:

- Creator
- Space
- Created date
- Last index date

You can add data sources by clicking Add files. You can index all sources by clicking Index all. You can also index individual data sources. For more information on indexing, see [*Indexing knowledge base data sources*](indexing-knowledge-bases.htm).

You can create an assistant for the knowledge base by clicking Create assistant. You can also view the assistants that use the knowledge based by clicking View <number> assistants.

### Source table

The source table lists the data sources and files used with a knowledge base. The source table has two views:

- Flat file view (![Flat file view](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list.svg))
- Hierarchical view (![Hierarchical view](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tree_view.svg))

The source table displays the following metadata:

- Source name: Hierarchical view only. Displays the connection name.
- File name: The name of the file.
- Space: The space the connection or file is in.
- Pages: How many pages are in the data source. Pages correspond to 2,000 characters of text data.
- Index status: The status of the last index for the data source.
- Last index: When the data source was last indexed.
- Used as source: How many times a data source was used to answer questions.

  Deleting an assistant will not change the values in Used as source.

  Deleting a file will not update the Used as source value for the data connection.

You can search the source table for specific data sources. The following filters are available for displaying content in the source table:

- Space
- Pages
- Index status
- Last index rage
- Last index date
- Used as source

### Hierarchical view

The hierarchical view sorts the source table by data source. You can click a data source to view the files added to the knowledge base from that connection.

At the data sources level, you can manage your connections to files. In the file level, you can manage your indexed files. For more information, see [*Managing knowledge base data sources*](managing-knowledge-base-data-sources.htm).

Hierarchical view

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_kb-summary-hierarchy.png "Click to view full size")

When viewing files from a data source, you can click All data sources to return to the top of the hierarchy.

### Flat file view

In the flat file view, you can see all the files used in a knowledge base. In the flat file view, you can manage your indexed files. For more information, see [*Managing knowledge base data sources*](managing-knowledge-base-data-sources.htm).

Flat file view

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_kb-summary-flat-file.png "Click to view full size")

### Index history

Index history shows the history of indexes in the knowledge base. It displays the following metadata:

- Date
- Source connection
- Page change
- Index status
- Duration

You can index all sources by clicking Index all sources.

Index history

![The Index history tab, showing all indexing events for the knowledge base.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui-kb-index-history-rev.png "Click to view full size")
