---
title: "Azure Cloud Storage Preview"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-Azure-Cloud-Storage.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to cloud storage"]
---

# Azure Cloud Storage  [Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Azure Cloud Storage is Microsoft’s managed object storage service for unstructured data, including text, binary files, media, logs, and application backups. It supports hot, cool, and archive access tiers, offers geo-redundant replication, and integrates with Microsoft Entra ID (formerly Azure Active Directory) for secure access control.

Qlik Talend Cloud connects to Azure Cloud Storage using a Microsoft Entra ID application (service principal) that has read access to the target storage account container. The connector retrieves files from the specified container, automatically discovers schemas by sampling file contents, and performs incremental data replication based on file modification timestamps.

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

To set up your Azure Cloud Storage account, you need:

- An Azure subscription with an Azure Storage account.
- A blob container in the storage account that contains the files to replicate.
- A Microsoft Entra ID application registration with a client secret.
- The Storage Blob Data Reader role assigned to the application's service principal, scoped to the storage account or the specific container. This is the recommended least-privilege role for read-only access.

To register a Microsoft Entra ID application and retrieve your credentials:

1. Log into your [Azure](https://portal.azure.com/) account.
2. Navigate to Microsoft Entra ID > App registrations > New registration.
3. Enter the following information for your application:
   - Name: Enter a name, for example QlikDataIntegration.
   - Supported account types: Select Accounts in this organizational directory only.
4. Click Register.
5. On the application Overview page, copy both the Application (client) ID and Directory (tenant) ID and save them to a secure file.
6. Navigate to Certificates & secrets > Client secrets > New client secret.
7. Enter a description and select an expiration period for the client secret.
8. Click Add.
9. Copy your client secret value and save it to a secure file.
10. In the Azure portal, open your storage account, then navigate to Access Control (IAM) > Add > Add role assignment.
11. Select the Storage Blob Data Reader role, and assign this role to the application you just registered.
12. Click Save.

### Supported file formats

- Delimited text files: `.csv`, `.tsv`, `.psv`, `.txt` (with configurable delimiter)
- JSON Lines: `.jsonl`
- Parquet: `.parquet`
- Avro: `.avro`
- Excel: `.xlsx` (multiple worksheets per workbook are supported; each sheet's rows are replicated, and the sheet name is appended to the `_sdc_source_file` column)
- Gzip-compressed files: `.gz` (containing any of the above formats)

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
| Storage Account Name | Name of the Azure Storage account, for example mystorageaccount without `https://` or `.blob.core.windows.net`. |
| Container Name | Blob container name, for example my-container. |
| Tenant ID | Tenant ID. |
| Tables | Table configuration determines which files are read and how their contents are interpreted. Each table definition includes a file search pattern, a table name, and optional settings for customizing file handling. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

### Tables configuration

Each entry in the tables configuration represents a logical table derived from files in the container. The following properties can be configured for each table:

| Property | Required or Optional | Description |
| --- | --- | --- |
| Table name | Required | Specify the name of the logical table (for example, `my_orders_csv`). This becomes the stream name in Qlik Talend Cloud. |
| Search pattern | Required | Provide a regular expression to match file names (for example, `.*\.csv$` matches all CSV files). Apply this to file names within the container or the specified directory, if provided. |
| Directory | Optional | Enter a folder path prefix within the container to narrow the file search (for example, `exports/orders/`). Improve performance by limiting the files scanned. This is not a regular expression. |
| Primary key | Optional | Define a comma-separated list of column names to use as the primary key (for example, `id` or `id,date`). For CSV files, use header field names; for JSONL files, use top-level object keys. Leave empty to use full-table replication. Populate to enable incremental replication based on file modification time. |
| Specify datetime fields | Optional | List the column names, separated by commas, to treat as datetime fields, even if not automatically detected during schema discovery (for example, `created_at`, `updated_at`). |
| Delimiter | Optional | Indicate the field separator for delimited text files. The default is `,` (comma). Use `\t` for TSV files or `|` for PSV files. If not specified, the delimiter is auto-detected based on the file extension. |

- Configure `.jsonl` and `.csv` files as separate tables to ensure accurate schema handling and data consistency.
- Ensure all `.csv` files matching a search pattern include a consistent header row with identical column names and order.
- Use consistent object attribute keys across all `.jsonl` files defined for each table. Key names and structures should align for reliable schema detection.

### Tables replicated

Tables are defined in the tables configuration that you provide. Each table corresponds to a set of files in the blob container that match the specified search pattern and, if applicable, the directory prefix. The connector discovers the table schema by sampling up to five files per table, reading every fifth row, and analyzing up to 1,000 records per file.

Replication uses an incremental approach based on file modification timestamps when a primary key is configured. Files modified after the last sync bookmark are processed during each extraction. If no primary key is specified, the entire table is fully replicated on every run.

The following system columns are added to each table by default:

| Column | Description |
| --- | --- |
| `_sdc_source_container` | The name of the Azure blob container where the record originated. |
| `_sdc_source_file` | The full path of the file containing the record. For Excel files, the sheet name is appended (for example, `exports/q1.xlsx/Sheet1`). |
| `_sdc_source_lineno` | The line number of the record within the file. |
| `_sdc_extra` | Extra fields parsed that do not match the discovered schema (`.jsonl` files only). |

## Limitations and considerations

- The storage account name is supplied as a bare name, not a URL.
- Gzip-compressed files (`.gz`) are supported. The connector reads the original filename from the gzip header to determine the inner file format. Gzip files created with `--no-name` (no filename in the header) are skipped.
- Files with `.csv`, `.txt`, `.tsv`, `.psv`, or `.jsonl` extensions are checked for gzip magic bytes and are transparently decompressed, even if the file does not have a `.gz` extension.
- Nested compression (for example, a `.gz` file inside another `.gz`) is not supported and is skipped.
- The Search pattern field uses regular expression syntax, not glob patterns (for example, use `.*\.csv$` instead of `*.csv`).
- Files without a recognized extension are skipped, and a warning is issued.
- The connector includes built-in retry logic with exponential backoff for Azure API rate limits (HTTP 429) and transient server errors (HTTP 500, 502, 503, 504), up to five attempts.
- File encoding is expected to be UTF-8.
