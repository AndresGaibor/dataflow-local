---
source: https://qlik.dev/changelog/185-namespaced-apis/
last_updated: 2025-12-01T10:31:29+01:00
---

# Introducing Namespaces in Qlik Cloud APIs

Namespaces for REST and Events APIs are being introduced in Qlik Cloud to support the growing number of APIs and
services in the platform, and to unlock versioning support in the future. This change makes it easier for you to
find, understand, and use Qlik APIs by grouping related resources by context, as well as standardizing the interface
for the APIs.

## What to expect \{#185-what-to-expect}

- The new namespaced APIs will be introduced in parallel with the existing APIs.
- The existing APIs will be deprecated and removed after a **minimum** 12-month deprecation period from the
  notice of deprecation on the [changelog](https://qlik.dev/changelog).
- No immediate action is needed. As each API is namespaced, a deprecation notice will be published with migration
  guides.

## Key changes \{#185-key-changes}

### REST \{#185-key-changes-rest}

1. **Removal of `v1` from the path**: `v1` will be removed from the path to prepare for versioning support in the
   future.
2. **Grouping resources by context**: Related APIs will be grouped together under a namespace which indicates in which
   context the resources are applicable. For example:
   - The `analytics` namespace for Analytics-specific resources such as apps, notes, and ODAGs apps.
   - The `core` namespace for platform-wide resources such as users, groups, ip-policies, and roles.
3. **Standardization of interfaces**: The payloads for the new namespaced APIs will be standardized to be compliant
   with Qlik's API design principles, meaning improved consistency of payloads, query parameters, and response formats
   between different APIs, irrespective of the context.

### Events \{#185-key-changes-events}

Events will adhere to the same namespace rule to avoid conflict of resource names and to match the REST resources.
This changes the pattern from `com.qlik.v<version>.<eventContext>.<action>`
to `com.qlik.<namespace>.<eventContext>.<action>`.

## Learn more \{#185-learn-more}

To learn more about the namespaced API changes, see the [API namespaces overview page](https://qlik.dev/apis/namespaces/).
