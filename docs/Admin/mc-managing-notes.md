---
title: "Enabling note creation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-managing-notes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Enabling note creation

In the Administration activity center, [tenant admins](#glossary-0 "Glossary term") can control user access to the [Notes](#glossary-1 "Glossary term") capability by configuring default permissions and custom roles.

Information note

The global switch to enable and disable Notes in the Administration activity center has been deprecated. To replace this feature control setting, configure default permissions and custom roles to control your tenant's Notes access. This help topic guides you through this process.

For information on how to create notes, see [*Capturing and sharing insights using Notes*](../Notes/notes-overview.htm).

The tenant admin can see all the notes in the tenant from **Catalog** by selecting Notes from the Types filter. However, to view the contents of a note, the tenant admin needs:

- The proper role in the space where the note is located.
- Either of the following:

  - Access via the note content being accessible to all space members.
  - Explicit view or edit access via a note share.

## Managing user access to Notes

The Manage notes permission is used to control user access to the Notes capability. This permission is controlled at the [tenant](#glossary-2 "Glossary term") level by [tenant administrators](#glossary-3 "Glossary term").

For the Manage notes permission, the following options are available:

- Allowed: Users can create, view, update, delete, and share [notes](#glossary-4 "Glossary term") in activity centers and applications.
- Not allowed: Users cannot create, view, update, delete, or share notes in activity centers and applications.

The Manage notes permission is assigned in the Administration activity center using the following two processes:

- [*Process 1: Change default permissions*](#UserDefault)
- [*Process 2: Create custom role*](#CustomRole)

### Process 1: Change default permissions

Tenant administrators can adjust default permissions. By default, the default permissions allow all tenant users to work with Notes. This can be changed if you want to restrict access to only some— or no—users.

Do the following:

1. In the Administration activity center, go to Manage users.
2. Switch to the Permissions tab.
3. Click Manage default permissions.
4. Under Permissions, expand Content types.
5. Expand Notes.
6. For Manage notes, change the permission value using the drop down menu.
7. Click Confirm.

### Process 2: Create custom role

Tenant administrators can create custom roles to grant additional permissions to selected users. You can limit Notes permissions by changing the default permissions, then create a custom role to grant Notes permissions to a specific set of users.

Do the following:

1. In the Administration activity center, go to Manage users.
2. Switch to the Permissions tab and click Create new to create a new custom role.
3. Enter a Name, and optionally, a Description for the new role.
4. Under Permissions, expand Content types.
5. Expand Notes.
6. If needed, change the Manage notes permission value using the drop down menu.
7. Click Confirm.
8. Switch back to the All users tab.
9. Select the checkboxes for the users whose permissions you want to modify.
10. Click Manage roles.
11. Assign the new custom role to specific users, and click Save.

## Data security

Note authors can add a snapshot to a note from any data that they can access. This includes sensitive data that could be restricted to other users based on section access rules. If the note is in a shared or managed space, all other space members with access to the note can see the snapshots that are in the note. Note authors should use caution when sharing data that other users may not be authorized to see.

Warning noteA user may have access to visibility of all other users within the same tenant - such visibility may include (but may not be limited to): user names, email addresses and the user’s subject, which is a unique string used to identify the user that is provided to Qlik Cloud by the configured Identity Provider.

## Learn more

- [*Notes permissions*](../Notes/notes-permissions.htm)
- [*Working with notes*](../Notes/notes-using.htm)
- [*Default permissions and custom roles*](permissions-scopes.htm)
