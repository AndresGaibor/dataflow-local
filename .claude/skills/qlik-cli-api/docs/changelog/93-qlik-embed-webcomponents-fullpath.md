---
source: https://qlik.dev/changelog/93-qlik-embed-webcomponents-fullpath/
last_updated: 2025-07-08T16:09:30Z
---

# Update your qlik-embed web components script src path

## qlik-embed web components script src attribute changes

A change to the latest release of qlik-embed web components requires references
to the `index.min.js` file be specified for the library to run.

If you are using qlik-embed web components it is recommended you update the `src`
property of the `script` element declaring the full path to the library.

Update the attribute to include `/dist/index.min.js` in the path. Here is an example of
the new path for the `src` attribute:
`src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"`.

> Note: If you do not want to use the latest version of qlik-embed web components, it is
> possible to set the version in the path.

Here is an example of the `src` attribute referencing a pinned version of qlik-embed
web components:
`src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1.1.1/dist/index.min.js"`.

## qlik-embed oauth callback page src attribute changes

Update the oauth-callback page used to handle connectivity between qlik-embed web components
and your Qlik Cloud tenant. Set the `src` attribute to use `oauth-callback.min.js`.

The resulting `src` attribute should look something like this:
`src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/oauth-callback.min.js"`.

You can learn more about qlik-embed
on the [Why qlik-embed](https://qlik.dev/embed/qlik-embed/why-qlik-embed/) page.
