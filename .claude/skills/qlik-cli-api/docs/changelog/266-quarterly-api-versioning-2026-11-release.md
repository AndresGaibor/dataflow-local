---
source: https://qlik.dev/changelog/266-quarterly-api-versioning-2026-11-release/
last_updated: 2026-11-10T16:53:24+01:00
---

# Quarterly API versioning and the 2026-11 API release

Qlik Cloud REST APIs and system events now follow a quarterly, date-based versioning policy.
API versions are released in February, May, August, and November, and use the `YYYY-MM` format.
Versioning started with `2026-05`, and `2026-11` is the latest release.

## Supported versions \{#266-supported-versions}

The following versions are supported from the November 2026 release:

- `2026-05`
- `2026-08`
- `2026-11`

Each release is supported for 12 months, unless otherwise specified.

## The `qlik-api-version` header \{#266-qlik-api-version-header}

For REST APIs, the `qlik-api-version` request header tells Qlik which API release your integration is aware of.
It doesn't select a fixed request or response structure.
Non-breaking changes, such as new endpoints, optional request parameters, and response properties, are deployed
continuously and are available regardless of the version you specify.

Qlik uses the acknowledged version to determine which version-dependent deprecation warnings to return.
If you omit the header, or specify an unsupported version, Qlik uses the oldest supported release.

For production integrations, specify a dated version and review relevant deprecation notices before updating it.

## Deprecations and sunsets \{#266-deprecations-and-sunsets}

Deprecations are documented in the API references and specifications. Additional information, including migration
guidance where available, is published in the [changelog](https://qlik.dev/changelog/).
REST APIs also communicate deprecations through the `deprecation`, `sunset`, and `link` response headers.
Deprecated functionality remains available during the deprecation period and may be removed on or after its sunset date.

For more information, including how to specify a version and how system events are versioned, see
[API versioning](https://qlik.dev/apis/versioning/).
