---
title: "Best practices for designing visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/create-viz-best-practices.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization"]
---

# Best practices for designing visualizations

## Decluttering your applications

Too much information in an application makes it difficult to see what is important. Today’s modern user interface style is a cleaner, simpler, flatter style of design. A simplified design subtly guides the reader and allows them to stay focused.

#### Less is more

Users often try to include too much information in one application. Line charts with several measures can be confusing and difficult to interpret. Try creating several smaller visualizations to spread this information out onto the page. It also allows the reader to efficiently compare and contrast visualizations that are side-by-side. You can also use alternative dimensions and measures to allow the reader to quickly switch between measures without overcrowding a visualization. For more information, see [*Changing the data of a visualization*](change-data-of-visualization.htm).

There are number of different ways you can improve the aesthetics and functionality of your application. Depending on your audience and what data you want to highlight, the way you design your [visualization](#glossary-1 "Glossary term") may have a serious impact on the reader's interpretation of the data.

#### Know your limits

Consumers of your visualizations may be working with limited screen space or resolution. Qlik Sense uses responsive design to address these limitations. However, if screen space or resolution is too limited, certain design accommodations are necessary. These can include:

- A subset of data being displayed in bar charts and line charts. When the number of dimension values exceeds the width of the visualization, a mini chart with a scroll bar is displayed.
- Collapsed menus for selecting data filters. When the number of dimension values exceeds the space available for the filter pane, the menu is collapsed. Application consumers have to click on the dimension name in the title of the filter pane to open a new pane. They can then make their selections in the new pane. Additionally, when there is limited space, dimension names may appear as ellipses in filter pane titles. Application consumers have to click on the ellipses to view the name of the filter pane.
- Truncated names in chart legends. Names that are too long for the space available for dimensions and measures are truncated. An ellipses is added to the end of truncated name. Application consumers can hover their mouse pointer over the truncated name to view the complete name.
- Missing legends, labels and titles.

Application consumers can expand visualizations to address some of these issues. However, we recommend that you test your applications on devices where the applications may be consumed. You can also use various tools to test, such as responsive design mode in Firefox (Ctrl + Shift + M). If necessary, you can move visualizations to new [sheets](#glossary-2 "Glossary term") reduce the amount of data shown in visualizations, and so on.

## Color accessibility

The spectrum of colors is narrower for people who have color-based visual impairment. They may interpret your visualization differently than you intended.

For example, some people see the colors red and green more as yellow or brown. This form of red-green color vision deficiency is the most common. This is worth noting since red often carries a negative connotation in data visualizations, especially in finance.

A red or green KPI status can be confusing. You can use shapes with colors as performance indicators to make your designs more accessible. For example, use a red empty circle to denote bad, a green full circle for good, and a triangle as a warning symbol that only appears when a KPI status is at an unacceptable level.

Lines, bars, and pie slices can be difficult to distinguish when the colors are distorted.

For more information, see [*Changing the appearance of a visualization*](change-appearance-of-visualization.htm).

## Filter and icon placement

Filers and icons are an essential part of data visualization, but it can be difficult to know where to place them or how to sort them.
You can often anticipate where the user will begin to read based on a few well-established design principles.

### Left placement

Several popular websites use left-side navigation tiles and filters. This is due to the fact that many languages read from left to right. As a result, the left-side of the screen is where these readers look most frequently.
Users who are scanning for
content tend to gravitate toward the left side of the screen. The farther to
the right objects are, the less users will look at them.
If all your filters and icons are stacked vertically on the left, it gives them equal weight.

Alternately, with languages where text is written right to left, the opposite of this is true. This should be kept in mind if your applications are translated into these languages.

### Top placement

Another common placement option for icons and filters is along the top of an application. By not placing filters or icons on the left it gives more space for larger visualizations with distracting menus. When filters and icons are placed above visualizations they are also seen as separate from the content below. This can help show the reader that you are prioritizing the filters or icon. If all your filters and icons are side-by-side at the top, the one furthest to the left carries more weight and is prioritized by the reader.

### Information hierarchy

Sometimes you want your reader to prioritize certain visualizations over others. You can show hierarchy of information by using a few key design best practices. For example, you can use different sizes to emphasize some visualizations. Larger information is seen as more important: by increasing the font or [chart](#glossary-3 "Glossary term") size, you can show the reader where to look first.

Page placement also plays a part in information hierarchy. The information at the top of a page is perceived as more important than information at the bottom of the page because it is read first. Information on the first page is perceived as more important than information on the last page.

## Adding context to KPIs

KPIs are a great way to communicate some of the
big ideas inside your application. However, KPI values do not provide any context to the numbers and calculations that are happening behind the scenes. A green light next to a KPI does not tell the reader if the goal was barely achieved, or if you greatly surpassed it.

To help bring context to
your KPIs, include supporting information next to the value in smaller text. For example, you can compare the current KPI value with the value from the previous year. You can also add a small bar chart without axes or values to provide information about the current trend.

## Avoid the pitfalls of data visualization

To experience the benefits of data visualizations you must avoid the pitfalls. Here are some common ones:

### Color abuse

Do not overdo colors. Be aware that the wrong color in the wrong place might cause confusion rather than clarity. Also, the same color may mean different things in different parts of the world.

### Misuse of pie charts

Avoid having pie charts side by side to compare. Try not to squeeze too much information into them.

### Visual clutter

Too much information defeats the purpose of clarity. Use a maximum of nine KPIs, and remove all visual clutter.

### Style over substance

A beautiful visualization is not necessarily the most effective. Use design best practices at all times.

### Bad data

Spot and correct issues with your data before you present it. Do not let your visualization take the blame for bad information.
