---
source: https://qlik.dev/embed/foundational-knowledge/find-ids/
last_updated: 2026-06-09T09:30:16+01:00
---

# Find IDs for embedding

This section shows how to find IDs for common Qlik Sense embedded resources.

## Qlik Sense app ID

Each Qlik Sense app in a Qlik Cloud tenant has a unique identifier, called a resource ID,
in GUID format (for example, `f9892da0-e236-466b-9ea4-107b4adc7991`).
This resource ID is used as the handle for opening the app.

> **Note:** The observant may spot that an app also has a corresponding item ID, which has a UID format
> such as `663115d4717b087f30d19604`.
> The item ID is used in catalog and search, and cannot be used for embedding.

You can find the app ID from an Activity Center or the app URL.

### Find the app ID from an Activity Center

The **Details** view in the activity center displays the resource ID for an app.

1. Navigate to the card for the app you wish to embed.
2. Click the **ellipses**.

![a screenshot of a tile in an activity center](https://qlik.dev/_astro/app-ac-1.CWEH_nca.png)

3. Select **Details** to open the app details window.

![a screenshot of the details menu](https://qlik.dev/_astro/app-ac-2.fFHy9jWr.png)

4. Copy the ID displayed in the **App ID** section.

![a screenshot of the details pane showing the app GUID](https://qlik.dev/_astro/app-ac-3.D-I39pUF.png)

### Find the app ID from the URL

Open the Qlik Sense app that you wish to embed. Take the URL from your browser,
which will look like `https://tenantname.us.qlikcloud.com/sense/app/b0702f9b-46a3-46ff-8c8e-3a5f83a9b898/...`.

The ID is the value immediately following `app/`, in this case
`b0702f9b-46a3-46ff-8c8e-3a5f83a9b898`.

## Qlik Sense sheet ID

A sheet is a canvas onto which visualizations are added, sometimes known as a dashboard.
A Qlik Sense app can have many sheets, and each sheet has a unique ID. A sheet is
a type of app object, meaning that each ID is
unique only within the app, so if the app is duplicated, the new copy of
the app will have identical sheet IDs to the original version.

The format of a sheet ID will either be:

- A GUID, such as `b4681bfa-c763-497b-a0cf-984f933c3080`, if the sheet was duplicated
  from an existing sheet.
- A shorter ID, such as `NHnMB`, if the sheet was created new.

You can find the sheet ID from the embedding dialog or the sheet URL.

### Find the sheet ID in the UI

The embedding dialog for a sheet includes the sheet ID.

1. In a Qlik Sense app, navigate to the **Assets** pane.
2. Select **Sheets**.
3. Click the **ellipses** for the sheet you wish to embed.

![a screenshot of a sheet in the assets pane](https://qlik.dev/_astro/sheet-1.Dh_Jb2qv.png)

4. Select **Embed** to open the embedding window.

![a screenshot of the details menu](https://qlik.dev/_astro/sheet-2.kcXSvk74.png)

5. Copy the ID displayed next to **Sheet ID** below the preview.

![a screenshot of the preview window showing the sheet ID](https://qlik.dev/_astro/sheet-3.BufS2UnP.png)

### Find the sheet ID from the URL

Open the Qlik Sense sheet that you wish to embed. Take the URL from your browser,
which will look like `https://tenantname.us.qlikcloud.com/sense/app/b0702f9b-46a3-46ff-8c8e-3a5f83a9b898/sheet/NHnMB/...`.

The ID is the value immediately following `sheet/`, in this case `NHnMB`.

## Qlik Sense chart ID

A chart is an object type which carries a definition for a visualization within
a Qlik Sense app. As an app object, IDs are unique only within the app, as with sheets.

The format of a chart ID is the same as for sheet IDs.

You can find the chart ID from the embedding dialog or using the developer mode.

### Find the chart ID in the UI

The embedding dialog for a chart includes the chart ID.

1. In a Qlik Sense app, navigate to the sheet containing your chart.
2. Click the **ellipses** for the chart you wish to embed.

![a screenshot of a chart](https://qlik.dev/_astro/chart-1.tgzclSy5.png)

3. Select **Share**.

![a screenshot of the details menu](https://qlik.dev/_astro/chart-2.DpRARM3q.png)

4. Select **Embed** to open the embedding window.

![a screenshot of the share menu](https://qlik.dev/_astro/chart-3.qvwTc8Wq.png)

5. Copy the ID displayed next to **Object ID** below the preview.

![a screenshot of the preview window showing the object ID](https://qlik.dev/_astro/chart-4.ib04merj.png)

### Find the chart ID in developer mode

Qlik Sense includes a developer mode to help investigate chart properties.

1. In a Qlik Sense app, navigate to the sheet containing your chart.
2. Update your browser URL to add `/options/developer` to the end.

As an example, you should amend `https://tenant.us.qlikcloud.com/sense/app/b0702f9b-46a3-46ff-8c8e-3a5f83a9b898/sheet/nAtvah/state/analysis`
to `https://tenant.us.qlikcloud.com/sense/app/b0702f9b-46a3-46ff-8c8e-3a5f83a9b898/sheet/nAtvah/state/analysis/options/developer`.

3. Click the **ellipses** for the chart you wish to embed.
4. select the new **Developer** option.

![a screenshot of the details menu with developer option](https://qlik.dev/_astro/chart-dev-1.Cl-DubVi.png)

5. Copy the ID displayed next to **Object ID**.

![a screenshot of the details menu](https://qlik.dev/_astro/chart-dev-2.DIRJxlBy.png)

## Qlik Sense bookmark ID

A bookmark is an object type which carries a snapshot of state and selections stored
by a user in a Qlik Sense app. As an app object, IDs are unique only within the app,
as with sheets.

The format of a bookmark ID is the same as for sheet IDs.

### Find the bookmark ID in the UI

The **Copy Link** dialog for a bookmark includes the bookmark ID in a URL.

1. In a Qlik Sense app, navigate to the **Assets** pane.
2. Select **Bookmarks**.
3. Click the **ellipses** for the bookmark you wish to embed.

![a screenshot of a bookmark in the assets pane](https://qlik.dev/_astro/bookmark-1.D-fCGon0.png)

4. Select **Copy Link** to open the link window.

![a screenshot of the link window](https://qlik.dev/_astro/bookmark-2.aaIM1Bg8.png)

5. Copy the URL in the **Link** section.

![a screenshot of the preview window showing the sheet ID](https://qlik.dev/_astro/bookmark-3.CkLvQezy.png)

The bookmark ID can be extracted from the URL. The URL will look like
`https://tenantname.us.qlikcloud.com/sense/app/b0702f9b-46a3-46ff-8c8e-3a5f83a9b898/sheet/NHnMB/bookmark/QjGmge...`.

The ID is the value immediately following `bookmark/`, in this case `QjGmge`.

## Programmatic access

The Qlik Sense engine APIs provide access to object metadata.

- If you're a qlik-cli user, you can programmatically list all objects in an app with
  the [app object ls](https://qlik.dev/toolkits/qlik-cli/app/app-object-ls) command.
- If you prefer a no-code solution, the Qlik Cloud Services blocks
  in [Qlik Automate](https://qlik.dev/toolkits/no-code) also support listing
  of some object types.
- For web apps, the various [SDKs and toolkits](https://qlik.dev/toolkits) provide this data, in addition
  to the [JSON RPC engine API](https://qlik.dev/apis/json-rpc/qix).

If you are using `qlik-embed`, you can avoid hard-coding resource IDs entirely by
resolving them at runtime using `@qlik/api`. See
[Look up a resource by name and embed it dynamically](https://qlik.dev/embed/qlik-embed/customize/resolve-resource-by-name/)
for a step-by-step tutorial.
