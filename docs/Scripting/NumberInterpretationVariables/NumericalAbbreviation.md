---
title: "NumericalAbbreviation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/NumericalAbbreviation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---
# NumericalAbbreviation

The numerical abbreviation sets which abbreviation to use for scale prefixes of numerals, for example M for mega or a million (106), and µ for micro (10-6).

Syntax:

NumericalAbbreviation

You set the `NumericalAbbreviation` [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/NumericalAbbreviation.htm#glossary-0 "Glossary term") to a string containing a list of abbreviation definition pairs, delimited by semi colon. Each abbreviation definition pair should contain the scale (the exponent in decimal base) and the abbreviation separated by a colon, for example, `6:M` for a million.

The default setting is `'3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:µ;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y'`.

Examples:

This setting will change the prefix for a thousand to t and the prefix for a billion to B. This would be useful for financial applications where you would expect abbreviations like t$, M$, and B$.

Set NumericalAbbreviation='3:t;6:M;9:B;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:µ;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y';
