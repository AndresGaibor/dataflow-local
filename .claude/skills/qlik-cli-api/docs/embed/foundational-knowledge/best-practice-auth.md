---
source: https://qlik.dev/embed/foundational-knowledge/best-practice-auth/
last_updated: 2023-12-12T15:15:01Z
---

# Auth best practices for embedding

Integrating an embedded SaaS like Qlik Cloud into your web application is made
easier when you follow these best practices.

## Use one identity provider for authentication

When you embed a SaaS into your web application, handling authentication
can be a poor user experience as end users may have to authenticate twice
through separate login entry points.

The best and easiest way to mitigate double-login is to conform the source and
target applications to use the same identity provider (IdP). Using the same IdP
allows the integrated applications to share the same user identity tokens in the
web browser. When the embedded SaaS makes requests to its backend, the SaaS
contacts the IdP, and the IdP tells the SaaS application an identity token
already exists, therefore the user is already authenticated. As a result, no
additional login splash pages or entry points appear for the user to get
through.

## Use OAuth2 for authorization

OAuth2 is the standard for web applications to access resources hosted by other
applications on behalf of a user or service. One of the main benefits of using
OAuth is that it implements token-based session management instead of cookie-based session management.
That means no more third-party cookie issues. Embedded applications like
Qlik Analytics are integrated most often into single-page
applications (SPA). You can create a single-page application
OAuth public clients from Qlik CLoud, and then use the client to complete the connection between your
web application and Qlik Cloud.

## Putting it together

Using the combination of one identity provider and OAuth2 assures your web
application and Qlik Cloud are going to work well together.
