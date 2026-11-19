---
title: "BrokenWeeks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/BrokenWeeks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---
# BrokenWeeks

This setting defines if weeks are broken or not.

Syntax:

BrokenWeeks

 In Qlik Sense, the regional settings are fetched when the application is created, and the corresponding settings are stored in the script as environment [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/BrokenWeeks.htm#glossary-1 "Glossary term").

A North American application developer often gets `Set BrokenWeeks=1;` in the script, corresponding to broken weeks. A European application developer often gets `Set BrokenWeeks=0;` in the script, corresponding to unbroken weeks.

Unbroken weeks means that:

- In some years, week 1 starts in December, and in other years, the last week of previous year continues into January.
- According to ISO 8601, week 1 always has at least 4 days in January. In Qlik Sense, this can be configured using the `ReferenceDay` variable.

Broken weeks means that:

- The last week of the year never continues into January.
- Week 1 starts on January 1 and is, in most cases, not a full week.

The following values can be used:

- 0 (=use unbroken weeks)
- 1 (= use broken weeks)

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

Examples:

If you want ISO settings for weeks and week numbers, make sure to have the following in the script:

Set FirstWeekDay=0;
Set BrokenWeeks=0; //(use unbroken weeks)
Set ReferenceDay=4;

If you want US settings, make sure to have the following in the script:

Set FirstWeekDay=6;
Set BrokenWeeks=1; //(use broken weeks)
Set ReferenceDay=1;
