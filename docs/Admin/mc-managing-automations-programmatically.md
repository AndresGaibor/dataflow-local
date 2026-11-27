---
title: "Managing automations programmatically"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-managing-automations-programmatically.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing automations"]
---

# Managing automations programmatically

Use an OAuth bot user with the admin.automations scope to manage automations across your tenant, including automations owned by other users.

This method supports backup, audit, migration, and bulk management without changing automation ownership. The bot can also read and manage automations in personal spaces.

The bot user can perform the following actions on any automation in the tenant, regardless of the owner or space:

- Create, read, update, and delete automations.
- Move an automation to another space.
- Enable and disable automations.
- Change the owner of an automation.
- Read all automation runs. The bot user cannot update or delete automation runs.

Information noteConnections are not in scope. The bot user cannot create, update, or delete automation connections.

When you create an OAuth client with the admin.automations scope and enable Allow Machine-to-Machine (M2M), the system automatically creates a bot user. You can view the bot user on the Manage users page in the Administration activity center.

Information noteOn the Events page in the Administration activity center, actions performed by the bot user appear as actions performed by the automation owner.

For more information, see [*Creating and managing OAuth clients*](mc-create-oauth-client.htm) and [Get started with OAuth machine-to-machine](https://qlik.dev/authenticate/oauth/getting-started-oauth-m2m/) on the Qlik Developer Portal.
