---
title: "Creating drill-down analysis with hierarchies in Insight Advisor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business-logic-hierarchies.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Building logical models for Insight Advisor with Business logic"]
---

# Creating drill-down analysis with hierarchies in Insight Advisor

Defining which groups in your [logical model](#glossary-0 "Glossary term") have a hierarchical relationship enables [Insight Advisor](#glossary-1 "Glossary term") to offer breakdown analysis along specified hierarchies and better detect dependencies among groups.

Hierarchies enable drill-down breakdowns in recommendations (such as Sales by Product category, Product sub-category, and Product). Hierarchies also help Insight Advisor avoid mixing geographic items in recommendations. For example, creating hierarchies for Supplier County with Supplier City and for Customer Country and Customer City prevents them from being used in erroneous combinations such as Supplier Country and Customer City.

Hierarchies are also used in [associative insights](#glossary-2 "Glossary term") to detect dependencies when making [selections](#glossary-3 "Glossary term"). For example, selecting Sweden in an Insight Advisor analysis and then having only Swedish city values be selected in another [chart](#glossary-4 "Glossary term") that uses the City [field](#glossary-5 "Glossary term").

There two kinds of logical model hierarchies: learned and defined. Learned hierarchies are detected from how fields are linked and used in the data model. For example, the logical model may see the hierarchical link between a city field and a country field and treat them as having a hierarchy. Defined hierarchies are user-created. Defined hierarchies are created and managed in Hierarchies. Hierarchies are optional for business logic.

You can edit or delete defined hierarchies by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and selecting Edit or Delete.

Information noteYou cannot view or modify learned hierarchies in Hierarchies.

Information note

Hierarchies is not available when a tenant is licensed for Qlik Answers. For more information, see [*Qlik Answers*](../QlikAnswers/Qlik-Answers.htm).

## Creating hierarchies

Do the following:

1. Click Create hierarchy
2. Enter a hierarchy name.
3. Add groups to the hierarchy in order from lowest level in the hierarchy to the highest level of the hierarchy.
4. Click Create.
