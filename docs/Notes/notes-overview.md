---
title: "Capturing and sharing insights using Notes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Notes/notes-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users"]
---

# Capturing and sharing insights using Notes

Create notes with [snapshots](#glossary-0 "Glossary term") of data to capture a personal narrative, and to collaborate with others.

Create a private note in your [personal space](#glossary-1 "Glossary term") for your own use. Create a note in a [shared](#glossary-2 "Glossary term") or [managed space](#glossary-3 "Glossary term") to collaborate with your team.

In analysis mode within sheet view, select Notes from the assets panel. Select the space where you want to create the note, and then select ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) Create new note.

Select space in sheet view

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_select-space-rev.png "Click to view full size")

Create new note in sheet view

![Creating a new note from within a shared space app.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_notes_create_app_view_rev.png "Click to view full size")

You can also go to the Create page in the Analytics [activity center](#glossary-4 "Glossary term") and select Note to create a new note.

Creating a new note from the Create page in the Analytics activity center

![Create new note from the 'Create' page.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_create-note.png "Click to view full size")

You can also create a new note from a snapshot. In sheet view, right-click a chart and select ![Note](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_note.svg) Notes, then click ![Camera](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_camera2.svg) Create note with snapshot. The snapshot is automatically added to the new note.

For more information, see [*Working with notes*](notes-using.htm).

## Permissions

Whether you can work with Notes is determined by the permissions granted to you by administrators, as well as by collaborators in shared and managed spaces.

For full details, see [*Notes permissions*](notes-permissions.htm).

## Data security

Note authors can add a snapshot to a note from any data that they can access. This includes sensitive data that could be restricted to other users based on section access rules. If the note is in a shared or managed space, all other space members with access to the note can see the snapshots that are in the note. Note authors should use caution when sharing data that other users may not be authorized to see.

Warning noteA user may have access to visibility of all other users within the same tenant - such visibility may include (but may not be limited to): user names, email addresses and the user’s subject, which is a unique string used to identify the user that is provided to Qlik Cloud by the configured Identity Provider.

## Notifications

You can set your note notification preferences globally (for the tenant), at the space level, and individually (for each note). Space-level notification settings override global tenant settings, and individual notification settings override global and space-level settings.

For global note [notifications](#glossary-5 "Glossary term"), you can manage the following notification preferences from your personal settings. To access these settings, click your user profile icon and then click Settings.

- When you are added as a collaborator on a note
- When you are mentioned in a note

At the space level, you can manage your note notifications by clicking Space settings > Notifications in the space view within the catalog. You can modify the following settings:

- When you are added as a collaborator on a note
- When a note is created in the space
- When you are mentioned in a note

You can also change the notification settings for an individual note. For a note, you can change whether you receive notifications when you are mentioned in a note.

For more information about your personal settings, see [*Managing your personal settings*](../Introduction/profile-settings.htm).

## Limitations

### General limitations

- Notes does not support the following:

  - Data spaces
  - Qlik Analytics mobile app
  - QlikView applications (documents) in Qlik Sense
  - Dynamic charts
- A maximum of 25 users can open the same note at the same time.
- Note creation in browsers on small screens, such as on mobile and tablet devices, is not supported. Notes are read-only.
- Right-to-left setting is not supported.
- Selections from dynamic [bookmarks](#glossary-6 "Glossary term") are not supported in note snapshots. The [selections](#glossary-7 "Glossary term") will be the selections that were applied in the visualization when the snapshot was added to the note.
- Previous or next selections from [set analysis](#glossary-8 "Glossary term") expressions are not supported in note snapshots.
- Variable values in note snapshots are set and are not updated in snapshots if they change in the source application.
- Shadows applied to chart objects in the application are not shown in the chart snapshots you can add to a note.

### Visualization support

Notes does not support the following [visualizations](#glossary-9 "Glossary term"):

- Button
- Date picker
- Filter pane
- Multi-KPI extension
- Navigation menu
- Slider
- Trellis container extension
- Variable input control
- Word cloud chart extension
- Video player

### Limitations for note sharing

The following limitations apply to a note owner sharing their notes in shared and managed spaces with other users. If you exceed any of these limitations, users can delete notes or make shared notes private again, freeing up capacity for further note sharing.

- A maximum of 2000 notes can be shared with each user in the Qlik Cloud [tenant](#glossary-10 "Glossary term").
- When a note is shared with other users, the access of each individual user (other than the note owner) to this note is counted as a note share. Within each shared or managed space, a maximum of 30,000 note shares can exist at once.

### Technical limitations for adding snapshots to notes

There are technical limitations that apply when adding snapshots to notes. These limits are checked when you click Add snapshot to note. If these limits are exceeded, you will see an error message. If this issue occurs, contact a user with Can edit permission in the application.

The specific limitations are listed below:

- Maximum number of fields in the selections: 125
- Maximum number of field values in the selections: 150,000 total field values across one or many fields
- Maximum number of alternate states: 125

  [*Using alternate states for comparative analysis*](../Visualizations/alternate-states-comparative-analysis.htm)
- Maximum number of patches: 100

  Patches are properties or styling applied in the application. For example: Adding a sort to a table column.
- Maximum number of variables: 1,100

  [*Using variables in expressions*](../Variables/work-with-variables.htm)
- Maximum image size: 4,000 x 4,000 pixels
- Minimum image size: 5 x 5 pixels for charts and 20 x 20 pixels for sheets

Related learning:

- [How do I collaborate with notes in Qlik Cloud?](/lnk/How_collaborate_notes_qlikcloud)
