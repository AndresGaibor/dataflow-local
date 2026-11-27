---
title: "Sharing insights with data storytelling"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/StoryTelling/use-data-storytelling.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data"]
---

# Sharing insights with data storytelling

Data storytelling provides a way to share your data insights, whether they belong to a larger discussion or the main topic.

The purpose of data storytelling is to turn data discoveries into a [story](#glossary-0 "Glossary term"). Emphasizing important elements helps create convincing stories and supports stakeholders in decision-making.

Data storytelling lets you combine reporting, presentation, and exploratory analysis techniques to create and collaborate. You take [snapshots](#glossary-1 "Glossary term") of your discovered data to use in stories composed of slides. Snapshots can be enhanced with effects. This lets you emphasize the data insights you want your audience to focus on.

As you tell the story, you can answer questions by switching to a snapshots source and accessing live data. This guides your story to new directions, triggering new conversations and deeper insights.

Storytelling becomes interactive by inserting live data [sheets](#glossary-2 "Glossary term") in slides, and making [selections](#glossary-3 "Glossary term") while presenting.

For a visual demo about storytelling, see [Sharing insights with data storytelling](https://share.vidyard.com/watch/NgMnNkx9i3AXVtbuVX8pJj?).

Wf-note**Get started by following these steps**

This section of the help features a step-by-step flow, that shows you how to get started with Sharing insights with data storytelling.

[See the steps](/en-US/cloud-services/wf/Subsystems/Hub/Content/Sense_Hub/StoryTelling/use-data-storytelling.htm)

## The story

In data storytelling, you use a story to collect and present insights and ideas to your audience. A story is presented as a timeline of slides. It can be based on traditional data storytelling structures, such as a three-act play or a hero’s journey.

Stories are contained within an application. A story is connected to its application, so you can return to the live data anytime, to discover new and hidden stories.

To build a story you use time-based snapshots of your data [visualizations](#glossary-5 "Glossary term") and live data sheets and place them on the story’s timeline.

You can, for instance add text and shapes, put emphasis on certain insights with visual effects, apply styling, and so on, to make the story compelling and engaging, and its purpose very clear.

Tip noteYou can download the story if you want to present it outside of Qlik Sense.

For more information, see
[*Working with stories*](Story/working-with-stories.htm) and [*Making stories compelling*](Story/make-story-compelling.htm).

## Snapshots

A snapshot is a graphical representation of the state (type and data) of a data object at a certain point in time that you can use when you build stories. The snapshot you take is a copy of the state. This means that the state of the snapshot does not change when the state of the corresponding data object gets updated.

Snapshots capture individual objects on a sheet during the analysis process. They store the visualization and data as you see it at that time enabling you to use them at a later point in time to tell a story. Each snapshot contains a [bookmark](#glossary-6 "Glossary term") back to the original context so that you quickly get access to the live data.

When you take a snapshot you can make an annotation for your snapshot. The annotation helps you distinguish between the different snapshots in the snapshot library when you build your story. The annotation is not visible when you play the story.

Warning noteA snapshot's state and selections will not be updated at a data reload. It will always reflect the data that existed at the point in time the snapshot was taken.

For more information, see [*Collecting insights for stories using snapshots*](Story/collect-insights-for-story.htm).

## Live data sheets

Using live data sheets in stories you can make sheet selections while playing the story. This way, you can show your insights without going to the application itself.

Playing a story, you can make and reset selections in the live data sheets. It works the same way as in any sheet, in sheet view.

Information noteThe reset gives you the possibility to always return to the same selections as when you inserted the live data sheet on the slide.

For more information, see [*Adding a live data sheet to a slide*](Slide/creating-a-slide.htm#Adding) and [*Selecting in a live data sheet*](PresentStory/select-embedded-sheet.htm).

Related learning:

- [Build and play stories](/lnk/Build_Play_Stories_QS)
- [Take Snapshots of Visualizations](/lnk/Take_snapshots_visualizations_QS)
