---
title: "Setting logical model scopefor Insight Advisor with packages"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business-logic-packages.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Building logical models for Insight Advisor with Business logic"]
---

# Setting logical model scopefor Insight Advisor with packages

Packages enable you to define and limit the scope of insights for specific areas of interest in your [logical model](#glossary-0 "Glossary term").

A package is a collection of related groups. [Insight Advisor](#glossary-1 "Glossary term") only uses groups in the same package together when generating results. Groups can belong to multiple packages. Logical model packages are created and managed in Packages.

For example, your data model may contain tables from separate business areas. If there are connections between the tables, a date [field](#glossary-2 "Glossary term") from Sales might be used in an Insight Advisor analysis with a date field from Support. By putting Sales groups and Support groups into separate packages, you could ensure that analysis for those business areas only use fields in the associated package.

The use of packages is optional. If you define no packages, then all fields and groups are considered to be in the same package for analysis.

You can edit or delete packages by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and selecting Edit or Delete.

Information note

Packages is not available when a tenant is licensed for Qlik Answers. For more information, see [*Qlik Answers*](../QlikAnswers/Qlik-Answers.htm).

## Creating packages

Do the following:

1. Click Create package.
2. Enter a package name.
3. Add groups to the package from Available groups

   Information notePackages must include at least one measure group.
4. Click Create.
