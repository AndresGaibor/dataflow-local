---
source: https://qlik.dev/changelog/199-qlik-embed-oauth-callback-updates/
last_updated: 2026-03-23T10:04:39Z
---

# Standardized OAuth callback approach for qlik-embed across all frameworks

OAuth callback examples in the [qlik-embed authentication guide](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/) and
quickstart guides now use the
[`@qlik/api`](https://qlik.dev/toolkits/qlik-api/) package instead of the `qlik-embed-webcomponents` package.

The OAuth callback functionality is now standardized under `@qlik/api` as the recommended approach across all
frameworks.
Whether you're using web components, Svelte, or another framework, you can use the same OAuth callback solution from
`@qlik/api`.
The `qlik-embed-webcomponents` version is maintained for backwards compatibility but is no longer the primary
recommendation.

If you're currently using `qlik-embed-webcomponents` for OAuth callback handling, consider migrating to `@qlik/api` for
a more flexible and framework-independent approach.
