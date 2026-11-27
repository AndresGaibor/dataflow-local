---
title: "Reviewing your hierarchies"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/Tutorial/tutorial-configuring-your-hierarchies.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Tutorial – Customizing how Insight Advisor interprets data"]
---

# Reviewing your hierarchies

Next, you will review the hierarchies in your [logical model](#glossary-0 "Glossary term"). Hierarchies is an optional [business logic](#glossary-1 "Glossary term") feature. It defines drill-down relationships between groups.

When you enable business logic, some hierarchies may be automatically created b from your data model. If you navigate to Hierarchies, you can see that business logic has created two hierarchies.

Hierarchies in the logical model

![Default hierarchies in the logical model. There is one for Categories and Products and one for Supplies and Products](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_hierarchies-saas.png "Click to view full size")

Hierarchies indicate groups that can be used to break each other down in analysis. For example, the two hierarchies created by Qlik Sense correctly identify two drill-down relationships in our logical model:

- The data in the Category fields can be broken down into the data in the Products fields.
- The data in the Suppliers fields can be broken down into the data in the Products fields.

If you navigate to Sheet, click Insight Advisor, and select CategoryName, Insight Advisor includes a treemap that breaks down CategoryName by ProductName.

Category and products breakdown

![Insight Advisor results. A breakdown chart for CategoryName and ProductName is selected.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_charts-hierarchy-example-saas.png "Click to view full size")

Tip noteHierarchies do not enable drill-down [selections](#glossary-2 "Glossary term") in the generated [charts](#glossary-3 "Glossary term"). That requires drill-down [dimension](#glossary-4 "Glossary term") [master items](#glossary-5 "Glossary term"). For example, if you want map charts that drill-down from to cities after a country is selected, you need to create a corresponding drill-down dimension master item.
