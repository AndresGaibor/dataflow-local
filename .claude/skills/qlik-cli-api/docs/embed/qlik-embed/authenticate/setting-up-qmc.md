---
source: https://qlik.dev/embed/qlik-embed/authenticate/setting-up-qmc/
last_updated: 2026-10-02T14:35:27+02:00
---

# Configure Qlik Sense Enterprise client-managed

This section shows how to set up the default authentication configuration of Qlik Sense Enterprise
client-managed for cross-domain embedding with authenticated users. If other authentication
mechanisms are used, the configuration shown here may not be valid.

> **Anonymous access:** For public embedding without user login, see
> [Embed analytics with anonymous access on Qlik Sense Enterprise client-managed](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-client-managed-anonymous-tutorial/).
> Anonymous access requires additional virtual proxy configuration.

To connect to Qlik Sense Enterprise client-managed with a cross-domain application the following
should be configured in the Qlik Management Console:

1. Navigate to "Virtual proxies" to configure the virtual proxy that will accept the connection for your
   embedded app. In most cases, this will be a new virtual proxy, rather than the default virtual proxy that
   you use for development and site management.
2. Select "Advanced" to access the advanced settings.
3. Change "SameSite attribute" (for http, https, or both) to "None" .
4. Add the following headers to the "Additional response headers" section:

```text
Access-Control-Allow-Credentials: true
Access-Control-Expose-Headers: Qlik-Csrf-Token
```

5. Add the hostname of the external cross-domain site that connects to Qlik Sense,
   for example `external-site.com`, to "Host allow list", including the port if applicable.

When developing a third-party application that integrates with Qlik Sense, the external
cross-domain site is likely hosted on `localhost`. Add the development hostname and port,
for example `localhost:4000`, to "Host allow list".
