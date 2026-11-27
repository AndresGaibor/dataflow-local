---
title: "Notes examples"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Notes/notes-examples.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Capturing and sharing insights using Notes"]
---

# Notes examples

Follow these examples to create and share [notes](#glossary-0 "Glossary term").

## Example: Create a note in a personal space

Only you can view notes that you create in your [personal space](#glossary-1 "Glossary term").

Do the following:

1. In an application, open a [sheet](#glossary-3 "Glossary term") in analysis mode. Expand the Assets panel.
2. Click Notes.

   Select Notes

   ![App in shared space.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_tab_select-rev.png "Click to view full size")
3. Select Personal in the drop-down menu, and then select ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) Create new note. The note will be created in your personal space.

   Create new note

   ![Create new note.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_create_new-rev.png "Click to view full size")
4. Enter a title and text for the note. Select ![Text](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text.svg) to open the formatting toolbar.

   Enter title and text for note

   ![Enter title and text for note.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_text_format.png "Click to view full size")
5. To add a snapshot of a chart to a note, right-click the chart and select ![Note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_note.svg)Notes. Click ![Note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_note.svg)Add snapshot to note.

   Add snapshot to note

   ![Add snapshot to note.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_add_snapshot.png "Click to view full size")

   The snapshot is added to the note.

   Snapshot added to note

   ![Snapshot added to note. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_snapshot_added_note-rev.png "Click to view full size")
6. Select ![Previous](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_left.svg) Back to finish editing and see a list of your notes. You can also see and open all your notes by selecting Catalog in the Qlik Sense navigation bar, and then selecting Notes from the Types filter.

   List of notes

   ![List of notes in personal space after creating new note ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_notes_listed-rev.png "Click to view full size")

## Example: Create a note and collaborate in a shared or managed space

By default, notes that you create in a shared or managed space can only be viewed by you. You can allow other individual space members to view and edit the note. You can also make the note public so that additional space members can see it.

For non-public notes, users with the Owner or Can manage role in the space can see the note exists in the space, but cannot view its contents unless they have been given access to the note. If they have not been given access to a note, users with these space roles can share the note and modify individual user access to the note, but cannot make it public.

To share a note in a shared space with another individual space member, the space member with whom you are sharing the note must have any of the available space roles except Can consume data in the space. When a note in a shared space is made public, all space members, except users with the Can consume data role only, can open and view the note.

To share a note in a managed space with another individual space member, the space member with whom you are sharing the note must have any of the available space roles except Can publish and Can consume data in the space. When a note in a managed space is made public, space members with any of the following roles in the space can open and view the note:

- Has restricted view
- Can view
- Can contribute
- Can manage

If the note owner would like to allow other space members to modify access controls for the note, they can provide edit access to the note for these users (make them coauthors).

You can add snapshots to a note from private or public sheets in a shared or managed space.  All space members with access to the note can see the snapshots in the note. However, since only you can access your private sheets, other members will not be able to go to the sheet by selecting ![ ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_export.svg) Link to source on the snapshot in the note.

The following example creates a note in a shared space. However, the same steps would apply in a managed space.

Do the following:

1. Open a public sheet in an application in a shared space. For more information, see [*Making application content public in shared spaces*](../Share/make-public-or-private.htm#MakeSheetPublic).
2. In analysis mode for the sheet, expand the Assets panel. Click Notes.

   Select Notes

   ![App in shared space.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_tab_expand-rev.png "Click to view full size")
3. Select a shared space in the drop-down menu, and then select Create new note. The note will be created in the shared space.

   Create new note in shared space

   ![Create new note in shared space.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_create_shared-rev.png "Click to view full size")
4. Enter a title for the note, and add text content. To add a snapshot of a chart to a note, right-click the chart and select ![Note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_note.svg) Notes. Click ![Note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_note.svg) Add snapshot to note.

   Note with text and snapshot

   ![Note with text and chart snapshot.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_text_snapshot.png "Click to view full size")
5. Select or type @ to mention the note owner, a coauthor, or a previously mentioned user. Select their name from the list that appears. To mention any other space member, type at least three letters of their name and select their name from the list that appears If the user already has access to the note, they will be notified in the Qlik Sense navigation bar.

   If the mentioned space member does not have access to the note, you are prompted to give them Can view or Can edit access to the note. If you do not provide access to the note for the user, they will not be notified of the mention, and will not be able to view the note.

   Mention tip notification that appears when you mention a user with no access to the note

   ![Popup dialog that appears for mentioned users with no note access, allowing you to give them view or coauthor access.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_mention_tip-rev.png "Click to view full size")

   The note should now contain a mention, text content, and a chart snapshot.

   Space member tagged in note content

   ![Note with mentioned user, containing text and snapshot. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_completed-rev.png "Click to view full size")

## Example: Create a private note and later share its contents with others

Personal spaces are private, therefore notes that you create there cannot be viewed by others. When creating a note, you may want to first create a draft in your personal space before sharing the note with others in a shared or managed space.

You can create a note in a personal space from an application or sheet in a shared or managed space. When you are ready, you can create a new note in a shared or managed space and copy and paste the contents of the private note into the new note.

In the new note, only [snapshots](#glossary-4 "Glossary term") taken from applications in the same shared or managed space as the note will be visible to the other users in the space. Snapshots taken either from applications in your personal space or applications in spaces other than the note’s shared or managed space will not be visible to other users.

The following example creates a note in a shared space. However, the same steps would apply in a managed space.

Do the following:

1. Open an application in a shared space.
2. Open a sheet in the application. For this example, the sheet is public so that others can navigate to the sheet from the note.

   Application in shared space

   ![App in shared space.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_app_overview-rev.png "Click to view full size")
3. In analysis mode for the sheet, expand the Assets panel. Click Notes.

   Select Notes

   ![Expanding the Notes tab in sheet view ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_expand-rev.png "Click to view full size")
4. Select your Personal space in the drop down menu, and then select Create new note.

   Create new note

   ![Create new note.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_create_new_personal-rev.png "Click to view full size")
5. Enter a title for the note, and add text content. To add a snapshot of a chart to a note, right-click the chart and select ![Note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_note.svg)Notes. Click ![Note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_note.svg)Add snapshot to note.

   Completed note in personal space

   ![Completed note in personal space.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_private_done-rev.png "Click to view full size")
6. Select all and copy the contents of the note.
7. Select ![Previous](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_left.svg) Back to finish editing and see a list of your notes in your personal space.

   Note in personal space

   ![Completed note in personal space.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_all_personal_space-rev.png "Click to view full size")
8. Select the shared space containing the application from which you took chart snapshots, and then select Create new note. The note will be created in the shared space.

   Switching from Personal to a shared space

   ![Switching from your personal space to a shared space ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_personal_to_shared-rev.png "Click to view full size")
9. Enter a title for the note, and paste the contents of the personal space note.

   Note in shared space

   ![Note in shared space.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_copied_note.png "Click to view full size")
10. Select or type @ to mention the note owner, a coauthor, or a previously mentioned user. Select their name from the list that appears. To mention any other space member, type at least three letters of their name and select their name from the list that appears If the user already has access to the note, they will be notified in the Qlik Sense navigation bar.

    If the mentioned space member does not have access to the note, you are prompted to give them Can view or Can edit access to the note. If you do not provide access to the note for the user, they will not be notified of the mention, and will not be able to view the note.

    Mention tip notification that appears when you mention a user with no access to the note

    ![Popup dialog that appears for mentioned users with no note access, allowing you to give them view or coauthor access.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_mention_tip-rev.png "Click to view full size")

    The note should now contain a mention, text content, and a chart snapshot.

    Space member tagged in note content

    ![Note with mentioned user, containing text and snapshot. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_completed-rev.png "Click to view full size")

Click ![Share](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_group_outline.svg) Share to manage permissions for the note.

By default, all notes created in a shared or managed space can only be accessed by the note creator and individual space members they have shared it with. You can add or modify individual space member access to the note, or make the note public so that all space members can access it. Once you make a note public, it cannot return to this default sharing configuration.

Do the following:

1. With the note open, click ![Share](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_group_outline.svg) Share.
2. Add a user by typing at least three characters of the user's name into the search box under Users. Confirm the selection and choose from Can view or Can edit in the dropdown list that appears.
3. Click Share.

   The user is given access to the note.

   Sharing a note with a space member

   ![Sharing a note with a space member using the 'Users' dialog](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_individual_share.png "Click to view full size")

You also have the option to add, remove, or modify individual space member to the note.

Do the following:

1. With the note open, click ![Share](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_group_outline.svg) Share.
2. Click Manage. The dialog for managing user permissions on the note appears.
3. Remove a user from the note by selecting the dropdown list next to their name and selecting No access.

   Similarly, you can change a member's access between Can view and Can edit, or add space members to the note by typing in the search box.
4. Click Done.

   Use the Manage dialog to add, remove, or modify individual user access to a note

   ![Sharing a note with a space member using the 'Users' dialog](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_add_remove_modify_user.png "Click to view full size")

By default, all notes created in a shared or managed space are not public. You can make the note public so that all space members with sufficient permissions can access it.

Do the following:

1. With the note open, click ![Share](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_group_outline.svg) Share.
2. Click the drop down list next to the text explaining the access of any space member.
3. Select Can view or Can edit.

   Warning note

   Once you have changed this setting to give all users access to the note, it cannot be undone. Once a note has been made public in a shared or managed space, it cannot be reverted to the default sharing configuration (access only for note owner and individual space members they share the note with). All space members with sufficient permissions will have access to the note unless it is deleted from the space.

   Warning message indicating that once a note is made public, it cannot be reverted to the default sharing configuration

   ![Warning message in note sharing dialog cautioning users that the action of changing users' access from private to public is not reversible. The note will never be able to be private again](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_make_public_warning.png "Click to view full size")
4. Click Confirm.

For more information about sharing notes in shared and managed spaces, see [*Working with notes*](notes-using.htm).

## Example: Create and view a note that is linked to a chart

When a note contains a snapshot of a chart, the note is linked with the original chart. This means that you can view notes that use a snapshot of a specific chart, or notes that are used in the current sheet or application.

The following example shows how you can link a chart to a note using snapshots, as well as search for other notes which may also use that chart. The example discusses applications in shared spaces, but the process will work in managed spaces as well.

Do the following:

1. Open a public sheet in an application located in a shared space.
2. In analysis mode for the sheet, expand the Assets panel. Click Notes.
3. Ensure the correct space is selected. If your Personal space is selected, any notes you see or create will be private. If the selected space is a shared or managed space, the note can be shared with other space members.
4. Right-click a chart and select ![Note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_note.svg) Notes, then click ![Camera](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_camera2.svg) Create note with snapshot.

   Create note with snapshot using a chart in the sheet

   ![Creating a note with snapshot using a chart in the sheet.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_create_w_snapshot.png "Click to view full size")
5. Edit the title of the note and add any relevant details about the snapshot to the note.

   Adding a title and text content to a note

   ![Adding a title and text content to a note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_examples_add_content.png "Click to view full size")
6. Select ![Previous](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_left.svg) Back to finish editing and see a list of your notes.
7. Next, follow a similar process to explore a list of all notes using that same chart. Right-click the chart again and select ![Note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_note.svg) Notes, and then click ![Note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_note.svg) Find notes related to this chart.

   Find notes using a selected chart

   ![Right-clicking chart and finding notes using the chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_find_related_note_example.png "Click to view full size")
8. View your new note, as well as any others created using this chart. You can switch between Your notes and notes which are Owned by others.

For more information, see [*View notes linked to charts, sheets, and applications*](notes-using.htm#View2).
