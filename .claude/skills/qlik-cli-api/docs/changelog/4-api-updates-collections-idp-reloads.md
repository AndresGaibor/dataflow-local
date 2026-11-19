---
source: https://qlik.dev/changelog/4-api-updates-collections-idp-reloads/
last_updated: 2025-07-08T16:09:30Z
---

# SaaS API updates to Collections, Identity Providers, Reloads and more

## Collections API adds new response information with app size metrics

Endpoints for the Collections API now include two new properties in the response
object. `appFile` displays the size of an app on disk and `appMemory` shows the
size of an app when it is loaded in memory. Both values are displayed in bytes
and appear under the `resourceSize` property.

```json
"appFile": {
    "description": "Size of the app on disk in bytes",
    "type": "number"
},
"appMemory": {
    "description": "Size of the app in memory in bytes",
    "type": "number"
}
```

Learn more about the Collections
API [here](https://qlik.dev/apis/rest/collections).

## Identity Providers V1 API released public/stable

The Identity Providers REST API is a Management API for
creating and
updating identity provider configurations in a tenant. For
more information regarding the API, please review the API
reference [here](https://qlik.dev/apis/rest/identity-providers).

## Licenses API releases two public/stable, three public/experimental endpoints

The Licenses REST API is a Management API for assigning, changing, and
removing license assignments from users in tenants.

This release includes two public/stable endpoints:

- get license status
- get license overview

and three public/experimental endpoints:

- assign access to users
- delete user license assignments
- update user license assignments

Learn more about the
API [here](https://qlik.dev/apis/rest/licenses).

## Reloads API re-released public/stable

The Reloads API is now verified public/stable in Qlik's API governance system.
The Reloads API was mistakenly set to public/stable in late 2020 after a
breaking change was introduced in the code. Subsequently, the Reloads API was
adjusted to public/experimental before the new year to indicate the correct
status. The outstanding issues with the API have been addressed.

## Temporary Contents API released public/stable

The Temporary Contents Service API is now public/stable in compliance with
Qlik's API governance policy. The `TCS` is used by other services to
provided
temporary file storage for uploads to the system (for example through Qlik Data
Transfer) and downloads from (for example image and sheet exports from
Qlik Sense
Client).

Learn more about the API [here](https://qlik.dev/apis/rest/temp-contents).
