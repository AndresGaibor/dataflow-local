---
source: https://qlik.dev/embed/iframe/
last_updated: 2026-02-24T11:23:58+01:00
---

# Iframes

> **Use qlik-embed for new integrations:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.

## Iframe

Iframe embedding allows sheets or objects to be integrated into web apps and portals, often without
the need for any JavaScript or other code. You only need an `iframe` tag, which can be generated on
any Qlik Sense page using the [App Integration API](https://qlik.dev/apis/javascript/app-integration/)
(for whole sheets), or [Single Integration API](https://qlik.dev/apis/javascript/single-integration/) (for
single objects). Iframes rely on cookies to authenticate the user for the session.

The App Integration API provides parameters that can be used to create an URL that returns a complete
HTML page containing the embedded app. For more information, see the
[Set default options for embedded applications from the URL guide](https://qlik.dev/embed/iframe/quickstart/app-integration-getting-started/).

With the Single Integration API, you can integrate single Qlik Sense visualizations, sheets, or snapshots
into an iframe. For more information, see the
[Embed single objects using iframes and the Single Integration API guide](https://qlik.dev/embed/iframe/quickstart/single-integration-getting-started/).

While iframes are often considered the simplest solution, they are flexible, and can even be used with
anonymous use cases when deployed in conjunction with other services or APIs. They can also be used with
other Qlik integration tools such as enigma.js to do things like setting themes within an iframe.

> **Performance impact of multiple iframes:** Each embedded iframe adds overhead and maintains its own connections (such as WebSockets).
> As the number of iframes increases, performance and reliability can degrade, especially on less powerful devices or
> unstable networks.
> For better performance and stability, use as few iframes as possible and avoid embedding many separate iframes on the same page.

### Prerequisite for using iframes

Web technology that supports iframes (for example, HTML)

### Use cases best suited for iframes

- When you want more native Qlik capability (sheets, data alerts, etc.).
- When you want a low-code solution for non-technical users.
- When you want to embed into a web page where security controls for content are lax.
- When you have framework isolation requirements (for example, the parent page is using Angular \< v2).

### Iframe examples

- [Set the theme for embedded iframe content with enigma.js](https://qlik.dev/embed/iframe/customize/set-content-theme-for-iframe-with-enigma)
