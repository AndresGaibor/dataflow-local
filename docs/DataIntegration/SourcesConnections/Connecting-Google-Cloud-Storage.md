---
title: "Google Cloud Storage"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-Google-Cloud-Storage.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to cloud storage"]
---

# Google Cloud Storage

Google Cloud Storage is Google's unified object storage service for storing and accessing data on Google Cloud infrastructure. It offers high availability, global redundancy, and integrates with the broader Google Cloud ecosystem.

Qlik Talend Cloud uses a Google Cloud service account with read access to the target bucket to connect to Google Cloud Storage (GCS). The connector retrieves files from the specified bucket, automatically discovers schemas by sampling file contents, and performs incremental data replication based on file modification timestamps.

Feature snapshot

A high-level look at this connector, including useful links, and supported features.

| Feature/Capability | Support details |
| --- | --- |
| Supported Qlik Talend Data Integration projects | [Replication projects](../Replicating/data-replication-task.htm) only. Data pipeline projects are not supported. |
| [*Target update methods*](Change-processing.htm) | Replication tasks:   - Apply changes - Store changes   Landing data in a data lake tasks:   - Change data capture (CDC) |
| [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm#Managing) | Manual metadata generation is not required. |
| [*Automatic schema evolution*](../Replicating/replicating-settings.htm#Schema) | Only the Change column data type operation is supported. |
| Replication of LOB columns (NCLOB, CLOB, and BLOB) | Not supported. |
| Scheduled CDC | Required. This is how the target is kept up-to-date with changes to the source.  For replication tasks, see [*Scheduling tasks*](../Replicating/replicating-settings.htm#Scheduli2)  For lake landing tasks, see [*Scheduling CDC for lake landing tasks*](../Replicating/landing-datalakes-settings.htm#Scheduli2) |
| Notifications | Partially supported  [*Setting notifications for changes in operation*](../Introduction/Notifications.htm) |
| Monitoring | CDC-only, as full load is not relevant for this connector.  [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm) |
| Automatic denesting of JSON column payloads | Not supported. JSON column payloads in source datasets are not denested automatically on the target. |

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Google Cloud Storage account, you need:

- A Google Cloud Platform (GCP) project with the Cloud Storage API enabled.
- A Google Cloud Storage (GCS) bucket that contains the files to be replicated.
- A service account with read access to the bucket.

  The recommended role is Storage Object Viewer (`roles/storage.objectViewer`), which grants the required `storage.objects.get` and `storage.objects.list` permissions.
  For more information, see [Google Cloud Storage IAM roles documentation](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) .
- A service account JSON key file downloaded for the service account.

To create a service account and retrieve your credentials:

1. Log into your [Google Cloud](https://accounts.google.com/v3/signin/identifier?authuser=0&ec=GAlAywI&hl=en&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S-1020015778%3A1777897358935634) account.
2. Navigate to IAM & Admin > Service Accounts.
3. Click Create Service Account.
4. Enter a name and description for the service account, then click Create and Continue.
5. Grant the service account the Storage Object Viewer role or a custom role with `storage.objects.get` and `storage.objects.list` permissions.
6. Click Continue and Done.
7. In your newly created service account, click the Actions menu.
8. Navigate to Manage keys > Add key > Create new key.
9. Select JSON, and click Create.

   The JSON key file is downloaded directly to your machine. This file includes the `project_id`, `client_email`, and `private_key` fields required to establish the connection.

   You can download the key file only once. Be sure to store it securely and back it up, as it provides access to your Google Cloud resources.

### Supported file formats

- Delimited text: CSV, TSV, PSV, TXT (with configurable delimiter)
- JSON Lines (`.jsonl`)
- Parquet (`.parquet`)
- Avro (`.avro`)
- Gzip-compressed files (`.gz`) containing any of the above formats
- ZIP archives containing CSV, JSON Lines, TXT, TSV, PSV, or Gzip files

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Client Email | Client email from the service account JSON key file. |
| Project ID | Project ID from the service account JSON key file. |
| Bucket | Name of the Google Cloud Storage (GCS) bucket where the files are stored, for example, `my-gcs-bucket`. Do not include the `gs://` prefix. |
| Tables | Configure tables to control which files are read and how their contents are interpreted. Each table definition includes a file search pattern, a table name, and optional settings for advanced behavior. |
| Private Key | Private key from the service account JSON key file. |

### Table configuration

Each entry in the table configuration specifies a logical table created from files in the target bucket. You can configure the following properties for each table:

| Property | Required or Optional | Description |
| --- | --- | --- |
| Table Name | Required | Specify a name for the logical table, for example `my_orders_csv`. This name will appear as the stream name in Qlik Talend Cloud. |
| Search Pattern | Required | Enter a regular expression to match file names, for example `.*\.csv$` to select all CSV files. The connector uses regex and glob search pattern syntax. In regex, `*.csv` does not match CSV file names because `*` must follow an expression to repeat. Use patterns such as `\.csv$` or `.*\.csv$` to match filenames like `report.csv` and `my.data.csv`. |
| Search Prefix | Optional | Provide a path prefix within the bucket to narrow the file search, for example `exports/orders/`. Using a prefix improves performance by limiting the number of files scanned. |
| Key Properties | Optional | List one or more column names, separated by commas, to define the primary key. For example: `id` or `id,date`. |
| Date Overrides | Optional | List column names, separated by commas, to be treated as date-time fields. Use this option if these fields are not automatically detected during schema discovery. |
| Delimiter | Optional | Specify the character that separates values in your files. The default is `,` (comma). Use `\t` for tab-delimited (TSV) files or `|` for pipe-separated (PSV) files. If left blank, the system automatically detects the delimiter based on the file extension. |

### Tables replicated

Tables are created based on the table configuration (see above). Each table corresponds to a set of files in the Google Cloud Storage (GCS) bucket that match both the specified search pattern and any optional prefix.
The connector automatically discovers schemas by sampling up to 5 files per table, reading every fifth row, with a maximum of 1,000 records per file.

Replication is incremental and uses file modification timestamps to track changes. During each extraction, the connector processes only those files that have been modified since the last successful sync, as recorded by the sync bookmark.

The following system columns are added to each table by default:

| Column | Description |
| --- | --- |
| `_sdc_source_bucket` | The name of the Google Cloud Storage (GCS) bucket where the record was read. |
| `_sdc_source_file` | The full path of the file containing the record. |
| `_sdc_source_lineno` | The line number of the record within the file. |
| `_sdc_extra` | Any extra columns found during parsing that do not match the discovered schema. Applies to JSONL files only. |

## Limitations and considerations

- Service account credentials (`project_id`, `client_email`, `private_key`) must be provided as individual values extracted from the JSON key file; file upload is not supported.
- Gzip-compressed files (`.gz`) are supported. The connector reads the original filename from the gzip header to determine the inner file format. Gzip files created with `--no-name` (no filename stored in the header) are skipped.
- Nested compression (for example, a `.gz` inside another `.gz` or a `.zip` inside a `.zip`) is not supported. These files are skipped.
- Files with `.csv`, `.txt`, `.tsv`, `.psv`, or `.jsonl` extensions are checked for gzip magic bytes and decompressed if gzip-compressed—even when the file does not have a `.gz` extension.
- The `search_pattern` field uses regex and glob search pattern syntax. In regex, `*.csv` does not match CSV file names because `*` must follow an expression to repeat. Use `.*\.csv$` to match filenames such as `report.csv` and `my.data.csv`.
- The connector has built-in retry logic with exponential backoff for Google Cloud Storage (GCS) API rate limits (`429`) and transient server errors (`500`, `502`, `503`, `504`). Up to five attempts are made before failing.
- Files without a recognized extension are skipped and a warning is issued.
