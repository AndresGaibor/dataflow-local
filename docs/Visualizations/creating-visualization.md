---
title: "Choosing the right visualization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/creating-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations"]
---

# Choosing the right visualization

Visualizations let you present data so that your applications users can interpret and explore it. For example, a bar chart that compares sales numbers for different regions, or a table with precise values for the same data. Good visualizations help you quickly and accurately interpret displayed data.

Visualizations are easy to add and customize. They can take the form of [charts](#glossary-1 "Glossary term"), such as bar charts, pie charts, tables, gauges, or treemaps. Each chart type has unique functionality. Qlik Cloud Analytics automatically highlights items associated with your selections so you can drill-down and filter.

## Select visualization types that align with your purpose

Each visualization type has a specific goal. You need to think about the purpose of your visualization, and pick a visualization type that lets you explore your data for that purpose effectively.

For example: You want to show how a measure, quarterly sales, behaves over time. You should create a line chart, because one of its strengths is displaying how measure values change over time. Alternatively, you can start with the type of analysis you want to make. From the available analyses, you could select trend over time as your analysis type, which builds a line chart for you.

For more information, see:

- [*Best practices for choosing visualization types*](when-to-use-visualizations.htm)
- [*Creating and editing visualizations*](create-visualizations-overview.htm#Best%20practices%20for%20designing%20visualizations)
- [*Creating and editing analyses*](../Analyses/creating-analyses.htm)

## Which visualizations are available?

The following types of visualizations are available from Charts in the assets panel:

- Charts that visualize the data with elements like bars, lines, or points, or present them textually.
- Dashboard objects that help with navigation through the available analytics. They can also automate the performance of certain actions.
- Legacy visualizations that are still supported, but may have newer version available or do not have the same level of support for features such as embedding.

There are also analyses available from Analyses in the assets panel. Analyses allow you to select the kind of analysis you want to visualize with your data and let the analytics application create the chart for you.

The best choice of chart or analysis type depends on the purpose of the visualization.

For more information, see [*Best practices for choosing visualization types*](when-to-use-visualizations.htm).

If the predefined visualizations does not fill your purpose, you can use a visualization extension. You find them in the assets panel under ![Extensions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_puzzle_outline.svg) Custom objects.

### Available built-in visualizations

The built-in visualizations are those that are included regardless of your Qlik Cloud subscription. Built-in visualizations are fully supported.

These are the built-in visualizations.

#### Visualizations

- ![Vertical bar chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bar_chart_outline.svg) Bar chart: Visualize differences in measures over one or more dimensions, arranged as a series of bars with varying height. Can be displayed in vertical or horizontal format, and with grouped, stacked, or butterfly presentation.

  - ![Box plot](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_boxplot.svg) Box plot: The box plot is suitable for comparing range and distribution for groups of numerical data, illustrated by a box with whiskers, and a center line in the middle.
  - ![Bullet chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bullet_chart_outline.svg) Bullet chart: Bullet charts can be used to visualize and compare performance of a measure to a target value and to a qualitative scale, such as poor, average, and good.
  - ![Vertical combo chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_combo_chart_outline.svg) Combo chart: The combo chart combines bars and lines in the same chart. The bars and lines have different axes to enable comparing percentages and sums. Available as horizontal or vertical combo chart.
  - ![Distribution chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_distribution_plot_outline.svg) Distribution plot: The distribution plot is suitable for comparing range and distribution for groups of numerical data. Data is plotted as value points along an axis.
  - ![Filter container](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filterpane_outline.svg)Filter pane: The filter pane allows you to control what data that is shown in the visualizations on a sheet. A filter pane can filter the data of several dimensions at once.
  - ![Funnel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filter2.svg) Funnel chart: A funnel chart is a visual representation of the connected stages of a linear process.
  - ![Gauge chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_gauge_chart_outline.svg) Gauge: The gauge is used to display the value of a single measure, lacking dimensions.
  - ![Grid chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_chart_outline.svg) Grid chart: A chart that displays comparative data and with the values represented as colors.
  - ![Histogram](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_histogram_outline.svg) Histogram: The histogram is suitable for visualizing distribution of numerical data over a continuous interval, or a certain time period. The data is divided into bins.
  - ![KPI](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_kpi_outline.svg) KPI: The KPI is used to present central performance figures. You can add a link to a sheet.
  - ![Line chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_chart.svg) Line chart: The line chart displays data lines between values. Line charts are often used to visualize a trend in data over intervals of time. Can also be presented as an ![Area line chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_chart_area.svg) Area line chart.
  - ![Map](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_map_outline.svg) Map: The map is used to combine geospatial data and measure values, such as the sales for a region or a store.
  - ![Mekko chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_marimekko.svg) Mekko chart: The mekko chart compares a group while comparing category items contained within these groups.
  - ![Org chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_org_chart_outline.svg) Org chart: Creates an organization chart with a tree structure.
  - ![Pie chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pie_chart_outline.svg) Pie chart: The pie and donut charts show the relation between a single dimension and a single measure. Can also be presented as a ![Donut chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pie_chart_donut.svg) Donut chart.
  - ![Pivot table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pivot_table_outline.svg) Pivot: Pivot presents dimensions and measures as rows and columns of a pivot table. The pivot table allows you to analyze data in multiple dimensions at a time. The data in a pivot table may be grouped based on a combination of the dimensions, and partial sums can be shown. Pivot has styling options not available to Pivot table.
  - ![Pivot table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pivot_table_outline.svg) Pivot table: The pivot table presents dimensions and measures as rows and columns of a table. The pivot table allows you to analyze data in multiple dimensions at a time. The data in a pivot table may be grouped based on a combination of the dimensions, and partial sums can be shown.
  - ![Sankey chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_stream.svg) Sankey chart: A flow chart diagram chart visually emphasizing major transfers or flows within defined system boundaries.
  - ![Scatter chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_scatter_chart_outline.svg) Scatter plot: The scatter plot presents values from two measures. This is useful when you want to show data where each instance has two numbers, for example, country (population and population growth). An optional third measure can be used and is then reflected in the size of the bubbles. When showing large data sets colors will be used instead of bubble size to represent the measure size.
  - ![Table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) Straight table: The straight table allows you to present tabular data for detailed analysis. You can apply pagination to simplify consumption of large data volumes. You can also allow users to add and remove columns temporarily during analysis, using an enhanced chart exploration experience.
  - ![Treemap](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_treemap_outline.svg) Treemap: The treemap shows hierarchical data. A treemap can show a large number of values simultaneously within a limited space.
  - ![Waterfall chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_waterfall_chart_outline.svg) Waterfall chart: The waterfall chart illustrates how an initial value is affected by intermediate positive and negative values.
  - ![Write table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_write_table_outline.svg) Write table: Use the write table to allow users to make changes in editable columns during data analysis.

#### Dashboard objects

- ![Treemap](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_play.svg) Animator: You can animate changes in your [visualizations](#glossary-2 "Glossary term") over a period of time.
- ![Button](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_button_outline.svg) Button: You can use buttons to add quick links for easy selection and navigation in your application.
- ![Date picker](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_calendar.svg) Date picker: You can select a single date or a range of dates from a calendar.
- ![Select image](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) Image: Insert images directly onto the sheet.
- ![Layout container](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_layout_container_outline.svg) Layout container: Add and arrange visualizations in a container.
- ![Line](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_object.svg) Line: Add vertical and horizontal lines to a [sheet](#glossary-3 "Glossary term").
- ![Navigation menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) Navigation menu: The navigation menu adds a sheet navigation options into your sheet.
- ![Natural language insights](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_natural_language_generation.svg) NL insights: The NL insights visualization displays natural language insights about data in the form of a chart.
- ![Slider](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_slider_outline.svg) Slider: Allow users to change the value of fields and variables during analysis.
- ![Container box](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_box_outline.svg) Tab container: You can add visualizations in a limited space and show or hide the visualizations inside the container based on conditions.
- ![Text](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text_object.svg) Text: You can use the text visualization to add text and links to webpages.
- ![Trellis container](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_outline.svg) Trellis container: Creates a trellis chart based on a master [visualization](#glossary-4 "Glossary term").
- ![Variable input](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) Variable input: You can set the value of a variable.
- ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_video_outline.svg) Video player: You can add a video to your sheet.

#### Legacy objects

- ![Funnel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filter2.svg) Funnel chart: A funnel chart is a visual representation of the connected stages of a linear process.
- ![Network chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_auto_layout_outline.svg) Network chart: Creates a cluster diagram representing a graphical chart of a computer network.
- ![Pivot table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pivot_table_outline.svg) P&L pivot: Creates a pivot table that you can style, for example for profit and loss reporting.
- ![Network chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_auto_layout_outline.svg) Radar chart: Creates a two-dimensional chart using radial axes to show the scoring of a measure in one dimension or another.
- ![Table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) Table: The table displays values in record form, so that each row of the table contains fields calculated using measures. Typically, a table includes one dimension and multiple measures. The Straight table has replaced the Table as the default table visualization.
- ![Text](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text_object.svg) Text & image: You can use the text & image visualization to add text, images, measures and links to a webpage.
- ![Variance Waterfall](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_waterfall_chart_outline.svg) Variance Waterfall: Shows the variance between two measures over the different values of a dimension.
- ![Word cloud](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_treemap_outline.svg) Word cloud: A cloud chart of words with their size based on measure value.

### Available analyses

- ![Anomaly (spike)](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_combo_chart_outline.svg) Anomaly (spike): Detect and show large data variations including spikes and dips in a time series.
- ![Anomaly (spike)](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_combo_chart_outline.svg) Anomaly (trend): Detect and show abrupt data variations including change points between time series segments.
- ![Breakdown](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_treemap_outline.svg) Breakdown: Show multiple dimensions in order of contribution.
- ![Breakdown (geospatial)](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_map_outline.svg) Breakdown (geospatial): Show geographical contributions to a measure.
- ![Calculated measure (KPI)](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_kpi_outline.svg) Calculated measure (KPI): Show a calculated measure.
- ![Clustering (k-means)](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_scatter_chart_outline.svg) Clustering (k-means): Show clusters of measures associated with a dimension using a statistical algorithm.
- ![Clustering (k-means)](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_scatter_chart_outline.svg) Comparison: Show multiple measures for a dimension.
- ![Correlation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_kpi_outline.svg) Correlation: Show the strength of the relationship between two fields.
- ![Mutual information](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bar_chart_outline.svg) Mutual information: Detect and show dependencies between the source and driver fields.
- ![Overview](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_boxplot.svg) Overview: Show the distribution of measures for one or more dimensions.
- ![Process control (mean)](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_chart.svg) Process control (mean): Show measures over a time period compared with the overall mean of expected values.
- ![Process control (mean)](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_chart.svg) Process control (rolling mean): Show the performance of a measure over time between two calculated control limits.
- ![Ranking](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bar_chart_outline.svg) Ranking: Show dimensions in the order of their contribution to a measure.
- ![Ranking](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bar_chart_outline.svg) Ranking (grouped): Show hierarchical dimensions in order of their contribution to a measure.
- ![Relative importance](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_combo_chart_outline.svg) Relative importance: Show the relative importance of dimensions contributing to a total.
- ![Time series decomposition](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_chart.svg) Time series decomposition: Decompose a time series into trend, seasonal, and residual components.
- ![Time series decomposition](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_chart.svg) Trend over time: Show the performance of a measure over time, optionally broken down by a dimension.
- ![Time series decomposition](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_chart.svg) Trend with forecast: Show measures along with forecast over the current and future time periods.
- ![Year to date](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bar_chart_outline.svg) Year to date: Show a comparison of dimensions for the same period in previous years.

Related learning:

- [Getting started with Qlik Sense](/lnk/Getting_started_QS)
- [Foundations of Building Visualizations](/lnk/Foundations_building_visualizations_QS)
- [How do I create visualizations?](/lnk/How_do_I_create_visualizations)
- [How do I use the chart suggestions toggle?](/lnk/How_use_chart_suggestions)
