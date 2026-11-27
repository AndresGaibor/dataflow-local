---
title: "Creating knowledge bases"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/KnowledgeBases/creating-knowledge-bases.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with knowledge bases"]
---

# Creating knowledge bases

Knowledge bases provide the unstructured data that assistants use to generate responses to user questions.

A knowledge base comprises one or more data sources. Data sources added to a knowledge base are indexed for use in assistants. You can reindex sources that have been updated, either manually or by scheduling a synchronization with the data source. For more information, see [*Indexing knowledge base data sources*](indexing-knowledge-bases.htm).

You can have five knowledge bases per assistant.

## Supported file types and data sources

A knowledge base has the following data source limitations:

- Maximum file size: 50 MiB
- Maximum number of files per data source: 10,000

The following file types are supported as knowledge sources for Qlik Answers knowledge bases:

- TXT
- PDF

  Information noteKnowledge bases can index images in PDF files.
- DOC, DOCX
- PPTX
- HTM, HTML
- MD
- ODT
- RTF

The following connections are supported for accessing supported file types:

- Amazon S3
- Amazon S3 V2
- Azure Storage
- File (via Direct Access gateway)
- Dropbox
- Google Cloud Storage
- Google Drive
- Office 365 Sharepoint

  Information noteKnowledge bases support a maximum of 5000 files from an Office 365 Sharepoint connection.
- OneDrive
- SFTP

Information noteFiles inside shared folders in Google Drive and OneDrive are not supported for Qlik Answers if the Google Drive or OneDrive account is a personal account. Shared folders with businesses accounts are supported for Qlik Answers.

## Enhanced accuracy

You can optionally activate enhanced accuracy with your knowledge base. Enhanced accuracycreates contextually relevant text chunks to power stronger answers and parses information in tables better for PDF, Word, and PowerPoint documents. Enhanced accuracy does increase index times for the knowledge base, however.

If you choose to use enhanced accuracy, you will not be able to revert the knowledge base to the legacy parsing. If you do want to use the legacy parsing, you will need to create a new knowledge base.

Information note

Enhanced accuracy is not available in the following regions:

- Asia Pacific (Singapore)

## Creating new knowledge bases

You can add data sources for the knowledge base during creation or add them later.

When adding data sources from connections, you can add files manually or select them dynamically. Dynamically selecting files allows you to select the folder within the connection to take files from. You can then use filter rules and regular expressions. Filter rules include:

- Folder depth
- Max files count
- Max files per folder
- Max file size
- Modified after date

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-0 "Glossary term") and select Knowledge base.

   You can also create knowledge bases from Answer in Analytics or by clicking Create new > Knowledge base in Catalog.
2. After Name, enter a name for your knowledge base.
3. Optionally, after Description, enter a description for the knowledge base.
4. After Space, select the destination space for the knowledge base.
5. Optionally, after Tag, enter any tags you want to apply to the knowledge base.
6. Optionally, turn on Enhanced accuracy for supported files to activate advanced parsing for PDF, Word, and PowerPoint files. This also allows the indexing of images from PDF files.
7. Click Create.
8. Add data files to the knowledge base. You can:

   - Add files from a connection.

     Do the following:

     1. Click Use data connection.
     2. Select a data connection and click Next.
     3. To select files manually:

        1. Click Manual selection.
        2. Select the files to add and click Select.
     4. To select files dynamically:

        1. Click Dynamic rules.
        2. After Folder, select the folder.
        3. Either use the filter rules or add regular expression patterns to select which files to include.
        4. Click Select.
   - Add files from the catalog.

     Do the following:

     1. Click Choose from catalog.
     2. Select the files to add and click Select.
   - Upload files from your computer.

     Do the following:

     1. Click Browse and upload files.
     2. In Add new files to knowledge base, click Browse and import files.
     3. Drag and drop your data files into the dialog.

        Alternatively, click Browse and navigate to your data files.
     4. Select a destination space for the files.
     5. Click Upload.

   If you want to add data files later, close Add new files to knowledge base.

The files added to the knowledge base are ready to be indexed. For more information, see [*Indexing knowledge base data sources*](indexing-knowledge-bases.htm).

You can add additional data sources to the knowledge base. For more information, see [*Adding data sources to knowledge bases*](adding-sources-knowledge-bases.htm).
