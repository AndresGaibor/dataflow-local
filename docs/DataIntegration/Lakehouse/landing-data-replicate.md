---
title: "Onboarding data from Qlik Replicate"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/landing-data-replicate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Onboarding data", "CDC data", "Landing data to Qlik Open Lakehouse"]
---

# Onboarding data from Qlik Replicate

You can use your existing Replicate infrastructure to load replicated data from Amazon S3 or Google Cloud Storage into [Qlik Open Lakehouse](lakehouse-pipeline-architecture.htm). The onboarding data wizard creates a pipeline to process Replicate output and store it as Iceberg tables.

Govnote-not-inNot supported in Qlik Cloud Government.

## Prerequisites

Before launching the onboarding data wizard, make sure that you have fulfilled the following prerequisites.

### Qlik Replicate prerequisites

Set up a Qlik Talend Data Integration task to move data to an Amazon S3 or Google Cloud Storage bucket by using the corresponding target endpoint.

#### Qlik Replicate task prerequisites

- Enable only the Full Load and/or Store changes replication options. Store changes is required to keep the data up to date.
- In the task settings' Store Changes Settings tab:

  - Configure the Change Table Settings as follows:

    - Suffix: `__ct`
    - Header column prefix: `header__`
    - DDL options: Apply to change table
    - On UPDATE: Store after image only
  - Leave Change Data Partitioning disabled (the default).
- In the task settings' Metadata > Control Tables tab, make sure the Apply Exceptions and DDL History control tables are selected.

