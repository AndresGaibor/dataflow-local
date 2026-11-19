---
source: https://qlik.dev/changelog/60-api-data-connections-dcaas/
last_updated: 2025-07-08T16:09:30Z
---

# New analytics data connection API

> **Updated on December 6, 2024**: The API referenced in this changelog is now deprecated.
> For more information, [review this changelog](https://qlik.dev/changelog/102-api-deprecation-dcaas/).

Qlik Sense applications running in Qlik Cloud rely on Analytics Data Connections
to load data from external sources. The
new Data Connectivity as a Service (DCaaS) API
provides you with the ability to provision new Analytics Data Connections to supported
sources using any supported authentication type.

This release of the DCaaS API supports creation of direct connections to:

- REST
- Microsoft SQL Server
- Databricks
- Google Big Query
- Amazon S3 (Web Storage and Metadata, via either v1 or v2 connector)
- Google Cloud Storage (Web Storage and Metadata)
- SFTP
- SFDC

> **Note:** Connections via the Direct Access or Data Movement Gateway are not
> supported in this release. Non-analytics data connections cannot be configured
> via DCaaS.

Additionally, support for calls to paths `/api/v1/dcaas` and `/api/v1/data-credentials`
have been added to the Raw blocks in the Qlik Cloud Services connector in
Qlik Automate (Qlik Platform Operations allows all endpoints by default).

## Learn more about Analytics Data Connections

To discover more about how to create Analytics Data Connections:

- Review the [data connections](https://qlik.dev/manage/data-connections/) topic
  to learn about the overall capability.
- Visit the [create a connection](https://qlik.dev/manage/data-connections/create-data-connections/)
  tutorial to begin creating new connections.
