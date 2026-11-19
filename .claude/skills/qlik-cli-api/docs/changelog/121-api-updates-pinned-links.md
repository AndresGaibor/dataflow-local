---
source: https://qlik.dev/changelog/121-api-updates-pinned-links/
last_updated: 2025-02-03T13:41:21Z
---

# New APIs - Pinned Links

Pinned links are now available in the Qlik Cloud navigation menu. Pinned links
allow you to create and manage your own links which appear under the `More`
section in the navigation menu, providing a way of surfacing important links to
your users via the global navigation controls.

![Screenshot of the Qlik Cloud navigation menu with two pinned links](https://qlik.dev/_astro/pinned-links-nav-menu.DGQpNy54.png)

This feature can only be set via the [Pinned Links API](https://qlik.dev/apis/rest/ui-config/). By
default, your tenant contains no links, and the `More` section will not be shown.
When the first link is added, it will be visible to all users in the tenant.

For example, to create a link to qlik.dev and qlik.com:

```bash
curl -L "https://<TENANT>/api/v1/ui-config/pinned-links/actions/bulk-create-pinned-links" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-type: application/json" ^
-d "{
    \"type\": \"custom-link\",
    \"scope\": \"tenant\",
    \"links\": [
        {
            \"name\": \"Qlik Developer Portal\",
            \"link\": \"https://qlik.dev\"        },
        {
            \"name\": \"Qlik.com\",
            \"link\": \"https://qlik.com\"        }
    ]
}"
```

Successful requests will return an `HTTP 201` status code along with the details of the created
links.

For more information, review the specification for the [Pinned Links API](https://qlik.dev/apis/rest/ui-config/).
