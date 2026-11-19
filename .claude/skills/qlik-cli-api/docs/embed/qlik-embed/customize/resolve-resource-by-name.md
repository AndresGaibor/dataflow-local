---
source: https://qlik.dev/embed/qlik-embed/customize/resolve-resource-by-name/
last_updated: 2026-06-09T09:30:16+01:00
---

# Look up a resource by name and embed it dynamically

Qlik Cloud resources such as apps and Qlik Answers assistants are identified by a
unique UUID. Embedding them with `qlik-embed` requires you to supply this ID
directly, which can be brittle: the ID changes if a resource is recreated, and it
differs across tenants or deployment stages that contain the same resource under
different IDs.

This tutorial shows how to use `@qlik/api` alongside `qlik-embed` on the same
page to resolve a resource by its display name at runtime. You pass the resolved
ID into the `qlik-embed` web component programmatically, so nothing needs to be
hard-coded or maintained out-of-band.

Because `@qlik/api` and `qlik-embed` share the same authenticated session, the
name lookup adds no extra round-trip cost and requires no additional OAuth
configuration beyond what `qlik-embed` already sets up.

> **Note:** This tutorial shows a single `<qlik-embed>` element. To embed multiple named
> resources on the same page, add one `<qlik-embed>` element per resource, give
> each a unique `id`, and call `embedResource` once for each element.

## Prerequisites

- An app or Qlik Answers assistant published to a named space on your Qlik Cloud
  tenant.
