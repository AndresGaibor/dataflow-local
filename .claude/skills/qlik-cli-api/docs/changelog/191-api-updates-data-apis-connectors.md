---
source: https://qlik.dev/changelog/191-api-updates-data-apis-connectors/
last_updated: 2026-01-19T14:21:00Z
---

# Updated APIs - Data Connections and Data Credentials APIs add support for Data Integration connectors

The [Data Connections](https://qlik.dev/apis/rest/data-connections/), [Data Sources](https://qlik.dev/apis/rest/data-sources/),
and [Data Credentials](https://qlik.dev/apis/rest/data-credentials/) APIs now support Data Integration connectors.
This enables programmatic creation and management of data connections for both Qlik Cloud Analytics applications
and Data Integration projects, enabling end-to-end deployment automation via public APIs.

The following table lists the supported connectors, along with their corresponding
`dataSourceId` values for use when creating data connections:

<details>
  <summary>Supported connectors</summary>

  | Connector                                  | dataSourceId                  |
  | ------------------------------------------ | ----------------------------- |
  | Amazon Redshift                            | `reptgt_qdiredshift`           |
  | Amazon S3                                  | `reptgt_qdis3`                 |
  | Azure Data Lake Storage                    | `reptgt_qdiadls`               |
  | Azure Synapse Analytics                    | `reptgt_qdisynapse`            |
  | Databricks                                 | `reptgt_qdidatabricks`         |
  | Google BigQuery                            | `reptgt_qdibigquery`           |
  | Google Cloud Storage                       | `reptgt_qdigooglecloudstorage` |
  | IBM DB2 for iSeries                        | `repsrc_db2iseries`            |
  | IBM DB2 for LUW                            | `repsrc_db2luw`                |
  | IBM DB2 for z/OS                           | `repsrc_db2zos`                |
  | Microsoft Fabric                           | `reptgt_qdimicrosoftfabric`    |
  | Microsoft SQL Server                       | `reptgt_mssqltarget`           |
  | Microsoft SQL Server (log based)           | `repsrc_mssql`                 |
  | Microsoft SQL Server (Microsoft CDC based) | `repsrc_azuresqlmscdc`         |
  | MySQL (source)                             | `repsrc_mysql`                 |
  | MySQL (target)                             | `reptgt_qdimysql`              |
  | Oracle (source)                            | `repsrc_oracle`                |
  | Oracle (target)                            | `reptgt_qdioracle`             |
  | PostgreSQL (source)                        | `repsrc_postgresql`            |
  | PostgreSQL (target)                        | `reptgt_qdipostgresql`         |
  | SAP (Application)                          | `repsrc_sapdbapplication`      |
  | SAP Extractor                              | `repsrc_sapextractor`          |
  | SAP HANA (Database)                        | `repsrc_saphana`               |
  | SAP ODP                                    | `repsrc_sapodp`                |
  | Snowflake                                  | `reptgt_qdisnowflake`          |
</details>

For more information, see:

- [The Data Connections API reference documentation](https://qlik.dev/apis/rest/data-connections/)
- [The Data Sources API reference documentation](https://qlik.dev/apis/rest/data-sources/) to list the available data sources for
  the creation of data connections.
- [Example data connection creation requests](https://qlik.dev/manage/data-connections/examples/data-connection-create-examples/)
