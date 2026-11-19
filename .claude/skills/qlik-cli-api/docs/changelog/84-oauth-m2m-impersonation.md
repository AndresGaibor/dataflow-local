---
source: https://qlik.dev/changelog/84-oauth-m2m-impersonation/
last_updated: 2026-01-19T14:21:00Z
---

# Introducing OAuth machine-to-machine impersonation for embedded analytics

When you embed Qlik Cloud into your web applications, you likely require an authentication
strategy that mitigates the [blocking of third-party cookies by browsers](https://community.qlik.com/t5/Official-Support-Articles/Need-to-Know-Embedding-Qlik-Analytics-and-the-End-of-Third-Party/ta-p/2158755).

Qlik is introducing support for OAuth impersonation tokens, which can be generated
using a confidential OAuth machine-to-machine client for users in your
Qlik Cloud tenant. Impersonation tokens are ideal for scenarios where:

- The identity provider for your web application does not match the one
  configured for your Qlik Cloud tenant.
- You wish to handle authentication on your backend.
- You wish to avoid client-side redirects in the browser.

If you intend to implement a client-side (front-end) authentication strategy or
if your web application does not have a back-end component, you should leverage
OAuth SPA
for your application.

**Considerations if moving from JWT**

This capability provides a comparable experience to using JWT to authenticate
from a web application to Qlik Cloud, with the benefit of not being blocked by
third-party cookie restrictions.

The key difference is that OAuth impersonation requires that users already
exist in the tenant and uses pre-existing user group mappings, rather than
supporting update of groups on the fly during token requests. This means that:

- Users must exist in the tenant prior to requesting an impersonation token. You can
  accomplish this with `qlik-api` as part of the login flow.
- You cannot update user-to-group mappings when requesting the impersonation token.
  If you wish to leverage groups for your security model, you should first impersonate
  a user login on the backend using JWT to associate the required groups with your user.

**Learn more about OAuth impersonation**

To discover more:

- Review the guiding principles
  for using OAuth impersonation in Qlik Cloud.
- Learn how to create a new client
  for requesting impersonation tokens.
- Explore how to retrieve impersonation tokens.
