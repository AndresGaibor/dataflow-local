---
title: "Collecting insights for stories using snapshots"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/StoryTelling/Story/collect-insights-for-story.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Sharing insights with data storytelling"]
---

# Collecting insights for stories using snapshots

To get your application's full picture, you need a way to collect the insights you encounter. To do this, you take static snapshots of your visualizations.

A snapshot is a graphical representation of the state (type and data) of a data object at a certain point in time that you can use when you build stories. The snapshot you take is a copy of the state. This means that the state of the snapshot does not change when the state of the corresponding data object gets updated.

When you take a snapshot you can make an annotation for your snapshot. The annotation helps you distinguish between the different snapshots in the snapshot library when you build your story. The annotation is not visible when you play the story.

After taking snapshots of a specific [visualization](#glossary-1 "Glossary term"), you can open the Snapshot library from the visualization's shortcut menu. From there you can decide which snapshots to keep and use in your stories. You can also edit the annotation and delete the snapshots.

Tip noteWhen the snapshot library is opened from storytelling view, all the snapshots from all the visualizations in the application are displayed.

If the visualization you want to take a snapshot of is an extension, make sure to enable the snapshot functionality in its main script. To do that, set the snapshot property to true.

For more information, see [Allow snapshots of your visualization](/en-US/sense-developer/November2026/Subsystems/Extensions/Content/Sense_Extensions/Howtos/working-with-data-storytelling.htm).

## Taking a snapshot

When you are in sheet view, you can take snapshots of the visualizations and use them to build a story in data storytelling.

You can take snapshots of all the different visualization types but not the filter panes.

Do the following:

1. In sheet view, go to the visualization.
2. Right-click on the visualization or click the hover menu ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
3. Click ![Story Mode](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_slide_show.svg) Storytelling snapshots > ![Snapshot](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_camera2.svg) Take Snapshot .
4. The snapshot is taken and saved to the snapshot library. It will have the same title as the visualization.

## Viewing snapshots

When you are working on a story you can view all your snapshots from the snapshot library.

Do the following:

1. In storytelling view, click ![Snapshot ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_photo_library_outline.svg) in the story tools panel.

   The snapshot library is opened with your snapshots sorted by date with the most recent snapshot on top.
2. Click ![Snapshot ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_photo_library_outline.svg) to close the snapshot library.

## Editing annotations

When taking a snapshot you can choose to add an annotation. From the snapshot library, you can change the annotations or add annotations to snapshots without annotations.

Do the following:

1. In storytelling view, click ![Snapshot ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_photo_library_outline.svg) in the story tools panel.

   The snapshot library is opened with a list of all your snapshots.

   Tip noteIn sheet view, right-click the visualization you want to view snapshots for, click ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Snapshot library in the shortcut menu.
2. Click ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
3. Click the annotation text area, to the right of the snapshot name.

   Information noteYou cannot edit annotations for snapshots that belong to a published version of an application.
4. Edit the annotation.
5. Click ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) or outside the text area.

   The annotation is saved.
6. Click outside the library to close it.

## Deleting snapshots

You can delete a snapshot from the snapshot library, which contains all snapshots you have taken in the application.

Do the following:

1. In storytelling view, click ![Snapshot ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_photo_library_outline.svg) in the story tools panel.

   The snapshot library is opened with a list of all your snapshots.

   Tip noteIn sheet view, right-click the visualization you want to view snapshots for, click ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Snapshot library in the shortcut menu.
2. Click ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).

   Editing is enabled.
3. Select the snapshots you want to delete.

   Information noteYou cannot delete snapshots that belong to a published version of an application.
4. Click ![Delete](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg).

   The selected snapshots are deleted.
5. Click ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) to stop editing.
6. Click outside the library to close it.

Related learning:

- [Take Snapshots of Visualizations](/lnk/Take_snapshots_visualizations_QS)
