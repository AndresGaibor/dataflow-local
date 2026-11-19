---
source: https://qlik.dev/changelog/241-admin-automations-scope-update/
last_updated: 2026-07-24T08:27:55-02:30
---

# Programmatically manage automations owned by other users using OAuth M2M

OAuth access tokens issued to bot users with the `admin.automations` scope can now be used to manage automations owned
by other users.

This update expands the resource coverage of [the administrative access model previously introduced](https://qlik.dev/changelog/86-m2m-access-personal-metadata/)
for the `admin.apps` scope to include automations.

It applies to both the [Automations API](https://qlik.dev/apis/rest/automations/) and the [`workflows/automations` namespaced API](https://qlik.dev/apis/rest/workflows/automations/).

An OAuth machine-to-machine client with the `admin.automations` scope can perform create, retrieve, update, and delete
operations on automations, including automations owned by other users. The bot user must have the required permissions
in the relevant space.

This update supports administrative and programmatic use cases such as:

- Backing up and auditing automations that the bot user has permission to access.
- Migrating automations between tenants.
- Managing automations when the original owner is no longer available.
- Changing automation ownership programmatically.
- Managing automations without temporarily transferring ownership to the bot user.

Connections are not included in this permission update.

To learn more, see [Deploy an automation to a tenant](https://qlik.dev/manage/platform-operations/deploy-automation-to-a-tenant/).
