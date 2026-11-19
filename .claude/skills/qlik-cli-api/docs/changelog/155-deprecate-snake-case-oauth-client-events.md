---
source: https://qlik.dev/changelog/155-deprecate-snake-case-oauth-client-events/
last_updated: 2025-07-22T13:46:22Z
---

# Deprecation notice - snake_case fields in OAuth-client events will be removed on or after October 22, 2025

> **Deprecation notice:** The `snake_case` fields in OAuth-client events are now deprecated and will be removed on or after October 22, 2025.

OAuth-client events now include both `snake_case` and `camelCase` field formats to ease the transition for customers
parsing them.
For example, OAuth-client event payloads temporarily contain both `app_type` and `appType`.

If you're consuming OAuth-client events via the [Audits API](https://qlik.dev/apis/rest/audits/), you should update your
integrations to use the `camelCase` fields. OAuth event names start with `com.qlik.v1.oauth-client`.

For more information, see the [Audits API reference](https://qlik.dev/apis/rest/audits/).
