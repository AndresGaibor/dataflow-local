---
title: "Enabling a custom logical model"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/Tutorial/tutorial-enabling-logical-model.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Tutorial – Customizing how Insight Advisor interprets data"]
---

# Enabling a custom logical model

The first step to customizing how [Insight Advisor](#glossary-0 "Glossary term") interprets your data is enabling the [business logic](#glossary-1 "Glossary term") [logical model](#glossary-2 "Glossary term").

Once enabled, Qlik Sense creates a logical model for business logic based on your data model. You can then start customizing this logical model.

Tip noteYou can toggle the logical model on and off by clicking Disable logic/Enable logic. This is useful when you want to compare results with the model applied to results without the model applied.

Do the following:

1. In the tutorial app, open the app navigation menu.
2. Under Business logic, select Logical model.
3. Click Continue.

## Results

Business logic analyzes your data model and automatically creates groups, hierarchies, and behaviors. Overview provides a look at your new logical model.

The new logical model in Overview

![The overview section of business logic with the initial settings displayed. In fields and master items, 29 are visible and 14 are hidden. 9 groups have been created. 2 hierarchies have been defined. 3 calendar periods have been defined.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_logical-model-saas.png "Click to view full size")

Qlik Sense has hidden 15 fields from analysis, so they are no longer available in Insight Advisor. 10 groups have been created from the data model, associating related fields together. 2 hierarchies have been defined, linking groups for drill-down analysis. 3 calendar periods have been defined, providing periods of time for use in analyses.

Next, you will edit this default logical model, starting by modifying the default fields and groups.
