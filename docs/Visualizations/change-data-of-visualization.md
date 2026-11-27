---
title: "Changing the data of a visualization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/change-data-of-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Changing the data of a visualization

The data displayed within a [visualization](#glossary-0 "Glossary term") can be changed after the visualization is created.

For example, you may want to add additional [dimensions](#glossary-1 "Glossary term") or [measures](#glossary-2 "Glossary term") to a [chart](#glossary-3 "Glossary term") to add depth to the existing data. Alternatively, you may need to correct an invalid dimension or measure.

## Adding dimensions and measures to a visualization

You can add multiple dimensions and measures to a visualization to add depth to the data displayed. Addition dimensions and measures enabled you to view more information in a single visualization. For example, the image below contains a visualization with the measure Sales and a dimension Month.

Line chart with the measure Sales.

![Line chart with one measure.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_LineChart2.png "Click to view full size")

You can add a second measure, Gross Sales. The example line chart now gives use more context by enabling a comparison of Gross Sales to Sales.

Line chart with the measures Sales and Gross Sales.

![Line chart with two measures.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_LineChart2.png "Click to view full size")

Do the following:

1. In the properties panel, click the Data tab.

   The Data tab is expanded.
2. In the Dimensions or Measures section, click Add to add a dimension or measure.

   A dialog with a text box opens. Below the text box all available dimensions or measures are listed, grouped into Dimensions or Measures (that is master items) and Fields.
3. Start typing in the text box.

   A list of matching fields and dimensions or measures is displayed.

   Information noteYou can also create a dimension by entering an expression directly in the text box, or by clicking ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to create a dimension in the expression editor.

   Information noteIf no measure is displayed, you need to create one. You can enter an expression directly in the text box, or you can click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to create a measure in the expression editor.
4. Select the dimension or measure that you want to use.

The dimension or measure is added to the visualization. The new dimension or measure settings are shown in the [properties](#glossary-4 "Glossary term") panel.

## Adding alternative dimensions and measures to a visualization

Alternative dimensions and measures are dimensions and measures that are added to a visualization, but are not displayed until a user chooses to switch which dimensions and measures are being displayed during visual exploration. You can toggle which of your dimensions and measures are displayed using the exploration menu of a visualization.

[Adding alternative dimensions and measures to a visualization](https://share.vidyard.com/watch/yHmdrk5feLWqpcNYs3gDEK)

For more information, see [*Visual exploration*](../UserInterface/visual-exploration-menu.htm).

Information noteYou can add alternative dimensions and measures to all chart types but changing alternative dimension and measures in the visualization can only be done in bar, line, and combo charts. Only alternative dimensions can be changed in the pie charts visualization and only alternative measures in scatter plots.

Alternative dimensions and measures enable you conserve space on your sheets. Rather than make multiple similar visualizations of the same type, you can use alternative dimensions and measure with a single visualization. You can then switch between the displayed dimensions and measures. For example, if you wanted to see total sales by product category and total sales by product subcategory, you could add product category as a dimension and product subcategory as an alternate dimension in the same visualization.

Alternative dimensions and measures enable you to have more dimensions and measures associated to a visualization that the display limit. Many visualizations have limitations on how many dimensions and measures that can be displayed at the same time. A line chart with two or more measures can only have one dimension, and a line chart with two dimensions can only have one measure. Alternative dimensions and measures enable you to exceed that limit.

Alternative dimensions and measures can be added like normal dimensions and measures in the properties pane. You can also drag dimensions and measures in the Data section of the properties panel into the Alternative dimensions or Alternative measures section.

Do the following:

1. In the properties panel, click the Data tab.

   The Data tab is expanded.
2. In the Dimensions or Measures section, click Add alternative.

   A dialog with a text box opens. Below the text box all available dimensions or measures are listed, grouped into Dimensions or Measures (that is master items) and Fields.
3. Start typing in the text box.

   A list of matching fields and dimensions or measures is displayed.

   Information noteYou can also create a dimension by entering an expression directly in the text box, or by clicking ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to create a dimension in the expression editor.

   Information noteIf no measure is displayed, you need to create one. You can enter an expression directly in the text box, or you can click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to create a measure in the expression editor.
4. Select the dimension or measure that you want to use.

The alternate dimension or measure is added to the visualization.

## Editing data in a visualization

You can edit and adjust the data in a visualization. You may need to edit an existing dimension or measure to adjust it to create a stronger visualization or correct an invalid dimension or measure. You may also want to edit a [master item](#glossary-5 "Glossary term") in a visualization to change the master item across all visualizations.

### Invalid dimensions and measures

Dimensions and measures are invalid when the associated expression cannot be interpreted by Qlik Sense.

If you create an invalid dimension or edit an existing one so that it becomes invalid, the dimension is presented in the properties panel as dimmed with a red hue and the text Invalid dimension to indicate that the dimension is invalid. If you use an invalid dimension in a visualization, the visualization cannot be displayed.

If you create an invalid measure or edit an existing one so that it becomes invalid, the Expression text box under Measures in the properties panel is presented with a red border to indicate that the measure is invalid.

### Editing a dimension

You can edit dimensions, including master dimensions. In the properties panel, under Data, select the dimension that you want to edit.

Dimensions have the following properties:

- Field: Start typing the field name to display a list of matching fields to choose from. You can also click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor, where you can create a calculated dimension.
- Label: Enter a name for the dimension.
- Include null values: When this is checked, the visualization will include the null values of the dimension, presented as a gap or a dash, depending on the type of visualization. For example, if you have sales figures but do not have any information about what company the figures belong to, the figures will be added to the measure value for the null value dimension.
- Limitation: You can limit the number of dimension values that are displayed.
- Show others: When you have set a limitation for the number of dimension values displayed, you have an option to summarize the measure values for the remaining dimensions by selecting Show others.
- Master item: Edit a master dimension to update all instances where the dimension is used, or create a new master dimension by adding a dimension to the master items.

### Editing a measure

You can edit measures, including master measures. In the properties panel, under Data, select the measure that you want to edit.

Measures have the following properties:

- Expression: Enter the expression. You can also click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open and use the expression editor. You can also apply a Modifier to automatically adjust the original expression. See [*Applying a measure modifier*](#ApplyModifier).
- Label: Enter a name for the measure. The label is not automatically updated when you make changes in Expression.
- Number formatting: Set the number formatting for the measure values. The options Number and Date offer custom formatting options for defining your own format pattern.
- Master item: Edit a master measure to update all instances where the measure is used, or create a new master measure by adding a measure to the master items.

#### Applying a measure modifier

Using a modifier, a measure expression can be automatically customized for a specific analytical purpose. For example, you might want an expression in which data is presented as an accumulation rather than standalone values.

Do the following:

1. In the properties panel, expand the Data section.
2. Under Measures, expand the measure to which you are applying a modifier.
3. Underneath the Expression, click Modifier.
4. Use the drop down menu to select a modifier.
5. Fill in the parameters specific to the modifier you are using.

When you are finished, click Output expression to view how the original expression was modified.

For more information about measure modifiers, see [*Modifiers*](../Measures/modifiers.htm).

### Editing master items

Dimensions and measures that are linked to a master item are displayed with a ![Linked Object](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) in the properties panel. You can edit the master item to update all instances that use the dimension or measure, or you can unlink the item from its master to edit only the current instance of the dimension or measure.

A visualization that is linked to a master item is indicated by ![Linked Object](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg)Linked visualization on the sheet. You can edit a master visualization to update all instances that use the visualization, or you can unlink a visualization from its master to edit only the current instance of the visualization. Unlinking a visualization does not unlink any master dimensions or master measures used in the visualization.

For more information about editing master items, see [*Editing a master dimension*](../Assets/edit-master-dimension.htm), [*Editing a master measure*](../Assets/edit-master-measure.htm), and [*Editing a master visualization*](../Assets/edit-master-visualization.htm).

For more information about unlinking from master items, see [*Unlinking from a master item*](../Assets/unlinking-from-a-master-item.htm) and [*Unlinking from a master visualization*](unlink-from-master-visualization.htm).

## Deleting dimensions and measures

In the properties panel, you can delete a dimension or measure. Long-touch or right-click the dimension or measure and select Delete in the dialog. Alternatively, click the dimension or measure and click Delete![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg). If you delete an instance of a master item, the master item is still available in the assets panel.

Information noteYou can undo a deletion by clicking ![Undo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_back.svg). Changing which sheet you are viewing will prevent you from undoing your deletion.

## Learn more

- [*Properties panel*](../Sheets/navigating-sheets.htm#Properti)
- [*Deleting a master dimension or master measure*](../Assets/delete-master-dimension-measure.htm)
