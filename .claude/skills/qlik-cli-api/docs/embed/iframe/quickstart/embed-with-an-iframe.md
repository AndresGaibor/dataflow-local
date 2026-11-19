---
source: https://qlik.dev/embed/iframe/quickstart/embed-with-an-iframe/
last_updated: 2025-07-08T16:09:30Z
---

# Embed a visualization to a web application with an iFrame

> **Use qlik-embed for new integrations:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
>
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.
>
> To do something similar with qlik-embed, refer
> to [embedding Qlik Analytics using qlik-embed web components](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-webcomponent-quickstart)
> and leverage the `classic/app` UI.

This tutorial is a step-by-step demonstration of embedding objects
using iFrames, which is a simple way to get started with embedding Qlik available
via the Qlik Sense interface.

If you want to build more custom and integrated experiences for your users,
take a look at the other tools and technologies available for embedding
Qlik technologies in [embedding overview](https://qlik.dev/embed/which-framework).

## 1: Generate the HTML code for the specific object

Qlik Cloud supports two types of embedded objects in an iframe: sheets
and charts.

To embed a Qlik Sense sheet, open the Qlik Sense application that you wish to
embed, open the sheet of interest, and click the drop down menu in the
upper left corner. Select “Embed sheet”.

![Dropdown menu with embed sheet highlighted](https://qlik.dev/_astro/embed_sheet.CUxr1PV0.png)

If you instead wish to embed an individual chart/object, rather than a full
sheet, right-click an object, click the Navigation button (three dots), then
select Share > Embed.

![Right click menu with embed chart highlighted](https://qlik.dev/_astro/embed_chart.JxS9zlQC.png)

Once you've done this for either a sheet or chart/object, a window appears
allowing you to configure various properties for the embedded object. At the
bottom of this window, you'll see the HTML code for the iframe, which can be
inserted directly into your web application or mashup.

> **Note:** The embed dialog also shows you the ID of the sheet or object you've selected to embed.
> These IDs are useful if you are building integrations with other Qlik APIs or frameworks such as the capability APIs
> and enigma.js.

![Embed sheet preview with sheet ID and iframe highlighted](https://qlik.dev/_astro/embed_sheet_preview.DDNiU9k7.png)

## 2: Configure a Content Security Policy

If you haven't already, configure a Content Security Policy entry for the web
application that will embed the iframe, setting the `frame-ancestors` directive.

For more information on how to do this, see
[Content Security Policies for embedding iframes](https://qlik.dev/embed/iframe/authenticate/csp-iframe-config/).

## 3: What next?

### Authentication

This approach assumes that you are leveraging an interactive Identity Provider on
Qlik Cloud. If your web application does not leverage the same configuration as
your Qlik Cloud tenant, then end users may be redirected away from your web
application to sign in to Qlik Cloud before they can see embedded content.

To improve this experience for your end users, explore:

- [Handling
  user sessions with iframes and enigma.js (interactive Identity Providers)](https://qlik.dev/embed/iframe/authenticate/managing-iframe-session-with-enigma)
- [Handling
  user sessions with iframes and enigma.js (JSON Web Token Identity Providers)](https://qlik.dev/embed/iframe/authenticate/managing-iframe-embedded-content-session-state-using-enigmajs-and-json-web-tokens)

Additionally, if you have users who access iframe embedded content on devices
which do not support third party cookies,
see [Third-party
cookie handling with embedded content](https://qlik.dev/embed/iframe/authenticate/third-party-cookie-handling-with-embedded-content).

### Customization

If you want to build more custom and integrated experiences for your users,
take a look at the other tools and technologies available for embedding
Qlik technologies in [embedding overview](https://qlik.dev/embed/which-framework).
