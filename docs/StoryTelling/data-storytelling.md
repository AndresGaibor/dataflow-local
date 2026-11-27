---
title: "Data storytelling"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/StoryTelling/data-storytelling.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Tutorial - Build an analytics application"]
---

# Data storytelling

With data storytelling you can create a presentation based on the data in your application. You can take [snapshots](#glossary-1 "Glossary term") of selected [visualizations](#glossary-2 "Glossary term") and use them in your narrative together with text, shapes, and effects.

You create slides and design the story with your particular audience in mind. In your narrative, you focus on key elements and create a convincing story to make your message clear.

An additional, useful feature of data storytelling is that you can easily switch between a snapshot in the presentation and its context in the application. In the application context, you can make new [selections](#glossary-3 "Glossary term") and continue the analysis from where you left off in the presentation.

After the analysis, you can resume the presentation.

## Taking snapshots

You will start the creation of your story by taking snapshots in the application. In the top right corner, use ![Previous](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_left.svg) to move to the [sheet](#glossary-4 "Glossary term") Dashboard.

In the presentation you will focus on the three largest regions and analyze the sales trends.

Do the following:

1. Right-click the visualization Sales per Region and select Storytelling snapshots > Take snapshot.
2. In Region, select Nordic.
3. Right-click the visualization Top 5 Customers and select Storytelling snapshots > Take snapshot.
4. In the annotation dialog that opens:

   1. Type Nordic in the annotation text field.
   2. Click outside the annotation dialog to close it.
5. Right-click the visualization Quarterly Trend and select Storytelling snapshots > Take snapshot.
6. In the annotation dialog that opens:

   1. Type Nordic in the annotation text field.
   2. Click outside the annotation dialog to close it.
7. In Region, deselect Nordic and select USA.
8. Take snapshots from the same visualizations as for Nordic (Top 5 Customers and Quarterly Trend) and annotate them with USA.
9. In Region, deselect USA and select Japan.
10. Take snapshots from the same visualizations as for Nordic (Top 5 Customers and Quarterly Trend) and annotate them with Japan.

You have taken all the snapshots you need and can start creating your data storytelling slides.

## Creating a simple story

You will create a short and simple story, where the focus is on creating a few slides with snapshots and titles. A screen shot of the slide is presented before the step-by-step instructions.

### Slide 1

Slide with title 'Three largest regions' and three snapshots of pie charts

![Slide with a title and three snapshots.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_Story1.png "Click to view full size")

Do the following:

1. In the toolbar, open the application navigation menu and under Narrate, select Storytelling.

   The data storytelling editor is opened.
2. Click ![Text](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text_object.svg) and drag a title to the slide.
3. Type the title Three largest regions.
4. Click ![Snapshot ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_photo_library_outline.svg) to see the snapshots that you took previously.
5. Drag the pie chart Sales per Region snapshot to the slide.
6. Resize the pie chart and place it to the leftmost on the slide.
7. Click ![Effects](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_effects_outline.svg) to open the Effect library.
8. Drag the option Any value to the pie chart.

   The value USA is automatically highlighted.
9. Copy the pie chart and paste it next to the first one. You can either use Ctrl+C and Ctrl+V or ![Duplicate](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) and ![Paste](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_paste.svg) in the toolbar.
10. In the new pie chart, click ![Effects](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_effects_outline.svg) and select Nordic in the list Select data point.
11. In the same manner as for the second pie chart, create a third pie chart and highlight Japan.

The slide is complete.

### Slides 2-4

Slide with title 'Nordic' and two snapshots of a bar chart and a line chart.

![Slide with one title and two snapshots.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_Story2.png "Click to view full size")

Slides 2-4 show the top five customers and the quarterly sales trend for the three regions. The snapshots are stored in the library in the order they were taken, with the latest one at the top. If you have followed the procedures when taking these snapshots, the two at the top should be Japan, the two ones below, USA, and the remaining two, Nordic.

Do the following:

1. In the left-hand corner, click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) and add a blank slide.
2. Click ![Snapshot ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_photo_library_outline.svg) to see the snapshots.
3. Drag the Top 5 Customers bar chart for Nordic to the slide.
4. Drag the Quarterly Trend line chart for Nordic to the slide.
5. Click ![Text](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text_object.svg) and drag a title to the slide.
6. Type the title Nordic.
7. Resize and align the title and snapshots according to the screenshots.
8. Right-click the sheet Nordic in the story timeline to the left and select Duplicate to create a new sheet that can be used as a template for the next sheet.
9. Change the title to USA.
10. Select the Top 5 Customers snapshot and click ![Snapshot ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_camera2.svg) to open the Replace snapshot dialog where you select the second snapshot in the drop-down list. If you followed the instructions it has the annotation USA.

    Tip noteYou can right-click the snapshot and select Go to source, if you want to see the selections in that version of the snapshot. Then, click Return to go back to the story.
11. Replace the Quarterly Trend snapshot just as you did with the Top 5 Customers snapshot.
12. Duplicate the USA sheet and adjust it to present Japan. Now use the snapshots in the top of the list in the Replace snapshot dialog. If you followed the instructions they have the annotation Japan.

When analyzing these slides it is important to know that the figures for 2014 are half-year figures. Extrapolating the figures for the full year would then give different forecasts for the different regions.

The story is complete. Click ![load data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_play_2_outline.svg) Play story in the toolbar to play your presentation. You can navigate with the left and right arrow keys.

Close the story and make edits, if needed. Below the slide, you have tools for cutting, copying, and pasting that can be useful when you edit your presentation. And, of course, you can use the panel to the right.

#### Switching between data storytelling and the application context

In data storytelling, you can switch any time from the presentation to the application context. Right-click the snapshot and select Go to source to open the application sheet where the snapshot was taken. This gives you a dynamic option to leave the presentation and make data analysis in response to questions from the audience. When you have finished analyzing, you return to the presentation by clicking Storytelling in the toolbar.

The go to source option is also useful for the special purpose of verifying that the correct bar charts and line charts are used. When you select Go to source you will see which region is selected for that specific snapshot.

#### Additional options

There are many options that have not been used in this story. Experiment on your own. Try and add effects to the bar chart. Add a new slide and embed a complete application sheet where you can make selections when you are in play mode. Add URLs or [bookmarks](#glossary-5 "Glossary term") to text strings. There is plenty more to discover.
