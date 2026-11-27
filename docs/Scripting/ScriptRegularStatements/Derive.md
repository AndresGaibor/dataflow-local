---
title: "Derive"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Derive.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Derive

The Derive statement is used to generate derived fields based on a field definition created with a Declare statement. You can either specify which data fields to derive fields for, or derive them explicitly or implicitly based on field tags.

Syntax:

Derive [fields]] From [Field[s]] field\_list Using definition

Derive [Field[s]] From Explicit [Tag[s]] tag\_list Using definition

Derive [Field[s]] From Implicit [Tag[s]] Using definition

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| definition | Name of the field definition to use when deriving fields.  Example: Calendar |
| field\_list | A comma separated list of data fields from which the derived fields should be generated, based on the field definition. The data fields should be fields you have already loaded in the script.  Example: OrderDate, ShippingDate |
| tag\_list | A comma separated list of tags. Derived fields will be generated for all data fields with any of the listed tags. The list of tags should be enclosed by round brackets.  Example: ('$date','$timestamp')  [*Field tags*](../field-tags.htm) |

Examples:

- Derive fields for specific data fields.

  In this case we specify the OrderDate and ShippingDate fields.

  DERIVE FIELDS FROM FIELDS OrderDate,ShippingDate USING Calendar;
- Derive fields for all fields with a specific tag.

  In this case we derive fields based on Calendar for all fields with a $date tag.

  DERIVE FIELDS FROM EXPLICIT TAGS ('$date') USING Calendar;
- Derive fields for all fields with the field definition tag.

  In this case we derive fields for all data fields with the same tag as the Calendar field definition, which in this case is $date.

  DERIVE FIELDS FROM IMPLICIT TAG USING Calendar;

[*Derived fields*](../derived-fields.htm) (full example)

## Learn more

- [*Declare*](Declare.htm)
