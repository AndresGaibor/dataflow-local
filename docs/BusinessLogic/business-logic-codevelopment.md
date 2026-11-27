---
title: "Co-developing business logic in shared spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business-logic-codevelopment.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor"]
---

# Co-developing business logic in shared spaces

You can co-develop application logical models and [vocabulary](#glossary-1 "Glossary term") with other members of a [shared space](#glossary-2 "Glossary term").

By default, only the application owner can develop the [logical model](#glossary-3 "Glossary term") and vocabulary in their application. The Can edit data in applications user role, however, allows other users in the shared space to develop application [load script](#glossary-4 "Glossary term") and [business logic](#glossary-5 "Glossary term") in applications they do not own

As a best practice, coordinate with your co-development team to avoid working on the same sections at the same time, such as Fields & groups or Custom analysis. When changes from two or more users are in conflict, the most recent change takes precedence over other work.

Additionally, changes to Fields & groups can impact users working in other sections of the logical model. If a single [field](#glossary-6 "Glossary term") is changed in Fields & groups, it only impacts other users in Fields & groups. If multiple fields are changed in one action in Fields & groups, it will impact all sections of the logical model.
