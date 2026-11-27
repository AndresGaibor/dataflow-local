---
title: "Linking terms to master items"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/BusinessGlossary/Tutorial/terms-to-master-items.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with business glossaries", "Tutorial - Creating a business glossary"]
---

# Linking terms to master items

Once you have added your terms, you can link them to master dimensions and master measures in your app. This shows app users the term definition when they interact with the master item.

For users creating sheets in the app in edit mode, the definition can be viewed by opening Master items and clicking on the master item. For users using a sheet in analysis mode, the definition can be viewed in Details for visualizations using those master items.

In this tutorial, you will link the term Annual Contact Value to the master measure Annual Contract Value (ACV).

Do the following:

1. Open the app ContractValues.
2. Open a sheet and click Edit sheet.
3. In Assets, click Master items.
4. Under Measures, select Annual Contract Value (ACV).
5. Click ![Edit](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
6. Click OK.
7. Under Glossary terms, click ![Add glossary term link](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg).
8. In the search field, search for Annual Contact Value and select the result.
9. Click Select.
10. Click Save.

Now, when you click on Annual Contract Value (ACV) under Master items, the definition is taken from the glossary term.

Definition in edit mode

![The master measure Annual Contract Value is selected, showing the definition for Annual Contract Value from the term definition in the glossary.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_glossary-tutorial-master-measure-edit.png "Click to view full size")

Click Edit sheet to switch to analysis mode. Now, right-click on a visualization and select ![Show details](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) Show details.

Details in analysis mode

![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_glossary-tutorial-master-measure-details.png "Click to view full size")

Return to the glossary. Select Annual Contact Value. Under Linked resources, Annual Contract Value (ACV) is listed as a linked master measure.

Annual Contract Value definition with linked resource to master measure

![The entry for Annual Contract Value in the glossary, showing the master measure in the app under Linked resources.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_glossary-tutorial-master-measure-linked-resource.png "Click to view full size")
