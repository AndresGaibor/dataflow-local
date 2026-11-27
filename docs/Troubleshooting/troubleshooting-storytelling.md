---
title: "Troubleshooting - Using data storytelling"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Troubleshooting/troubleshooting-storytelling.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Sharing insights with data storytelling"]
---

# Troubleshooting - Using data storytelling

This section describes problems that can occur when using data storytelling in Qlik Sense.

## A sheet is missing

When I play a story a [sheet](#glossary-0 "Glossary term") is missing.

Possible cause

The sheet has been deleted.

The sheet is private (located in another user's My sheets).

Proposed action

If the sheet is private, ask the owner of the sheet to make it public.

## I cannot change a snapshot’s appearance

I want to use auto for a snapshot property but the snapshot’s appearance is not affected.

Possible cause

The snapshot is too small.

Proposed action

In storytelling view, increase the size of the snapshot.

For more information, see [*Editing slides*](../StoryTelling/Slide/editing-slides.htm).

## I cannot take a snapshot

I want to take a snapshot but it is not possible.

Possible cause

The [visualization](#glossary-1 "Glossary term") you are trying to take a snapshot of is incomplete.

The visualization you are trying to take a snapshot of is an extension. Extensions do not have enabled snapshot functionality by default.

The visualization you are trying to take a snapshot of is a filter pane. Snapshots of filter panes are not supported.

Proposed action

Complete the visualization.

For more information, see [*Creating and editing visualizations*](../Visualizations/create-visualizations-overview.htm).

Enable snapshot functionality in the main script of the visualization extension. To do this you have to set the snapshot property to true. You need permission to edit the script or need to get help from a developer.

For more information, see [Allow snapshots of your visualization](/en-US/sense-developer/November2026/Subsystems/Extensions/Content/Sense_Extensions/Howtos/working-with-data-storytelling.htm).

## I cannot re-order slides in a story

I want to move a slide in the story timeline but it is not possible.

Possible cause

You are using the mouse on a hybrid device.

Proposed action

Do one of the following:

- Turn touch device support off by tapping the navigation button (![Menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg)) and toggling off Touch screen mode.
- Hold the mouse button pressed for a while before moving the slide.
- Alternatively, use the touch screen instead and move the item by long-touch and drag.

## The data in my snapshot does not exist in the visualization

When I go to the snapshot source, I cannot see the same data in the visualization as in the snapshot.

Possible cause

The user taking the snapshot has access to data you do not. This is because of section access rights defined in the data load script.

Proposed action

Request the same section access rights for you in the script.
