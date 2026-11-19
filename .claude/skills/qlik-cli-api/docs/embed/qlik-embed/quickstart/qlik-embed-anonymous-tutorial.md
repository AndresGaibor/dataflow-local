---
source: https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-anonymous-tutorial/
last_updated: 2026-03-03T13:42:07Z
---

# Anonymous Access with qlik-embed

## Introduction

In this tutorial, you will learn how to use the Anonymous Access capability in Qlik
Cloud with `qlik-embed` to display Qlik Cloud Analytics on a public website without
requiring users to authenticate to a Qlik Cloud tenant.

> **Limitations:**
>
> - Qlik Anonymous Access is available in the Europe (Stockholm) region (`se`) . It is not available in other regions, or in
>   Qlik Cloud Government.
> - [Visualization extensions](https://qlik.dev/embed/foundational-knowledge/visualizations/) are not supported when accessed via an
>   anonymous access link for an app, due to security and API restrictions for anonymous sessions.

## Requirements

- A Qlik Cloud tenant in the Europe (Stockholm) region (`se`)  entitled with Anonymous Access.
- The tenant administrator role assigned to your user.
- A valid Client ID from a configured
  [anonymous embed OAuth2 client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-anonymous/).
- The Qlik Cloud Analytics app you intend to share and embed.
- The object identifiers necessary to embed content from your Qlik Cloud Analytics app
  into your website.

Code samples are shown with `qlik-embed-web-components`. It is also
possible to use `qlik-embed-react` or `qlik-embed-svelte` to embed analytics
from a Qlik Cloud tenant enabled with the Anonymous Access capability.

This tutorial is presented in three sections:

1. Prepare your tenant in the Administration activity center
2. Share the Analytics app
3. Embed the app into your website with `qlik-embed`

## 1: Prepare your tenant in the Administration activity center

In addition to creating the
[Anonymous embed OAuth2 client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-anonymous/),
you need to perform the following tasks in the Administration activity center of your tenant:

1. Grant a user permissions to create public links so that you can obtain an
   embed access code.
2. Create a managed space to publish the analytics app you want to
   embed into your website.

### Create a custom role

Create a custom role with the necessary permissions and assign it to the users
or groups on the tenant who need to create public links.

1. Access the administration activity center and select **Users**.

![The users menu item](https://qlik.dev/_astro/usersmenu.D7id3Ap6.png)

2. Click the **Permissions** tab.

![The permissions tab in the users management interface](https://qlik.dev/_astro/permissionstab.BT8J44b4.png)

3. Click **Create new** to open the **Create new role** dialog.

4. Give the new role a name and optional description.

5. Select the **All** filter and expand **Features and actions**.

6. In the **Public link creation** list, select **Allowed**. This
   change will grant a user or group assigned to this role the ability to turn on
   Anonymous Access for a Qlik Cloud Analytics app.

7. Click **Confirm** to create this new custom role.

![Completed custom role configuration before confirmation](https://qlik.dev/_astro/createnewrole.BkfRMl41.png)

### Assign a user to the custom role

1. Click the arrow next to the new custom role.

![The expanded role assignment window](https://qlik.dev/_astro/rolecreated.n-wrgjOr.png)

2. Click **Assign** and search for the user or group on the tenant you want to
   give permission to create public links by name or email and add them to the list.

3. Click **Assign** to add the role to the user or group.

![The user assignment window](https://qlik.dev/_astro/assignuser.C5Uza-6W.png)

Congratulations, at least one person on your tenant is able to create public
links.

Now, create a managed space to hold the apps you will share and embed into your website.

> **Note:** If you have a managed space on your tenant that you plan to use for holding apps with Anonymous Access turned on, see
> [Share the Analytics app](#2-share-the-analytics-app).

### Create a managed space

You can now create a [managed space](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-managed-spaces.htm)
to hold the apps you will share and embed into your website.

1. Access the administration activity center and select **Spaces**.

![The Spaces menu item](https://qlik.dev/_astro/spacesmenu.B2H5Ave1.png)

2. Click **Create new**. The Spaces dialog opens.

3. In the **Type** list, select **Managed**.

4. Enter a name and an optional description for the space.

5. Click **Create** to create the space.

![The space creation window](https://qlik.dev/_astro/createmanagedspace.CtLlckGd.png)

You have granted a user permission to create public links and you have
created a managed space to hold your analytics app. Now, it's time to
share the app so you can embed it into your website.

## 2: Share the Analytics app

From the Analytics activity center, you will publish your app
to the [managed space you just created](#create-a-managed-space)
and create the sharing code needed to embed the app into your website.

> **Note:** If you have already published the app you intend to share to the managed space, see [Share the app for Anonymous Access](#share-the-app-for-anonymous-access).

### Publish the app to a managed space

1. In the Analytics activity center, find the analytics app you want to share.

![An app card in the analytics activity center](https://qlik.dev/_astro/exampleapp.BGw4krtP.png)

2. Right-click the app and select **Publish**.

![The Publish menu item in the app context menu](https://qlik.dev/_astro/publishmenuitem.Bge-rK7r.png)

3. In the window that appears, select **Publish new**.

4. In the **Spaces** list, select the managed space you want to publish the app to. You can
   also update the name of the published version and the description of the app, or add tags.

5. Click **Publish**.

![The publish app window](https://qlik.dev/_astro/publishapp.DiVqt24r.png)

At this point you may wish to retrieve the [ID of the app](https://qlik.dev/embed/foundational-knowledge/find-ids#qlik-sense-app-id),
and the [ID of the visualization](https://qlik.dev/embed/foundational-knowledge/find-ids#qlik-sense-chart-id)
that you wish to embed.

### Share the app for Anonymous Access

You now need to enable the app for Anonymous Access.

1. In the catalog, right-click the published app, then select **Share**. If you're still in the app details view, click
   the **ellipses**, then select **Share**.

![The Share menu item from the context menu for the app](https://qlik.dev/_astro/shareapp.CbGvMBEH.png)

2. In the window that appears, toggle on **Anyone with the link**. When the toggle is on, a cog appears.

![The sharing dialog window for the application](https://qlik.dev/_astro/turnonlink.DzMMRoms.png)

3. Click the cog to open the **Anonymous link settings** window.

4. Copy the embed code to your clipboard.

![An example of embed code](https://qlik.dev/_astro/copylink.l0_0HZkk.png)

> **Note:** The embed code is bound to the hostname used to access the tenant at the time of generation (when sharing the app
> with **Anyone with the link** is toggled on.)
> Make sure to record the hostname in the address bar of your browser. You will need it to configure `qlik-embed`.

With the embed code in hand, it's time to use `qlik-embed` to add the analytics
app to your website.

## 3: Embed the app into your website with qlik-embed

Now that you've configured the tenant, user, and app for Anonymous Access,
you can update your web application to display the app.

### Configure the qlik-embed script element

1. Copy the example script element and paste it into the `<HEAD>` section of the
   website you will embed your analytics.

`embed:./snippets/qlik-embed/anonymous-config-example.html`

2. Update the following properties in your `script` element:

- `data-host`: Set the value to the URI of your tenant as it appeared when you
  shared the app.
- `data-client-id`: Set the value to the Anonymous embed OAuth2 Client ID.
- `data-access-code`: Set the value to the embed code generated when you shared the app for Anonymous Access.

### Add a qlik-embed web component

1. In the `body` of your website, add a `qlik-embed` web component containing the
   properties for the UI type you wish to embed. In the following example, an `analytics/chart` UI is
   configured.

2. Replace `<APP_ID>` with the app ID of your published app and
   `<OBJECT_ID>` with the ID of the visualization in the app that you want to display.

```html
<qlik-embed
  id="visualization"
  ui="analytics/chart"
  app-id="<APP_ID>"
  object-id="<OBJECT_ID>"
></qlik-embed>
```

3. Run your website and witness the magic of Anonymous Access on Qlik Cloud with
   `qlik-embed`.

## Next steps

You can discover more UIs and corresponding parameters on the
[UI and parameters](https://qlik.dev/embed/qlik-embed/parameters) page.
