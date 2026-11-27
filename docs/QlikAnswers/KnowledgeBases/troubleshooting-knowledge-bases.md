---
title: "Troubleshooting knowledge bases"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/KnowledgeBases/troubleshooting-knowledge-bases.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with knowledge bases"]
---

# Troubleshooting knowledge bases

This section describes possible problems and solutions for these issues when working with knowledge bases in Qlik Answers.

## File issues

If files in a knowledge bases have issues, such as duplicate entries or if files become corrupted, you can rebuild the knowledge base by deleting the data source, re-adding it, and then indexing it again.

Do the following:

1. Confirm the content in the data source has no issues.
2. In the hierarchical view, click ![Source options](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Remove connection or Remove file on the data source that has issues.
3. Click Add files and select Use data connection, Choose from catalog, or Browse and upload to re-add that data source.
4. Click Index all to index the data source.

## Connection issues

If you lose connection to a data source while indexing or have other connection issues to your data sources with your knowledge base, as a best practice, try recreating the connection and indexing again.
