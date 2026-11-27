---
title: "Streaming lake landing settings"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/landing-data-settings-streaming.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Onboarding data", "Streaming data", "Landing streaming data to Qlik Open Lakehouse"]
---

# Streaming lake landing settings

The following Streaming lake landing task settings apply to Qlik Open Lakehouse projects using a streaming source.

## General

Folder to use

 Select the folder to use when landing data to the staging area.

- Default folder

  This creates a folder with the default name: <project name>/<data task name>.
- Root folder

  Store data in the root folder of the storage.
- Folder

  Specify a folder name to use.

Folder retention

 Select how long to retain the data:

- Data and metadata are not deleted: Neither the data or the metadata are deleted.
- Delete data and metadata after the retention period: Data and metadata are deleted after the retention period is passed,
- Delete metadata after the retention period. The data is deleted by external system.The data is deleted permanently after this period elapses. The metadata is purged, but the underlying object in cloud storage is not deleted by Qlik.

Read data from

 Select when to ingest the data from:

- Start from now

  Ingest only the events that arrive when the pipeline begins.
- Start from the earliest event (default)

  Ingest all historical data.

Content type

Select the file format from the list, for example, JSON, or CSV. This can be changed after the task has been run by recreating the task.
See [Content types](#Content_Types) for details for each file format.

## Schema evolution

New topic/streamSelect how to handle new streams/topics.

- Add to target: If you load all tables to a single target table, new data is added to this table. If you load each topic to a different dataset, a new topic is added to a new dataset.
- Ignore: New data is not added to the target.

## Run time

Number of readers

- Apache Kafka: Select the number of readers to use. The value must be between 1 and 1,000.
- Amazon Kinesis: Select the number of stream shards.
- Amazon S3: This setting is not applicable to S3 streaming sources.
- GCS Data Stream: This setting is not applicable to Google Cloud Storage streaming sources.

Lakehouse cluster

Select the streaming cluster. The Streaming landing task and Streaming Transform tasks do not need to be on the same cluster, but do need to be on the same network integration.

## Content Types

The following settings apply to each file format.

- JSON

  - This is the default file format if not otherwise define.
- CSV and TSV

  - First row contains headers: Selected by default to specify that the first row contains the header record.
  - Header row (Optional): If the first row is not the header, define the header names.
  - Delimiter: Select the default delimiter if this is not the default (comma for CSV, tab for TSV.
  - Quote escape character: Select the default quote escape character if this is not a double quote as defined by default.
  - Null value (Optional): Enter the replacement null value.
  - Allow duplicate headers: If two columns have the same name, the second is added with a different name.
- Parquet, Avro, and ORC

  - No additional settings require configuration.
- Regex

  - Pattern: Enter the regular expression pattern.
  - Multi-line: Selected by default.
- Split lines:

  - Regex: Enter the regular expression for the split.

Information noteThe following compressed files formats are supported and will be decompressed automatically: GZIP, SNAPPY, LZ4, ZSTD, TAR, and LZO.

### Auto-detecting content types

Auto detect: Click to automatically detect whether the source file format is JSON, Parquet, or Avro. Other file formats need to be manually selected.
