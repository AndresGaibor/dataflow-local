---
title: "Creating custom tooltips"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/custom-tooltips.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating custom tooltips

Create a custom tooltip to add extra information to a [visualization](#glossary-0 "Glossary term"). You can include [measures](#glossary-1 "Glossary term") a master visualization [chart](#glossary-2 "Glossary term") or an image. Tooltips display when you hover over a visualization.

Custom tooltip over a pie chart slice

![Custom tooltip over a pie chart slice](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CustomTooltip_501x493.png "Click to view full size")

Custom tooltips are available with the following visualization types:

- Bar chart
- Bullet chart
- Combo chart
- KPI
- Line chart
- Map
- Pie chart
- Scatter plot
- Treemap

## Creating a custom tooltip

Tooltips can contain measures, a chart, or an image. Add a measure from a [field](#glossary-3 "Glossary term") or using an expression. Select a chart from the master visualizations available in the application. Choose an image from the media library or by URL. You can also hide the basic rows that appear in a tooltip by default.

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Select the chart to edit.
3. In the properties panel, click Appearance, and then click Tooltip.
4. Set the toggle to Custom.
5. Optionally, enter a Title and Description for the tooltip.

   Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to use the expression editor if you need to add more than 512 characters.

Tip note
You can remove basic tooltip rows that appear by default by clicking Hide basic rows.

6. If you want to add a measure, under Measures, click Add measure. Select a measure from a field using From a field, or use an expression. The existing expression displays by default, or you can create a custom expression. Click ![Open Expression editor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor. You can change the label of the tooltip using Label as well as its formatting using Number formatting.
7. If you want to add a chart, under Chart, click Add chart.

- From the Master items list, select the master visualization to add to the tooltip.
- Under Chart size, select the size of the chart container in the tooltip.
  - Small. Sets the width and height of the container to 140 pixels.
  - Medium. Sets the width and height of the container to 200 pixels.
  - Large. Sets the width and height of the container to 340 pixels.

  Tip noteAfter you add the chart, you can edit it by clicking Edit master item. See [*Editing a master visualization*](../Assets/edit-master-visualization.htm).

8. If you want to add an image, under Images, Click Add an image.

- Under Type, select whether to add the image from your Media library or from a URL.
  - Media library: Select the image from the media library.
  - URL: Enter a URL. Your Qlik Sense administrator must allowlist external URLs in the Content Security Policy.
- Under Size, select the size of the image container in the tooltip.
  - Small. Sets the width and height of the container to 50 pixels.
  - Medium. Sets the width and height of the container to 200 pixels.
  - Large. Sets the width and height of the container to 340 pixels.
  - Original. Qlik Sense fits the image into the container. If the image is larger than 340 pixels, it is scaled down.

## Limitations

Custom tooltips have the following general limitations:

- Custom tooltips are disabled for a bar or line chart if any of the dimensions in the chart are using a show condition.

### Limitations of charts in custom tooltips

Charts have the following limitations with custom tooltips:

- Charts will not appear in custom tooltips when selecting visualizations on touch devices.
- Treemap chart must have only one [dimension](#glossary-5 "Glossary term") to use the chart in a custom tooltip.
- Chart in tooltip is not supported in Storytelling.
- Using container and trellis container charts inside a custom tooltip is not supported.
- Charts within custom tooltips will not be included in the tooltip when you are monitoring a visualization.

Related learning:

- [How do I customize a tooltip display?](/lnk/How_customize_tooltip)
