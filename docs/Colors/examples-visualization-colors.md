---
title: "Examples of visualization color settings"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Colors/examples-visualization-colors.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Changing the appearance of a visualization", "Coloring a visualization"]
---

# Examples of visualization color settings

You can use a number of different methods to control the use of colors in your [visualizations](#glossary-0 "Glossary term").

You can manually apply colors to your visualizations using the following methods:

- Color by single color
- Color by multiple colors
- Color by [dimension](#glossary-1 "Glossary term")
- Color by [measure](#glossary-2 "Glossary term")
- Color by expression

In the example dashboard below, each method of setting colors has a corresponding visualization. This section outlines each example as well as the specific settings used in the [properties](#glossary-3 "Glossary term") panel.

![Dashboard with each method of setting colors has a corresponding visualization.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_en_us_LabeledVisualizations.png "Click to view full size")

## Color by single color

Visualizations can be colored with a single user-defined color. Colors can be selected from a palette or color wheel or by entering a hex color code.

In this example visualization, a single color has been applied to the line chart.

![Line chart with single color applied.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_en_us_LabeledVisualizationsColorBySingleColor.png)

Properties panel settings

For this visualization, the following properties were set in the properties panel under Appearance > Colors and Legends:

- Colors: Set to Custom and Single color. Color set as hex value 4477aa.

## Color by multiple colors

Visualizations with multiple measures can have different colors applied to each measure. When a visualization is colored using Multicolor, colors are automatically applied from a default color scheme of 12 colors or 100 colors.

In this example visualization, multiple colors have been applied to the measures of Expense Amount and Budget in the line chart.

![Line chart with multiple colors applied.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_en_us_LabeledVisualizationsColorByMulticolor.png "Click to view full size")

Properties panel settings

For this visualization, the following properties were set in the properties panel under Appearance > Colors and Legends:

- Colors: Set to Custom and Multicolored.
- Color scheme: Set to 12 colors.

## Color by master item

Colors can be kept consistent across visualizations for dimensions or measures through setting colors in [master items](#glossary-4 "Glossary term"). When set to use master item colors, visualizations will use all colors associated to the master items in the visualization. Master item colors can be used when Color is set to Single color or Multicolor.

In these example visualizations, both the bar chart and line chart share a master measure, Revenue, that is colored orange. In each visualization, the same assigned color is used for each instance of Revenue. The line chart is colored by a second master measure, Expense Amount, which is colored blue.

![Bar chart and line chart with colors by master item.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_en_us_LabeledVisualizationsColorByMasterItem.png)

Master measure settings

For this visualization, the following settings were applied to the master measures in Edit measure:

- Color: Hex color set as f8981d for Revenue and 4477aa for Expense Amount.

For more information, see [*Assigning colors to master items*](assigning-colors-to-master-items.htm).

Properties panel settings

For the bar chart, the following properties were set in the properties panel under Appearance > Colors and Legends:

- Colors: Set to Custom and Single color.
- Use library colors: Set to enabled.

For the line chart, the following properties were set in the properties panel under Appearance > Colors and Legends:

- Colors: Set to Custom and Multicolor.
- Use library colors: Set to enabled.

## Color by measure

When a visualization colored by measure, sequential or diverging gradients or classes are applied to values in the chart based on the values of the selected measure. Visualizations can be colored by measures within the visualization or they can be colored with measures associated to values in the visualization.

In this example, this bar chart is colored by the measure used in the visualization, Revenue. A diverging gradient has been applied to the values in the chart based on the Revenue value for each dimension value.

![Bar chart with colors by measure.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_en_us_LabeledVisualizationsColorByMeasure.png "Click to view full size")

Properties panel settings

For this visualization, the following properties were set in the properties panel under Appearance > Colors and Legends:

- Colors: Set to Custom and By measure. The measure selected is Revenue.
- Color scheme: Set to Diverging gradient.
- Reverse colors: Set to enabled.
- Range: Set to Auto.

## Color by dimension

When a visualization is colored by dimension, each value within the visualization is assigned a color based on an associated value from the coloring dimension. When colored by dimension, colors are automatically applied from a default palette set of 12 or 100 colors.

### Example 1: Coloring by a dimension in the visualization

In this example, the line chart is colored by the dimension of the different sales representatives, using the 100 colors scheme. Each sales representative has their own distinct color in the visualization.

Line chart colored by dimension

![Line chart with colors by dimension.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_en_us_LabeledVisualizationsColorByDimension.png "Click to view full size")

Properties panel settings

For this visualization, the following properties were set in the properties panel under Appearance > Colors and Legends:

- Colors: Set to Custom and By dimension. The dimension Sales Rep Name is selected.
- Persistent colors: Set to enabled.
- Color scheme: Set to 100 colors.

### Example 2: Coloring by a dimension not included in the visualization

In this example, the bar chart is colored by the dimension of Region, using the 12 colors scheme. The bar for each sales representative is colored by the region in which they work.

![Bar chart with colors by dimension not in cluded in the visualization.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_en_us_LabeledVisualizationsColorByDimension2.png "Click to view full size")

Properties panel settings

For this visualization, the following properties were set in the properties panel under Appearance > Colors and Legends:

- Colors: Set to Custom and By dimension. The dimension Region is selected.
- Persistent colors: Set to enabled.
- Color scheme: Set to 12 colors.

## Color by expression

You can use expressions to set specific colors to appear with specific values, enabling conditional coloring of values in your visualizations. When a visualization is colored by expression, you define the colors and how the colors are applied to values within the expression.

### Example 1: Color by expression in a table

In this example, the table visualization uses two expressions, one for the background color and one for the text. These expressions apply conditional colors to the background and text based on which rows contain the top 10 and bottom 10 values for Revenue.

![Table with colors by expression.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_en_us_LabeledVisualizationsColorByExpression.png "Click to view full size")

Properties panel settings

For this visualization, the following properties were set in the properties panel under Data > Columns:

- Background color expression: if(Rank(Sum([Sales Quantity]\*[Sales Price])) <= 10, 'honeydew', if(Rank(-Sum([Sales Quantity]\*[Sales Price])) <= 10, 'mistyrose', ))
- Text color expression: if(Rank(Sum([Sales Quantity]\*[Sales Price])) <= 10, 'green', if(Rank(-Sum([Sales Quantity]\*[Sales Price])) <= 10, 'red', ))

### Example 2: Color by expression in a chart

In this example, the bar chart uses an expression to assign specific colors to different values in the Customer [field](#glossary-5 "Glossary term").

![Bar chart with colors by expression.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_en_us_LabeledVisualizationsColorByExpression2.png "Click to view full size")

Properties panel settings

For this visualization, the following properties were set in the properties panel under Appearance > Colors and Legends:

- Colors: Set to Custom and By expression.
- Expression: Set to if([Customer]= 'Fill It', rgb(100, 149, 227), if([Customer]= 'Hetrick Systems', rgb(100, 149, 200), if([Customer]= 'Icon', rgb(100, 149, 175), if([Customer]= 'J. S. Lee Associates', rgb(100, 149, 150), 'grey')))).
- This expression is a color code: Set to enabled.
