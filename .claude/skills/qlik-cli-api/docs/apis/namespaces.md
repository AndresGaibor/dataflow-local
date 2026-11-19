---
source: https://qlik.dev/apis/namespaces/
last_updated: 2026-11-10T16:53:24+01:00
---

# API namespaces

Namespaces for REST and Events APIs are being introduced in Qlik Cloud to support the growing number of APIs and
services in the platform. They group related resources by context and standardize API interfaces.
For information about API versioning and deprecation, see [API versioning](https://qlik.dev/apis/versioning/).

Subscribe to the [changelog](https://qlik.dev/changelog) for updates. As each API is namespaced, a deprecation notice
will be published, providing a minimum 12-month notice period for migration, and migration guides will be provided.

## What to expect: Implication on existing APIs

- The new namespaced APIs will be introduced in parallel with the existing APIs.
- The existing APIs will be deprecated and removed after a **minimum** 12-month deprecation period from the notice
  of deprecation on the [changelog](https://qlik.dev/changelog). The API reference will clearly indicate the deprecated API, and the
  new namespaced API.

## Key changes

### REST

1. New namespaced REST APIs use a namespace in place of the `/v1/` path segment (for example, `/api/analytics/apps`).
   Legacy `/api/v1/` APIs continue to coexist during migration, with deprecations announced in the [changelog](https://qlik.dev/changelog).
   Header-based API versioning is independent of this URL migration.
2. **Grouping resources by context**: Related APIs will be grouped together under a namespace which indicates in which
   context the resources are applicable. For example:
   - The `analytics` namespace will contain APIs which are context specific to Analytics, such as APIs for
     managing apps, notes, ODAGs, and other Analytics-specific resources which require the context of an analytics
     application to be used.
   - The `core` namespace will contain APIs which are applicable to the entire platform, irrespective of the context.
     For example, APIs for managing users, groups, ip-policies, and roles.
   - The `ai` namespace will contain APIs which are context specific to AI, such as APIs for managing AI assistants,
     knowledgebases, and other AI-specific resources.
   - The `data-governance` namespace will contain APIs which are context specific to data governance, such as APIs for
     managing data products, data lineage, and other data governance-specific resources.
   - The `machine-learning` namespace will contain APIs which are context specific to machine learning, such as APIs for
     managing machine learning models, machine learning deployments, and other machine learning-specific resources.
   - The `telemetry` namespace will contain APIs which are context specific to telemetry, such as APIs for managing
     audit logs, consumption metrics, and other telemetry-specific resources.
3. **Standardization of interfaces**: The payloads for the new namespaced APIs will be standardized to be compliant
   with Qlik's API design principles, meaning improved consistency of payloads, query parameters, and response formats
   between different APIs, irrespective of the context.

For example, after applying the namespace changes, the following REST API paths would be renamed:

```diff
- /v1/apps
+ /analytics/apps

- /v1/ip-policies
+ /core/ip-policies

- /v1/users
+ /core/users
```

Grouping resources by context reduces conflicts and confusion between different parts of the Qlik Cloud product
offering.

### Events

Events will adhere to the same namespace rule to avoid conflict of resource names and to match the REST resources.

This changes the pattern from:

```diff
-com.qlik.v<version>.<eventContext>.<action>
+com.qlik.<namespace>.<eventContext>.<action>
```

For example, after applying the namespace changes, the following events would be renamed:

```diff
- com.qlik.v1.app.created
+ com.qlik.analytics.app.created
```

### Namespace information

Each namespace groups related APIs by product area or platform capability.
The following namespaces are currently available:

| Namespace         | Description                                                                                                    |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| `ai`              | APIs for integrating AI capabilities and tool execution into task-oriented applications.                       |
| `alerting`        | APIs for managing alerts, scheduled reporting, subscriptions, and related notification workflows.              |
| `analytics`       | APIs for building analytics experiences using dynamic generation and discovery workflows.                      |
| `connectivity`    | APIs for managing data connectivity resources, including data sources, connections, credentials, and gateways. |
| `core`            | APIs for administering security, identity, access controls, and operational resources.                         |
| `data-governance` | APIs for governing trusted data products and quality controls across the organization.                         |
| `workflows`       | APIs for automating business processes and connecting external systems into unified workflows.                 |