- A [SPA OAuth2 client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-spa/)
  configured, with its redirect URI pointing to your page or a dedicated
  [callback page](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/#using-a-callback-handler-with-data-redirect-uri).

## Variable substitution

Variables in the sample code appear as `VARIABLE_NAME`. Replace each one with your
own value.

| Variable               | Description                                                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `QLIK_TENANT_URL`      | Hostname of your Qlik Cloud tenant, for example `tenant.eu.qlikcloud.com`.                                                                              |
| `QLIK_OAUTH_CLIENT_ID` | Client ID of your SPA OAuth2 client.                                                                                                                    |
| `QLIK_REDIRECT_URI`    | Redirect URI configured on your OAuth2 client.                                                                                                          |
| `SPACE_NAME`           | Display name of the space containing the resource, or `"personal"` to search the current user's personal space. If omitted, no space filter is applied. |
| `RESOURCE_NAME`        | Display name of the app or assistant you want to embed.                                                                                                 |

## Step 1: Configure the page

Use an import map to load `@qlik/embed-web-components` and `@qlik/api` from the
CDN. A module script imports both libraries and sets the default host configuration.
Setting a default means both `qlik-embed` and `@qlik/api` REST calls use the same
authentication without any further configuration.

Leave `app-id` off the `<qlik-embed>` element for now; you will set it once the
resource name has been resolved.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Dynamic embed</title>

    <script type="importmap">
      {
        "imports": {
          "@qlik/embed-web-components": "https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js",
          "@qlik/api": "https://cdn.jsdelivr.net/npm/@qlik/api@2/index.js"
        }
      }
    </script>

    <script type="module">
      import "@qlik/embed-web-components";
      import { auth } from "@qlik/api";

      auth.setDefaultHostConfig({
        host: "https://QLIK_TENANT_URL",
        authType: "Oauth2",
        clientId: "QLIK_OAUTH_CLIENT_ID",
        redirectUri: "QLIK_REDIRECT_URI",
        accessTokenStorage: "session",
      });
    </script>
  </head>
  <body>
    <!-- app-id is set dynamically after name resolution -->
    <qlik-embed id="embed" ui="classic/app"></qlik-embed>
  </body>
</html>
```

## Step 2: Resolve a resource by name

Add a module script to the page that imports `items` and `spaces` from `@qlik/api`
and defines a function to look up a resource ID by name.

Qualifying the search by space is recommended to reduce the chance of a name
collision between resources in different parts of the tenant. The `spaceName`
argument is optional: if omitted, no space filter is applied to the query.

Pass `"personal"` to search the current user's personal space. The items API
accepts this as a literal `spaceId` value, so no space lookup is needed.

The `resourceType` argument filters results to a specific kind of resource. This
tutorial uses `"app"` for Qlik Sense apps and `"assistant"` for Qlik Answers
assistants.

```html
<script type="module">
  import { items, spaces } from "@qlik/api";

  /**
   * Returns the resource ID (UUID) of the first item matching the given name,
   * or undefined if no match is found.
   *
   * @param {string} resourceType - Resource type to filter by. Use "app" for
   *   Qlik Sense apps or "assistant" for Qlik Answers assistants.
   *
   * Takes the first match from the API response. If the scope contains more than
   * one resource with the same name, the result is the first one returned and may
   * not be the one you expect. Use precise, unique names to avoid this.
   */
  async function resolveResourceByName(spaceName, resourceName, resourceType) {
    let spaceId;

    if (spaceName === "personal") {
      // The items API accepts "personal" as a literal spaceId — no lookup needed.
      spaceId = "personal";
    } else if (spaceName) {
      // Named space: resolve to an ID, since the items API filters by ID not name.
      const { data: spacesData } = await spaces.getSpaces({ name: spaceName });
      const space = spacesData.data?.[0];

      if (!space) {
        console.warn(`Space "${spaceName}" not found.`);
        return undefined;
      }

      spaceId = space.id;
    }

    const { data: itemsData } = await items.getItems({
      name: resourceName,
      resourceType,
      ...(spaceId && { spaceId }),
    });

    const match = itemsData?.data?.[0];

    if (!match) {
      const scope = spaceName ? `in space "${spaceName}"` : "in the tenant";
      console.warn(`No ${resourceType} named "${resourceName}" found ${scope}.`);
      return undefined;
    }

    // resourceId is the app or assistant UUID used by qlik-embed.
    return match.resourceId;
  }
</script>
```

> **Note:** The items API may return more than one result when names are not unique within
> the search scope. This function picks the first result returned. Where possible,
> enforce unique display names in the spaces your application uses, or qualify the
> search further using additional criteria such as `createdAt`.

## Step 3: Set the ID on the embed component

Once you have the resolved ID, set it as an attribute on the `<qlik-embed>`
element. The component reacts to attribute changes and renders the resource.

For apps, set the `app-id` attribute. For Qlik Answers assistants, set
`assistant-id` instead and use `ui="ai/assistant"`.

```javascript
  async function embedResource(spaceName, resourceName, resourceType) {
    const resourceId = await resolveResourceByName(spaceName, resourceName, resourceType);
    const embedElement = document.getElementById("embed");

    if (!resourceId) {
      embedElement.textContent = `Could not find ${resourceType} "${resourceName}" in space "${spaceName}".`;
      return;
    }

    if (resourceType === "app") {
      embedElement.setAttribute("app-id", resourceId);
    } else {
      // Assistants use assistant-id and ui="ai/assistant".
      embedElement.setAttribute("assistant-id", resourceId);
    }
  }

  // Resolve by name and embed. Replace the placeholder values.
  await embedResource("SPACE_NAME", "RESOURCE_NAME", "app");
```

When the `app-id` attribute is set, `qlik-embed` opens the app and renders it
inside the element. No page reload is required.

## Full code example

<details>
<summary>

### index.html

</summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Dynamic embed</title>

    <script type="importmap">
      {
        "imports": {
          "@qlik/embed-web-components": "https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js",
          "@qlik/api": "https://cdn.jsdelivr.net/npm/@qlik/api@2/index.js"
        }
      }
    </script>

    <script type="module">
      import "@qlik/embed-web-components";
      import { auth } from "@qlik/api";

      auth.setDefaultHostConfig({
        host: "https://QLIK_TENANT_URL",
        authType: "Oauth2",
        clientId: "QLIK_OAUTH_CLIENT_ID",
        redirectUri: "QLIK_REDIRECT_URI",
        accessTokenStorage: "session",
      });
    </script>
  </head>
  <body>
    <qlik-embed id="embed" ui="classic/app"></qlik-embed>

    <script type="module">
      import { items, spaces } from "@qlik/api";

      async function resolveResourceByName(spaceName, resourceName, resourceType) {
        let spaceId;

        if (spaceName === "personal") {
          spaceId = "personal";
        } else if (spaceName) {
          const { data: spacesData } = await spaces.getSpaces({ name: spaceName });
          const space = spacesData.data?.[0];

          if (!space) {
            console.warn(`Space "${spaceName}" not found.`);
            return undefined;
          }

          spaceId = space.id;
        }

        // Takes the first match — use a precise name to minimise ambiguity.
        const { data: itemsData } = await items.getItems({
          name: resourceName,
          resourceType,
          ...(spaceId && { spaceId }),
        });

        const match = itemsData?.data?.[0];

        if (!match) {
          const scope = spaceName ? `in space "${spaceName}"` : "in the tenant";
          console.warn(`No ${resourceType} named "${resourceName}" found ${scope}.`);
          return undefined;
        }

        return match.resourceId;
      }

      async function embedResource(spaceName, resourceName, resourceType) {
        const resourceId = await resolveResourceByName(spaceName, resourceName, resourceType);
        const embedElement = document.getElementById("embed");

        if (!resourceId) {
          embedElement.textContent = `Could not find ${resourceType} "${resourceName}" in space "${spaceName}".`;
          return;
        }

        if (resourceType === "app") {
          embedElement.setAttribute("app-id", resourceId);
        } else {
          embedElement.setAttribute("assistant-id", resourceId);
        }
      }

      await embedResource("SPACE_NAME", "RESOURCE_NAME", "app");
    </script>
  </body>
</html>
```

</details>

## Next steps

- See the [qlik-embed parameters guide](https://qlik.dev/embed/qlik-embed/parameters/) for the full
  list of attributes each UI accepts, including `sheet-id` and `object-id` for
  more targeted embeds.
- To interact with the app after it loads without hard-coding IDs, see
  [Interacting with Qlik Sense apps via qlik-embed and refApi](https://qlik.dev/embed/qlik-embed/customize/interact-with-ref-api/).
- For multi-tenant deployments where the same resource name maps to different IDs
  across tenants, see
  [Using qlik-embed with multiple tenants](https://qlik.dev/embed/qlik-embed/authenticate/multi-environments/).
