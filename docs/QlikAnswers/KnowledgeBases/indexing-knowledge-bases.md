---
title: "Indexing knowledge base data sources"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/KnowledgeBases/indexing-knowledge-bases.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with knowledge bases"]
---

# Indexing knowledge base data sources

Files in knowledge bases must be indexed for use in assistants.

When you create a new knowledge base, you must index the files for use in assistants.

To update indexed files in a knowledge base, you can manually index the files or schedule daily indexing.

Indexing is measured by the page, which corresponds to 2,000 characters of text data. You can review the changes before indexing files manually.

You can view the history of indexing in Index history.

## Indexing images in PDF files

When your knowledge base contains PDF files with embedded images, such as diagrams, charts, or screenshots, those images are automatically indexed alongside text content. This indexing enables more contextually relevant search results when visual information answers a user's query.

Information noteIndexing images is only available for knowledge bases with Enhanced accuracy for supported files turned on.

Images in PDFs are vectorized using multimodal embeddings, which means they are processed and understood in the same semantic space as text. When users search for information that might be visually represented, image results appear in search responses with thumbnails, and users can view the full images in the source documents.

### Limitations

Images have the following limitations:

- Image indexing applies only to PDF documents with embedded images.
- Standalone image files (JPG, PNG) are not supported.
- This capability is available for new knowledge bases created after this feature release. Existing knowledge bases must update to use the feature.

## Manually indexing data sources

You can manually index all data sources for a knowledge base. You can also index individual data sources and files.

### Indexing all data sources

Do the following:

- In Summary, click Index all.

  A message appears indicating indexing has started. You can view the progress of the indexing under Index status.

### Indexing a single data source or file

If you do not want to index all data sources, you can index:

- The files of a single data connection
- Individual single files

Do the following:

- In Summary, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside the data connection or file you want to index and click Index or Index file.

  Alternatively, select the data connections or files you want to index and select Index selected items.

## Checking for changes before indexing

You can view both the number of files and size of files that will be indexed from a source connection before indexing them.
This is useful for keeping track of how many pages you are using versus total capacity. It can also check that a connection is picking up changes to files.

Do the following:

1. In Summary, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside the source connection you want to check and click Check for changes.
2. In Index new files, review the differences.
3. To index the changes, click Start indexing.
4. If you do not want to index the changes, click Close.

## Scheduling indexing for data sources

Do the following:

1. In Summary, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside the source connection you want to index and click Set schedule.
2. Turn on Daily index schedule for "<data connection name>".
3. Under Start time, select the start time for the indexing.
4. Under Timezone, select the time zone to use.
5. Click Save.
