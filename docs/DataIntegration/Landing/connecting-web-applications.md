---
title: "Connecting to SaaS applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/connecting-web-applications.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources"]
---

# Connecting to SaaS applications

You can land or replicate data from a large number of SaaS applications in Qlik Talend Data Integration.

To see all supported applications, go to [*Supported SaaS applications*](supported-saas-applications.htm).

Information note

For customers with Qlik Talend Cloud Standard, Qlik Talend Cloud Premium, or Qlik Talend Cloud Enterprise subscriptions, the best practice is to use *Data Movement gateway* when moving data from Infor, Jira, Microsoft Dynamics 365 CRM, NetSuite, Oracle Fusion, or Salesforce.

For more information, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm) documentation.

## Limitations and considerations of SaaS application connectors

When using a SaaS application connector, you should be aware of the following limitations and considerations:

### General limitations and considerations

- It is not possible to use the same SaaS application connector for more than one task, regardless of the task type
- Replication of LOB columns is not supported
- JSON column payloads in source datasets are not denested automatically on the target. The full fidelity of the source data is preserved: Nested and semi-structured content is delivered as native JSON for targets that support it, or as VARCHAR for those that do not.

### Why SaaS extraction is single-threaded

SaaS application connectors extract one table at a time, even when a task includes multiple tables. Database sources can read multiple tables in parallel, and tasks can write to multiple targets in parallel.

Most SaaS applications limit the number of API requests allowed within a given period. Connectors request data as quickly as the source permits and wait before retrying when the source applies a rate limit. Parallel table extractions would share the same request limit and could trigger more retries without increasing throughput.

Some applications also limit the number of active sessions for one set of credentials. Other connectors use authentication tokens that refresh with each request. Parallel extractions using the same credentials could invalidate each other's tokens and interrupt the task.

For details about SaaS API limits and connector retry behavior, see [*Managing SaaS API limits and backoff*](managing-saas-api-limits-and-backoff.htm).

### SaaS application Lite connectors

A small number of SaaS application connectors are categorized as Lite connectors. Lite connectors are marked with a Lite label, both in the UI and in the help.

Qlik may initially develop some connectors for a specific use case and then release them with a Lite label. Lite connectors are fully supported by Qlik in accordance with Qlik’s Service Level Agreement (SLA) for critical issues related to data integrity, security, and reliability. The primary distinction between standard connectors and Lite connectors is that Lite connectors are tested against a limited set of use cases.

### Change tables in landing and lake landing tasks

Typically, Change Tables are created only for source tables that support Change Data Capture (CDC). However, when the source is a SaaS application and the task type is Landing (data pipeline use case) or Lake Landing (replication use case), Change Tables are also created for tables that support only Full Load. This behavior is designed to address the increased likelihood of duplicate records when ingesting data from SaaS application sources. Duplicate records are added to the Change Tables before the data is propagated downstream, helping to ensure data quality and consistency.

## Connecting to a SaaS application

Connecting to SaaS applications might require you to set up Data Movement gateway, depending on your use case. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

Information noteWhen you connect to data sources, you might need to add underlying Qlik Cloud IP addresses to your allowlist. For more information, see [*Allowlisting domains and IP addresses*](../../Introduction/qlik-cloud-dns-ip.htm).

1. The first step of connecting to a SaaS application is to add a connection to the data source. You can do this in several ways.

   - In Connections, click Create connection.
   - Click Create connection where source connections are listed (for example, in the data task setup wizard).

   Select Application in Category to filter the list of connectors to SaaS application connectors.

   You can also select from recently used connectors.
2. Select which application to connect to.
3. Complete the connection details to authenticate the connection. The connection details and authentication process are different for each SaaS application.

   For more information, go to [*Connecting to SaaS applications*](#Supporte) and select your data source.

   Warning noteIf you are using Data Movement gateway and need to create a new task with a SaaS application connector, you must upgrade to Data Movement 2025.11.66 or later. Otherwise, the task will not run.

After you have configured your connection, you can use that connection in a pipeline project.
