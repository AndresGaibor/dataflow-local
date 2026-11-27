---
title: "Notes permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Notes/notes-permissions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Capturing and sharing insights using Notes"]
---

# Notes permissions

Whether you can work with Notes is determined by the permissions granted to you by administrators, as well as by collaborators in shared and managed spaces.

The following types of permissions can affect your access to Notes:

- [*Permissions assigned by tenant administrators*](#AdminAssigned)
- [*Space permissions and individual note shares*](#SpacesShares)

## Permissions assigned by tenant administrators

Tenant administrators can control which users in the Qlik Cloud tenant can work with the Notes capability. If your tenant administrator has not allowed you to work with Notes, you cannot view, create, edit, or delete any notes, regardless of space or note-level permissions.

For more information about assigning Notes permissions as an administrator, see [*Enabling note creation*](../Admin/mc-managing-notes.htm).

Any user who has been assigned Notes permissions can create notes in their personal space.

## Space permissions and individual note shares

When working in shared and managed spaces, you can share and collaborate on notes with other users in the space.

Information noteThis section is only applicable when you have been given access to the Notes capability by a tenant administrators. See [*Permissions assigned by tenant administrators*](#AdminAssigned).

Notes that you create in a personal space are private and cannot be viewed by others.

By default, notes that you create in a shared or managed space can only be viewed by you. You can allow other individual space members to view and edit the note. You can also make the note public so that additional space members can see it.

For non-public notes, users with the Owner or Can manage role in the space can see the note exists in the space, but cannot view its contents unless they have been given access to the note. If they have not been given access to a note, users with these space roles can share the note and modify individual user access to the note, but cannot make it public.

To share a note in a shared space with another individual space member, the space member with whom you are sharing the note must have any of the available space roles except Can consume data in the space. When a note in a shared space is made public, all space members, except users with the Can consume data role only, can open and view the note.

To share a note in a managed space with another individual space member, the space member with whom you are sharing the note must have any of the available space roles except Can publish and Can consume data in the space. When a note in a managed space is made public, space members with any of the following roles in the space can open and view the note:

- Has restricted view
- Can view
- Can contribute
- Can manage

If the note owner would like to allow other space members to modify access controls for the note, they can provide edit access to the note for these users (make them coauthors).

For more information about note sharing in shared and managed spaces, see [*Working with notes*](notes-using.htm).

### Breakdown by space role

For a breakdown of the required space roles for working with notes, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](../Spaces/permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](../Spaces/permissions-managed-space-admin.htm)

### Snapshots in notes

You can create a note from a snapshot, or add snapshots to a note from private or public sheets in personal, shared or managed spaces. All space members with access to the note can see the snapshots in the note. However, since only you can access your private sheets, other members will not be able to go to the sheet by selecting ![ ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_export.svg) Link to source on the snapshot in the note. For more information, see [*Making application content public in shared spaces*](../Share/make-public-or-private.htm#MakeSheetPublic).

Depending on the managed space to which it is published, a single application can have multiple versions or copies in different spaces. This can impact the set of notes that are available to you. For example, if you publish an application from a personal or shared space to a managed space, then add a note to the application in the managed space (such as a note that includes a snapshot of a [chart](#glossary-1 "Glossary term")), the note will not be visible in the copy of the application that resides in the personal or shared space.

### Access levels for notes

For notes in shared and managed spaces, there are different access levels for space members. Some of these can be set globally or individually. The possible access levels on a note consist of the following, which are ranked from highest to lowest permission level:

- Is owner: This is the note owner, and the user who created the note. It is similar to  Can edit note access, but with some important exceptions. This access level cannot be changed or moved to another space member. This user has full control over whether or not the note is shared with other space members, and over who is given the initial access. When mentioning the note owner in a note, the access level of the user is displayed as Can edit.

  The note owner can delete the note from the space, whereas other users with Can edit access cannot.
- Can edit: Users with this access level are note coauthors. With this level of access, a user can edit the contents of a note, and set sharing configurations for the note (making the note public and managing individual space member access).
- Can view: Users with this access level can see the note exists, and read its contents. They cannot modify the contents of the note, nor can they modify access levels of other space members on the note.
- No access: This is the default permission level that is given to all other space members except the note owner upon creation of the note. Unless they have the Owner or Can manage role in the space, they cannot see that the note exists, and subsequently cannot view its contents. If a user with the No access permission level is mentioned in a note, they will not be notified of the mention.

Information noteNo user — including the note owner, co-author, space owner, space facilitator, or tenant administrator — can update their own access level to a note.

### Deleting notes

The following users can delete a note:

- Note owner
- Space owners and administrators
- Tenant admin

### Tenant administrators

The [tenant admin](#glossary-2 "Glossary term") can see all the notes that have been created by others in the tenant. However, the tenant admin cannot open or view the content of a note unless they are a member of the shared or managed space where the note resides, and have been given access to the note.
