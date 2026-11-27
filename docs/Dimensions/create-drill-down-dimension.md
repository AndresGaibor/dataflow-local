---
title: "Creating a drill-down dimension"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Dimensions/create-drill-down-dimension.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Reusing dimensions with master dimensions"]
---

# Creating a drill-down dimension

When adding a [dimension](#glossary-0 "Glossary term"), you can select between creating a single or a drill-down dimension.

The following description explains how to create a drill-down group from the Create new dimensions dialog.

Information note

If selections cause the current drill-down dimension field to have only one possible value, the next field in the list is used instead.

Do the following:

1. Select Drill-down as dimension type.
2. Click at least two fields from the fields list on the left-hand side to insert them as the referenced fields.

   Tip noteYou can filter which table to select fields from in the drop-down list.

   Tip noteYou can rearrange the order of the fields you have selected by dragging them to new positions in the list of selected fields.
3. Optionally, add labels for the fields added to your drill-down dimension.

   Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) in Label to add an expression for the label. The expression must start with =.
4. Type a name for the dimension.
5. Type a description for the dimension (optional).

   If you do not add a description and then link a glossary term to your master item as a definition, the term definition will be used in the description.
6. If you want to specify a color, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_triangle_bottom.svg) in the color drop down and select a color through one of the following methods:

   - Click one of the colors in the palette.
   - Type a 6 character color code in the Hex input field: #.
   - Click ![Show options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) at the bottom of the dialog, select a color in the color wheel, and optionally adjust the saturation slider.
7. Add tags (optional).
8. Optionally, if you have access to a glossary, link the dimension to a glossary term.

   [*Linking terms to master items*](../Catalog/BusinessGlossary/business-glossaries-master-items.htm)
9. If a custom [logical model](#glossary-1 "Glossary term") is activated for the application, optionally select the Logical model group to which the master dimension will be added. If you do not select a group, the master dimension is ungrouped and therefore cannot be used in Insight Advisor interactions by any user. You can later select or change the group when editing the master dimension, or by editing the logical model of the application.

   [*Defining fields and groups in Insight Advisor*](../BusinessLogic/business-logic-fields-groups.htm)
10. Click Create.
11. Click Close.

The drill-down dimension is now saved in the Dimensions category among the master items.

When you click the dimension in the panel on the left-hand side, the preview displays the dimension type and which fields are included in the drill-down dimension.

The preview displays the dimension type and which fields are included in the drill-down dimension.

![Dimension preview.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DrillDownDimPreview_rev.png "Click to view full size")