For more information on these settings, refer to the [Qlik Replicate tasks settings help](https://help.qlik.com/en-US/replicate/Content/Global_Common/Content/SharedEMReplicate/Customize%20Tasks/tasks_settings.htm).

#### Qlik Replicate target endpoint prerequisites

Configure the Amazon S3 or Google Cloud Storage target endpoint.

In the General tab:

- In the Metadata Files section, enable metadata file creation. Depending on your Replicate version, select Create metadata files in the target folder or Create a metadata file for each data file. Replicate creates a matching .dfm file for each data file in the target bucket.
- In the File Attributes section, make sure that:
  - CSV is the selected Format (the default)
  - Compress files using is set to None for Amazon S3 or NONE for Google Cloud Storage (the default)
  - Both Add metadata header options are enabled (With column names
    and With data types)
- If the target bucket contains files that are not from Replicate, specify a Target folder. This makes it easier to find the Replicate output when you onboard the data.

For endpoint details, see the [Amazon S3 target endpoint help](https://help.qlik.com/en-US/replicate/Content/Replicate/Main/Amazon%20S3/set_up_file_as_target_in_tasks3.htm) or [Google Cloud Storage target endpoint help](https://help.qlik.com/en-US/replicate/Content/Replicate/Main/Google%20Cloud%20Storage/googlecloud_set_up_file_as_target_in_tasks3.htm). For Google Cloud Storage permissions, see [Google Cloud Storage target prerequisites](https://help.qlik.com/en-US/replicate/Content/Replicate/Main/Google%20Cloud%20Storage/googlecloud_s3_prerequisitess3.htm).

### Qlik Open Lakehouse prerequisites

An Amazon S3 Data Stream or GCS Data Stream connection configured to access the Replicate output in the target bucket.

For information about streaming connections, see [*Connecting to data streams*](../SourcesConnections/Connecting-Data-Streams.htm).

## How Replicate organizes data

Replicate creates a folder for each source table in the target folder. This structure helps you locate Replicate files in the Directory browser when you create an onboarding task.

- <bucket>/<target-folder>/<schema.table>/

  Contains full Load files and DFM metadata files in sequential format, as in the following example:

  - LOAD00000001.csv
  - LOAD00000001.dfm
  - LOAD00000002.csv
  - LOAD00000002.dfm
- <bucket>/<target-folder>/<schema.table\_\_ct>/

  Contains Change Data Capture files and DFM metadata files in timestamp format, as in the following example:

  - 20250121-083015000.csv
  - 20250121-083015000.dfm
  - 20250121-091522000.csv
  - 20250121-091522000.dfm

## Create an onboarding task

Follow these steps to configure an onboarding task for Replicate data:

1. Launch the onboarding wizard as follows:

   - New project: Click Onboard data in the middle of the project window.
   - Existing project: In the top right of your Qlik Open Lakehouse project, click Create new > Onboard data to launch the onboarding wizard.
2. Enter a task name and description.
3. Select Qlik Replicate from the Data origin options. Then, click Next.
4. Select the Amazon S3 Data Stream or GCS Data Stream connection you configured earlier. Then, click Next.
5. In the Directory browser pane on the left, select the root directory containing the Replicate output.

   Tip noteIf you did not specify a target folder in the Replicate endpoint settings, the bucket might contain unrelated files. If you know the path, you can enter it in the Replicate root directory path field.
6. Click Load to detect available tables. Any available tables will be shown in the Selected tables to register list.
7. In the Select data source to discover tables region on the right, the following settings are available:
   - Include all current tables: Toggle on to land all existing tables. When this option is toggled off, select individual tables.
   - Delete the source files following ingestion: Toggle on to permanently remove files from the Replicate bucket after they are processed.

     Deleting source files makes them unavailable to other pipelines that use the same bucket and files. Enable this option only if other processes do not need the files.
8. Click Next.
9. On the Content Type step, the file format (CSV) is automatically detected from your Replicate data. The following options are also available:
   - Historical Data store (Type 2): Toggle on this option to maintain historical versions of records and keep an archive of the changes.
   - Verify that events are correctly loaded: Select a dataset to verify that it contains the correct data.
10. Click Next.
11. Review the task configuration and click Create to create the onboarding task.
12. Click Prepare to catalog the data task and prepare it for execution.

    You can track the prepare progress in the task tile. On completion, Prepare: Success should be displayed.
13. When you are ready to start onboarding data, click Run.

## What happens next

Once activated, the onboarding task:

1. Monitors the Replicate bucket for new data files
2. Detects Full Load and CDC (Change Data Capture) files from Replicate
3. Processes the files and creates Iceberg tables in Qlik Open Lakehouse
4. Continues to monitor for new data
5. If enabled, automatically deletes source files after successful ingestion

In GCP, the Storage data task writes the Replicate data to Iceberg tables in Google Cloud Storage. You can add a Mirror data task to make the tables available in BigQuery. For more information, see [*Mirroring data to a cloud data warehouse*](mirroring-data.htm).

## Tasks settings

To change the task settings, open the Onboarding\_Qlik\_Replicate (default name) task and click the Settings toolbar button.

The Settings: <task name> dialog opens.

### General tab

These options are described in Step 7 of Create a landing task above.

- Automatically include all current and future tables
- Delete the source files following ingestion

### Runtime tab

Change the Lakehouse cluster

## Considerations and limitations

### General considerations and limitations

- Full Load and Reload operations may experience a processing delay before data appears in Iceberg tables. The system waits up to 15 minutes after Full Load completion to ensure the files are complete. As a result, running full loads in Replicate (scheduled or manually) less than 15 minutes apart is not supported.
- Empty Replicate tables (tables with no data files) are not detected or registered by the system.
- If you enable Delete the source files following ingestion, the landing task cannot be reloaded. To reload data, you must regenerate it in Replicate.
- Qlik Replicate's [Tables are already loaded. Start processing changes from](/en-US/replicate/May2026/Content/Global_Common/Content/SharedEMReplicate/Tasks%20at%20Runtime/monitor_detailed_run_options.htm#:~:text=Tables%20are%20already%20loaded.%20Start%20processing%20changes%20from%3A) Advanced Run option is not supported. When Type 2 (historical data) is enabled, using this option will corrupt the history table.

### CDC vs Replicate Pipeline

In a regular pipeline ingesting from CDC sources, the Data is updated to metric reflects freshness based on access to the database transaction log. A Replicate pipeline reads files from a target bucket instead, so the metric uses file timestamps. If the source database has no new changes, Replicate does not create a new file and the timestamp can appear old even when the data is current.
