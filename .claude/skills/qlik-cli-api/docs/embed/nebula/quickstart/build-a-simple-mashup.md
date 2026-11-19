---
source: https://qlik.dev/embed/nebula/quickstart/build-a-simple-mashup/
last_updated: 2026-06-02T18:15:45+01:00
---

# Build a simple mashup using nebula.js

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) rather than this framework.\
> For more information, review the [embedding Qlik Analytics using qlik-embed web components tutorial](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-webcomponent-quickstart).

> **Third-party cookies:** This tutorial leverages cookies for auth, which are blocked by some browser vendors.
> Please use an OAuth solution where possible, which doesn't leverage cookies.

This guide walks you through creating a simple mashup that connects to Qlik
Cloud and visualizes some data.

It includes the following steps:

1. Set up a Qlik Cloud Analytics tenant.
2. Create a simple web project.
3. Configure connection.
4. Visualize data.

This guide requires that you have:

- `node.js` `v10.0.0+` installed on your machine
- A decent IDE, [VS Code](https://code.visualstudio.com/) is recommended.

## Set up a Qlik Cloud Analytics tenant

Although `nebula.js` works and can be integrated with all Qlik Sense products,
this guide shows you how to integrate with Qlik Cloud Analytics.

Perform the following steps:

1. [Register for a subscription on Qlik Cloud Analytics](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qcs-register.htm).
2. [Configure your deployment](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qcs-tenant-domain.htm).
3. [Create a new web integration](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-adminster-web-integrations.htm)
   from the [Management console](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/management-console.htm).
   1. You later run the mashup from your local machine; to allow this
      connection to happen, you should add `http://localhost:1234` to the whitelist
      of origins.
   2. Once the web integration has been created, an ID is assigned to it;
      this is the `qlik-web-integration-id` you need later on.
4. [Upload an app](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/create-app-cloud-hub.htm)
   1. If you don't have an app or data already prepared, you can
      [download the movies dataset](https://github.com/qlik-oss/nebula.js/blob/main/data/apps/the_movies.qvf)
      from the GitHub repository and upload it to the cloud.

Each Qlik Sense app on Qlik Cloud has a global unique identifier (GUID), which you need
later on. The GUID can be extracted from the URL and is the part that
follows `/app`. For example, if the URL is `https://your-tenant.us.qlikcloud.com/sense/app/7fc4d85c-0e07-4160-90a9-c2ca4a45fd81`
, then the GUID of the app is `7fc4d85c-0e07-4160-90a9-c2ca4a45fd81`.

## Create a simple web project

The quickest way to create a web project is to use the `nebula.js` command line
interface:

```bash
npx @nebula.js/cli create mashup hello-saas
```

The command scaffolds a web project into the `hello-saas` folder with the
following structure:

- `/src`
  - `configure.js` - Initial configuration of `nebula.js`
  - `connect.js` - Connection setup with `enigma.js`
  - `index.html` - A minimal HTML page
  - `index.js` - Connect and visualize

`/src/index.js` is where you need to make modifications later on to bring
everything together.

## Configure connection

To configure the connection, you need the following:

- The Qlik Cloud tenant URL.
- The web integration ID (`qlik-web-integration-id`).
- The GUID of the app you want to open.

Open up `src/index.js` and update the `<>` placeholders with the correct values,
for example:

```js
const app = await connect({
  url: "https://your-tenant.us.qlikcloud.com",
  webIntegrationId: "8Ys9sBVyq6i2lxtclPWaaZhQr7OgwKaT",
  appId: "7fc4d85c-0e07-4160-90a9-c2ca4a45fd81",
});
```

## Visualize data

The movies dataset you uploaded earlier has a bar chart on the first sheet with
the ID `EAjjuyE`. You can render that same bar chart in your mashup by providing
the ID and an element to render the visualization into:

```js
n.render({
  element: document.querySelector(".object"),
  id: "EAjjuyE",
});
```

To get the object Id of a chart you do the following:

- Right click the chart object itself or open context menu to select "share“.
- Then select "Embed"
- Find and copy the object Id

![Chart embed dialog displays object Id](https://qlik.dev/_astro/chart-object-id.DSWq0Ohv.png)

Start the web development server by executing the following in a terminal:

```bash
npm run start
```

The server runs on `http://localhost:1234`.

When opening the page, you may be re-routed to your tenant to
sign in if the session timed out since you did the setup. Once signed in, you
are re-routed back to the development server where you should see the same bar
chart:

![Bar chart representing 'Top grossing movies of all time'](https://qlik.dev/_astro/mashup-sample.CReApNUY.png)

The visualization is fully interactive, any selections you make are
reflected in the current app selections toolbar at the top.

## More visualizations

### Render on the fly

You can render a visualization without having to create it in the app by
providing the `type` and some data `fields`:

```js
n.render({
  element: document.querySelector(".object"),
  type: "barchart",
  fields: ["title", "=avg(rating)"],
});
```

### More types

The core `stardust` module doesn't contain any visualizations. Each
visualization is its own separate module and needs to be loaded and registered
before it can be used.

Official visualizations from Qlik are published under the `@nebula.js` scope
and are prefixed with `sn-`.

For a list of available visualizations, see [Supported charts](https://qlik.dev/embed/nebula/render/supported-charts/).
The template you created your mashup from only includes the `bar-chart` module.
You can add more types by installing each one you want to use:

```bash
npm install @nebula.js/sn-pie-chart
```

Then modify `/src/configure.js` to include the new modules:

```js
import piechart from '@nebula.js/sn-pie-chart';
//...

embed.createConfiguration({
  // ...
  types: [
    // ...
    {
      name: 'piechart',
      load: () => Promise.resolve(piechart)
    }
  ];
}
```

### Without node and a bundler

While it is recommended to use a bundler like Webpack, Rollup, or Parcel
to get the most out of your mashup development, it is still possible to
use Nebula with regular `<script>` tag imports on any web page.

```html
<script src="https://cdn.jsdelivr.net/npm/@nebula.js/stardust"></script>
<script src="https://cdn.jsdelivr.net/npm/@nebula.js/sn-bar-chart"></script>
<script src="https://cdn.jsdelivr.net/npm/enigma.js"></script>
```

By importing the packages this way, they will be available on the global
window object like this:

```js
const embed = window.stardust.embed;
const barchart = window[`sn-bar-chart`];
const enigma = window.enigma;
```

They can then be used as normal.
