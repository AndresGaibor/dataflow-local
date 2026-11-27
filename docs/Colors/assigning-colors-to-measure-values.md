---
title: "Assigning colors to master measure values"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Colors/assigning-colors-to-measure-values.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Assigning colors to master items"]
---

# Assigning colors to master measure values

You can assign a color gradient or segment scheme to a master [measure](#glossary-0 "Glossary term"), enabling you to color [visualizations](#glossary-1 "Glossary term") by measure, using colors other than the default color schemes.

If you choose to color by single color, the master measure's color is used instead of the color scheme.

To assign custom segment or gradient colors to the values in a master measure, do the following:

1. Access and enable segment colors.
2. Select the template scheme.
3. Select the segment format.
4. Optionally, add or remove limits.
5. Optionally, edit your segment limits.
6. Assign colors to your segments.
7. Save.

## Accessing and enabling segment colors

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Click Master items.
3. Select a master measure from your library.
4. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
5. Click on the Segment colors tab.
6. Set the Segment colors button to Custom coloring.

## Selecting the template scheme

The template scheme provides a default template to edit. You can choose from the default classes and gradients.

Do the following:

- Under Select a template scheme, select a template scheme.

## Selecting the segment format

The segment format determines how colors will be applied. Percentage adds value classes based on where values fit into the percentile of their value. Fixed value uses defined values to set the limits of each segment.

Do the following:

- Set Segment format to Fixed value or Percentage.

## Adding, editing and removing limits

By default, the number of segments depends on the scheme selected. You can create additional segments by adding limits. When a new segment is created a pointer marks the value of its limit.

Do the following:

- Click on the Add limit button to add a limit to the gauge.
- Use the slider to change the value of a limit. You can also type a value for the selected limit.
- Click on the Remove limit button to remove the selected limit.

## Editing segments

By default, segment colors depend on the scheme selected. You can change the color of a segment and its ending.

Do the following:

- Click the segment to change colors.
- Select Gradient to use different shades of colors in the transition between segments for the selected limit.
